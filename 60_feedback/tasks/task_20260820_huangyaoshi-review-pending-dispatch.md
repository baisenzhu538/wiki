---
id: 389
assignee: huangyaoshi
status: in_progress
title: REVIEW-PENDING 待终审自动登记段（P2，老朱 08-20 拍板立项）
priority: P2
dependency: []
code_files:
- 90_control/scripts/queue_transition.py
- 70_product/tasks/production-queue.md
updated_at: '2026-08-20T04:00:23.786585+00:00'
---

# #389 REVIEW-PENDING 待终审自动登记段

## 来源

- 建议书：`60_feedback/diagnosis/diag_20260820_wangyuyan-review-pending-dispatch.md`（**必读**，含事件证据链/根因分层/设计约束/验收标准）
- 事件：08-20 #387 提审后欧阳锋"找不到"——**根因经黄药师洞察+git 实锤修正（11:34 后）**：提审产物（任务单/队列行/dashboard）只在工作区未 commit，欧阳锋从独立 git 同步 checkout 读，文件对其不存在——"提审未提交=不在审查通道"（与"修复未提交=不存在"同病）。黄药师已补提交 e4e6f1f53。建议书原"旧快照"表述以本修正为准。
- 老朱 08-20 拍板：立项，另开任务，不改动在飞任务

## 任务目标

给队列加 REVIEW-PENDING 自动登记段，与 INBOX-PENDING 完全对称：complete 自动登记、review 自动划掉，欧阳锋开工只看这一段。

## 执行范围

1. `70_product/tasks/production-queue.md` 增加 `<!-- REVIEW-PENDING-BEGIN/END -->` 自动维护段（"勿手改"惯例同 INBOX-PENDING）
2. `queue_transition.py complete`（门禁通过后）自动登记一行：任务号 + slug + assignee + 提审时间 + 任务单路径
3. `queue_transition.py review` 终审完成时自动划掉对应行
4. dashboard 同步展示 REVIEW-PENDING：执行时评估工作量，量小（仅读段渲染）则并入本单，需改 generate-dashboard 架构则出评估报告另立项（老朱拍板项②授权执行者评估）

## 设计约束（建议书写死）

1. 只加登记段，**不动状态机语义**——登记段是纯日志视图
2. 与 #363 提审门禁兼容：登记发生在门禁通过之后，被拦截的 complete 不登记
3. 段内格式与 INBOX-PENDING 对齐
4. 367 个历史任务不补登记（只向前生效，不回填）

## 边界（不做的事）

- 不改任务单命名惯例
- 不做主动推送（飞书通知等）
- 不动 queue_transition.py 的状态机/门禁逻辑
- **不改动在飞任务**（#387 pending_review / #388 queued 的单据与队列行零接触——老朱 08-20 明确指令）

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅新增机制代码与队列模板段，无删除/移动

## 验收标准

1. 正向实测：测试任务 complete → REVIEW-PENDING 段自动出现登记行（任务号/时间/路径齐）
2. 反向实测：review 后对应行自动划掉；手动乱改段内内容会被下次流转纠正或报警
3. 门禁拦截的 complete（未提交代码）不产生登记行
4. INBOX-PENDING 段功能零回归
5. 测试夹具清理干净，队列真实任务行零污染

## 交付

1. 代码 + 队列模板段 + 正反向实测记录（diff 贴执行报告）
2. dashboard 展示：并入则一并交付；另立项则出评估结论
3. 送欧阳锋终审
