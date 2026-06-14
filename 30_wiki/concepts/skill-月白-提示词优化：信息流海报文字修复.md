---
id: "skill-月白-提示词优化：信息流海报文字修复"
title: "技能：提示词优化：信息流海报文字修复"
type: "skill"
status: "draft"
domain:
  - "design"
source_person: "月白"
source_context: "AI设计基础"
source_refs: ""
wiki_refs: ""
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
tags:
  - None
  - None
  - None
  - None
pipeline:
  - "confidence-draft"
author: "legacy"
reviewed_by: "pending"
confidence: 0.6
trust_level: "low"
---

# 技能：提示词优化：信息流海报文字修复

## 原始表述

提示词优化：信息流海报文字修复是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 生成基础海报后发现中文文字错误
2. 不修改其他提示词
3. 直接追加一句：'用最高分辨率重新生成这张图，修改中文中的文字错误'
4. 重新生成

## 适用场景

- AIGC/即梦/云即梦生成的海报文字效果不佳
- 中文出现错别字或乱码
- 需要快速提升文字准确率

## 不适用场景

- 整体画面构图需要大改
- 非文字类问题（如人物变形、空间错误）

## 工具/环境

- 即梦
- 云即梦
- 其他支持中文文字的AIGC模型

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

提示词过多会模糊关键指令，超短精准提示词有时比重写长提示词更有效；'最高分辨率'触发模型重新渲染细节，'修改中文文字错误'直接定位问题

## 关联技能

- 待补充

## 来源

- 月白，AI设计基础

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
