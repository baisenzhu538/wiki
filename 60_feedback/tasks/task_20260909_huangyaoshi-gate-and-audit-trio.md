---
id: task_20260909_huangyaoshi-gate-and-audit-trio
title: "门禁审计三小件：pre-submit 绝对化声称 diff 检查器 + review-check 场次对账弱校验 + daily_review.py 自锁修复"
seq: 693
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-09
decision_source: 王语嫣 09-09 00:45 裁定采纳欧阳锋两建议书（diag_20260908_ouyangfeng-686-merge-claim-discipline + diag_20260908_ouyangfeng-retro-coverage-gap）+王语嫣 09-07 friction（daily_review 自锁）合并
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T00:50:00+08:00'
---

# #693 门禁审计三小件（黄药师）

> 三件同族（都是门禁/审计脚本增强），一单三件串行做。排 #690 E 盘单后，不并行。

## 件 1：pre-submit「绝对化声称」diff 检查器（源自 #686 终审发现）

正文含「无信息损失/verbatim/零丢失」类措辞且文件含 merged_into 时 → WARNING 提示附 diff 证据（git show <merge前>^ vs 合并后主卡的已验节/未迁节清单）。与 F-035 负向判词同族：绝对化声称必附核查锚。WARNING 级不 HARD 拦。

## 件 2：review-check.py 场次对账弱校验

当日 todos 非叫醒动作块数 > 复盘文件场次节数时标 🟡 提示「可能缺场」，不硬拦（单场长会话多动作是常态，防误伤）。背景：09-08 欧阳锋 4 个实质动作块只 1 个落复盘——文件存在≠场次全覆盖，文件级审计看不见。

## 件 3：daily_review.py 自锁 PermissionError 修复

根因已实锤（王语嫣 09-07 23:38 friction + 欧阳锋 09-08 复盘场同撞）：脚本收尾 `LOG_PATH.open("a")` 撞 cmd 包装的重定向占用。修复=脚本内日志写改独立句柄或写 stderr 由包装统收。修完 schtasks LastTaskResult 应回 0（连续两晚 =1 脏信号）。

## 验收标准

- 件 1：合成样本卡（含「无信息损失」+merged_into）触发 WARNING 实测截图/日志
- 件 2：构造缺场场景标 🟡、全齐场景不误报，双向实测
- 件 3：修复后 daily_review 手动跑一轮 exit 0 + 当晚 23:37 实跑 LastTaskResult=0
- 欧阳锋终审

## 边界

- 不改既有检查器的判定口径，只新增；三件套串行，不插队 #690
