---


id: skill-月白-图片逆向提示词提取
title: 技能：图片逆向提示词提取
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
---
# 技能：图片逆向提示词提取

## 原始表述

图片逆向提示词提取是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 准备需要逆向分析的图片
2. 使用标准逆向提示词框架：从风格限定、角色构图、主体描述、背景设定、细节、色调、对焦、物品画面质感、画面构图、画面尺寸等方面描述
3. 将图片和逆向提示词一起发送给豆包
4. 获取豆包生成的详细提示词
5. 使用该提示词在AIGC工具中生成新图片

## 适用场景

- 看到优秀图片想要复刻风格
- 需要分析图片的构成要素
- 想要基于现有图片生成类似风格
- 所有类型的图片逆向需求

## 不适用场景

- 图片版权受限不可参考
- 需要完全原创不参考任何风格

## 工具/环境

- 豆包
- 任意AIGC图片生成工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

通过结构化维度拆解图片，AI能精准提取视觉要素并转化为可复用的生成指令，解决'看到但说不出'的痛点

## 关联技能

- 待补充

## 来源

- 月白，AI设计基础

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
