---
id: tool-月白-风格不变局部调整
title: 技能：风格不变局部调整
type: tool
status: draft
domain: design- design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
- 10_raw/sources/src_20260522_38173b48-design-ai-image-generation.md
wiki_refs: null
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- src_unknown
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- "[[tool-月白-多窗口并行工作法]]"
- "[[tool-月白-竞品图精益替换法]]"
- "[[tool-月白-眼高手低训练法]]"
- "[[tool-月白-线下门店设计复杂度评估]]"
- "[[tool-月白-AIGC橱窗陈列设计流程]]"
---
# 技能：风格不变局部调整

## 原始表述

风格不变局部调整是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 用超长详细提示词首次抽卡
2. 识别局部问题（姿势/颜色/元素）
3. 定位提示词中对应描述部分
4. 精准修改该部分描述
5. 重新生成验证效果
6. 重复直至局部满意

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown
- src_unknown

## 工具/环境

- src_unknown

## 为什么有效

超长提示词提供稳定基础，局部修改避免破坏已满意的整体效果，实现精准控制

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI图像生成中"整体满意但局部有瑕疵"的精准修复问题。适用于需要对AI生成结果做微调（如修正姿势偏差、颜色不协调、多余元素）而不破坏整体风格的场景。核心价值是将"重新生成赌运气"转变为"定位修改精准控制"，大幅降低返工成本。

## 质疑

**前提假设**是"超长提示词的各部分描述独立可控"，但实际上提示词各语义片段之间存在耦合效应——修改一处描述可能引发模型对整体理解的漂移，导致预期外的连锁变化。**边界**在于：当局部问题涉及全局构图关系（如透视、光影一致性）时，局部修改无法解决，必须整体重生成。**反例**：修改"左手姿势"描述后，模型重新生成的图中右手也发生了变化——说明局部控制远不如预期精确。**Philipp Schmitt** 在研究AI生成可控性时指出，当前扩散模型的注意力机制使得提示词各部分权重难以精确隔离，所谓的"局部修改"本质上仍是全图重新采样，只是受初始种子约束较多而已。**Antonio Torralba** 在MIT的可解释AI研究中也批评道，人类直觉上认为可以"外科手术式"修改图像局部，但生成模型的潜在空间并不支持这种像素级隔离操作，更多是一种心理安慰。
