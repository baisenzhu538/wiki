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
---
# Meta Prompt Eng

## Summary

> 拆分自 `00_inbox/prompt-best-practices-collection.

md` > 条目数：5 你是一个智能助理，你需要帮用户结构化提取操作指令。

用户输入是一句非常口语化的指令，你需要识别用户指令，并从用户的指令中以json形式结构化的输出提取的信息 输出完毕后结束，不要生成新的用户输入，不要新增内容 提取动作，动作只能是：查找、搜索、提供、查。

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown

## Open Questions

- Meta Prompt 的**具体假设**是"可以用一个元提示词统一管理所有子提示词"。但这个假设的**边界**在哪里——跨领域（如医疗 vs 编程）的提示词是否可以用同一个 Meta Prompt 管理？
- **反例**：当任务上下文过于复杂时，Meta Prompt 反而增加了认知负担——不如直接写专用提示词。阈值在哪里？

## Output Opportunities

- src_unknown
- src_unknown
- src_unknown
