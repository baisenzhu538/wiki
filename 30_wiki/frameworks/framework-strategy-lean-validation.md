---
id: framework-strategy-lean-validation
title: 战略假设的精益验证流程
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-23
created_at: 2026-06-23
confidence: 0.85
trust_level: high
language: zh-CN
domain:
aliases:
  - audience:ceo
  - scene:diagnosis
  - skill-level:advanced
  - 低成本验证认知篇
  - 假设的精益验证流程
  - 战略假设的精益验证流程
  - 略假设验证
  - 略流程
  - 略精益验证
  - 益战略流程
  - 益验证
  - 设验证
source_refs:
related:
discoverable_by:
  - "战略精益验证"
  - "战略假设验证"
  - "精益战略流程"
tags:
---
# 战略假设的精益验证流程

> 把战略选择翻译成一个可验证的假设清单，并用精益工具按优先级和成本排序验证。

## 触发问题

- src_unknown
- src_unknown
- src_unknown

## 端到端流程

```
战略输出（来自 strategy-domain）
  ├── 赛道选择      → 验证：市场容量、竞争格局、时机窗口
  ├── 定位选择      → 验证：目标用户是否认可差异化价值
  ├── 商业模式      → 验证：用户是否愿意按预期付费
  ├── 增长路径      → 验证：渠道成本/转化率是否成立
  └── 壁垒假设      → 验证：优势能否持续、能否被快速模仿
           ↓
    用 ABCD/假设金字塔排序关键假设
           ↓
    用 FALSE 模型选择最低成本验证工具
           ↓
    按十倍速公式设计实验 → 执行 → 学习 → 战略迭代
```

## 战略假设类型 → 待验证问题 → 精益工具 → 通过/不通过标准

| 战略假设类型 | 典型问题 | 推荐精益工具 | 通过标准示例 | 不通过标准示例 |
|:---|:---|:---|:---|:---|
| 赛道存在 | 这个市场真实存在且足够大吗？ | 假营销/新闻稿测试、竞品分析 | 100+ 有效线索 | 投放后 CTR < 0.5% |
| 需求真实 | 用户会为这个概念付费吗？ | 假产品页面、预售 | 预售转化率 > X% | 1000 UV 0 订单 |
| 方案有效 | 产品/服务能交付承诺价值吗？ | 人工 VIP、MVP | NPS > 40 | 复购率 < 5% |
| 商业模式 | 单元模型能跑正吗？ | 最小版本、小规模试运营 | LTV/CAC > 3 | 单客亏损且无法收窄 |
| 增长可扩展 | 这个渠道能放大吗？ | 灰度测试、组合测试 | CAC 随规模不上升 | CAC 翻倍而转化率不变 |
| 壁垒可持续 | 竞争优势能维持多久？ | 竞品对标、时间窗口验证 | 6 个月内无直接竞品 | 巨头 3 个月内进入 |

> 上表工具映射来自 [[framework-lean-false-model]] 与 [[framework-lean-abcd-model]] 的接口设计 [conf=0.85, source=60_feedback/audit/cross-domain-bridge-design-specs.md §2.4]。

## 与相邻卡的关系

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 验证顺序错误 | 先验证商业模式，后发现需求不存在 | 按 A→B→C→D 优先级排序，A 类商业成败假设优先验证 |
| 把战略口号当假设 | “我们要做行业第一”不是可证伪假设 | 把口号改写成“如果……那么……”形式的预测句，并设定不通过标准 |
| 实验设计过度粗糙 | 用一个 landing page 验证需要深度访谈才能回答的问题 | 按 FALSE 成本光谱选择最省钱的“够好”工具 |
| 通过标准太软 | “用户很感兴趣”替代“用户付费” | 每个实验必须同时定义定量或强定性的通过/不通过信号 |

## 适用边界

- src_unknown
- src_unknown

---

*老顽童 · 2026-06-23 · 跨域融合计划（策略 A）P0 桥接卡*
