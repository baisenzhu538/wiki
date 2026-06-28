---
id: task_20260628_laowantong-link-repair-b3-island-cards
type: task
status: queued
assignee: 老顽童
priority: P2
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 70_product/tasks/production-queue.md
- 60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md
---

# B3：孤岛卡片 `kdo link-suggest` 批量推荐

## 目标

对全库 related 为空或全为占位符、但 status 为 enriched/reviewed 的孤岛卡片，使用 `kdo link-suggest` 批量生成相关链接推荐清单，经人工审核后写入。

## 范围

- `related` 为空或全部含 `src_unknown`/`pending_unknown`
- `status` 为 `enriched` 或 `reviewed`
- 预计文件数：50-100 张

## 规则

1. 先用 `kdo link-suggest --batch` 生成推荐清单（候选卡 + 相似度分数）。
2. 老顽童逐张审核推荐结果：
   - 高置信度（≥0.8）且主题相关 → 直接写入
   - 中置信度（0.5-0.8） → 人工判断是否写入
   - 低置信度（<0.5） → 丢弃，改用 `pending_unknown`
3. 每张卡最终 `related` 至少包含 1 个真实 wikilink；无法确定时保留 `pending_unknown`。
4. 不因为凑数量而引入无关链接。

## 执行方式

- **半自动**：`kdo link-suggest` 批量生成 + 老顽童人工审核写入
- 每张卡改完后跑 `kdo pre-submit -f <路径>`
- 批量提交前跑 `kdo pre-submit -f <清单> --expect-changes <数量>`

## 验证

- 孤岛卡片数量减少 ≥80%
- `kdo lint` 不再报 related 为空的相关 WARNING
- `kdo pre-submit` 全量通过
- 欧阳锋抽查 10 张
