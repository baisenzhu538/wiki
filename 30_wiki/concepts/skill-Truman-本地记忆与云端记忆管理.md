---
id: "skill-Truman-本地记忆与云端记忆管理"
title: "技能：本地记忆与云端记忆管理"
type: "skill"
status: "draft"
domain:
source_person: "Truman"
source_context: "AI工具应用AMA"
source_refs:
wiki_refs:
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tags:
  - "#confidence/draft"
  - "#domain/AI"
tools_required:
prerequisite_skills:
related:
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：本地记忆与云端记忆管理

## 原始表述

本地记忆与云端记忆管理是Truman在AI工具应用AMA中提出的实操方法。

## 操作步骤

1. 理解记忆本质：大模型+提示词+上下文管理
2. 选择层级：记事本+ChatGPT（最简）→飞书文档+Code（协作）→Coze/LangChain（结构化）→高级模型（自我优化）
3. 根据项目规模选择：小型项目用Cubox类内部成套方案；自动化场景用LangChain类；自我优化场景用更高级模型
4. 持续同步和更新记忆文档

## 适用场景

- AI记忆不稳定或丢失
- 需要长期维护项目上下文
- 多轮对话后AI遗忘关键信息

## 不适用场景

- 单次对话无需记忆
- 完全确定性任务无需上下文

## 工具/环境

- Cubox
- LangChain
- LangSmith
- Coze
- 飞书文档
- 记事本
- 各类Memory组件

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

记忆管理归根结底是上下文管理，不同工具是逐层递进关系；理解底层原理后可根据场景灵活选择，无本质区别

## 关联技能

- 待补充

## 来源

- Truman，AI工具应用AMA

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
