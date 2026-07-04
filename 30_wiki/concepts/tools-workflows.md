---
id: tools-workflows
created_at: 2026-05-21
domain: healthcare
source_refs:
- 10_raw/sources/src_20260522_9d322e81-tools-workflows.md
status: enriched
title: Tools Workflows
type: concept
updated_at: '2026-06-29'
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
related:
- '[[yt-panproduct-execution-good-tools]]'
- '[[tool-yitang-weapon-ai-tools]]'
- '[[yt-unit-model-three-tools]]'
- '[[yt-personal-pan-product-tools]]'
- '[[tool-lean-leverage-tools]]'
- '[[ai-methodology-tools]]'
- yt-system-course-map-lecture
---
# Tools Workflows

## Summary

> 拆分自 `00_inbox/prompt-best-practices-collection.

md` > 条目数：9 https://promptpilot.

volcengine.

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Open Questions

- 6 种 prompt archetype 中，哪些在中文场景下需要调整具体假设？
- Coze 工作流的三阶段确认协议在边界情况下（用户沉默、部分修改）如何处理？
- GEO 医疗内容适配的前提条件是什么——是否需要领域专家审核？
- "善用佳软"精确匹配框架的反例：什么场景下工具匹配反而不如自由选择？
- 超级角色选角的适用边界——多轮对话中角色一致性如何保证？
- 客服 AI 的关键假设：用户意图分类的准确率达到多少才可用？
- 提示词模式选择的决策树前提——是否假设用户已具备基本的 prompt engineering 知识？
- 工具层策略与其他 5 种模式的关联：是否存在互斥场景？

## Output Opportunities

Content: <article: "Prompt Engineering Pattern Library" — cataloging the 6 reusable prompt archetypes from the source (inspiration flash, GEO adaptation, customer service AI, super-character casting, Coze workflow design, tool-layer strategy) with cross-references to the "善用佳软" precision-matching framework, plus a decision tree for selecting the right pattern based on task type, output format, and verification requirements>
Code: <script: "Coze Workflow Stage-Gate Validator" — automates the three-phase confirmation protocol from the source, with built-in handling for edge cases (silence, partial modification, ambiguous response) that the source leaves undefined, integrating the "必须获得用户明确肯定" constraint with timeout/escalation logic>
Capability: <workflow: "AI Content Adaptation Safety Protocol" — addresses the open question about GEO medical content risk by adding a mandatory "Accuracy Verification Gate" before any health/science GEO adaptation, with role-based sign-off (domain expert + legal review) and provenance tracking for source claims>
