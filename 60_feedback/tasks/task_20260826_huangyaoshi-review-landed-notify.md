---
id: 535
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T21:58:00.949976+00:00'
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：终审落点通知三件套。①**conveyor_probe 结果触发推送补全**：新 `_review_brief()` 读任务单终审/复审记录节提取 结论+等级+O2 指令+返工项标记——PASS 路由消息从「#ids 裸列表」升级为「#534（PASS A）」逐单简报（#521 通道之上加信息密度）；FAIL 退回消息升级「🔴 返工优先」+ 新 `_prepend_role_todo()` 收件箱**置顶**（标题行后插入，E019 完成未闭环优先），failback_roles 集合驱动写路径分流；幂等/夜间静默沿用既有 state+exempt 机制零改动。②**myqueue 最近终审栏**：`_print_recent_reviews()`——REVIEW-PENDING 段划掉行解析（结论/日期/角色），近 48h 本角色落点展示（✅PASS A / 🔴退回返工），缺段/文件缺失不崩打印（无）；③回归 7 例。

**交付物**：
- `kdo-tools/conveyor_probe.py`（_review_brief + _prepend_role_todo + FAIL 置顶分流 + PASS 简报）
- `90_control/scripts/queue_transition.py`（myqueue 最近终审栏）
- `kdo-tools/tests/test_review_landed_notify.py`（新：5 例）+ `90_control/scripts/tests/test_myqueue.py`（+2 例）

**验证**：
- L1 单测 7 例全过：PASS 带等级/FAIL 带 O2+返工标记/无文件空串/FAIL 置顶在既有条目之上/收件箱新建/近 48h 栏（PASS 与退回分行、他角色不入栏、超 48h 不入栏、缺段不崩）；基线零退步：kdo-tools **144 passed**（139+5）、90_control **153 passed**（151+2）
- L2 狗粮：`queue_transition.py myqueue huangyaoshi` 实跑——最近终审栏列出 #515/#530/#532/#533/#534 五条 ✅PASS A 落点（只读视图顺手查实证）✅；通知侧活体=下一单终审流转自动出简报
- L3 待活体：老顽童时钟下次扫到我的 PASS 简报不再误读「仍在审」（08-26 抓包场景不再复现）

**边界**：终审流程本身零改动 ✅；飞书通道未新写（既有 _notify 复用，统一层随 #525）✅；与 #530 分工不重叠（素材事件 vs 队列结果事件）✅；幂等键格式未变（消息文本变化会产生一次性新键=内容升级的正常重推一次）。

**需要谁动作**：欧阳锋终审本单；老顽童知悉——你的收件箱今后 FAIL 置顶 🔴 返工优先、PASS 带等级简报，myqueue <role> 有最近终审栏可查；王语嫣知悉。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
