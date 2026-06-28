---


id: framework-strategy-brm
title: 冉鹏版 BRM 框架（源于 IBM BLM 方法论）
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- strategy
source_refs:
  - 00_inbox/战略专题/引擎点火20260110 战略破局（冉鹏）(1)_ocr.md
  - pending_archive:src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
- 00_inbox/战略专题/引擎点火20260110 战略破局（冉鹏）(1)_ocr.md
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---# 冉鹏版 BRM 框架（源于 IBM BLM 方法论）

> ⚠️ 注意：国际通行的"BRM"= Business Relationship Management（IT与业务关系管理），是另一个领域。冉鹏的 BRM 源于他在 IBM 担任咨询总监时所学的 BLM (Business Leadership Model)，经过30年中国实战改编。华为"五看三定"就是 BLM 的中国版本。

## 三段结构

```
差距分析（起点）
  → 业绩差距（内部目标 vs 实际）
  → 机会差距（我们 vs 对手）
    ↓
战略规划（路径）
  → 五看：看行业/市场/客户/竞争/自己
  → 三定：定战略控制点/目标/路径
    ↓
战略执行（落地）
  → 连续动作：战略先行 + 动态适配
  → 组织对齐：能力→人数→意愿→架构→流程
```

## 三个关键词

**选择**：不是什么都做，是选择做什么不做什么
**竞争优势**：你比对手好在哪？而且这个优势能持续
**连续动作**：战略不是一次性的规划，是持续迭代的动态适配

## 企业业绩公式

`企业业绩 = 赛道景气 + 自己争气`

两者都重要，但战略的核心是"自己争气"——在不景气的赛道里也能做出好业绩。

## Agent执行指令

```python
# BRM框架分析流程
def brm_analysis(company):
    gaps = gap_analysis(company)  # 业绩差距 + 机会差距
    strategy = five_see_three_set(company)  # 五看三定
    execution = align_organization(strategy)  # 组织对齐
    return {"gaps": gaps, "strategy": strategy, "execution": execution}
```

## 外部验证

| 主张 | 验证结果 | 来源 |
|:
|:---|:---|
| BRM源于IBM BLM | ✅ 冉鹏曾任IBM咨询总监，BLM三段结构(差距→战略→执行)与BRM一致 | IBM BLM文档 |
| 五看三定=BLM变种 | ✅ 华为五看三定明确源自IBM BLM | 华为公开文献 |

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 跳过差距分析 | 直接做战略规划 | 强制第一步：列业绩差距+机会差距 |
| 把战略当一次性规划 | 年初做完就锁死 | BRM是循环——执行中的变化应回馈到差距分析 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：framework | 审核状态：待审*
