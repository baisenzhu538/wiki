---
id: task_20260816_codex-migration-t1
assignee: codex
status: queued
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: 迁移建议书会审裁定（2026-08-16）
related: #342
---

# T1 三个最慢组合迁 Windows 原生（#343）

## 涉及 profile
basic-skills-coach / coaching-leadership-assistant / meeting-assistant（WSL 运行+Windows profile 最差组合，/mnt/c 27x 实测瓶颈）

## 任务（Codex 执行 + 黄药师验证，每 profile 独立不并行）
预检 Windows profile 完整性 → 备份（WSL unit + Windows profile hash）→ 停 WSL user 服务 → 验证旧侧无进程无锁 → **Windows 侧 NSSM 服务化**（直接 NSSM/WinSW，不用 Task Scheduler——#328 教训：Restart=always 是保命配置）→ 启动 → 冒烟（版本识别+kdo query+读 wiki 文件）→ 观察 15 分钟 → 验收/回滚

## 验收标准
- WSL 侧 inactive/disabled；Windows 侧稳定无崩溃
- 冒烟输出与迁移前一致；15 分钟无 restart 无 lock
- 任务耗时较 WSL 明显下降

## 回滚
停 Windows → 恢复 WSL user 服务 → 验证 PID/锁/NRestarts 恢复

## 执行门禁
⏸ **挂起：等老顽童 CLI 手头工作完成 + 用户命令**


## 挂起条件解除（2026-08-18 王语嫣编排更新）

- 老顽童 CLI 已确认空闲（2026-08-18 老顽童本尊：活跃待命、无在产任务、失忆恢复完成）
- 用户已下令起链（2026-08-18）——本任务可领取执行
