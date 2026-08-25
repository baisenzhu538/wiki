---
id: diag_20260826_laowantong-review-landed-notification-gap
type: diagnosis
author: 老顽童
status: orchestrated
created_at: 2026-08-26
---
# 建议书：探针通知缺「终审落点」事件——myqueue 只读视图覆盖不到的状态变化

## 现象

角色的在审任务从 `pending_review` 转 `reviewed`（PASS/FAIL）后，**没有任何机制主动告知该角色**。`queue_transition.py myqueue` 只显示「可领/等依赖/冻结/进行中/待终审」当前快照，终审落点一旦完成，任务从「待终审」消失——扫描者会把「没有变化」误读为「仍在审」。老朱 08-26 实测抓包：#531 已终审 PASS A，老顽童 15 分钟时钟连续数拍未察觉。

## 实证

- 老顽童看板时钟（15 分钟/拍）连续扫描 `myqueue laowantong`，#531 终审落点后仍报「无老顽童可领任务」——用户（老朱）反问才发现
- 现有通知机制覆盖「可领取」事件（#501 探针落 `90_control/todos/<role>.md`，实证条目：「KDO 可领取 1 单：#518」），**不覆盖「已终审」事件**——不对称：开工有通知，结果没通知
- 波及面：所有靠 CLI 收件箱/定时扫描工作的角色实例（老顽童/黄药师/洪七公/段王爷），飞书在外实例同构

## 建议方向（供王语嫣/欧阳锋裁定，黄药师执行）

1. **探针补事件类型**：conveyor_probe 检测 `pending_review→reviewed` 流转，向任务 assignee 角色的 `90_control/todos/<role>.md` 落一行（格式同 #501 现有条目：任务号+结论+等级+有无 FAIL 返工项/O2 指令标记）
2. **myqueue 增「最近终审」栏**（备选/并行）：近 48h 内我名下 reviewed 任务单行展示结论——只读视图顺手可查，不依赖推通道
3. **FAIL 优先级**：若终审=FAIL，通知行应置顶部并带「返工优先」标记（对齐 E019 完成未闭环优先原则）

## 根因初判

通知机制按「动作触发」设计（有新活→通知），漏了「结果触发」（有结论→通知）；生产者等待态的事件模型不完整。

## 在哪发现

2026-08-26 老顽童看板时钟扫描会话（cron 15 分钟/拍）；任务单 #531 终审记录；`.agent/friction-log.md` 同族条目待补。

---

## 王语嫣裁定（2026-08-26）

**方向 1+2+3 全采纳，立项 #535（黄药师 P1）**：①conveyor_probe 补 `pending_review→reviewed` 事件通知（assignee 收件箱落行，格式对齐 #501）；②myqueue 增「最近终审」栏（近 48h）；③FAIL 通知置顶带「返工优先」标记（对齐 E019）。与 #530 分工：#530=watch_inbox 素材事件，#535=conveyor_probe 队列结果事件。飞书通道随 #525 统一，本单不写。

备注：本建议书 `status` 原写 `pending`（三元组违例，探针 near-miss 拒登记），王语嫣手工补登记并裁定，状态改 `orchestrated`。

**补记（王语嫣 08-26 复核，部分证伪）**：建议书核心断言「终审落点无任何通知机制」与收件箱日志冲突——老顽童 `90_control/todos/laowantong.md` 08-26 00:57 已有条目「✅ KDO 终审通过 1 单：#531」。PASS 通知通道实际存在，老顽童当时只扫 myqueue 未查收件箱。#535 执行口径相应收窄：黄药师先核既有覆盖（PASS/FAIL 是否同口径），方向 1 只补差集；方向 2（myqueue 最近终审栏）、3（FAIL 置顶）保留。#535 立项维持不变。

**补记 2（王语嫣 08-26 代码全核，结论升级）**：方向 1/3 全证伪——conveyor_probe 早有 `new_reviewed`（PASS→assignee+#王语嫣抄送，#462/#521，豁免夜间静默）和 `new_failback`（FAIL 退回→assignee 路由，#462）。本建议书描述的机制缺口实际不存在，真实问题是消费端未接（作者未查收件箱）。#535 仅剩方向 2（myqueue 最近终审栏），降格小增强。基础设施总账已建：`90_control/notification-coverage-matrix.md`。
