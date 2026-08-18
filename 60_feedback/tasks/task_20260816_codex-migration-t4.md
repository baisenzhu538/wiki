---
id: task_20260816_codex-migration-t4
assignee: codex
status: pending_review
priority: P2
wsjf: 1.5
created_at: 2026-08-16
updated_at: '2026-08-18T15:50:46.166996+00:00'
source: 迁移建议书会审裁定（2026-08-16）
related: null
---

# T4 过渡 profile 归档/停用（#346 · P2 停车场）

## 涉及 profile
duan（废弃，#325 确认）/ kimi-test（测试 profile）——**note-coach 保留**（用户确认要用，2026-08-16）

## 任务（等 T0-T3 稳定 + 用户确认后执行）
记录用途与最后活跃时间 → 用户确认不用 → 停用+归档（不删除）→ 观察 7 天 → 再决定真删

## 验收标准
服务 inactive+disabled / 数据归档 hash 完整 / 无其他服务依赖

## 执行门禁
⏸ **挂起：T0-T3 稳定 + 用户确认 + 老顽童 CLI 工作完成**


## 挂起条件解除（2026-08-18 王语嫣编排更新）

- 老顽童 CLI 已确认空闲（2026-08-18 老顽童本尊：活跃待命、无在产任务、失忆恢复完成）
- 用户已下令起链（2026-08-18）——本任务可领取执行

---

## 执行报告（2026-08-18 codex 收尾 · 解冻后）

**三处最终去向已核验**：
- `duan` → 已归档 WSL `~/.hermes/profiles_archive/duan` ✅（未真删）
- `kimi-test` → 已归档 WSL `~/.hermes/profiles_archive/kimi-test` ✅（未真删）
- `note-coach` → 保留于 `.hermes\profiles\note-coach`（旧 Windows 家目录）；未服务化、未迁 AppData\Local、gateway_state 陈旧（06-07）

**状态**：duan/kimi-test 归档完成，可提审；**note-coach 位置/激活状态待明确**（迁 AppData\Local 并激活，还是“保留即归档旧目录”）——需用户/王语嫣拍板。

