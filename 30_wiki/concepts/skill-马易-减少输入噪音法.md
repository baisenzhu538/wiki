---
id: skill-马易-减少输入噪音法
title: 技能：减少输入噪音法
type: skill
status: draft
domain: []
source_person: 马易
source_context: AI落地场景识别
source_refs: []
wiki_refs: []
definition_of_done:
  - 操作步骤清晰可执行
  - 适用场景有正反例
  - 工具要求明确
tags:
  - "#domain/AI"
  - "#domain/scene-analysis"
tools_required: []
prerequisite_skills: []
related: []
created_at: '2026-06-07'
updated_at: '2026-06-07'
---

# 技能：减少输入噪音法

## 原始表述

减少输入噪音法是马易在AI落地场景识别中提出的实操方法。

## 操作步骤

1. 识别核心判断内容
2. 剔除无关冗余信息
3. 控制输入内容在300字内
4. 必要时单独提取关键信息处理

## 适用场景

- AI判断准确性下降时
- 长文档中关键信息提取时
- 需要高精度判断时

## 不适用场景

- 需要全局上下文理解时
- 信息关联性复杂时

## 工具/环境

- 文本提取工具
- 关键信息标注
- 分段处理流程

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

大模型Attention机制存在噪音问题，300字内容在3000字无关文本中准确性降低70%，窄范围短输入有效性更高

## 关联技能

- 待补充

## 来源

- 马易，AI落地场景识别

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
