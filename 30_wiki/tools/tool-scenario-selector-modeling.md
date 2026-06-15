---
id: tool-scenario-selector-modeling
title: 场景→工具选择器：根据需求快速匹配合适的建模工具
type: tool
source_refs:
- src_20260614_73352fa5
- src_20260614_8269ccdb
- src_20260614_42f1e977
status: draft
domain:
- yitang
- product
- ai-collaboration
created_at: '2026-06-14'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
review_date: '2026-06-14'
trust_level: medium
confidence: 0.75
related:
- '[[modeling-weapon-library]]'
- '[[tool-canvas-weapon-library-modeling]]'
- '[[modeling-three-stages]]'
- '[[modeling-level-map]]'
tags:
- '#method/modeling'
- '#content-format/concept-card'
- '#selector'
- '#scenario'
- '#decision-support'
---
# 场景→工具选择器：根据需求快速匹配合适的建模工具

> **Burn line**: 先问“我要解决什么问题”，再问“哪个工具最合适”。

这是本批建模能力卡片的“入口工具”。用户（包括未来的你）描述一个场景或需求时，可以用这个选择器快速定位到合适的建模工具卡。它把“常见模型武器库”从静态目录变成动态匹配系统。

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

- `10_raw/assets/modeling-capability/Truman-高阶建模-抽象建模-常见模型武器库-图-01.png`
- `src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md`
- `src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md:58-66`

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）*
