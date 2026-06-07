---
id: "case-纪浩-focus-prompt-design"
title: "案例：纪浩的 AI 协作产品设计——从 S1 设计冻结到 S7 实现交接"
type: "case"
status: "draft"
domain:
  - "prompt-engineering"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享 + 真实项目 /focus 功能的产品设计提示词"
source_refs:
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-提示词案例01.txt"
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-提示词案例02.txt"
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-图片01.png"
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-图片02.png"
tags:
  - "#boundary/not-for-creative"
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#confidence/verified-by-case"
  - "#domain/prompt-engineering"
  - "#domain/yitang"
  - "#scene/agent-infrastructure"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#scene/note-taking"
  - "#scene/product-design"
  - "#scene/skill-engineering"
  - "#type/case"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "case-纪浩-skills-market"
  - "case-truman-ai-partner"
---

# 案例：纪浩的 AI 协作产品设计

> 纪浩用自己讲的五层方法论，建造了一个 AI 辅助的现场工作台（`/focus`）。这两份提示词是方法论在真实产品上的落地实例——不是"怎么用 AI"的方法论，是"怎么用结构化 prompt 做产品设计"的工程方法。

## 场景

纪浩在做一个名为 Daily 的时间管理工具。其中 `/focus/[timeNodeId]` 是一个核心功能——用户在时间流中进入"现场执行工作台"，记录重要信息、处理阻塞、推进任务状态。

他不只是让 AI 写代码。他写了两份结构化提示词，用产品设计的标准流程（S1-S5 设计冻结 → S6-S7 实现交接）来驱动 AI 协作。

## 四要素验证

### Before-After

| | Before | After |
|:---|:---|:---|
| 产品设计 | 边想边改，需求膨胀，越做越模糊 | S1-S5 设计冻结，29 条封闭决策，Scope 被显式锁死 |
| 实现交接 | 口头描述 + 随手截图，AI 理解偏差大 | 结构化手稿：TypeScript 接口 + 组件清单 + 测试脚本 + 日志 schema |
| 拒绝表达 | 实现中临时判断"这个不做" | S1-S5 冻结稿里明确写了"这不是什么"（不是项目管理页、不是完整看板、不做浏览器验证） |

### 真实锚点

真实项目。`/focus` 是 Daily 产品的核心 feature。两份提示词不是教学案例——它们本身就是项目的交付物。

### 受益人

- **纪浩自己**：S1-S5 冻结后不用每次对话重讲上下文。提示词 = 持久化的决策文档
- **AI（Claude/Codex）**：收到的是结构化规格而不是模糊描述。接口定义到 TypeScript 级别，组件清单到名字级别，测试脚本到步骤级别
- **接手的人**：如果代码作者换了，S6-S7 手稿 + 终版 HTML 就是完整的交接文档

### 可解性

因果链：
1. 产品设计天然有"需求膨胀→越做越模糊"的倾向 → S1-S5 冻结解决
2. AI 理解模糊描述时输出偏差大 → 结构化 prompt + TypeScript 接口解决
3. 实现阶段容易"做着做着就做多了" → Migration Stop Point 硬门禁解决

## 核心设计洞察：提示词就是冻结决策文档

这两份提示词不是一个"prompt 工程技巧"——它是一种**产品设计方法论**。

**S1-S5 冻结稿的特征**：

- 每个 section 都在回答"做什么"的同时回答"**不做什么**"
- `/focus` 是 Live Execution Workbench，**不是**通用项目管理页、**不是**聚焦记录展示页、**不是**完整看板
- Capture Mode 被精细分类：Explore 和 Experiment 被**故意拆开**——"思维模式、行为模式和目标不同"
- "Migration Stop Point"：如果实现需要 DB migration，停下，单独开 schema gate。选择困难的路径、显式表达代价

**S6-S7 实现手稿的特征**：

- 29 条封闭决策，每条有理由
- TypeScript 接口定义到字段级别（`FocusExecutionProjection`、`CaptureMode`、`FlowBoardLane`）
- 组件清单到名字级别（`CurrentProblemSelector`、`CaptureDock`、`FlowBoard`、`ContextDrawer` 等 11 个组件）
- 7 个 Journey Test Script，每个有步骤 + 通过条件
- 日志 schema 到字段级别（`.data/focus-execution-trace.ndjson`，9 个必追踪项）

## 五层方法论在案例中的对应

| 纪浩的五层 | 在 /focus 设计中的体现 |
|:---|:---|
| L1 四要素验证 | "`/focus` 是 Live Execution Workbench"——每条设计决策有 Before-After 和拒绝理由 |
| L2 Agent Workspace | 10 Capture Mode + Flow Board + Context Drawer = Agent Workspace 的组件化实现 |
| L3 Do-first PDCA | S1-S5 冻结→ HTML 原型→ 回填文档→ 29 条封闭→ 实现交接——完整的迭代路径 |
| L4 Skills Market | 这套设计是可复用的 product pattern——下次做类似功能时直接引用 frozen decision |
| L5 认知哲学 | Migration Stop Point——"选择困难的路径、显式表达代价" |

## 可迁移场景

1. **任何需要"设计冻结→实现交接"的 AI 协作场景**：不是每次对话从零开始，而是把设计决策持久化为 prompt 文档
2. **产品需求文档的编写**：结构化 prompt 可以作为轻量级 PRD——比传统 PRD 更精确（有接口定义），比纯对话更持久（可重入）
3. **KDO 自身的 manifest 和 system prompt 编译**：纪浩的 S1-S5→S6-S7 流水线，和 KDO 的 manifest→encapsulate 流水线是同构的——都是"结构化知识 → AI 可执行的决策文档"

## 反例

**什么时候不应该学这个案例**：
- 项目还在探索阶段，核心定位一周变三次——S1-S5 冻结的前提是方向已经过验证
- 团队只有 1 人且不需要和 AI 协作——结构化手稿的价值在于"人→AI"或"人→人"的信息传递，如果只给自己看，笔记就够了

## 对 KDO 的启发

这两份提示词展示了 `kdo encapsulate` 的编译模式能扩展到什么程度——不只是编译 skill 的 system prompt，而是编译**任何结构化知识到 AI 可执行的决策文档**。

纪浩的 S1-S5 冻结稿本质上就是一个"产品设计的 manifest"——定义了边界（不是什么）、组件（Capture Mode×10）、交互（Flow Board + Material Accordion）、质量门（Migration Stop Point）。KDO 的 manifest.yaml 完全可以对接到这种级别的产品设计 prompt 编译。

> ⚠️ 洪七公 OCR 的两张图（五层结构图 + 参考案例图）待补充后更新本卡。
