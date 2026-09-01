---
id: task_20260902_huangyaoshi-image-detail-deadloop-fix
title: image_detail 死循环修复——识别该类型直接 mark_seen 跳过（三症联诊动作3漏项补立）
seq: 608
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 黄药师建议书 diag_20260902_huangyaoshi-vault-scatter-obsidian-config-pipeline 动作3（原口径「随#1同单」但 #601 任务单未含，09-02 王语嫣裁定补立）
reviewer: 欧阳锋
---

# #608 image_detail 死循环修复（黄药师）

## 背景

黄药师三症联诊症状 3 实测暴露的真 bug：采集链监控对 image_detail 类型链接死循环重试（不 mark_seen，每 10 分钟空转重试）。原建议口径「随 #601 同单」，但 #601 任务单未含此项（提审后不可追加，E025），补立本单。

## 任务

采集链监控脚本中识别 image_detail 类型 → 直接 mark_seen 跳过，不进解析重试。

## 红线

- 小改单点，不碰 #601 刚终审的去重/归一化逻辑（若 #601 未终审完成需等其 reviewed 后动手，防同文件冲突）
- 改完实跑一轮监控验证：image_detail 类链接一轮 mark_seen 后不再重复出现

## 交付

- 修复 diff + 实跑验证证据（前后两轮日志对比）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 608 附证据）
