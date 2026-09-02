---
id: task_20260902_huangyaoshi-gate-suite-fixes
title: 门禁顺手套件双修：F-036 否定句 emoji 误伤豁免 + review 通过时交付卡转正提醒
seq: 612
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋两份最小建议书（f036-gate-negation-false-positive + review-mark-missed-recurrence）09-02
  王语嫣裁定并单
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T01:23:46.025691+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-gate-suite-fixes.md
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

## 执行报告

**交付物**：`90_control/scripts/queue_gate.py`（F-036 否定豁免）、`90_control/scripts/queue_transition.py`（review pass 转正提醒）、`90_control/scripts/tests/test_gate_suite_fixes_612.py`（回归用例 9 条）、`90_control/notification-coverage-matrix.md`（§3.19 同步：行 3/行 7）

**完成内容**：①F-036 落点门禁加否定语境豁免——`check_issue_disposition` 判定前用 `_NEGATION_EMOJI_RE` 剔除「不落/不构成/不算/不标/不判/不记/不涉及/没有/无/非」紧邻前挂的 emoji（🟠/🟡 连写对共享否定），报错文案同步加否定句写法提示（欧阳锋口径两条腿都落）；②`action_review` verdict=pass 分支新增 `_review_card_mark_reminder`——执行报告「交付物」节含 30_wiki/*.md 时输出「N 张交付卡待 review_mark 转正」提醒（复用 `_extract_deliverable_paths`，只提醒不代写 frontmatter）

**验证**：`python -m pytest 90_control/scripts/tests/test_gate_suite_fixes_612.py -q` → 9 passed（否定放行×3「不落/不构成/无」+真问题无落点仍拦+落点词放行不回归+否定词不紧邻不误豁免；提醒输出 2 卡命中/无 30_wiki 空串/无执行报告空串）；全套 `pytest 90_control/scripts/tests/` → 214 passed 无回归；`import queue_gate/queue_transition/conveyor_probe` 冒烟通过

**边界**：选型理由——豁免+文案提示双落而非只加文案：豁免改动仅一个正则+sub 调用，成本低且直接消灭误伤（#608 连拦两轮类案），文案提示兜底豁免词表外的否定写法；否定词表有意收窄为 10 个明确否定词且要求紧邻 emoji，「暂无落点：🟠」类不误豁免（回归用例锁定）；自动转正不做（权限边界，任务单原口径）；不动状态机、不动 conveyor_probe（共用函数自动生效）

**需要谁动作**：欧阳锋终审（重点看豁免词表口径是否过宽/过窄）；转正提醒的消费端是终审通过后的生产方，提醒文案已注明需手动回填

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
