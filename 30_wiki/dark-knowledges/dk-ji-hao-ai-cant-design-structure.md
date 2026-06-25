---

id: dk-ji-hao-ai-cant-design-structure
title: 暗知识：AI不会自己搞结构设计
type: dk
status: enriched
domain:
- ai-collaboration
- yitang
source_person: 纪浩
source_context: AI俱乐部·人和AI协作（第三次分享，2026-06）
source_refs:
- 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
- 10_raw/sources/src_20260617_50e2866a-ai俱乐部-人和ai协作-纪浩-五层结构-结构化.md
related:
  - '[[dk-modeling-ai-judgment-limit]]'
  - '[[dk-wanghuan-ai-lifts-personal-ceiling]]'
  - '[[dk-wanghuan-standard-by-iteration]]'
  - '[[dk-ban-fei-mao-silky-answer-warning]]'
  - '[[dk-wanghuan-magic-defeats-magic]]'
- '[[concept-ji-hao-ai-collaboration-methodology]]'
created_at: 2026-06-08
updated_at: '2026-06-19'
pipeline:
- confidence-draft
- confidence-source-cited
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 你给 AI 一个开放性任务，它产出的内容永远"看起来对"但无法直接落地
  lens: 结构缺失
  follow_up_question: 我是否已经先定义了输出框架、层级和判断标准？
- signal: 同一个任务反复 prompt，AI 每次给出的组织方式都不一样
  lens: 结构不稳定
  follow_up_question: 我是否把工作空间模板化、导诊台化，让 AI 只负责填充？
- signal: 团队里每个人用 AI 的产出格式不同，难以拼接
  lens: 协作结构未对齐
  follow_up_question: 是否在开始协作前约定好了统一的结构/字段/输出规范？
---
# 暗知识：AI不会自己搞结构设计

## 用一句话讲清楚

AI 是模式匹配系统，不是结构创造系统：它只能在你给出的结构里高效填充，不会主动为你创造正确的任务结构。

## 核心洞察

让 AI 做事的第一步不是写 prompt，而是先搭建一个结构化的工作空间。如果人不定义结构，AI 会在一个没有边界的空间里随机模糊地工作，产出质量完全看运气。

**纪浩的原话**："你的系统的架构都得由人来定义。AI不会自己搞这个。AI它不会说，哦，我应该把系统拆成这几部分。不会。AI只会在你给它的框架里填充内容。"

这也是人和 AI 协作中最容易被忽视的边界——人们常常以为把任务描述得越清晰，AI 就会越好地组织工作。但事实是，**结构设计是人的责任，不是 AI 的能力**。

## 边界 / 适用场景

| 场景 | 是否适用 | 说明 |
|---|---|---|
| 任务结构显而易见（如"写一个排序算法"） | ✅ 适用 | 结构已被问题本身限定，AI 可直接处理 |
| 使用成熟模板/框架（如 React、Django、五层结构） | ✅ 适用 | 框架已经替人完成了结构设计 |
| 研究性/探索性任务，允许自由发散 | ⚠️ 部分适用 | 结构可在探索中逐步浮现，但仍需人最终收敛 |
| 复杂协作任务，需要多人/多轮 AI 产出拼接 | ❌ 不适用 | 必须先由人定义统一的结构与标准 |
| 目标模糊，连"输出应该长什么样"都不确定 | ❌ 不适用 | 必须先由人澄清并搭建输出框架 |

## 失败模式 / 常见错觉

| 失败模式 | 常见错觉 | 纠正方式 |
|---|---|---|
| 把 AI 当成架构师，期望它自动拆分系统 | "我把需求说清楚了，AI 就知道该怎么组织" | 先自己画出结构，再让 AI 在结构中填内容 |
| 反复优化 prompt，却不优化工作空间 | "prompt 越精细，输出就越有组织" | 把重复出现的结构固化成模板/字段/导诊台 |
| 不同轮次/不同人拿到的 AI 产出格式不一致 | "AI 自然会把内容归类" | 在 prompt 前统一输出结构、字段名和验收标准 |
| 直接把开放性任务甩给 AI | "AI 比我更懂该怎么做" | 先缩小范围、定义边界、给出示例 |

## 行动 Checklist

- [ ] 在写 prompt 之前，先画出最终输出的结构（层级、字段、顺序）
- [ ] 把工作空间中可复用的结构固化成模板
- [ ] 为 AI 设定明确的"导诊台"：输入什么、按什么格式输出、边界在哪里
- [ ] 对复杂任务，先让 AI 在你的结构内填充，而不是让它自己创造结构
- [ ] 验收时先检查结构是否符合预期，再检查内容是否正确

## 相关卡 / 互链

- [[skill-纪浩-AI工作空间与导诊台设计法]] —— 工作空间搭建法就是"人帮 AI 搞结构设计"的具体实操，包含五大模块的搭建方法
- [[concept-ji-hao-ai-collaboration-methodology]] —— 这个暗知识是纪浩五层体系的基础性前提：如果人不做结构设计，五层体系本身就不存在
