---
id: tool-增强数据供给
title: 技能：增强数据供给
type: tool
domain:
  - learning-methodology
  - design
  - yitang
  - decision-making
status: draft
source_person: Truman
source_context: src_20260609_03491271
aliases:
  - Truman
  - 增强数据供给
  - 技能
  - 技能：增强数据供给
source_refs:
- 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
discoverable_by:
  - 技能：增强数据供给
  - 增强数据供给
related:
- '[[tool-反向提示获取优化建议]]'
- '[[tool-多轮确认防偏差]]'
- '[[tool-主动摘要压缩上下文]]'
- '[[tool-提示词结构化迭代]]'
- '[[tool-渐进式披露上下文]]'
- tool-ai-prd-for-ai
tags:
- audience:executor
- scene:execution
- skill-level:beginner
- 自用的
---
# 技能：增强数据供给

## 原始表述
> 1.给案例集 2.专家资料 3.用多模态 4.联网搜索 5.接入API 6.使用RAG

## 操作步骤
1. 识别任务所需的外部知识类型
2. 选择供给方式：案例集（few-shot）、专家资料（角色注入）、多模态（图文音视频）、实时搜索、私有API、RAG检索
3. 将数据格式化接入模型上下文
4. 评估效果调整供给策略

## 适用场景
- src_unknown
- src_unknown
- src_unknown

## 为什么有效
在不对模型微调的情况下，通过上下文学习注入特定能力和知识，灵活且成本低

## 工具/环境
- src_unknown
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

- **具体假设**：该工具假设工具本身能解决问题，但工具只是'能力放大器'——如果使用者的判断力不足，工具只会放大错误而非放大正确。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Amy Edmondson**（哈佛商学院教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
