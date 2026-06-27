---

id: tool-red-team-analysis
title: Red Team Analysis：模拟竞对的最优策略
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---

# Red Team Analysis

> 与第3掌（竞对跟踪）的互补：跟踪=观察竞对做了什么，Red Team=模拟竞对会做什么。

## 四步法

### Step 1：定义对手

不只是"竞对A公司"——明确：他们的CEO是谁、背景是什么、过去做过什么决策、资源有多少。

### Step 2：理解对手的动机和能力

| 维度 | 问题 |
|:---|:---|
| **动机** | 竞对今年的KPI是什么？投资者的期望是什么？ |
| **能力** | 竞对有多少现金？多少人才？什么技术壁垒？ |
| **约束** | 竞对受什么限制（监管/供应链/人才）？ |
| **风格** | 竞对CEO是激进派还是稳健派？过去怎么应对竞争？ |

### Step 3：模拟对手的最优策略

"如果我是竞对CEO，我会怎么打垮我们？"
- src_unknown
- src_unknown
- src_unknown

### Step 4：制定应对方案

每个模拟的攻击路径 → 我们的防御/反制策略。

## Agent执行指令

```python
# Red Team Prompt模板
prompt = """你现在是[COMPETITOR]的CEO [NAME]。
背景：[CEO的履历、风格、过去重大决策]
你的公司有：[资源、能力、约束]
你的目标：[市场份额/营收/KPI]

我们的公司（你的竞对）有以下弱点：[WEAKNESSES]

作为[NAME]，请制定摧毁我们公司的最优策略：
1. 你会先攻击哪个市场？为什么？
2. 你会用什么手段（价格战/挖人/产品抄袭/渠道封锁）？
3. 你的策略中有什么是我们最意想不到的？
4. 我们最强的防御是什么？你怎么突破它？
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 镜像思维 | 假设竞对像自己一样思考 | 深入研究竞对CEO的背景和决策历史 |
| 过度乐观 | 低估竞对的资源和决心 | 给竞对假设"最坏情况"的资源上限 |
| 只模拟一次 | 竞对有多种可能策略 | 至少模拟3种策略：激进/稳健/防御 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
