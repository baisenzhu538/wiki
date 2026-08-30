---
id: 580
assignee: huangyaoshi
status: pending_review
type: infra
priority: P3
created: 2026-08-30
source: 老顽童 08-30 返工
matrix_exempt: true
instance: huangyaoshi
updated_at: '2026-08-30T14:30:48.598583+00:00'
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

## 执行报告

**交付物**：
- `90_control/scripts/queue_gate.py`——`TASKS_DIR` 模块级 + `_is_rework_task()`（frontmatter `rework: true` 读侧，仿 `_is_batch_task` 先例）；`can_claim` own-pending 分支加 rework 豁免
- `90_control/scripts/queue_transition.py`——`action_review` fail 分支 + `#538` `_action_review_override` 分支：FAIL 打回 queued 时 `apply_updates(..., rework=True)` 自动打标（幂等，多轮返工重复写 true 无副作用）
- `90_control/scripts/tests/test_rework_reclaim.py`——新增回归 10 例

**完成内容**：终审 FAIL 打回（review fail + #538 改判）自动给任务单打 `rework: true`；返工重提 claim 时 `_is_rework_task` 命中即豁免 #504 own-pending 阻塞——重提≠接新单，不再需要 --force。非 rework 单 #504 原语义不变；他人前方 pending FIFO 阻塞与 #503 claimed 锁均不豁免。force-exceptions.log 机制保留（其他例外仍走留痕）。

**验证**：`python -m pytest 90_control/scripts/tests/ -q` → **205 passed**（基线 195 + 新增 10，Python312）。含任务单验证节三场景：①own pending + rework:true → 无 force 可领（含 #575 在 #578 前的 FIFO 陷阱用例——第一版实现 `pass` 跳过会跌入下方 FIFO 分支照样被拦，自查发现改为把 own 从阻塞集剔除）②own pending + 普通新单 → 仍拦，报文含 #504 ③FAIL 打回/override 打标 → frontmatter `rework: true` 真落盘（真身 apply_updates 验证）+ PASS 不打标 + 他人前方 pending/#503 锁不豁免。真实队列冒烟：`queue_gate.py status` → claimed 执行中 1（#580）正常。

**边界**：kdo-seed 种子包 `90_control/kdo-seed/seed/90_control/scripts/queue_transition.py` 与主版自 #532 起即不同步（seed 停在旧版，主库新增代码不在 seed），本单维持现状不同步（seed 更新属另案，非本单范围）；`queue_gate.py` seed 副本本单未触碰。matrix_exempt 理由：纯状态机门禁内部逻辑，不改任何检出信号与通知通道（#569/#568 同款豁免口径）。历史 FAIL 打回的任务单（rework 机制上线前）无自动标，如再遇 #504 误拦仍走 --force 留痕。

**需要谁动作**：待欧阳锋终审（queue_transition complete 提审，REVIEW-PENDING 自动登记）。建议后续观察：下次真实 FAIL 打回→返工重提链路走通后，可在 kdo-queue-operations skill 坑 6 补一笔「#580 起 rework 场景不需 force」。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
