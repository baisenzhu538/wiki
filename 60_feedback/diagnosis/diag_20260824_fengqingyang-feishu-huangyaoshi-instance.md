---
id: diag_20260824_fengqingyang-feishu-huangyaoshi-instance
title: 建议书：为老朱新建飞书「黄药师」实例（外出远程可用）
type: proposal
status: pending_orchestration
author: 风清扬
audience: 王语嫣
date: 2026-08-24
---

# 一、结论先行

- 老朱 08-24 CLI 直令：在飞书建一个「黄药师」，供其外出远程干活；已提供飞书自建应用 app_id=`cli_a97dbf6295b89cc4` 与 app_secret（app_secret **不落本文档**，处理见 §五）。
- 此事属基础设施（新建 Hermes profile + nssm 服务），按分工归 **黄药师施工**。风清扬只审计、不施工、不动基建脚本；本建议书只做编排与验收标准。
- 建议王语嫣立项入队：assignee=黄药师，P1；终审=欧阳锋；上线后风清扬审计验收。

# 二、现状审计（实测，非转述）

- 现有飞书 agent 全部为「nssm 服务 + Hermes gateway」范式，已核实的统一参数：
  - 服务名 `hermes-gateway-<role>`，二进制 `C:\tools\nssm\nssm.exe`
  - `AppDirectory = C:\Users\Administrator\AppData\Local\hermes\profiles\<role>`
  - `AppParameters = gateway run`
  - `AppEnvironmentExtra = HERMES_HOME=<profile 目录>, PYTHONIOENCODING=utf-8, PYTHONUTF8=1`
- 现役 profile 10 个：wangyuyan（模型 deepseek-v4-pro，服务当前 Paused）、ouyangfeng（deepseek-v4-flash，Running）、laowantong-feishu（Running）等。
- 当前 **无** `huangyaoshi` profile、**无** `hermes-gateway-huangyaoshi` 服务 → 需从零新建。
- 参照 profile 关键件（以 ouyangfeng/wangyuyan 为模板）：
  - `.env`：`<PROVIDER>_API_KEY`、`HERMES_MAX_ITERATIONS=90`、`FEISHU_APP_ID`、`FEISHU_APP_SECRET`、`FEISHU_DOMAIN=feishu`、`FEISHU_CONNECTION_MODE=websocket`、`GATEWAY_ALLOW_ALL_USERS=true`
  - `config.yaml`：`model.*`、`platforms.feishu`、`FEISHU_HOME_CHANNEL`、`terminal.cwd=C:\Users\Administrator\Desktop\wiki`、`mcp_servers.kdo`、`skills.external_dirs=wiki/40_outputs/capabilities/skills/shared`
  - `SOUL.md`：角色人设（黄药师=建设者，取 `30_wiki/agent-specs/agent-spec-huangyaoshi-builder.md`）

# 三、施工步骤（交黄药师）

1. **飞书开放平台侧前置（需老朱账号）**：确认 app `cli_a97dbf6295b89cc4` 已启用「机器人」能力 + 「事件订阅」选「长连接(WebSocket)」+ 已开通消息收发权限。若未开，gateway 连不上——此项黄药师无法代做，需老朱在开放平台操作。
2. 新建 profile 目录 `C:\Users\Administrator\AppData\Local\hermes\profiles\huangyaoshi`。
3. 写 `.env`：`FEISHU_APP_ID=cli_a97dbf6295b89cc4`、`FEISHU_APP_SECRET=<向老朱索取，不落文档>`、`FEISHU_DOMAIN=feishu`、`FEISHU_CONNECTION_MODE=websocket`、`GATEWAY_ALLOW_ALL_USERS=true`、`HERMES_MAX_ITERATIONS=90`、模型 `*_API_KEY`。
4. 写 `config.yaml`：以 ouyangfeng profile 为模板，改 `model`（建议 deepseek-v4-pro，见 §四）、`platforms.feishu`、`terminal.cwd=wiki`、`mcp_servers.kdo`、`skills.external_dirs`；`FEISHU_HOME_CHANNEL` 待老朱指定（默认=老朱私聊）。
5. 写 `SOUL.md`：黄药师建设者定位，与 Claude 端黄药师同人设；遵守双实例纪律（事实共享、判断独立、daily-context 分 instance、状态变更走 queue_transition、不产卡、终审仍归欧阳锋）。
6. 注册 nssm 服务 `hermes-gateway-huangyaoshi`（AppDirectory/HERMES_HOME 指向该 profile），启动并观察无 crash-loop。
7. 验证：飞书给机器人发消息 → 黄药师回应 + 日志无鉴权错误 + `channel_directory.json` 出现老朱 dm 频道。

# 四、待老朱裁定（未裁前不施工）

- **模型**：飞书黄药师建议 `deepseek-v4-pro`（与王语嫣同档；黄药师做基建任务重）。沿用与否请老朱拍板。
- **FEISHU_HOME_CHANNEL**：黄药师挂到哪个群/私聊？默认老朱私聊。

# 五、密钥处理（硬性）

- app_secret **严禁写入本 wiki**（wiki 走 git + 坚果云同步，进版本史即泄露）。
- 只进 profile 本地 `.env`（`C:\Users\Administrator\AppData\Local\hermes\profiles\huangyaoshi\.env`）。
- 建议流转：老朱在飞书私发给王语嫣 → 王语嫣随任务单转给黄药师。本文档不承载 app_secret。

# 六、验收标准（上线后风清扬审计）

- `hermes-gateway-huangyaoshi` 服务 Running 且无 crash-loop。
- `.env` 仅本地；wiki 全库无 app_secret 残留（grep 负向核查）。
- 飞书可双向对话（老朱→机器人、机器人→老朱）。
- 黄药师飞书端遵守双实例纪律与角色边界（不产卡、不终审、状态变更走脚本）。