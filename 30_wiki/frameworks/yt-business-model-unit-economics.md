---
domain:
  - business-model

id: yt-business-model-unit-economics
title: 单元经济学：LTV > CAC
type: framework
status: enriched
confidence: 0.93
trust_level: high
source_context: 一堂商业模式系列课——单元经济学
source_refs:
  - src_20260606_640c2818-一堂-产品内核实操课-Truman-口述.md
  - src_20260606_094098c1-一堂-产品内核验证课-Truman-口述.md
created_at: "2026-06-19"
updated_at: "2026-06-19"
author: 老顽童
reviewed_by: "待审"
review_date: "2026-06-19"
related:
  - yt-business-model-definition
  - yt-business-model-canvas
  - yt-entrepreneur-unit-model
  - yt-five-step-method
  - yt-entrepreneur-business-growth
diagnostic_signals:
  - signal: "用户说'我们用户增长很快'，但不知道CAC"
    framework_lens: 单元经济学——增长快≠健康，需要看LTV和CAC
    follow_up_question: "你的获客成本（CAC）是多少？用户生命周期价值（LTV）是多少？LTV > CAC吗？"
  - signal: "用户LTV < CAC，还在烧钱增长"
    framework_lens: 单元经济学——单元模型不成立，增长是烧钱
    follow_up_question: "LTV < CAC时，增长越快亏损越大。你计划什么时候单元模型成立？"
  - signal: "用户说'我们先做规模，再优化单元模型'"
    framework_lens: 单元经济学——规模不解决单元模型问题
    follow_up_question: "规模能让LTV > CAC吗？如果不能，规模越大亏损越大。"
  - signal: "用户只看收入，不看LTV和CAC"
    framework_lens: 单元经济学——收入≠健康，单元模型才是健康指标
    follow_up_question: "你的收入中，有多少是可持续的？获客成本是否被摊薄？"
  - signal: "用户说'我们的单元模型很好'，但计算错误"
    framework_lens: 单元经济学——单元模型计算需要完整
    follow_up_question: "你的LTV计算是否包含了所有成本？CAC是否包含了所有获客成本？"

---
# 单元经济学：LTV > CAC

> 一堂五步法：单元经济学是商业模式的验证标准。LTV（用户生命周期价值）> CAC（获客成本），单元模型才成立。

## 核心框架

```
单元模型 = LTV / CAC

LTV（用户生命周期价值）
= ARPU × 毛利率 × 用户生命周期
= ARPU × 毛利率 / 月流失率

CAC（获客成本）
= 总营销费用 / 新增用户数
= 付费获客成本 + 自然获客成本分摊

单元模型健康标准：LTV / CAC > 3
```

## 关键洞察

### 1. LTV的计算

| 要素 | 说明 | 计算 |
|:---|:---|:---|
| **ARPU** | 每用户平均收入 | 总收入 / 总用户数 |
| **毛利率** | 收入扣除直接成本 | （收入 - 直接成本）/ 收入 |
| **用户生命周期** | 用户平均使用时长 | 1 / 月流失率 |
| **LTV** | 用户生命周期价值 | ARPU × 毛利率 × 用户生命周期 |

LTV计算示例：
- ARPU = 100元/月
- 毛利率 = 80%
- 月流失率 = 5%
- 用户生命周期 = 1 / 5% = 20个月
- LTV = 100 × 80% × 20 = 1600元

### 2. CAC的计算

| 要素 | 说明 | 计算 |
|:---|:---|:---|
| **付费获客成本** | 广告、推广费用 | 付费营销费用 / 付费获客数 |
| **自然获客成本** | 内容、SEO、口碑 | 相关成本 / 自然获客数 |
| **总CAC** | 总获客成本 | 总营销费用 / 总新增用户数 |

CAC计算示例：
- 月度营销费用 = 10万元
- 新增用户 = 1000人
- CAC = 10万 / 1000 = 1000元/人

### 3. 单元模型健康度

| 指标 | 健康标准 | 说明 |
|:---|:---|:---|
| **LTV / CAC** | > 3 | 每投入1元获客，回报3元 |
| **回本周期** | < 12个月 | 获客成本在12个月内回收 |
| **月流失率** | < 5% | 用户留存健康 |
| **毛利率** | > 70% | 有足够空间覆盖运营成本 |

### 4. 单元模型的优化

| 优化方向 | 方法 | 效果 |
|:---|:---|:---|
| **提升LTV** | 提升ARPU、降低流失、提升毛利率 | 长期价值 |
| **降低CAC** | 优化获客渠道、提升自然获客、提升转化率 | 获客效率 |
| **提升回本速度** | 预付费、年费、提升首月价值 | 现金流 |

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **忽视单元模型** | 只看收入增长，不看LTV和CAC | 建立单元模型监测 |
| **LTV计算错误** | 只算收入，不算成本和流失 | 完整计算LTV |
| **CAC计算错误** | 只算广告费用，不算所有获客成本 | 完整计算CAC |
| **LTV < CAC还增长** | 增长越快，亏损越大 | 先优化单元模型，再增长 |
| **回本周期太长** | 现金流压力大 | 优化付费方式，加速回本 |
| **单元模型不可规模化** | 小规模成立，大规模不成立 | 测试规模化后的单元模型 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 商业模式验证 | 技术架构设计 |
| 增长决策 | 品牌传播策略 |
| 投资评估 | 运营活动评估 |
| 产品商业化 | 纯公益项目 |

## 行动触发器

- 当评估商业模式时 → 先算单元模型
- 当考虑增长时 → 检查LTV > CAC
- 当融资时 → 展示单元模型健康度
- 当优化产品时 → 同时优化LTV和CAC

## 关联卡片

- `yt-business-model-definition`：商业模式定义
- `yt-business-model-canvas`：商业模式画布
- `yt-entrepreneur-unit-model`：单元模型
- `yt-five-step-method`：五步法总纲
- `yt-entrepreneur-business-growth`：商业增长

## 来源与验证

- 一堂商业模式设计课
- SaaS单元经济学研究
- 精益创业（Eric Ries）：单元模型验证
