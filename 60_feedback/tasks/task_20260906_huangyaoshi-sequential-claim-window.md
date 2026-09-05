---
id: task_20260906_huangyaoshi-sequential-claim-window
title: "queue_transition 同执行者连续派工窗口：显式多单指令免 force（第3次复发工具化，F-050 族）"
seq: 655
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 friction 三连（09-06 03:48/04:33/04:47 编排者一次性多单指令撞 #504 等待窗口，3 次 force+reason）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T05:10:00+08:00'
---

# #655 同执行者连续派工窗口微单（黄药师）

## 实证（第 3 次复发）
09-06 夜班三次：编排者一条指令派多单（#649+#650 / #651+#652），执行者 complete 前单→claim 下一单撞「同执行者 pending_review 占位」等待窗口，只能 --force+reason（留痕 3 次）。F-050 batch 豁免拍板过（#492）但覆盖的是批次验收场景，不是「显式多单连发」场景。

## 修法（二选一取稳者）
1. claim 增加 `--sequence` flag：同执行者显式连发时（编排指令含多单），允许 claim 下一单，状态机注记「sequential: 前单 pending_review」
2. 或等待窗口规则加豁免：前一单 pending_review 的审查者=本单终审者且挂审<30min 时放行连发

## 验收
模拟场景（两单连发）不再 force；force 台账不再新增同型记录；回归不红。
