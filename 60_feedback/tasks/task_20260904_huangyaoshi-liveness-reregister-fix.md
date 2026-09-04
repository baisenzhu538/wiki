---
id: task_20260904_huangyaoshi-liveness-reregister-fix
title: "#635/#636 族返工第三刀：role-clock/liveness 路径陈旧事件重登记（17:17/17:47 连发实证）——告警面去重覆盖 role_registry 路径"
seq: 637
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 王语嫣值守拍复发实证（#636 落地后 liveness 陈旧事件仍重登记：走的是 role-clock/check-liveness 路径不在 conveyor 去重修正面内）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-04T12:49:29.730466+00:00'
evidence: 60_feedback/tasks/task_20260904_huangyaoshi-liveness-reregister-fix-workdir/evidence.md
reviewed_by: 欧阳锋
review_date: '2026-09-04'
grade: A-
---

# #637 liveness 重登记修根（黄药师）

## 背景

#635（liveness 有单才报）+ #636（conveyor 去重键事件身份化）落地后，陈旧 liveness 事件（08-27/09-02 的 stale 记录）仍每 30min 重登记进 PROPOSAL-PENDING（17:17/17:47 实证）。漏网路径=role_registry check-liveness 的告警状态文件（.kdo/role-liveness-alert-state.json）旧记录被反复重发。

## 任务

1. check-liveness 告警前查「该事件是否已登记且已划销」（事件身份=角色+原始时间戳，与 #636 同口径）
2. 顺带核查 #635「有单才报」是否真的生效（今晚空窗误报仍在发——疑似只改了判定没接通知面）

## 验证

- 清掉当前陈旧事件后，连续两拍零重登记
- 有单角色真死实例仍能正常报（防过度收敛）

## 交付

- diff + 两拍零重登记实证 + 真报警实证 + 执行报告
- claim/complete 走 queue_transition（complete 637）

## 执行报告（黄药师 2026-09-04 20:15）

**交付物**：
- `90_control/scripts/role_registry.py`：check_liveness 新增划销抑制闸 `_role_liveness_struck`（板面 PROPOSAL-PENDING 划销行=处置标记，角色粒度）
- `kdo-tools/conveyor_probe.py`：`_scan_gate_blocked` 改水位线扫描（`gate_seen_pos`），根治 500-cap 排序淘汰翻滚
- 回归测试：`90_control/scripts/tests/test_liveness_struck_suppression_637.py`（5 测）、`kdo-tools/tests/test_gate_blocked_watermark_637.py`（5 测）；旧迁移断言同步更新（`test_conveyor_probe.py`）

**完成内容**：
- 任务1（check-liveness 去重）：已报过（alert-state 在）+ 板面已有划销行（王语嫣处置过）+ 持续未恢复 → 抑制；恢复时 state 清零重新武装、再死必报（防过度收敛）
- 顺带根治漏网根因：gate_seen_v2 超 500 上限后按哈希字母序淘汰=随机淘汰，每拍淘汰一批、下拍重现为「新记录」（14:17~17:47 六连滴真根，#636 事件身份去重拦不住——每滴都是首次登记的独立身份）；append-only 日志改水位线，hash 集只兜尾部
- 任务2（#635 核查）：F-074「有单才报」13:18 落地（d5580782a）后零误报——09-03 晚 21:02~23:02 空窗误报全部在部署前；通知面=conveyor_probe 消费 gate-blocked.log 同一通道（无独立通知面漏接，疑点排除）

**验证**：
- 新增 10 测全绿 + 两目录全量 507 passed（含 #635/#636 回归）
- 实跑：修复随工作区上线后探针 5+ 拍（18:47→20:07）零陈旧重登记；板面未划销 liveness 回声=0；沙盒重扫 conveyor_state 0 新记录（gate_seen_pos=612=当前记录总数）
- 真报警实证：19:02 huangyaoshi（有单 #637 claimed + 全实例 stale）正确报警 → 19:07 上板 → 通知王语嫣（生产线真实事件，非构造）

**边界**：
- 划销抑制是角色粒度：恢复清零重新武装已覆盖「再死必报」主路径；恢复→再死的中间态以 state 清零为准
- 水位线依赖 gate-blocked.log append-only；截断/轮换 → 水位重置 + hash 集兜重（测试覆盖）
- notification-coverage-matrix：无新增事件类型/通道（复用既有 gate-blocked 行），无需补登

**需要谁动作**：欧阳锋终审。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（截断）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

## 终审记录

**结论**：PASS　**等级**：A-　**终审**：欧阳锋　**日期**：2026-09-04 20:48　**methodology_version**：v2.3

**通过维度**：
- O0 溯源（逐文件审代码）：git show 078940ade——role_registry.py 新增 `_role_liveness_struck`（+29 行，判定面=production-queue.md PROPOSAL-PENDING 段划销行 `- ~~…role-liveness｜{role} `，PROPOSAL 段标记单一真相源 B3 复用 conveyor_probe）；conveyor_probe.py `_scan_gate_blocked` 改水位线 `gate_seen_pos`（+25 行，替换原 500-cap `sorted(known)[-500:]` 哈希字母序淘汰）；test_conveyor_probe 迁移断言同步更新
- 逻辑骨架（独立审读）：划销抑制闸置于 `role in state` 且冷却分支之后——首报不压、冷却内压、冷却后已划销才压；恢复清零重新武装（防过度收敛）语义闭合；段/文件读不出 → False（fail-open，误发>漏发）。水位线三态迁移（老 state 压末尾吸收存量止滴 / 全新全扫 / 截断重置）边界闭合，hash 集只兜尾部且 `sorted(known)[-500:]` 保持有界不翻滚
- 验证复现（O3，独立重跑非引用）：新增 10 测全绿（test_liveness_struck_suppression_637 5 测 + test_gate_blocked_watermark_637 5 测）；两目录全量 pytest 90_control/scripts/tests/ kdo-tools/tests/ 实测 **507 passed**，与执行报告口径一致
- 生产态佐证：.kdo/conveyor_state.json `gate_seen_pos=614` 与 gate-blocked.log 时间戳起始记录数 614 精确对齐（证据 20:15 记 612，其后 20:19 F-034/E040 两条新记录推进至 614，属正常增量非回退）；板面 PROPOSAL-PENDING 段 liveness 行全为划销态、无未划销回声行；19:02 huangyaoshi 真报警行在 gate-blocked.log 尾部在位（19:07 上板→19:08 王语嫣划销，链路闭合）
- 边界判定：划销抑制=角色粒度、恢复清零重新武装覆盖「再死必报」主路径；水位线依赖 gate-blocked.log append-only、截断/轮换重置由测试覆盖——与执行报告边界节一致，口径不过宽不过窄

**缺陷（不阻断）**：`_scan_gate_blocked` 函数头 docstring 仍描述 #562 旧迁移语义（「首跑静默吸收存量记录」），新水位线语义以 #637 内联注释为准——注释漂移 🔵 无需本单修复，随后续维护带掉

**残余风险**：①划销抑制依赖板面划销行持久在位——若划销行被整段清出板块，`_role_liveness_struck` 判定失效，同死况将恢复 2h 冷却重报（误发方向、非漏发；与 #636 身份记忆同源局限，本单未恶化）；②水位线迁移吸收存量以「老方案已通知过（或翻滚通知过）」为前提——若存量中存在从未通知的记录将被静默吸收（首跑止滴意图内的已知取舍）

**scores**：溯源完整 25/25｜逻辑骨架 24/25｜暗知识密度 18/20｜可操作性 14/15｜表达质量 14/15
**blocking**：无　**residual_risks**：划销行清出板块→抑制失效（条件式）；存量吸收取舍（见上）

**存在性核查**：负向判词=「划销行清出板块→抑制失效」与「存量未通知记录被静默吸收」，均为条件式风险非现状断言。检索面=role_registry.py:139-160（判定面仅取 PROPOSAL-PENDING 段内划销行，源码实证）+ conveyor_probe.py:619-636（迁移吸收存量分支，源码实证）+ 板面现况（划销行全部在位，风险未触发）；结论：机制依赖成立、现状未发，判词限定为条件风险
