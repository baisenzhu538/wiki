---


id: tool-strategy-three-horizons
title: 三个地平线：现金流（现在）/增长（1-3年）/种子（3-5年）
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
  - pending_archive:src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---# 三个地平线

> 所有公司都在同时做三件事：养活今天、投资明天、赌后天。问题是多数公司只做了第一件。

## 三层定义

| 地平线 | 时间维度 | 核心动作 | 资源占比 |
|:
|:---|:---|:---:|
| H1 现金流 | 现在 | 优化效率，榨取利润 | 70% |
| H2 增长 | 1-3年 | 规模化已验证的增长引擎 | 20% |
| H3 种子 | 3-5年 | 探索全新机会，允许失败 | 10% |

## Agent执行指令

```python
def horizon_audit(company):
    h1 = [p for p in company.products if p.stage == "cash_cow"]
    h2 = [p for p in company.products if p.stage == "growth"]
    h3 = [p for p in company.products if p.stage == "seed"]
    return f"H1={len(h1)} H2={len(h2)} H3={len(h3)}"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| H3=0 | 只有今天没有明天 | 每年强制投入10%资源到H3 |
| H2太多 | 同时做5个增长项目，资源分散 | 聚焦1-2个，其余砍掉 |

---

*卡片类型：tool | 审核状态：待审*
