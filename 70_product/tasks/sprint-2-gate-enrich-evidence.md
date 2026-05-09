---
title: "Sprint 2 门禁系统 + Enrich 举证 — 任务清单"
type: task
status: pending
domain:
  - kdo
sprint: 2
source_refs:
  - "30_wiki/systems/sprint-2-gate-enrich-evidence.md"
  - "30_wiki/decisions/kdo-ec-industrialization-migration-proposal.md"
created_at: "2026-05-09"
tags:
  - "#kdo"
  - "#sprint"
---

# Sprint 2 任务清单

> 审批人：欧阳锋 | 执行人：黄药师

## 任务列表

### T1: 新建 `kdo/gate.py` 门禁模块

- [ ] 定义 `GateIssue` dataclass（severity / stage / check_name / message）
- [ ] 实现 `check_gate(root, state, stage)` 函数，返回 `list[GateIssue]`
- [ ] 实现五个阶段的检查规则：ingest / enrich / produce / validate / ship
- [ ] P0 违规标 `severity: "error"`，P1 标 `"warning"`
- [ ] 安装验证：`pip install -e .` 无报错

### T2: 新增 `kdo gate` CLI 命令

- [ ] `kdo/commands/quality.py` 新增 `cmd_gate()` handler
- [ ] `kdo/cli.py` 注册 `gate` 子命令 + `--stage` + `--skip-gate` 参数
- [ ] `--skip-gate <reason>` 写入 state.json + log.md
- [ ] Exit code：有 P0 且无 --skip-gate → 1；否则 0

### T3: Enrich 举证自动记录

- [ ] `cmd_enrich()` enrich 成功后自动生成举证记录
- [ ] 举证文件写入 `60_feedback/enrich-evidence/ev_*.md`
- [ ] 举证内容：wiki_path / method / source_used / changes_summary
- [ ] state.json 的 sources 记录追加 `enrich_evidence_id`

### T4: 验收 — 端到端走通

- [ ] 在 `00_inbox/` 放一个新素材
- [ ] `kdo ingest` → skeleton 创建成功
- [ ] `kdo enrich --llm` → 三步编译完成 + 举证文件生成
- [ ] `kdo gate enrich` → 通过，0 P0 违规
- [ ] `kdo gate enrich --skip-gate "test"` → 越过记录写入
- [ ] `kdo lint` → 保持 0 errors
- [ ] 通知欧阳锋复审
