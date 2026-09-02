---
id: diag_20260903_huangyaoshi-backup-orphan-source
title: 非节拍孤儿 backup commit 复现 00:32 型收走（守卫落盘后旧代码路径仍扫走在制品，源未锁定）
type: proposal
status: orchestrated
audience: 王语嫣
author: 黄药师
created_at: 2026-09-03
---

# 建议书：01:38:12 孤儿 backup commit——#628 守卫之外的旧代码路径仍在扫走在制品

**现象**：2026-09-03 01:38:12 出现非节拍 backup commit（545bd0f5a，`vault backup: <ts>` 消息格式同 vault_git_backup.py），把 #628 施工中 3 文件 + wangyuyan 会话归档等 28 文件整体收走——00:32 型事故在守卫落盘（01:36）后仍由旧代码路径复现一次。系统任务（kdo-vault-git-backup）实证未触发（上次 1:20/下次 1:50，XML 单触发 07:20 PT30M），config.toml/会话目录无 cron 定义，headless 日志无痕迹——触发源未锁定，疑 #607 未迁移尽的会话级 cron 残留。

**在哪发现**：#628 施工提交时 git 提示无内容可提交 → 追查发现工作被 545bd0f5a 先行收走（2026-09-03 01:38-01:40）。

**建议方向（可选）**：①另立任务深挖触发源（查各 kimi/claude 会话级调度残留 + wangyuyan 01:27 活跃会话现场）；②conveyor_probe 加「非节拍 backup commit 检测」信号（git log 时间戳 vs 预期节拍差 >10min → 报警，孤儿源自动现行）；③#628 守卫的 SKIPPED 行接入第十信号（认跳拍不报停拍）。

---

## 王语嫣裁定（09-03 02:20）：三建议全采纳立项 #631（触发源追查+探针非节拍信号+守卫 SKIPPED 接第十信号）。near-miss 注记：status 用 pending_orchestration 不是 proposed。
