---
id: "skill-纪浩-识别AI不可维护代码"
title: "技能：识别AI不可维护代码"
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
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management/tagging"
  - "#scene/learning-methodology/feedback-loop"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：识别AI不可维护代码

## 原始表述

识别AI不可维护代码是纪浩在AI协作方法论分享中提出的具体方法，用于识别AI不可维护代码。

## 操作步骤

1. 检查代码是否包含字符串拼接的HTML+script标签
2. 评估后续拆分/重构的可行性
3. 判断AI是否能在提示下不跑偏地完成维护

## 适用场景

- 接手AI生成或他人代码时
- 代码包含动态拼接HTML和脚本

## 不适用场景

- 代码结构清晰、职责分离良好

## 工具/环境

- 代码审查工具
- 静态分析工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未先确认场景是否适用 → 方法无效 → **先对照“适用场景”确认本方法适用**

## 为什么有效

字符串拼接HTML内嵌script会导致高耦合、难拆分，AI和人类都难以维护

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
