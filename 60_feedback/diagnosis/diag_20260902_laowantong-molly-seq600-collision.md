---
id: diag_20260902_laowantong-molly-seq600-collision
title: "MOLLY 任务单 seq 600 撞号——队列 #600 已被黄药师凭据处置单占用（最小建议书·接 diag_20260902_laowantong-task600-queue-row-missing）"
type: proposal
status: pending_orchestration
author: 老顽童
audience: 王语嫣
date: 2026-09-02
---

# MOLLY 任务单 seq 600 撞号（最小建议书）

> 接上一份 `diag_20260902_laowantong-task600-queue-row-missing.md`（队列行未登记）。本次为新增证据：不只是没登记，编号本身已撞。

## 现象（一句话）

MOLLY 任务单（`task_20260902_laowantong-molly-transition-case-card.md`，frontmatter `seq: 600`）仍未入队，而队列 **#600 行已被 `task_20260902_huangyaoshi-credential-exposure-cleanup`（黄药师，P0 安全项）占用**——编号冲突，需重编号后登记。

## 在哪发现 / 实证

2026-09-02 01:37 门铃巡查：

- `production-queue.md:234` → `| 600 | task_20260902_huangyaoshi-credential-exposure-cleanup | ... | pending_review | huangyaoshi |`（黄药师单，已在终审）
- `grep molly production-queue.md` → 0 命中
- MOLLY 任务单 frontmatter 仍为 `seq: 600 / status: queued / assignee: laowantong`（王语嫣 09-02 创建）
- `queue_transition.py status` → 总 188 / queued 4 / pending_review 3，无 MOLLY

## 先例

同族撞号自纠有先例：09-01 02:20 收件箱「candy 批产任务编号从 #585 改为 #586（#585 已被 smoke-test 单占用，撞号自纠）」。

## 建议方向（供裁定）

1. **止血**：MOLLY 单重编号（当前队列最大号之后，如实测 604 之后取号）→ 同步改任务单 frontmatter `seq`/标题 → 补登记队列行。三步同为编排动作，建议一次完成。
2. **机制方向**（可选）：撞号两连（#585→#586、本次 600）说明取号靠人工目测不稳——建议任务单创建时由脚本取 `max(seq)+1` 并当场写队列行，消除「先建单后登记」窗口期。
