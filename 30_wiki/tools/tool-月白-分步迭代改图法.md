---
id: tool-月白-分步迭代改图法
title: 技能：分步迭代改图法
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
reviewed_by: 欧阳锋
reviewed_at: '2026-07-04'
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-多窗口并行工作法]]'
- '[[tool-月白-竞品图精益替换法]]'
- '[[tool-月白-餐饮海报AB测试法]]'
- '[[tool-月白-线下门店设计复杂度评估]]'
- '[[tool-月白-控制产品画面尺寸比例]]'
- tool-纪浩-问题导向备课法
- productization-judgment
---
# 技能：分步迭代改图法

## 原始表述

分步迭代改图法是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 第一轮：找出最不满意的核心问题（限1-3个）
2. 针对性修改提示词
3. 生成新图
4. 第二轮：在已改进基础上再找新问题
5. 继续修改
6. 重复直至满意
7. 最后才用PS处理字体等细节

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

AI单次理解有限，分步聚焦避免指令混乱；不跳步保证每个环节质量，最终累积出优质结果

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI生图中"一次给太多指令导致全部跑偏"的问题。AI单次理解能力有限，如果同时要求修改构图、配色、材质、光影、比例，指令之间会产生冲突，最终哪个都没改好。分步迭代改图法要求每轮只聚焦1-3个核心问题，解决后再进入下一轮，最后用PS处理字体等细节。适用于需要多维度优化的复杂设计图，尤其是AI生成初稿后的迭代改进阶段。

## 质疑

分步迭代的时间成本在多轮修改中快速膨胀。**David Carson**（著名平面设计师）质疑，设计不是"修bug"——你不能像程序员修代码一样逐行改设计，因为视觉元素之间存在不可分割的格式塔关系。每次只改一个维度，可能解决了一个问题却破坏了整体协调性。**Hannah Williams**（AIGC产品经理）指出，多轮迭代意味着每次都要消耗新的API调用成本，且每轮之间AI可能"忘记"前一轮的上下文，导致改A时破坏了B。对于时间紧迫的商业项目，快速多开几组并行生成并选最优结果，往往比分步迭代更高效。
