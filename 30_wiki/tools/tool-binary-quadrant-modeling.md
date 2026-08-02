---
id: tool-binary-quadrant-modeling
title: 二分法/象限图建模法：用正交维度做分类与取舍
type: tool
aliases:
  - 二分法/象限图建模法
  - 二分法/象限图建模法：用正交维度做分类与取舍
  - 交维度做分类与取舍
  - 用正交维度做分类与取舍
  - 象限图建模法
source_refs:
- 10_raw/sources/src_20260614_73352fa5-Truman-高阶建模-抽象建模-常见模型武器库-图-01.md
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
- 10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md
status: reviewed
domain:
- src_unknown
- src_unknown
- src_unknown
quality_labels:
- actionable
- validated
created_at: '2026-06-14'
updated_at: '2026-06-28'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-18'
trust_level: medium
confidence: 0.91
related:
- '[[tool-动手建模法]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[tool-scenario-selector-modeling]]'
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- audience:executor
- scene:execution
- skill-level:intermediate
diagnostic_signals:
- framework_lens: binary-quadrant-modeling
  follow_up_question: 这个议题是否真的适合用两个离散维度分类？中间态/边界案例如何处理？
- framework_lens: binary-quadrant-modeling
  follow_up_question: 两个维度是否相对独立、可判断，且与决策直接相关？
- framework_lens: binary-quadrant-modeling
  follow_up_question: 每个象限是否对应了清晰且差异化的行动策略？
- 常见模型武器库
- 建模能力培训
- 抽象建模
---

# 二分法/象限图建模法：用正交维度做分类与取舍

> **Burn line**: 当你能把一群人分成两类，并让两类人各自得到不同的处理策略时，你就已经做了一个有用的模型。

二分法和象限图是分类建模的核心工具。二分法用一个关键维度把事物分成两类（如 P 型/L 型创业者、重要/紧急、内部/外部）；象限图用两个正交维度把事物分成四类（如重要-紧急矩阵、增长-壁垒矩阵）。一堂有大量象限图：ABCD 关键假设图、人生红点四大坐标图等。

---

## 用一句话讲清楚

用一个关键维度把事物切成两类，或用两个相对独立的维度画成 2×2 象限，让混沌集合变成可处理、可策略化的分类。

## 核心要点

1. **分类是为了差异化行动**，不是为了贴标签；每个类别必须对应明确策略。
2. **维度选择决定视野**：选错维度会漏掉关键信息，甚至把连续谱硬切成离散块。
3. **优先选择正交维度**：两个维度应相对独立，避免象限退化成一维。
4. **二分法是象限图的退化形式**：能用一个维度说清楚，就不必硬凑 2×2。
5. **用真实案例验证稳定性**：拿 5–10 个案例往里放，看分类是否稳定、策略是否一致。

## Visual Analysis

二分法通常表现为一条线或一个判断问题。象限图表现为一个 2×2 矩阵，横轴和纵轴各代表一个维度，四个象限代表四种策略或类型。两者的核心都是**通过维度切割，把混沌变成可处理的类别**。

---

## Claims

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Purpose

通过关键维度把复杂集合分类，让不同类型得到差异化策略，避免“一刀切”。

---

## Protocol

### 步骤 1：明确分类目的

你要解决什么问题？
- src_unknown
- src_unknown
- src_unknown

### 步骤 2：选择关键维度

维度必须：
- src_unknown
- src_unknown
- src_unknown

常见维度对：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 步骤 3：画象限/分两类

- src_unknown
- src_unknown
- src_unknown

### 步骤 4：为每个类别定义策略

分类不是目的，目的是差异化行动。每个象限/类别必须对应一个明确策略：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 步骤 5：用案例验证分类有效性

拿 5–10 个真实案例往象限里放：
- src_unknown
- src_unknown
- src_unknown

---

## 诊断信号

当你遇到以下情况时，考虑使用二分法或象限图：

| 信号 | 说明 |
|---|---|
| **一堆事物混在一起，难以决策** | 需要快速把复杂集合拆成可处理的子集 |
| **团队对“重点是什么”争执不下** | 把争论的维度可视化，转向“哪类优先做” |
| **需要为不同类型匹配不同策略** | 分类后能给每类明确差异化行动 |
| **战略取舍场景** | 资源有限，需要决定做/不做、先做/后做 |

---

## 失败模式

| 场景 | 为什么失效 | 替代方案 |
|---|---|---|
| **维度无法明确二分** | 事物是连续谱，强行二分会丢失中间态。 | 用段位图、演化图或连续坐标 |
| **两个维度高度相关** | 象限图退化成一维，失去分类价值。 | 重新选择独立维度 |
| **需要表达动态变化** | 象限图是静态快照，看不出迁移路径。 | 用演化图、曲线图、段位图 |
| **分类后策略没有差异** | 分类只是贴标签，没有指导行动。 | 回到目的，先定义要什么行动 |

---

## 边界

| 边界 | 说明 |
|------|------|
| **维度数量** | 二分法 1 维，象限图 2 维，超过 2 维用横纵表或雷达图 |
| **维度独立性** | 优先选择正交维度，避免冗余 |
| **行动导向** | 每个类别必须对应差异化策略 |
| **避免过度简化** | 复杂现实不是非黑即白，必要时应补充“中间态” |

---

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## [Critique]

### 内部局限性

- src_unknown
- src_unknown
- src_unknown

### 外部攻击：Karl Weick — "分类塑造所见"

**Karl Weick**（组织感知理论）会警告：你选择什么维度分类，就决定了你能看到什么。一个糟糕的象限图会把重要但难以归类的信息挤出视野。象限图的威力也是它的危险。

### 反事实测试

- src_unknown
- src_unknown

---

## 相关卡/互链

### 关联卡片

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 一堆事物混在一起，想快速分类 | 找一个最关键维度做二分 | 两类得到不同处理 |
| 需要做战略取舍 | 找两个关键维度画象限图 | 每个象限有明确策略 |
| 团队对“重点是什么”争执不下 | 把争论的维度可视化成分类 | 从“谁更重要”转向“哪类优先做” |

---

## Sources

- src_unknown
- src_unknown
- src_unknown

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）*

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？
