---
id: "skill-马易-低置信度样本黄金漏斗处理"
title: "技能：低置信度样本黄金漏斗处理"
type: "skill"
status: "draft"
domain: ""
source_person: "马易"
source_context: "AI落地场景识别"
source_refs: ""
wiki_refs: ""
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tags:
  - "confidence-draft"
  - "#domain/AI"
  - "#domain/scene-analysis"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/note-taking/checklist-method"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：低置信度样本黄金漏斗处理

## 原始表述

低置信度样本黄金漏斗处理是马易在AI落地场景识别中提出的实操方法。

## 操作步骤

1. 对低置信度样本按特征类型分类
2. 设定分层阈值和自动分流规则
3. 设计二次校验机制（规则引擎+人工复核）
4. 建立特殊情况的人工干预通道
5. 持续优化阈值和校验规则

## 适用场景

- 模型在长尾场景表现不稳定
- 样本量不足但业务价值高
- 人工复核成本过高成为瓶颈

## 不适用场景

- 样本纯度本身过低无法分类
- 业务可接受全人工复核
- 没有持续优化的工程资源

## 工具/环境

- 分类模型
- 规则引擎
- 人工复核平台
- 阈值调参系统

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

低置信度样本是模型落地的典型瓶颈，2025年提出的黄金漏斗方法通过分类+分层校验，在保持准确性的同时降低人工负担，是高级模型工程的关键技术

## 关联技能

- 待补充

## 来源

- 马易，AI落地场景识别

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
