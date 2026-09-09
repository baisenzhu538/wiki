---
id: task_20260910_huangyaoshi-claimed-stall-auto-relaunch
title: "claimed 停摆自动补拉门禁化：探针发现 claimed 超 45min 无产出心跳→自动拉起对应角色（不等王语嫣人工补拉）"
seq: 697
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-10
decision_source: 老朱 09-10 令「不相信纪律只相信门禁」——王语嫣门铃 v5 的人工心跳督查只是过渡，本单把它机制化（F-080 出停车场）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-10T02:10:00+08:00'
---

# #697 claimed 停摆自动补拉门禁（黄药师）

> 背景实证（09-10 凌晨）：老顽童 #684 被 kimi headless cron wedge 掐死后 claimed 挂了 2.5h 无人续命；黄药师 #690 领后实例自然退出挂 1.5h。王语嫣人工补拉是纪律不是门禁——老朱口径：不信纪律信门禁。

## 现状

conveyor_probe 已有「claimed 超 45min 无产出→todos 落提醒」的检测（门铃 v4 时代靠它提醒、王语嫣手动补拉）。本单=把「提醒」升级为「自动补拉」。

## 规格

1. **停摆判定**（探针侧）：claimed/in_progress 任务 45min 无产出心跳（headless 日志 mtime 或产出物 mtime 无增长）→ 判定停摆
2. **自动补拉**：调 `90_control/scripts/kimi-headless-launch.py <role> "<续产指令>"`（通道预检 fallback 复用 #656）——拉起即补位
3. **防误伤三件套**：①同一任务 2h 内最多自动补拉 2 次（防死循环烧额度）②连续 2 次补拉仍无产出→停拉升级报警（gate-blocked 落账等王语嫣裁定，可能是任务本身有问题）③补拉前后各落一行台账（原 proc/停摆时长/新 proc）
4. **幂等**：探针多实例/重跑不重复拉起（拉起前先查该角色活跃 headless 进程是否真在跑）
5. 顺带修：kimi headless cron wedge（"next fire time stuck in the past" 掐死会话）——至少加检测与记录，根治另议

## 验收标准

- 构造停摆场景（杀进程留 claimed）→ 探针下一拍自动补拉成功，台账完整
- 防误伤三条款各有实测证据（连补 2 次后停拉+报警）
- 欧阳锋终审

## 边界

- 排 #693/#696 后；只动 conveyor_probe/拉起链路，不动队列状态机
- 自动补拉指令模板沿用王语嫣值守口径（续产指令含任务单路径+剩余规格提示）
