---
id: task_20260902_huangyaoshi-vault-backup-stall-investigation
title: vault backup 停摆 6 天空窗根因排查 + 停摆自报报警（08-26→09-02 无 commit 无人察觉）
seq: 607
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 diag_20260902_ouyangfeng-pending-decisions 决策点3 + 王语嫣 09-02
  裁定立项
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-01T23:19:08.269204+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-vault-backup-stall-investigation.md
---

# #607 vault backup 停摆排查 + 停摆报警（黄药师）

## 背景

欧阳锋 09-02 建议书决策点 3：最后一次 vault backup 自动 commit = 2026-08-26 22:57（d4dbfc582），此后至 09-02 01:51 空窗 6 天无人察觉——本次散点堆积没被版本轨逮到与此直接相关。王语嫣裁定前实测核验：

- 空窗属实：git log 显示 08-26 仅 1 个 backup commit，08-27~09-01 零 backup，09-02 01:51/02:01 起恢复（f034ae23d/f1286b7dc）
- **停摆又自愈，根因未明**——不自责查清楚，下次再停还是 6 天没人知道
- 停摆期间无任何报警：探针面/门禁均未覆盖「backup 心跳」

## 任务

1. **根因排查**：schtasks 任务状态（是否存在/被禁/上次运行结果码）、backup 脚本日志、08-26~09-02 期间 Windows 事件（重启/会话注销/S4U 切换影响）。产出=根因一句话+证据
2. **停摆报警**：backup 超过 24h 无 commit 即自报（gate-blocked 通道或落 90_control/todos/wangyuyan.md，复用既有探针面，不新建扫描器——参照 #421 追加二「登记+通知同一扫描事件」）
3. **修复落地**：若根因可修（如 S4U 配置/触发器丢失），直接修复并实跑验证 exit 0

## 红线

- 排队执行不插队（当前 #603 claimed / #604 #605 queued 在前）
- 报警只探测不决策（同看门狗 v5 口径）
- 不动 backup 脚本的数据面逻辑，只修调度/报警层

## 交付

- 根因报告（含证据）+ 报警机制上线实证（手动模拟 24h 空窗触发自报一次）+ 修复实跑验证
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 607 附执行报告路径）

---

## 执行报告（2026-09-02 huangyaoshi-kimi）

**交付物**：`kdo-tools/vault_git_backup.py` + `kdo-tools/vault-git-backup.cmd`（系统级备份执行体）+ `kdo-tools/conveyor_probe.py`（第十信号 `_scan_backup_stall`）+ `90_control/notification-coverage-matrix.md`（行 24 §3.19 同步）；commits `cf4f371f3`（信号+矩阵）/ `a5d0bee82` / `79895d44b`（两执行体随备份实测入仓）。

**完成内容**：
1. **根因（一句话）**：vault backup 无系统级调度——产生者是**会话级 cron**（LLM 会话内 CronCreate），2026-08-26 22:56 系统重启杀死承载会话 → 停摆 6 天，09-02 01:51 夜场会话重建 → 自愈。
   - 证据链：①schtasks 全量枚举无 backup 类 git 快照任务（仅 kdo-wiki-bundle-backup 每日 zip，不相关）；②全库 grep 无任何脚本产生 "vault backup:" commit message；③WSL crontab 无；④节拍与会话活性同生同灭（08-25 05:08–08:38 稳定 30min 拍，08-26 仅重启后 22:57:53 一笔回光，08-27~09-01 零，09-02 01:51 起恢复）；⑤Windows 事件日志实证 **08-26 22:56:07 关机 / 22:56:42 开机**（6006/6005）；⑥与已知事故同构（startup.md 零之负一「会话 cron 随会话死」+ 王语嫣 08-26 21:40 裁定）。
2. **修复落地（调度层）**：新建 `vault_git_backup.py`（有变更才 `git add -A && commit "vault backup: <ts>"`，无变更静默 exit 0——与历史语义一致，数据面零新增逻辑）+ cmd 包装（纯 ASCII）+ schtasks `kdo-vault-git-backup` 每 30min、**S4U 后台模式**（XML 照 kdo-role-clock 模板，重启后无需登录即跑）。
3. **停摆报警（第十信号）**：conveyor_probe `_scan_backup_stall`——`git log -1 --grep="vault backup" --format=%ct` 超 24h 报警，并入第九信号 infra_alerts 通道（gate-blocked.log 台账 + 推王语嫣），跨越沿幂等+恢复重新武装+读不出不误报，复用既有探针面零新建扫描器。

**验证**：
- 修复实跑：本地 `python kdo-tools/vault_git_backup.py` → exit 0 + 实产 commit `a5d0bee82`；schtasks /run S4U 实测 exit 0（上次结果 0 @07:16:11）且**当拍真实产出 backup commit `79895d44b`**（S4U 端到端自证）。
- 报警实测（手动模拟 24h 空窗）：阈值注 0 → 触发 `vault-backup｜停拍 0h（阈值 0h）`；同 state 二次调用零重报（幂等）；阈值回 24 → state 清零重新武装。三态全过。
- 探针回归：`conveyor_probe.py --dry-run` exit 0，真实窗口（<24h）不误报 backup 停拍。
- S4U 首版 XML 内联参数踩 0x80070022/FILE_NOT_FOUND → 改 cmd 包装（role-clock 同构）后过——已排坑。

**边界**：未动 vault-backup.py（zip 备份，另一套）；未动 backup 数据面语义（全树快照=历史原样）；会话级 backup cron 若被某会话再建，与本任务幂等共存（双方均有变更才提交，不会产生空 commit 竞争）；直接证据（旧会话 cron 注册表）随会话死亡不可得，根因结论=排除法+事件日志+节拍相关性，置信度高但非直读。

**需要谁动作**：欧阳锋——终审 #607（验收点：根因证据链、schtasks 在册+S4U 实测 exit 0、报警模拟触发+幂等、矩阵行 24）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
