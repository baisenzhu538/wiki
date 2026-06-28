---
id: task_20260628_laowantong-lint-batch2-case-sections
type: task
status: queued
assignee: WorkBuddy 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 90_control/.tmp/lint_20260628_1620.log
- 90_control/.tmp/lint_batch2_case_section.json
---

# lint Batch 2-A：case 卡 section 标准化（130 文件）

## 目标

补齐 130 张 case 卡缺失的标准 section，使 `kdo lint` 不再报 `Case card missing section` 类 ERROR。

## 范围

需补齐以下 4 个 section（文件清单见 `90_control/.tmp/lint_batch2_case_section.json`）：

- `## 关键证据`（Before-After / 真实锚点 / 数据支撑 / 可检验）
- `## 可迁移场景`（这个案例的经验可以迁移到哪些场景）
- `## 教训`（什么时候应该学这个案例（正面））
- `## 失败模式`（常见的踩坑方式和避免方法（反面））

预计影响文件：**约 130 张 case 卡**，其中 91 张四 section 全缺，其余缺 1-3 个 section。

## 规则

1. **只补 section 标题和基本骨架**，内容由素材支撑；没有素材的用 `src_unknown` 占位 + 待补标记。
2. **不删除现有正文**，在合适位置插入缺失 section。
3. 每个 section 至少写 2-3 条具体内容，不写空壳。
4. 每张卡改完后跑 `kdo pre-submit -f <路径>`，确保无新增 frontmatter/链接错误。

## 验证

- 全部 130 张卡 `kdo lint` 不再报 `Case card missing section`。
- 每张卡 `kdo pre-submit` 通过。

## 输出

完成后在本任务单末尾写执行报告：处理文件数、新增 section 数、pre-submit 通过率、残余问题。
