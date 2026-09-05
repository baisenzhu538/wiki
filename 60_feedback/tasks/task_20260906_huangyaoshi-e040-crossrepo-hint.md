---
id: task_20260906_huangyaoshi-e040-crossrepo-hint
title: "E040 报错提示跨仓前缀全路径（第2次复发工具化，#639 同族）"
seq: 653
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 #649 friction 03:46（第2次复发，老朱「两次复发立即工具化」口径）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T04:20:00+08:00'
---

# #653 E040 跨仓前缀提示微单（黄药师）

## 实证
#639 friction（09-04 21:45）首次：交付物节写 CLI 仓裸相对路径→门禁按 vault 相对判 untracked；#649 friction（09-06 03:46）复发：建议报错补一句「KDO 份交付物请写带仓前缀的全路径」。

## 修法
E040 报错文案：检测到疑似 KDO CLI 仓路径（Knowledge Delivery OS 0.0.1/ 前缀缺失）时，报错信息自动补提示「KDO CLI 份交付物请写带仓前缀的全路径，参照 #542 先例」。一行改动+回归。

## 验收
模拟场景复现提示出现；现有回归不红。
