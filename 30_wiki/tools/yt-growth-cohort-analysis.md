---
id: yt-growth-cohort-analysis
title: 同期群分析：用户行为追踪
type: tool
status: enriched
confidence: 0.92
trust_level: high
domain:
  - yitang
  - business
source_person: Truman
source_context: 一堂增长策略系列课——同期群分析
source_refs:
  - src_20260606_640c2818-一堂-产品内核实操课-Truman-口述.md
  - src_20260606_094098c1-一堂-产品内核验证课-Truman-口述.md
created_at: "2026-06-20"
updated_at: "2026-06-20"
author: 老顽童
reviewed_by: "待审"
review_date: "2026-06-20"
related:
  - yt-growth-strategy-overview
  - yt-growth-retention-metrics
  - yt-growth-data-driven-decision
  - yt-growth-funnel-optimization
  - yt-five-step-method
diagnostic_signals:
  - signal: "用户说'我们的留存率在下降，但不知道原因'"
    framework_lens: 同期群分析——留存率下降需要分群分析，找到具体 cohort
    follow_up_question: "哪个 cohort 的留存率下降？是新用户还是老用户？哪个渠道的用户？"
  - signal: "用户说'我们改了产品，但不知道对留存的影响'"
    framework_lens: 同期群分析——产品改动的影响需要对比 cohort
    follow_up_question: "改动前后的 cohort 留存曲线有变化吗？哪个 cohort 受影响最大？"
  - signal: "用户说'我们的用户行为很复杂，不知道怎么分析'"
    framework_lens: 同期群分析——同期群分析把复杂行为结构化
    follow_up_question: "你的用户按什么维度分群？注册时间、渠道、版本？"
  - signal: "用户说'我们的数据很多，但看不出趋势'"
    framework_lens: 同期群分析——同期群分析能揭示趋势和异常
    follow_up_question: "你的 cohort 留存曲线是什么形状？是改善还是恶化？"
  - signal: "用户说'我们不知道哪个渠道的用户质量最好'"
    framework_lens: 同期群分析——按渠道分群，对比留存
    follow_up_question: "不同渠道的用户 cohort 留存曲线对比如何？"
---

# 同期群分析：用户行为追踪

> 一堂五步法：同期群分析是留存分析的利器。把用户按时间分群，看留存曲线变化，找到问题 cohort。

## 核心框架

同期群分析的核心：

```
按注册时间分群 → 追踪每个群的留存曲线 → 对比不同群的留存 → 找到问题

示例：
        第1天  第7天  第30天  第90天
1月 cohort  50%    30%    20%    15%
2月 cohort  55%    35%    25%    18%
3月 cohort  45%    25%    15%    10%  ← 问题 cohort
```

## 关键洞察

### 1. 同期群的分群维度

| 维度 | 说明 | 适用 |
|:---|:---|:---|
| **注册时间** | 按注册月份/周分群 | 通用 |
| **获客渠道** | 按渠道分群 | 渠道评估 |
| **产品版本** | 按使用版本分群 | 产品评估 |
| **用户行为** | 按首次行为分群 | 行为分析 |
| **用户属性** | 按地域、设备分群 | 属性分析 |

### 2. 留存曲线的解读

| 曲线形状 | 说明 | 行动 |
|:---|:---|:---|
| **逐月改善** | 产品/运营在优化 | 继续 |
| **逐月恶化** | 产品/运营在退化 | 找原因 |
| **某个 cohort 异常** | 该 cohort 有特殊因素 | 分析 |
| **所有 cohort 平行** | 产品稳定 | 寻找突破 |
| **新 cohort 更好** | 近期优化有效 | 学习 |
| **新 cohort 更差** | 近期变化有害 | 回滚 |

### 3. 同期群分析的应用

| 应用 | 说明 | 方法 |
|:---|:---|:---|
| **留存分析** | 分析留存趋势 | 按注册时间分群 |
| **渠道评估** | 评估渠道质量 | 按渠道分群 |
| **产品评估** | 评估产品改动 | 按版本分群 |
| **活动评估** | 评估活动效果 | 按活动参与分群 |
| **生命周期** | 分析用户生命周期 | 按生命周期阶段分群 |

### 4. 同期群分析的指标

| 指标 | 说明 | 计算 |
|:---|:---|:---|
| **留存率** | 某 cohort 在T日仍活跃的比例 | 活跃数/注册数 |
| **流失率** | 1 - 留存率 | 流失数/注册数 |
| **回流率** | 流失后回来的比例 | 回流数/流失数 |
| **LTV** | 某 cohort 的总价值 | 收入/注册数 |
| **CAC回收周期** | 某 cohort 回收CAC的时间 | 回收天数 |

### 5. 同期群分析的工具

| 工具 | 说明 | 功能 |
|:---|:---|:---|
| **Excel** | 基础分析 | 简单 cohort 表 |
| **SQL** | 自定义查询 | 灵活分析 |
| **Mixpanel** | 产品分析 | 自动 cohort |
| **Amplitude** | 产品分析 | 自动 cohort |
| **Tableau** | 可视化 | 可视化 cohort |

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **分群太粗** |  cohort 太大，看不出差异 | 细分维度 |
| **分群太细** |  cohort 太小，统计不显著 | 合并维度 |
| **只看留存** | 忽视其他指标 | 多维分析 |
| **忽视时间** | 不同 cohort 时间不同 | 对齐时间 |
| **不行动** | 发现问题不解决 | 分析→行动 |
| **工具依赖** | 只用工具，不思考 | 工具+思考 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 留存分析 | 技术架构 |
| 渠道评估 | 品牌传播 |
| 产品评估 | 创意判断 |
| 用户行为 | 一次性决策 |

## 行动触发器

- 当留存下降时 → 同期群分析找问题 cohort
- 当评估渠道时 → 按渠道分群对比
- 当产品改动时 → 对比改动前后 cohort
- 当数据复杂时 → 同期群分析结构化

## 关联卡片

- `yt-growth-strategy-overview`：增长策略总纲
- `yt-growth-retention-metrics`：留存指标
- `yt-growth-data-driven-decision`：数据驱动决策
- `yt-growth-funnel-optimization`：漏斗优化
- `yt-five-step-method`：五步法总纲

## 来源与验证

- 一堂增长策略课
- 同期群分析研究
- 用户行为分析实践
