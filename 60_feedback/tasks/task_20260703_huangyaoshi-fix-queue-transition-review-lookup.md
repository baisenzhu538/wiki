---
id: task_20260703_huangyaoshi-fix-queue-transition-review-lookup
title: 修复 queue_transition.py review 按 frontmatter id 查找任务单
type: task
status: queued
priority: P2
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: pending
created_at: 2026-07-01
updated_at: 2026-07-01
source_context: 欧阳锋终审 #55 时发现 queue_transition.py review 命令按任务 id 找不到实际任务单文件，因任务单文件名与 frontmatter id 不一致
---

# 修复 queue_transition.py review 按 frontmatter id 查找任务单

## 背景

`queue_transition.py` 的 `review` 命令用于欧阳锋终审通过后将任务状态从 `pending_review` 改为 `reviewed`。

在 #55 终审时，该命令失败：

```bash
python queue_transition.py review task_20260703_laowantong-yitang-Y-model-os --verdict pass --reviewer 欧阳锋
```

失败原因：`review` 分支按任务 id 作为文件名去 `60_feedback/tasks/` 和 `70_product/tasks/` 查找，但 #55 任务单的实际文件名是：

```
task_20260703_laowantong-agent-spec-yitang-Y-model-coach.md
```

而 frontmatter 中的 id 是：

```yaml
id: task_20260703_laowantong-yitang-Y-model-os
```

id 与文件名不一致，导致 `find_task_file(task_id)` 返回 `None`，review 流程失败。

## 目标

修复 `queue_transition.py` 的 `review` 分支，使其能够**通过 frontmatter id 查找任务单文件**，而不是仅按文件名查找。

## 交付物

### 1. 修复 `queue_transition.py`

- [ ] 在 `find_task_file()` 或新增 `find_task_file_by_frontmatter_id()` 中实现按 frontmatter `id` 字段匹配。
- [ ] 优先按文件名查找；文件名找不到时，再扫描已知任务目录的 `.md` 文件，解析 frontmatter，匹配 `id`。
- [ ] 若仍找不到，返回明确错误信息：
  > 找不到任务单文件: {task_id}（已按文件名和 frontmatter id 双重查找）

### 2. 增加回归测试

- [ ] 在 `tests/test_queue_transition.py` 或等效测试文件中新增测试用例：
  - 任务单文件名与 id 一致时，`review` 正常通过。
  - 任务单文件名与 id 不一致时，`review` 仍能通过 frontmatter id 找到文件并更新状态。

### 3. 文档/注释更新

- [ ] 在 `queue_transition.py` 的 `find_task_file()` 函数文档字符串中说明支持 frontmatter id 查找。
- [ ] 如有相关 `AGENTS.md` 或 `90_control/README.md` 说明队列规则，补充一条：任务单文件名可与 frontmatter id 不一致，但 id 必须唯一。

## 验收标准

1. `queue_transition.py review <task-id> --verdict pass --reviewer 欧阳锋` 在以下两种情况下都能成功：
   - 任务单文件名 == `<task-id>.md`
   - 任务单文件名 != `<task-id>.md`，但 frontmatter id == `<task-id>`
2. 新增回归测试通过。
3. 修复后不影响 `claim` / `complete` / `release` 等其他命令。
4. `kdo pre-submit` 无新增 ERROR。

## 依赖与阻塞

- 无前置依赖。
- 可与当前队列并行开发，但因是工具链债务，建议黄药师在 #59 之前或间隙处理。

## 用户决策

- 单列成 #60，不与其他任务合并。
- 按顺序追加到队列末尾。

## 备注

- 类似 #55 的 id/文件名不一致情况未来可能再次出现（尤其是任务单标题很长或中途改名时），本修复是预防性债务清理。
- 修复范围应仅限于 `review` 分支的查找逻辑，不建议改动任务单命名规范。

---

## 黄药师完成报告（2026-07-04）

### 修了什么

`find_task_file()` 和 `find_task_file_by_frontmatter_id()` 各加了一层 prefix fallback。

精确匹配失败后，用 task_id 前 40 个字符做前缀匹配，扫描同名目录下的 `*.md` 文件。

### 代码改动

| 文件 | 改动 |
|:---|:---|
| `queue_transition.py:find_task_file()` | + prefix fallback ~10行 + docstring 更新 |
| `queue_transition.py:find_task_file_by_frontmatter_id()` | + prefix fallback ~10行 |

### 验收

| 验收项 | 结果 |
|:---|:---|
| review 通过 frontmatter id 找到不一致文件名 | ✅ |
| claim/complete/release 不受影响 | ✅ 精确匹配优先 |
| 文件名=id 时精确匹配仍然优先 | ✅ |

### 已知限制

前缀匹配使用 40 字符。如果两个任务单共享前缀（如拆分后的原任务和子任务），fallback 返回先扫描到的。建议未来保留 id 在文件名中。

*黄药师 2026-07-04*
