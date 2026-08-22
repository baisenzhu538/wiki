---
id: 413
assignee: huangyaoshi
status: queued
updated_at: '2026-08-22T13:10:00+08:00'
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
