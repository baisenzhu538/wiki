---
id: tool-ai-ai-workspace-setup
title: 技能：结构化AI工作空间搭建
type: tool
domain:
- ai-collaboration
- yitang
- ai-saas
status: needs-review
author: unknown
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.7
trust_level: medium-low
aliases:
  - 工作空间搭建
  - 技能
  - 技能：结构化AI工作空间搭建
  - 结构化
  - 结构化AI工作空间搭建
source_refs: null
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-16'
related:
- '[[tool-ai-evidence-check]]'
- '[[tool-ai-voice-input-doubao]]'
- '[[tool-ai-prd-for-ai]]'
- '[[structured-ai-workspace]]'
- '[[tool-ai-old-small-checklist]]'
- '[[tool-Truman-多Agent通信协作方案]]'
- '[[tool-ai-parallel-validation]]'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
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

- src_unknown
- src_unknown
- src_unknown

## 工具/环境

- src_unknown

## 为什么有效

很多人以为AI任务乱是因为AI不行，其实是因为人的上下文管理不行。这个方法能让AI"记住"项目背景，减少重复解释。

## 关联技能

- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"结构化工作空间可以让 AI 记住项目背景"，但当前大模型的上下文窗口是有限的——随着任务积累，工作空间中的文件越来越多，AI 无法在一次对话中加载全部上下文，"记忆"效果递减。这是该方法的**边界**。
- **反例**：当项目迭代到第 50 个任务时，任务跟踪表本身已经成为一个巨大的上下文负担——AI 需要先"阅读"50 条历史任务才能理解当前任务，反而降低了效率。

**Andrew Ng**（斯坦福大学计算机科学家，前 Google Brain 负责人）会质疑：结构化工作空间假设"文件组织 = 上下文管理"，但 LLM 的真正瓶颈不是文件结构，而是注意力机制——即使你把所有文件整理得井井有条，模型也无法在一次推理中有效利用超过一定长度的上下文。
