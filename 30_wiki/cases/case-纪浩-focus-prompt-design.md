---

id: case-纪浩-focus-prompt-design
title: 案例：纪浩的 AI 协作产品设计——从 S1 设计冻结到 S7 实现交接
type: case
status: enriched
domain:
- prompt-engineering
- yitang
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论 分享 + 真实项目 /focus 功能的产品设计提示词
source_refs:
- 10_raw/sources/src_20260619_76cc7f71_00_inbox_AI俱乐部_人和AI协作_纪浩_提示词案例01.txt
- 10_raw/sources/src_20260619_5ec7f3c8_00_inbox_AI俱乐部_人和AI协作_纪浩_提示词案例02.txt
- 10_raw/sources/src_20260619_d9794671_00_inbox_AI俱乐部_人和AI协作_纪浩_五层结构_图片01.png
- 10_raw/sources/src_20260619_df980155_00_inbox_AI俱乐部_人和AI协作_纪浩_参考案例_图片02.png
tags:
- '#perspective/compliance'
- '#perspective/professional'
- '#confidence/source-cited'
- '#confidence/verified-by-case'
- '#domain/prompt-engineering'
- '#domain/yitang'
- '#scene/agent-infrastructure'
- '#scene/ai-collaboration/pdca-execution'
- '#scene/ai-collaboration/problem-validation'
- '#scene/ai-collaboration/prompt-engineering'
- '#scene/ai-collaboration/workspace-design'
- '#scene/hardware-debugging/prototyping'
- '#scene/knowledge-management/tagging'
- '#scene/learning-methodology'
- '#scene/note-taking'
- '#scene/product-design/design-freeze'
- '#scene/product-design/focus-workbench'
- '#scene/skill-engineering/manifest-design'
- '#content-format/case-study'
created_at: 2026-06-07
updated_at: '2026-06-17'
related:
  - '[[case-纪浩-from-zip-to-five-layers]]'
- '[[case-ji-hao-skills-market]]'
- '[[case-truman-ai-partner]]'
- '[[case-纪浩-from-zip-to-five-layers]]'
- '[[dk-ji-hao-ai-cant-design-structure]]'
- '[[dk-ji-hao-pdca-starts-from-do]]'
- '[[case-ji-hao-ui-design-constraint-evolution]]'
author: 纪浩
reviewed_by: 老顽童
confidence: 0.75
trust_level: medium
diagnostic_signals:
- signal: AI 在实现阶段反复问"这个做不做""这个要不要算进去"
  framework_lens: S1-S5 设计冻结缺少"不是什么"
  follow_up_question: 你能否列出 3 条明确"不做"的决策？每条是否都有理由？
- signal: 同一个输入表单既要"收集信息"又要"验证假设"
  framework_lens: Explore / Experiment 未拆分
  follow_up_question: 这个任务是剪枝假设（Experiment）还是扩大边界（Explore）？二者思维模式不同，应否拆成两个 Capture Mode？
- signal: 实现两周后需求还在变， freeze 稿被不断推翻
  framework_lens: S1-S5 开放问题未封闭
  follow_up_question: S1-S5 是否已签字？剩余问题是否已明确标为"进入 S6/S7 处理"而不是"现在再讨论"？
- signal: 遇到需要改 schema 或 DB migration 的需求时直接动手
  framework_lens: Migration Stop Point 硬门禁缺失
  follow_up_question: 这个改动是否必须新增 indexed/generated fields、专表或 DB migration？如果是，有没有先停下进入 schema/data contract gate？
---

# 案例：纪浩的 AI 协作产品设计——从 S1 设计冻结到 S7 实现交接

> 纪浩用自己讲的五层方法论，建造了一个 AI 辅助的现场工作台（`/focus`）。这两份提示词是方法论在真实产品上的落地实例——不是"怎么用 AI"的方法论，是"怎么用结构化 prompt 做产品设计"的工程方法。

## Background

纪浩在做一个名为 **Daily** 的时间管理工具。其中 `/focus/[timeNodeId]` 是一个核心功能：用户在时间流中安排 `TimeBlock`，点击 block 后进入"现场执行工作台"，记录重要信息、处理阻塞、推进任务状态。

这个功能的典型困境是：

1. **需求天然膨胀**：现场工作台很容易从"记录当前推进"滑向"通用项目管理页""完整看板""焦点记录展示页"。
2. **AI 理解偏差大**：如果只用口头描述 + 随手截图，AI（Claude/Codex）会把模糊需求按照自己的模式补全，产出偏离设计意图。
3. **实现做着做着就做多**：没有显式边界时，实现阶段会顺手把 "Later" 当成 "Should"，把 "Should" 当成 "Must" 做掉。

纪浩的应对方式不是写更长的 PRD，而是把产品设计流程本身写成两份结构化提示词：**S1-S5 设计冻结稿** + **S6-S7 实现交接稿**。

## What Happened

### 第一步：S1-S5 设计冻结（332 行提示词）

日期：2026-05-14。范围：冻结 `/focus/[timeNodeId]` 的产品定位、开放问题结论、信息架构（IA）和方案方向；不修改页面代码，不变更 DB schema。

核心动作：

| 阶段 | 关键决策 | 在 /focus 中的体现 |
|:---|:---|:---|
| S1 Discover | 明确项目事实与最佳实践输入 | `/time` 是时间编排 surface；`/focus` 已具备基础投影；GTD/Jira/Trello/Research log/PDCA 等作为输入 |
| S2 Requirements | Must / Should / Could / Later 四级需求 | Must 含"首屏突出当前推进""Capture Mode 必须含 Explore/Experiment""阻塞处理入口"；Later 含"外部知识源连接""多人协作、SLA" |
| S3 Model / Journey | 主旅程 + 10 种 Capture Mode | `Action` / `ImportantInfo` / `HumanSignal` / `Blocker` / `Interruption` / `Meeting` / `Explore` / `Experiment` / `StateSummary` / `ContextEdit` |
| S4 IA / Interaction | Surface Model + Information Architecture | `Live Execution Workbench` = `FocusExecutionShell` + Header + Current Progress + Capture Dock + Collapsible Flow Lanes + Context Drawer + Recent Important Info |
| S5 Prototype Direction | 首版采用 Execution Console | 不做完整 Kanban，不做 Evidence-first Logbook；先做日志追踪，不急于新增 schema |

冻结稿的每条决策都在回答"做什么"的同时回答"**不做什么**"：

- `/focus` 是 **Live Execution Workbench**，不是通用项目管理页、不是聚焦记录展示页。
- `Explore` 和 `Experiment` **故意拆开**——"思维模式、行为模式和目标不同"。
- Flow Lanes **默认折叠**，是执行辅助，不是完整看板。
- 上下文编辑的边界是"整理任务上下文和背景知识"，**不是重构任务本身**。

### 第二步：S6-S7 实现交接（632 行提示词）

日期：同一天（2026-05-14），依据 S1-S5 冻结稿。范围：封闭 UI 结构、验证脚本、实现切分、projection 需求、命令复用、日志追踪与索引检查。

产出物：

- **29 条封闭决策**（Closed Decisions），每条有编号和理由。
- **终版 HTML 原型路径**：`docs/prototypes/focus-s7-static.html`，作为视觉/交互基准。
- **TypeScript 接口定义到字段级别**：`FocusExecutionProjection`、`CaptureMode`、`FlowBoardLane`、`MaterialAccordionGroup` 等。
- **组件清单到名字级别**：`CurrentProblemSelector`、`CurrentProgressPanel`、`CaptureDock`、`FlowBoard`、`MaterialAccordion`、`FocusContextDrawer`、`RecentImportantInfo`、`StateTransitionModal` 等 11 个组件。
- **7 个 Journey Test Script**，每个有步骤 + 通过条件：进入现场并推进多个并行项、快速收集到 Inbox/Problem、阻塞转化、Explore/Experiment 支撑 Plan、会议记录与关联主体、Context Drawer 整理上下文、状态转变总结确认。
- **日志 schema 到字段级别**：`.data/focus-execution-trace.ndjson`，9 个最低追踪项（`at`、`timeNodeId`、`event`、`counts`、`captureMode`、`flowLane`、`materialGroup`、`queryMs`、`noiseFeedback`）。

### 关键硬门禁：Migration Stop Point

S6-S7 交接稿里有一条显式规则：

> 如果实现发现必须新增 indexed/generated fields、专表、FTS 或 DB migration，**必须停下并单独做 schema/data contract gate**。

这不是技术细节，是产品哲学——"选择困难的路径、显式表达代价"。纪浩用这条规则防止实现阶段顺手把schema改掉，让设计冻结真正成立。

## 结果

| 维度 | Before | After |
|:---|:---|:---|
| 产品设计 | 边想边改，需求膨胀，越做越模糊 | S1-S5 冻结，29 条封闭决策，Scope 被显式锁死 |
| 实现交接 | 口头描述 + 随手截图，AI 理解偏差大 | 结构化手稿：TypeScript 接口 + 组件清单 + 测试脚本 + 日志 schema |
| 拒绝表达 | 实现中临时判断"这个不做" | S1-S5 冻结稿里明确写了"这不是什么" |
| 变更控制 | 实现中顺手改 schema | Migration Stop Point 硬门禁，改 schema 必须先停下 |

两份提示词本身就是项目的交付物。它们让：

- **纪浩自己**：S1-S5 冻结后不用每次对话重讲上下文；提示词 = 持久化的决策文档。
- **AI（Claude/Codex）**：收到的是结构化规格而不是模糊描述。
- **接手的人**：如果代码作者换了，S6-S7 手稿 + 终版 HTML 就是完整的交接文档。

## 可迁移

1. **任何需要"设计冻结→实现交接"的 AI 协作场景**：不是每次对话从零开始，而是把设计决策持久化为 prompt 文档。
2. **产品需求文档的编写**：结构化 prompt 可以作为轻量级 PRD——比传统 PRD 更精确（有接口定义），比纯对话更持久（可重入）。
3. **KDO 自身的 manifest 和 system prompt 编译**：纪浩的 S1-S5→S6-S7 流水线，和 KDO 的 manifest→encapsulate 流水线是同构的——都是"结构化知识 → AI 可执行的决策文档"。
4. **多 Agent / 多角色协作的接口设计**：当 AI 需要与另一个 AI 或人交接时，TypeScript 接口 + 组件清单 + 测试脚本是一种可验证的"契约"。

## 诊断信号

以下信号说明你也可以/需要使用"S1-S5 设计冻结 + S6-S7 实现交接"模式：

| 信号 Signal | 透镜 Lens | 跟进问题 Follow-up |
|:---|:---|:---|
| AI 在实现阶段反复问"这个做不做""这个要不要算进去" | S1-S5 设计冻结缺少"不是什么" | 你能否列出 3 条明确"不做"的决策？每条是否都有理由？ |
| 同一个输入表单既要"收集信息"又要"验证假设" | Explore / Experiment 未拆分 | 这个任务是剪枝假设（Experiment）还是扩大边界（Explore）？二者思维模式不同，应否拆成两个 Capture Mode？ |
| 实现两周后需求还在变，freeze 稿被不断推翻 | S1-S5 开放问题未封闭 | S1-S5 是否已签字？剩余问题是否已明确标为"进入 S6/S7 处理"而不是"现在再讨论"？ |
| 遇到需要改 schema 或 DB migration 的需求时直接动手 | Migration Stop Point 硬门禁缺失 | 这个改动是否必须新增 indexed/generated fields、专表或 DB migration？如果是，有没有先停下进入 schema/data contract gate？ |

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:---|:---|:---|
| **把冻结写成"需求清单"但不说"不是什么"** | AI 在实现阶段反复确认"这个做不做"；团队争论"当初不是说要做这个吗" | 每条 Must/Should/Could 必须配一条对应的 Not："这不是 ___，所以不做 ___" |
| **Explore 和 Experiment 混在一起** | 同一个 capture 既要"收集外部信息"又要"动手验证假设"，字段互相打架 | 强制拆成两个 Capture Mode：Explore 只扩大边界、记录线索；Experiment 只剪枝假设、记录 trial/result |
| **遇到 schema 改动不喊停** | 实现中顺手新增 indexed/generated fields、专表或 DB migration，导致冻结稿被悄悄推翻 | 建立 Migration Stop Point 硬门禁：任何 schema 改动必须先停下，单独走 schema/data contract gate，写入决策理由 |
| **用完整 Kanban 替代折叠 Flow Lanes** | 主区被六栏看板淹没，用户找不到当前推进入口 | Flow Lanes 默认折叠，只承载执行辅助；可流转对象用三栏 Flow Board，不可流转材料用 Material Accordion |
| **把 S6-S7 交接稿当成"最后才写"的文档** | 实现已经开始，甚至快做完了，才补交接稿，AI 和接手人都读不懂设计意图 | S6-S7 必须在 S1-S5 冻结后立即产出，作为实现的输入条件而不是事后总结 |

## 落地工具

### S1-S5 设计冻结检查清单

| 检查项 | 通过标准 | 未通过时的修复 |
|:---|:---|:---|
| 定位是否一句话能说清？ | 用"是 ___，不是 ___"格式写出 | 回到 S1，用 Project Facts + Best Practice Inputs 重新收敛 |
| 是否有明确的"不是什么"？ | 至少 3 条"不做"决策，每条有理由 | 每条 Must/Should/Could 补一条 Not |
| 开放问题是否已封闭或移交？ | S1-S5 开放问题全部关闭，剩余问题明确标"进入 S6/S7" | 把还在争论的问题移出 S1-S5，不要让它阻塞冻结 |
| Explore / Experiment 是否拆分？ | 两个 Capture Mode 的字段和目标不同 | 合并的拆成两个；重复的字段只保留在一个里 |
| 是否有 Migration Stop Point？ | 文档中显式写明"新增 schema/DB migration 必须先停下" | 在 S5 或 S6 开头加入硬门禁条款 |
| 需求是否分 Must/Should/Could/Later？ | 四级需求都有内容，且 Later 不会被实现阶段误读 | 把 Later 列表单独成段，并写"本轮不做" |

### S6-S7 实现交接最小模板

```markdown
# {功能名} S6-S7 实现交接

## 0. Closed Decisions
1. {决策1} — {理由}
2. {决策2} — {理由}
...

## 1. Final HTML / Prototype
- 路径：{docs/prototypes/xxx.html}
- 范围：{做什么 / 不做什么}

## 2. Component Handoff
| 组件名 | 职责 | 复用/新建 |
| ... | ... | ... |

## 3. Projection (TypeScript 接口)
```ts
interface XxxProjection { ... }
```

## 4. Journey Test Scripts
- Script A: {目标} / {步骤} / {通过条件}
- Script B: ...

## 5. Logging & Index
- 日志落点：{文件路径}
- 追踪字段：{列表}
- Migration Stop Point：{触发条件与处理流程}

## 6. Validation Commands
```bash
npm run lint
npm run test
npm run build
```
```

### Migration Stop Point 快速决策卡

当实现中出现以下任一情况时，必须停下：

- [ ] 需要新增 indexed/generated fields
- [ ] 需要新增专表
- [ ] 需要新增 FTS（全文搜索）
- [ ] 需要 DB migration
- [ ] 需要修改稳定 `.kb` 或 apply `.kbp`

停下后执行：

1. 在 S1-S5 冻结稿或 S6-S7 交接稿中补充一条 Closed Decision，说明为什么必须改 schema。
2. 评估是否有替代方案（日志追踪、交互降噪、payload_json 承载展示字段）。
3. 如果必须改，单独写 schema/data contract gate 文档，定义字段、索引、迁移脚本、回滚方案。
4. 不执行 Act，不修改 stable `.kb`，直到 gate 通过。

## Feedback Path

应用本案例后，用以下问题循环复盘：

1. 我的产品设计是否有一句话能说清的定位（是/不是什么）？
2. 我是否把"不做"的决策写进了 prompt/文档，而不是口头约定？
3. AI 在实现阶段是否还在反复确认边界？如果是，哪条"不是什么"没写清楚？
4. 我有没有为 schema/DB migration 设置硬门禁？
5. 如果明天换一个人/换一个 AI 接手，他能否只读 S6-S7 交接稿就继续实现？

- 使用本案例后有反馈，提交至 `60_feedback/cases/case-纪浩-focus-prompt-design`。

## 关联卡牌

- **[[case-ji-hao-skills-market]]** — 同一演讲者的另一个真实案例：一堂内部 Skills 分发平台，从"微信传 zip"到"Agent 自助"。与本案例共同展示纪浩五层方法论在不同工程问题上的落地。
- **[[case-纪浩-from-zip-to-five-layers]]** — 纪浩从微信传 zip 的混乱到五层协作体系的完整演化。本案例是 L2 Agent Workspace 与 L3 Do-first PDCA 在产品设计场景的具体应用。
- **[[dk-ji-hao-ai-cant-design-structure]]** — 本案例的底层暗知识："AI 不会自己搞结构设计，必须人先定义结构"。S1-S5 冻结稿就是人帮 AI 定义的产品结构。
- **[[dk-ji-hao-pdca-starts-from-do]]** — S1-S5 冻结前的 HTML 原型来自 Do-first 迭代：先做出一版，再加 Check/Plan/Act，而不是先写完整计划再动手。
- **[[case-ji-hao-ui-design-constraint-evolution]]** — 约束文档从临时规则沉淀为 L3 工作手册的演化案例。与本案例的"29 条封闭决策"形成"规则如何被持久化"的对照。
- **[[case-truman-ai-partner]]** — Truman 的 AI Partner 设计哲学。纪浩的 /focus 提示词是同一套"给 Agent 结构化环境"思想在产品功能设计上的工程实现。
- **[[concept-ji-hao-ai-collaboration-methodology]]** — 纪浩 AI 协作方法论总纲。本案例是其中 L2 Agent Workspace、L3 Do-first PDCA 与 L5 Skills Market 思想的共同产物。
