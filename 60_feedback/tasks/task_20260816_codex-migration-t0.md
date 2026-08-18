---
id: task_20260816_codex-migration-t0
assignee: codex
status: queued
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: 迁移建议书会审裁定（2026-08-16 欧阳锋通过）；#328 实证
related: #328
---

# T0 冲突止血验收确认（#342）

## 背景
canonical=user 级已裁定通过（四方一致 + 欧阳锋抽查）。#328 已执行同方案（boot 退役+system 3 退役+user 8/8），本任务 = **验收确认不重跑**。

## 任务（Codex 执行，正式观察记录落盘）
1. **正式 10 分钟观察记录**（洪七公 60 秒零增长 + 10 小时零新增 already-running 可作证据引用，但按标准流程补正式记录）
2. **进程级唯一性**：ps 逐行确认 8 profile 各 1 进程无锁残留（**不单信 pgrep 计数**——欧阳锋实测 pgrep -fc 输出 9 vs ps 8，shell 模式匹配时序差）
3. **XDG_RUNTIME_DIR 前置**：查 user journal 前 `export XDG_RUNTIME_DIR=/run/user/$(id -u)`（洪七公坑，写入运维手册/skill）
4. **linger 常驻项**：wsl.conf systemd=true + linger 检查——写入验收常驻项（防 WSL 升级重置）
5. **PID 1624 用途已确认（codex 核实 2026-08-16）**：= 老顽童 CLI **在用实例**（WSL 默认根模式，无 -p 参数/HERMES_HOME——非 profiles/laowantong）。**不关闭**；迁移时随"老顽童记忆继承"（#344 子项）一并处理

## 验收标准
- system 级 4 unit disabled（文件保留不删——回滚路径）
- user 级 8/8 running + NRestarts 零增长（观察期）
- journal 无新增 Gateway already running + ps 进程唯一性
- 观察记录落盘

## 回滚
system unit 文件保留（disabled），重新 enable 即回滚。

## 执行门禁
⏸ **挂起：等老顽童 CLI 手头工作完成 + 用户命令**（迁移涉及 gateway 停启，不中断生产）


## 挂起条件解除（2026-08-18 王语嫣编排更新）

- 老顽童 CLI 已确认空闲（2026-08-18 老顽童本尊：活跃待命、无在产任务、失忆恢复完成）
- 用户已下令起链（2026-08-18）——本任务可领取执行
