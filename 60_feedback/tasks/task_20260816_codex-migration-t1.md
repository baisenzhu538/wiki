---
id: task_20260816_codex-migration-t1
assignee: codex
status: reviewed
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: '2026-08-18T16:46:25.828643+00:00'
source: 迁移建议书会审裁定（2026-08-16）
related: null
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A
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

---

## 执行报告（2026-08-18 codex 收尾 · 解冻后）

**物理交付已核验（刚 re-check，非过时快照）**：
- Windows NSSM 服务三 profile 全部 Running/Automatic：`hermes-gateway-basic-skills-coach` / `hermes-gateway-coaching-leadership-assistant` / `hermes-gateway-meeting-assistant`
- `AppData\Local\hermes\profiles\` 对应三目录齐全
- WSL 侧此三 profile 无残留

**冒烟证据（详见 `agent复盘/codex/迁移链核销记录-2026-08-18.md`）**：
- 08-17 01:03 飞书“在吗？” → 12.2s / 13.6s / 14.3s 应答（43 / 54 / 224 chars）
- gateway.log：Active profile + feishu connected
- kdo MCP：registered 8 tools；session cwd = Desktop\wiki
- 约 19.6h 未重启

**状态**：可提审欧阳锋。


---

## 补审记录（2026-08-19 欧阳锋 · 状态回退异常）

**异常**：2026-08-18 终审 PASS A 后（reviewed_by/review_date 已落盘），任务单 status 与队列状态列在 08-19 00:2x-00:4x 被回退为 pending_review（#342/#346 未受影响）。原因待查（疑为队列维护基于旧快照编辑覆盖）；reviewed_by/review_date 残留证明终审本身有效。

**处置**（补审 SOP）：产物不重验（2026-08-18 O3 全过：#343 三服务 RUNNING/AUTO+目录齐全+冒烟证据；#344 同+Q&A state.db 原文判定答对），重新执行 queue_transition review 修复状态一致性。
