---
id: '318'
assignee: huangyaoshi
status: reviewed
claimed_at: 2026-08-13
reviewed_by: 欧阳锋
updated_at: '2026-08-13T11:39:59.114822+00:00'
task_id: '318'
priority: P2
review_date: '2026-08-13'
grade: A-
---

# #318：Feature 分层水位报告 kdo feature --by-layer（P2，基建 0.25d）

## 任务目标

按 L0-L5 统计周期表 verified 覆盖率，输出分层水位报告。价值：① 教练 agent 回答"我该学哪层"的数据依据 ② 周期表补卡优先级 ③ 用户群体水位实况。

> 来源：黄药师基建迭代洞察 P2-2（2026-08-13）。素材证据：10 案例全在 L0-L3，L4/L5 零触碰（仅黄谦导演提及"探索"）——用户群体实际水位在提示词层。

## 产出

- `kdo feature --by-layer` 命令：按层输出 Feature 总数/verified 数/覆盖率
- 首次报告：周期表 v0.8 分层水位（100 Feature：L0:3/L1:14/L2:38/L3:14/L4:18/L5:13，verified 25）
- 与 #317 evidence 分级衔接：分层报告含 evidence 分布（可选，若 #317 已完成）

## 验收标准

1. `kdo feature --by-layer` 输出各层覆盖率，数字与 JSON 一致
2. 报告含一行解读（哪层是当前水位、哪层是空白区）

## 边界

- 纯统计展示，不做补卡建议（建议归编排侧）
