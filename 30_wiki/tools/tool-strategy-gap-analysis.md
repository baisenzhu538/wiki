---
id: tool-strategy-gap-analysis
title: 差距分析：战略的起点——业绩差距（内部）+机会差距（外部）
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [strategy]
source_refs:
- 00_inbox/战略专题/冉鹏老师战略课程知识点_ocr.md §25-26
related:
- "[[framework-strategy-brm]]"
- "[[tool-key-assumptions-check]]"
---

# 差距分析

> BRM的起点。先搞清楚"差在哪"再谈"怎么追"。两个差距：业绩差距（自己和目标比）+机会差距（自己和对手比）。分析顺序：先看业务指标，再看组织问题。

## 两步操作

**Step 1：业绩差距**
- 列今年目标 vs 实际 → 哪些没达成？
- 拆解到最细维度（按产品/区域/客户群）

**Step 2：机会差距**
- 对标最强对手 → 他们做到了什么我们没做到？
- 市场在增长但我们在萎缩？→ 机会差距

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
|:---|:---|:---|
| 先看人再看事 | "销售团队不行"→换人 | 先看业务指标，确认不是流程问题再判断人 |

---

*卡片类型：tool | 审核状态：待审*
