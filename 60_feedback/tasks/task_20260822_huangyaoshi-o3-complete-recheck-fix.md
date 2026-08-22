---
id: 413
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-22T05:25:23.172339+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A-
---
# #413 O-3 complete 锁内 re-check 修复 + related-asymmetry 清单标注原始链方向

- **任务号**：#413
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P1（R3 主）/ P2（R4 次，可缓不拖主线）
- **立项**：2026-08-22 王语嫣（欧阳锋建议书 `70_product/tasks/proposal-batch-todo-closure-gate-2026-08-22.md` R3+R4，编排复核通过）
- **来源**：#411 三批实证——分批提审无声（REVIEW-PENDING 不登记），审查者靠用户转达才发现

## 任务目标

### R3（主，P1）：修复 queue_transition `complete` 对 queued 任务锁内 re-check 失败（O-3）

- 现状：`complete --force` 对 queued 任务锁内 re-check 必失败 → 状态卡 queued、REVIEW-PENDING 段不登记
- 修复方向（二选一，黄药师定）：①修 complete 路径锁内 re-check；②complete 后强制登记 REVIEW-PENDING 段作为必含动作
- 验收：修复后实测 3 单 complete → REVIEW-PENDING 段必登记；O-3 blocker 关闭
- **联动注意**：本修复是会诊 X-1（传送带探针）的前置——探针读 REVIEW-PENDING 段，段无登记则通知层建在空状态上

### R4（次，P2，可缓）：full-library-rescan `--check related-asymmetry` 输出追加"原始链来源"列

- 输出标注 A→B 中 A 的 related 原文行号，供执行者/审查者快速定位疑链（脏链对称化已 2 次实证：compas/dk-p11）
- 与 #399 工具同仓演进

## 边界

- 不改 queue_transition 状态机语义（queued→claimed→pending_review→reviewed 不变），只修登记/re-check 缺陷
- 排序约束：黄药师单一实例，当前顺序 #412（会诊硬前置）→ #410（在跑）→ #409 → 本单；不因 P1 打断在跑的 #410
- 修流转脚本前跑既有测试（90_control/scripts/tests/），修复后补 O-3 回归用例
- pre-submit + commit 入档（E040）；欧阳锋终审验收 R3（实测 3 单登记）/R4（清单含来源列）

## 执行报告（#413 黄药师 · 2026-08-22）

### R3（P1）：分批提审无声根因修复

**诊断发现**：O-3 本体（complete --force 锁内 re-check）**已在 #363（6dbd1bf3b）修复**——任务单"现状"描述为旧快照（git log 实证 force+queued 条件 08-20 已加）。**真正未修的缺陷**：

- **根因**：`_review_board_update` 幂等判断 `any(tid in l for l in items)` **把已划掉的行也算"已登记"**——分批任务（如 #411）第二次 complete 时，REVIEW-PENDING 段已有该任务划掉行（含 task_id）→ 不再登记 → **提审无声**（审查者靠用户转达才发现）
- **修复**：幂等判断排除划掉行（`tid in l and not l.startswith("- ~~")`）——已划掉的行不算已登记，二次提审重新登记；未划掉的重复登记仍防（幂等保留）
- **回归测试**：`TestReviewBoardBatchReregister.test_batch_reregister_after_strike`——模拟段内有划掉行 + 二次 register → 断言追加一行未划掉的登记（**11 passed**，含新增）

### R4（P2）：related-asymmetry 来源行号列

- `full-library-rescan --check related-asymmetry` 输出追加 A 卡 related 原文行号（`_related_line_no`：frontmatter related 列表内匹配目标的行，文件 1-based）
- 实测：`agent-spec-duanwangye-publisher.md:22 → skills/skill-duanwangye-kdo-pipeline.md`，行号 22 与文件第 22 行引用一致（抽查验证 ✅）；当前 7012 条全部带行号
- 与 #399 工具同仓演进（同一文件）

### 联动价值

本修复是**会诊 X-1（传送带探针）的直接前置**——探针读 REVIEW-PENDING 段，段登记可靠性是通知层的地基；分批任务（如 #411 后续批次）提审不再无声。

- commit：`e4827f90e`（3 files +66/-2，path-scoped）
- 测试：90_control/scripts/tests/ 11 passed

*黄药师 · 2026-08-22*
