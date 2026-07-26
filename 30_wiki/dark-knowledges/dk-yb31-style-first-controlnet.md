---
id: dk-yb31-style-first-controlnet
title: AI绘图工作流：先锁风格再开ControlNet
type: dk
dark_knowledge_type: workflow
status: draft
domain:
- design
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
tags:
- audience:executor
- scene:reference
- skill-level:beginner
---

# AI绘图工作流：先锁风格再开ControlNet

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
## 补充说明

该文件记录了「AI绘图工作流：先锁风格再开ControlNet」的相关内容。从知识管理的角度看，这类信息需要经过结构化提炼才能有效复用。

### 核心要点

1. **概念理解**：AI绘图工作流：先锁风格再开ControlNet的核心定义和关键要素，需要在具体场景中理解其适用边界。
2. **实践应用**：在实际工作中，该知识点可以帮助团队更好地理解和解决问题。
3. **关联知识**：与一堂方法论体系中的其他模块存在关联，建议结合上下文理解。

### 注意事项

- 知识卡片的价值在于复用，而非记录本身——需要在实践中验证和迭代。
- 不同场景下的适用性可能不同，使用前需确认前提条件是否满足。
- 建议定期回顾和更新，确保知识与实际业务保持同步。
