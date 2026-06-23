---

id: yt-product-kernel-mvp-design
title: 内核MVP设计：最小可验证产品
type: tool
status: enriched
confidence: 0.92
trust_level: high
domain:
  - productsource_person: Truman
source_context: 一堂产品内核系列课——MVP设计
source_refs:
  - src_20260606_640c2818-一堂-产品内核实操课-Truman-口述.md
  - src_20260606_094098c1-一堂-产品内核验证课-Truman-口述.md
created_at: "2026-06-19"
updated_at: "2026-06-19"
author: 老顽童
reviewed_by: "待审"
review_date: "2026-06-19"
related:
  - yt-product-kernel-definition
  - yt-product-kernel-validation
  - yt-product-kernel-hypothesis-test
  - yt-product-kernel-premature-optimization
  - yt-five-step-method
  - yt-entrepreneur-lean-validation
diagnostic_signals:
  - signal: "用户的MVP做了3个月，功能还是太多"
    framework_lens: 内核MVP设计——MVP不够M，需要聚焦核心
    follow_up_question: "你的MVP去掉了哪些功能？剩下的功能是否只验证核心假设？"
  - signal: "用户说'MVP必须完整，否则用户体验不好'"
    framework_lens: 内核MVP设计——MVP不是完整产品，是验证工具
    follow_up_question: "MVP的目标是验证假设，还是提供完美体验？"
  - signal: "用户的MVP上线后，无法判断假设是否成立"
    framework_lens: 内核MVP设计——MVP需要可衡量
    follow_up_question: "你的MVP有明确的验证指标吗？能衡量关键转化率吗？"
  - signal: "用户做MVP时，花大量时间在非核心功能上"
    framework_lens: 内核MVP设计——资源应聚焦核心
    follow_up_question: "非核心功能占用了多少开发时间？如果砍掉，能提前多久上线？"
  - signal: "用户说'我们先做MVP，但MVP和最终产品一样'"
    framework_lens: 内核MVP设计——MVP是验证工具，不是缩小版产品
    follow_up_question: "MVP和最终产品的区别是什么？MVP验证什么假设？"

---

# 内核MVP设计：最小可验证产品

> 一堂五步法：MVP（Minimum Viable Product）不是"最小产品"，而是"最小可验证产品"——用最小成本验证核心假设。

## 核心框架

MVP的设计原则：

| 原则 | 说明 | 错误理解 | 正确理解 |
|:---|:---|:---|:---|
| **Minimum** | 最小功能集 | 功能少=简陋 | 只保留验证假设必需的功能 |
| **Viable** | 可验证 | 能用就行 | 用户能完成核心任务，产生验证数据 |
| **Product** | 可交付 | 必须是软件 | 可以是服务、人工、 landing page |

## 关键洞察

### 1. MVP的功能选择

选择标准：这个功能是否服务于核心假设验证？

| 功能类型 | 是否保留 | 示例 |
|:---|:---:|:---|
| 验证核心假设必需 | ✅ | 核心功能流程 |
| 提升体验但非必需 | ❌ | 动画、精美UI |
| 未来可能需要 | ❌ | 扩展功能 |
| 竞品有但用户不用 | ❌ | 边缘功能 |
| 技术炫技 | ❌ | AI、大数据展示 |

### 2. MVP的验证指标

MVP必须有明确的验证指标：

| 指标 | 说明 | 目标 |
|:---|:---|:---|
| 关键转化率 | 从了解到选择的转化 | >5%（付费产品） |
| 激活率 | 完成核心任务的比例 | >30% |
| 留存率 | 次日/7日/30日留存 | 根据产品类型设定 |
| NPS | 推荐意愿 | >30 |

### 3. MVP的类型

| 类型 | 说明 | 适用场景 | 示例 |
|:---|:---|:---|:---|
| **原型MVP** | 可点击原型，无后端 | 概念验证 | Figma原型 |
| **Concierge MVP** | 人工服务模拟产品 | 服务类产品 | 人工推荐 |
| **Wizard of Oz** | 用户以为自动化，实际人工 | 技术未成熟 | 人工客服假装AI |
| **Landing Page** | 只有介绍页，收集意向 | 概念验证 | 产品预告页 |
| **单功能MVP** | 只有一个核心功能 | 工具类产品 | 只做搜索功能 |

### 4. MVP的迭代节奏

| 阶段 | 时间 | 目标 |
|:---|:---|:---|
| 设计 | 1-2周 | 确定MVP功能和验证指标 |
| 开发 | 2-4周 | 开发最小功能集 |
| 测试 | 1-2周 | 小范围测试，收集反馈 |
| 验证 | 2-4周 | 验证核心假设 |
| 决策 | 1周 | 继续/调整/放弃 |

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **MVP不够M** | 功能太多，开发时间长 | 砍掉非核心功能，只保留验证必需 |
| **MVP不可验证** | 上线后无法判断假设是否成立 | 设计明确的验证指标 |
| **MVP追求完美** | 花大量时间在UI和细节上 | 接受简陋，聚焦验证 |
| **MVP和最终产品混淆** | MVP做了最终产品的所有功能 | 明确MVP是验证工具，不是最终产品 |
| **MVP无验证指标** | 上线后不知道看什么数据 | 上线前定义验证指标 |
| **MVP验证后不行动** | 验证结果不支持，但继续投入 | 建立"验证-决策"闭环 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 新产品验证 | 成熟产品优化 |
| 创业早期 | 规模化阶段 |
| 方向不确定时 | 方向明确，需要提升体验 |
| 资源有限时 | 资源充足 |

## 行动触发器

- 当设计MVP时 → 问"这个功能验证什么假设？"
- 当MVP功能膨胀时 → 做"假设验证必要性测试"
- 当MVP上线时 → 检查验证指标是否可衡量
- 当验证结果出来时 → 根据结果决策，不凭直觉

## 关联卡片

- `yt-product-kernel-definition`：产品内核定义
- `yt-product-kernel-validation`：产品内核验证三维度
- `yt-product-kernel-hypothesis-test`：内核假设测试
- `yt-product-kernel-premature-optimization`：过早细化陷阱
- `yt-five-step-method`：五步法总纲
- `yt-entrepreneur-lean-validation`：精益验证方法

## 来源与验证

- 一堂产品内核实操课口述（Truman，2026-06-06）
- 一堂产品内核验证课口述（Truman，2026-06-06）
- 精益创业（Eric Ries）：MVP方法论
