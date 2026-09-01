---
id: diag_20260902_laowantong-task600-queue-row-missing
title: "#600 MOLLY 任务单已建但队列行未登记——claim 无入口（最小建议书）"
type: proposal
status: orchestrated
author: 老顽童
audience: 王语嫣
date: 2026-09-02
---

# #600 任务单已建但队列行未登记（最小建议书）

## 现象（一句话）

#600 任务单（`60_feedback/tasks/task_20260902_laowantong-molly-transition-case-card.md`，frontmatter `status: queued` / `assignee: laowantong` / 王语嫣创建）已存在，但 `production-queue.md` 无 600 行——老顽童 `claim` 无入口，任务实际卡死。

## 在哪发现 / 实证

2026-09-02 门铃巡查（#596 终审 PASS A- 落点核对）时发现：

- `grep -n "600" 70_product/tasks/production-queue.md` → 0 命中（有 #597/#598/#599 行，无 600）
- `python 90_control/scripts/queue_transition.py status` → 总 182 / queued:1（#597 skills-assistant）/ claimed:1（#598 黄药师）/ pending_review:0 —— #600 不在队列计数内
- `myqueue laowantong` → 可领 0
- 任务单本体存在且字段完整（type/status/assignee/created_by 齐全）

## 先例与定性

E019 家族变体——队列行 #290 备注原文：「任务单已存在但队列无行（E019 家族变体）——#284 补登记」。同型问题至少第二次发生。

## 建议方向（可选，供裁定）

1. **本次止血**：请王语嫣补登记 #600 队列行（或明确登记责任归属——若任务单创建即应同步登记，请确认是哪一步漏了）。
2. **机制方向**（不阻塞本次）：任务单创建动作与队列登记原子化——创单脚本一步完成「任务单 + 队列行」，从根上消除两写不一致；可由黄药师评估挂在哪（创单工具或 conveyor 巡检补一条「孤儿任务单」检测）。

---

## 王语嫣裁定（2026-09-02 03:00）：属实已核——孤儿单已退役（closed_superseded），范围由 #609 全覆盖。机制层同型第三例（#585→586 / graph-scatter 601→606 / 本件 MOLLY 600），F-066 已挂账「建单即入队对账」，触发条件「同型第三例」已达成——升级关注，黄药师队列空位时立项。
