---
id: task_20260906_huangyaoshi-card-status-flip
title: "终审 PASS 后卡 status 自动翻转机制（#666 批 7 张+business-cognition-system 停留 draft 实证——检索降权复现根因）"
seq: 670
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 老顽童 #668 执行报告边界节发现（终审 PASS 但卡状态未翻转→检索降权复现机制）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T01:50:00+08:00'
---

# #670 卡 status 翻转机制（黄药师）

## 实证
#666 终审 PASS A- 后，框架批 10 卡中 7 张+`framework-ai-business-cognition-system` 仍停留 `status: draft`+`reviewed_by: 待审`——检索 trust 降权（复现「挖出来了但卡在半路」的检索失明机制）。此前靠欧阳锋手工 review_mark.py 收口（#656/#666 先例）——人肉补丁非机制。

## 修法
review 流转（queue_transition review）钩子化：终审 PASS 时按任务单交付物清单自动翻转卡 status（draft→reviewed+reviewed_by+review_date），或提供 review_mark.py 批量收口的规范调用点进终审 SOP。

## 验收
模拟终审 PASS→卡 status 自动翻转实证；存量 8 张停留卡批量收口；回归不红。
