---
id: tool-react行动推理循环
title: 技能：ReACT行动推理循环
type: tool
domain:
- ai-collaboration- ai-saas
- yitang
status: draft
source_person: Truman
source_context: src_20260609_03491271
source_refs:
- 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
definition_of_done: null
tools_required: null
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
related:
- '[[tool-反向提示获取优化建议]]'
- '[[tool-多轮确认防偏差]]'
- '[[tool-主动摘要压缩上下文]]'
- '[[tool-提示词结构化迭代]]'
- '[[tool-渐进式披露上下文]]'
- '[[tool-strategy-customer-selection]]'
- tool-ai-prd-for-ai
tags:
- audience:executor
- scene:execution
- skill-level:beginner
aliases:
- 自用的
---

# 技能：ReACT行动推理循环

## 原始表述
> 6.使用ReACT

## 操作步骤
1. 定义可调用工具集（搜索/计算/代码执行等）
2. 模型循环执行：Thought（思考需要什么）→ Action（调用工具）→ Observation（获取结果）→ ...
3. 直到获得最终答案
4. 显式追踪每一步的推理和工具调用

## 适用场景
- src_unknown
- src_unknown
- src_unknown

## 为什么有效
将推理与行动交织，模型自主决定何时需要外部信息，比纯生成更准确和及时

## 工具/环境
- src_unknown
- src_unknown
- src_unknown

## 关联技能
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

- **具体假设**：该工具假设现有方法论框架能指导实践，但框架的有效性依赖于'环境稳定性'——当环境发生颠覆性变化时，旧框架不仅无效，还可能误导。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Clayton Christensen**（哈佛商学院教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
