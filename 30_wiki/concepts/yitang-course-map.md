---
title: 一堂课程大地图
type: concept
subtype: hub
domain:
- yitang
status: stable
created_at: 2026-05-06
updated_at: '2026-06-16'
id: yitang-course-map
tags: []
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: medium
source_refs:
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
source_context: （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
---
# 一堂课程大地图

> Dataview 驱动的课程列表页。方法论框架和体系解读见 30_wiki/systems/一堂方法论体系总图|一堂方法论体系总图（权威 Hub）。

!

## 按地图浏览

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "personal"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "management"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "entrepreneur"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "infinite"
SORT yitang.module ASC, file.name ASC
```

## 全部课程卡片

```dataview
TABLE yitang.map AS "地图", yitang.module AS "模块", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang
SORT yitang.map ASC, yitang.module ASC, file.name ASC
```

## 相关页面

- 30_wiki/systems/一堂方法论体系总图|一堂方法论体系总图 — 权威方法论 Hub，含四张地图详解、十层解读、学习路径
- 30_wiki/entities/一堂|一堂实体页 — 公司背景与方法论总览
- yt-system-course-map-lecture|一堂课程地图精华串讲 — 2025 开学第一课转录
- 一堂调研武器库13招 — 调研方法论武器库
- 一堂调研行动营-ai辅助系统式调研方法论 — AI 协同调研范式
## Critique

#### Nassim Taleb — 过度结构化与黑天鹅风险

**Nassim Taleb** (《反脆弱性》《黑天鹅》作者) 对任何"将复杂现实编码为结构化框架"的尝试都持深切怀疑。他的核心论点：**我们过度估计了我们能理解的东西，而低估了我们理解不了的东西。** 任何模板、框架或方法论都是一种"确定性幻觉"——它们假设未来会像过去一样发展，忽视了那些不可预测、不可分类、不可量化的黑天鹅事件。

> **为什么应该让你睡不着**：如果你正在依赖这张卡片做出关键决策，你已经在暗中排除了那些不可被编码为"步骤"的风险。这些"残留风险"不在框架内，但它们可能在一夜之间彻底改变一切。

#### Herbert Simon — 有限理性与认知超载

**Herbert Simon** (诺贝尔经济学奖得主、"有限理性"理论提出者) 从认知科学角度攻击：人类决策者的大脑处理信息的能力是有限的——复杂框架要求同时综合考虑多个维度，这对人类的工作记忆来说是超载的。

> **为什么应该让你睡不着**：如果这张卡片的使用者无法在一次会议中保持全部维度的逻辑一致性，那么它的产出就是多个独立假设而非一个综合分析。这种"分裂式分析"会让团队产生"每个维度都对但整体不对"的错觉。

### 内部局限

## Synthesis

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
| 在无专业背景的情况下做出重大决策 | 框架是信息输入，不是决策代理 | 结合自身业务场景做二次判断 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份框架/方法做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
| 结构化分析后感觉"都对但整体不对" | 停下来检查是否忽视了框架之外的因素——团队、时机、技术债务 | 能指出至少一个被框架排除但实际影响很大的因素 |
| 使用过程中感到信息过载 | 不要一次性尝试应用整个框架——选择其中一个最直接相关的模块先用 | 在一个具体项目中成功应用了≥1个模块 |
