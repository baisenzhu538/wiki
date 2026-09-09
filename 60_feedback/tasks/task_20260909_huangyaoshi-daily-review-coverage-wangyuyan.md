---
id: task_20260909_huangyaoshi-daily-review-coverage-wangyuyan
title: "daily_review 复盘覆盖补齐：ROLES 加王语嫣（全员复盘口径，老朱 09-09 令）"
seq: 696
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-09
decision_source: 老朱 09-09 令「抽空复盘、按规定模式、内化迭代；其他 agent 包括王语嫣都要编排复盘任务入列」（王语嫣编排）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T18:43:28.709219+00:00'
---

# #696 复盘覆盖补齐（黄药师）

> 现状实锤：`kdo-tools/daily_review.py` ROLES 只有 laowantong/huangyaoshi/ouyangfeng 三角色（L27-30）。王语嫣交互场无自动复盘拉起，靠自觉——09-08 晚~09-09 的值守/拍板/部署长场就是靠老朱提醒才补。

## 工作项

1. ROLES 加 `("wangyuyan", "王语嫣")`——拉起逻辑与三角色同规格（Truman 11 章 + daily-context-save 自检）
2. 调研三 agent（research-digging/oscar/auto-partner）是外部消费者 agent（飞书端），不进本单——其复盘形态另行评估（建议书通道）
3. 与 #693 件 3（daily_review 自锁修复）同单施工可合并顺序：先修自锁再加角色，一次提审

## 验收标准

- 次日 23:37 实跑拉起四角色（logs 四份 headless 日志）
- 王语嫣 headless 复盘落 agent复盘/wangyuyan/daily-context/ 且 daily-context-save 自检 🟢/🟡
- 欧阳锋终审

## 边界

- 排 #693 后；洪七公/段王爷=外部挂起角色不入 ROLES（E058 口径）
