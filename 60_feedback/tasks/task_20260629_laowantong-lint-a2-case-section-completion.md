---
id: task_20260629_laowantong-lint-a2-case-section-completion
type: task
status: pending_review
assignee: 老顽童(Hermes)
priority: P1
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 90_control/.tmp/lint_current.log
- 60_feedback/tasks/task_20260628_laowantong-lint-batch2-case-sections.md
---

# A2：case section 缺失补全（132 文件）

## 目标

修复当前 `kdo lint` 中 case 卡相关的 ERROR，使 case 类 ERROR 彻底清零。

## 当前状态（2026-06-29）

`Case card missing section` ERROR 已为 0，可能已被之前的清理修复。

当前 case 卡实际存在的问题：
- ~100 个 case 卡缺少 `created_at`/`updated_at`
- 5 个 case 卡 frontmatter parse error
- 1 个 case 卡缺少 title/type

## 范围调整

1. 为所有缺少 `created_at`/`updated_at` 的 case 卡补全日期字段（设为文件创建日期或 2026-06-28）
2. 修复 5 个 frontmatter parse error 的 case 卡
3. 修复 1 个缺少 title/type 的 case 卡

## 规则

1. **不删除现有正文**，只修复 frontmatter。
2. 日期字段统一设为 `2026-06-28`（批量修复日期）。
3. frontmatter parse error 需手动检查并修复 YAML 格式。
4. 每张卡改完后跑 `kdo pre-submit -f <路径>`。

## 批量处理门禁

1. 全量处理完成后跑 `git diff --stat`，确认变更文件数。
2. 跑 `kdo lint`，确认 case 相关 ERROR 清零。
3. 批量提交前跑 `kdo pre-submit` 抽检通过。

## 验证

- `kdo lint` 中 case 卡相关 ERROR 清零
- 全库 lint ERROR 显著下降

## 输出

完成后写执行报告：处理文件数、修复类型统计、`kdo lint` 前后 ERROR 数对比。
