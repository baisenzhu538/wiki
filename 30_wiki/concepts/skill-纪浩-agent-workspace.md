---
id: "skill-纪浩-agent-workspace"
title: "技能：Agent Workspace 搭建法——AI 的工作环境设计"
type: "skill"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/not-for-creative"
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/ai-collaboration"
  - "#scene/agent-infrastructure"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management"
  - "#scene/learning-methodology"
  - "#scene/product-design"
  - "#scene/skill-engineering"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "concept-纪浩-ai-collaboration-methodology"
  - "skill-纪浩-progressive-disclosure"
  - "dk-纪浩-ai-cant-design-structure"
---

# 技能：Agent Workspace 搭建法

> AI 是模式匹配系统，不会自己搞结构设计。你给它一个乱的工作空间，它就会在错误的道路上越走越远——"目录乱七八糟，最后只能放弃让 AI 重新投胎"。先搭好工作空间，再让 AI 动手。

## Purpose

为 AI Agent 搭建一个结构化的信息环境，让它能可靠地理解系统、访问知识、执行任务、记录日志。Agent Workspace 不是在 AI 开始工作之后才需要的——它是 AI 开始工作之前必须做好的第一步。

## Protocol

### 五大模块

| 模块 | 内容 | 为什么需要 | 例子 |
|:---|:-----|:-----------|:---|
| **① 系统自述** | 架构、组件、技术栈、目录结构 | 没有这个，需求越多架构越漂移 | `README.md` 含系统架构图 |
| **② 领域知识** | 业务逻辑、概念定义、规则、术语库 | AI 没有这些会自己猜，导致不可验证 | KDO 的 `30_wiki/concepts/` |
| **③ 服务文档** | 导诊台、工作手册、工具集、经验模式库 | 复杂任务需要分类+分流+标准作业程序 | KDO 的 `manifest.yaml` |
| **④ 任务管理** | 任务上下文、执行记录、状态跟踪 | AI 接手多个任务后会混乱 | KDO 的 `70_product/tasks/` |
| **⑤ 日志** | 执行日志、反馈记录 | 复盘和迭代的基础 | KDO 的 `60_feedback/` |

### 搭建顺序

1. **先写系统自述**：一句话说清这个项目是干什么的 + 目录结构 + 技术栈
2. **再建领域知识**：把你脑子里关于这个项目的关键概念写下来，不会超过 20 条
3. **定义服务文档**：AI 需要做什么类型的任务？每种类型的标准流程是什么？
4. **任务管理**：每一个对话只围绕一个任务。任务有标题、状态、交付物
5. **日志**：AI 每次执行后记录关键信息——做了什么、遇到什么问题、产出什么

### 信息组织原则：按场景聚合，不按分类聚合

纪浩原话："你信息的聚合应该从场景进行聚合，而不是按照分类去进行聚合。"

错误做法（按分类）：设计规范/ → 组件文档/ → 品牌规范/——AI 做一个 UI 任务需要跨三个目录找信息。

正确做法（按场景）：UI设计/ 下面放所有跟 UI 设计相关的——规范 + 组件 + 品牌——AI 进入这个场景，一次拿到所有需要的。

## When to Use

- 开始一个新项目，需要 AI 持续参与
- AI 接手多个任务后出现混乱（干A干了B、流程走偏、重复犯错）
- 想让 AI 从"一次性工具"变成"持续协作者"

## When NOT to Use

- 一次性任务（问个问题就跑）——不需要 Workspace
- 项目还在探索方向，工作内容每周都在大改——这时搭 Workspace 是过度工程
- 你是唯一的 AI 使用者且只用它做简单任务

## Critique

### 内部局限

- **维护成本**：五个模块需要持续更新。经验模式库最容易膨胀——每次 AI 犯错都加一条，半年后可能变成几百条，AI 自己都看不过来
- **过度结构的风险**：有些工作流还没稳定，强行用五个模块的结构去套，可能反而限制灵活性
- **"导诊台"的正确性依赖人**：如果导诊台把任务分流错了方向，后续所有步骤都是错的——导诊台本身需要定期校准

### 外部攻击

#### David Weinberger 的"知识不需要结构"

**David Weinberger**（*Everything Is Miscellaneous* 作者，哈佛互联网与社会研究中心研究员）挑战了"结构化知识管理"的核心理念：

- **数字化时代的组织方式不是层级结构**：Weinberger 的核心论点是，在数字时代，信息的组织方式从"提前分类"（先建目录结构）转向了"事后搜索"（需要时搜索）。标签、全文搜索、链接比层级目录更适合大规模信息管理
- **五个模块是在模拟物理世界的文件柜**：系统自述/领域知识/服务文档/任务管理/日志——这五个模块本质上是五个文件夹。Weinberger 会说：如果 KDO 已经有了 Graph RAG 和语义搜索，为什么还要让 Agent 跨五个目录找信息？为什么不把信息打上标签，让 Agent 按需检索？
- **"按场景聚合"的前提是"你事先知道所有场景"**：纪浩的按场景组织信息，需要预测 AI 会遇到哪些场景。但复杂任务的场景是无法穷举的。当一个新的场景出现（比如"AI 需要同时参考电子工程和产品设计两套知识"），你的聚合结构就失效了——因为你不曾为这个交叉场景建过一个聚合目录

对纪浩体系的直接挑战：Weinberger 会说——**建 Agent Workspace 不如建一个好的检索系统。** 五个模块是给人看的目录结构，对 AI 来说，真正有用的是一个能理解任务上下文、自动聚合相关信息的检索层。KDO 的 Graph RAG 比五个文件夹更接近这个目标。

> **Weinberger 的拷问**："你花了两小时搭 Agent Workspace 的五个模块。三个月后，新来了一个完全不同的任务，需要的信息跨了两个模块、涉及你从未预料到的交叉领域——你的导诊台怎么处理？你的按场景聚合怎么覆盖这个新场景？如果你的回答是'重新组织信息'——那你在维护的不是一个 Workspace，是一个信息分类系统。这个系统的维护成本会被 AI 的使用频率放大。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|----|---|
| 上层框架 | [[concept-纪浩-ai-collaboration-methodology]] | L2——搭建 AI 的工作环境 |
| 配套技能 | [[skill-纪浩-progressive-disclosure]] | 渐进式披露是 Workspace 的信息组织方式 |
| 暗知识 | [[dk-纪浩-ai-cant-design-structure]] | "AI 不会自己搞结构设计"——这是 Workspace 存在的前提 |
| 暗知识 | [[dk-纪浩-pdca-starts-from-do]] | Workspace 不是一次搭完的——是在 Do-first PDCA 中迭代的 |
