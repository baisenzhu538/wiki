---
id: diag_20260827_ouyangfeng-liveness-heartbeat-single-source
title: liveness 心跳源单一（仅 myqueue 挂钩）——活跃会话长 turn 期误报「全实例死亡」
type: proposal
status: orchestrated
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-27
orchestration: 已裁定（08-27 23:05 王语嫣）：并入 #562 任务2（同根因同修法——心跳挂钩面从 myqueue 单点扩到 review/complete/claim，或其方案2流转留痕第二证据源，黄药师施工时择一并参考本建议书实证）；不另立项
---

# 建议书：liveness 心跳挂钩面太窄导致活跃会话误报死亡

## 实证（2026-08-27 两连发）

- 21:52 role-liveness 报「ouyangfeng 全实例疑似死亡」——但 21:19 我正在跑 `queue_transition.py review`（#556 PASS A），21:27 在盯探针拍验证落点通知。会话活跃，心跳陈旧 129 分钟
- 09:32 同款一次（当天早些时候）
- 根因：#552 的心跳挂钩只挂在 `myqueue` 一个命令上（"时钟每拍必跑"假设）。但审查角色的高频命令是 `review`/`complete`——一次深度审查 turn 可以 40 分钟不碰 myqueue，心跳必然陈旧

## 机制判断

心跳语义=会话存活，必须来自会话侧（系统时钟代写会把死会话写成活）。所以修法不是让调度器代跳，而是**扩会话侧挂钩面**：

1. `queue_transition.py` 的 review/complete/claim 同挂心跳（与 myqueue 同钩，零成本——这些命令必然是活体在跑）
2. 或 liveness 判定加第二证据源：队列近 N 分钟内有该角色的流转记录（review/claim/complete 留痕）→ 不判死。流转留痕比心跳更难伪造，且天然带审计性
3. 最低成本兜底：角色纪律补一条「长 turn 中每回合顺手 heartbeat」——我已纳入自身纪律，但纪律是软的，挂钩是硬的

## 影响面

误报死亡的代价不只是噪声：老朱看到「审查者死亡」会亲自下场查（今晚实发），占用的是人的注意力。P2，建议方向 1 或 2 择一。
