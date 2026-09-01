---
id: task_20260902_wangyuyan-uncommitted-changes-ledger
title: 93 文件未提交改动落账（散点审计 R4，P0——为后续清理提供 git 兜底）
seq: 602
status: in_progress
assignee: wangyuyan
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-01T17:30:57.767676+00:00'
instance: wangyuyan-kimi-0902
---

# #602 未提交落账

## 背景

风清扬审计：截至 09-02 01:00 有 93 个已跟踪文件改动（+13063/-331）+ 165 个未跟踪文件未落账。后续 #601/#603/#604 有移动/清理动作，**先把在账改动落盘，给清理提供 git 回滚点**。

## 范围（三批分开 commit，只提交零改动）

1. **SKILL BOM 清洗批**：37 个 shared SKILL.md（#595 后续清洗，去 BOM，零内容改动）——提交前 diff 抽查 3 个确认仅编码层。
2. **todos/队列/任务单留痕批**：`90_control/todos/*`、队列相关、本次立项任务单。
3. **logs 批**：`logs/`、`90_control/*.log` 等运行日志。

## 边界

- 未跟踪文件（00_inbox 新素材、10_raw/sources 重复件）**不在本任务提交**——重复件归 #601 处置，素材留 untracked 等编排。
- 其他 agent 在制品（.agent/friction-log.md 等）逐项判断：内容完整则随批提交，半截工作不代提交。
- path-scoped add，严禁 `git add -A`（queue_transition 红线同律）。

## 交付物

3 个 commit + 执行报告（每批文件计数 + diff 抽查证据）。

## 验收

欧阳锋终审：`git status` 已跟踪改动清零（除其他 agent 当时在途工作面），三批 commit 信息可溯源。
