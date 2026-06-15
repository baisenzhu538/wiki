---
id: skill-月白-AIGC文字大小精确控制
title: 技能：AIGC文字大小精确控制
type: skill
status: draft
domain:
- design
source_person: 月白
source_context: 文创案例 （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
source_refs:
- source_unknown
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
---
# 技能：AIGC文字大小精确控制

## 原始表述

AIGC文字大小精确控制是月白在文创案例中提出的实操方法。

## 操作步骤

1. 首选方案：直接指定像素值，如'18px''20px''超大标题字号'
2. 备用方案：要求AI'去掉产品上的小字'，避免小字糊掉
3. 终极方案：AI出图后，用稿定设计等工具手动填入精确文字
4. 权衡性价比：评估修改成本vs重新生成成本

## 适用场景

- AIGC生成图中文字大小不符合要求
- 产品图/徽章等小字需要清晰
- 大标题需要突出层级

## 不适用场景

- 文字极多且排版复杂的场景（AI难以控制）
- 需要特殊字体/品牌字体

## 工具/环境

- 豆包AI
- 稿定设计
- 其他在线设计工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

当前AIGC对小字控制仍不稳定，尤其是产品级小字；明确指定像素值可提升成功率，但需知边界，必要时人工介入保证效果

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
