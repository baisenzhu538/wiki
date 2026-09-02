---
id: task_20260902_huangyaoshi-instance-naming-role-only
title: 实例命名铁律落地：拉起器/状态机实例名去工具后缀（{role}-kimi → {role}），兼容在途旧名
seq: 620
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 直令铁律：实例命名只有角色名没有工具名（工具可换，工具名进实例名=制造混乱）
reviewer: 欧阳锋
---

# #620 实例命名去工具后缀（黄药师）

## 背景

老朱 09-02 直令：双实例/拉起实例命名**只有角色名**，禁带工具后缀（laowantong-kimi → laowantong）。理由：工具可换（kimi 没额度会换其他 agent 干活），工具名进实例名制造不必要混乱。

实证现状：`kimi-headless-launch.py` L45 prompt 模板写死 `--instance {role}-kimi`；队列里已有 claimed-huangyaoshi-kimi（#619 在途）等旧名。

## 任务

1. `90_control/scripts/kimi-headless-launch.py`：实例名改 `{role}`（工具仍走 TOOLS 路由表，工具是变量不进名字）
2. `queue_transition.py` 实例锁匹配兼容：过渡期接受 `{role}` 精确匹配 + `{role}-<tool>` 旧名尾缀（在途单如 #619 claimed-huangyaoshi-kimi 须能 complete）；新 claim 一律裸角色名
3. `#616` 翻转通道里「查 wangyuyan 登记实例」的逻辑同步裸名口径
4. active-instances.json / liveness 登记面如有工具后缀写入，一并改

## 红线

- 过渡期兼容不清历史数据（队列里旧名行不改写）
- 回归：旧名 complete 能过 + 新名 claim/complete 全流程走通

## 交付

- diff + 回归实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 620）
