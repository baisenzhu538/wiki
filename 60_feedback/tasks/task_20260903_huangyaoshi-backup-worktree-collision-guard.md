---
id: task_20260903_huangyaoshi-backup-worktree-collision-guard
title: vault backup × agent 在制品互撞防护：备份前活动会话检测（#607 上线后新事故面，00:32 险些丢工作实证）
seq: 628
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师建议书 diag_20260903_huangyaoshi-vault-backup-agent-worktree-collision（09-03 王语嫣裁定：纪律①立即生效+机制②立项本单）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-02T17:41:29.308115+00:00'
evidence: _tmp/628-evidence.txt
---

# #628 备份×在制品互撞防护（黄药师）

## 背景（事故实证）

#607 的 30min 系统级备份（git add -A 式快照）会把 agent 施工中未提交改动整批扫入 backup commit——00:32 实证：#625 headless 实例施工中被收走，stash pop 冲突 aborted 险些丢工作。

## 任务

1. **机制层**：vault_git_backup.py 备份前检测活动 agent 会话（role_registry 心跳或运行中 headless 进程），有活动则本拍跳过（留痕 skipped 行）——宁可少一拍备份，不可收走在制品
2. **纪律层落字**：kimi-headless-launch.py 拉起模板加一条「备份节拍 :02/:32 前后 5 分钟禁 stash/worktree 切换类操作；长任务隔离验证一律 git worktree」
3. 回归：模拟活动会话存在时备份跳过实证

## 交付

- diff + 跳过实证 + 执行报告
- claim/complete 走 queue_transition（complete 628）

## 执行报告（黄药师 09-03，工作落 HEAD=545bd0f5a）

**交付物**：①vault_git_backup.py #628 互撞防护（活动会话检测 + 跳拍留痕）；②kimi-headless-launch.py 拉起模板备份避让纪律行；③test_vault_git_backup_gate.py +5 守卫用例（现 10 passed）。

**完成内容**：
- 机制层：`active_sessions()` 双信号 OR——①role_registry 非 platform 实例心跳 ≤20min（逐实例判，规避 role 级 last_heartbeat 字段 ts=0 污染）；②运行中 agent CLI 进程（wmic ExecutablePath + 路径特征过滤：`.kimi-code`/`claude-code`/`codex-win32`——kimi-desktop GUI 与 hermes 网关 Services 常驻均排除，实测 4 个 kimi-desktop 零误报）。任一命中 → 本拍跳过并打印 `vault backup: <ts> SKIPPED（#628 活动会话 N：…）` 留痕，rc=0（不触发停摆报警）；读失败/查询失败一律 fail-open 不拦备份。
- 纪律层：拉起模板「通用纪律」追加「备份避让（#628）……拍前 5 分钟禁 stash/worktree 切换类操作；长任务隔离验证一律 git worktree」。节拍按实况落字：schtasks XML 实证 2026-09-02 07:20 起 PT30M → 实际落 :20/:50（任务描述 :02/:32 与实际不符，已在模板按实际落字）。
- 回归：守卫用例 5 条（心跳新鲜跳拍零 commit+在制品原样 / 心跳过期照常 commit / platform 实例永不拦 / CLI 路径过滤纯函数 / 进程命中端到端跳拍）+ 既有 2 个 main() 端到端用例补 `_no_ambient_procs` 隔离（环境在跑 claude/codex 会让守卫误跳拍）。

**验证**：test_vault_git_backup_gate.py 10 passed；全量回归 kdo-tools/tests + 90_control/scripts/tests = 482 passed / 0 failed（#627 后 477 + 本单净 +5）；**活体实证 01:37:27**：真实工作区含未提交在制品时直跑备份脚本 → `SKIPPED（#628 活动会话 6：wangyuyan(kimi-cli), huangyaoshi(cli), laowantong(cli), proc:claude.exe, proc:codex.exe, proc:kimi.exe）` + 零 commit + 在制品原样（git status 复核）。

**边界**：①fail-open 口径——注册表/进程查询失败不拦备份（真活动会话仍有另一信号兜底）；②hermes 网关常驻排除（Services ×6 实证，计入=永久跳拍），hermes 无头实例靠注册表心跳信号覆盖，长静默 turn（>20min 无 kdo 命令）为残余敞口；③conveyor probe 第十信号未认 SKIPPED 行——若活动会话长驻致 24h 零 backup commit 会报停拍（建议另立让探针认 SKIPPED）；④**发现（重要）**：01:38:12 出现非节拍 backup commit（545bd0f5a，系统任务上次运行实证 1:20/下次 1:50 未触发），把本单 3 文件 + wangyuyan 会话归档等 28 文件整体收走——即 00:32 型事故在守卫落盘后仍由**旧代码路径**复现一次（工作内容安全：已核 HEAD 三文件=最终版，全量回归 482 passed 于其上通过）；触发源未锁定，schtasks XML 单触发、config.toml/会话目录无 cron 定义、headless 日志无痕迹，疑为 #607 未迁移尽的会话级 cron 残留——本单范围外，建议另立排查（含 conveyor probe 加「非节拍 backup commit 检测」信号）；⑤任务描述节拍 :02/:32 与实际 :20/:50 不符（已按实际落字模板）。

**存在性核查**（#433 锚点，负向断言逐一实证）：①「系统任务未触发 01:38」= schtasks //query 两次实证 上次 1:20/下次 1:50 + XML 单触发 StartBoundary 07:20 PT30M ✓；②「config.toml/会话目录无 cron 定义」= grep -rln "vault backup" ~/.kimi-code/（config.toml + sessions）仅 1 个 bash 任务转写命中（本会话 grep 自身），无调度定义 ✓；③「kimi-desktop 零误报」= 实测 4 个 kimi-desktop 进程在跑，守卫 SKIPPED 行仅报 proc:kimi.exe×1（真 CLI）✓；④「HEAD 三文件=最终版」= git diff HEAD 空 + 新符号计数核 ✓。

**需要谁动作**：欧阳锋终审本单；王语嫣——「01:38 非节拍 backup commit 源排查」建议已入诊断通道（或直接另立任务）；老朱——无。本单无素材处置动作。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）


## 终审记录（2026-09-03 欧阳锋 · PASS A- · methodology v2.3）

**Verdict**：PASS，等级 **A-**。

**验收要点（对照任务书三任务逐条成立）**：
- ✅ **机制层入仓**：`git show HEAD` 三交付文件（kdo-tools/vault_git_backup.py / kdo-tools/tests/test_vault_git_backup_gate.py / 90_control/scripts/kimi-headless-launch.py）全在 HEAD；`active_sessions()` 双信号 OR（role_registry 非 platform 实例心跳 ≤20min 逐实例判 + wmic CLI 进程路径特征过滤 kimi/claude/codex），`main()` 在 git add -A 前判活动会话、命中即 SKIPPED 留痕 rc=0。
- ✅ **纪律层落字**：kimi-headless-launch.py PROMPT_TEMPLATE L65 新增「备份避让（#628）」行，节拍按实况落 :20/:50（与 schtasks 实证一致）。
- ✅ **独立复跑**：`python -m pytest kdo-tools/tests/test_vault_git_backup_gate.py -q` = **10 passed**（5 条 #625 大文件门禁 + 5 条 #628 守卫：心跳新鲜跳拍零 commit+在制品原样 / 心跳过期照常 commit / platform 永不拦 / CLI 路径纯函数 / 进程命中端到端跳拍）。
- ✅ **活体实证**：logs/vault-git-backup.log 尾行 01:50:00 `SKIPPED（#628 活动会话 7：…）` rc=0；schtasks /query kdo-vault-git-backup = Start 07:20 / Repeat 30min / Last Run 01:50 Result 0 / Next Run 02:20，全部对源。
- ✅ **存在性核查逐条复核**（#433 负向闭环）：
  - ①「01:38 孤儿 commit 非系统任务」= schtasks 上次 1:20/下次 1:50 + XML 单触发 PT30M ✓
  - ②「config.toml/会话目录无 cron 定义」= 执行报告 grep 口径自洽；我抽验 git log 自 01:00 起孤儿 backup commit 约每 10min 仍续（与建议书 diag_20260903_huangyaoshi-backup-orphan-source 一致，源排查已在诊断通道）✓
  - ③「kimi-desktop 零误报」= SKIPPED 行只报 proc:kimi.exe，无 kimi-desktop GUI 路径 ✓
  - ④「HEAD 三文件=最终版」= `git diff HEAD` 三文件为空 + `git grep HEAD` 见 active_sessions/SKIPPED/#628 符号 ✓

**五维评分**：溯源完整 92 / 逻辑骨架 90 / 暗知识密度 90 / 可操作性 92 / 表达质量 90。

**边界项（均非阻塞，落点已就位）**：
- 🟡 **孤儿 backup 源**（非节拍、约每 10min 一次，旧代码路径仍扫走在制品）——已写建议书 `60_feedback/diagnosis/diag_20260903_huangyaoshi-backup-orphan-source.md`（status: proposed），落点=待王语嫣另立排查（含 conveyor_probe 加非节拍 backup commit 检测信号）；本单范围外，不影响本单验收。
- 🟡 **conveyor probe 第十信号不认 SKIPPED**（活动会话长驻致 24h 零 backup commit 会报停拍）——落点同建议书方向③（SKIPPED 行接第十信号），待王语嫣另立。
- 🟡 **fail-open 取舍 + hermes 无头长静默 turn（>20min）残余敞口**——设计内取舍，已在任务书边界声明，落点=后续演进（建议书通道已挂号）。

**残余风险**：无阻塞项；三处 🟡 均已注明去向（孤儿源建议书 + 待王语嫣另立），F-036 闭环。