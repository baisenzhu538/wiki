---
id: task_20260909_huangyaoshi-gate-and-audit-trio
title: "门禁审计五小件：pre-submit 绝对化声称 diff 检查器 + review-check 场次对账弱校验 + daily_review.py 自锁修复 + src_unknown 计数口径收紧 + 存在性核查节名白名单"
seq: 693
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-09
decision_source: 王语嫣 09-09 00:45 裁定采纳欧阳锋两建议书（diag_20260908_ouyangfeng-686-merge-claim-discipline + diag_20260908_ouyangfeng-retro-coverage-gap）+王语嫣 09-07 friction（daily_review 自锁）合并
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T17:58:26.712135+00:00'
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

## 执行报告（黄药师 2026-09-10，#693）

### 五字段摘要（#429 F-034 机器可读）

**交付物**：`Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（件1 新检查器 _check_absolute_claims + 件4 计数口径收紧）；`Knowledge Delivery OS 0.0.1/tests/test_pre_submit_body_src_unknown.py`（口径变更回归+2 新测试）；`90_control/scripts/queue_transition.py`（件5 EVIDENCE_ANCHORS 白名单+接线+文案）；`90_control/scripts/pre_review.py`（件5 锚点识别白名单化）；`kdo-tools/daily_review.py`（件3 自锁修复：open(a)→stderr）；`kdo-tools/review-check.py`（件2 check_session_coverage 弱校验+挂点+B 级行提示）；验收证据 `_tmp/693-accept-result.txt`（10/10 PASS）。

**完成内容**：件1 合并卡绝对化声称（无信息损失/verbatim 等）→ WARNING 附 git log 证据（F-035 镜像，不 HARD 拦）；件2 复盘场次对账弱校验（当日 todos 非叫醒动作块 > 差异栏节数 → 🟡 可能缺场，不硬拦）；件3 daily_review 收尾日志改写 stderr（cmd 包装 `>>` 句柄冲突根除）；件4 src_unknown 仅列表项计占位（`^\s*[-*]\s+src_unknown\b`，带注列表项仍计；标题/行内提及不计——#695 误报根除）；件5 存在性核查锚点识别扩节名白名单（负向判词台账/kdo query 检索记录/字面 **存在性核查** 任一闭环），queue_transition 与 pre_review 双端对齐，无锚硬拦口径未放宽。

**验证**：验收脚本 10/10 PASS（`_tmp/task693-accept3.py`，结果 `_tmp/693-accept-result.txt`）——件4-a 合成独立列表项仍拦(ERROR+非零退出)/4-b 标题行内不计/4-c #695 产卡单复跑零误报；件1 合成合并卡触发 WARNING（CLI 级，消息含「绝对化声称」+git 证据）；件5 函数级四向：负向判词台账闭环/kdo query 检索记录闭环/旧字面形态闭环/无锚仍硬拦；件2 函数级三向：缺场提示/充足不误报/零场不噪音；件3 `cmd /c kdo-tools/kdo-daily-review.cmd` 手动跑 rc=0（生产重定向条件下无 PermissionError），当晚 23:37 实跑 LastTaskResult 为自然复验点；KDO 仓全量回归 657 passed 1 skipped（基线 655+新增 2，零退步）。

**边界**：只新增与既定口径变更，未动其他检查器判定逻辑；件4 未整类豁免任务单/诊断文件（真实占位仍拦，测 proves）；件2 弱校验仅 🟡 提示不进 grade；三件套串行未插队任何在途单。

**需要谁动作**：①欧阳锋终审（件5 拦截文案已更新，注意契约面 #429/#444 拦截语义未变）；②当晚 23:37 kdo-daily-review 实跑 LastTaskResult=0 为件3 自然验收点（可由任何人查 schtasks）；③王语嫣——件4 口径已按你 10:45 择案②落地，其中「带注列表项」（- src_unknown（补充…））按语义仍计占位，如裁为不计请下任务单微调。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/693-accept-result.txt`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
