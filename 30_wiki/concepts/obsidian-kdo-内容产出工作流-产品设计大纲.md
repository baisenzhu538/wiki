---
title: "Obsidian + KDO 内容产出工作流 — 产品设计大纲"
type: "concept"
status: "draft"
source_refs: ["src_20260501_58b6edef"]
created_at: "2026-05-01T05:26:43+00:00"
updated_at: "2026-05-01T05:26:43+00:00"
---

# Obsidian + KDO 内容产出工作流 — 产品设计大纲

## Summary

0 > 日期：2026-05-01 > 文档类型：产品设计大纲 KDO（Knowledge Delivery Orchestrator）是一款面向内容创作者和知识工作者的"画布+流水线"双模态内容生产操作系统。

它以 Obsidian 为自由创作前台，以 KDO 为结构化产出管理后台，两者共享同一本地优先的知识库，形成人机协作的"外挂大脑"。

这一设计的核心假设是：创作需要无序的自由（画布），而产出需要有序的纪律（流水线），现有工具要么偏重前者导致产出效率低下，要么偏重后者压制创作灵性，KDO 首次将两者无缝衔接于同一知识基座之上。

## Source Refs

- `src_20260501_58b6edef` -> `10_raw/sources/src_20260501_58b6edef-obsidian-kdo-内容产出工作流-产品设计大纲.md`

## Reusable Knowledge

- 用户捕获输入时可附加一段判断，说明"为什么这个素材值得进入后续流程"。
- KDO 设置三道质量门禁，按严格程度递进： | 门禁 | 名称 | 类型 | 检查内容 | 失败行为 | 人工介入点 | |-----|------|------|---------|---------|-----------| | Gate 1 | Skeleton Detection | 硬阻断 | Core Thesis 非空、Draft 含实质内容、TODO 比例低于阈值 | 阻断 ship，状态锁定 `draft` | 作者补充后重新触发 | | Gate 2 | Reference Integrity | 警告 | frontmatter 声明的 wiki_refs/source_refs 在正文中被实际引用 | 输出 WARN，不阻断但要求确认 | 编辑阶段修复引用 | | Gate 3 | Simulated Reader | 人工审核 | artifact 经人工阅读（`reviewed_by` 确认）、done 条件满足 | 状态无法推进至 `shipped` | Reviewer 审批或打回 | 三道门禁构成 KDO 的核心质量约束体系。
- 它不仅检查通用的 `source_refs`、`wiki_refs`、`definition_of_done`、`feedback_path`、`TODO placeholders`，还为 content、code、capability 三类产物定义了差异化的质量门禁——code 产物额外检查 `setup/install` 说明，capability 产物检查 `eval` 路径。

## Open Questions

- TODO: What open questions does this source raise?

## Output Opportunities

- Content: article or tutorial
- Code: script or tool
- Capability: workflow or playbook
