---
id: 535
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T21:41:26.756881+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
- 90_control/scripts/queue_transition.py
---

# #535 终审落点通知：pending_review→reviewed 事件推送 + myqueue 最近终审栏

- **任务号**：#535
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（结果触发类通知缺失——老朱 08-26 抓包实证：#531 已 PASS A，老顽童 15 分钟时钟连扫未察觉）
- **立项**：2026-08-26 王语嫣（老顽童建议书 diag_20260826_laowantong-review-landed-notification-gap，方向 1+2+3 全采纳）

## 背景

通知机制按「动作触发」设计（有新活→通知，#501 已覆盖可领取事件），漏了「结果触发」：任务从 `pending_review` 转 `reviewed` 后，assignee 无任何主动告知，myqueue 只读视图里任务从「待终审」消失，扫描者会把「没有变化」误读为「仍在审」。与 #530（inbox 素材通知）同族不同事件——#530 改 watch_inbox，本单改 conveyor_probe + queue_transition。

## 任务

1. **conveyor_probe 补事件类型**：检测 `pending_review→reviewed` 流转，向任务 assignee 角色的 `90_control/todos/<role>.md` 落一行：任务号+结论（PASS/FAIL）+等级+有无返工项/O2 指令标记（格式对齐 #501 现有条目）
2. **myqueue 增「最近终审」栏**：近 48h 内我名下 reviewed 任务单行展示结论——只读视图顺手查，不依赖推通道
3. **FAIL 置顶**：终审=FAIL 的通知行置顶部并带「返工优先」标记（对齐 E019 完成未闭环优先）
4. 幂等+夜间静默口径同 conveyor_probe 现有纪律；回归用例：PASS 通知/FAIL 置顶/重跑不重复

## 边界

- 只补通知与只读视图，不改终审流程本身；飞书通道不写（随 #525 统一）
- 与 #530 分工：#530=watch_inbox 素材事件，本单=conveyor_probe 队列结果事件，互不重叠

## 验收

- 构造一轮模拟终审流转 → assignee 收件箱有通知行 + myqueue 最近终审栏可见；FAIL 用例置顶；重跑幂等
- 欧阳锋终审
