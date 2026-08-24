---
id: 509
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24T16:00:00+00:00'
version: v0.1
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
