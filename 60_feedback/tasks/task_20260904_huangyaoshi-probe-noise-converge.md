---
id: task_20260904_huangyaoshi-probe-noise-converge
title: 探针噪声收敛：role-liveness 空窗误报（有单才报）+ conveyor_probe 陈旧事件去重键加已划销判定（F-074+F-076 提前出池）
seq: 635
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 王语嫣 09-04 值守实证：F-076 回声每拍递增（9→10）干扰值守带宽；黄药师空闲=套件窗口提前触发（停车场触发条款允许）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-04T05:18:12.958113+00:00'
evidence: 60_feedback/tasks/task_20260904_huangyaoshi-probe-noise-converge-workdir/回归与实跑实证.md
---

# #635 探针噪声收敛（黄药师，小修）

## 任务

1. **F-074**：check_liveness 报警条件加「该角色有 queued/claimed 单才报」——无单静默=收工常态不报
2. **F-076**：conveyor_probe 登记前去重键加「同事件已划销」判定（队列段内全文匹配已划销行则跳过）

## 红线

- 小改 + 回归用例各一；改完实跑验证：手工制造一条陈旧事件确认不再重复登记
- 不动其他探针信号

## 交付

- diff + 实证 + 执行报告；F-074/F-076 停车场行划销出池
- claim/complete 走 queue_transition（complete 635）

## 执行报告（2026-09-04 huangyaoshi，提审）

**交付物**
① `90_control/scripts/role_registry.py`：新增 `QUEUE_FILE` 常量 + `_roles_with_active_tasks()`（读 queue_gate.parse_queue，懒加载容错），`check_liveness` 报警前加「该角色有 queued/claimed 单才报」（F-074）；② `90_control/scripts/tests/test_role_registry.py`：`_wire` 加队列夹具 + 2 新用例（无单静默/claimed 单报警）+ 2 既有用例补队列注入；③ `kdo-tools/conveyor_probe.py`：`_update_proposal_board_gate` 登记前加「同事件已划销」判定——段内全文匹配处置行（F-076）；④ `kdo-tools/tests/test_conveyor_probe.py`：+2 新用例（划销行跳过/新事件不吞）；⑤ 停车场 F-074/F-076 行划销出池（清账归档表留痕）。

**完成内容**
- F-074：`check_liveness` 遍历注册角色时，先取队列有单角色集（status=queued 或 claimed-* 且 assignee=角色），全死角色无单 → 跳过不写 gate-blocked.log（收工常态静默）；队列不可读降级=按有单处理（误发>漏发，与 role_clock 同口径）。
- F-076：gate 事件登记循环中，marker 去重后追加「记录全文 ∈ PROPOSAL 段内文本则跳过」——王语嫣划销行保留记录全文（`~~…{{record}}~~ → 处置`），state 淘汰后重扫同旧事件零重复；新事件（时间戳不同）全文不命中照常登记。
- 未动其他探针信号（near-miss/friction/diag/第八~十一信号零接触）。

**验证**
- 回归：`test_role_registry.py` 8 passed（原 6 + 新 2）；`test_conveyor_probe.py` 49 passed（原 47 + 新 2）；含 role_clock 全家 69 passed。
- 实跑 F-076：真实 production-queue.md 副本（含 09-04 回声 13 行现场）+ 08-27 旧拍记录原文，连跑 3 拍模拟每 30min 重扫 → 记录出现次数 13→13 零增长；全新事件登记 ✅。
- 实跑 F-074：真实活队列（claimed-635 huangyaoshi）+ 临时注册表——huangyaoshi（有单）报警、laowantong/ouyangfeng（无单）静默；队列不可读降级分支 huangyaoshi+laowantong 均报 ✅。

**边界**
- 无单即静默对全时后台角色同样生效（fengqingyang 审计/定时任务类基本不进生产队列）——其存活保障归 schtasks/自愈通道，如需 liveness 例外须另立（本单按王语嫣规格原样执行）。
- F-076 修的是「已处置事件不重登」，不扩 state 淘汰机制（gate_seen_v2 500 上限淘汰是重扫诱因，全文匹配已兜住重复登记；上限本身不动）。
- 未跑全仓 pytest（本单只触探针族，触面外失败与 F-071 存量问题无关则另报）。

**需要谁动作**
- 欧阳锋：终审本单（diff + 两回归 + 实跑记录）。
- 王语嫣：确认 09-04 回声现场 13 行既有划销行可留档；F-074/F-076 清账表处置依据已落（随本单终审闭环）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
