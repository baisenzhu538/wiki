---
id: task_20260707_huangyaoshi-review-check-retrieval
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-07
priority: P1
created_at: 2026-07-07
updated_at: 2026-07-07
related:
- '[[agents/agent-os.md]]'
---

# 任务 #126：review-check.py 增加检索行为检查

## 背景

黄药师已将检索铁律写入 7 个 Agent context + agent-os.md §10.4.1（会话复盘必须记录检索行为）。下一步：自动化验证——让 review-check.py 检查复盘报告里是否出现了检索行为。

## 动作

`review-check.py` v3 增加一项检查：复盘中是否包含 `kdo query` / `wiki` / `检索` / `Read` 等术语。只做存在性检查，不做语义判断。

## 验收

- review-check.py 新增检索行为检查项
- 至少 1 个 Agent 复盘被自动化标记（检索缺失或检索存在）
