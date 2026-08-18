---
id: dk-research-sampling-correction-three-rounds
title: 打样纠偏三轮法：5-10 个样本定颗粒度
type: dk
status: reviewed
reviewed_by: 待审
review_date: 2026-08-16
author: 老顽童
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- research
- ai-collaboration
aliases:
- 打样纠偏三轮法
- 5到10个样本定颗粒度
- 打样定方向
- 爆炸式调研
- 马易
- 爆炸式调研-下-口述
source_person: 马易
source_context: Live259 爆炸式调研（2026-08-11 口述）——打样纠偏（下 L3762-3768，一堂课表案例）
source_refs:
- 00_inbox/爆炸式调研/爆炸式调研-下-口述.txt
related:
- '[[framework-baozhashidiaochan-five-step]]'
- '[[case-design-principles-90]]'
- '[[dk-research-classification-mece-table]]'
- '[[concept-research-saturation-coverage]]'
- '[[tool-nine-character-mantra-14-strategies]]'
- '[[framework-r-type-research-partner-five-state]]'
- '[[dk-research-total-anchor-private-library]]'
- '[[dk-ai-collaboration-degradation-spiral]]'
- bridge-how-to-know-person-to-business
- case-cross-xingangwan-pharma
tags:
- audience:executor
- scene:execution
- skill-level:beginner
---
# 打样纠偏三轮法：5-10 个样本定颗粒度

> **定位**：属于 [[framework-baozhashidiaochan-five-step]] 的搜索⇄建模循环——打样定颗粒度

## 原始表述

> 「之所以给你们 5 到 10 个用来打样的，如果你们最后的结果这 5 到 10 个特别理想，如果不是你一定要跟他调好。」（口述下 L3764）
> 「你看你打好了，我们就要丢手了……这个案例一定程度上决定了后面所有工作的方向，一定要跟他磨合，一定要磨合。」（L3766-3768）
> 一堂课表案例：每个叶子节点就是一节课的颗粒度，一定要纠偏（L3760-3762）

## 使用场景

- 开始大规模 AI 分类/建模前——先用 5-10 个样本打样定颗粒度
- 颗粒度不对（太粗/太细）时——纠偏后再放量
- 任何"样本决定方向"的建模任务（课表/案例库/分类树）

## 操作方法

1. **取 5-10 个样本打样**：让 AI 先处理一小批样本，观察颗粒度是否合适
2. **检查颗粒度**：叶子节点的粒度（如"一节课"级 vs "一张地图"级）是否匹配需求
3. **纠偏**：结果不理想就调——颗粒度太粗就细化，太细就合并
4. **打样达标才放量**：5-10 个打样理想后"丢手"，让 AI 按此颗粒度处理全量
5. **持续磨合**：打样案例决定后面所有工作的方向（L3768）——先磨好再放量

## 适用边界

- 适用于 AI 大批量分类/整理任务；小批量任务直接做不需要打样
- 打样样本要有代表性（覆盖不同类别）——全同质样本打样无意义
- 颗粒度标准依赖人判断——需求不清时先定义"叶子节点"是什么

## 为什么值钱

- **成本控制**：5-10 个样本纠偏 vs 全量返工——打样是"小成本试错"
- **方向锁定**：颗粒度决定后面所有工作方向，错了全错（L3768）
- **AI 对齐**：打样让 AI 理解你的颗粒度标准，放量后少跑偏

## Critique

- **反驳**：打样 5-10 个太主观，换个样本结果不同——所以强调"代表性样本+持续磨合"，且打样达标才放量。
- **反驳**：颗粒度可以边做边调，不需要专门打样——大规模任务返工成本高，打样是廉价的保险。
- **条件**：此 dk 前提=任务量大到值得打样；一次性小任务直接做。
- **注意**：打样阶段是最佳纠偏时机——放量后再纠偏=浪费 token（饱和自证同构）。

## 与其他知识的关联

- `framework-baozhashidiaochan-five-step`：搜索⇄建模循环中的"打样定颗粒度"动作
- `case-design-principles-90`：四轮打样纠偏（92→90）的完整实证
- `dk-research-classification-mece-table`：打样后进入分类选择（流程衔接）
- `concept-research-saturation-coverage`：打样颗粒度=饱和建模的粒度基准
- `tool-nine-character-mantra-14-strategies`：纠偏 09 问题边界/13 分析方向
- `framework-r-type-research-partner-five-state`：饱和送阶段的打样机制
- `dk-research-total-anchor-private-library`：打样后总量锚定（一堂课表案例连用）
- `dk-ai-collaboration-degradation-spiral`：不打样直接放量=跑偏的退化起点
- `bridge-how-to-know-person-to-business`：从人到企业——调研本质是理解人与企业（跨域桥）
- `case-cross-xingangwan-pharma`：山西药房新政调研——饱和调研方法的决策域实证（跨域）
