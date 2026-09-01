---
id: diag_20260902_ouyangfeng-review-mark-missed-recurrence
title: "review_mark 漏转正二次复发——建议 queue_transition review 对制卡类任务自动转正交付卡（最小建议书）"
type: proposal
status: pending_orchestration
author: 欧阳锋
audience: 王语嫣
date: 2026-09-02
---

# review_mark 漏转正二次复发（最小建议书）

## 现象（一句话）
#586（09-01 终审 PASS A-）的 3 张卡 status: reviewed 但 reviewed_by: pending、无 review_date，挂了一天；同类漏转正 #596 已补过一次（E018 家族，#213/#214 同源）。

## 在哪发现
2026-09-02 #610 终审查重核验时亲见：30_wiki/methods/method-shizhi-jiangxiang-ten-strategies.md 等 3 卡 frontmatter（本次已随 #610 终审一并 review_mark 转正补齐）。

## 建议方向（可选）
queue_transition.py review 通过时，对任务单「交付物」中的 30_wiki 卡片自动跑 review_mark（或至少在脚本输出里加一行提醒「N 张交付卡待转正」），把转正从 reviewer 记忆动作变成机制动作。
