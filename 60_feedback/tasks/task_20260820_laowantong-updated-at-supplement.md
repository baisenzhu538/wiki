---
id: 394
assignee: hermes
status: in_progress
title: 缺 updated_at 补充清单 25 张（P3，#391 终审另立项）：5 月 yt-* 22 张 + rust-* 3 张——#391 扫描口径漏网
priority: P3
dependency: []
updated_at: '2026-08-20T10:43:06.766087+00:00'
---

# #394 缺 updated_at 补充清单 25 张

## 来源

#391 终审（PASS A-）欧阳锋独立全库复扫发现：**缺 updated_at 实际 41 张（非 16）**——#388/#391 扫描口径漏 25 张：5 月 yt-* 卡 22 张 + rust-* 3 张（如 yt-entrepreneur-barriers created_at 2026-05-06 实证缺）。

**口径教训（欧阳锋原话）**："全量复扫归零"声明为清单范围归零，非全库——本单验收用**全库口径**。

## 任务目标

25 张补 updated_at，全库缺 updated_at **真归零**。

## 执行范围

1. 欧阳锋复审发现的 25 张清单为基础，**但先自己全库重扫**（不照抄清单——他的扫描也可能有时差），实扫数与 25 有出入以实扫为准并报告差异
2. 每张补 `updated_at: '2026-08-20'`（同 #385/#388/#391 模式），只加这一个字段
3. 修复后**全库复扫**确认缺 updated_at = 0（E017：修复了≠清干净了，且这次是全库口径）

## 边界

- 只动 frontmatter updated_at 字段，正文零改动
- 批量三问（dry-run 清单贴报告）
- 完成后 commit 入档（E040）
- 欧阳锋随下批 spot-check 复终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅元数据机械修正，无删除/移动

## 验收标准

1. 全库缺 updated_at = 0（全库口径复扫，非清单口径）
2. pre-submit 0 ERROR
3. 实扫数 vs 25 的差异说明（如有）

## 交付

1. dry-run 清单 + diff 统计 + 全库复扫证据
2. 送欧阳锋终审（随下批 spot-check）
