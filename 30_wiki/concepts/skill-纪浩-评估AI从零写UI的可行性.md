---
id: "skill-纪浩-评估AI从零写UI的可行性"
title: "技能：评估AI从零写UI的可行性"
type: "skill"
status: "draft"
domain: ""
source_person: "纪浩"
source_context: "AI协作方法论"
source_refs:
  - "00_inbox/纪浩-AI协作方法论-口述.md"
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
  - #domain/AI
  - #domain/collaboration
  - #scene/ai-collaboration/prompt-engineering
  - #scene/learning-methodology/feedback-loop
pipeline:
  - #boundary/requires-human-judgment
  - confidence-draft
---

# 技能：评估AI从零写UI的可行性

## 原始表述

评估AI从零写UI的可行性是纪浩在AI协作方法论分享中提出的具体方法，用于评估AI从零写UI的可行性。

## 操作步骤

1. 判断是否有高质量参考案例
2. 判断历史代码是否会产生干扰
3. 评估是否能通过提示词让AI输出清晰结构

## 适用场景

- 需要AI生成新UI模块
- 缺乏明确设计规范时

## 不适用场景

- 有成熟组件库和设计规范可参考
- 需求非常明确且边界清晰

## 工具/环境

- 提示词工程
- 设计规范文档
- 组件库

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未先确认场景是否适用 → 方法无效 → **先对照“适用场景”确认本方法适用**

## 为什么有效

AI容易被参考案例或历史代码带偏，难以自主产出结构良好的UI

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
