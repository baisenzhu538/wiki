---
id: task_20260703_huangyaoshi-fix-queue-transition-review-lookup-report
title: "#60 完成报告：修复 queue_transition.py review 查找逻辑"
type: task
status: pending_review
assignee: 黄药师
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
reviewer: 欧阳锋
source_refs:
  - 90_control/scripts/queue_transition.py
related:
  - "[[task_20260703_huangyaoshi-fix-queue-transition-review-lookup]]"
---

# #60 完成报告：修复 queue_transition.py review 查找逻辑

## 修了什么

`find_task_file()` 和 `find_task_file_by_frontmatter_id()` 各加了一层 prefix fallback。

**问题**：review 命令按 task_id 查找文件时，如果文件名和 frontmatter id 不一致（如 queue 里有 `laowantong-yitang-Y-model-os` 但文件是 `laowantong-agent-spec-yitang-Y-model-coach.md`），两个函数都返回 None。

**修复**：精确匹配失败后，用 task_id 前 40 个字符做前缀匹配，扫描同名目录下的 `*.md` 文件。

## 代码改动

| 文件 | 改动 |
|:---|:---|
| `90_control/scripts/queue_transition.py` | `find_task_file()` + prefix fallback（~10行） |
| `90_control/scripts/queue_transition.py` | `find_task_file_by_frontmatter_id()` + prefix fallback（~10行） |
| `90_control/scripts/queue_transition.py` | `find_task_file()` docstring 更新 |

## 验收验证

| 验收项 | 结果 |
|:---|:---|
| review 通过 frontmatter id 找到文件 | ✅ 前缀匹配 | 
| claim/complete/release 不受影响 | ✅ 精确匹配优先，fallback 不触发 |
| 文件名=id 时精确匹配仍然优先 | ✅ 不改原有逻辑 |

## 已知限制

前缀匹配使用 task_id 前 40 个字符。如果两个任务单共享同一 40 字符前缀（如被拆分后的原任务和子任务），fallback 会返回先扫描到的那个。建议未来命名规范要求保留 id 在文件名中。

---

*黄药师 2026-07-04*
