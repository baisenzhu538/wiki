---
id: file-flow-protocol-amend-shared-file-write
title: 《KDO 文件流转规范》增补件：共享文件并发写三条约定
type: protocol-amend
version: v1.0
author: 黄药师
created_at: '2026-08-25'
updated_at: '2026-08-25'
status: effective
amends: file-flow-protocol
source_task: '#505'
approved_by: 欧阳锋（2026-08-25 终审 PASS A，规范生效）
---

# 共享文件并发写三条约定（file-flow-protocol 增补件）

> 依据原件 §3「增补 = 另起新文件引用原件」订立，不改动已冻结的 v1.0 正文。
> 背景：E050 反向变体 ×3（#484/#485/#486 队列行被并发 commit 带走——共享 git index，
> add 文件级 + commit 全局，时间窗内被带走）+ #488 队列行错位（按旧快照插入主表外）。
> 根因：共享文件写操作无约定无工具兜底，靠自觉。

## S1 适用文件

多实例共享、并发写高发：`70_product/tasks/production-queue.md`、
`70_product/tasks/parking-lot-*.md`、`.agent/context.md`、`.kdo/CAPSULE_STARTUP.md`、
`70_product/tasks/dashboard.md` 及任何两个以上实例会写的文件。

## S2 三条约定（写操作必守）

| # | 约定 | 防什么 |
|:--|:--|:--|
| ① | **写前核最新态**：插入/改写前重新读取文件当前内容（队列类文件：grep 当前最大任务号 + 确认插入位置仍在主表内）；非原子流程用 `shared_file_guard.py snapshot/verify` 记录并比对基线（git HEAD + 文件 hash），STALE 即停笔重读 | #488 旧快照插入错位 |
| ② | **落盘即 path-scoped commit**：写完立刻 `git commit -m "..." -- <path>`（部分提交语义），不 `add -A`、不裸 `git commit`（全局提交会在时间窗内带走别人已 staged 的在制品） | E050 反向变体（行被带走） |
| ③ | **commit message 标 `by <instance>`**：谁写谁署名，并发冲突时可追溯可归责 | 冲突定责 |

## S3 工具落点（小改优先，不引新子系统）

| 层 | 机制 | 状态 |
|:--|:--|:--|
| queue_transition 写路径 | QueueLock + 读改写原子化 + `_git_commit_transition`（#390：path-scoped commit + `by <actor>` message） | 既有，已合规 |
| conveyor_probe 队列写点 | 3 个写函数统一套 QueueLock（同锁名 `production-queue`，#505 装饰器注入） | 本增补件落地 |
| 手工/编排侧写操作 | `90_control/scripts/shared_file_guard.py snapshot/verify`——写前基线比对，STALE 报警退出 1 | 本增补件落地 |

## S4 外部监督者（原件 §6.5 必答项）

- **约定遵守复核**：欧阳锋终审涉及共享文件的任务时抽查 commit 记录（path-scoped + by 署名）。
- **兜底巡检**：`gate-blocked.log` / force 台账之外，并发写事故一经发现按 E050 家族记录错误模式库并复盘。
- **本增补件修订**：按原件 §3 走（订正/增补另起新件，amends 引用本件）。

---

*黄药师 · 2026-08-25 · #505 交付物 · 依据风清扬 capsule-audit-08-24 F3 裁定 + E050/E055 + #488 实证*
