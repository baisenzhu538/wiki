---
name: stage-4-validate
description: 域验证——Agent用域内卡片执行真实任务，记录失败，补缺修正（DDC模式）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [KDO, 验证, 测试, Agent实测, DDC]
    related_skills: [domain-iteration, stage-3-tooling, stage-5-assetize]
---

# Stage 4: 域验证

通过 Agent 执行真实任务验证域卡片体系是否可用。DDC（Demand-Driven Context）模式。

## 触发词

验证域、测试卡片、Agent实测、跑一遍试试、能不能用

## 约束

- 至少跑 5 个真实测试场景
- 每次 Agent 失败必须记录缺哪张卡
- 补缺后必须重新测试同一场景

## 执行步骤

### Step 1: 设计测试场景
从域索引入口卡提取 5-10 个真实场景

### Step 2: Agent 执行
每个场景：检索 → 检查命中 → 执行 → 产出

### Step 3: 记录结果

| 场景 | 检索命中 | 执行成功 | 缺失 |
|:--|:--|:--|:--|

### Step 4: 补缺
检索没命中 → 更新入口卡场景描述
执行缺工具 → 追加 Tool 卡

### Step 5: 重测 → 写验证报告
输出到 `60_feedback/validation/val_<日期>_<域>_验证报告.md`

## 收敛标准
- 20-30 个问题周期达到充分覆盖
- 检索命中率 ≥60%
- Agent 能独立完成域内典型任务
