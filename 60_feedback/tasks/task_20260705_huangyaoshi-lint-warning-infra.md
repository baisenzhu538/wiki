---
id: task_20260705_huangyaoshi-lint-warning-infra
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-05
priority: P2
created_at: 2026-07-05
updated_at: 2026-07-05
related:
- '[[task_20260629_kimi-lint-content-debt-by-domain]]'
---

# 任务 #108：lint WARNING 基础设施迭代

## 背景

#28 完成后 lint WARNING ↓92%，剩余 ~160 条 WARNING 主要是内容质量类（如 weak synthesis、missing key terms）。欧阳锋判断：这些需要黄药师迭代 lint 规则或工具，不是内容生产问题。

## 任务

分析 160 条 WARNING 的分类和根因，判断哪些需要：
1. Lint 规则调整（如降低误报）
2. 工具改进（如自动补全建议）
3. 内容修复（确实需要老顽童修的，拆任务给老顽童）

## 验收

- 分析报告（分类 + 根因 + 建议）
- 不超过 20 条确实需要老顽童修的，拆分任务入队
- 其余通过规则/工具迭代消化

## 优先级

P2——不阻塞主线队列。黄药师在 #69/#73/#98 之后处理。
