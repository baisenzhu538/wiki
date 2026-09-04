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
