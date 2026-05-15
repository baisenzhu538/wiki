---
title: Hermes Gateway Revival Skill
type: capability
subtype: skill
status: ready
target_user: 黄药师（Builder）— 修复五绝中 Hermes 系 bot 离线/认证失败问题
delivery_channel: local
source_refs: [laowantong/hermes-gateway-troubleshooting-20260516.md]
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
artifact_id: hermes-gateway-revival-v1
created_at: 2026-05-16
updated_at: 2026-05-16
origin: builtin
---

# Hermes Gateway Revival Skill

## Capability Type

skill

## Mission

诊断并修复 Hermes Gateway 管辖的三个 bot（老顽童/洪七公/段王爷）离线或无响应问题。
最常见根因是 API Key 认证失败（HTTP 401），修复涉及 **3 层同步更新**——只改一处必然复发。

## Target User

黄药师（Builder）。此 skill 不需要 欧阳锋 参与。

## 背景：五绝架构

| Bot | Hermes Profile | systemd Service |
|-----|---------------|-----------------|
| 老顽童（周伯通） | `laowantong` | `hermes-gateway-laowantong.service` |
| 洪七公（北丐） | `beikai` | `hermes-gateway-beikai.service` |
| 段王爷 | `duanwangye` | `hermes-gateway-duanwangye.service` |

三个 bot 都通过飞书 WebSocket 接收消息，调用 Kimi API（`kimi-coding` provider）生成回复。

## Inputs

- 用户报告：bot 没反应 / 不回复飞书消息
- 可选：新的 API Key（如果旧 Key 已过期）

## Outputs

- 诊断报告（哪个病灶导致离线）
- 修复后的服务状态确认（三个全部 `active (running)`）
- 日志验证（无 401 / auth error）

## 关键认知：3 层病灶必须同步修复

**只改一处必然被另一处覆盖。** 这是历史上多轮修复失败的根本原因。

| 层 | 路径 | 作用 | 典型错误 |
|---|------|------|---------|
| ① 全局 .env | `~/.hermes/.env` | Hermes 启动时 `load_dotenv` 加载 | **只改了 profile .env，全局未改** |
| ② auth.json 缓存 | `~/.hermes/auth.json` | credential_pool 缓存 Key + 状态 | **旧 Key 的 access_token 未更新；last_status=exhausted 未清除 → Hermes 认为 Key 已死直接跳过** |
| ③ config.yaml | `~/.hermes/profiles/<name>/config.yaml` | provider 名映射 | `kimi-for-coding` → 应为 `kimi-coding` |

## Tool Permissions

| Tool | Allowed operations | Requires approval |
| --- | --- | --- |
| `systemctl --user status/restart` | 查看/重启 Hermes 服务 | No |
| `journalctl --user -u` | 查看服务日志 | No |
| Read `~/.hermes/.env` | 读全局环境变量 | No |
| Read `~/.hermes/auth.json` | 读认证缓存 | No |
| Write `~/.hermes/.env` | 更新 API Key | No |
| Write `~/.hermes/auth.json` | 清除 credential_pool 过期状态 | No |
| Read/Write `~/.hermes/profiles/*/config.yaml` | 修 provider 名 | No |

## Procedure

### Phase 1 — 诊断

```
# 1. 检查服务状态
systemctl --user status hermes-gateway-laowantong hermes-gateway-beikai hermes-gateway-duanwangye --no-pager

# 2. 查找认证错误
journalctl --user -u hermes-gateway-laowantong.service --no-pager -n 50 | grep -iE "401|auth|kimi.*fail|error.*api"
journalctl --user -u hermes-gateway-beikai.service --no-pager -n 50 | grep -iE "401|auth|kimi.*fail|error.*api"
journalctl --user -u hermes-gateway-duanwangye.service --no-pager -n 50 | grep -iE "401|auth|kimi.*fail|error.*api"
```

**诊断决策树**：

| 日志信号 | 病灶 | 动作 |
|---------|------|------|
| `HTTP 401: The API Key appears to be invalid` | Key 过期或被拒绝 | Phase 2 全流程 |
| `Provider: kimi-for-coding` | provider 名错误 | Phase 2 步骤 ③ |
| 无日志 / 服务 inactive | 服务挂了 | `systemctl --user restart` |
| 服务 running 但飞书没反应 + 无 API 错误 | Feishu WebSocket 断连 | 重启服务，检查飞书 app 凭证 |

### Phase 2 — 修复（3 层同步）

拿到新 Key 后，**必须三步都做**：

#### ① 更新全局 .env

```bash
sed -i 's/^KIMI_API_KEY=.*/KIMI_API_KEY=<新Key>/' ~/.hermes/.env
grep KIMI ~/.hermes/.env  # 验证
```

> 注意：是 `~/.hermes/.env`，不是 `~/.hermes/profiles/xxx/.env`！

#### ② 清除 auth.json 缓存

```bash
python3 -c "
import json
with open('$HOME/.hermes/auth.json') as f:
    auth = json.load(f)
for cred in auth.get('credential_pool', {}).get('kimi-coding', []):
    cred['access_token'] = '<新Key>'
    cred['last_status'] = None
    cred['last_error_code'] = None
    cred['last_error_message'] = None
    cred['last_error_reason'] = None
    cred['last_error_reset_at'] = None
with open('$HOME/.hermes/auth.json', 'w') as f:
    json.dump(auth, f, indent=2)
print('Done')
"
```

#### ③ 确认 provider 名

```bash
grep "default:" ~/.hermes/profiles/{laowantong,beikai,duanwangye}/config.yaml
# 应为 kimi-coding（不是 kimi-for-coding）
```

### Phase 3 — 重启 & 验证

```bash
# 重启
systemctl --user restart hermes-gateway-laowantong hermes-gateway-beikai hermes-gateway-duanwangye

# 等 3 秒后验证
sleep 3
systemctl --user status hermes-gateway-laowantong hermes-gateway-beikai hermes-gateway-duanwangye --no-pager

# 确认无 401
journalctl --user -u hermes-gateway-laowantong.service --no-pager -n 20 | grep -iE "401|error.*auth|kimi.*fail"
```

**验证标准**：
- 三个服务全部 `active (running)`
- 日志中无 `HTTP 401` 或 `invalid_authentication_error`
- 飞书上发消息给 bot → 收到回复

## 失败处理

| 症状 | 可能原因 | 对策 |
|------|---------|------|
| 修复后仍然 401 | Key 本身无效/过期 | 去 Kimi 后台确认 Key 状态，生成新 Key 后重走 Phase 2 |
| 修复后仍 401 + Key 确认有效 | auth.json 被 Hermes 重新写回旧值 | 检查是否有其他 Hermes 进程在运行（`ps aux | grep hermes`），全部停掉后再改 auth.json |
| Bot 回复了但内容错乱 | model 名不对 | 检查 config.yaml 中 `model.default` 值 |
| `Failed to load prefill messages from SOUL.md` | SOUL.md 为空或格式错误 | 非致命警告，bot 仍可正常工作。如需修复：在 profile 目录创建合法 JSON 的 SOUL.md |

## 不要做的（禁止清单）

- ❌ 不要只改 profile `.env` 不改全局 `.env` → 无效
- ❌ 不要只改 `.env` 不清 `auth.json` → 缓存覆盖
- ❌ 不要 `systemctl --user daemon-reload`（不需要，改了 .env 不需要 reload systemd）
- ❌ 不要在 Windows 侧用 PowerShell 写 WSL 文件 → 编码问题可能导致 Key 损坏
- ❌ 不要 `git` 追踪任何含 API Key 的文件

## 关联

- 踩坑记录：`20_memory/pitfalls.md` § P-4
- 五绝状态：`laowantong/five-heroes-status.md`
- 历史排障记录：`laowantong/hermes-gateway-troubleshooting-20260516.md`
