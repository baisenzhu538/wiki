---
id: "meta-prompt-eng"
created_at: 2026-05-21
domain:
  - "ai-saas"
source_refs:
  - "src_20260522_a89ab860"
status: "draft"
title: "Meta Prompt Eng"
type: "concept"
updated_at: 2026-05-21
tags:
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#scene/note-taking/checklist-method"
---

# Meta Prompt Eng

## Summary

> 拆分自 `00_inbox/prompt-best-practices-collection.

md` > 条目数：5 你是一个智能助理，你需要帮用户结构化提取操作指令。

用户输入是一句非常口语化的指令，你需要识别用户指令，并从用户的指令中以json形式结构化的输出提取的信息 输出完毕后结束，不要生成新的用户输入，不要新增内容 提取动作，动作只能是：查找、搜索、提供、查。

## Source Refs

- `src_20260522_a89ab860` -> `10_raw/sources/src_20260522_a89ab860-meta-prompt-eng.md`

## Reusable Knowledge

- 模式演示与固化 (ReACT 执行范式) 请严格学习并模仿以下 ReACT 执行的流程和格式，这是你的工作范式： Agent (LLM): L0 确认（边界/示例/问询）→ 等待用户确认 用户 (You): [确认 L0 / 补充材料] Agent (LLM): Thought → Action: google:search[.

## Open Questions

- 我应该分享关于哪个行业的最终智慧？
- 强制确认：在进入 CoT 之前，必须向用户确认：对边界界定是否满意？对提供的 5 个清单体示例的风格、粒度、深度是否认可？

## Output Opportunities

- Content: report or analysis
- Code:
- Capability: workflow or playbook
