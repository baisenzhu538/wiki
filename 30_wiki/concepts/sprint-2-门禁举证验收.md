---
title: "Sprint 2 门禁举证验收"
type: "concept"
status: "draft"
source_refs: ["src_20260510_9e98a292"]
created_at: "2026-05-09T16:49:59+00:00"
updated_at: "2026-05-09T16:49:59+00:00"
---

# Sprint 2 门禁举证验收

## Summary

KDO 管线的 ingest → enrich → gate 三阶段需要端到端验证。

关键设计决策： - 门禁是强警告非硬阻断（P0 exit 1 但有 --skip-gate 覆盖） - 举证是变更摘要非全量 diff（记录 what changed 而非源码 diff） - enrich 出口条件不依赖 status 字段（避免 parse_frontmatter nested YAML bug 误报）

## Source Refs

- `src_20260510_9e98a292` -> `10_raw/sources/src_20260510_9e98a292-sprint-2-门禁举证验收.md`

## Reusable Knowledge

- TODO: Extract stable concepts, claims, decisions, and reusable patterns.

## Open Questions

- TODO: What open questions does this source raise?

## Output Opportunities

- Content:
- Code:
- Capability:
