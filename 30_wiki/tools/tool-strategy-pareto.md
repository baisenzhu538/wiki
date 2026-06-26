---

id: tool-strategy-pareto
title: 帕雷托图（80/20法则）：识别库存/客户/品类的关键少数
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
- 00_inbox/战略专题/冉鹏老师战略课程知识点_ocr.md §64
related:
  - '[[feishu-docx-pagination-extraction]]'
  - '[[tool-strategy-four-moves]]'
  - '[[tool-strategy-nine-problems]]'
  - '[[tool-yitang-supplier-interview]]'
  - '[[concept-feishu-api-pagination-trap]]'
  - "[[tool-strategy-fishbone]]"
---

# 帕雷托图

> 运动用品公司案例：80%的产品贡献5%的销售额，但占70%的库存。帕雷托图让你看清：你在为谁搬砖？

## 操作

1. 按贡献度排序（销售额/利润/客户价值）
2. 累计百分比 → 找到"20%贡献80%结果"的关键少数
3. 尾部80%：砍掉/合并/提价？

## Agent执行指令

```python
def pareto(data, metric="revenue"):
    sorted_data = sorted(data, key=lambda x: x[metric], reverse=True)
    cumulative = 0
    for i, item in enumerate(sorted_data):
        cumulative += item[metric] / total
        if cumulative >= 0.8:
            return f"前{i+1}个占80%，后{len(data)-i-1}个只占20%"
```

## 适用边界

- **适用**：SKU优化、客户分层、资源分配
- **不适用**：品类数本身就很少（<10个）

---

*卡片类型：tool | 审核状态：待审*
