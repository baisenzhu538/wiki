---
id: 511
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-24T18:38:36.839040+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/memory_capsule.py
- 90_control/scripts/queue_transition.py
- kdo-tools/conveyor_probe.py
- kdo-tools/tests/test_capsule_events.py
- 90_control/scripts/tests/test_queue_transition.py
- 90_control/infrastructure-inventory.md
reviewed_by: 欧阳锋
review_date: '2026-08-24'
grade: A
---

# #511 记忆胶囊事件层补 4 类关键事件（queue_transition / decision / friction / error）

- **任务号**：#511
- **状态**：queued
- **assignee**：huangyaoshi（事件层扩展；欧阳锋终审）
- **优先级**：P2（排在 #505-#510 后；不压当前基建线）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-capsule-audit-08-24.md` F1 裁定采纳）

## 背景

`activity_log.db` 16 条事件**全部是 `review_saved`（复盘登记簿）**——无 queue_transition / decision / friction / error 事件。影响：靠「提取记忆胶囊」只能还原「谁落了复盘」，不能还原「谁领单/提审/拍板/踩坑」；真正的全量上下文在 L1-full 原文，但事件索引缺工作流语义。F-041 已留「L0 后续扩 event_type=judgment/decision/insight」的演进钩子，本单是其落地。

## 任务

1. 事件层补 4 类关键事件写入：
   - `queue_transition`：claim/complete/review 流转时落事件（挂 queue_transition 写入点，复用 #434 自动写入端模式）
   - `decision`：终审结论/拍板记录落事件
   - `friction`：friction-log 新增行落事件
   - `error`：gate-blocked / force-exceptions 落事件
2. 失败可见不静默（沿用 #434 口径）；单写入面（每类事件一个写入点，不多头写）
3. 幂等：重跑/重试不产生重复事件

## 验证（验证分层）

- L1：构造四类动作各一次，activity_log 出现对应事件类型
- L2 狗粮：一次真实 claim→complete→review 链，事件层可还原全过程
- L3 待活体：风清扬每日审计（#507 digest）只读事件层即可还原「谁领单/提审/拍板/踩坑」

## 边界

- 只做事件层补充，不改 L1-full 采集；不动 review_saved 既有写入
- 不回填历史事件（只向前生效，同 #389 口径）
- 与 #507 digest 衔接：digest 抽数源不变，事件层丰富了其原料

## 关联

- 风清扬建议书 F1（capsule-audit-08-24，含「事件层太薄」实测）
- F-041（判断落盘锚点，L0 事件类型扩展钩子）/ #434（L0 自动写入端）/ #432（记忆胶囊 L0）
- #507（每日 digest 消费端）

## 需要谁动作

- **黄药师**：四类事件写入点
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：事件层补 4 类关键事件——①统一入口 `memory_capsule.log_event_safe`（失败可见不静默：stderr 报警+pending-git-commits.log 待收口，不阻断主流程；各写入点只调它不碰 sqlite=单写入面）；②`queue_transition` 事件：queue_transition main() 成功钩（claim/complete/review，task_9999_ 测试件不写）；③`decision` 事件：review 动作同步落（verdict/grade/reviewer）；④`friction` 事件：conveyor_probe `_scan_friction` 新行逐条落（agent 取行首 [角色]，friction_seen state 幂等——重跑不重复）；⑤`error` 事件：`_log_gate_blocked`（真实拦截，测试件同 #483 分流不写）+ `_log_force_exception`（force 例外即风险事件）。**测试污染事故防范**：既有 test_force_exception_ledger_written 被新钩波及写真实库（task_test_444 入真实事件库 id=53）——已删行+给该测试加 _capsule_event mock 隔离，复查零残留。

**交付物**：
- `kdo-tools/memory_capsule.py`（log_event_safe 统一入口）
- `90_control/scripts/queue_transition.py`（_capsule_event 钩+main() 流转/终审事件+gate-blocked/force error 事件）
- `kdo-tools/conveyor_probe.py`（friction 事件写入）
- `kdo-tools/tests/test_capsule_events.py`（新：6 例）+ `90_control/scripts/tests/test_queue_transition.py`（1 处测试隔离修复）
- `90_control/infrastructure-inventory.md`（memory_capsule 行更新）

**验证**：
- L1：`cd kdo-tools && python -m pytest tests/ -q` → **90 passed**（新增 6 例：写行成功/DB 只读失败可见不抛/流转+decision 双事件/gate-blocked error 真实写+测试件不写/force 例外 error 写+测试件不写/friction 行 agent 解析）；`90_control/scripts` 116 passed 零回归；真实事件库测试残留复查 0
- L2 狗粮：本单 complete 即真实触发——提审后 activity_log 应出现 #511 queue_transition 事件（complete 时验证，欧阳锋 review 时 decision 事件再补一环——真实 claim→complete→review 链由本单自身走完）
- L3 待活体：风清扬每日审计（#507 digest 明早 06:00）只读事件层即可还原「谁领单/提审/拍板/踩坑」

**边界**：只做事件层补充，L1-full 采集未动；review_saved 既有写入未动；历史事件不回填（向前生效同 #389）；老朱口头拍板（非机器可捕获的 decision）维持现状不落事件——机器可捕获面=review 终审结论，口径已在案；digest 抽数源未改（事件层丰富其原料）。

**需要谁动作**：欧阳锋终审本单（review 动作本身将触发首个真实 decision 事件——终审即狗粮）；风清扬知悉事件层已丰富（明早 digest ①节将出现非 review_saved 类型事件）。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**
- **版本对齐**：冻结版=02:31 commit cc0e52d3f=提审时刻；提审后补件 f52ad7a4f（02:33，测试隔离 mock，生产代码零改动）已在执行报告"测试污染事故防范"节如实声明——透明覆盖，裁定合规但记录：补件晚于提审 2 分钟，属提审后补丁，今后宜先补件再提审
- **O0 溯源（逐条对 diff 原文）**：①`log_event_safe` 统一入口 ✓（失败 stderr 报警+pending-git-commits.log 待收口，不阻断主流程；写入点只调它不碰 sqlite=单写入面）；②queue_transition main() 钩 ✓（claim/complete/review→queue_transition 事件，review→decision 事件含 verdict/grade/reviewer，task_9999_ 分流不写）；③gate-blocked/force 例外→error 事件 ✓（同 #483 测试件分流纪律）；④conveyor_probe friction 新行逐条落 ✓——**我起疑复核的一点**：friction-log 数据行是 `YYYY-MM-DD｜场景｜…` 格式并非 `[角色]` 开头，但 `_scan_friction` 返回行包装为 `[{role}] {ln}`（`conveyor_probe.py:429` role 取目录名），正则 `^\[([^\]]+)\]` 正好匹配——设计与正则自洽 ✓；friction_seen state 幂等（只处理新行，重跑不重复）✓
- **独立复跑**：kdo-tools 90 passed、90_control/scripts 116 passed，与声明一致 ✓
- **事件库实测（亲自查 sqlite）**：56 条——review_saved 52（既有）+queue_transition 2（含 id=58 本单 complete 狗粮事件）+error 1（id=60 force-exception 真实拦截）——三类新事件活体在库 ✓
- **存在性核查**（#433 负向断言"测试残留 0"附证）：亲自跑 `agent_id LIKE '%test%' OR payload LIKE '%task_test%'/'%task_9999%'` 计数=**0**；唯一 `capsule_test` 条目为 id=1（2026-08-22 #432 狗粮测试事件）=历史既有非本单污染 ✓ | 核查人：欧阳锋 08-25
- **边界**：L1-full 采集未动、review_saved 既有写入未动、历史不回填 ✓；老朱口头拍板不落事件（机器不可捕获）口径在案合理
- **观察项（非本单范围，不阻断）**：`_log_gate_blocked` 外层仍有 `except Exception: pass`（原状保留），事件写入失败可见性靠 log_event_safe/_capsule_event 内层双保险——若外层先失败（如日志文件不可写）事件钩不执行，静默风险在旧层不在新层，本单边界内不动它合理
- **后续**：本 review 流转将触发首个真实 decision 事件（终审即狗粮），流转后我验证入库；明早 06:00 digest ①节=L3 活体验证点（风清扬）
