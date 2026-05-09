---
title: "门禁举证端到端验收测试"
type: concept
topic: kdo
target_user: developer
created_at: "2026-05-10"
---

# 门禁举证端到端验收测试

这是一个用于验证 Sprint 2 全链路（ingest → enrich → gate）的临时测试素材。

## 背景

KDO 目前完成了两个 Sprint：
- Sprint 1：建立了 ingest + enrich + lint 基础管线
- Sprint 2：增加了 gate 门禁系统 + enrich 举证自动记录

三条核心管道命令：
- `kdo ingest` — 将 inbox 素材摄入为 wiki skeleton
- `kdo enrich --llm` — 三步编译填充知识卡片
- `kdo gate enrich` — 检查 enrich 阶段出口条件

每个 enrich 完成后自动生成举证记录到 `60_feedback/enrich-evidence/ev_*.md`。
