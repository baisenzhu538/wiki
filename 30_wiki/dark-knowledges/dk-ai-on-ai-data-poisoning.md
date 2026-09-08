---
id: dk-ai-on-ai-data-poisoning
title: AI 叠加 AI 的数据是给自己投毒：二手生成数据入库禁令
type: dk
status: draft
domain:
- ai-data
- ai-collaboration
confidence: 0.9
trust_level: medium
author: 老顽童
reviewed_by: 待审
created_at: '2026-09-08'
updated_at: '2026-09-08'
source_person: Truman
source_context:
- 一堂-AI数据必修课·认知篇
- yitang
quality_labels:
- insight
- principle
reuse_direction: "数据入库前质检、数据湖分区设计、训练/测评数据原料筛选、RAG 语料清洗"
aliases:
- AI叠加AI投毒
- AI on AI 数据投毒
- 二手生成数据禁令
- 一堂-AI数据第一课口述02
discoverable_by:
- AI 叠加 AI 数据投毒
- AI 生成数据 失真 幻觉 入库
source_refs:
- 00_inbox/AI-study/AI数据/一堂-AI数据第一课口述02.txt:1164-1190
- 60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md
related:
- '[[framework-adaptive-data-flywheel]]'
- '[[tool-data-governance-four-layers]]'
- '[[concept-data-three-constants-three-shifts]]'
- '[[dk-data-timely-review]]'
- '[[case-truman-bedtime-story-datapack]]'
tags:
- audience:general
- scene:data-quality
- skill-level:intermediate
- content-format:dk
- source-person:Truman
- 数据治理
- 数据质量
- 数据投毒
---

# AI 叠加 AI 的数据是给自己投毒：二手生成数据入库禁令

> **定位**：一堂「AI数据必修课·认知篇」暗知识（#683 任务包 7/8）——`[[framework-adaptive-data-flywheel]]` 收集步「入库三判断」中最重要的一条否定性规则：湖仓思维鼓励什么都存，但有一类数据「还不如别存」。

## 原始表述

> 口述02 L1172-1190：
> 「你们一定要警惕一类数据叫 AI 叠加 AI 的叠加数据……如果他是基于事实的数据，再怎么着都是可靠的，再怎么着都还行。怕的是它本来就是 AI 生成的东西，然后你让 AI 再分析 AI 生成的东西，叠加来叠加去之后，你觉得是一个看上去很好的数据，其实里面大量的失实、失真、幻觉可能全在里面。这种数据还不如别存，还不如别输，非常重要非常重要……一次 AI 生成的其实可能还好，但是 AI 叠加也真的要特别谨慎。你就给自己在投毒，本来那个数据就不靠谱，你叠加不靠谱，它是用不稳定数据叠加的。」

## 使用场景

- 数据湖/知识库入库质检：判断一条数据该不该存
- RAG 语料清洗：AI 摘要、AI 改写稿、AI 生成的「最佳实践」混入语料库
- 训练/测评数据原料筛选：拿 AI 生成的 Q&A 对当训练样本
- 用 AI 分析 AI 的产出再存档：让 AI 总结另一段 AI 对话/AI 文章并入库

## 操作方法

1. **溯源标注**：入库时给每条数据标来源属性——事实原始数据（录音/交易凭证/真人聊天记录/原始文档）vs AI 生成数据（摘要/改写/合成问答）。
2. **一次生成可容忍，叠加要警惕**：AI 一次生成（如让 AI 把录音提纯成文稿，原料是事实）风险可控；风险在「原料本身是 AI 生成物」的二次加工。
3. **分区存放**：AI 生成数据与事实数据分区/打标隔离，禁止混同权重进入检索与训练。
4. **用途限制**：AI 二手数据禁止作为训练集、黄金测评集、事实型知识库的原料；可作参考线索，但必须回溯到事实源核验后才能升格。
5. **定期巡检**：统计数据湖里「AI 生成占比」——占比持续上升就是投毒进行时。

## 适用边界

- 适用于：事实敏感型数据（知识库、训练原料、测评集、经营决策依据）。
- 不适用于（容忍度高的场景）：创意类任务的多样性合成（如 `[[case-truman-bedtime-story-datapack]]` 阶段 4 用 AI 生成 30 选题创意库）——创意场景「失实」不是缺陷是特性，但这类合成数据应标注用途，不得回流事实库。
- 「一次 AI 生成可能还好」的前提是原料为事实（如语音转写提纯）；原料即生成物时不适用此豁免。

## 为什么值钱

1. **错误会自我强化**：AI 生成物已含幻觉与失真，再被 AI 分析、总结、引用，错误被包装成「看上去很好的数据」层层固化，且无法回溯证伪——负向复利。
2. **污染的是整个飞轮**：数据飞轮（`[[framework-adaptive-data-flywheel]]`）的前提是每轮循环增值；投毒数据让收集、处理、使用、反馈全部环节在错误原料上空转，转得越快中毒越深。
3. **纪律成本低、收益大**：只需入库时一个来源标注动作，就能避免「大量失实、失真、幻觉全在里面」的系统性风险——是数据治理（`[[tool-data-governance-four-layers]]` 防污染）性价比最高的一招。

## Critique

- **内部局限**：「一次生成还好、叠加谨慎」的边界是经验判断，没有给出可操作的叠加次数阈值；实操中「原料纯度」本身是连续谱（AI 辅助写作的文章算几手？），需要组织自行定标。
- **外部攻击（合成数据研究视角）**：机器学习界对合成数据并非全盘否定——受控合成数据（self-instruct、蒸馏）在特定场景有效；本戒律的准确读法是「无溯源、无核验的二手生成数据禁止混入事实原料」，而非「一切 AI 生成内容皆毒」。关键在标注与隔离，不在绝对禁止。

## 与其他知识的关联

- 与 `[[framework-adaptive-data-flywheel]]` 收集步配套：湖仓思维（先存再说）的正向规则 + 本卡（AI 叠加 AI 别存）的否定规则，合起来才是完整入库策略。
- 与 `[[tool-data-governance-four-layers]]`「防污染」同构：本卡是防污染在个人/团队数据习惯层的落点。
- 与 `[[concept-data-three-constants-three-shifts]]`「错误数据崛起」的张力：错误数据（Not Do List）作为训练对齐材料宝贵，但 AI 生成的错误数据不是「真实的错误」而是幻觉——前者要收，后者要防。
- 与 KDO 自身实践同构：KDO 以「raw sources are the source of truth」（AGENTS.md Prime Directive）、wiki 不作真相源——正是本戒律在知识工厂的制度化。

## kdo query 检索记录（宪法第六条 / 验收标准 §3）

> 检索日期 2026-09-08（诊断报告 §一 实锤，照抄不重查）。

| # | 查询词 | 有效命中 | 结论 |
|:-:|:--|:--|:--|
| 10 | Adaptive数据飞轮 预判 识别 收集 处理 使用 反馈 治理 | 0 直中 | 收集步配套暗知识零覆盖佐证 |
| 1 | AI数据 数据供给 数据标注 数据分层 | 0（Top5 全为近邻域卡） | 域级查重佐证 |
