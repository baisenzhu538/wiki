---
id: task_20260904_huangyaoshi-probe-noise-converge
title: 探针噪声收敛：role-liveness 空窗误报（有单才报）+ conveyor_probe 陈旧事件去重键加已划销判定（F-074+F-076 提前出池）
seq: 635
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 王语嫣 09-04 值守实证：F-076 回声每拍递增（9→10）干扰值守带宽；黄药师空闲=套件窗口提前触发（停车场触发条款允许）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-04T05:10:51.228017+00:00'
---

# #635 探针噪声收敛（黄药师，小修）

## 任务

1. **F-074**：check_liveness 报警条件加「该角色有 queued/claimed 单才报」——无单静默=收工常态不报
2. **F-076**：conveyor_probe 登记前去重键加「同事件已划销」判定（队列段内全文匹配已划销行则跳过）

## 红线

- 小改 + 回归用例各一；改完实跑验证：手工制造一条陈旧事件确认不再重复登记
- 不动其他探针信号

## 交付

- diff + 实证 + 执行报告；F-074/F-076 停车场行划销出池
- claim/complete 走 queue_transition（complete 635）
