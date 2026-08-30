---
id: 580
assignee: huangyaoshi
status: in_progress
type: infra
priority: P3
created: 2026-08-30
source: 老顽童 08-30 返工
instance: huangyaoshi
updated_at: '2026-08-30T14:19:59.923587+00:00'
---

# #580 返工重提绕过 #504 拦截的状态机改进（F-064）

## 背景

08-30 老顽童返工 #578（终审 FAIL 后重提）时，claim 被 #504「审查等待期不接新单」拦截——名下有 pending_review 任务（#575/#578/#579）时无法领返工单，只能 `--force` 绕过（已留痕 force-exceptions.log）。同批 #577 返工（黄药师）同撞。返工重提≠接新单，#504 误拦了返工通道。

## 任务

改 `90_control/scripts/queue_transition.py` 的 can_claim 逻辑：

1. **区分「返工重提」与「接新单」**：任务单 frontmatter 或队列行带 `rework: true`（终审 FAIL 打回时自动打标）→ claim 时不触发 #504 pending_review 阻塞
2. **非 rework 单维持 #504 原语义**：审查等待期不接新单照旧
3. force-exceptions.log 机制保留（rework 通道不需要 force 了，但其他例外仍走留痕）

## 验证

- 模拟场景：assignee 名下有 pending_review + 一张 rework:true 单 → 可直接 claim（无 force）
- 模拟场景：assignee 名下有 pending_review + 普通新单 → 仍被 #504 拦截
- 既有测试套件通过（`90_control/scripts/tests/`）

## 边界

- 只改 can_claim 一处判断 + FAIL 打回时打 rework 标记（queue_transition 的 review/complete 分支）
- 不动 #504 本身的其他拦截场景
- 改完自查 notification-coverage-matrix：若 queue_transition.py 被触碰，按 §3.19 同改矩阵或标 `matrix_exempt: true` 并注明理由

## 关联

- 停车场 F-064
- #504（原 #504 拦截语义）
- force-exceptions.log（临时方案，本单落地后 rework 场景不再需要 force）
