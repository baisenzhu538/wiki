---
id: task_20260907_huangyaoshi-bundle-bat-branch-fix
title: "wiki-bundle-backup.bat :daily_only fall-through 双问题修复（周一误导读日志+obsidian快照仅周一跑与注释不符）"
seq: 675
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋 #673 终审附带发现建议书 diag_20260907_ouyangfeng-bundle-bat-branch-structure（08-31 事故修复被周节拍静默削弱）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T21:14:57.084483+00:00'
---

# #675 bundle bat 结构双问题修复（黄药师）

## 实证（欧阳锋 #673 终审独立读 bat 源码+daily.log）
1. `:daily_only` 标签双角色：周一产完 bundle 后仍无条件 echo「skip: not Monday」误导读日志（09-07 L143→L145 实证）
2. **obsidian 快照仅周一执行**，与头注释「Obsidian snapshot 仍每日跑」不符——08-31 事故的 .obsidian 盲点修复被周节拍静默削弱（非周一 09-06 无 snapshot 行实证）

## 修法
拆分标签职责（周一全量路径/每日路径各归各）+ obsidian 快照节拍按注释意图对齐（或改注释如实声明节拍，二选一给依据）+ 日志行修正。

## 验收
周一/非周一两天模拟：日志行如实+快照行为与文档声明一致；回归不红。
