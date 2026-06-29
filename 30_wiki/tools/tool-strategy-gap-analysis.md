---


id: tool-strategy-gap-analysis
title: 差距分析：战略的起点——业绩差距（内部）+机会差距（外部）
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
  - strategy
source_refs:
  - pending_archive:src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---
# 差距分析

> BRM的起点。先搞清楚"差在哪"再谈"怎么追"。两个差距：业绩差距（自己和目标比）+机会差距（自己和对手比）。分析顺序：先看业务指标，再看组织问题。

## 两步操作

**Step 1：业绩差距**
  - src_unknown
  - src_unknown

**Step 2：机会差距**
  - src_unknown
  - src_unknown

## Agent执行指令

```python
def gap_analysis(company):
    perf_gap = [
        (target, actual, target-actual)
        for target, actual in company.kpis
    ]
    opp_gap = [
        (competitor, metric, our_value-comp_value)
        for competitor in company.competitors
    ]
    return {"业绩差距": perf_gap, "机会差距": opp_gap}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:
|:---|:---|
| 先看人再看事 | "销售团队不行"→换人 | 先看业务指标，确认不是流程问题再判断人 |

---

## 业绩差距外部原因简析

差距不只来自内部。三层次分析：
- src_unknown
- src_unknown
- src_unknown

先排除外部因素再分析内部——避免"环境变了"被误诊为"能力不行"

---

*卡片类型：tool | 审核状态：待审*
