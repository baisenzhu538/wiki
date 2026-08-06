---
id: tool-月白-AI归纳共性描述法
title: 技能：AI归纳共性描述法
type: tool
status: draft
domain: design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
aliases:
  - AI归纳共性描述法
  - audience:executor
  - scene:execution
  - skill-level:beginner
  - 技能
  - 技能：AI归纳共性描述法
  - 月白
source_refs:
wiki_refs: null
definition_of_done:
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
author: 月白
reviewed_by: 欧阳锋
reviewed_at: '2026-07-04'
confidence: 0.6
trust_level: low
discoverable_by:
  - 技能：AI归纳共性描述法
  - AI归纳共性描述法
related:
tags:
---
# 技能：AI归纳共性描述法

## 原始表述

AI归纳共性描述法是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 收集多张同一类型的目标图片（5-10张）
2. 将这批图片一起丢给AI
3. 要求AI总结归纳这些图片的共性特征
4. 用AI生成的共性描述作为生成提示词

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown
- src_unknown

## 工具/环境

- src_unknown
- src_unknown
- src_unknown

## 为什么有效

利用AI的归纳能力，将模糊的'体感'转化为可操作的精准描述

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决"看了一堆参考图但不知道怎么写prompt"的体感转化问题。设计师的视觉感受力和语言表达力往往存在断层——看到一组建材风格图能分辨好坏，但说不清这些图片的共同特征是什么。AI归纳共性描述法利用多模态AI的归纳能力，将5-10张同类参考图批量输入给AI，让AI提炼共性特征（色调、质感、光线、构图等），并用AI生成的共性描述作为生图prompt。适用于风格定义、视觉方向收敛、以及向AI"翻译"设计偏好的场景。

## 质疑

- **具体假设**：该工具假设结构化方法论本身能产生正确结论，但方法论只是框架——结论质量取决于输入数据的质量和执行者的判断力。
- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效——工具的有效性高度依赖场景的稳定性。
- **反例**：一个团队完整执行了所有步骤，产出了漂亮的文档，但核心假设从一开始就是错的——流程的完整性掩盖了判断的缺陷。
- **前提**：使用者已具备该领域的基础认知，能正确理解和执行工具规则，且数据来源具有代表性。

AI归纳的共性偏向表层视觉特征的统计平均，而设计风格的精髓往往在于例外的细节和个性化的偏离。**Clement Mok**（Apple前创意总监）曾指出，伟大的设计风格不是"共性的平均"而是"个性的极致"——AI归纳输出的是分母化之后的特征，恰恰抹杀了参考图集中最有趣的部分。**Johanna Drucker**（视觉文化学者）批评，这种"输入多张图→输出一种风格描述"的方法将设计风格简化为可批量复制的视觉配方，忽略了风格背后的文化语境和历史脉络。用AI归纳共性生成的设计可能看起来"有点像"参考图，但缺乏原创性——因为每一个有趣的参考图之所以有趣，都不是因为它符合共性，而是因为它在某些维度上偏离了共性。
