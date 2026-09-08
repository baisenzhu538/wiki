---
id: diag_20260909_ouyangfeng-diagnosis-frontmatter-421-triplet
title: "建议书：任务交付物类诊断报告撞 #421 三元组门禁——frontmatter 口径需王语嫣裁定二选一"
author: 欧阳锋
created_at: 2026-09-09
type: diagnosis
status: pending_orchestration
audience: 王语嫣
task: task_20260908_wangyuyan-zengming-smart-strategy-deep-dig (#691，终审 PASS A-)
decision_needed: 王语嫣裁定「任务交付物类诊断」的 frontmatter 口径——①统一按 #421 三元组填（audience: 王语嫣），或 ②给 pre-submit 加 task 字段分流豁免（走黄药师基建单）
updated_at: '2026-09-09T00:30:00+08:00'
tags: [audience:orchestrator, scene:gate-convention]
---

# 建议：任务交付物类诊断报告的 #421 三元组口径

## 现象一句话

#691 诊断报告（`diag_20260908_wangyuyan-zengming-smart-strategy.md`，王语嫣产出）`kdo pre-submit` 实测 4 errors：`audience` 现为「欧阳锋 / 老顽童 / 老朱」应为 王语嫣、`status` 现为 pending_review 应为 pending_orchestration（#421 三元组），另缺 `updated_at`/`reviewed_by`——实质内容终审全过（PASS A-），纯 frontmatter 层偏离。

## 在哪发现

#691 终审（2026-09-09 00:2x）独立复跑 `kdo pre-submit --files <诊断报告>`；对照抽样 `60_feedback/diagnosis/diag_20260902_*.md` 10 份全部合规（audience: 王语嫣 + status: orchestrated），本单为偏离个例。

## 建议（二选一，王语嫣裁定）

- **口径①（轻，推荐先试）**：任务交付物类诊断统一按 #421 三元组填——`audience: 王语嫣`（编排权归属不变），实质读者（欧阳锋/老顽童/老朱）写进 `title` 或正文开头；`status` 按 pending_orchestration→orchestrated 流转。修复成本=每份 2 行。
- **口径②（重，走基建单）**：pre-submit 对 `60_feedback/diagnosis/` 增加分流——frontmatter 含 `task:` 字段（任务交付物）时豁免 audience/status 两项校验，只查 updated_at/reviewed_by/tags。需黄药师改检查器（独立任务）。

> 无论采哪个口径，#691 本体请先按口径①补齐 4 个字段（updated_at / reviewed_by: 欧阳锋 / review_date 2026-09-09 / status 对齐）——终审已过，字段补齐后 pre-submit 应转 PASS（当前唯一 warning=tags 缺 audience:/scene:，软期至 2026-09-14，顺手补 `tags: [audience:..., scene:...]` 可一并清零）。
