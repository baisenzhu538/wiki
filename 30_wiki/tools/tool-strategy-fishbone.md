---
id: tool-strategy-fishbone
title: 鱼骨图拆解：按维度拆销售/利润/组织问题找到根因
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
- 00_inbox/战略专题/冉鹏老师战略课程知识点_ocr.md §27-30
related:
- "[[tool-strategy-nine-problems]]"
---

# 鱼骨图拆解

> 九个问题告诉你"什么类型"，鱼骨图帮你找到"具体根因在哪"。四层拆解：销售→利润→组织→管理。

## 四层拆解

| 层级 | 拆解维度 | 示例问题 |
|:---|:---|:---|
| **销售** | 单店规模 / 品类相加 / 客户分类 | 是客单价降了还是客流量降了？ |
| **利润** | 先看销售是否下降 → 再看成本 | 利润降是因为收入降还是成本涨？ |
| **组织** | 能力→人数→意愿→架构→流程规则 | 是人不够还是人不对还是流程卡？ |
| **管理** | 流程规则→管理工具→文化→领导力 | 规则清晰但执行不了？→文化问题 |

## Agent执行指令

```python
def fishbone(problem, layers=["销售","利润","组织","管理"]):
    for layer in layers:
        causes = decompose(problem, layer)
        if root := find_root(causes):
            return f"根因在 {layer} 层: {root}"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 只看销售层 | 销售额降了就做促销 | 利润降可能是因为成本涨了——往下拆 |
| 跳过组织层 | "业务问题"→只分析业务 | 业务问题背后往往是组织问题 |

---

*卡片类型：tool | 审核状态：待审*
