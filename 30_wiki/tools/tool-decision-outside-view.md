---
id: tool-decision-outside-view
title: 技能：团队决策外部视角法
type: tool
status: draft
domain:
  - decision-making
  - 团队
  - 噪声减少
source_person: 消化全库后提炼
source_context: 基于master-decision-hygiene框架提炼，2026-05-18
source_refs:
- src_unknown
wiki_refs:
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
- src_unknown
prerequisite_skills:
- src_unknown
created_at: 2026-06-11
updated_at: '2026-06-16'
reviewed_by: laowantong
author: unknown
confidence: 0.7
trust_level: low
related:
  - [[tool-decision-delay-intuition]]
  - [[pilot-atomic-chunk-comparison]]
  - [[master-decision-hygiene]]
  - [[tool-first-principles-assumption-classify]]
  - [[tool-cognitive-bias-12-check]]
---
# 技能：团队决策外部视角法

> **来源**：基于 master-decision-hygiene 框架提炼（Kahneman《噪声》）
> **核心**：团队对同一问题做判断时，先找历史基率，再独立评估，最后聚合——减少判断噪声。

---

## 原始表述
> "框架减少偏差但不减少噪声。同一个画布，分析师A估计'2%营收增长'，分析师B估计'0.5%'——这个差异不是偏差，是噪声。"
> —— Kahneman

---

## 操作步骤

### Step 1：分解判断（Break It Down）

把"这个项目能成吗？"拆成多个子判断：

```
分解维度（至少3个）：
1. 市场规模（1-10分）
2. 竞争强度（1-10分）
3. 团队能力（1-10分）
4. 资金需求（具体金额）
5. 执行风险（1-10分）

规则：每个维度给一个独立评分，禁止在分解前给出整体判断。
```

### Step 2：外部视角（Outside View）

在分析"这个特定案例"之前，先看"同类案例的历史统计"：

- src_unknown
- src_unknown
- src_unknown

**强制操作**：写出"我们的项目和同类案例的三个关键差异"，判断差异是否足以推翻基率。

### Step 3：独立评估（Independent Judgment）

每个人在**不知道别人答案**的情况下，独立填写：

```
独立评估表（每人一份）：
姓名：________
日期：________

1. 市场规模：___分
2. 竞争强度：___分
3. 团队能力：___分
4. 资金需求：___万
5. 执行风险：___分

整体判断：建议投资 / 不建议投资 / 不确定
理由：________________________

规则：提交前禁止讨论。讨论后需重新评估。
```

### Step 4：聚合（Aggregate）

汇总所有独立判断，用统计方法减少噪声：

| 判断类型 | 聚合方法 | 示例 |
|:---------|:---------|:-----|
| 数值估计 | 取**中位数**（比平均数更抗极端值） | 2%, 5%, 10% → 中位数5% |
| 是非判断 | 取**多数票** | 3人认为"该做"→"该做" |
| 排序判断 | 取**Borda计数** | 综合得分最高者胜出 |

**陷阱**：聚合前必须确保"独立性"——如果已经讨论过，评估已经失效，必须重新来过。

---

## 适用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

- src_unknown
- src_unknown
- src_unknown

---

## 为什么有效

**金句**：偏差是"枪总打偏"，噪声是"枪到处乱飞"。框架修的是"偏"，卫生修的是"散"。

独立评估的平均值比任何一个人的判断都更准确——这是"群体智慧"的数学基础。但前提是**独立性**——一旦你知道了别人的答案，你的判断会被锚定。

---

## 工具/环境

- src_unknown
- src_unknown
- src_unknown

---

| 失败现象 | 原因 | 解决方案 |
|---------|------|---------|
| 独立评估不独立 | 讨论前已经有人说了看法 | 物理隔离或匿名提交 |
| 外部视角被绕过 | "我们的项目不一样" | 强制写三个关键差异 |
| 聚合后忽视极端值 | 中位数丢失了关键信息 | 同时看"中位数"和"最极端的两个估计" |
| 基率过时 | 历史基率不适用于当前环境 | 评估基率的时效性 |
| 流程太复杂 | 团队不愿意执行 | 从"简化版"开始：只分解2个维度+只取中位数 |

---

## 关联技能

- src_unknown
- src_unknown
- src_unknown

---

## 来源

- src_unknown
- src_unknown

---

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
