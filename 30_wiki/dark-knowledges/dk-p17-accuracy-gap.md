---

id: dk-p17-accuracy-gap
title: P-17：auto_label 声称"85%准确率"——实测34.8%，差距来自被忽略的5个维度
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-17
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - [[labeling-final-consolidation]]
  - [[kdo-15-dimension-label-spec]]
  - [[data-labeling-best-practices-report]]
  - [[dk-ai-social-progress-not-automatic]]
  - [[tool-demand-agent-auto-verify]]
  - [[labeling-research-alignment]]
  - [[ocr-项目背景问题思考的8个维度]]
  - [[gold-standard-manual-labels]]
  - [[ouyangfeng-labeling-research-review]]
  - [[dk-c7-auto-backup-conflict]]
  - [[label-accuracy-standard-alignment]]
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# P-17：auto_label 声称“85%准确率”——实测34.8%，差距来自被忽略的5个维度

---

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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **准确率声明必须附带测量方法**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

2. **建立 Gold Standard 基线**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **独立验证流程**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **报告完整性**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型症状 | 为什么危险 |
|
|---|---|
| 只测能标的维度 | 报"85%"但只算了 4/9 个维度，其余维度全部 `<missing>` | 高准确率掩盖了系统真实覆盖能力缺口 |
| 缺少 Gold Standard 基线 | 调优前后对比没有独立标准答案，只凭自我感觉 | 无法区分"真正进步"和"测量条件变化" |
| 缺标维度被排除 | 把 `<missing>` 样本排除在分母外 | 分母缩水，准确率被人为抬高 |
| 测量口径不一致 | 开发者和审查者用不同数据集/公式/维度计算 | 双方数字不可比，导致误判 |
| 把"进步"当"绝对水平" | "从 20% 提升到 80%"但起点和上限都没有校准 | 看不到与真实目标的距离 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
