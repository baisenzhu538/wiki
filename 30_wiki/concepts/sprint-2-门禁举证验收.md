---
id: sprint-2-门禁举证验收
created_at: 2026-05-09
domain: master
source_refs:
- src_20260510_9e98a292-sprint-2-门禁举证验收
status: enriched
title: Sprint 2 门禁举证验收
type: concept
updated_at: 2026-05-09
pipeline:
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
related:
- '[[sprint-6-cli-gap-proposal]]'
- '[[sprint-2-gate-enrich-evidence]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
---

# Sprint 2 门禁举证验收

## Summary

KDO 管线的 ingest → enrich → gate 三阶段需要端到端验证。

关键设计决策： - 门禁是强警告非硬阻断（P0 exit 1 但有 --skip-gate 覆盖） - 举证是变更摘要非全量 diff（记录 what changed 而非源码 diff） - enrich 出口条件不依赖 status 字段（避免 parse_frontmatter nested YAML bug 误报）

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
## Output Opportunities

- src_unknown
- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研/框架做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |

## Synthesis

## Critique

#### 研究者偏差风险——调研者本身是最大的系统性偏差源

**研究者偏差风险**（Researcher Bias——来自科学哲学和方法论）：任何调研报告都是一个"被构建的叙事"——调研者的假设、工具、语言、时间窗口全都在形塑结果。这张卡片告诉你"什么是真的"，但它没告诉你"什么被排除了"。调研报告越详细，排除的东西越多——而那些被排除的，可能正是你最需要的。

> **核心质问**：这个调研报告在哪些关键决策点上排除了反例？调研者为什么选了这个时间点做调研？如果换一个不同背景的人来做同样的调研，结果会不会不同？

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
