---
title: codex-relay 故障修复备忘（2026-08-22）
type: memo
status: active
domain: infrastructure
created_at: '2026-08-22'
updated_at: '2026-08-22'
author: 欧阳锋
source_context: codex 启动失败现场修复记录，供后续故障排查快速定位
related:
- 90_control/cli-reference.md
- .agent/context.md
---

# codex-relay 故障修复备忘（2026-08-22）

> 一句话：codex 报 `502 Bad Gateway: http://127.0.0.1:4444/v1/responses` → 根因是 relay 进程没起来 + schtasks 自启任务丢失 → 拉起 relay + 重建自启任务。

## 故障现象

- codex 无法启动，报 `unexpected status 502 Bad Gateway: Unknown error, url: http://127.0.0.1:4444/v1/responses`
- `netstat -ano | grep 4444`：**无 LISTENING**——relay 根本没在监听

## 根因

1. **relay 进程未运行**：最后一次正常监听是 08-21 12:55（日志 `codex-relay listening on 127.0.0.1:4444 → https://api.deepseek.com/v1`），之后进程消失
2. **schtasks 自启任务丢失**：`schtasks /query` 查无 Codex-Relay 任务——08-19 配的开机自启**仅存活 3 天即丢失**，重启后无人拉起 relay

## 修复动作

| 步骤 | 动作 | 命令 |
|:--|:--|:--|
| 1 | 拉起 relay（bat 自带防端口占用守卫 + 无限重启循环） | `cmd /c start "" C:\Users\Administrator\.codex\start-relay.bat` |
| 2 | 重建自启任务（onlogon + Administrator + 最高权限 + 交互式） | `schtasks /create /tn "Codex-Relay" /tr "C:\Users\Administrator\.codex\start-relay.bat" /sc onlogon /ru Administrator /it /rl highest /f` |

> ⚠️ Git Bash 跑 schtasks 必须加 `MSYS_NO_PATHCONV=1`，否则 `/create` 被转成路径报"无效参数"。

## 验证结果

- `netstat`：127.0.0.1:4444 LISTENING（relay 进程存活）
- `curl http://127.0.0.1:4444/v1/models`：返回 `deepseek-v4-flash / deepseek-v4-pro / deepseek-v4-flash-vision-exp`——转发链路真实可用
- 日志确认：`codex-relay listening on 127.0.0.1:4444 → https://api.deepseek.com/v1`
- schtasks 查询：Codex-Relay 任务存在（模式=登录）

## 架构真相（勿偏离）

- **正确架构**：`codex-relay:4444 → DeepSeek`（start-relay.bat 显式传 `--upstream https://api.deepseek.com/v1 --api-key ...`，不依赖 env，防静默回退 openrouter）
- **劣化陷阱**：`kimi-proxy.py` 勿用（08-19 教训）
- start-relay.bat 内置端口占用守卫：4444 已有监听时本实例自动退出——重复拉起不会双开

## 历史与教训

- **08-19**：relay 停止后守护随窗口死 → 修复 = 拉起 + schtasks 开机自启（进程独立）
- **08-22**：schtasks 配置丢失（任务计划中查无此任务）→ 本次重建（改用 onlogon，因 bat 内 `%USERPROFILE%` 依赖用户环境）
- **待验证**：下次重启后登录，relay 是否自动拉起——若再丢，需排查是否有任务清理机制

## 跟进项

1. **下次重启后验证自启**（onlogon 是否真正生效）
2. relay 日志 08-20/08-21 有多次 `api.deepseek.com` 上游请求失败记录（转发层网络错误，relay 本身存活）——codex 偶发报错先查上游连通性，不要直接重启 relay
3. 故障排查速查：`netstat -ano | grep 4444` → 无监听 = 手动跑 `start-relay.bat`；有监听但 502 = 查上游 DeepSeek 连通性
