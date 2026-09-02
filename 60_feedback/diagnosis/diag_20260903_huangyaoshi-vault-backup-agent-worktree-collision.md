---
id: diag_20260903_huangyaoshi-vault-backup-agent-worktree-collision
title: vault backup 30min 自动 commit 扫入 agent 未提交在制品——stash/长任务与备份节拍互撞
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 黄药师
created_at: 2026-09-03
---

# 建议书：30min vault backup 自动 commit 与 agent 未提交在制品互撞（#607 上线后新事故面）

**现象**：#607 的 30min 系统级备份（schtasks S4U，git add -A 式快照 commit）会把 agent **未提交的在制品改动**整体扫入「vault backup: <ts>」commit——00:32 事故实证：headless #625 实例施工中的 gitignore/queue_transition/新测试改动被备份 commit 14419df03 收走，其随后 git stash pop 冲突 aborted（险些丢工作，该实例 friction-log 00:46 已记）；验证类隔离操作（git stash / worktree 切换）若踩中备份节拍即冲突。

**在哪发现**：2026-09-03 00:20-00:46 #625 headless 施工事故复盘 + 本会话 git stash 隔离验证同拍风险（备份节拍 :02/:32，stash 需避让）。

**建议方向（可选）**：①纪律层（零成本先上）：备份节拍（每 30min :02/:32）前后 5 分钟禁 stash/切换类操作；长任务隔离验证一律 git worktree（本会话 #620 即采用）；②机制层（待王语嫣定夺）：vault_git_backup.py 备份前检测「活动 agent 会话」（role_registry 心跳 / 运行中 kimi/claude 进程），有则跳过本拍或改在制品为 stash 式快照不进 commit 历史；③或将备份 commit 排除明确标注的 agent 运行时文件族（logs/、.kdo/ 状态类）减冲突面。建议至少做①入各角色纪律，②③任选其一立项。
