---

id: tool-ci-define-phase
title: CI Define阶段：KITs和KIQs——从决策倒推信息需求
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
  - yitang
  - research
source_refs:
- src_unknown
related:
  - [[tool-key-assumptions-check]]
  - [[tool-devils-advocacy]]
  - [[business-research-skill-oscar-13-weapon-system]]
  - [[tool-candy-oral-polish]]
  - [[tool-indicators-signposts]]
  - [[framework-ci-operating-model]]
  - [[dk-yitang-research-question-quality]]
---
# CI Define阶段：KITs和KIQs

> 大多数调研失败不是因为收集不够，而是因为没搞清楚"收集什么"和"为什么收集"。KITs和KIQs是CI界解决这个问题的标准方法。

## 方法

### Step 1：定义KITs（Key Intelligence Topics）

列出当前最需要情报支持的3-5个决策领域。决策驱动，不是好奇心驱动。

| KIT示例（好） | 不是KIT（坏） |
|:---|:---|
| "竞对的新定价是否会在Q3影响我们的win rate？" | "了解一下竞对在做什么" |
| "A公司的新品在哪些客户群获得了traction？" | "A公司的产品怎么样" |

### Step 2：将KITs拆解为KIQs（Key Intelligence Questions）

每个KIT拆成3-5个可回答的具体问题。

> KIT: "竞对的新定价是否会在Q3影响我们的win rate？"
> → KIQ1: 竞对的新价格比我们低多少？
> → KIQ2: 哪些客户群对价格最敏感？
> → KIQ3: 过去竞对调价后，我们的win rate变化规律是什么？
> → KIQ4: 竞对的定价策略是永久性还是促销性？

### Step 3：四象限区分"需要知道"vs"想知道"

| | 能直接回答决策 | 不能直接回答决策 |
|:---|:---|:---|
| **容易获取** | ✅ 优先做 | ⚠️ 做了但别花太多时间 |
| **难获取** | 🔑 核心投入 | ❌ 砍掉 |

## Agent执行指令

```python
# KIQ生成模板（Agent根据决策场景自动生成KIQs）
prompt = """你是一个CI分析师。当前关键决策是：
[DECISION]
请生成5-8个KIQs（Key Intelligence Questions），要求：
1. 每个KIQ是可回答的具体问题（不要用"了解"这类模糊动词）
2. 每个KIQ标注数据来源难度（easy/medium/hard）
3. 用四象限区分优先级
4. 输出格式：| KIQ | 难度 | 优先级 | 数据来源建议 |
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 问题太宽 | "竞对在做什么"——无法回答 | 加限定词：哪个竞对？在哪个市场？什么时间范围？ |
| 问题太多 | 20个KIQ，资源无法覆盖 | 强制Top 5，其余放入"如果时间允许"清单 |
| 问题与决策无关 | 收集了很多有趣但与决策无关的信息 | 每个KIQ必须回答"这个答案会改变什么决策" |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
