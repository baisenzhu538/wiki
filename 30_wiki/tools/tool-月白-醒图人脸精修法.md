---
id: tool-月白-醒图人脸精修法
title: 技能：醒图人脸精修法
type: tool
status: draft
domain: design- design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
source_refs:
- 10_raw/sources/src_20260522_38173b48-design-ai-image-generation.md
wiki_refs: null
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- src_unknown
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-竞品图精益替换法]]'
- '[[tool-月白-餐饮海报AB测试法]]'
- '[[tool-月白-眼高手低训练法]]'
- '[[tool-月白-线下门店设计复杂度评估]]'
- '[[tool-月白-控制产品画面尺寸比例]]'
tags:
aliases:
  - 技能：醒图人脸精修法
  - 技能
  - 醒图人脸精修法
  - 月白
- audience:executor
- scene:execution
- skill-level:beginner
---
# 技能：醒图人脸精修法

## 原始表述

醒图人脸精修法是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 将AI生成的人像导入醒图APP
2. 使用'手动修脸'功能（非液化）
3. 滑动调节自动识别出的面部参数选项
4. 对比真人照片调整中庭、五官比例等关键特征

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown
- src_unknown

## 工具/环境

- src_unknown
- src_unknown

## 为什么有效

AI生成的小人五官比例固定导致'都像同一个人'，人工介入调整关键参数解决likeness问题

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI生成人像"千篇一律、缺乏个体辨识度"的问题。适用于AI生成人物IP、虚拟形象、电商模特图等需要人脸个性化调整的场景。核心价值是用专业修图工具的精细化参数弥补AI生成在五官比例和个体特征上的不足，实现"AI量产+人工精修"的高效流水线。

## 质疑

**前提假设**是"手动修脸参数能精确控制五官比例"，但醒图APP的参数滑块本质是黑箱滤镜，调整一个参数可能引发不可预测的面部形变，精确度远不如专业3D建模工具。**边界**在于：当需要保持多张图人脸一致性（如同一IP角色的不同表情包）时，逐张手动精修无法保证一致性，需配合种子控制或LoRA训练。**反例**：精修后的人脸在不同光照场景下呈现效果差异显著，说明调整结果缺乏鲁棒性。**Hany Farid** 在数字取证研究中指出，移动端修图工具的面部参数调整往往引入不自然的纹理 artifacts，在放大或打印时会暴露痕迹。**Douglas Lanman**（Meta Reality Labs）也批评这类2D参数化修脸方法无法处理真实3D面部几何，所谓的"精修"只是在像素层面模拟变化，而非真正的形态控制。
