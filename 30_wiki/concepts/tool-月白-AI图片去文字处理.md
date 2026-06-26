---
id: tool-月白-AI图片去文字处理
title: 技能：AI图片去文字处理
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
- '[[tool-月白-AI图片风格逆向提取（抄图法）]]'
- '[[tool-月白-产品反光修复术]]'
- '[[tool-月白-Token效价比决策公式]]'
- '[[tool-月白-控制产品画面尺寸比例]]'
- '[[tool-月白-AIGC橱窗陈列设计流程]]'
---
# 技能：AI图片去文字处理

## 原始表述

AI图片去文字处理是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 获取带文字的产品原图
2. 使用AI指令：'去掉产品上面图片中的所有文字'
3. 生成无文字版本
4. 后期用PS手动添加正确文字贴图

## 适用场景

- 产品图原有文字会AI变形
- 需要保持品牌文字准确
- 接到真实客户订单有标准贴图

## 不适用场景

- 产品无文字
- 允许AI生成装饰性文字

## 工具/环境

- 豆包AI
- PS

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI生成产品文字99%会乱码变形，先去除再后期添加是唯一可靠方案；Cubox等AI修复字体工具效果不稳定且字体可能不一致

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
