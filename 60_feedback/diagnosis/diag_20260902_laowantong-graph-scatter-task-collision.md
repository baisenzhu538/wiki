---
id: diag_20260902_laowantong-graph-scatter-task-collision
title: 图谱散点治理任务单 seq=601 撞号且未入队——老顽童 myqueue 可领 0，治理单悬空
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 老顽童
created_at: 2026-09-02
source_refs:
- 60_feedback/tasks/task_20260902_laowantong-graph-scatter-cleanup.md
- 70_product/tasks/production-queue.md
---

# 建议书：图谱散点治理任务单撞号未入队

## 发现（实测证据）

1. **任务单已建**：`60_feedback/tasks/task_20260902_laowantong-graph-scatter-cleanup.md`，frontmatter `seq: 601`，assignee: laowantong，status: queued。
2. **队列撞号**：`production-queue.md` 里 **#601 已被占用**——`task_20260902_huangyaoshi-wechat-promote-dedup-fix`（黄药师，pending_review）。队列当前最大号 **#605**。
3. **未入队**：`grep "graph-scatter" 70_product/tasks/production-queue.md` = 0 命中。该治理单从未登记进队列。
4. **后果实测**：`python 90_control/scripts/queue_transition.py myqueue laowantong` → 可领 0。老顽童按纪律无法领取——**图谱散点治理（老朱 0902 直接指令）实际处于无人可领的悬空态**。

## 先例

#585→#586 撞号自纠（09-01 王语嫣编排更正，收件箱有通知）。本次是同一模式第二例：**建任务单时 seq 抄了队列号但没有同时入队占号**。

## 建议

1. graph-scatter 单改号 **#606**（任务单 frontmatter seq + 队列登记行同步改）。
2. 入队后老顽童即刻 claim 施工（任务内容已逐字读过，范围 A/B/C 清楚）。
3. 机制建议：任务单创建脚本/流程里加一步「seq 与队列对账」——建单即入队，或建单时校验 seq 未被占用。防第三例。

## 本建议书合规声明

- type: proposal / status: pending_orchestration / audience: 王语嫣（探针契约三元组齐全）
- 落盘后当场跑 conveyor_probe 验回执（A7 纪律）
