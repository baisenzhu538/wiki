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

---

# 执行报告（黄药师 2026-08-20 12:5x）

## 一、实现

`90_control/scripts/queue_transition.py`（唯一代码改动，+约 75 行）：
1. `_review_board_update(register=..., strike=..., strike_note=...)`——REVIEW-PENDING 段维护函数：登记（task_id 级幂等）/划掉（附终审注记）/段不存在则创建（插到 INBOX-PENDING 段前）；列表行非表格行，parse_queue 零干扰；失败不阻断流转但 stderr 打印警告（吸取 _filter_by_trust 静默吞错教训）
2. `action_complete` 钩子：#363 门禁通过、状态落锁后登记——**被门禁拦截的 complete 到不了登记点**（设计约束 2）
3. `action_review` 钩子：pass 划掉附「已终审 PASS X（date 欧阳锋）」；fail 划掉附「终审退回 queued」

## 二、正反向实测（沙盒：KDO_QUEUE_PATH/KDO_TASK_DIR/KDO_BATCH_DIR 环境变量隔离，真实队列零接触）

| 验收 | 实测 | 结果 |
|:--|:--|:--|
| ① 正向登记 | 测试任务A claim→complete → 段自动创建+登记行（#999/slug/assignee/提审时间/任务单路径齐） | ✅ |
| ② 反向划掉 | review pass → 行自动 `~~划掉~~ → 已终审 PASS A（2026-08-20 欧阳锋）` | ✅ |
| ②b 手改纠正 | 手动破坏 BEGIN 标记后再 complete → 段自动重建，登记正常 | ✅ |
| ③ 门禁拦截不登记 | 任务B code_files 指向脏文件 → complete 被 #363 门禁拒绝 → 段内无 B 行 | ✅ |
| ④ INBOX-PENDING 零回归 | 沙盒 INBOX 段内容流转前后字节不变 | ✅ |
| ⑤ 夹具清理 | 沙盒在 %TEMP%（仓外），已整体删除；真实队列任务行零污染 | ✅ |

## 三、dashboard 评估结论（拍板项②）

**不并入本单，也不需要另立项**：dashboard 的「审查中」组已由队列表格驱动（complete 后 queue_transition 自动 _refresh_dashboard，pending_review 任务实时在列）——REVIEW-PENDING 段解决的是「欧阳锋开工只看一段」的人读入口，dashboard 已有等价展示，无需改 generate-dashboard 架构。

## 四、设计约束遵守自查

- 只加登记段，状态机/门禁逻辑零改动（diff 可证：TRANSITIONS/_check_code_gate/apply_updates 未碰）
- 登记发生在 #363 门禁之后 ✅（实测③）
- 367 历史任务不回填 ✅（段初始为空，只向前生效）
- 在飞任务（#387/#388）单据与队列行零接触 ✅

## 五、自证循环

本任务 complete 时，#389 自己将成为 REVIEW-PENDING 段的第一条真实登记——机制上线即自用。
