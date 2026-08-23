---
id: diag_20260823_ouyangfeng-queue-slim-handover
title: 队列瘦身移交——首次瘦身已完成（611→131 行），后续维护归王语嫣编排域
type: proposal
author: 欧阳锋（Architect / 审查者）
created_at: 2026-08-23
status: resolved
audience: 王语嫣
---

# 队列瘦身移交（2026-08-23 欧阳锋误接任务，按边界移交）

## 背景

- 老朱 08-23 指令"看板任务定期归档瘦身"，**误发给欧阳锋**；欧阳锋执行了首次瘦身并设了每周 cron。
- 边界澄清（老朱确认误发）：**队列/看板维护=王语嫣编排域**（production-queue.md owner: 王语嫣）。欧阳锋已删除自己设的 cron，本单为移交记录。

## 已执行的首次瘦身（不可逆，历史可追溯）

- commit c2f9b505（2026-08-23 12:46）：`production-queue.md` 611→131 行（-79%）
- 归档：终态任务行 370 条 + PENDING 段划线 112 条 → `70_product/tasks/archive/production-queue-archive-20260823.md`（199KB）
- 保留：活跃行（queued 7/claimed 1/pending_review 2/blocked 1）+ 最近 10 条 reviewed + 全部分段结构标记
- 验证：`queue_transition status` 正常 + dashboard 正常

## 后续维护（王语嫣域）

- 建议触发线：队列 >450 行时执行瘦身（归档到 `archive/production-queue-archive-YYYYMMDD.md`）
- 脚本要点（踩坑 3 次的教训）：① 表头分隔行正则 `^:?-+:?$` 必须排除（否则 parse_queue 归零）② 归档后立即验证 `queue_transition.py status` + `generate-dashboard.py` ③ 终态=reviewed（保留最近 10）/done/closed_*/confirmed；活跃=queued/claimed/pending_review/blocked
- 若王语嫣需要脚本模板：可让黄药师把上述逻辑固化为 `kdo-tools/queue-slim.py`（可选项，不做也行）

## 需要谁动作

- **王语嫣**：知悉归档位置与触发线；后续瘦身归你编排（可自己执行或派黄药师工具化）
- **欧阳锋**：不再持有该定期任务（cron 已删）；context 已更正
