---
id: tool-月白-AI高清重绘去模糊
title: 技能：AI高清重绘去模糊
type: tool
status: draft
domain:
- design- design
source_person: 月白
source_context: 文创案例 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
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
- '[[tool-月白-AI平台算法咨询法]]'
- '[[tool-月白-AI生成棉花娃娃形象]]'
- '[[tool-月白-口喷式设计工作流]]'
- '[[tool-月白-表情包风格筛选与确定]]'
- '[[tool-月白-AIGC生成人物证件照]]'
---
# 技能：AI高清重绘去模糊

## 原始表述

AI高清重绘去模糊是月白在文创案例中提出的实操方法。

## 操作步骤

1. 确认问题是清晰度不足而非画幅不够
2. 选择LiblibAI的4K高清模型
3. 输入提示词：'高清''同风格重绘'
4. 获取超高清4K版本
5. 检查是否有变形，必要时重新生成
6. 禁止扩图操作（解决的是构图非清晰度）

## 适用场景

- 图片像素不足、模糊
- 需要印刷级高清大图
- 原始素材分辨率低

## 不适用场景

- 图片清晰但需要更大画幅（用扩图）
- 矢量文件需要缩放
- 图片本身质量极差，AI无法识别内容

## 工具/环境

- LiblibAI（推荐）
- 豆包（备选，可能有奇怪观感）

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

清晰度问题是像素点不足，扩图只增加边界宽度；专门的4K高清重绘能在保持原构图和内容不变的前提下提升像素密度

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
