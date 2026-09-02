---
id: task_20260902_huangyaoshi-gate-suite-fixes
title: 门禁顺手套件双修：F-036 否定句 emoji 误伤豁免 + review 通过时交付卡转正提醒
seq: 612
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋两份最小建议书（f036-gate-negation-false-positive + review-mark-missed-recurrence）09-02 王语嫣裁定并单
reviewer: 欧阳锋
---

# #612 门禁顺手套件双修（黄药师）

## 任务 1：F-036 落点门禁否定句误伤

- 实证：`queue_gate.py:308` 按 emoji 字面出现判定，「不落 🟠/🟡」（声明不标记）与「落 🟠」（标记问题）同拦。#608 终审被连拦两轮，删字样才放行
- 修法（欧阳锋口径，低成本优先）：门禁报错文案加提示「否定句勿写 emoji 字样」；若改动小可加否定语境豁免（「不落/不构成/无」前挂词）。你定，执行报告写明选型理由

## 任务 2：review 通过时交付卡转正提醒

- 实证：review_mark 漏转正二次复发（#586 批 3 卡挂一天；#596 已补过一次，E018 家族 #213/#214 同源）
- 修法：`queue_transition.py review` verdict=pass 时，若任务单「交付物」含 30_wiki 卡片路径，输出一行提醒「N 张交付卡待 review_mark 转正」（提醒即可，自动转正涉及代写卡片 frontmatter 权限边界，不做）

## 红线

- 小改单点，各配一个回归用例（否定句放行案例 + 提醒输出案例）
- 不动状态机逻辑

## 交付

- 两处 diff + 回归实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 612 附证据）
