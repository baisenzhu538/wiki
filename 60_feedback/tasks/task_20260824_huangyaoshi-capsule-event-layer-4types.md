---
id: 511
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T18:23:07.350637+00:00'
version: v0.1
instance: huangyaoshi
---

# #511 记忆胶囊事件层补 4 类关键事件（queue_transition / decision / friction / error）

- **任务号**：#511
- **状态**：queued
- **assignee**：huangyaoshi（事件层扩展；欧阳锋终审）
- **优先级**：P2（排在 #505-#510 后；不压当前基建线）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-capsule-audit-08-24.md` F1 裁定采纳）

## 背景

`activity_log.db` 16 条事件**全部是 `review_saved`（复盘登记簿）**——无 queue_transition / decision / friction / error 事件。影响：靠「提取记忆胶囊」只能还原「谁落了复盘」，不能还原「谁领单/提审/拍板/踩坑」；真正的全量上下文在 L1-full 原文，但事件索引缺工作流语义。F-041 已留「L0 后续扩 event_type=judgment/decision/insight」的演进钩子，本单是其落地。

## 任务

1. 事件层补 4 类关键事件写入：
   - `queue_transition`：claim/complete/review 流转时落事件（挂 queue_transition 写入点，复用 #434 自动写入端模式）
   - `decision`：终审结论/拍板记录落事件
   - `friction`：friction-log 新增行落事件
   - `error`：gate-blocked / force-exceptions 落事件
2. 失败可见不静默（沿用 #434 口径）；单写入面（每类事件一个写入点，不多头写）
3. 幂等：重跑/重试不产生重复事件

## 验证（验证分层）

- L1：构造四类动作各一次，activity_log 出现对应事件类型
- L2 狗粮：一次真实 claim→complete→review 链，事件层可还原全过程
- L3 待活体：风清扬每日审计（#507 digest）只读事件层即可还原「谁领单/提审/拍板/踩坑」

## 边界

- 只做事件层补充，不改 L1-full 采集；不动 review_saved 既有写入
- 不回填历史事件（只向前生效，同 #389 口径）
- 与 #507 digest 衔接：digest 抽数源不变，事件层丰富了其原料

## 关联

- 风清扬建议书 F1（capsule-audit-08-24，含「事件层太薄」实测）
- F-041（判断落盘锚点，L0 事件类型扩展钩子）/ #434（L0 自动写入端）/ #432（记忆胶囊 L0）
- #507（每日 digest 消费端）

## 需要谁动作

- **黄药师**：四类事件写入点
- **欧阳锋**：终审本单
