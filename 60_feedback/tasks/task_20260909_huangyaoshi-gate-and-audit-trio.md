---
id: task_20260909_huangyaoshi-gate-and-audit-trio
title: "门禁审计五小件：pre-submit 绝对化声称 diff 检查器 + review-check 场次对账弱校验 + daily_review.py 自锁修复 + src_unknown 计数口径收紧 + 存在性核查节名白名单"
seq: 693
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-09
decision_source: 王语嫣 09-09 00:45 裁定采纳欧阳锋两建议书（diag_20260908_ouyangfeng-686-merge-claim-discipline + diag_20260908_ouyangfeng-retro-coverage-gap）+王语嫣 09-07 friction（daily_review 自锁）合并
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T17:32:39.771494+00:00'
---

# #693 门禁审计三小件（黄药师）

> 三件同族（都是门禁/审计脚本增强），一单三件串行做。排 #690 E 盘单后，不并行。

## 件 1：pre-submit「绝对化声称」diff 检查器（源自 #686 终审发现）

正文含「无信息损失/verbatim/零丢失」类措辞且文件含 merged_into 时 → WARNING 提示附 diff 证据（git show <merge前>^ vs 合并后主卡的已验节/未迁节清单）。与 F-035 负向判词同族：绝对化声称必附核查锚。WARNING 级不 HARD 拦。

## 件 2：review-check.py 场次对账弱校验

当日 todos 非叫醒动作块数 > 复盘文件场次节数时标 🟡 提示「可能缺场」，不硬拦（单场长会话多动作是常态，防误伤）。背景：09-08 欧阳锋 4 个实质动作块只 1 个落复盘——文件存在≠场次全覆盖，文件级审计看不见。

## 件 3：daily_review.py 自锁 PermissionError 修复

根因已实锤（王语嫣 09-07 23:38 friction + 欧阳锋 09-08 复盘场同撞）：脚本收尾 `LOG_PATH.open("a")` 撞 cmd 包装的重定向占用。修复=脚本内日志写改独立句柄或写 stderr 由包装统收。修完 schtasks LastTaskResult 应回 0（连续两晚 =1 脏信号）。

## 件 4：BODY_SRC_UNKNOWN 计数口径收紧（源自 #694 终审附议，王语嫣 10:45 裁定择案②）

`src_unknown` 仅当**独立成 list-item**（`- src_unknown`）时才计为占位；标题/行内提及不计。实证误报：#695 产卡单标题「P0回填7张旧卡src_unknown空洞」被计 2 处占位。不整类豁免任务单/诊断文件（里面也可能真有占位）。

## 件 5：「存在性核查锚点」识别扩为节名白名单

机器预审 F-035 类检查只认字面 `**存在性核查**`——扩展为节名白名单：「负向判词台账」「kdo query 检索记录」「存在性核查」任一即闭环（与宪法 v1.1 第二/六条落盘形态对齐）。实证漏认：#694 诊断 L208「负向判词台账」节 4 条全附锚仍被报缺失。

## 验收标准

- 件 1：合成样本卡（含「无信息损失」+merged_into）触发 WARNING 实测截图/日志
- 件 2：构造缺场场景标 🟡、全齐场景不误报，双向实测
- 件 3：修复后 daily_review 手动跑一轮 exit 0 + 当晚 23:37 实跑 LastTaskResult=0
- 件 4：#695 产卡单重跑 pre-submit 不再误报；真占位卡（合成 `- src_unknown` 列表项）仍拦
- 件 5：#694 诊断报告重跑预审，「负向判词台账」节被认列
- 欧阳锋终审

## 边界

- 不改既有检查器的判定口径，只新增；三件套串行，不插队 #690
