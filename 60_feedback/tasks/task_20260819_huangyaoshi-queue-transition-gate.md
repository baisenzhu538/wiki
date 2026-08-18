---
id: 363
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: queue_transition 提审门禁（P1）——代码类任务提审强制 git 收净 + 修 complete --force 锁内重检 bug
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #363 queue_transition 提审门禁（P1）

## 任务目标

提审环节强制"修复已入版本控制"：代码类任务 complete 流转前，改动文件涉及路径 git status 必须清零。治"修复不 commit"复发（08-18 #359 收了一次，当晚 23:44 KDO 仓又复发）。

## 素材/证据

- friction-log 2026-08-19：complete --force 锁内重检 bug（L260 不认 force 路径，从 queued 直跳必败；历史"queue_transition被拦+手动流转"同根因）
- 复发实证：KDO 仓 delivery.py/graph.py 23:44 改动未提交（#361 收口前置）

## 修改范围

1. **complete 门禁**：任务单"改动文件"涉及路径在 git 仓内仍有未提交改动 → 拒绝流转，报错指明未提交文件清单
2. **代码类识别**：方案黄药师裁决——任务单 frontmatter 加 `type: code` 字段 / 按改动文件扩展名自动判定（.py/.js/.yaml 等）；制卡类豁免（pre-submit 门禁已管）
3. **修 force bug**：complete --force 锁内重检接受 queued（force 语义）——现行绕行 claim+complete 两步转正或保留兼容
4. wiki 仓 + KDO 源码仓双仓都要查（#357 跨两仓前科）

## 边界

- 只改 90_control/scripts/queue_transition.py（+ 任务单模板如需加字段）
- 不溯及既往（已在审/已终审任务不回头查）

## 验收标准

1. 构造未提交改动 → complete 被拒且报错清单正确；commit 后 → 放行
2. 制卡类任务流转不受影响（回归）
3. --force 从 queued 直跳可用（回归 friction-log 场景）
4. 双仓路径均覆盖

## 交付

1. 修复 + 门禁 + 正反向实测
2. 送欧阳锋终审
