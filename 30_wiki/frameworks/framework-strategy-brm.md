---
id: framework-strategy-brm
title: 冉鹏版 BRM 框架（源于 IBM BLM 方法论）
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-04
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- strategy
source_refs:
- 00_inbox/战略专题/引擎点火20260110 战略破局（冉鹏）(1)_ocr.md
- pending_archive:src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
  - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown - src_unknown
  - src_unknown
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
related:
  - '[[framework-strategy-basics-01-core]]'
  - tool-strategy-gap-analysis
  - case-strategy-exit-remove
updated_at: '2026-07-04'
---

# 冉鹏版 BRM 框架（源于 IBM BLM 方法论）

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

- **BRM 是战略规划工具，不是持续迭代引擎**：它覆盖"差距分析→战略规划→战略执行"的规划闭环，但执行之后的反馈收集、假设验证、认知升级需要借助 Y模型 或其他机制
- **执行中的变化应回馈到差距分析**：BRM 不是年初做完就锁死的静态规划——市场变化、执行结果、新情报应触发新一轮差距分析
- **适用于**：年度战略规划、新业务方向探索、组织级战略对齐
- **不适用于**：日常运营决策、单次微型实验、个人时间管理

## 与 Y模型 的关系

BRM 和 Y模型 不是竞争关系，而是分层协作：

| 层级 | 工具 | 做什么 |
|:---|:---|:---|
| **战略规划层** | BRM | 五看三定、差距分析、组织对齐——产出战略方向和资源配置方案 |
| **认知引擎层** | Y模型 | 对 BRM 产出的每条战略假设做持续验证和迭代——"我们定的这个战略方向对吗？什么证据支持？什么证据反对？" |

**协作方式**：BRM 做战略规划 → Y模型 引擎对关键战略假设做持续验证 → 验证结果回馈到下一轮 BRM 差距分析。BRM 负责"想清楚"，Y模型 负责"验证对"。

> 引擎循环参见：[[method-yitang-y-model-engine-cycle]]

---

*卡片类型：framework | 审核状态：待审*
