---

id: tool-demand-assessment-triangle
title: 需求评估三角形：普遍性×频次×刚性
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [yitang, five-step-method]
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-需求评估三角形_ocr_text.md
related:
  - '[[case-demand-financial-literacy]]'
  - '[[case-demand-restaurant-hiring]]'
  - '[[case-demand-rural-5g]]'
  - '[[dk-demand-pitfall-tier4-housekeeping]]'
  - '[[dk-demand-misjudgment-rate]]'
  - "[[framework-demand-iceberg]]"
  - "[[tool-demand-iceberg-l6-hypothesis]]"
---

# 需求评估三角形

> L6产出机会卡片后，用评估三角形做Go/No-Go判断。三个维度相乘：普遍性×频次×刚性=需求强度。

## 三维评分

| 维度 | 高 | 中 | 低 | 极低 |
|:---|:---|:---|:---|:---|
| **普遍性** | 全民（几亿） | 大众（千万/百万） | 小众（十万/几万） | 特殊（几千/几百） |
| **频次** | 高频（一天一次） | 中频（一月一次） | 低频（一年一次） | 极低（一生一次） |
| **刚性** | 非常刚（加钱抢着用） | 比较刚（收费我也用） | 不太刚（免费我才用） | 没刚性（白给也不用） |

## 判定逻辑

- 三个都是"高"→ 黄金机会，值得重投入
- 两个"高"一个"中"→ 好机会，适合创业
- 一个"高"两个"低"→ 细分机会，需要精确切入
- 两个以上"低"或"极低"→ 危险，重新评估

## Agent执行指令

```python
prompt = """对以下机会做评估三角形打分：

机会：{OPPORTUNITY}

1. 普遍性：目标用户群规模？
2. 频次：用户多久需要一次？
3. 刚性：用户有多需要它？（免费才用/收费也用/加钱抢着用）

结合三个维度给出Go/No-Go/需验证判断。
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 普遍性高估 | "所有职场人都需要"——实际可能只有10% | 用TAM/SAM/SOM分层估算 |
| 刚性自欺 | "免费才用"标成"收费我也用" | 问：如果明天开始收费，留存率多少？ |

## 适用边界

- **适用**：L6机会卡片产出后，需要做优先级排序
- **不适用**：需求已经过大量用户验证的成熟产品

---

*卡片类型：tool | 审核状态：待审*
