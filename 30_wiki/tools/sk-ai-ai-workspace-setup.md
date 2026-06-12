---


id: sk-ai-ai-workspace-setup
title: 技能：结构化AI工作空间搭建
type: skill
status: draft
domain:
- AI
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论分享，2026-06
source_refs:
- src_20260606_42e11f09
wiki_refs:
- structured-ai-workspace
- sk-ai-problem-validation
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tags:
- '#skill/ai'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-06'
tools_required:
- 笔记本和笔
prerequisite_skills: []
related:
- structured-ai-workspace
- sk-ai-problem-validation
domain: [ai-collaboration]
diagnostic_signals:
  - signal: "TODO: User scenario that triggers this diagnostic"
    framework_lens: "TODO: What perspective the framework provides"
    follow_up_question: "TODO: The first follow-up question"
---

# 技能：结构化AI工作空间搭建

## 原始表述

纪浩提出，AI任务多了以后会变得很乱，需要建立结构化工作空间。核心模块包括：系统自述、领域知识、Agent服务文档、任务管理、日志。

## 操作步骤

1. 最小化搭建（只需要3个文件）
2. 写清楚：
3. AI是谁：你的AI助手的"人设"和能力范围
4. 常见任务SOP：每类任务的标准步骤
5. 输出格式要求：AI返回结果的统一格式
6. 业务术语库
7. 项目背景和约束
8. 已验证的Skill模板
9. 每个任务记录：
10. 任务名称
11. 当前状态（待开始/进行中/待验收/已完成）
12. 输入材料
13. 预期输出
14. 验收标准
15. 遇到的问题
16. 使用流程
1. 新任务来了，先填任务跟踪表
2. 把相关背景从领域知识库拷贝到当前对话的上下文中
3. 3. 如果是常见任务，让AI按工作手册执行
4. 4. 任务结束后更新状态，记录问题

## 适用场景

- AI任务越来越多，文件乱成一团
- 同一个任务每次都要重新给AI解释背景
- 团队成员不知道AI做了什么、做到哪了

## 工具/环境

- 笔记本和笔

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行，每步必须验收后进入下一步**
- 单人操作忽视团队协作 → 成果难推广 → **步骤1就征求团队意见**
- 惯性思维干扰 → 跳过某步 → **按清单逐条打勾，不要靠感觉**

## 为什么有效

很多人以为AI任务乱是因为AI不行，其实是因为人的上下文管理不行。这个方法能让AI"记住"项目背景，减少重复解释。

## 关联技能

- [[structured-ai-workspace]]
- [[sk-ai-problem-validation]]

## 来源

- 纪浩，AI俱乐部-AI协作方法论分享，2026-06

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
