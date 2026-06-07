---
id: "skill-纪浩-AI项目五层知识结构设计"
title: "技能：AI项目五层知识结构设计"
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
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#domain/design"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management"
  - "#scene/learning-methodology"
tools_required:
prerequisite_skills:
related:
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：AI项目五层知识结构设计

## 原始表述

AI项目五层知识结构设计是纪浩在AI协作方法论中提出的实操方法。

## 操作步骤

1. 将项目知识分为五层：系统自述、领域知识、Agent服务文档、任务管理与上下文、日志
2. 系统自述记录架构/组件/技术栈，防止架构漂移
3. 领域知识独立存放业务逻辑（如课程运营、马拉松规则），避免AI猜测
4. Agent服务文档包含：导诊台（任务分类）、工作手册（不同任务的SOP）、工具集（脚本化工具）、经验模式库（纠错总结）
5. 任务管理包含：任务定义与状态、交付物标准、执行流程与上下文
6. 日志单独管理用于排查问题
7. 确保五类知识物理分离，不混放

## 适用场景

- 启动AI协作项目时
- AI开始频繁出错、理解偏差、输出混乱时
- 项目需要长期维护、多任务并行时

## 不适用场景

- 一次性简单任务
- 实验性、短期验证场景

## 工具/环境

- 文档系统/知识库（如Notion、飞书）
- 任务管理平台
- 版本控制工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI是模式匹配系统，不会做结构设计，只会模仿预训练中的相似结构；五层分离可防止知识混淆导致的架构漂移、业务逻辑冲突和不可验证输出

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
