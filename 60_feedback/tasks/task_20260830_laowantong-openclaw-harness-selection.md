---
id: 575
assignee: laowantong
status: in_progress
updated_at: '2026-08-30T05:31:05.774877+00:00'
version: v0.1
instance: laowantong
---

# #575 OpenClaw vs Harness 选型决策树卡

- **任务号**：#575 ｜ **状态**：queued ｜ **assignee**：老顽童（欧阳锋终审）｜ **优先级**：P1
- **立项**：2026-08-30 王语嫣编排（诊断 `diag_20260830_战略笃定篇`，老朱拍板）

## 背景

老朱核心问题："到底什么情况下用 OpenClaw、什么情况下用 Harness？" Truman 在口述稿里反复讲但散落多处，知识库已有 `tool-ai-agent-feature-comparison` 只覆盖 Claude/Hermes/Codex/CodeBuddy，缺 OpenClaw + Harness + "项目制/Agent 级/工作台"三分法。

## 任务

产出 `framework-openclaw-vs-harness-selection` 选型决策树卡，必须含：

1. **70% 论**（Truman 原话："CodeX/WorkBody/龙虾/Hermes/Harness 这套 70% Feature 一样，每个有额外 10-30 个差异化 Feature"）
2. **三分法决策树**：OpenClaw=养员工（长期记忆/角色身份/主动/陪伴进化）｜Harness=造工具（组件化/插件可改/跨平台/多机部署，"Everything is a Plugin"）｜Codex/Claude Code=打短工（一次性 Session）
3. **触发场景表**（每类 2-3 个具体场景 + 1 个反例）
4. **KDO 映射**：六角色=Hermes（≈OpenClaw 层），pipeline/门禁/脚本可 Harness 化

## 素材锚点

- 口述稿 66000-77616（Harness 详述："把个人定制 Harness 工作台门槛打掉""组件化连官方都组件化"）+ 第七轮（OpenClaw：灵魂赋能/10 角色硅基团队）
- 外部调研：GitHub `deepseek-ai/deepseek-harness`（"Everything is a Plugin"）、`garrytan/gbrain`（"OpenClaw/Hermes Agent Brain"——OpenClaw 与 Hermes 同类）
- 已有卡：`tool-ai-agent-feature-comparison`（四工具 Feature 表，复用其表格结构）

## 验证

- 选型树能一句回答"什么情况用 OpenClaw / 什么情况用 Harness"，含触发场景 + 反例
- 与 `tool-ai-agent-feature-comparison` 不重复（本卡=三分法决策视角，该卡=逐工具 Feature 明细）

## 边界

- 不重写 `tool-ai-agent-feature-comparison`（那是 #576 黄药师的活），本卡只出"选型决策树"框架卡
- 不涉及 Harness 实跑验证（老朱自己在手操验证中）

## 需要谁动作

- **老顽童**：生产 `framework-openclaw-vs-harness-selection`
- **欧阳锋**：终审
