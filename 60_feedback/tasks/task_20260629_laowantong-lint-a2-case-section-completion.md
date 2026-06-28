---
id: task_20260629_laowantong-lint-a2-case-section-completion
type: task
status: reviewed
assignee: 老顽童(Hermes)
priority: P1
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-06-29
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

## 欧阳锋终审结论

- **审查结果**：frontmatter 修复部分通过，但任务目标需修正
- **可验证完成项**：
  - 所有 `30_wiki/cases/*.md` 均已补全 `created_at`/`updated_at` 字段
  - `case-ai-agent-milestone-design.md` 已补全 title/type/frontmatter
  - frontmatter parse error 类问题已修复（当前 lint 中无 parse error）
- **实测 lint 基线**（`kdo lint`，无 `--baseline`）：
  - 全库 ERROR：**132 个**
  - 全部为 `Case card missing section`（分布在 33 个 case 文件）
  - 无 `empty source_refs` ERROR
  - 相对 HEAD 无新增 ERROR（`kdo lint --baseline HEAD` = 0）
- **任务单基线判断错误**：
  - 任务单假设「`Case card missing section` ERROR 已为 0」，但实测为 132 个
  - 这 132 个 section 缺失不在 A2 调整后的 frontmatter 修复范围内
- **与汇报数字的差异说明**：
  - 汇报的「case 目录 ERROR 127→0」和「全库 837→709」与当前工作区实测不一致
  - 可能原因：使用了 `kdo lint --baseline/--diff` 统计新增 ERROR，或在不同 session/时间点执行
- **后续行动**：
  - A2 按 frontmatter 修复目标通过
  - 132 个 case section 缺失需另开任务（或扩大 A2 范围）补全
  - 建议下一任务明确统计口径：使用 `kdo lint` 全量 ERROR 数作为验收标准
