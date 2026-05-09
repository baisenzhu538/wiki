---
title: "Sprint 2 门禁举证验收"
type: concept
topic: kdo
target_user: developer
created_at: "2026-05-10"
---

# Sprint 2 门禁举证验收

KDO 管线的 ingest → enrich → gate 三阶段需要端到端验证。

关键设计决策：
- 门禁是强警告非硬阻断（P0 exit 1 但有 --skip-gate 覆盖）
- 举证是变更摘要非全量 diff（记录 what changed 而非源码 diff）
- enrich 出口条件不依赖 status 字段（避免 parse_frontmatter nested YAML bug 误报）
