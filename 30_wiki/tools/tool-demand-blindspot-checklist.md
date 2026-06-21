---
id: tool-demand-blindspot-checklist
title: 2B/2C盲区和机会清单：场景拆解的维度小抄
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, five-step-method]
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-盲区和机会清单-图-01_ocr_text.md
related:
- "[[tool-demand-iceberg-l2-scenario]]"
- "[[tool-demand-iceberg-l1-user]]"
---

# 盲区和机会清单

> L1/L2场景拆解时容易遗漏维度。这份清单是"别漏了"的小抄——按5个维度系统扫描。

## 五维扫描

| 维度 | 2B示例 | 2C示例 |
|:---|:---|:---|
| **流程环节** | 报价/排产/质检/报销/采购/审批 | 搜索/比价/下单/支付/收货/售后 |
| **操作地点** | 车间/办公室/会议室/大屏/实验室 | 家里/通勤/办公室/商场/户外 |
| **人物协作** | 跨部门沟通/上下级汇报/供应商对接 | 家人协作/朋友推荐/社群讨论 |
| **时间节点** | 公司起步/扩张/增长受阻/新品上市 | 毕业/入职/结婚/生子/搬家 |
| **重大事件** | 融资并购/战略转型/上市筹备/危机公关 | 健康危机/财务危机/关系危机 |

## Agent执行指令

```python
prompt = """扫描以下需求的五个盲区维度，找出之前遗漏的场景机会：

{DEMAND_DESCRIPTION}

按5个维度逐一列出：哪些场景/用户/时刻之前被忽略了？
"""
```

## 适用边界

- **适用**：L1/L2完成后自检——有没有漏掉重要维度
- **不适用**：场景已经非常明确的窄领域

---

*卡片类型：tool | 审核状态：待审*
