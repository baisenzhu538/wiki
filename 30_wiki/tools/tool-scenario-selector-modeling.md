---


id: tool-scenario-selector-modeling
title: 场景→工具选择器：根据需求快速匹配合适的建模工具
type: tool
source_refs:
  - 10_raw/sources/src_20260614_73352fa5-Truman-高阶建模-抽象建模-常见模型武器库-图-01.md
  - 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
  - 10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md
status: enriched
domain:
- yitang
- product
- ai-collaboration
created_at: '2026-06-14'
updated_at: '2026-06-17'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-17'
trust_level: high
confidence: 0.90
related:
  - '[[dk-modeling-explanatory-vs-predictive-essence]]'
  - '[[case-modeling-essence-schools]]'
  - '[[dk-modeling-question-scaffold-not-answer]]'
  - '[[dk-tool-as-answer-trap]]'
  - '[[dk-modeling-unit-pairs-milestone]]'
  - '[[modeling-weapon-library]]'
  - '[[tool-canvas-weapon-library-modeling]]'
  - '[[modeling-three-stages]]'
  - '[[modeling-level-map]]'
tags:
- '#method/modeling'
- '#content-format/concept-card'
- '#method/decision-framework'
- '#chunk-type/use-case'
diagnostic_signals:
- signal: 用户说"工具太多，我不知道该用哪个"
  framework_lens: 场景→工具选择器
  follow_up_question: 你要解决的是筛选、分类、排序、诊断、设计还是执行问题？
- signal: 用户描述一个场景后直接问"这个该用什么模型"
  framework_lens: 场景→工具选择器
  follow_up_question: 能否用一句话说明你要解决什么问题，以及有哪些可选对象或约束？
- signal: 用户在雷达图和象限图之间犹豫
  framework_lens: 场景→工具选择器
  follow_up_question: 你的重点是"评估多个选项"还是"按两个维度分类并配策略"？
- signal: 用户想系统梳理一个复杂主题但无从下手
  framework_lens: 设计/规划 → 画布/武器库
  follow_up_question: 这个主题的关键维度是否已知？是否需要一个完整扫描框架？
- signal: 团队对"该用什么方法"争执不下
  framework_lens: 场景→工具选择器
  follow_up_question: 大家是否先对问题类型和前提条件（数据、共识、可干预性、ROI）达成了一致？
- signal: 用户把一个工具套用到明显不匹配的场景
  framework_lens: 场景→工具选择器
  follow_up_question: 你是因为这个工具顺手，还是因为它真的适合当前问题？
---
# 场景→工具选择器：根据需求快速匹配合适的建模工具

> **Burn line**: 先问“我要解决什么问题”，再问“哪个工具最合适”。

## 用一句话讲清楚

场景→工具选择器是建模武器库的**动态入口**：先把问题归入筛选/评估、分类/取舍、排序/优先级、诊断/复盘、设计/规划、执行/固化六大场景，再按子问题推荐 1–2 个候选建模工具，并检查数据、共识、可干预性、ROI 四个前提，从而降低“在武器库里盲目翻找”的选择成本。

---

## 核心要点

- **问题先于工具**：选择器的第一步永远是澄清“我要解决什么问题”，而不是“我想用什么工具”。
- **六大场景覆盖多数建模需求**：筛选/评估、分类/取舍、排序/优先级、诊断/复盘、设计/规划、执行/固化。
- **子问题是第二级过滤器**：同一类场景下，子问题不同，推荐工具也不同。
- **推荐工具 + 备选工具**：每个子问题给出主工具和备选工具，方便根据资源或数据条件调整。
- **四个前提条件**：数据是否足够、团队对维度是否有共识、输出能否导出行动、使用成本是否小于收益。
- **复杂场景需要组合**：诊断类问题常常需要“漏斗图 + 冰山图”，设计类问题可能需要“画布 + 本质建模”。
- **选择器是经验规则，不是算法**：边界案例可能匹配不准，需要结合判断和验证。

---

## Purpose

降低建模工具的选择成本。当你面对一个具体场景时，先通过选择器锁定 1–2 个最合适的工具，再深入阅读对应的 tool 卡，避免在武器库里盲目翻找。

---

## Protocol

### Step 1：明确你的场景类型

从下面 6 个高频场景类型中选择最接近的一个：
1. **筛选/评估** —— 要从多个选项中挑一个
2. **分类/取舍** —— 要把一堆事物分组并制定不同策略
3. **排序/优先级** —— 事情太多，要决定先做哪个
4. **诊断/复盘** —— 出了问题，要找根本原因
5. **设计/规划** —— 要设计一个系统、产品或个人发展路径
6. **执行/固化** —— 要把关键动作稳定执行

### Step 2：根据子问题选择工具

| 场景 | 子问题 | 推荐工具 | 备选工具 |
|------|--------|---------|---------|
| **筛选/评估** | 多维度比较几个选项 | [[tool-radar-chart-modeling]] | [[tool-binary-quadrant-modeling]] |
| **筛选/评估** | 量化业务流程中的损耗点 | [[tool-funnel-formula-modeling]] | [[tool-radar-chart-modeling]] |
| **分类/取舍** | 用一个关键维度二分 | [[tool-binary-quadrant-modeling]] | [[tool-sabc-tier-modeling]] |
| **分类/取舍** | 用两个维度四分类并配策略 | [[tool-binary-quadrant-modeling]] | [[tool-canvas-weapon-library-modeling]] |
| **排序/优先级** | 任务太多，强制排优先级 | [[tool-sabc-tier-modeling]] | [[tool-checklist-cheatsheet-modeling]] |
| **排序/优先级** | 给能力/业务水平分级 | [[tool-sabc-tier-modeling]] | [[modeling-level-map]] |
| **诊断/复盘** | 从表象深挖根本原因 | [[tool-iceberg-triangle-modeling]] | [[tool-essence-nfactor-modeling]] |
| **诊断/复盘** | 找系统的三个核心支撑要素 | [[tool-iceberg-triangle-modeling]] | [[tool-essence-nfactor-modeling]] |
| **设计/规划** | 完整扫描一个复杂主题 | [[tool-canvas-weapon-library-modeling]] | [[tool-essence-nfactor-modeling]] |
| **设计/规划** | 提炼核心变量并预测 | [[tool-essence-nfactor-modeling]] | [[tool-iceberg-triangle-modeling]] |
| **执行/固化** | 把步骤变成可检查清单 | [[tool-checklist-cheatsheet-modeling]] | [[tool-sop-template-modeling]] |
| **执行/固化** | 把关键动作变成标准流程 | [[tool-sop-template-modeling]] | [[tool-checklist-cheatsheet-modeling]] |
| **执行/固化** | 建立快速可调用的工具库 | [[tool-canvas-weapon-library-modeling]] | [[modeling-weapon-library]] |

### Step 3：检查前提条件

每个工具都有前提：
- **数据**：是否有足够事实/数据？
- **共识**：团队对维度/标准是否有共识？
- **可干预性**：工具输出能否导出具体行动？
- **ROI**：使用这个工具的收益是否大于成本？

如果某个前提不满足，先回到更基础的工具（如案例包、清单）积累事实。

---

## Quick Decision Tree

```
你要解决什么问题？
├── 要从多个选项中挑一个/排优先级
│   ├── 有明确量化数据 → 漏斗图/公式
│   ├── 多维度主观评估 → 雷达图
│   └── 任务太多要取舍 → SABC分级
├── 要把事物分类并制定策略
│   ├── 一个关键维度 → 二分法
│   └── 两个关键维度 → 象限图
├── 要找根本原因/核心变量
│   ├── 从表象逐层下挖 → 冰山图
│   ├── 三个核心要素支撑 → 三角图
│   └── 提炼 N 个不可或缺变量 → N要素/本质
├── 要完整设计/规划一个系统
│   ├── 需要扫描所有维度 → 画布
│   ├── 要抓核心本质 → 本质/N要素
│   └── 要建立长期成长路径 → 段位图
└── 要把动作稳定执行
    ├── 简单检查点 → 清单/小抄
    ├── 标准流程 → SOP/模板
    └── 需要匹配多种工具 → 武器库
```

---

## Complexity vs. Tool Mapping

| 模型难度 | 适用工具 | 何时升级 |
|---------|---------|---------|
| **基础** | 案例包、清单、SOP/模板、画布/武器库 | 问题重复出现，需要更系统解释 |
| **进阶** | 雷达图、N要素、逻辑链、漏斗图、公式、二分法、象限图、横纵表、SABC分级、段位图、演化图 | 基础工具无法解释差异，需要找规律 |
| **深度** | 三角图、冰山图、圈层图、三环图、曲线图、火箭图、本质/N要素、花瓣图、字母图、卡牌 | 需要洞察、预测、抓本质 |

---

## Example Queries

| 用户场景 | 推荐工具 | 原因 |
|---------|---------|------|
| "我要从 5 个选题中选一个做视频" | [[tool-radar-chart-modeling]] | 多维度评估选题 |
| "我要给团队的能力排个级" | [[tool-sabc-tier-modeling]] + [[modeling-level-map]] | 分级+参考段位 |
| "直播总是翻车，不知道哪里有问题" | [[tool-funnel-formula-modeling]] + [[tool-iceberg-triangle-modeling]] | 量化损耗+深挖根因 |
| "我想系统梳理我的商业模式" | [[tool-canvas-weapon-library-modeling]] | 完整扫描商业画布 |
| "我要把成功经验固化下来" | [[tool-sop-template-modeling]] | 流程化 |
| "我不知道一堂到底是做什么的" | [[tool-essence-nfactor-modeling]] | 本质建模 |

---

## When NOT to Use

| 场景 | 为什么失效 | 替代方案 |
|---|---|---|
| **问题描述模糊** | 选择器需要明确场景类型。 | 先用 5W1H 或访谈澄清问题 |
| **没有事实基础** | 再合适的工具也建不出好模型。 | 先做案例包，收集数据 |
| **追求工具而忽略问题** | 不要为了用某个工具而扭曲问题。 | 回到问题本身，选择最朴素的方法 |

---

## 边界

| 边界 | 说明 |
|------|------|
| **适用前提** | 问题已被描述到可以归入六大场景之一；过于模糊的问题需先澄清 |
| **数据依赖** | 选择器只推荐工具，不替代事实收集；数据不足时推荐会失效 |
| **共识依赖** | 如果团队对维度/标准没有共识，推荐工具后仍需先对齐 |
| **工具粒度** | 推荐的是“入口工具”，复杂问题通常需要组合 2–3 个工具 |
| **动态维护** | 随着新工具加入和旧工具淘汰，选择器需要定期更新匹配规则 |
| **经验而非算法** | 边界案例可能匹配不准，最终需结合人的判断和验证 |

---

## 失败模式

| 失败模式 | 典型症状 | 根因 | 修复动作 |
|---------|---------|------|---------|
| **问题不清就硬选工具** | 场景类型反复跳转，无法锁定工具 | 跳过了“用一句话说明问题”和场景归类 | 回到 Step 1，用 5W1H 或访谈澄清问题 |
| **忽视前提条件** | 选中的工具无法落地或产出空泛 | 数据/共识/可干预性/ROI 不满足 | 先补数据、对齐共识，或降级到更基础工具 |
| **把推荐当唯一答案** | 无论场景多复杂都只用一个工具 | 误解选择器的定位 | 复杂场景主动组合 2–3 个工具 |
| **为了顺手而扭曲问题** | 问题明明适合 A 工具，却强行用 B 工具 | 对某个工具有路径依赖 | 回到问题本身，用选择器重新匹配 |
| **选择器长期不更新** | 推荐工具库与实际工具卡脱节 | 新增/淘汰工具后未同步选择器 | 建立定期 review 机制，每新增工具就更新匹配规则 |
| **边界案例硬套规则** | 某个场景同时匹配多个工具，团队争执不下 | 场景描述不够具体 | 进一步拆解子问题，或用反事实测试比较不同工具 |

---

## 行动 Checklist

- [ ] 已用一句话清晰描述要解决的问题
- [ ] 已从六大场景类型中定位最接近的一类
- [ ] 已根据子问题找到推荐工具及备选工具
- [ ] 已检查数据、共识、可干预性、ROI 四个前提
- [ ] 已判断当前场景需要单一工具还是组合工具
- [ ] 已打开对应 tool 卡交叉验证推荐是否合适
- [ ] 已记录选择理由、预期输出和成功指标
- [ ] 使用后将结果和偏差回灌，用于迭代选择器

---

## 相关卡/互链

- [[modeling-weapon-library]] —— 一堂常见模型武器库总览与难度分层
- [[tool-canvas-weapon-library-modeling]] —— 武器库的具体构建方法
- [[modeling-three-stages]] —— 按建模阶段（基础/进阶/深度）选择工具
- [[modeling-level-map]] —— 按能力段位选择工具复杂度

---

## [Critique]

### 内部局限性

- 选择器是经验规则，不是算法，边界案例可能匹配不准
- 工具选择依赖对问题的准确描述
- 复杂场景通常需要组合多个工具

### 外部攻击：Karl Weick — "分类塑造所见"

**Karl Weick** 会警告：在复杂情境中，问题本身是不确定的。先用工具选择器可能过早锁定问题框架，忽略了真正的问题是什么。有时候，花更多时间“框定问题”比“选择工具”更重要。

### 反事实测试

- 如果一个问题同时适合雷达图和象限图，怎么选？看重点是“评估选项”还是“分类策略”。
- 如果用户说不清楚场景，选择器如何引导？用决策树逐步缩小范围。

---

## [Synthesis]

### 关联卡片

- [[modeling-weapon-library]] —— 工具总览和难度分层
- [[tool-canvas-weapon-library-modeling]] —— 武器库的具体构建方法
- [[modeling-three-stages]] —— 按建模阶段选择工具
- [[modeling-level-map]] —— 按能力段位选择工具复杂度

---

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 用户描述一个场景，问用什么工具 | 用本选择器匹配 1–2 个候选工具 | 用户能说出为什么选这个工具 |
| 不确定场景类型 | 用 6 大场景类型做初步分类 | 明确归属 |
| 复杂场景 | 推荐工具组合 | 覆盖评估、诊断、执行多个层面 |

---

## Sources

### 原始素材

- 10_raw/sources/src_20260614_73352fa5-Truman-高阶建模-抽象建模-常见模型武器库-图-01.md` — 常见模型武器库原图摘要
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md` — 建模能力培训口述稿
- 10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md` — 建模能力培训笔记

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）*
