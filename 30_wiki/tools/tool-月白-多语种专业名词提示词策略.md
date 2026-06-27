---
id: tool-月白-多语种专业名词提示词策略
title: 技能：多语种专业名词提示词策略
type: tool
status: draft
domain:
- design- design
source_person: 月白
source_context: 文创案例 （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
source_refs:
- src_unknown
wiki_refs: null
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- confidence-draft
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-口喷作图工作流]]'
- '[[tool-月白-AIGC反向拆解法]]'
- '[[tool-月白-AIGC设计作业复盘法]]'
- '[[tool-月白-设计参考图精准定位法]]'
- '[[tool-月白-AIGC人群画像驱动详情页规划]]'
---
# 技能：多语种专业名词提示词策略

## 原始表述

多语种专业名词提示词策略是月白在文创案例中提出的实操方法。

## 操作步骤

1. 识别专业领域的核心名词（如艺术、医学、建筑等）
2. 查找该名词的英语原文
3. 追溯更高精度的语源语言（如意大利语Bastone、法语等）
4. 在提示词中优先使用原始语源词汇
5. 配合精准约束条件形成双重策略

## 适用场景

- 涉及高度专业化视觉生成（如西文字体设计、古典艺术、建筑设计）
- 中文或英文翻译导致语义损失或模糊时
- 需要消除AI幻觉的严谨场景
- 使用国外模型（如A）进行生成时

## 不适用场景

- 日常通用场景（国内豆包等模型处理国内用途图片）
- 非专业领域的普通描述
- 成本敏感且精度要求不高的批量任务

## 工具/环境

- AI对话模型（A/文心一言/豆包等）
- 专业术语词典/语源学资料
- 多语言翻译工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI模型对英文语料的训练精度和丰富度高于中文翻译词，而某些专业领域（如意大利艺术、音乐）的核心名词源自特定语言，使用原始语源词汇能激活更精准的视觉样本关联，大幅降低语义偏差和幻觉

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
