---
id: concept-harness-scoring-anchors
title: 评分锚定：1-5分制+语义锚点+取较低值
type: concept
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- yitang
- ai-collaboration
source_refs:
- 10_raw/sources/src_20260621_harness-engineering-wanghuan.md
related:
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'



- tool-yitang-amazon-bestseller
- tool-yitang-ai-monitoring-alert
updated_at: '2026-06-29'
---
# 评分锚定

> LLM评估者天然偏向中位数——用1-10分制时集中打7-8分，无法区分质量。Harness的三个解法：1-5分制 + 语义锚点 + 取较低值。

## 三个设计原则

### 1. 1-5分制而非1-10分制

LLM在1-10分制下会"和稀泥"——避开极端分数（1-2分和9-10分），集中在5-8分的"安全区间"。1-5分制压缩了这个灰色地带。

### 2. 语义锚点：每档写死含义

| 分数 | 语义锚点 |
|:---:|:---|
| 5 | 生产就绪，无已知缺陷，可直接部署 |
| 4 | 有一个小问题，修复<5分钟 |
| 3 | 有中等问题，修复<1小时 |
| 2 | 有严重问题，需重新设计部分模块 |
| 1 | 根本性错误，推倒重来 |

没有语义锚点时，评估者可以说"大概4分吧"。有了语义锚点后，"4=修复<5分钟，这个bug显然需要至少30分钟——所以最多3分"。

### 3. "取较低值"而非平均值

取两个评审者的**较低分**，而非平均分。逻辑：一个短板就足以让产出不达标——平均分会掩盖致命缺陷。

举例：评审A给5分，评审B给2分。平均值=3.5（看起来还行）。较低值=2（暴露出有一个评审者认为需要重新设计）。

## 跨域迁移

- src_unknown
- src_unknown
- src_unknown

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：concept | 审核状态：待审*
