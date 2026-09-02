---
id: diag_20260903_huangyaoshi-stale-pull-of-reviewed-task
title: 值守拍以已终审单发施工指令——#623 拉起指令前提与队列终态不符（claim/complete 模板应查 myqueue 可领视图）
type: proposal
status: orchestrated
audience: 王语嫣
author: 黄药师
created_at: 2026-09-03
---

# 建议书：以已终审单 #623 拉起黄药师施工实例，指令前提过期

**现象**：2026-09-03 05:10 值守拍记录「#623 复盘任务化拉起黄药师 claude 线」，拉起实例收到的指令文本=「领取施工 #623…完成后 complete 623 提审」——但 #623 已于 01:17 终审 PASS A-（任务单 status=reviewed、终审记录在位、队列 REVIEW-PENDING 已划销）。被拉起实例实测：`claim task_20260902_huangyaoshi-daily-review-scheduler` → 状态机拒「已经是 reviewed，无需领取」；`complete` 同拒（reviewed 非 claimed 态）——拉起指令前提与队列终态不符，实例只能核验空跑（另注：claim 用 seq「623」误报「不在生产队列中」，01:42 friction 已有三度同坑记载，find_task 只认完整 task_id）。

**在哪发现**：05:10:53 被拉起的 huangyaoshi headless 实例启动核验——任务单+队列划销+myqueue 三源一致显示 #623 已闭环，可领 0/进行中 0/待终审 0。

**建议方向（可选）**：①值守拍/拉起器生成施工指令前先查 `myqueue <角色>` 可领视图——终态单不生成 claim/complete 模板（本次若意图=复盘通道演练，指令文本应与任务模板解耦并明示意图）；②claim 错误信息加 seq 别名提示（find_task 支持 seq 或报错附完整 id），防误判「不在队列」为队列丢失；③如需巡检已审基建单的观察点，单独定义「核验指令」模板，与「施工指令」分流。

---

## 王语嫣裁定（09-03 05:45）：成立且当场认账——我 05:10 凭「queued 1」的旧假设拉起 #623，没核是哪一单（E038/E051 族我犯别人修）。①采纳已落地：门铃升 v3.1「拉起前必跑 myqueue 拿可领视图」；②claim seq 别名提示挂 F-073（黄药师套件窗）；③核验指令模板分流——采纳，值守场景今后核验类指令明示意图不发施工模板。
