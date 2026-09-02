---
id: task_20260903_huangyaoshi-orphan-backup-source-hunt
title: 孤儿 backup commit 触发源追查（01:38 非节拍收走在制品，#628 守卫外的旧路径）+ 探针非节拍检测信号
seq: 631
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师建议书 diag_20260903_huangyaoshi-backup-orphan-source（09-03 王语嫣裁定）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T18:31:25.734561+00:00'
---

# #631 孤儿 backup 触发源追查（黄药师）

## 背景

01:38:12 出现非节拍 backup commit（545bd0f5a）收走 #628 施工中 3 文件+王语嫣会话归档等 28 文件——#628 守卫（01:36 落盘）之外的旧代码路径。系统任务未触发，疑 #607 前会话级 cron 残留。

## 任务

1. **触发源锁定**：查各 kimi/claude 会话级调度残留（CronList 类机制的历史 session 残留不起作用——重点查 schtasks 全量表+各 CLI 会话 cron 残留+旧版备份脚本调用点），找到 01:38 那次是谁发的
2. **conveyor_probe 加「非节拍 backup commit 检测」**：git log 时间戳 vs 预期节拍（:02/:32）差 >10min → 报警
3. **#628 守卫 SKIPPED 行接第十信号**：认跳拍不报停拍（哨兵口径细化）

## 交付

- 触发源结论（含证据）+ 探针信号上线 + 执行报告
- claim/complete 走 queue_transition（complete 631）

## 执行报告（2026-09-03 黄药师）

**交付物**：① `kdo-tools/conveyor_probe.py` 第十二信号 `_scan_offbeat_backup`（非节拍 backup commit 检测）+ 第十信号 `_scan_backup_stall` 口径细化（`_last_skip_age_h`：守卫 SKIPPED 认跳拍不报停拍）② `kdo-tools/tests/test_backup_signals_631.py`（6 测）③ `90_control/notification-coverage-matrix.md` 行 28 登记 ④ 本任务单执行报告（含触发源结论证据链）

**完成内容**：① 触发源锁定——**孤儿源 = obsidian-git 插件 auto backup**，证据链三铁证：a) `.obsidian/plugins/obsidian-git/data.json`：autoSaveInterval=10（min）、commitMessage/autoCommitMessage="vault backup: {{date}}"——与 vault_git_backup.py 消息模板**完全同文**（这正是 obsidian-git 出厂默认模板）；b) commit 时间链实证：01:28:02→01:38:12→01:48:24→01:58:34 严格 ~10min 链，孤儿 commit 545bd0f5a（01:38:12）正落链上；c) 双写手对照：整秒命中 :20/:50 的 commit（00:20:00/00:50:00/01:20:00…）= schtasks kdo-vault-git-backup（触发器 07:20 起 PT30M），非整秒 ~10min 链 = obsidian-git（Obsidian.exe 两进程在跑）。obsidian-git 走自带 git 通道，#628 守卫（只拦 vault_git_backup.py 路径）管不到——这就是「守卫落盘后旧代码路径仍扫走在制品」的真身，且它从 #607 之前就一直与脚本双写并存 ② 第十二信号：3h 窗内 `vault backup:` commit 距节拍格（:20/:50，#628 实测口径——任务书写的 :02/:32 是旧印象）超 ±10min → 告警，沿触发幂等、全窗干净重新武装，并入 infra_alerts 通道 ③ 第十信号口径细化：commit 停拍超窗但守卫 SKIPPED 行（logs/vault-git-backup.log）在窗内 = 主动跳拍=健康不报；SKIPPED 也超窗则照报（守卫不能成停拍遮羞布）

**验证**：① 新测试 6 条全过（非节拍告警+幂等 / 格点容差不报 / 窗口过期重新武装 / 停拍+近期SKIPPED不报 / SKIPPED也超窗照报 / 原始停拍语义保留）② 真机首拍即现行：`_scan_offbeat_backup` 对真实仓报「非节拍 commit 02:39:59（窗内 5 个）——孤儿写手嫌疑（obsidian-git）」——信号上线即抓到活的第二写手 ③ 真机 `_scan_backup_stall` 健康无告 ④ 全量回归 488 passed / 0 failed（kdo-tools + 90_control/scripts 两测试树，#627 清红后基线）⑤ 节拍格证据：git log 整秒 :20/:50 序列 vs obsidian-git 10min 链逐条比对（见完成内容①）

**边界**：第十二信号在 obsidian-git 未处置前会 latch 脏态（报一次后静默，沿触发口径）——处置（关 auto backup）后窗口自然干净、自动重新武装；节拍格 :20/:50 为写死常量（schtasks 触发器若改需同步，代码注释已标）；obsidian-git 侧不做任何修改（.obsidian 机器本地配置不入库，且处置权属王语嫣/老朱）；**存在性核查**：负向判词「#607 前会话级 cron 残留」经 CronList（本实例 0 残留外任务）+ 建议书已查 config.toml/会话目录/headless 日志无痕迹 + 本单锁定真凶为 obsidian-git——「会话级 cron 残留」假设不成立，排除依据=真凶已锁定且证据链闭合

**需要谁动作**：欧阳锋终审（重点核：双写手结论证据链、节拍格取 :20/:50 实测口径、SKIPPED 认跳拍口径）。**王语嫣/老朱处置决策**：obsidian-git auto backup 是否关闭——⚠️注意 autoPushInterval=10 + disablePush=false，它同时是**当前唯一活跃 push 通道**，关 auto backup 会连 push 一起停，需先另立 push 机制（或仅知情保留、容忍双写）
