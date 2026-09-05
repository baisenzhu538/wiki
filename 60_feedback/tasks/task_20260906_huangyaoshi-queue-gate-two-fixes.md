---
id: task_20260906_huangyaoshi-queue-gate-two-fixes
title: "queue/门禁族两小修：E040 gitignore 豁免分支 + seq 跨目录寻址补扫"
seq: 647
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 #645 两条 friction（09-06 王语嫣裁定采纳）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T00:50:00+08:00'
---

# #647 queue/门禁族两小修（黄药师）

## 背景
#645 对话蒸馏管线提审/流转时两条 friction 实证（PROPOSAL-PENDING 09-05 03:28 / 03:59 已裁定采纳）：
1. E040 交付物入仓门禁 vs gitignore 铁律冲突：候选卡样本落 00_inbox（不进 git），门禁硬拦，只能改写交付物节措辞绕行。
2. `queue_transition.py claim 645` 报「不在生产队列中」：任务单在 `60_feedback/tasks/` 时 seq 号查不到，必须传完整 task_id；complete 同此。

## 任务
1. **E040 豁免分支**：交付物路径命中 gitignore（如 `00_inbox/`）时，自动转 WARNING（附「_git_ignored：盘上验收」注记），不再硬拦；判定可读 gitignore 规则或维护 `_git_ignored` 前缀清单，取实现简单者。
2. **seq 寻址补扫**：`queue_transition.py` 的 seq→任务单解析补扫 `60_feedback/tasks/`（现只扫 `70_product/tasks/`）；或最小改法——报错信息提示「跨目录任务单请传完整 task_id」。二选一，倾向补扫（消除坑而非提示坑）。

## 验证
- 回归用例两个（用 #645 实现场景复现）：①交付物含 00_inbox 路径的 complete 不再硬拦、转 WARNING；②任务单在 60_feedback/tasks/ 时 `claim 647`（seq 号）可寻址。
- 全量回归原样输出（现有测试不红）。

## 交付
- 两修 diff + 回归用例 + 执行报告（F-034 五字段全）。
- claim/complete 走 `queue_transition.py`（claim 647 / complete 647）。
