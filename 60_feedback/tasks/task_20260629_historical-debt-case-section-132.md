---
id: task_20260629_historical-debt-case-section-132
type: task
status: parked
assignee: 待定
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_laowantong-lint-a2-case-section-completion.md
- 30_wiki/projects/parking-lot.md
---

# 历史债务：132 个 Case card missing section 修复

## 债务来源

A2 任务（`task_20260629_laowantong-lint-a2-case-section-completion.md`）在 frontmatter 修复目标完成后，欧阳锋终审实测发现：

- 全库 `kdo lint` 仍有 **132 个 ERROR**
- 全部为 `Case card missing section`
- 分布在 **33 个 case 文件**
- 相对 HEAD 无新增 ERROR，属于历史遗留

## 当前状态

- 不阻塞任何 pending_review 任务
- 不影响新卡生产
- 属于可延后处理的历史债务

## 处理方案（待定）

| 方案 | 说明 | 预估工作量 |
|:---|:---|:---:|
| 方案 A：批量补 section | 为 33 个 case 文件补全标准 section | 1-2 天 |
| 方案 B：重新设计 case 卡规范 | 如果规范要调整，可借机统一 | 3-5 天 |
| 方案 C：暂不处理 | 作为已知历史债务，等新卡生产稳定后再处理 | - |

## 验收标准

- `kdo lint` 全量 ERROR 中不再包含 `Case card missing section`
- 修改后的文件 `kdo pre-submit` 通过

## 关联任务

- 前置：A2 frontmatter 修复（已完成 reviewed → done）
- 后续：由用户决定是否入队生产

---

> 本任务为**历史债务记录**，当前状态 `parked`，已转入停车场清单 `30_wiki/projects/parking-lot.md`（PL-013），不进入活跃生产队列。用户可随时决定启动。
