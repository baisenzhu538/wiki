---
id: tool-月白-AI设计三段式里程碑流程
title: 技能：AI设计三段式里程碑流程
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
reviewed_by: 欧阳锋
reviewed_at: '2026-07-04'
confidence: 0.6
trust_level: low
related:
- '[[tool-月白-AIGC餐饮海报优化一抽流]]'
- '[[tool-月白-竞品图精益替换法]]'
- '[[tool-月白-关键要素提取改图法]]'
- '[[tool-月白-眼高手低训练法]]'
- '[[tool-月白-线下门店设计复杂度评估]]'
- '[[tool-月白-AIGC模型选型决策法]]'
- '[[tool-月白-AI逆向反推描述法]]'
- '[[tool-月白-一抽流改图法（自然语言精准许愿法）]]'
- '[[tool-月白-口喷式AIGC设计法]]'
- '[[tool-月白-模型识别与边界测试法]]'
tags:
- audience:executor
- scene:execution
- skill-level:beginner
---

# 技能：AI设计三段式里程碑流程

## 原始表述

AI设计三段式里程碑流程是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 里程碑一：调提示词与AI沟通→提示词迭代→生成初始图
2. 里程碑二：AIGC无限迭代优化→局部重绘→扩图
3. 里程碑三：人工精修改图（必须在前两步完成后才启动）

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
- src_unknown

## 为什么有效

过早人工介入会浪费AI批量迭代优势，过晚介入则无法修正底层问题

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决设计流程中"什么时候用AI、什么时候转人工"的决策混乱。很多设计师要么过早人工介入（浪费AI批量迭代优势），要么过度依赖AI（当AI产出不到位的底层结构问题时继续无效迭代）。三段式里程碑流程将AI设计过程分为三个清晰阶段：里程碑一纯靠提示词迭代生成初稿、里程碑二用AI做无限迭代优化（局部重绘/扩图）、里程碑三才启动人工精修。核心价值是为AI和人工的工作边界提供了明确的决策节点。适用于AI生图项目、产品图批量生成、海报迭代优化的全流程管理。

## 质疑

- **具体假设**：该工具假设结构化方法论本身能产生正确结论，但方法论只是框架——结论质量取决于输入数据的质量和执行者的判断力。
- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效——工具的有效性高度依赖场景的稳定性。
- **反例**：一个团队完整执行了所有步骤，产出了漂亮的文档，但核心假设从一开始就是错的——流程的完整性掩盖了判断的缺陷。
- **前提**：使用者已具备该领域的基础认知，能正确理解和执行工具规则，且数据来源具有代表性。

三段式里程碑假设了流程的线性推进，忽略了设计实践中常见的"回退"需求。**John Maeda**指出，设计流程本质上是循环的而非线性的——里程碑三的人工精修经常暴露需要回到里程碑一重新调整提示词的底层问题。如果严格按照三段式不回溯，设计师在三阶段可能被迫在错误的基础上打补丁。**Sarah Gibbons**（Nielsen Norman Group副总裁）从UX视角批评，过于强调流程里程碑会扼杀设计师在过程中的直觉判断——有时一个有经验的设计师看一眼AI产出就知道需要推倒重来，而三段式会让他"按要求"走完整个流程。里程碑思维适用于新手设计师建立纪律，但对资深设计师而言可能是不必要的约束。
