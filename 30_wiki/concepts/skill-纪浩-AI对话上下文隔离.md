---
id: "skill-纪浩-AI对话上下文隔离"
title: "技能：AI对话上下文隔离"
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
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management"
tools_required:
prerequisite_skills:
related:
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：AI对话上下文隔离

## 原始表述

AI对话上下文隔离是纪浩在AI协作方法论中提出的实操方法。

## 操作步骤

1. 一次对话只围绕一个任务展开
2. 对话前预判：需要几轮对话、每轮说什么、AI会做什么、可能卡在哪里
3. 若当前对话已'脏'（混乱/不可挽回），果断放弃，复制有效信息开启新对话
4. 新对话明确注入所需知识（工作手册、经验库、领域知识），而非依赖污染后的上下文

## 适用场景

- AI开始理解偏差、输出混乱时
- 对话已进行多轮，上下文累积过多时
- 需要切换任务或重新开始时

## 不适用场景

- 简单单轮对话即可完成时

## 工具/环境

- 对话历史管理
- 知识库片段复制
- 新会话启动

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI上下文有限且会累积错误，'脏'对话会让AI在错误道路上越走越远；隔离上下文可重置状态，确保AI基于正确信息执行

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
