---
id: case-truman-sales-report-structure
title: 案例：Truman 重构销售失利汇报——把 10 个散点升级成逻辑链
type: case
status: draft
problem_domains: &id001
- 工作汇报
- 复盘结构化
industry: 通用
scale: 团队
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
source_refs:
- src_20260614_8269ccdb
wiki_refs:
- '[[dk-modeling-checklist-formatting-rules]]'
definition_of_done:
- 问题描述清晰
- 方案可理解
- 可迁移点明确
tags:
- '#case'
- '#problem/reporting'
- '#source/truman'
related_skills:
- '[[dk-modeling-checklist-formatting-rules]]'
related_concepts:
- '[[dk-modeling-logical-cleanliness-root]]'
related_cases: []
created_at: '2026-06-15'
updated_at: '2026-06-15'
author: 老顽童
reviewed_by: pending
confidence: 0.8
trust_level: medium
domain: *id001
---

# 案例：Truman 重构销售失利汇报——把 10 个散点升级成逻辑链

## 原始表述

> 我真的见过下属连换行都不给我加的，就长成这样的一个一大坨给我……如果做成优先级，这是 P0 的三个，这是 P1 的三个，这是 P2 的三个，有没有好一点？……如果有一个完整的逻辑顺序，就是输入的部分，然后旧的是怎么样，新的是怎么样的，这个处理的部分……每个人都可以找到自己的位置，每个人都知道自己可能谁依赖谁。

## 问题

下属汇报销售失利经验时，把内容写成“一大坨”或不排序的 10 个要点。领导既无法判断遗漏，也无法决策；团队也看不清各因素之间的依赖关系。

## 方案

用逻辑洁癖把汇报从 L1/L2 升级到 L3/L4/L5：

1. **排优先级**：把 10 个点分成 P0/P1/P2；
2. **MECE 拆分**：按“总分总 + 问题与机会 + 输入信息 + 讨论定位 + 决策 + 链条回顾”重新组织；
3. **形成逻辑链**：用“输入 → 优化空间 → 处理 → 输出”的严格顺序表达因果关系；
4. **显性化依赖**：让团队每个人都知道自己处在链条的哪一环。

## 结果

- 汇报从 **10 个无序点**变成有优先级、有结构、有推理关系的模型；
- 团队能看清“谁依赖谁”，每个人都能在链条中找到自己的位置；
- 输入质量差 → 处理差 → 输出差的因果链被显性化；
- 负责人“动过脑子”的程度一眼可见。

## 可迁移

- 任何复盘/汇报不要停留在“清单”，而要追问优先级、MECE、逻辑链；
- L5 级的表达能把团队从“信息罗列”推进到“可行动的推理”；
- 这是训练团队逻辑洁癖最直接的工作场景。

## 关键标签

- 问题域：工作汇报、复盘结构化
- 行业：通用
- 方法：优先级、MECE、逻辑链

## 关联

- 技能：[[dk-modeling-checklist-formatting-rules]]
- 概念：[[dk-modeling-logical-cleanliness-root]]
- 案例：无

## 来源

- Truman，一堂建模能力培训，2026-06-12，`src_20260614_8269ccdb#990-1074`
