---

id: sk-ai-evidence-check
title: 技能：AI输出证据核查三问法
type: tool
status: reviewed
domain:
author: 半肥猫
reviewed_by: 欧阳锋
confidence: 0.88
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地分享，2026-06
aliases:
  - AI输出证据核查三问法
  - audience:executor
  - scene:execution
  - skill-level:intermediate
  - 半肥猫
  - 技能
  - 技能：AI输出证据核查三问法
  - 没有人呀现在
  - 证据核查三问法
  - 输出证据核查三问法
source_refs:
wiki_refs: null
discoverable_by:
  - 技能：AI输出证据核查三问法
  - AI输出证据核查三问法
related:
tags:
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required: null
prerequisite_skills: null
definition_of_done: null
trust_level: medium
---
# 技能：AI输出证据核查三问法

## 用一句话讲清楚

每次AI给出结论后，用“依据是什么、有无具体证据、是否来自上下文”三问，快速识别并阻断AI的编造风险。

## 核心要点

- src_unknown
- src_unknown
- src_unknown

## 边界

- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败信号 | 典型表现 | 应对动作 |
|---|---|---|
| Q1 无依据 | AI只给结论，无法说明来源 | 要求重新回答并给出依据 |
| Q2 证据模糊 | 只有概括描述，无具体数据/案例 | 要求在提供的上下文内寻找，或承认不确定 |
| Q3 来源混淆 | 把AI补充信息包装成输入事实 | 要求逐条标注“来自上下文”/“AI补充” |
| 跳步执行 | 只问一遍或没有后续动作 | 强制按 Checklist 逐项验收后再进入下一步 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown

## 来源

- src_unknown
- 10_raw/sources/src_20260606_90b44191-没有人呀现在.md

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

**Gary Marcus**（纽约大学认知科学家，《Rebooting AI》作者）会质疑：三问法假设 AI 的编造风险可以通过事后核查阻断，但当前大模型的"幻觉"问题本质上是训练数据缺陷导致的——核查可以发现"有没有引用"，但无法判断"引用本身是否真实存在"。

- **具体假设**："三问法"假设 AI 的编造风险可以通过事后核查阻断，但如果 AI 在推理过程中已经基于错误前提生成了自洽的论证链，三问法只能检查"有没有依据"，无法检查"依据本身是否正确"。
- **边界**：三问法适用于事实型输出（数据引用、来源追溯），但对推论型输出（如策略建议、创意方案）的核查价值有限——推论没有"证据"但有"逻辑链"。
- **反例**：当 AI 的输出完全来自训练数据（而非上下文），三问法中的"是否来自上下文"一问会得到诚实回答"不是"，但这并不意味着输出是错误的——可能只是模型的内化知识。
- **前提**：框架假设用户有足够领域知识来判断"证据是否具体"，但对于新手用户，模糊证据和具体证据的区分本身就很困难。
