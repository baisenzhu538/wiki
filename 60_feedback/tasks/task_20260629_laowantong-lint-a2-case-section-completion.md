---
id: task_20260629_laowantong-lint-a2-case-section-completion
type: task
status: queued
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

修复当前 `kdo lint` 中报 `Case card missing section` 的 132 张 case 卡，补齐 4 个标准 section，使 case section 类 ERROR 彻底清零，全库 lint ERROR 归零。

## 范围

- 当前 `kdo lint` 中报 `Case card missing section` 的 132 个文件
- 来源清单：运行 `kdo lint` 后过滤 "Case card missing section" 获得

## 需补齐的 4 个 section

1. `## 关键证据`（Before-After / 真实锚点 / 数据支撑 / 可检验）
2. `## 可迁移场景`（这个案例的经验可以迁移到哪些场景）
3. `## 教训`（什么时候应该学这个案例（正面））
4. `## 失败模式`（常见的踩坑方式和避免方法（反面））

## 规则

1. **读正文优先**：补 section 前先读正文，优先从正文萃取内容填入对应 section。
2. **不删除现有正文**，在合适位置插入缺失 section。
3. **没素材的用 `src_unknown` 占位 + `待补` 标记**，不允许空壳 section。
4. 每个 section 至少写 2-3 条具体内容。
5. 注意 section 标题必须为中文：
   - ❌ Key Evidence / Lessons / Failure Patterns
   - ✅ 关键证据 / 教训 / 失败模式
6. 每张卡改完后跑 `kdo pre-submit -f <路径>`。

## 批量处理门禁

1. 全量处理完成后跑 `git diff --stat`，确认 132 个文件均有变更。
2. 跑 `kdo lint`，确认 `Case card missing section` ERROR 清零。
3. 批量提交前跑 `kdo pre-submit -f <清单> --expect-changes 132` 通过。

## 验证

- `kdo lint` 不再报 `Case card missing section`
- 132 张卡 `kdo pre-submit` 全量通过
- 全库 lint ERROR 从 140 降至 8（仅剩 A1 的 8 个空 source_refs）

## 输出

完成后写执行报告：处理文件数、从正文萃取的 section 数、用 `src_unknown` 占位的 section 数、`kdo lint` 前后 ERROR 数对比。
