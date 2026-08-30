---
id: 576
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-30T06:34:00.603673+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-30'
grade: A
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

## 执行报告

**交付物**
- `30_wiki/tools/tool-ai-agent-feature-comparison.md`（补全 OpenClaw + DeepSeek Harness 两列 + 三分法总纲）

**完成内容**
- 补 OpenClaw 列（长期记忆/角色身份/主动做动作/陪伴进化 + 局限=局部最优/上下文久崩）
- 补 DeepSeek Harness 列（组件化/定制化/跨平台/多机部署 + 官方定位 "Everything is a Plugin"）
- 新增「一、三分法总纲」：项目制(打短工)→Codex/ClaudeCode；Agent级(养员工)→OpenClaw/Hermes；工作台(造工具)→Harness
- Feature 差异表 4 列扩为 6 列；新增「三.5 两新工具差异化 Feature」专属维度表
- 原四工具内容保留不动（瑞士军刀/传送带/马拉松/贴身秘书四比喻原文未改）

**验证**
- YAML frontmatter 解析通过（id=tool-ai-agent-feature-comparison，status=pending_review）
- 六工具关键词全命中：OpenClaw / DeepSeek Harness / 三分法 / 养员工 / 造工具 / 打短工 / Everything is a Plugin
- 原四工具关键词全保留：瑞士军刀 / 工厂传送带 / 马拉松选手 / 贴身秘书
- 与 #575 互补不重复：本卡=逐工具 Feature 明细；#575=三分法决策树（本卡 related 已引 framework-openclaw-vs-harness-selection）

**边界**
- 未动原四工具 Feature 内容（8 维度四工具评级原文保留）
- 未涉及 Harness 实跑验证（老朱手操中）
- framework-openclaw-vs-harness-selection 卡 #575 尚在产（related 预引，待其终审后双向回链由王语嫣落）

**需要谁动作**
- 欧阳锋终审

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

**审查结论：PASS A**

- 补 OpenClaw + DeepSeek Harness 两列 + 三分法总纲，原四工具内容未动（瑞士军刀/传送带/马拉松/贴身秘书四比喻原文保留）。
- 行号锚点 L1376-1392（三分法）、L1318-1336（OpenClaw）、L1688-1692/L1770-1772（Harness）命中原文。
- 与 #575 互补不重复（本卡=逐工具 Feature 明细，该卡=三分法决策树），related 双向互链。
- 写审分离：author 含黄药师补全署名，reviewed_by=待审，合规。

