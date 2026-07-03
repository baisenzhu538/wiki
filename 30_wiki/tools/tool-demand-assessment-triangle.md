---
id: tool-demand-assessment-triangle
title: 需求评估三角形：普遍性×频次×刚性
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
- yitang
- five-step-method
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-需求评估三角形_ocr_text.md
related:
- '[[yitang-domain-digest]]'
- '[[tool-项目方案评估三角形]]'
- '[[ocr-一堂-科学决策-决策三角形]]'
- '[[tool-提升笔记练习频次的方法]]'
- '[[ocr-一堂-科学决策-项目方案评估三角形]]'
- '[[framework-科学决策三角形]]'
- yt-market-size-estimation
- proposal-prompt-injection-infrastructure
updated_at: '2026-06-29'
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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

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

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
