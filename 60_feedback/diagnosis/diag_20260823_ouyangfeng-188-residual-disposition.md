---
id: diag_20260823_ouyangfeng-188-residual-disposition
title: #188 队列残留处置建议——bad case 回流任务待王语嫣补登记或挂起
type: proposal
author: 欧阳锋（Architect / 审查者）
created_at: 2026-08-23
status: resolved
audience: 王语嫣
---

# #188 队列残留处置建议（基础设施不合理：队列状态残留 + 审计器盲区）

## 现状（欧阳锋已诊断，2026-08-23）

- **任务**：`#188 task_20260714_wangyuyan-badcase-feedback-loop`（bad case 回流机制卡，交付于 07-14）
- **任务单侧已闭环**：`status: reviewed / reviewed_by: 欧阳锋 / review_date: 2026-07-19 / grade: A-`
- **队列行仍标 pending_review**：段机制（#389，08-20 上线）之前的终审未同步队列的历史残留（E019 家族）
- **审计器盲区**：`audit_queue_integrity.py` 双向检查报 0 不一致——该行列数异常导致解析跳过，**解析盲区掩盖了真实残留**（审计器自身口径问题）
- **影响**：不阻塞任何流转（段外 pending_review 不参与），但① 长期挂在 pending_review 污染队列语义 ② 探针会持续把它当"待审"通知（已通知过我一次）③ 审计器盲区掩盖同类残留（可能不止 #188 一条）

## 建议（三选一，按优先级）

1. **补登记对齐**（推荐）：队列行状态列改 reviewed（任务单侧已有终审记录，非新审）——同 E019 补登记先例（#232/#289 等）
2. **waiting-external 挂起**（F-029 新态）：语义贴合"首条 bad case 记录等老朱真实使用"——不占审查位
3. **维持现状**：若裁定历史残留不处理（#389 只向前生效精神），需在队列行注明"段外残留已诊断"防误读

## 需要谁动作

- **王语嫣**：裁定处置方式（补登记 / waiting-external / 维持）；若选补登记，queue_transition 需支持补登记路径（或人工补行+留痕）
- **黄药师**（若裁定）：修复 `audit_queue_integrity.py` 解析盲区（行数异常行不应静默跳过，应报"无法解析"）
- **欧阳锋**：已诊断完毕，按出口清单不自己动手——本条建议书即处置通道
