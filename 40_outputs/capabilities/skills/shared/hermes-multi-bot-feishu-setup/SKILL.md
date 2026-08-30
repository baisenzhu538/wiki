---
name: hermes-multi-bot-feishu-setup
description: Hermes 多 bot 飞书独立配置 — 每个 bot 独立飞书 app + 独立 LLM API
version: 1.0
tags: [hermes, multi-agent, feishu, profile, websocket]
---

# Hermes 多 Bot 飞书独立配置指南

## Purpose

Hermes 多 bot 飞书接入与排障的完整操作手册：从零配置独立 profile（独立飞书 app + 独立 LLM API），到常见故障（SSL 断连、429/402 欠费假象、bot 变慢）的根因定位与修复。覆盖配置、验证、运维三条线。

## When to Use

- 新建/迁移五绝或其他 bot 的飞书 gateway 时
- 飞书 bot 报 SSL 错误、连接失败、401/402/429 时
- 飞书 bot 干活明显变慢（秒回变 8-9 分钟）时
- 切换 bot 的 LLM 模型/provider（如 DeepSeek ↔ 智谱）时
- 排查 bot 实际运行模型与 config.yaml 期望不一致时

## When NOT to Use

- 单 bot 单平台、无多 profile 需求的场景（用官方 hermes setup 即可）
- 非飞书平台（Telegram/Discord/微信）的接入问题
- 业务内容质量问题（那是 KDO 卡片生产流程的事，不是基础设施）

## Protocol

### P1 配置（新 bot / 迁移）

1. `hermes profile create <name> --clone-from default --no-alias`
2. 配置 `.env`：FEISHU_APP_ID/SECRET/DOMAIN/CONNECTION_MODE + GATEWAY_ALLOW_ALL_USERS + LLM key
3. 配置 `config.yaml`：`model.default/provider/base_url` + `platforms: ['cli', 'feishu']`
4. 清理 auth.json credential_pool 残留
5. 启动 gateway：`hermes -p <name> gateway run`

### P2 验证（改配置后必做）

1. 重启 NSSM 服务：`sc stop/start hermes-gateway-<profile>`
2. 看 `logs/nssm-stdout.log` 启动横幅确认实际 Provider/Model/Endpoint
3. `hermes -p <profile> chat -q "回复OK" -Q -v` 看 `API call #1` 的 latency 与 cache 命中率
4. 飞书真实消息看 `logs/gateway.log` 的 `response ready: time=Xs`

### P3 排障（按症状路由）

- SSL 断连 → 关代理 TUN/系统代理，飞书域名加直连
- 429「余额不足」但 code plan 有额度 → 检查三处 base_url（见下）
- bot 变慢 → 查会话膨胀 + hygiene 压缩（见下）

## 核心概念

每个 bot（洪七公/段王爷等）是独立的 Hermes profile，有自己独立的：
- 飞书 Bot（独立 App ID + Secret）
- LLM API（独立 API Key）
- 工作区、记忆、技能

所有 bot 通过 Hub（WebSocket :8765）协调，Hub 是共享的。

## 标准配置步骤

### 1. 创建 profile

```bash
hermes profile create <profile_name> --clone-from default --no-alias
```

### 2. 配置 .env（关键！）

每个 profile 需要完整配置，不能继承主 bot 的：

```env
FEISHU_APP_ID=cli_xxx          # 该 bot 独立的飞书 app
FEISHU_APP_SECRET=xxx
FEISHU_DOMAIN=feishu
FEISHU_CONNECTION_MODE=websocket
GATEWAY_ALLOW_ALL_USERS=true

# ⚠️ Kimi/Moonshot API 必须用 KIMI_API_KEY，不是 OPENAI_API_KEY！
KIMI_API_KEY=sk-kimi-xxx
HERMES_MAX_ITERATIONS=90
```

**Kimi API 关键**：Hermes 识别 Kimi/Moonshot 用 `KIMI_API_KEY` 环境变量，不是 `OPENAI_API_KEY`。用错变量名会导致 "Provider 'kimi-coding' is set but no API key was found" 错误。

### 3. 配置 config.yaml（坑点！）

profile 的 `config.yaml` 必须包含：

```yaml
model:
  default: moonshot-v1-8k
  provider: kimi-coding
  base_url: https://api.kimi.moonshot.cn

platforms:
  - cli
  - feishu        # 必须有！否则飞书连接会走 open.feishu.cn 而不是 msg-frontier.feishu.cn
```

**关键 bug**：`platforms` 为空数组 `[]` 时，飞书 WebSocket 会连接到 `open.feishu.cn` 而非 `msg-frontier.feishu.cn`，导致 SSL 错误且无法收发消息。必须加上 `['cli', 'feishu']`。

### 4. 配置 SOUL.md（可选）

定义 bot 的人设和职责。

### 5. 清理 auth.json

如果之前有残留的无效 credentials，清理 credential_pool：

```json
{
  "version": 1,
  "providers": {},
  "credential_pool": {}
}
```

### 6. 启动 gateway

```bash
hermes -p <profile_name> gateway run
```

或后台运行：

```bash
nohup hermes -p <profile_name> gateway run > ~/.hermes/profiles/<profile_name>/logs/gateway.log 2>&1 &
```

## 故障排查

### 症状：飞书 bot 干活非常慢（响应从几秒变 8-9 分钟）

**典型日志**：
```
📦 Preflight compression: ~500,868 tokens >= 500,000 threshold
⚠️  Session compressed 2 times — accuracy may degrade
Session hygiene: 433 messages, ~131,550 tokens (actual) — auto-compressing
Session hygiene compression for session xxx still streaming after 240s (last progress 0.0s ago) — extending wait (ceiling 600s)
```

**根因链（按排查顺序）**：
1. **会话膨胀**：飞书 DM 会话长期累积（几周），state.db 里 `input_tokens` 可能到 100 万+。查：`python -c "import sqlite3; ...SELECT id, message_count, input_tokens FROM sessions WHERE session_key LIKE '%feishu%'"`
2. **hygiene 压缩卡死**：`compression.hygiene_hard_message_limit`（默认 400，消息数超线就强制压缩）触发压缩，但压缩要消化整个巨型历史，LLM 一次处理不完 → 压缩任务永远 streaming，gateway 干等 600s。**这是"慢得像蜗牛"的直接机制**（8/28 就有 420s 记录，与切换模型无关）
3. **cron job deliver=feishu 喂大会话**：定时 job 每 30 分钟往飞书会话发内容，会话永不 idle → 永不自动重置 → 无限膨胀
4. **智谱缓存未预热**（如果刚切模型）：命中率 12% → 87% → 100% 爬升，越用越快

**修复**：
1. **重置膨胀会话（必须从 DB 终结，只删 sessions.json 会被 gateway 恢复逻辑挂回去）**：
   ```bash
   cd <profile_dir> && python -c "
   import sqlite3, time
   conn = sqlite3.connect('state.db')
   conn.execute(\"UPDATE sessions SET end_reason='session_reset', archived=1, ended_at=? WHERE id='<session_id>'\", (time.time(),))
   conn.commit()
   # 再删 sessions.json 里对应映射
   "
   ```
   然后重启 gateway。重启后确认日志出现 `pruning stale sessions.json entry` 才算干净。
2. **调大 hygiene_hard_message_limit**：400 条对高频飞书 agent 太激进 → `compression.hygiene_hard_message_limit: 2000`
3. **cron deliver 改 local**：编辑 `<profile>/cron/jobs.json`，`deliver: feishu` → `deliver: local`（改完重启 gateway 让调度器加载）
4. **验证**：`hermes -p <profile> chat -q "回复OK" -Q -v` 看 `API call #1` 的 latency 和 cache 命中率（应 <5s、>90%）；真实飞书消息看 gateway.log 的 `response ready: time=Xs`

**判断模型本身快慢的正确方法**：不要只看"感觉"，直接 API 基准（urllib 打 chat/completions，测 total + streaming TTFT）。智谱 coding glm-5.3-flash 与 DeepSeek v4-flash 原始速度几乎一样（差 0.2~0.4s），巨大差异几乎都是上下文/缓存/压缩问题。

### 症状：智谱 GLM 报 429「余额不足或无可用资源包」但实际 code plan 有额度

**根因**：code plan 的额度**只认 coding 专用端点**，普通 paas 端点报 429。且 base_url 要在**三处一致**，漏一处就会被覆盖：
1. `config.yaml` → `model.base_url: https://open.bigmodel.cn/api/coding/paas/v4/`（provider: zai）
2. `.env` → `GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4`（环境变量优先于 config！）
3. `auth.json` → credential_pool 里 zai 条目的 `base_url`（credential pool 也可能覆盖 config）

**验证**（不猜，直接打 API）：
```python
# https://open.bigmodel.cn/api/coding/paas/v4/chat/completions + Bearer GLM_API_KEY + glm-5.3-flash → 200
# https://open.bigmodel.cn/api/paas/v4/chat/completions → 429 余额不足（正常，别被骗）
```

**改完重启 gateway**，用 `hermes -p <profile> chat -q "x" -v` 看日志里 `base_url=` 确认是 coding 端点。

### 症状：飞书连接成功（✓ feishu connected）但 Lark SSL 错误

看日志：
```
ERROR Lark: connect failed, err: open.feishu.cn
```

**原因**：`config.yaml` 里 `platforms` 为空

**解决**：在 `config.yaml` 加上 `platforms: ['cli', 'feishu']`，然后重启 gateway

### 症状：401 credential pool exhausted

**原因**：auth.json 里有旧的无效 API key 残留

**解决**：清空 `credential_pool: {}` 在 auth.json 里

### 症状：unknown provider 'kimi-for-coding'

**原因**：`config.yaml` 里把 model 名当成了 provider 名

**错误配置**：
```yaml
model:
  default: kimi-for-coding
  provider: kimi-for-coding    # ❌ 错误
```

**正确配置**：
```yaml
model:
  default: kimi-for-coding     # ✅ 模型名
  provider: kimi-coding        # ✅ provider 名
  base_url: https://api.kimi.com/coding/v1
```

### 症状：WSL 环境下飞书反复断连（SSL 错误 / keepalive timeout）

**典型日志**：
```
ERROR Lark: connect failed, err: SSLEOFError(8, 'UNEXPECTED_EOF_WHILE_READING')
ERROR Lark: receive message loop exit, err: keepalive ping timeout; no close frame received
```

**根因**：Windows 代理工具（Clash/V2Ray/SSR）在网卡层或系统层拦截了 SSL/TLS 流量。常见三层干扰：
1. **TUN 模式** — 虚拟网卡全局拦截，规则模式也绕不过
2. **系统代理** — Windows 系统设置里的代理服务器，影响所有 HTTP 客户端
3. **证书替换/MITM** — 代理工具解密 HTTPS 后重新加密，Python 不信任其自签名证书

**关键诊断：Windows Python 对照实验**

在 WSL 里无法确定是 WSL 网络问题还是代理问题，用 **Windows 本地 Python** 做对照：

```powershell
# Windows PowerShell 执行
C:\Users\<User>\.workbuddy\binaries\python\versions\<version>\python.exe -m pip install requests
```

- ❌ 如果 **Windows Python 也报 `SSLError(SSLEOFError)`** → **代理工具本身在全局干扰 SSL**，不是 WSL 问题。迁到 Windows 也解决不了。
- ✅ 如果 Windows Python 正常 → 问题确实在 WSL 网络层，考虑迁 bot 到 Windows

**诊断步骤**：
1. `env | grep -i proxy` — WSL 内通常没有显式代理变量，但不代表没被拦截
2. 检查 Windows 代理工具：**TUN 模式** + **系统代理** 两个开关都要关
3. 检查代理工具的 DNS 劫持设置（fake-ip 模式会干扰所有域名解析）
4. 检查 Windows 系统代理设置：设置 → 网络和 Internet → 代理 → 关闭"使用代理服务器"
5. 检查日志中 SSL 错误是否集中在 `open.feishu.cn`、`msg-frontier.feishu.cn`、`pypi.org`

**解决**：
1. **关闭 TUN 模式**（Clash/V2Ray 客户端里）
2. **关闭系统代理**（Windows 设置 + 代理工具里的系统代理开关）
3. 代理改为「规则模式」，将以下域名加入直连/绕过列表：
   ```
   *.feishu.cn
   *.larksuite.com
   pypi.org
   files.pythonhosted.org
   ```
4. 如果代理工具安装了根证书用于 MITM，在「不拦截」列表中加入上述域名
5. 重启 bot gateway

**⚠️ 重要发现**：WSL 与 Windows 共享网络内核栈，但 **Windows 本地进程不受 WSL 网络影响**。如果 Windows Python 也 SSL 失败，说明代理工具在 Windows 系统层做了全局拦截，这是必须先在 Windows 侧修复的问题。

**验证修复**：
```bash
# WSL 侧：看进程和连接
ps aux | grep "<profile_name> gateway" | grep -v grep
lsof -i -a -p <PID> | grep ESTABLISHED

# 看日志是否还有 SSL/timeout 错误
grep -E "connect failed|disconnected|timeout" ~/.hermes/profiles/<profile_name>/logs/gateway.log
```

## 进阶：Bot 跨平台迁移（WSL ↔ Windows）

当 WSL 网络问题无法根除时，可能需要将某些 bot（如段智兴）迁到 Windows 本地运行。

### 迁移前判断

**先做 Windows Python 对照实验** （见上方 SSL 故障排查）：
- 如果 Windows Python 也 SSL 失败 → **不要迁**，先修代理
- 如果 Windows Python 正常 → 可以迁

### 迁移步骤

**从 WSL 复制到 Windows**：

```powershell
# 在 Windows PowerShell 执行
$HermesHome = "C:\Users\$env:USERNAME\.hermes"
$ProfileName = "duanwangye"

# 创建目录
New-Item -ItemType Directory -Force -Path "$HermesHome\profiles\$ProfileName\skills"
New-Item -ItemType Directory -Force -Path "$HermesHome\profiles\$ProfileName\logs"
```

**必须复制的文件**：
| 文件 | 说明 |
|------|------|
| `auth.json` | 飞书凭证 + API key |
| `config.yaml` | 配置（需要修改 provider 和路径） |
| `SOUL.md` | 人格设定 |
| `.env` | 环境变量 |
| `state.db` + `state.db-shm` + `state.db-wal` | Hermes 状态数据库 |
| `skills/` | 技能目录 |

**配置文件必须修改的项**：
1. **provider 名称**：`kimi-for-coding` → `kimi-coding`（model 名 vs provider 名不同）
2. **路径**：
   - `prefill_messages_file: /home/...` → `C:\Users\...\SOUL.md`
   - `cwd: /mnt/c/...` → `C:\Users\...`
3. **skills 路径**：改为 Windows 格式

### 常见坑：Windows Hermes venv 损坏

**现象**：启动时报 `No Python at 'C:\Users\...\python.exe'`

**原因**：Windows 版 Hermes 的 venv 是用某个 Python 版本（如 3.11.9）创建的，`pyvenv.cfg` 里记录了该版本路径。当这个 Python 被删除/更新后，venv 里的 `python.exe` 只是一个 launcher，找不到真正的解释器。

**检查**：
```powershell
Get-Content "C:\Users\...\hermes-agent\venv\pyvenv.cfg"
# 如果 home = 指向不存在的路径，就是这个问题
```

**解决**：用现有 Python 重建 venv（需要在 Windows 侧执行）：
```powershell
$Py = "C:\Users\...\.workbuddy\binaries\python\versions\3.13.12\python.exe"
$Venv = "C:\Users\...\AppData\Local\hermes\hermes-agent\venv"
& $Py -m venv $Venv --upgrade
```

### 跨平台调试工具

| 检查项 | WSL 命令 | Windows 对照 |
|--------|----------|--------------|
| 进程是否在跑 | `ps aux \| grep hermes` | PowerShell: `Get-Process python` |
| 网络连接 | `lsof -i -a -p <PID>` | PowerShell: `Get-NetTCPConnection` |
| 最新日志 | `tail logs/gateway.log` | `Get-Content logs\gateway.log -Tail 20` |
| SSL/代理问题 | `curl -v https://api.kimi.com` | PowerShell: `python -m pip install requests` |

### 什么时候迁、什么时候不迁

| Bot 类型 | 建议 | 原因 |
|----------|--------|------|
| 纯飞书网关（段智兴） | 可迁 Windows | 工具链简单，网络敏感度高 |
| 多模态渲染（洪七公） | 留 WSL | 依赖 HyperFrames/ffmpeg/Chrome/Linux 工具链 |
| 内容生产（黄药师） | 留 WSL | KDO + Obsidian 路径一致性 |
| 协调中枢（周伯通） | 留 WSL | 工具链多，跡象少 |

