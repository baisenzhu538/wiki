# 通道-模型认知表（channel-model-map）

> **为什么要有这张表**：09-05 夜→09-06 晨 kimi 403 周额度 + codex relay 余额尽两墙连撞，值守「报通道名」时没人知道通道背后真实是哪家供应商、哪个模型——欧阳锋晨问「glm-5.3-flash 怎么会没额度」暴露认知盲区（#656 立项起因）。
> **纪律**：①值守报通道**必须同时报真实供应商+模型**（本表 3 列连报）；②配置漂移随发随更（下面每行附核对命令）；③key 一律只记**指纹**不记明文。
> **指纹约定**：`sha256(key)[:8] + '…' + key[-4:]`。本表两条 key 均按此约定核验吻合（sha256 前缀+尾 4 位与王语嫣台账一致）【实证：黄药师 09-06 本机重算】。
> **机器可读面**：`90_control/scripts/channel_health.py` 的 `TOOL_UPSTREAM`（fallback 按上游去重就靠它）。

## 一、通道→真实供应商总表（09-06 核验版）

| CLI/通道名 | 真实供应商（上游） | 模型 | 端点（来源） | key 归属/指纹 | 健康探针 | 09-06 状态 |
|:--|:--|:--|:--|:--|:--|:--|
| `claude.exe` | **智谱 GLM**（**不是** Anthropic） | `glm-5.3-flash` | `https://open.bigmodel.cn/api/anthropic`（`~/.claude/settings.json` → env.ANTHROPIC_BASE_URL） | settings.json 单一 token，**全厂唯一无覆盖**（王语嫣核实）；指纹 `1cdfd9b3…uOra` | HTTP POST `/v1/messages` max_tokens=1（正 key 200/1.2s，坏 key 401/0.1s 实测） | 🟢 全夜存活（09-05 夜扛下全部产出） |
| `codex.exe` | **DeepSeek**（经本地 relay，**relay 不是 GLM、上游不是智谱**） | `deepseek-v4-pro` | `http://127.0.0.1:4444/v1`（`~/.codex/config.toml` model_providers.relay.base_url）→ 上游 `https://api.deepseek.com/v1` | 上游 deepseek key 在 relay 进程命令行 `--api-key`，指纹 `1511248f…b2f0`；relay 本地调用方 token=`~/.codex/auth.json`（`ccx-prox…2026`，**relay 不校验它**） | HTTP POST `/v1/responses` max_output_tokens=16（200/0.9s 实测）；余额尽=上游 402/Insufficient Balance | 🟢 已充值复活（王语嫣 12:10 `/v1/responses` 100 tokens 实测；黄药师 11:58 探针 200 互证） |
| `kimi.exe` | **Kimi（月之暗面）** | 别名 `kimi-code/k3` → 实际 **`kimi-for-coding`** | `https://api.kimi.com/coding/v1`（`~/.kimi-code/config.toml` providers.managed:kimi-code） | OAuth 文件态 `~/.kimi-code/credentials/kimi-code.json`（access_token 15min 一换，**CLI 自刷**——外部 HTTP 探针会撞过期 401 假阴性，已实测） | CLI 级：`kimi.exe -m kimi-code/k3 -p 最小prompt`（403 时 2.7s 快败） | 🔴 403 周额度（7 天窗，23:37 起） |
| `hermes.exe` | **Kimi（月之暗面）——与 kimi 同上游** | `kimi-for-coding` | `https://api.kimi.com/coding/v1`（`~/.hermes/config.yaml`：provider kimi-coding） | 各 profile `auth.json`（存放粒度未逐一核实【推断】） | **无独立探针**：上游=kimi，按 kimi 探测结果判定（fallback 按上游去重，不撞二遍墙） | 🔴 随 kimi 连坐（同上游同额度墙） |

### 关键结论（#656 待核实项闭环）

1. **relay ≠ GLM，与 claude.exe 不同账号不同供应商**【实证】：relay 进程命令行 `codex-relay --port 4444 --upstream "https://api.deepseek.com/v1" --api-key "sk-…b2f0"`（PID 161248，09-06 netstat+wmic 实取）；claude.exe 上游=`open.bigmodel.cn`。两墙是**两堵独立的墙**——deepseek 余额尽不连坐 GLM，kimi 周额度不连坐 deepseek。
2. **kimi 与 hermes 是同一堵墙**【实证】：两者上游同为 `api.kimi.com/coding/v1`。kimi 403 周额度时 hermes 同死——**fallback 链里 hermes 形同虚设**（kimi 健康时轮不到它，kimi 死时它也死），仅 `--tool hermes` 显式指定时使用。
3. **relay 会吞掉调用方 key**【实证】：对 relay 打坏 Bearer 仍 200（它只认自己 `--api-key`）——codex 通道的「坏 key 模拟」只能模拟上游 key 死，测试用 `--force-dead` 钩子代替。

## 二、fallback 链（#656 落地，`kimi-headless-launch.py`）

```
FALLBACK_ORDER = claude(GLM) → codex(deepseek) → kimi → hermes(随kimi连坐)
角色主通道：huangyaoshi=kimi / laowantong=kimi / ouyangfeng=codex（ROLE_TOOL）
规则：launch 前逐通道最小探针 → 首个健康通道拉起；主通道死→自动切（todos+stdout 通知）；
     全死→不硬派 exit 2 报王语嫣；同上游去重（一堵墙只撞一次）。
应急：--no-probe 跳过预检硬拉；--force-dead kimi,claude 模拟死通道（测试钩）。
台账：logs/channel-health.log（append-only JSONL，每次决策一行）。
```

顺序依据：claude(GLM) 09-05 夜全通道连死时唯一全夜存活→最优先；codex(deepseek) 充值复活次之；kimi/hermes 同墙排最后。

## 三、核对命令（配置漂移自查）

```bash
# claude.exe 真上游+模型（对照本表第 1 行）
python -c "import json,io;d=json.load(io.open(r'C:/Users/Administrator/.claude/settings.json',encoding='utf-8'))['env'];print(d['ANTHROPIC_BASE_URL'],d['ANTHROPIC_MODEL'])"
# codex relay 真上游+模型（对照第 2 行）
grep -E "^(model|base_url)" C:/Users/Administrator/.codex/config.toml
netstat -ano | grep ":4444.*LISTEN"   # 再用 PID 查进程命令行里的 --upstream
# kimi 真模型（对照第 3 行）
grep -A3 "managed:kimi-code" C:/Users/Administrator/.kimi-code/config.toml
# hermes 真上游（对照第 4 行）
cat C:/Users/Administrator/.hermes/config.yaml
# 手动全量预检
python -c "import sys;sys.path.insert(0,'90_control/scripts');import channel_health as c;[print(r) for r in c.probe_chain(['claude','codex','kimi','hermes'])]"
```

## 四、维护记录

| 日期 | 事件 |
|:--|:--|
| 2026-09-06 | 建表（#656）。四行全部本机实证核验（配置文件+进程命令行+实弹探针）；kimi 403 周额度、deepseek 充值复活为当日实测口径 |
