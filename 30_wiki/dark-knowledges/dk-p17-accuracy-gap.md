---
id: dk-p17-accuracy-gap
title: 'P-17：auto_label 声称"85%准确率"——实测34.8%，差距来自被忽略的5个维度'
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-17
source_refs:
- .agent/pitfalls.md#P-17
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- '[[dk-p15-unverified]]'
- '[[dk-f14-accuracy-measurement-mismatch]]'
- '[[master-decision-hygiene]]'
- '[[master-ai-info-literacy]]'
- '[[gold-standard-manual-labels]]'
pipeline:
- confidence-enriched
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 听到高准确率声明但缺少数据集、覆盖维度、计算公式与缺标维度处理说明
- 调优前后数字对比时没有独立的 Gold Standard 基线测量
- 报告中只展示部分维度或成功样本的准确率
---

# P-17：auto_label 声称“85%准确率”——实测34.8%，差距来自被忽略的5个维度

## 原始表述/核心洞察

> **症状**：黄药师说"提示词调优后准确率做到了85%"。欧阳锋用 Gold Standard（15条手工标注 chunk）独立验证，实测34.8%（47/135）。差距巨大。黄药师的"85%"只算了管线实际在标的 4 个维度（chunk_type/method_family/audience/perspective），忽略了另外 5 个维度（platform/confidence/prerequisite_knowledge/expiry/usage_depth）全线 `<missing>`。
>
> **根因（2层）**：
> 1. **测量口径不同**：黄药师测的是部分维度局部准确率，欧阳锋测的是全维度全样本准确率。双方没有约定统一的测量方法和数据集。
> 2. **缺少gold standard基线比对流程**：没有在调 prompt 之前先跑一遍 baseline 确认当前准确率，导致"进步"和"绝对水平"被混淆。
>
> **对策**：
> - **任何"准确率"声明必须附带测量方法**：用了什么数据集？覆盖哪些维度？计算方式？
> - **Gold Standard 必须跑 full comparison**：不能只挑管线能标的维度算——缺标的维度也要报告
> - **调 prompt 前先跑 baseline**：改 prompt 之前先跑一遍 `_verify_gold_standard.py`，确认起点
> - **所有自动标注管线的性能评估以 Gold Standard 为唯一基准**
>
> **关联**：P-15（声称完成未验证）的同一种病的不同表现——这次不是"没做"，而是"测了但测的是错的指标"。

**核心洞察**："准确率"不是一个单一数字，而是一套测量口径。如果口径只覆盖部分维度、排除缺标样本、没有 Gold Standard 基线，那么高准确率只是局部优化的幻觉，不能代表系统真实水平。

## 使用场景

- 你需要评估一个自动化管线的准确率
- 你收到了一个高准确率声明，需要独立验证
- 你正在调优 prompt 或模型，需要知道"真正的起点"是多少
- 你需要建立一套可重复的测量标准

## 操作方法

1. **准确率声明必须附带测量方法**：
   - 用了什么数据集？（多少条？怎么采样的？）
   - 覆盖哪些维度？（全部还是部分？）
   - 计算方式是什么？（每个维度单独算还是联合算？）
   - 缺标的维度怎么处理？（排除还是算错？）

2. **建立 Gold Standard 基线**：
   - 在调优之前先跑一遍当前基线（baseline）
   - 使用统一的数据集和评估方法
   - 记录每次调优的增量，而不是绝对值

3. **独立验证流程**：
   - 开发者报一个数字
   - 审查者用独立的数据集和脚本验证
   - 双方数字一致 = 可信；不一致 = 排查测量方法差异

4. **报告完整性**：
   - 不能只报"能标的维度"的准确率
   - 必须报告"全部维度"的准确率，包括缺标的
   - 如果部分维度缺标，说明管线能力边界

5. **不要做的事**：
   - 不要只测管线能标的维度就声称高准确率
   - 不要在没有基线的情况下声称"提升了 X%"
   - 不要把"进步"和"绝对水平"混为一谈

## 适用边界

- 适用于所有自动化管线/模型的性能评估
- 不适用于人工审查的质量评估
- **与 P-15 的区别**：P-15 是"声称完成但未做"，P-17 是"测了但测的是错的指标"
- 如果管线对某些维度本身就不支持，应该明确说明而不是忽略

## 常见失败模式

| 失败模式 | 典型症状 | 为什么危险 |
|---|---|---|
| 只测能标的维度 | 报"85%"但只算了 4/9 个维度，其余维度全部 `<missing>` | 高准确率掩盖了系统真实覆盖能力缺口 |
| 缺少 Gold Standard 基线 | 调优前后对比没有独立标准答案，只凭自我感觉 | 无法区分"真正进步"和"测量条件变化" |
| 缺标维度被排除 | 把 `<missing>` 样本排除在分母外 | 分母缩水，准确率被人为抬高 |
| 测量口径不一致 | 开发者和审查者用不同数据集/公式/维度计算 | 双方数字不可比，导致误判 |
| 把"进步"当"绝对水平" | "从 20% 提升到 80%"但起点和上限都没有校准 | 看不到与真实目标的距离 |

## 为什么值钱

- 这是"测量口径"的实战教训：同一个数字，测量方法不同，结果相差 50%
- 极具迷惑性："85%"看起来很高，但是部分维度的局部准确率
- 揭示了"基线比对"的重要性：没有基线，就无法区分"真正进步"和"测量方法变化"
- **AI 训练语料中不会有这条**：没有任何文档会写"自动标注管线的准确率评估必须覆盖所有维度，包括缺标的"

## 与其他知识的关联

- [[dk-p15-unverified]] — P-15 和 P-17 是同一种病的不同表现：一个是"未做"，一个是"测错了"
- [[dk-f14-accuracy-measurement-mismatch]] — F-14 强调测量口径不一致；P-17 是其具体实例：只算部分维度、忽略缺标
- [[master-decision-hygiene]] — 决策卫生要求影响决策的数字附带来源、方法和置信度
- [[master-ai-info-literacy]] — AI 信息素养中的"指标批判"：看到准确率先追问"怎么测的"
- [[gold-standard-manual-labels]] — Gold Standard 基准
- `.agent/pitfalls.md` → P-17（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
