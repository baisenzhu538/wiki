---
title: "Sprint 2 门禁举证验收"
type: "concept"
status: "enriched"
source_refs: ["src_20260510_9e98a292"]
created_at: "2026-05-09T16:49:59+00:00"
updated_at: "2026-05-09T16:51:19+00:00"
---


# Sprint 2 门禁举证验收

## Summary

KDO 管线的 ingest → enrich → gate 三阶段需要端到端验证。

关键设计决策： - 门禁是强警告非硬阻断（P0 exit 1 但有 --skip-gate 覆盖） - 举证是变更摘要非全量 diff（记录 what changed 而非源码 diff） - enrich 出口条件不依赖 status 字段（避免 parse_frontmatter nested YAML bug 误报）

## Source Refs

- `src_20260510_9e98a292` -> `10_raw/sources/src_20260510_9e98a292-sprint-2-门禁举证验收.md`

## Reusable Knowledge

- KDO 管线采用 ingest → enrich → gate 三阶段，需要端到端验证以确保整体流程正确。
- 门禁（gate）设计为强警告而非硬阻断，P0 时以 exit 1 退出但允许通过 --skip-gate 参数覆盖继续执行。
- 举证（evidence）应记录变更摘要（what changed），而非全量源码 diff，以聚焦影响而非细节。
- enrich 阶段的出口条件不应依赖 frontmatter 中的 status 字段，以避免 parse_frontmatter 处理嵌套 YAML 时的 bug 导致误报。
- 多阶段管线中每个阶段的出口条件需独立设计，并针对已知解析缺陷进行容错设计。

## Open Questions

- 门禁的“强警告”与“P0 exit 1”的触发条件是否明确定义？是否有可操作的严重性分级标准来区分警告与阻断场景？
- --skip-gate 覆盖机制是否会生成审计日志或证据记录？如何防止该选项被滥用或误用后无法追溯？
- 举证以变更摘要代替全量 diff，如何确保摘要生成逻辑完整覆盖所有影响范围？是否会遗漏隐式副作用（如全局变量修改、配置漂移）？
- enrich 阶段避开 frontmatter 的 status 字段后，采用哪些具体字段或逻辑作为出口条件？这些替代方案对边缘情况的处理是否经过系统测试？
- parse_frontmatter 的嵌套 YAML 解析 bug 是否已有修复计划或临时缓解措施？该缺陷是否会影响管线的其他 YAML 相关操作？
- 端到端验证的测试用例是否覆盖了各阶段的部分失败、重试、数据残留等异常路径？预期行为的验收标准是否文档化？
- 当门禁以 exit 1 退出但通过 --skip-gate 继续时，后续阶段和最终产物中如何标记该次执行的状态（例如“带警告通过”），以便合规审查？

## Output Opportunities

- Content: analysis
- Code: script
- Capability: workflow
