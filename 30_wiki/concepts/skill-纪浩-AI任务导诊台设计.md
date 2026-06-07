---
id: "skill-纪浩-AI任务导诊台设计"
title: "技能：AI任务导诊台设计"
type: "skill"
status: "draft"
domain:
source_person: "纪浩"
source_context: "AI协作方法论"
source_refs:
wiki_refs:
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tags:
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#domain/design"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management"
tools_required:
prerequisite_skills:
related:
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：AI任务导诊台设计

## 原始表述

AI任务导诊台设计是纪浩在AI协作方法论中提出的实操方法。

## 操作步骤

1. 梳理Agent需要处理的所有任务类型（开发/改bug/运维/需求讨论/运营等）
2. 设计分类规则或分类Prompt，让AI能自动判断任务类型
3. 为每类任务关联对应的工作手册（不同SOP）
4. 确保导诊台与知识库独立，工作手册再关联领域知识和经验库

## 适用场景

- Agent需要处理多种不同类型任务时
- 出现AI用错误流程解决任务、任务混淆时

## 不适用场景

- Agent只处理单一类型任务（如仅数据分析）

## 工具/环境

- 分类Prompt模板
- 工作手册文档

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

不同任务需要不同规范和流程，导诊台实现渐进式披露，避免AI拿到复杂任务后直接盲目执行

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
