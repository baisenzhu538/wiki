---
id: task_20260910_huangyaoshi-claimed-stall-auto-relaunch
title: "claimed 停摆自动补拉门禁化：探针发现 claimed 超 45min 无产出心跳→自动拉起对应角色（不等王语嫣人工补拉）"
seq: 697
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-10
decision_source: 老朱 09-10 令「不相信纪律只相信门禁」——王语嫣门铃 v5 的人工心跳督查只是过渡，本单把它机制化（F-080 出停车场）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T18:45:24.772570+00:00'
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

## 执行报告（黄药师 2026-09-10 03:0x，#697）

### 五字段摘要（#429 F-034 机器可读）

**交付物**：`kdo-tools/conveyor_probe.py`（第十一信号 `_scan_claimed_stall`：45min 停摆判定+自动补拉+三件套+幂等+wedge 兜底检测；--no-relaunch 应急开关）；`90_control/notification-coverage-matrix.md` 行 20（信号面同步登记，§3.19 义务）；台账 `logs/claimed-relaunch.log`（验收实测 8 行在案）；验收证据 `_tmp/task697-accept.py` + `_tmp/697-accept-result.txt`（8/8 PASS）。

**完成内容**：①停摆判定=任务单 mtime 超 45min（claim/报告/流转都触碰 mtime，无产出即老化）；②自动补拉调 kimi-headless-launch.py（#656 通道预检内建），指令模板自带「先查在制品，10min 内有他实例痕迹立即收工」防双写纪律（00:42 撞车事件教训内嵌）；③防误伤三件套：2h 窗口 2 次上限（state.claimed_relaunch 计数）/连 2 次无产出停拉+gate-blocked 升级/前后台账；④幂等：该角色 headless 日志 10min 内有增长=活实例在跑，跳过且不耗次数；⑤wedge 检测：wedge 掐死实例无产出心跳，被本信号判定捕获补拉——检测+台账+补拉兜底在本信号内闭环（kimi cron 根治另议，按任务书第 5 条口径）。

**验证**：验收 8/8 PASS（合成停摆任务 mtime 回拨 50min+monkeypatch parse_queue+真弹头）——第1拉真 launcher 拉起真 headless 会话（logs/headless-huangyaoshi-*.log 新鲜落盘）+计数=1+台账 BEGIN/END；幂等拍（日志新鲜）跳过不耗次；第2拉到上限=2；第3拉停拉升级+gate-blocked `relaunch-exhausted` 落账；探针主干 `--no-relaunch` 冒烟 rc=0 全信号正常；py_compile 过。

**边界**：不动队列状态机（只读 parse_queue）；合成任务单已删、演练 state 为进程内不落盘、gate-blocked 的 relaunch-exhausted 演练行是真实测试记录（非故障）；kimi cron wedge 根治另议（本单仅兜底检测，任务书原口径）；演练拉起的真 headless 会话按指令④对缺失任务单落 todos 收工——其 todos 行属演练痕迹。

**需要谁动作**：①欧阳锋终审（重点：补拉指令的防双写纪律措辞与矩阵行 20 口径）；②王语嫣——你现在是本信号的裁定端：收到「停拉升级」通知即代表某任务连补 2 次无产出，需人工判任务本身是否有问题；③全员知悉——名下 claimed 任务超 45min 不碰任务单文件会被自动补拉，长思考/长拷贝期间请保持任务单 updated_at 新鲜（写一行进度即可续命）。
