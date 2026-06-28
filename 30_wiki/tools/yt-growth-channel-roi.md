---

domain:
- src_unknown
id: yt-growth-channel-roi
title: 渠道ROI评估与优化
type: tool
status: enriched
confidence: 0.92
trust_level: high
source_context: 一堂增长策略系列课——渠道ROI
source_refs:
- 10_raw/sources/src_20260606_640c2818-一堂-产品内核实操课-Truman-口述.md
- 10_raw/sources/src_20260606_094098c1-一堂-产品内核验证课-Truman-口述.md
created_at: '2026-06-20'
updated_at: '2026-06-28'
author: 老顽童
reviewed_by: 待审
review_date: '2026-06-20'
related:
  - [[ocr-一堂-科学决策-roi决策评估画布]]
  - [[tool-ROI决策评估画布]]
  - [[ocr-一堂-科学决策-roi决策评估画布-案例02]]
  - [[yt-panproduct-execution-roi-analysis]]
  - [[ocr-一堂-科学决策-roi决策评估画布-案例01]]
  - [[ocr-泛产品设计-落地卡片-roi分析]]
  - [[ocr-一堂-科学决策-roi决策评估画布-案例04]]
  - [[case-科学决策-ROI案例02]]
  - [[case-科学决策-ROI案例03]]
  - [[case-truman-poker-deck-roi]]
  - [[tool-泛产品落地-ROI分析]]
  - [[ocr-一堂-科学决策-roi高阶训练全景图]]
  - [[tool-马易-AIGC项目ROI评估]]
  - [[dk-decision-value-overrides-roi]]
diagnostic_signals:
- framework_lens: 渠道ROI评估——需要建立渠道归因模型，明确每个渠道的贡献
  follow_up_question: 你的渠道归因模型是什么？最后点击、首次点击、还是多触点归因？
- framework_lens: 渠道ROI评估——CAC低≠ROI高，需要看LTV
  follow_up_question: 这个渠道用户的LTV是多少？LTV/CAC是否健康？
- framework_lens: 渠道ROI评估——渠道ROI下降可能是市场变化或竞争加剧
  follow_up_question: ROI下降是短期波动还是长期趋势？竞品是否也在同一渠道？
- framework_lens: 渠道ROI评估——渠道多元化是风险管理
  follow_up_question: 你的渠道集中度是多少？是否有计划拓展新渠道？
- framework_lens: 渠道ROI评估——渠道成本上升需要优化或寻找替代渠道
  follow_up_question: 成本上升是因为竞争加剧还是渠道本身效率下降？有没有替代渠道？

---

# 渠道ROI评估与优化

> 一堂五步法：渠道ROI不是CAC越低越好，而是LTV/CAC越高越好。渠道优化 = 增量预算给ROI高的渠道。

## 核心框架

渠道ROI的核心公式：

```
渠道ROI = (渠道带来的LTV - 渠道CAC) / 渠道CAC

渠道LTV/CAC = 渠道用户LTV / 渠道CAC

健康标准：LTV/CAC > 3，回收周期 < 12个月
```

## 关键洞察

### 1. 渠道归因模型

| 模型 | 说明 | 适用 | 局限 |
|:---|:---|:---|:---|
| **最后点击** | 归因于最后触点 | 简单 | 忽视前期触点 |
| **首次点击** | 归因于首次触点 | 品牌认知 | 忽视后续触点 |
| **线性归因** | 平均分配所有触点 | 均衡 | 不区分触点重要性 |
| **时间衰减** | 越近越重要 | 短期决策 | 忽视长期影响 |
| **数据驱动** | 基于算法分配 | 精准 | 需要大量数据 |

### 2. 渠道评估矩阵

| 维度 | 说明 | 评估 |
|:---|:---|:---|
| **获客成本** | 单用户获客成本 | 越低越好 |
| **用户质量** | 用户LTV | 越高越好 |
| **规模化** | 能否规模化 | 能→优先 |
| **可持续性** | 是否可持续 | 是→长期 |
| **可控性** | 是否可控 | 高→优先 |

### 3. 渠道优化策略

| 策略 | 说明 | 适用 |
|:---|:---|:---|
| **增量优化** | 增加ROI高渠道的预算 | ROI差异大 |
| **效率优化** | 优化现有渠道效率 | 渠道成熟 |
| **渠道拓展** | 寻找新渠道 | 现有渠道饱和 |
| **渠道替代** | 用新渠道替代旧渠道 | 旧渠道衰退 |
| **渠道组合** | 优化渠道组合 | 多渠道 |

### 4. 渠道ROI的监控

| 指标 | 说明 | 频率 |
|:---|:---|:---|
| **CAC** | 单用户获客成本 | 每日 |
| **LTV** | 用户生命周期价值 | 每月 |
| **LTV/CAC** | 健康度 | 每月 |
| **回收周期** | CAC回收时间 | 每月 |
| **渠道贡献** | 渠道带来的收入占比 | 每月 |

### 5. 渠道ROI的误区

| 误区 | 说明 | 避免 |
|:---|:---|:---|
| **只看CAC** | 忽视LTV | 看LTV/CAC |
| **短期视角** | 只看当月ROI | 看长期LTV |
| **忽视归因** | 归因不准确 | 建立归因模型 |
| **忽视渠道协同** | 渠道之间有协同 | 看整体 |
| **忽视渠道成本** | 隐性成本不计 | 全成本核算 |

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **归因错误** | 渠道贡献评估不准 | 建立归因模型 |
| **只看短期** | 忽视长期LTV | 长期跟踪 |
| **渠道集中** | 过度依赖单一渠道 | 多元化 |
| **忽视渠道协同** | 渠道之间互相影响 | 整体评估 |
| **成本核算不全** | 隐性成本不计 | 全成本核算 |
| **优化过度** | 优化到边际收益为负 | 边际分析 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 渠道优化 | 技术架构 |
| 预算分配 | 品牌定位 |
| 获客策略 | 创意判断 |
| 规模化获客 | 一次性决策 |

## 行动触发器

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关联卡片

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源与验证

- src_unknown
- src_unknown
- src_unknown
