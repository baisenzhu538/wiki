---




id: skill-月白-产品反光修复术
title: 技能：产品反光修复术
type: "tool"
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
  - '[[skill-月白-多窗口并行工作法]]'
  - '[[skill-月白-AI图片风格逆向提取（抄图法）]]'
  - '[[skill-月白-餐饮海报AB测试法]]'
  - '[[skill-月白-AI图片去文字处理]]'
  - '[[skill-月白-眼高手低训练法]]'

---
# 技能：产品反光修复术

## 原始表述

产品反光修复术是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 生成基础场景图后检查材质反光
2. 发现不锈钢/玻璃反光不正确时
3. 使用指令：'给产品中的[材质]添加符合场景反光'
4. 重新生成验证反光一致性

## 适用场景

- 产品含不锈钢、玻璃、镜面等反光材质
- AI生成图保留了原产品图的错误反光
- 追求真实感的产品图

## 不适用场景

- 产品无反光材质
- 风格化设计不需要真实反光

## 工具/环境

- 豆包AI

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI容易保留原产品图的'锈光'或错误反光，必须显式指令让AI根据新场景重新计算环境光反射

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
