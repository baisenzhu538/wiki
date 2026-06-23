---




id: skill-月白-提示词长度控制法
title: 技能：提示词长度控制法
type: "tool"
status: draft
domain:
  - design- design
source_person: 月白
source_context: AI设计基础 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
  - src_20260522_38173b48-design-ai-image-generation
wiki_refs: null
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- confidence-draft
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - '[[skill-月白-课程问题预埋法]]'
  - '[[skill-月白-背景消除与分辨率修复]]'
  - '[[skill-月白-AI需求拆解咨询法]]'
  - '[[skill-月白-用一堂方法论找最佳实践并拉满执行]]'
  - '[[skill-月白-三步作业反馈法]]'

---
# 技能：提示词长度控制法

## 原始表述

提示词长度控制法是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 判断任务复杂度：简单修复/标准生成/复杂创意
2. 简单任务（如文字修复）：用超短提示词（10-30字）
3. 标准任务：用中等长度提示词（100-300字）
4. 复杂创意任务：可用超长提示词（1000字+），但需标注优先级
5. 测试验证：对比不同长度的生成效果
6. 识别有效提示词：保留触发关键效果的，删除干扰项

## 适用场景

- 提示词效果不稳定时
- 需要优化生成效率时
- 模型有输入长度限制时（如即梦800字限制）

## 不适用场景

- 已经找到最佳提示词长度且效果稳定
- 盲目追求长或短而不测试

## 工具/环境

- 各AI生图平台
- 提示词测试记录文档

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

提示词不是越长越好，关键在于有效信息的密度；超长提示词容易稀释重点，超短提示词可能信息不足；'够用就好'是核心原则，需根据模型特性和任务类型动态调整

## 关联技能

- 待补充

## 来源

- 月白，AI设计基础

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
