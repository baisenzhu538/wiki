---
id: 505
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-24T17:00:15.428811+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- 90_control/scripts/shared_file_guard.py
- 90_control/scripts/tests/test_shared_file_guard.py
- kdo-tools/conveyor_probe.py
- 90_control/file-flow-protocol-amend-shared-file-write.md
reviewed_by: 欧阳锋
review_date: '2026-08-24'
grade: A
---

# #505 共享文件并发写根治（写前核最新编号 + 落盘即 commit + message 标 instance）

- **任务号**：#505
- **状态**：queued
- **assignee**：huangyaoshi（工具化/约定固化；王语嫣编排；欧阳锋终审）
- **优先级**：P1（E050 反向变体一日 3 次复发 + #488 队列行错位实证）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-capsule-audit-08-24.md` F3 裁定采纳）

## 背景

`production-queue.md` 等共享文件多实例并发 add/commit：E050 反向变体 ×3（#484/#485/#486 队列行被并发 commit 带走——共享 git index，add 文件级 + commit 全局，时间窗内被带走）；#488 队列行错位（加到主表外）。根因：共享文件写操作无约定无工具兜底，靠自觉。

## 任务

1. **约定固化**（落 file-flow-protocol 或 queue 操作规范）：共享文件（production-queue.md / parking-lot.md / context.md 等）写操作三条——①写前 grep 最大任务号/核最新 HEAD（防旧快照插入错位）②落盘后**立即 path-scoped commit**（秒级缩窗口）③commit message 标 `by <instance>`
2. **工具化兜底**：评估在 queue_transition / 编排侧加「写前 stale 检测」（git HEAD 落后于远端/上次读则报警）——小改优先，不引新子系统
3. 与 #503/#504（queue_transition 同文件区）无代码冲突前提下实施；若触同函数区则排队错位实施

## 验证（验证分层）

- L1：约定条文落规范文档 + 回归用例（模拟并发 add 同文件场景，检测/报警生效）
- L2 狗粮：本任务单自身落盘即按新约定执行（写前核编号 + 立即 commit + message 标 instance）
- L3 待活体：下一次并发窗口（多实例同写队列）不再出现行被带走/错位

## 边界

- 不改 git 工作流大框架（不引锁服务/不强制 rebase 流程）
- 只治「共享文件并发写」一族；实例隔离（F-048）不在本单
- 规范文档落点由黄药师定（file-flow-protocol 优先），王语嫣不指定工具形态（B1-4）

## 关联

- 风清扬建议书 F3（capsule-audit-08-24）
- E050/E055（错误模式库，王语嫣 08-24 复盘）；E034（行动前核最新态同族）
- #488 队列行错位实证；#390 自动 commit（path-scoped 红线）

## 需要谁动作

- **黄药师**：约定固化 + stale 检测兜底
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：共享文件并发写根治三层落地——①约定固化：三条约定（写前核最新态/落盘即 path-scoped commit/message 标 by instance）以增补件 `90_control/file-flow-protocol-amend-shared-file-write.md` 落规范（原件 v1.0 已冻结，按 §3 增补件路径订立，含 S4 外部监督者）；②工具兜底 A：conveyor_probe 队列文件 3 个写函数（4 个写点）统一套 QueueLock（与 queue_transition 同锁名，装饰器注入零函数体改动）——消除 probe×transition read-modify-write 竞态（probe 读旧版→transition 改状态→probe 写回 = 状态被吞，E050 同族温床）；③工具兜底 B：新建 `shared_file_guard.py`（snapshot/verify，git HEAD+文件 hash 基线比对，STALE 报警退出 1，stdlib 零依赖）——编排侧/手工写共享文件的 stale 检测。评估结论：queue_transition 自身写路径已合规（QueueLock+原子读写+#390 path-scoped commit+by actor message），无需加检测；stale 风险集中在 probe 写点与手工编排两处，均已兜底。

**交付物**：
- `90_control/file-flow-protocol-amend-shared-file-write.md`（三条约定+工具落点+外部监督者，amends: file-flow-protocol）
- `90_control/scripts/shared_file_guard.py`（新：snapshot/verify 两命令）
- `kdo-tools/conveyor_probe.py`（3 写函数套 QueueLock，装饰器注入）
- `90_control/scripts/tests/test_shared_file_guard.py`（新：7 例回归）

**验证**：
- L1：`cd 90_control/scripts && python -m pytest tests/ -q` → **116 passed**（新增 7 例：并发改文件→STALE/HEAD 移动→STALE/零变更→FRESH/unknown fail-open/格式错拒绝/文件被删→STALE + probe 三写函数锁行为验证）；`kdo-tools/tests/test_conveyor_probe.py` 21 passed（既有探针用例零回归）
- L2 狗粮：本任务自身按新约定执行——commit 前 `shared_file_guard.py snapshot+verify production-queue.md` → FRESH（基线 `393e849ab|fe814990ef2705f7`）；交付 commit 走 path-scoped + message 标 by huangyaoshi；狗粮中抓到工具自身 bug 一个（GBK 控制台输出崩溃+全角分隔符被 shell 捕获层破坏 → stdout reconfigure+ASCII 分隔符修复，当场验证）
- L3 待活体：下一次并发窗口（多实例同写队列/探针与流转同刻）不再出现行被带走/错位；probe 每 10 分钟计划任务带锁运行无死锁（QueueLock 300s 自过期兜底）

**边界**：未改 git 工作流大框架（无锁服务/无强制 rebase）；queue_transition 写路径未动（评估已合规）；实例隔离（F-048）不在本单；增补件规范效力以欧阳锋终审为准（原件 §9——老朱拍板若需另行触发，已在增补件 frontmatter 标注 approved_by 待终审）；conveyor_probe 的非队列文件写点（state 文件等）不在共享文件一族，未加锁。

**需要谁动作**：欧阳锋终审本单（增补件规范地位一并裁定）；王语嫣知悉三条约定（编排侧手工写队列前 snapshot/verify 可选但推荐，queue_transition 路径已全自动合规）；全员：手工写共享文件遵循 S2 三条。

## 终审记录

- **结论**：PASS A（2026-08-25 欧阳锋）；**增补件规范地位裁定：批准生效**（approved_by 已落笔欧阳锋，原件 §9 程序完成）
- **通过维度**：版本对齐三问全过（63bebec17 在 HEAD 链 / CLI+计划任务探针磁盘码=运行码 / HEAD 最新）；L1 独立复跑 116 passed（20.85s）+ probe 21 passed 零回归——双套件与报告一致；L2 狗粮我侧独立复现（snapshot→verify FRESH exit=0）
- **溯源要点**：
  1. **约定固化** ✅：增补件 S1 适用文件/S2 三条约定（写前核最新态/落盘即 path-scoped commit/message 标 by instance）/S3 工具落点/S4 外部监督者齐全——三条约定与根因（E050 反向变体/#488 错位）一一对应
  2. **工具兜底 A** ✅：conveyor_probe 3 写函数（4 写点）装饰器注入 QueueLock("production-queue")——与 queue_transition 锁名一致（L513/709/814 实证）；装饰器注入零函数体改动，既有 21 例零回归佐证兼容；写点直读确为 QUEUE_FILE（production-queue.md）
  3. **工具兜底 B** ✅：shared_file_guard.py snapshot/verify 我侧实跑——snapshot 出基线（HEAD|filehash）→ verify FRESH exit=0；7 例回归覆盖并发改文件/HEAD 移动/零变更/fail-open/格式错/文件被删/probe 锁行为
  4. **评估结论核实** ✅：queue_transition 写路径未动——其既有 QueueLock+原子读写+#390 path-scoped commit 合规判断属实（diff 零 touch 该区）
  5. **L2 狗粮副产品** ✅：工具自身 GBK 崩溃 bug 当场抓当场修——狗粮真跑过的证据（非纸面声称）
- **缺陷**：无
- **残余风险**：L3 待活体（下一并发窗口不再行被带走/错位；probe 每 10 分钟带锁运行无死锁——QueueLock 300s 自过期兜底已在）；增补件遵守情况由 S4 抽查机制承接（我终审共享文件任务时查 commit path-scoped+by 署名）
- **存在性核查**：「116+21 passed」→ 双套件独立复跑；「锁名一致」→ 两侧 QueueLock("production-queue") grep 实证；「guard 工具可用」→ 我侧 snapshot/verify 实跑 FRESH；「增补件格式」→ 全文直读（S1-S4 齐）

*欧阳锋 · 2026-08-25 · #505 终审 PASS A + 增补件批准生效*
