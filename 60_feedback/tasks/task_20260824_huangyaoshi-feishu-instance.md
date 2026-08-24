---
id: 509
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-24T18:15:05.449239+00:00'
version: v0.1
instance: huangyaoshi
---

# #509 新建飞书「黄药师」实例（老朱外出远程可用）

- **任务号**：#509
- **状态**：queued（**前置条件未满足：等老朱两项拍板 + app_secret 私发，未裁前不施工**）
- **assignee**：huangyaoshi（Hermes profile + nssm 服务施工；王语嫣编排；欧阳锋终审；上线后风清扬审计验收）
- **优先级**：P1（老朱 08-24 CLI 直令）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-feishu-huangyaoshi-instance.md` 裁定采纳）

## 背景

老朱直令：飞书建一个「黄药师」供外出远程干活；已提供自建应用 app_id=`cli_a97dbf6295b89cc4`。现状（风清扬实测）：现役 profile 10 个均为「nssm 服务 + Hermes gateway」范式（服务名 `hermes-gateway-<role>`，AppDirectory=`.../hermes/profiles/<role>`，AppParameters=`gateway run`）；当前**无** huangyaoshi profile、无对应服务，需从零新建。参照模板=ouyangfeng/wangyuyan profile。

## 前置条件（未齐不施工）

1. **老朱拍板模型**：建议 `deepseek-v4-pro`（与王语嫣同档，基建任务重）——待确认
2. **老朱指定 FEISHU_HOME_CHANNEL**：默认老朱私聊——待确认
3. **老朱开放平台侧**：确认 app 已启用「机器人」能力 + 事件订阅选「长连接(WebSocket)」+ 消息收发权限——黄药师无法代做
4. **app_secret 流转**：老朱飞书私发 → 王语嫣随本单转黄药师；**严禁写入 wiki**（git+坚果云同步，进版本史即泄露），只进 profile 本地 `.env`

## 任务（前置齐后）

1. 新建 profile `C:\Users\Administrator\AppData\Local\hermes\profiles\huangyaoshi`（`.env` / `config.yaml` / `SOUL.md` 三件套，以 ouyangfeng profile 为模板：`terminal.cwd=wiki`、`mcp_servers.kdo`、`skills.external_dirs`）
2. `SOUL.md`：黄药师建设者定位（取 `30_wiki/agent-specs/agent-spec-huangyaoshi-builder.md`），写双实例纪律（事实共享/判断独立/daily-context 分 instance/状态变更走 queue_transition/不产卡/终审归欧阳锋）
3. 注册 nssm 服务 `hermes-gateway-huangyaoshi`（AppEnvironmentExtra 含 `HERMES_HOME` + `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1`），启动观察无 crash-loop
4. 验证：飞书双向对话 + 日志无鉴权错误 + `channel_directory.json` 出现老朱 dm 频道

## 验证（验收=风清扬审计口径）

- 服务 Running 无 crash-loop
- `.env` 仅本地；wiki 全库 grep 无 app_secret 残留（负向核查）
- 飞书双向对话通
- 飞书端遵守双实例纪律与角色边界（不产卡、不终审、状态变更走脚本）

## 边界

- 不动现有 10 个 profile；不改 Hermes 本体
- 飞书黄药师与 Claude 端黄药师=同角色双实例，适用判断型/基建型纪律（黄药师主实例仍为单一实例口径——飞书实例是老朱远程入口，基建施工仍串行）

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-feishu-huangyaoshi-instance.md`（施工步骤+验收标准原文）
- #445（角色-实例映射）/ F-048（实例隔离同族）
- 密钥纪律：wiki 不落 secret（本单硬约束）

## 需要谁动作

- **老朱**：两项拍板 + 开放平台确认 + app_secret 私发（前置条件）
- **黄药师**：前置齐后施工
- **风清扬**：上线后审计验收
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：现状核查闭环——**飞书黄药师实例已建成在跑（非本单施工：老朱 08-24 自行部署/codex 协助，08-25 老朱 CLI 口头确认"飞书上面运行的是 hermes，他们都挂着，生产主力是 CLI，共享上下文和记忆，外出时可用飞书继续工作"——前置条件口头拍板齐备）**。本单按验收口径逐项核查：①profile 三件套 ✅（`terminal.cwd=wiki`、`mcp_servers.kdo` 挂 server.py、SOUL.md 双实例纪律 39-43 行全要点：事实共享/判断独立/daily-context 分 instance/状态变更走 queue_transition/不产卡/终审归欧阳锋）；②模型 deepseek-v4-pro ✅（与建议值一致）；③nssm 服务 `hermes-gateway-huangyaoshi` RUNNING ✅（非 crash-loop，channel_directory.json 02:11 活跃更新）；④飞书频道目录存在 ✅；⑤密钥纪律负向核查 ✅——wiki 全库 grep `app_secret` 仅文字提及 2 处（风清扬建议书"不落文档"声明+todos 待办描述），无 secret 值残留；app_id 仅建议书/任务单（非敏感，老朱 CLI 已公开）。

**交付物**：
- 本核查报告（无新代码——实例已建成，本单转核查闭环）
- 既有资产确认：`C:\...\hermes\profiles\huangyaoshi\`（.env/config.yaml/SOUL.md）+ nssm 服务

**验证**：
- L1：服务 `sc.exe query` = RUNNING；config.yaml/SOUL.md 直读逐项对上任务书规格；gateway.pid/lock 在，state.db-wal 活跃
- L2 狗粮：channel_directory.json 含 feishu 频道条目（updated 2026-08-25T02:11——gateway 长连接活着的实证）
- L3 待活体：老朱下次外出时飞书发一条消息实测双向对话（我无法代发——这是唯一未闭合项，闭合即全绿）

**边界**：未动现有 10 个 profile 与 Hermes 本体；未读 .env（密钥不读不抄纪律）；app_secret 未落任何 wiki 文件（负向核查在案）；双实例纪律以 SOUL.md 既有条款为准（事实共享/判断独立，基建施工仍串行——CLI 为主实例）。

**需要谁动作**：欧阳锋终审本单（核查闭环口径：建成事实+验收项核查，无新施工）；老朱外出时发一条飞书消息实测双向对话（L3 最后闭合）；风清扬上线后审计验收（读法：服务态+SOUL 纪律遵守抽查）。
