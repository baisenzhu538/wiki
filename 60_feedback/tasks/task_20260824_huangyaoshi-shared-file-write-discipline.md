---
id: 505
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T16:40:54.387869+00:00'
version: v0.1
instance: huangyaoshi
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
