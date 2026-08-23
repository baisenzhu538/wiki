---
id: 477
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T12:59:17.587628+00:00'
version: v0.1
instance: huangyaoshi
---
# #477 任务单 doc_id 字段违规处置（模板移除+存量清理，E045 闭环）

- **任务号**：#477
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（编号体系混用，#450 lint 已把门持续报，模板修掉断源——非阻塞但防违规成常态）
- **立项**：2026-08-23 王语嫣（欧阳锋建议书 `diag_20260823_ouyangfeng-task-docid-violation` 裁定采纳方向①）

## 背景（#473 工具实证）

#449 文件流转规范（08-23 13:51 拍板生效）明确「三套编号不混用（E045）：任务单沿用 #队列号；doc_id 只用于建议书/诊断/审查意见书」。但 #450 lint 实证：规范生效后的新任务单普遍在 frontmatter 带 `doc_id: D-YYYYMMDD-NNN`（#463/#464/#471/#472/#473/#476 等 10+ 份）——四件套惯性全加，未按编号空间区分。`agent-spec-zhu-boss.md`（spec 卡）frontmatter 也含 doc_id——spec 卡编号空间=卡片 id，同样违规。

**讽刺自证**：连刚终审的 #476（E051 闭环单）frontmatter 都自带 `doc_id: D-20260823-024`——模板惯性之深，编排者自己都在违规。这正是工具化断源的必要性。

## 任务

### 任务 1 · 模板移除 doc_id（断源）

任务单模板（`90_control/templates/` 下任务单模板若存在，或 queue_transition.py 生成模板）移除 `doc_id` 字段——任务单只用 `id`（队列号）。本单 #477 及之后所有新单以身作则不带 doc_id。

### 任务 2 · 存量清理（机械批，先清单后批量）

1. **先全量扫描出清单**：跑 #450 lint（file-flow-lint）全库扫任务单 frontmatter 带 doc_id 的文件，输出清单（禁手搓正则，用 #450 既有检查器或 yaml.safe_load 结构化解析——E017 族）
2. **dry-run**：副本演练移除 doc_id 字段，diff 验证只动该字段
3. **单卡验证**：先移除 1 份（如 #476），yaml.safe_load 校验 frontmatter 合法 + 队列对账 status 不变
4. **人工审查内容未被破坏**（禁止清单第 8 条）：确认只删 doc_id 行，其余字段/正文不动
5. **批量移除**：确认后批量移除清单内全部任务单 doc_id 字段
6. **spec 卡侧**：`agent-spec-zhu-boss.md` 的 doc_id 移除（spec 卡编号空间=卡片 id，doc_id 违规）

### 任务 3 · 防复发（已就位，本单确认）

#450 lint L9 已上线——任务单带 doc_id 会被持续报（工具已把门）。模板侧修掉即断源。本任务只需确认 lint 规则覆盖任务单+spec 卡两类，无需新增。

## 验证（验证分层）

- L1：单测——doc_id 字段移除后 frontmatter 仍 yaml.safe_load 合法；lint 全扫零 doc_id 任务单残留
- L2 狗粮：副本 dry-run + 单卡验证（#476）diff 只动 doc_id 行
- L3 待活体：批量后跑 #450 lint 全库零 doc_id 任务单报告 + queue_transition status 对账活跃数不变

## 边界

- 只移除 doc_id 字段，不动任务单其他字段/正文/队列行（E046 append-only 同律，禁吞节）
- 不修订规范 #449（口径不变，E045 维持——纠偏非口径变更，不需老朱拍板）
- spec 卡只移除 doc_id，不改卡片内容（spec 卡归 30_wiki 老顽童域，但机械字段移除可黄药师脚本批——老顽童/黄药师分工：黄药师出脚本+清单，若需老顽童确认内容未动则老顽童复核）
- 存量清理前 git tag 快照（E003：批量操作前恢复点）
- commit path-scoped 禁 add -A（E050：共享 git index 捎带）

## 关联

- 欧阳锋建议书 `diag_20260823_ouyangfeng-task-docid-violation`（裁定采纳方向①）
- #449 文件流转规范（doc_id 编号空间）；#450 file-flow-lint（已把门）；#473 lint 遗留收口（L9 全库扫描）
- E045（三套编号不混用）；E017（治理脚本 yaml 解析非正则）；E003（批量快照）；E046（append-only 不吞节）；E050（commit path-scoped）
- 顺序：黄药师单 #479(P1)→#477(P2)→#478(P2)，禁同轮 ≥3 独立单并发领取

## 内容价值判断（#375 处置门禁补充节）

- 本任务为模板修正+机械字段清理：移除 frontmatter doc_id 行，不删任务内容/不动队列行
- 移除前 dry-run + 单卡验证 + 人工审查内容未破坏（禁止清单第 8 条红线）
- PROTOCOL §7 不触发（移除冗余字段非内容删除，归机械清理）

## 需要谁动作

- **黄药师**：模板移除 + 存量扫描清单 + dry-run + 单卡 + 批量移除 + spec 卡 doc_id 移除
- **王语嫣**：编排核验（lint 全扫零残留 + queue_transition 对账）
- **欧阳锋**：终审（抽「只动 doc_id 字段/内容未破坏/对账一致」）
