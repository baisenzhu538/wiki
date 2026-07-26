---
id: tool-strategy-pareto
title: 帕雷托图（80/20法则）：识别库存/客户/品类的关键少数
type: tool
status: enriched
author: 老顽童
reviewed_by: pending
review_date: 2026-06-21
created_at: 2026-06-21
updated_at: '2026-06-30T16:07:51+00:00'
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- strategy
source_refs:
- pending_archive:src_unknown
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---

# 帕雷托图

> 运动用品公司案例：80%的产品贡献5%的销售额，但占70%的库存。帕雷托图让你看清：你在为谁搬砖？

## Purpose

帕雷托图用于快速识别“关键少数”——在客户、SKU、渠道、库存或问题中，找出贡献大部分结果的少数项，从而把有限资源投入到杠杆点最高的地方。

## Protocol

1. **明确指标**：选择贡献度指标，如销售额、利润、客户价值、库存金额或缺陷次数。
2. **排序并累加**：将对象按指标从高到低排序，逐行计算累计百分比。
3. **绘制帕雷托曲线**：横轴为对象，纵轴为指标绝对值与累计百分比双轴，定位累计贡献约80%的切点。
4. **划分关键少数与长尾**：切点左侧为重点管理对象，右侧进入“砍掉/合并/提价/外包”决策池。
5. **制定行动并跟踪**：针对关键少数制定保留/优化策略，对长尾设定退出或自动化规则，并复查分布是否漂移。

```python
def pareto(data, metric="revenue", threshold=0.8):
    total = sum(item[metric] for item in data)
    sorted_data = sorted(data, key=lambda x: x[metric], reverse=True)
    cumulative = 0
    for i, item in enumerate(sorted_data):
        cumulative += item[metric] / total
        if cumulative >= threshold:
            return f"前{i+1}个占80%，后{len(data)-i-1}个只占20%"
```

## When NOT to Use

| 场景 | 原因 | 替代方案 |
|---|---|---|
| 数据分布均匀、无明显集中 | 80/20 规律不存在，排序无法区分杠杆点 | 聚类分析、流程分析 |
| 需要寻找系统性根因 | 帕雷托只显示现象频次，不揭示因果机制 | 鱼骨图、五个为什么 |
| 战略差异化或蓝海探索 | 关键少数可能是既有惯性，长尾可能孕育创新 | 四层战略分析、蓝海画布 |
| 样本小、类别不稳定 | 统计噪声会让“关键少数”失真 | 扩大样本、A/B测试 |

## Critique

**内部局限**：帕雷托图隐含的**具体假设**是“历史分布可代表未来”，其适用**边界**是结果可量化、类别相对稳定的场景；潜在**反例**包括平台经济中的长尾爆款、创新业务中尾部用户触发网络效应；使用**前提**是数据完整、指标与战略目标一致，否则会把旧业务的“大而不强”误判为核心资产。

**外部攻击者**：**Michael Porter** 会质疑：帕雷托只告诉你现在谁贡献了80%，却没解释为什么竞争对手能让那80%的价值流向别处。若把“关键少数”当成静态护城河，忽视产业结构和差异化来源，企业只是在优化效率曲线，而非建立可持续竞争优势。

## Synthesis

- [[case-strategy-cool-boiled-water]]
- [[case-strategy-edward-jones]]
- [[concept-strategy-evolution-cycle]]
- [[tool-strategy-12-word-test]]

---

*卡片类型：tool | 审核状态：待审*
