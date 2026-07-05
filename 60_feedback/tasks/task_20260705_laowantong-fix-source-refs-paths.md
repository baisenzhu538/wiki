---
id: task_20260705_laowantong-fix-source-refs-paths
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-05
updated_at: '2026-07-05T03:21:08.160720+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-05'
---

# 任务 #107：修复 4 个 source_refs 路径

## 问题

`kdo lint` 报告 4 个 source_refs 指向不存在的文件：

| 卡片 | 错误路径 |
|:---|:---|
| case-yihang-dual-triangle-guoshuai-ai-editorial | `_processed/郭帅·AI编辑部_vlm.md` |
| case-yihang-dual-triangle-kunte-virtual-idol | `_processed/鲲特·虚拟艺人_vlm.md` |
| framework-yihang-dual-triangle-ai-landing-five-steps | `_processed/贝壳找房案例口述_text.md` |
| feishu-docx-pagination-extraction | `60_feedback/audit/synthesis_kdo_infrastructure.md` |

## 修复

查找正确文件路径，更新 source_refs。找不到的用 `pending_archive` 占位。

## 验收

- 4 个 source_refs ERROR 清零
- `kdo lint` 无新增 ERROR
