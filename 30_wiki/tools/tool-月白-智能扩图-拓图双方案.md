---
id: tool-月白-智能扩图-拓图双方案
title: 技能：智能扩图/拓图双方案
type: tool
status: draft
domain:
- design- design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
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
- '[[tool-月白-Token效价比决策公式]]'
- '[[tool-月白-AI图片去文字处理]]'
- '[[tool-月白-餐饮海报AB测试法]]'
- '[[tool-月白-线下门店设计复杂度评估]]'
- '[[tool-月白-控制产品画面尺寸比例]]'
---
# 技能：智能扩图/拓图双方案

## 原始表述

智能扩图/拓图双方案是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 方案一（PS）：新版PS使用'图片扩展'或'扩展画布'功能直接扩图
2. 方案二（AI）：将产品P到白底图，标注白色区域
3. 使用指令：'填充画面中的白色色块，要按照图片[方向]的场景去延伸'
4. 多次生成抽卡直到满意

## 适用场景

- 原图尺寸不够
- 需要特定比例适配平台
- 画面某边缺失需要补全

## 不适用场景

- 原图构图完整无需扩展
- 扩展方向场景极其复杂

## 工具/环境

- 新版PS
- 豆包AI扩图

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

PS扩展最快捷，AI扩展更智能能理解场景延续；标注'按左边场景延伸'给AI明确的方向参考，避免自由发挥偏离

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
