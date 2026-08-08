---
id: concept-truman-feature-four-scenarios
title: 「概念：Feature四大应用场景——解题地图·调优·练习·坐标系」
type: concept
status: draft
confidence: 0.90
trust_level: high
domain:
  - ai-basic
  - methodology
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
source_person: Truman
source_context: Truman口述下 L80-110（四场景矩阵）
reviewed_by: 待审
aliases:
  - 四场景
  - 解题地图
  - 无限调优
  - 共同坐标系
discoverable_by:
  - 四场景
  - 解题地图
  - 无限调优
  - 刻意练习
  - 共同坐标系
related:
  - framework-truman-feature-thinking-core
  - framework-truman-feature-layered-system
  - concept-truman-feature-six-stages
  - framework-一堂-关键假设
  - concept-一堂-基本功-刻意练习四要素
tags:
  - method:feature-thinking
  - method:application
  - scene:ai-learning
  - audience:general
  - content-format:concept
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - actionable
  - cited
diagnostic_signals:
  - signal: "Feature库建了但不知道什么时候用哪个Feature"
    lens: 缺场景匹配——四场景帮你在不同情境下选择不同Feature策略
    follow_up: 定位当前场景（短期事/长期事/短期人/长期人）→匹配对应象限的Feature策略
---

> 本卡属于AI基本功域——Feature思维四大应用场景。与 `[[concept-truman-feature-six-stages]]`（刻意练习的六阶段路径）互补。

# Feature四大应用场景：解题地图·调优·练习·坐标系

> 一句话：Feature不只是"学习对象"——它在你做新项目、优化旧项目、训练自己、对齐团队四个场景中扮演四种角色。

---

## 四场景矩阵

```
          短期              长期
  事  ┌──────────┬──────────┐
      │ 解题地图  │ 无限调优  │
      │ 提假设    │ 螺旋上升  │
      ├──────────┼──────────┤
  人  │ 刻意练习  │ 共同坐标系 │
      │ 拆小练    │ 通用语言  │
      └──────────┴──────────┘
```

### 左上：解题地图（事×短期）

**场景**：接手一个新AI项目，不知道从哪下手。

**Feature的角色**：像点菜一样从周期表中挑5-10个Feature提假设→做实验→复盘。

> "你们不需要额外学什么SWOT、Omega模型——只要用Feature思维讨论问题，自然就科学了。"（口述下L130-132）

**KDO映射**：王语嫣诊断素材→从卡片库选相关卡→生产

### 右上：无限调优（事×长期）

**场景**：项目卡住了，加功能加参数都没用，准备放弃。

**Feature的角色**：一个Feature没效果就换另一个——源源不断的假设让你永远有牌可出。

> 作图工作流：提示词60分→+换模型+版本管理→+抽卡+Skill+Agent分工→成功率50-70%（口述下L472-552）

**KDO映射**：编排迭代——诊断→生产→反馈→改进→再诊断

### 左下：刻意练习（人×短期）

**场景**：想提升AI能力但不知道怎么练。

**Feature的角色**：每个Feature是可练习的最小单位——"最终意图"一天可以练十次。

> "Feature不是学会的，是用会的。"（口述下L816-858）

**KDO映射**：技能进化日志——每次会话加一行

### 右下：共同坐标系（人×长期）

**场景**：产品/技术/运营对AI的理解各说各话。

**Feature的角色**：Feature是跨岗位通用语言——"向所有人兼容"（口述下L980-1034）。

> "技术说'RAG'、产品说'让AI知道我们的产品信息'、运营说'给AI喂资料'——说的是同一个Feature：上下文增强。"（⚠️ 演绎示例，非口述原文）

**KDO映射**：Agent编排——不同角色Agent用同一套Feature语言协作

## AI推平均分的警示

Truman（口述下L1650）：

> "AI会把所有人都推向平均分。"

刻意练习象限的深层动因：如果不刻意练Feature，AI会把你拉到"所有人的平均水平"——不高不低、不差也不好。刻意练习的目的不是"学会AI"，是在AI推平所有人的时候，你还能保持差异化优势。

## When NOT to Use
- 临时性团队（不会长期协作，共同坐标系价值低）
- 团队成员AI水平差异过大（需要先拉到L2基线）

## Critique
Truman讲的"向所有人兼容"依赖团队有一个"翻译者"角色——掌握Feature框架的人把不同角色语言翻译成Feature。如果团队没有这个人，Feature仍然会是各说各话。
