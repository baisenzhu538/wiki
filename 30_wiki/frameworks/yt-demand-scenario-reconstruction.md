---
domain: demand-analysis
id: yt-demand-scenario-reconstruction
title: 用户场景重构法：使用前中后的完整体验地图
type: framework
status: reviewed
confidence: 0.78
trust_level: medium
source_context: 一堂五步法需求分析口述——"描述用户使用场景的三个层次"
source_refs:
- pending_archive:src_20260610_2a188b41-一堂-一堂五步法-需求-口述.md
created_at: '2026-06-19'
updated_at: '2026-06-20'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-28'
related:
- '[[yt-demand-hierarchy-model]]'
- '[[yt-demand-qualitative-analysis]]'
- '[[yt-demand-jtbd-application]]'
- '[[yt-demand-peak-end-rule]]'
- '[[yt-five-step-method]]'
diagnostic_signals:
- framework_lens: 场景缺失——停留在功能视角，未切换到用户视角
  follow_up_question: 你能描述一个典型用户，从早上醒来到晚上睡觉，会在什么具体时刻使用你的产品吗？
- framework_lens: 场景碎片化——只有片段，没有完整旅程
  follow_up_question: 用户使用你的产品前，在做什么？使用中遇到什么？使用后得到什么？
- framework_lens: 场景未结构化——缺乏统一的分析框架
  follow_up_question: 你能把不同用户的描述填进'使用前中后'三个阶段的框架吗？
- framework_lens: 场景假设错误——设计场景≠实际场景
  follow_up_question: 你有观察过真实用户实际使用产品的过程吗？和你设计的场景一致吗？
- framework_lens: 场景断点——体验地图有缺口
  follow_up_question: 用户在'使用中'的哪个节点最容易放弃？为什么？
tags:
- audience:ceo
- scene:diagnosis
- skill-level:intermediate
---


# 用户场景重构法：使用前中后的完整体验地图

> 一堂五步法：需求分析不是"问用户想要什么"，而是"还原用户真实使用的完整场景"。

## 核心框架

场景重构要求描述用户使用产品的**完整旅程**，分为三个阶段：

| 阶段 | 核心问题 | 关键要素 | 常见遗漏 |
|:---|:---|:---|:---|
| **使用前** | 用户为什么需要这个产品？ | 触发事件、痛点强度、现有方案 | 忽视"不用产品时的状态" |
| **使用中** | 用户怎么使用这个产品？ | 操作步骤、体验节点、情绪变化 | 只描述功能，不描述体验 |
| **使用后** | 用户得到了什么？ | 结果、价值、下一步行动 | 忽视使用后的反馈和扩散 |

## 关键洞察

### 1. 使用前的三个层次

一堂口述稿要求能回答三个递进问题：

- src_unknown
- src_unknown
- src_unknown

### 2. 场景描述的颗粒度

不是"用户用我们的APP管理客户"，而是：

```
使用前：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

使用中：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

使用后：
- src_unknown
- src_unknown
- src_unknown
```

### 3. ToB场景的决策链

ToB产品必须描述**决策链**，不是单一用户：

| 角色 | 关注点 | 决策影响力 |
|:---|:---|:---|
| 使用者 | 好不好用、效率提升 | 低（提建议） |
| 影响者 | 团队接受度、培训成本 | 中（影响决策） |
| 决策者 | ROI、战略匹配、预算 | 高（最终决策） |
| 采购者 | 价格、合同、交付 | 高（执行决策） |

场景重构必须覆盖：每个角色在什么场景下接触产品？他们的顾虑是什么？

## 场景重构的段位

| 段位 | 特征 | 示例 |
|:---|:---|:---|
| **L1 功能描述** | 只说产品功能 | "我们有一个客户管理功能" |
| **L2 用户描述** | 能说出用户类型 | "销售经理用来管理客户" |
| **L3 场景描述** | 能描述具体场景 | "周一早上汇报前，销售经理用我们的APP整理客户状态" |
| **L4 旅程描述** | 能描述使用前中后 | "使用前焦虑→使用中惊喜→使用后推荐" |
| **L5 情绪描述** | 能描述情绪变化 | "从焦虑到放松，从烦躁到愉悦" |
| **L6 决策链描述** | 能描述ToB决策链 | "使用者推荐→影响者评估→决策者批准→采购者执行" |

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **功能视角** | "我们做了一个XX功能" | 强制用"用户的问题是..."开头 |
| **场景太泛** | "所有销售都用" | 聚焦一个具体用户、具体时间、具体场景 |
| **忽视使用前** | 直接从"打开APP"开始描述 | 先描述"不用APP时的痛苦和替代方案" |
| **忽视使用后** | 描述到"用完"就结束 | 追问"用完后用户做了什么？会推荐吗？" |
| **ToB忽视决策链** | 只描述使用者，不描述决策者 | 画出决策链，每个角色单独描述场景 |
| **场景假设未验证** | 设计场景≠实际场景 | 观察真实用户，对比假设场景和实际场景 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 新产品需求验证 | 成熟产品数据优化（已有行为数据） |
| 用户访谈设计 | 技术架构设计 |
| 产品体验设计 | 竞品功能对比 |
| ToB销售话术设计 | 定价策略制定 |

## 行动触发器

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关联卡片

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源与验证

- src_unknown
- src_unknown
- src_unknown
