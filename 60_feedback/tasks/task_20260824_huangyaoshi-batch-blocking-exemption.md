---
id: 492
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T18:19:05.219966+00:00'
version: v0.1
instance: huangyaoshi
---

# #492 长程分批任务阻塞豁免（batch:true + can_claim 跳过 pending_review）

- **任务号**：#492
- **状态**：queued
- **assignee**：huangyaoshi（改状态机；王语嫣编排；欧阳锋终审）
- **优先级**：P1（老朱 2026-08-24 拍板方案一——#426 长程任务不得阻塞主线）
- **立项**：2026-08-24 王语嫣（老朱拍板 F-050 方案一）

## 背景

#426（739 张 tags 分批治理，P2 长程）每治理一批就提审一次，每次进 pending_review 就阻塞它后面所有主线任务的领取（实证：#469/#470 领不了、#480/#485/#486 靠 --force 跳过）。根因：queue_transition 分不清「批次提审」（验收后恢复 queued）与「整单提审」（终审闭环），两者都进 pending_review、都触发前方阻塞。

## 任务

### 任务 1 · can_claim 跳过 batch 任务（状态机小改）

- 任务单 frontmatter 加 `batch: true` 标记语义：batch 任务 pending_review 期间**不阻塞**前方队列的后续任务领取
- `can_claim` 逻辑：遇到前方 pending_review 任务时，若该任务 frontmatter `batch: true`，则跳过其阻塞（只跳过 batch 任务，非 batch 任务仍正常阻塞）
- 状态机改一处（`can_claim`），不动 claim/complete/release/review 其他语义

### 任务 2 · #426 加 batch:true 标记

- `60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md` frontmatter 加 `batch: true`
- 验证：#426 下一批提审进 pending_review 时，后方主线任务（#487 口喷等）可正常 claim，不被阻塞

## 验证（验证分层）

- L1 单测：can_claim 跳过 batch 任务的 pending_review 阻塞（正测）；非 batch 任务仍阻塞（反测）
- L2 狗粮：#426 加 batch:true 后，下一批提审时后方任务可领取（实测）
- L3 待活体：长程分批任务（#426）全程不再卡主线

## 边界

- **只改 can_claim 一处**，不动队列其他状态机语义（claim/complete/release/review/cancel 不变）
- 只跳过「batch 任务」的阻塞，非 batch 任务（整单终审语义）仍正常阻塞——终审闭环语义不破坏
- batch 任务自身仍需欧阳锋批次验收（验收语义不变，只是不阻塞后方领取）
- 与 F-029（队列等待外部输入态）同族但独立——本单只解 batch 阻塞，F-029 解「等外部输入」阻塞，不合并

## 关联

- F-050（老朱 2026-08-24 拍板方案一）
- #426（tags 治理长程任务，加 batch:true）
- #479（queue_batch_accept 批次验收工具，已保障验收节奏）
- F-029（队列等待外部输入态，同族不合并）

## 需要谁动作

- **黄药师**：can_claim 改 batch 跳过逻辑 + #426 加 batch:true + 单测
- **王语嫣**：编排（本单）
- **欧阳锋**：终审本单
- **老顽童**：#426 下一批治理时验证不被阻塞

## 执行报告（F-034 五字段，complete 前必填）

（黄药师填写）
