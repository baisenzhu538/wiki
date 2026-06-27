---
id: dk-yb31-style-first-controlnet
title: AI绘图工作流：先锁风格再开ControlNet
type: dk
dark_knowledge_type: workflow
status: draft
domain:
- src_unknown
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- 00_inbox/design/AI设计-AI设计基础01.txt
created_at: 2026-06-04
updated_at: '2026-06-16'
related: null
pipeline:
- src_unknown
- src_unknown
author: 月白
reviewed_by: pending
confidence: 0.7
trust_level: low
---# AI绘图工作流：先锁风格再开ControlNet

## 原始表述

> 先调风格提示词，不要打开先调你的风格提示词，风格提示词调对了再打开。

## 使用场景

AI绘图设计师/运营对接场景，需要快速验证甲方需求方向时使用。

## 操作方法

1. 用模板快速跑图测试（30分钟内完成前四步）
2. 先调整风格提示词，确认风格方向正确
3. 风格确定后再开启ControlNet等控制网络进行精细化控制
4. 拿结果给甲方/运营确认方向是否正确

## 适用边界

- src_unknown
- src_unknown

## 为什么值钱

公开教程通常教"ControlNet+提示词一起调"，但实战中先开ControlNet会锁定构图干扰风格判断，导致反复在错误方向上迭代。这是大量甲乙双方来回撕扯后的效率妥协策略。

## 与其他知识的关联

- src_unknown
