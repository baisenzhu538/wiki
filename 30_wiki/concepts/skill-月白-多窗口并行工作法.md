---


id: skill-月白-多窗口并行工作法
title: 技能：多窗口并行工作法
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
# 技能：多窗口并行工作法

## 原始表述

多窗口并行工作法是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 产品图生成一个窗口
2. 风格参考/提示词优化另开新窗口
3. 改图/扩图再开新窗口
4. 遇到生成效果偏离预期时，不纠结调整，直接新开窗口重来

## 适用场景

- 需要同时处理多个生成任务
- 当前对话窗口生成效果变差
- 需要避免AI受之前错误提示词影响

## 不适用场景

- 单任务简单生成
- 需要保持上下文连贯的复杂迭代

## 工具/环境

- 豆包AI多窗口

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI会受对话历史影响，新窗口能清除错误印象；多线程并行提升效率，且新窗口免费无成本

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
