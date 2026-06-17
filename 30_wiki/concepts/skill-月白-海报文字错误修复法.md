---

id: skill-月白-海报文字错误修复法
title: 技能：海报文字错误修复法
type: "tool"
status: draft
domain:
- design
source_person: 月白
source_context: AI设计基础 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
- src_20260522_38173b48
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
# 技能：海报文字错误修复法

## 原始表述

海报文字错误修复法是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 发现AI生成海报中的错别字或文字错误
2. 使用超短提示词：'用最高清模式重新生成这张图，并修复图片中的中文字'
3. 若效果不佳，换用image效果修复
4. 或用完整逆向提示词重新约束文字部分

## 适用场景

- AI生成海报出现乱码、错字、缺字
- 需要保留整体设计只修正文字

## 不适用场景

- 文字设计本身需要创意变形（修复会标准化）

## 工具/环境

- 豆包
- 即梦（image效果）
- 逆向提示词库

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI生成中文文字的'幻觉'是普遍问题，通过明确约束或专用修复指令可大幅改善

## 关联技能

- 待补充

## 来源

- 月白，AI设计基础

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
