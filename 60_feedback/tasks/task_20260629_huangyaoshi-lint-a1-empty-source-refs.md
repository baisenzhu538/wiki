---
id: task_20260629_huangyaoshi-lint-a1-empty-source-refs
type: task
status: queued
assignee: 黄药师
priority: P1
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 90_control/.tmp/lint_current.log
---

# A1：空 source_refs 清理（8 文件）

## 目标

修复当前 `kdo lint` 中报 `concept card has empty source_refs` 或 `tool card has empty source_refs` 的 8 张卡片，使 source_refs 类 ERROR 彻底清零。

## 范围

- 当前 `kdo lint` 中标记为 `empty source_refs` 的 8 个文件
- 文件类型：concept / tool 为主
- 来源清单：运行 `kdo lint` 后过滤 "empty source_refs" 获得

## 规则

1. **优先找真实源文件**：在 `10_raw/sources/`、`00_inbox/` 中搜索同名或同 hash 源文件。
2. **找不到的补 `pending_archive:<原路径>` 占位**：不凭空编造。
3. **如果卡片内容确实来自外部 URL**：移入正文 `## Sources` 段落或新增 `external_refs` 字段（如 schema 支持）。
4. 不改动卡片正文内容，只调整 frontmatter 的 `source_refs`。

## 验证

- `kdo lint` 不再报 `empty source_refs` ERROR
- 8 张卡 `kdo pre-submit -f <路径>` 全部通过
- 批量提交前跑 `kdo pre-submit -f <清单> --expect-changes 8` 通过

## 输出

完成后写执行报告：处理文件数、找到真实源文件数、pending_archive 数、URL 处置数。
