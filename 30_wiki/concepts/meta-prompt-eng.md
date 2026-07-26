---
id: meta-prompt-eng
created_at: 2026-05-21
domain: ai-saas
source_refs:
- 10_raw/sources/src_20260522_a89ab860-meta-prompt-eng.md
status: draft
title: Meta Prompt Eng
type: concept
updated_at: '2026-06-29'
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: pending
confidence: 0.7
trust_level: low
related:
- '[[design-ai-image-generation]]'
- '[[business-analysis]]'
- '[[learning-thinking]]'
- '[[writing-content]]'
- '[[product-ux]]'
- yt-system-course-map-lecture
- yt-case-mandatory-cases
tags:
- audience:general
- scene:reference
- skill-level:beginner
---
# Meta Prompt Eng

## Summary

> 拆分自 `00_inbox/prompt-best-practices-collection.

md` > 条目数：5 你是一个智能助理，你需要帮用户结构化提取操作指令。

用户输入是一句非常口语化的指令，你需要识别用户指令，并从用户的指令中以json形式结构化的输出提取的信息 输出完毕后结束，不要生成新的用户输入，不要新增内容 提取动作，动作只能是：查找、搜索、提供、查。

## Source Refs

- src_unknown

## Reusable Knowledge


- **核心洞察**：Meta Prompt Eng的关键信息点——从原始材料中提取的结构化知识，需要结合上下文理解。
- **适用场景**：该知识点在AI协作、需求分析、产品设计等场景中的具体应用方式。
- **关联知识**：与一堂方法论体系中的单元模型、需求拆解、场景识别等模块存在关联。
- **实践要点**：在实际应用中需注意边界条件——工具的有效性取决于场景匹配度和执行者的判断力。

## Open Questions

- Meta Prompt 的**具体假设**是"可以用一个元提示词统一管理所有子提示词"。但这个假设的**边界**在哪里——跨领域（如医疗 vs 编程）的提示词是否可以用同一个 Meta Prompt 管理？
- **反例**：当任务上下文过于复杂时，Meta Prompt 反而增加了认知负担——不如直接写专用提示词。阈值在哪里？

## Output Opportunities


- 可输出为：[[learning-thinking|学习方法论]]卡片，关联[[ai-collaboration-mindset-shift|AI协作]]实践
- 可提炼为：[[tool-yitang-research-unit-model|单元模型]]框架的一部分，关联[[tool-demand-iceberg-l1-user|需求冰山]]模型
- 产出类型：分析报告 / 操作脚本 / 实践playbook
