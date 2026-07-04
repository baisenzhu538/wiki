---
id: tool-月白-控制产品画面尺寸比例
title: 技能：控制产品画面尺寸比例
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
updated_at: '2026-06-29'
pipeline:
- src_unknown
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-多窗口并行工作法]]'
- '[[tool-月白-竞品图精益替换法]]'
- '[[tool-月白-餐饮海报AB测试法]]'
- '[[tool-月白-眼高手低训练法]]'
- '[[tool-月白-线下门店设计复杂度评估]]'
- tool-yitang-reverse-data-analysis
---
# 技能：控制产品画面尺寸比例

## 原始表述

控制产品画面尺寸比例是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 方法一：给出具体尺寸数据（如800×400像素）+参考图，重复强调尺寸约束
2. 方法二：产品旁放置参照物（如手机）建立比例关系
3. 上传带参照物的图片作为参考
4. 让AI理解相对比例

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

AI对绝对尺寸理解有限，具体像素数据或相对参照物能建立可感知的比例约束

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI生成产品图时比例失调、产品失真这一常见痛点。AI模型对绝对物理尺寸的理解有限，经常产出门把手比车身还大、手机比例被拉长压扁等诡异结果。方法提供两种互补策略——给出具体像素数据（800×400）+重复强调约束，或在产品旁放置参照物（如手机、硬币）建立相对比例关系——让AI通过数据或类比感知正确的尺寸关系。适用于产品电商图生成、包装设计预览、需要对尺寸有严格要求的工业设计可视化等场景，尤其适合没有3D建模能力但需要准确产品展示的设计师。

## 质疑

**William J. Mitchell**（数字影像理论家）会指出：AI并不真正"理解"尺寸和比例。给出像素数据或放置参照物本质上都是提示词的修辞策略——AI只是在其训练数据中寻找与这些描述相关的最匹配视觉模式，而非进行任何物理模拟。这意味着方法的成功是统计巧合而非可靠工程，结果无法保证重复性。同一组提示词下一次生成可能比例完全错误。

**Hany Farid**（计算机视觉研究者）会批评：参照物方法引入了一个往往被忽略的问题——参照物本身的识别准确度。AI对"手机""硬币"等参照物的视觉理解也存在偏差，不同品牌、型号、年代的手机外观差异巨大，AI可能将老式翻盖手机和新款全面屏手机混为一谈，导致参照物本身就不可靠。两个"不准确"相乘，结果的不确定性更高。
