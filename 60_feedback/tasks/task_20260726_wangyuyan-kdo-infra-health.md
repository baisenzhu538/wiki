---
id: task_20260726_wangyuyan-kdo-infra-health
task_id: 203
assignee: huangyaoshi
status: queued
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P2
source: 00_inbox/KDO-生产工厂调研与改进建议-2026-07-26.md (小昭外部审计)
---

# KDO基础链路健康检查 + 快赢项

> P2优先级——紧急任务到达时让路。

## 背景

小昭外部审计发现：生产队列#131-#162全reviewed（空窗期收窄中），后链路未激活，17牌组件库draft。三条低投入高杠杆动作。

## 任务

| # | 动作 | 执行者 | 产出 | 验收 |
|:--|:--|:--|:--|:--|
| 1 | 全库健康基线扫描 | 黄药师 | source_refs覆盖率(当前%)、broken links数量、status漂移量 | 三个数字写入 `60_feedback/audit/`，不修只取数 |
| 2 | 17牌组件库终审 | 欧阳锋 | `concept-kdo-component-library` draft→reviewed | 抽审≥5张牌，确认每张来自真实pitfall |
| 3 | 基础链路Dashboard | 黄药师 | 一个Markdown表（source_refs覆盖率/status分布/broken links）写入 `70_product/` | 三个指标+当前基线数字 |

## 边界

- 不修——本轮只取基线数字。修复任务是后续独立任务
- 不新增lint规则——遵循 `dk-kdo-leaky-pipe-pressure` 警告
- 紧急任务到达时暂停
