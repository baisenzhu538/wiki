---
id: 574
assignee: huangyaoshi
status: queued
updated_at: '2026-08-28T15:44:40+00:00'
version: v0.1
code_files: []
---

# #574 check-review-sla 升级「超时必推」+ 推送通道对齐调研（R1+R3 合并立项）

- **任务号**：#574 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P1
- **立项**：2026-08-28 王语嫣裁定（欧阳锋建议书 `diag_20260828_ouyangfeng-review-wakeup-gap.md`，R1+R3 合并，R2 欧阳锋自执行）

## 背景

待审提醒断链（#573 事件实证）：todos/cron/webhook 三通道全部工作但止于「文件/群」，无一能真实唤醒审查者会话——#573 提审后挂审 40min 无人响应，直到用户飞书追问才叫醒。性质=推送通道与唤醒通道不匹配的机制断链，非「agent 不自觉」。且 #521 R2 老朱已拍板「终审类通知不静默」未落地。

## 任务

1. **R1（治本门禁）**：check-review-sla.py 升级「超时必推」——pending_review 最大年龄 30min → 推送提醒（复用 conveyor_probe._send_hook 加签，零新基建）+ todos 落盘；2h → 升级 @ 负责人/老板。消息含「#xxx 待终审 + 挂审时长 + 任务单路径」。
2. **R3（调研，并入本单）**：webhook 群机器人接收端（17f2a4cd-50b8-4e4e-9036-ec26b0c9d67d）是否用户/老朱可见常用；若不可见，评估角色 webhook 指向「gateway 监听 DM 入站通道」或统一 cron deliver=feishu；调研 Hermes gateway 是否支持 webhook 入站（消息进输入流=「提醒即唤醒」完全自动化）。

## 验证

- R1：构造 31min 挂审样例 → 触发 webhook 推送 + todos 落盘；2h 样例 → 升级消息含 @ 标记。
- R3：调研结论落档（webhook 接收端可见性 + gateway 入站可行性）。
- 回归：#573 同场景重演——提审后 30min 内审查者会话被真实唤醒（用户/老朱飞书可见提醒即达标）。

## 边界

- 本单不改判任何既有机制（#520 叫醒通道/探针全保留），只补「超时升级」与「通道对齐」两环。
- R2（ouyangfeng-clock-v1 deliver local→feishu）不占本单——欧阳锋自改非共享基建，即时见效。
- 复用 #519 空转报警（check-conveyor-state）同族先例：「有异常必须响」机制化。
- 若实现触碰 conveyor_probe.py/queue_transition.py/role_clock 三基础设施文件，按第七信号精度纪律（08-28 裁定）在任务单 frontmatter 预标 matrix_exempt: true+理由。

## 关联

- 欧阳锋建议书 `diag_20260828_ouyangfeng-review-wakeup-gap.md`（R1+R2+R3 全采纳裁定）
- #520 R3（check-review-sla 初版，SLA_HOURS=2h 只 print 无推送）/ #519（空转报警同族）/ #521 R2（老朱拍板「终审类通知不静默」）

## 需要谁动作

- **黄药师**：R1+R3 施工，回归验证
- **欧阳锋**：终审本单；R2 自改 ouyangfeng-clock-v1 deliver→feishu（与本单并行，不占产线）
