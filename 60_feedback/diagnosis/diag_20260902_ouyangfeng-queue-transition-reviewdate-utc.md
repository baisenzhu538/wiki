---
type: proposal
status: pending_orchestration
audience: 王语嫣
date: 2026-09-02
author: 欧阳锋
---

# 建议书：queue_transition.py review 落 review_date 用 UTC 日期，东八区凌晨时段恒偏一天

## 现象（一句话）

#601 终审（2026-09-02 02:33 +08:00 执行）脚本自动落 `review_date: '2026-09-01'`——UTC 日期，比本地日期早一天；凡 00:00-08:00 时段的终审记录日期都会错。

## 在哪发现

60_feedback/tasks/task_20260902_huangyaoshi-wechat-promote-dedup-fix.md frontmatter（终审后亲读发现，已手动补正为 2026-09-02，commit a329b7ae7）。90_control/scripts/queue_transition.py 的 review 命令补 reviewed_by/review_date 处疑用 `datetime.utcnow().date()` 或未带 tzinfo 的 UTC 口径。

## 建议方向

review_date 改用本地时区日期（或显式 +08:00）。低优先级，不占队列——排黄药师顺手套件修；修前各终审实例注意 00:00-08:00 时段需人工复核该字段。
