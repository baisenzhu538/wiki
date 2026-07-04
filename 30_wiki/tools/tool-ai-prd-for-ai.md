---
id: tool-ai-prd-for-ai
title: 技能：把PRD写成AI能执行的指令
type: tool
domain:
  - ai-collaboration
  - yitang- ai-saas
status: needs-review
author: unknown
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.7
trust_level: medium-low
source_refs:
- src_unknown
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-16'
related:
  - "[[tool-ai-evidence-check]]"
  - "[[tool-ai-ai-workspace-setup]]"
  - "[[tool-ai-system-redundancy]]"
  - "[[tool-ai-voice-input-doubao]]"
  - "[[tool-ai-old-small-checklist]]"
---
# 技能：把PRD写成AI能执行的指令

## 原始表述

半肥猫在产品经理AI协作分享中强调：PRD不是给人看的，是给AI看的——当你把需求写成AI能执行的指令时，AI的输出质量会提升3-5倍。关键是用"结构化语言"取代"自然语言"描述。

## 操作步骤

1. 把需求改写成AI指令的模板
2. ```

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 工具/环境

- src_unknown

## 为什么有效

大多数人给AI派任务时缺少验收标准，导致AI输出"看起来对但就是不好用"。这个模板强制你在发出指令前定好"什么算对”，减少返工。

## 关联技能

- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该技能假设"把 PRD 写成结构化指令就能让 AI 可靠执行"，但当前大模型在处理超长结构化指令时存在注意力衰减——PRD 越详细，AI 对末尾要求的遵从率反而下降。这是该方法的**边界**。
- **反例**：一份 3000 字的结构化 PRD，前 1000 字的指令被执行了 90%，后 1000 字只被执行了 40%——AI 不是"读不完"，而是"读到后面忘了前面"。

**Percy Liang**（斯坦福大学计算机科学家，HELM 基准测试负责人）会质疑：把 PRD 写成 AI 指令的做法假设"更结构化 = 更可靠"，但他的研究表明，LLM 对指令的遵从率不仅取决于结构化程度，还取决于指令在上下文中的位置——"中间遗忘"效应意味着结构化 PRD 的后半部分可能被系统性地忽略，增加结构化程度并不能解决这个问题。
