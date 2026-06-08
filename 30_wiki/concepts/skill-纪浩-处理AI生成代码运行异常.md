---
id: "skill-纪浩-处理AI生成代码运行异常"
title: "技能：处理AI生成代码运行异常"
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
tags:
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#scene/ai-collaboration/prompt-engineering"
  - "#scene/learning-methodology/feedback-loop"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：处理AI生成代码运行异常

## 原始表述

处理AI生成代码运行异常是纪浩在AI协作方法论分享中提出的具体方法，用于处理AI生成代码运行异常。

## 操作步骤

1. 确认异常现象和复现路径
2. 检查提示词是否表达清晰（避免promote歧义）
3. 人工加班排查（必要时）

## 适用场景

- AI代码报错或行为异常
- 提示词存在歧义导致理解偏差

## 不适用场景

- 问题已定位且可自动修复

## 工具/环境

- 日志系统
- 调试工具
- 版本控制

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未先确认场景是否适用 → 方法无效 → **先对照“适用场景”确认本方法适用**

## 为什么有效

提示词歧义或AI理解偏差会导致代码问题，需要人工介入定位

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
