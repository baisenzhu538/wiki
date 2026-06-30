---
id: task_20260630_kdo-query-label-filter
title: "实现 kdo query --label 质量标签过滤命令"
type: task
status: queued
assignee: 黄药师
priority: P1
created_at: 2026-06-30
updated_at: 2026-06-30
reviewer: 欧阳锋
source_refs:
  - 60_feedback/tasks/task_20260629_vikki-five-tag-quality-labels.md
related:
  - [[task_20260629_vikki-five-tag-quality-labels]]
  - [[system-kdo-quality-labels]]
  - [[framework-kdo-quality-gate]]
---

# 实现 kdo query --label 质量标签过滤命令

## 背景

#31 `task_20260629_vikki-five-tag-quality-labels` 已完成，全库已有 227 张卡片带有 `quality_labels` 字段。欧阳锋在终审时发现：

> 任务验收标准要求 `kdo query --label actionable` 可过滤，但当前尚未实现，用 `rg` 临时等效替代。

这不算阻塞 #31，但需排期实现，否则质量标签体系的查询入口不完整。

## 目标

为 `kdo query` 命令增加 `--label` 参数，支持按 `frontmatter.quality_labels` 过滤卡片。

## 验收标准

- [ ] `kdo query --label actionable` 返回所有 `quality_labels` 包含 `actionable` 的卡片
- [ ] 支持多个 label：`kdo query --label actionable --label cited`
- [ ] 与现有 `--trust`、`--view`、`--limit` 参数可组合使用
- [ ] `kdo query --label actionable --stats` 显示该 label 下的统计信息
- [ ] 实现 `kdo query --list-labels`（可选），列出所有可用 label 及其卡片数
- [ ] `kdo pre-submit` 相关文件通过
- [ ] 更新 `system-kdo-quality-labels` 使用指南，替换 `rg` 临时方案

## 实现建议

修改文件：`kdo/commands/delivery.py::cmd_query()`

1. 在 argparse 中新增：
   ```python
   p_query.add_argument("--label", action="append", dest="labels",
                        help="Filter cards by quality_labels (can be repeated)")
   ```

2. 在查询流程中，先按 label 过滤 `30_wiki/**/*.md`：
   ```python
   if args.labels:
       matched = []
       for page in all_wiki_pages:
           fm = parse_frontmatter(page)
           labels = set(fm.get("quality_labels", []))
           if labels.issuperset(args.labels):
               matched.append(page)
   ```

3. 如果同时有 `question`，在 label 过滤后的结果上做 LightRAG / 向量检索。

4. 如果只有 `--label` 没有 `question`，直接返回匹配的卡片列表（类似 preset view）。

## 关联任务

- [[task_20260629_vikki-five-tag-quality-labels]]（已 reviewed）
- #35 [[task_20260630_kdo-state-json-sqlite-migration-mvp]]（本周黄药师主责，本任务可并行或紧随其后）
