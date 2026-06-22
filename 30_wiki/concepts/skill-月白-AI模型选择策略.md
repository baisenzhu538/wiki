---



id: skill-月白-AI模型选择策略
title: 技能：AI模型选择策略
type: "tool"
status: draft
domain:
- design
source_person: 月白
source_context: AI设计基础 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
  - src_20260522_38173b48-design-ai-image-generation
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
  - '[[skill-月白-关键要素提取改图法]]'
  - '[[skill-月白-多语言提示词精准法]]'
  - '[[skill-月白-PPT全AI生成工作流]]'
  - '[[skill-月白-精准提示词消除模型幻觉]]'
  - '[[skill-月白-AI设计严苛批评法]]'
---
# 技能：AI模型选择策略

## 原始表述

AI模型选择策略是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 明确任务类型：真实质感/文字生成/艺术风格/角色设计
2. 真实世界质感+文字直出：优先选AIGC/GPT-4o
3. 艺术人文风格、特定艺术家风格：选Midjourney/Stable Diffusion
4. 2D动漫角色：各家模型差异不大
5. 日常免费快速出图：选豆包
6. 根据实际效果迭代，不盲目追新

## 适用场景

- 开始新项目前评估工具
- 当前模型效果不满意时
- 需要控制成本（Token费用）时
- 批量生产与单张精品的权衡

## 不适用场景

- 已经找到最适合当前任务的模型且效果满意
- 所有场景都强行使用同一模型

## 工具/环境

- 豆包
- GPT-4o
- Midjourney
- Stable Diffusion/Flux
- 即梦
- 通义千问

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

不同模型语料和训练侧重不同，没有绝对最好的模型，只有最适合当前任务的模型；选择正确模型直接影响出图质量和成本效率

## 关联技能

- 待补充

## 来源

- 月白，AI设计基础

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
