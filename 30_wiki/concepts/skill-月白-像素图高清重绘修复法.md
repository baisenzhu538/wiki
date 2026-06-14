---
id: skill-月白-像素图高清重绘修复法
title: 技能：像素图高清重绘修复法
type: skill
status: draft
domain:
- design
source_person: 月白
source_context: 文创案例
source_refs: null
wiki_refs: null
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: 2026-06-07
pipeline:
- confidence-draft
author: legacy
reviewed_by: pending
confidence: 0.6
trust_level: low
---

# 技能：像素图高清重绘修复法

## 原始表述

像素图高清重绘修复法是月白在文创案例中提出的实操方法。

## 操作步骤

1. 判断问题为清晰度不足（像素点不够）而非构图需要扩图
2. 将模糊图片导入Liblib AI
3. 选择4K高清版本模型
4. 提示词仅写'高清同绘'或类似极简描述
5. 生成超高清版本，检查是否变形

## 适用场景

- AI生成图尺寸过小、DPI不足（印刷需150-300DPI）
- 图片放大后模糊，像素点不足
- 需要用于线下印刷的高清素材

## 不适用场景

- 图片清晰度足够，需要扩展画面边界（应使用扩图而非高清重绘）
- 矢量图无限放大场景（直接用AI等矢量软件）
- 图片变形、内容错误等非清晰度问题

## 工具/环境

- Liblib AI（4K高清版本）
- 豆包（备选，可能有奇怪观感）

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

扩图解决的是画面边界问题，高清重绘解决的是像素密度问题；Liblib的4K模型能在保持构图不变的前提下提升像素密度，避免印刷糊版

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
