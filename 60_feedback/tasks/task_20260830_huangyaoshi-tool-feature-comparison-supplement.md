---
id: 576
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-30T05:24:36.096326+00:00'
version: v0.1
instance: huangyaoshi
---

# #576 工具 Feature 对比卡补全（OpenClaw + DeepSeek Harness）

- **任务号**：#576 ｜ **状态**：queued ｜ **assignee**：黄药师（欧阳锋终审）｜ **优先级**：P1
- **立项**：2026-08-30 王语嫣编排（诊断 `diag_20260830_战略笃定篇`，老朱拍板）

## 背景

`tool-ai-agent-feature-comparison` 已有卡对比 Claude Code/Hermes/Codex/CodeBuddy 四工具，但漏了 Truman 最新明确的两个：OpenClaw（龙虾）+ DeepSeek Harness，以及他"项目制用 Codex/ClaudeCode、长期记忆用 OpenClaw/Hermes、定制工作台用 Harness"的三分法视角。

## 任务

更新 `tool-ai-agent-feature-comparison`，补两列：

1. **OpenClaw 列**：长期记忆（多维）、角色身份（真人名/岗位/边界）、主动做动作（心跳/主动汇报）、陪伴进化；局限=局部最优/上下文久崩
2. **DeepSeek Harness 列**：组件化（官方都组件化/插件可改）、定制化（造自己的 Agent 工作台）、跨平台（Linux/Win/指令集）、多机部署（内网穿透）；官方定位="Everything is a Plugin"（GitHub 实证）
3. **加"三分法"总纲**：项目制（一次性）→ Codex/ClaudeCode；Agent 级（长期记忆）→ OpenClaw/Hermes；工作台（定制/多机）→ Harness

## 验证

- 补全后 6 工具对比，每工具差异化 Feature 明确可查
- 与 #575 选型树互补不重复（本卡=逐工具 Feature 明细，该卡=三分法决策）

## 边界

- 只补 OpenClaw/Harness 两列 + 三分法总纲，不动已有四工具内容（除非发现事实错误）
- 不涉及 Harness 实跑（老朱手操中）

## 需要谁动作

- **黄药师**：补全工具对比卡
- **欧阳锋**：终审
