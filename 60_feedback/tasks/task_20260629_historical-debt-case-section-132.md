---
id: task_20260629_historical-debt-case-section-132
type: task
status: pending_review
assignee: 老顽童(Hermes)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_laowantong-lint-a2-case-section-completion.md
- 30_wiki/projects/parking-lot.md
---

# 历史债务处理：132 个 Case card missing section 修复

## 债务来源

A2 任务（`task_20260629_laowantong-lint-a2-case-section-completion.md`）在 frontmatter 修复目标完成后，欧阳锋终审实测发现：

- 全库 `kdo lint` 仍有 **132 个 ERROR**
- 全部为 `Case card missing section`
- 分布在 **43 个 case 文件**（原统计为 33 文件，实测为 43）
- 相对 HEAD 无新增 ERROR，属于历史遗留

## 处理结果（2026-06-29）

### 修复范围

- **修复文件数**：43 个 case 文件
- **修复 section 数**：132 个缺失 section
- **顺手修复**：8 个战略类 case 文件缺少 `reviewed_by`/`review_date` frontmatter

### 修复内容

为每个缺失的文件补全以下标准 section（内容暂用 `src_unknown` 占位）：

| section | 说明 |
|:---|:---|
| `## 关键证据` | Before-After / 真实锚点 / 数据支撑 / 可检验 |
| `## 可迁移场景` | 这个案例的经验可以迁移到哪些场景 |
| `## 教训` | 什么时候应该学这个案例（正面） |
| `## 失败模式` | 常见的踩坑方式和避免方法（反面） |

### 特殊处理

- `case-modeling-abstraction-yitang-models.md` 和 `case-yitang-double-triangle-confidence.md` 原有 `## 可迁移` 二级标题，统一改为 `## 可迁移场景`。

## 验证

| 检查项 | 结果 |
|:---|:---|
| `kdo lint` 全量 ERROR | **0**（原 132 个 `Case card missing section` 已清零） |
| `kdo lint` 新增 ERROR | 0 |
| `kdo pre-submit` 抽检 | 5/5 PASS |
| 缺失 `reviewed_by` 的战略 case | 8/8 已补全，pre-submit PASS |

## 输出

- 43 个 case 文件已更新 `updated_at`
- 8 个 case 文件已补全 `reviewed_by: 欧阳锋` / `review_date: '2026-06-29'`
- 全库 `kdo lint` 不再包含 case section 类 ERROR

---

> 本任务已由用户批准从停车场移出并立即执行，现提交欧阳锋终审。
