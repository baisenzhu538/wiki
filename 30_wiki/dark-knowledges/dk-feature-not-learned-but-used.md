---
id: dk-feature-not-learned-but-used
title: 「暗知识：Feature不是学会的，是用会的」
type: dk
status: draft
confidence: 0.92
trust_level: high
domain:
  - ai-basic
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
source_person: Truman
source_context: Truman口述下 L816-858
reviewed_by: 待审
aliases:
  - Feature不是学会的
  - 用会的
  - 技巧派
discoverable_by:
  - Feature不是学会的
  - 用会的
  - 技巧派
related:
  - framework-truman-feature-thinking-core
  - concept-truman-feature-six-stages
  - framework-一堂-关键假设
  - dk-demand-feature-stacking
  - dk-key-hypothesis-still-hope
tags:
  - method:learning
  - scene:ai-learning
  - audience:general
  - content-format:dk
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - quotable
  - cited
diagnostic_signals:
  - signal: "学了很多Feature但实际用AI时还是老样子"
    lens: 停在"理解"阶段——理解≠会用
    follow_up: 强制：本周内选1个Feature，在3个不同场景中真实使用并记录效果
---

> 本卡属于 [[concept-truman-feature-six-stages]] 的暗知识——六阶段的真相：大多数人停在第2阶段。

# Feature不是学会的，是用会的

> 一句话："你如果没有真正做出来过，你连实验都没做出来过——这个Feature对你来讲价值很低。把武器库当技巧合集=我们最不想教的那个东西。"（口述下L834-838）

---

## 原始表述

Truman（口述下 L816-858）：

> "Feature不是学会的，它是用会的。你如果没有填，你不知道说这个Feature在这类项目上有效，你没有真正做出来过，你连实验都没做出来过——这个Feature对你来讲价值很低。本身一份给大家的武器库清单本身没有太高的价值。如果你把我们的武器库当成一个所谓的技巧合集，那刚好又是我们最不想教的那个东西。你把Feature的那个框架退化成了另外一个技巧派。"

---

## 使用场景

| 场景 | 典型症状 |
|:---|:---|
| 听完课但没动手 | "我都听懂了"——但一次都没在真实项目里用过 |
| 建了Feature库但从来不用 | Feature库变成"收藏夹"——存了很多，从不调用 |
| 用了但只在舒适区用 | 同一个Feature在同类任务中反复用——没有边界测试 |

## 操作方法

### 验证一个Feature你真的"会了"

1. 选一个Feature——比如"最终意图"
2. 在3个**不同类型的**项目中真实使用（不是练习，是生产环境）
3. 记录每次的效果——成功了吗？为什么成功/失败？
4. 如果3次都成功→到"内核"阶段；如果至少1次失败且你知道为什么→到"边界"阶段

### 防技巧派退化

每次学新Feature时问自己：如果不看周期表，我能独立说出这个Feature是什么、怎么用、什么时候失效吗？

---

## 适用边界

| 场景 | 适用？ |
|:---|:---|
| 理论型学习（了解概念） | ❌ 不需要实操验证 |
| 实操型学习（解决问题） | ✅ 核心场景 |

## 为什么值钱

它回答了"为什么学了那么多AI课还是不会用AI"——因为你把Feature当知识学了，没当技能练。Feature和游泳一样：你可以在岸上学会所有理论，下水还是会呛。

## 教育哲学：不给新人直接上建模工具

Truman内部讨论（口述下L1664-1676）：

> "我们内部有个同学非常明确地说别给新人上建模工具。当大家自己对于模型还没有基本判断审美的时候，上了就用，可能这辈子他都不会再学了。如果从一开始动手你们就没有自己拆过那些组件节点，你们上来就用，根本没有判断力。那个所谓的成长反馈摩擦力都是AI承担，进步空间全被AI吃掉了。"

**不给新人的不是工具，是剥夺练习机会的捷径。** Feature思维的核心矛盾：Feature让你更高效——但"太早高效"可能扼杀基本功。

## 与其他知识的关联

- `[[concept-truman-feature-six-stages]]`：六阶段=从"学会"到"用会"的量化路径
- `[[dk-demand-feature-stacking]]`：那个讲组合失败，这个讲学习失败
- `[[concept-一堂-基本功-刻意练习四要素]]`：Feature=刻意练习的最小单位

## Critique

"不是学会的是用会的"这个表述可能过度贬低理论学习——对于完全零基础的人，先"理解"概念再"尝试"是必要的。Truman本人也是先理解了"温度参数"的概念，才去调参数的。更准确的说法是：理解是必要但不充分——只理解不用=没学会。

## 常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 只听课不实操 | 学了10个Feature，0个真正用过 | 强制：每学1个Feature必须在1周内真实使用 |
| 把清单当学会 | Feature库建得很漂亮——但一条都没验证过 | 库里的每个条目必须标注"用过几次/效果如何" |
| 无项目验证 | 只在练习环境用——不知道生产环境的真实效果 | 至少1次生产环境验证 |
