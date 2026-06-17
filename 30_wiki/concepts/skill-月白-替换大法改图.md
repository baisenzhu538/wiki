---


id: skill-月白-替换大法改图
title: 技能：替换大法改图
type: "tool"
status: draft
domain:
- design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
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
# 技能：替换大法改图

## 原始表述

替换大法改图是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 确定需要替换的维度（位置/风格/内容/视角）
2. 准备参考图A
3. 明确目标需求并整理提示词
4. 将参考图+提示词提交给AIGC
5. 迭代调整直至满意

## 适用场景

- 需要修改图片角度/位置关系
- 需要保持风格只改局部
- 需要改变视角但保留主体
- 描述困难时直接用参考替换

## 不适用场景

- 需要完全原创无参考
- 涉及版权敏感素材直接复制

## 工具/环境

- 豆包/Cubox等AIGC工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

降低描述难度，通过参考图+明确指令让AI执行替换，比纯文字描述更精准可控

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
