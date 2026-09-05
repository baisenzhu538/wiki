---
id: task_20260906_huangyaoshi-inbox-subdir-autoscan
title: "watch_inbox 顶层新子目录自动纳管（SCAN_SUBDIRS 白名单外子目录不可见——AI大航海20260905 实证盲区）"
seq: 651
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（03:37 拍，#605/#619 白名单族缺口第三例）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T20:17:44.201235+00:00'
---

# #651 watch_inbox 顶层新子目录自动纳管（黄药师）

## 实证（03:37 值守拍）

- `kdo-tools/watch_inbox.py` L52：`SCAN_SUBDIRS = ("pending-cards", "wechat-collect", "video_transcripts", "video_transcripts_small")`——只扫顶层文件+四个白名单子目录
- 09-06 02:55 老朱投放 `00_inbox/AI大航海20260905/`（14 件：口述×2/笔记×2/逐字稿×1/PNG×8）→ `inbox_state.json` 0 条记录、INBOX-PENDING 0 行登记——**整个文件夹对探针不可见**，靠老朱人肉指出才发现
- 白名单族缺口第三例：#605 裁剪误伤 wechat-collect/video_transcripts（05:47 四件漏登记）→ #619 回补 → 本例=新子目录类盲区

## 修法（二选一，取稳者）

1. 顶层目录扫描：非 `_` 前缀、非 SKIP_SUBDIR_PARTS 的顶层子目录自动纳入扫描（白名单退化为「需递归深扫的目录」清单）
2. 目录级登记：顶层发现未知子目录时，至少登记一行「目录待编排」让编排者知晓（目录内文件不全扫，避免大目录爆炸）

## 验收

- 新建测试子目录（含 1 个 .md）→ 下一拍 INBOX-PENDING 出现登记行；AI大航海20260905 补登记
- 现有回归不红；_ 前缀目录与 SKIP 目录不被误扫
