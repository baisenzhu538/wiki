---
id: task_20260903_huangyaoshi-backup-worktree-collision-guard
title: vault backup × agent 在制品互撞防护：备份前活动会话检测（#607 上线后新事故面，00:32 险些丢工作实证）
seq: 628
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师建议书 diag_20260903_huangyaoshi-vault-backup-agent-worktree-collision（09-03 王语嫣裁定：纪律①立即生效+机制②立项本单）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-02T17:34:05.889695+00:00'
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
