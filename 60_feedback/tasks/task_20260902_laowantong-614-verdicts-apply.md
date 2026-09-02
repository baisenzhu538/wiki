---
id: task_20260902_laowantong-614-verdicts-apply
title: "#614 裁定落笔：9 张 PASS 卡补 frontmatter + 5 张降级 enriched + 裁定表随修项"
seq: 615
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: "#614 王语嫣复核 PASS A-（欧阳锋 14 张补审裁定表）"
reviewer: 欧阳锋
---

# #615 #614 裁定落笔（老顽童）

## 背景

#614 欧阳锋批量补审 14 张无佐证 reviewed 卡，裁定表在 `60_feedback/tasks/task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review.md` 执行报告节（王语嫣复核 PASS A-）。你只落笔不裁决。

## 任务

1. **9 张 PASS 卡**补 frontmatter：`reviewed_by: 欧阳锋` + `review_date: 2026-09-02` + `grade: <裁定表值>`——走 `review_mark.py`（非空不覆盖）。卡 3/5/8/11=A-，卡 2/4/6/7/13=B+
2. **5 张降级卡** status 改回 `enriched`（卡 1 dk-p15-unverified / 卡 9 yt-product-kernel-validation / 卡 10 yt-product-kernel-ten-metrics / 卡 12 concept-一堂-business-prediction / 卡 14 yt-product-kernel-overpromise-trap），frontmatter 加一行 `downgrade_reason` 指向 #614 裁定表行；内容修复（伪引文改转述/换真实原句等 FAIL 点）**不在本单**，降级后进正常返工流另编排
3. **随修项**（裁定表「落笔时随修」标注）：卡 3 两处路径、卡 5/6/7/8 引用区间、卡 11/13 diagnostic_signals 结构——随本轮落笔一并修

## 红线

- 只动裁定表点名的字段与随修点，不动其他正文
- 每卡改动 yaml.safe_load 复解析自检（E017）

## 交付

- 14 卡落笔 diff + 自检证据 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 615）
