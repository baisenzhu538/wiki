---
id: task_20260904_huangyaoshi-liveness-reregister-fix
title: "#635/#636 族返工第三刀：role-clock/liveness 路径陈旧事件重登记（17:17/17:47 连发实证）——告警面去重覆盖 role_registry 路径"
seq: 637
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 王语嫣值守拍复发实证（#636 落地后 liveness 陈旧事件仍重登记：走的是 role-clock/check-liveness 路径不在 conveyor 去重修正面内）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-04T10:16:53.539632+00:00'
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

## 终审记录
