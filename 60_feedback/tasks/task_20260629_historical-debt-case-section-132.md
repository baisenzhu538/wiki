---
id: task_20260629_historical-debt-case-section-132
type: task
status: claimed-kimi
assignee: 老顽童(Kimi)
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

## 当前状态

- 已从停车场移出，进入活跃生产队列
- 认领人：老顽童(Kimi)
- 处理方式：批量补全缺失的 case 标准 section

## 问题定位（2026-06-29）

缺失 section 类型统计：

| 缺失 section | 出现次数 |
|:---|:---:|
| `## 关键证据` | ~43 |
| `## 可迁移场景` | ~43 |
| `## 教训` | ~43 |
| `## 失败模式` | ~43 |

涉及文件清单（43 个）：

```
30_wiki/cases/case-ai-time-management-tiered-growth.md
30_wiki/cases/case-ban-fei-mao-conversion-hacker-skill.md
30_wiki/cases/case-ban-fei-mao-skill-ab-test.md
30_wiki/cases/case-coffee-shop-foresight.md
30_wiki/cases/case-escort-service-tiered-growth.md
30_wiki/cases/case-ether-online-acquisition.md
30_wiki/cases/case-five-step-fake-vs-real-barriers.md
30_wiki/cases/case-five-step-growth-first-lever.md
30_wiki/cases/case-guang-leng-dian-zi-hx-smj.md
30_wiki/cases/case-ji-hao-ai-workspace-chaos.md
30_wiki/cases/case-ji-hao-ui-design-constraint-evolution.md
30_wiki/cases/case-livestream-sop-modeling.md
30_wiki/cases/case-modeling-abstraction-yitang-models.md
30_wiki/cases/case-modeling-essence-schools.md
30_wiki/cases/case-modeling-process-livestream-roles.md
30_wiki/cases/case-modeling-process-sop-evolution.md
30_wiki/cases/case-modeling-process-sop-examples.md
30_wiki/cases/case-personal-map-modeling.md
30_wiki/cases/case-smart-medicine-cabinet-failure-patterns-library.md
30_wiki/cases/case-strategy-m-brand-profit-model.md
30_wiki/cases/case-strategy-model-selection-quiz.md
30_wiki/cases/case-strategy-retailer-activity-scope.md
30_wiki/cases/case-strategy-revival-13-bestore.md
30_wiki/cases/case-strategy-revival-14-gucci.md
30_wiki/cases/case-strategy-snack-business-design.md
30_wiki/cases/case-strategy-snack-industry-chain.md
30_wiki/cases/case-strategy-walmart-vs-costco-pyramid.md
30_wiki/cases/case-toy-cabinet-barrier.md
30_wiki/cases/case-toy-cabinet-business-model.md
30_wiki/cases/case-truman-ai-partner.md
30_wiki/cases/case-truman-ai-skill-engineering-guide.md
30_wiki/cases/case-truman-ai-skill-self-packaging.md
30_wiki/cases/case-truman-livestream-sop-iteration.md
30_wiki/cases/case-truman-motivation-map-12-versions.md
30_wiki/cases/case-truman-personal-growth-map-creation.md
30_wiki/cases/case-truman-poker-deck-roi.md
30_wiki/cases/case-truman-prd-checklist-evolution.md
30_wiki/cases/case-truman-sales-report-structure.md
30_wiki/cases/case-yitang-double-triangle-confidence.md
30_wiki/cases/case-yitang-model-asset-inventory.md
30_wiki/cases/case-yitang-radar-chart-selection.md
30_wiki/cases/case-yitang-weekly-modeling-engine.md
30_wiki/cases/case-zhihu-vs-degetao-network-effect.md
```

## 处理规则

1. **不删除现有正文**，只补全缺失 section。
2. **section 标题必须与 lint 要求完全一致**：
   - `## 关键证据`
   - `## 可迁移场景`
   - `## 教训`
   - `## 失败模式`
3. **内容暂用 src_unknown 占位**，符合历史批量修复惯例。
4. **插入位置**：在 Lessons/Case Details 之后、Synthesis/Sources 之前统一追加。
5. **每个文件改完后跑 `kdo pre-submit -f <路径>` 抽检**。
6. **批量完成后跑 `kdo lint`，确认 Case section ERROR 清零**。

## 验证

- `kdo lint` 中不再包含 `Case card missing section`
- 全库 lint ERROR 显著下降

## 输出

执行报告：处理文件数、修复 section 类型统计、`kdo lint` 前后 ERROR 数对比。

---

> 本任务已由用户批准从停车场移出，立即执行。
