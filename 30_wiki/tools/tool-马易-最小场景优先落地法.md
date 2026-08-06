---

id: tool-马易-最小场景优先落地法
title: 技能：最小场景优先落地法
type: tool
domain:
status: reviewed
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-29'
created_at: '2026-06-15'
confidence: 0.7
trust_level: medium-low
aliases:
  - audience:executor
  - scene:execution
  - skill-level:intermediate
  - 技能
  - 技能：最小场景优先落地法
  - 最小场景优先落地法
source_refs: null
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-29'
discoverable_by:
  - 技能：最小场景优先落地法
  - 最小场景优先落地法
related:
tags:
---
# 技能：最小场景优先落地法

## 原始表述

最小场景优先落地法是马易在AI落地场景识别中提出的实操方法。

## 操作步骤

1. 避开Y模型最高场景
2. 选择Y模型最低、最熟悉的场景
3. 优先找老的、小的业务环节
4. 验证成功后再扩展

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

全球最成功功能皆从最小场景完成，头部公司如微软、蚂蚁均在原有业务优化而非重创新，降低风险积累能力

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI落地中"一上来就做最大最复杂场景导致失败"的问题——团队倾向选择最有想象力的场景（如全面智能客服、全自动化流程），但这些场景涉及的数据复杂度、业务边界、用户接受度都是最高的，失败概率极大。最小场景优先落地法要求选择Y模型中最低、最熟悉的场景（通常是老的、小的业务环节），在最小风险下验证AI能力并积累工程经验，成功后再扩展。适用于AI项目首次落地阶段，尤其是资源和经验有限的团队。

## 质疑

最小场景优先落地法的隐含前提是"最小场景的成功可以外推到更大场景"，但这个假设在AI系统中可能严重失效。**Dario Amodei** 在Scaling Laws研究中表明，AI系统的行为在规模变化时并非线性外推——在小数据量上有效的模型架构和训练策略，在大规模场景中可能完全失效。一个具体反例：团队在最小场景（100条标注数据）中训练的模型达到95%准确率，扩展到全量场景（10万条数据）后准确率骤降至60%，因为小场景中未出现的边缘案例在大场景中占比极大。另一个前提是"最小场景足以验证核心假设"，但**Rita McGrath** 指出，最小场景的"低风险"可能只是因为场景太小以至于无法暴露核心风险——团队在小场景中获得虚假信心，到扩展阶段才发现根本性问题。
