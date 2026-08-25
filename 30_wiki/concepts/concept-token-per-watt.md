---
id: concept-token-per-watt
title: Token per Watt：词元经济的核心 KPI 与电力定价权
type: concept
status: reviewed
confidence: 0.85
trust_level: high
domain:
- strategy
- ai-saas
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-08-26'
updated_at: '2026-08-26'
source_person: 方振义（拆书口述者）
source_context: 拆书会《词元经济》方振义口述——书中观点与口述者判断分层标注，转述二等（原书一等）
source_refs:
- 00_inbox/拆书-词元经济-方振义-口述.txt
aliases:
- Token per watt
- 每瓦特词元
- 电力定价权
- 一度电的故事
discoverable_by:
- token per watt
- 电力成本
- 绿电算力
- 词元成本
related:
- '[[framework-token-economy-three-layer]]'
- '[[concept-agent-as-token-consumer]]'
- '[[dk-token-economy-critical-reading]]'
tags:
- audience:general
- scene:reference
- skill-level:intermediate
- 词元经济
- 电力
- 能效
- 定价权
- 概念
---

# Token per Watt

> 本卡属于 `framework-token-economy-three-layer` 的成本侧子卡——解释「为什么电力决定词元定价权」。

## 一句话

黄仁勋提出的 **Token per Watt**（每瓦特产出词元数）是词元经济的核心 KPI——电力占数据中心成本 60-70%，谁拿到更低电价、谁单位电力产出更多 token，谁就握有定价权；**词元竞争的本质是效率竞争**。

## 1° 电的故事（书引，定价权直觉泵）

- 新疆戈壁光伏 1° 电 = **0.15 元**，卖给当地居民还是 0.15 元
- 卖到上海 = 0.6 元（翻 3-4 倍）
- 通过 GPU 转成 token 卖给全球 = **几美元到 10 美元**——超过 **100 倍**增值

同一度电，形态转换（电→算力→词元）带来数量级溢价。这就是「词元工厂=印钞机」叙事的来源——但注意批判层：印钞机叙事忽略了折旧、运维、模型迭代和价格战（见 dk-token-economy-critical-reading）。

## 成本锚点（书引数据，标注口径）

- 电力占 AI 数据中心运营成本 **60-70%**（10 块钱办厂，6-7 块是电费）
- 生成 100 万 token 平均耗电 **15-20 度**：美国约合 22 元人民币 vs 中国西部约 3 元——**成本 1/6~1/10**
- 绿电案例（书引）：字节乌兰察布电价 0.28 元（比东部省 30%）；阿里宁夏绿电占比 90%

> 以上均为原书转述数据，**待独立核实**；方向（西部绿电成本优势）与公开报道一致，具体数字引用时保留本注。

## 口述者补充层（避坑）

方振义调研后警告：**不是所有西部绿电都赚钱，也不是所有西部绿电都跟 AI 有关——只有少部分有**（L98-104）。投资绿电概念要逐个看财报：哪些电厂真赚钱、真和 AI/绿电相关——这是作业不是结论（绿电幸存者偏差，详见 dk 卡）。

## 与其他知识的关联

- `framework-token-economy-three-layer`：本卡是生产公式「成本三要素」中电力项的展开
- `concept-agent-as-token-consumer`：效率竞争的需求侧背景（token 消耗爆炸放大能效价值）
