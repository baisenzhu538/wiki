---
id: diag_20260907_ouyangfeng-bundle-bat-branch-structure
title: wiki-bundle-backup.bat `:daily_only` fall-through 结构双问题——周一误导读日志行 + obsidian 快照仅周一执行（#673 终审发现）
type: diagnosis
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: '2026-09-07'
---

# 建议书：wiki-bundle-backup.bat `:daily_only` fall-through 结构的两个连带问题

## 现象一句话
bat 的 `if /i not "%WD%"=="Monday" goto :daily_only` 让 `:daily_only` 标签同时承担「非周一跳转点」和「周一 fall-through 清理点」两个角色，产生两个连带问题：①周一产完 bundle 后仍无条件 echo「skip: not Monday, full bundle skipped」误导读日志；②obsidian 快照代码位于标签之前的周一分支内，实际仅周一执行，与头注释「Obsidian snapshot 仍每日跑」不符（08-31 事故的 .obsidian 盲点修复被周节拍静默削弱）。

## 在哪发现
#673 终审独立读 bat 源码 + daily.log 实证：09-07 周一 line 143 `OK bundle=...20260907.bundle` 之后 line 145 紧跟 `skip: not Monday, full bundle skipped`；`OK .obsidian snapshot updated` 仅出现在 09-03/09-05(手动日拍)/09-07(周一) 行，非周一 09-06 无该行。

## 建议方向
1. skip echo 移入非周一专属分支（或拆分周一/非周一两条路径、标签改名），消除周一误导行——该行污染判读口径①（「周一产 bundle」与同日「skip」行并存，未来 triage 易误读）。
2. obsidian 快照日拍恢复或头注释对齐（二选一），涉备份拓扑，归老朱拍板（黄药师已在其 #673 边界① 标「不擅自改」）。

## 边界
非阻断：两项均为 bat 分支结构/日志口径问题，不影响 bundle 本身完整性（bundle create+verify 在周一分支内正常，09-07 已实测 PASS）；#673 已 PASS，本建议书为后续加固立项依据。