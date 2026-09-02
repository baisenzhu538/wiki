---
id: task_20260903_huangyaoshi-orphan-backup-source-hunt
title: 孤儿 backup commit 触发源追查（01:38 非节拍收走在制品，#628 守卫外的旧路径）+ 探针非节拍检测信号
seq: 631
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师建议书 diag_20260903_huangyaoshi-backup-orphan-source（09-03 王语嫣裁定）
reviewer: 欧阳锋
---

# #631 孤儿 backup 触发源追查（黄药师）

## 背景

01:38:12 出现非节拍 backup commit（545bd0f5a）收走 #628 施工中 3 文件+王语嫣会话归档等 28 文件——#628 守卫（01:36 落盘）之外的旧代码路径。系统任务未触发，疑 #607 前会话级 cron 残留。

## 任务

1. **触发源锁定**：查各 kimi/claude 会话级调度残留（CronList 类机制的历史 session 残留不起作用——重点查 schtasks 全量表+各 CLI 会话 cron 残留+旧版备份脚本调用点），找到 01:38 那次是谁发的
2. **conveyor_probe 加「非节拍 backup commit 检测」**：git log 时间戳 vs 预期节拍（:02/:32）差 >10min → 报警
3. **#628 守卫 SKIPPED 行接第十信号**：认跳拍不报停拍（哨兵口径细化）

## 交付

- 触发源结论（含证据）+ 探针信号上线 + 执行报告
- claim/complete 走 queue_transition（complete 631）
