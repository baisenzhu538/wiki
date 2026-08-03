---

id: concept-harness-cattle-not-pets
title: 牲口而非宠物：每次迭代用全新Generator实例
type: concept
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- ai-collaboration
aliases:
  - 每次迭代用全新
  - 每次迭代用全新Generator实例
  - 牲口而非宠物
  - 牲口而非宠物：每次迭代用全新Generator实例
  - 而非宠物
  - 迭代用全新
source_refs:
- 10_raw/sources/src_20260621_harness-engineering-wanghuan.md
discoverable_by:
  - 牲口而非宠物：每次迭代用全新Generator实例
  - 牲口而非宠物
  - 每次迭代用全新Generator实例
related:
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'
- '[[concept-ai-native-organization-five-steps]]'
- business-research-skill-oscar-13-weapon-system
- tool-yitang-amazon-bestseller
updated_at: '2026-06-29'
tags:
- audience:general
- scene:reference
- skill-level:advanced
---

# 牲口而非宠物

> 传统模式：一个Agent实例持续运行，不断修改自己的代码——久而久之，Agent会对自己的代码产生"情感依附"，舍不得删、不敢大改。牲口模式：每轮迭代起全新Generator实例，从checkpoint重建状态，无历史包袱。

## 对比

| 维度 | 宠物模式（传统） | 牲口模式（Harness） |
|:---|:---|:---|
| Agent实例 | 同一个实例持续运行 | 每轮全新实例 |
| 状态恢复 | 依赖Agent"记忆" | 从checkpoint重建 |
| 代码依附 | Agent不愿大改自己的代码 | 无包袱，该删就删 |
| 适用场景 | 简单连续任务 | 质量敏感任务（代码/报告/方案） |

## 为什么有效

1. **消灭"这是我的代码"心态**：新实例没有历史包袱，不会为了保护"自己的作品"而拒绝大幅修改
2. **状态一致性**：从checkpoint重建确保每轮从确定的基线出发
3. **与Swarm模式的同构**：调研域的Swarm模式同样受益——每次探索用新Worker实例，避免前一任务的"认知惯性"污染新任务

## 与GAN三角色的关系

GAN三角色（Generator/Executor/Evaluator）中的Generator天然适合牲口模式——每轮重新实例化，旧Generator的输出由Evaluator独立评审，不合格就扔掉。

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：concept | 审核状态：待审*
