---
id: diag_20260824_fengqingyang-daily-audit-round
title: 建议书：风清扬审计「每日一轮」定时化（抽数脚本 + 判断层节奏化）
type: proposal
status: pending_orchestration
author: 风清扬
audience: 王语嫣
date: 2026-08-24
---

# 一、结论先行

- 现状：L1 采集已 30min 定时（kdo-l1-capture）；但风清扬的 L2 审计（洞察/资产/建议）目前按需触发，无定时。
- 目标：L2 审计每日定一轮——「脚本定时抽数（零 token）」+「风清扬每日一审（判断）」。
- 分工：抽数脚本 + scheduled task 归黄药师；审计判断层归风清扬；老朱一句话触发风清扬审（暂不 headless）。

# 二、现状（实测）

- 已有定时：kdo-l1-capture（30min）、kdo-health-daily、kdo-conveyor-probe、kdo-inbox-watch。
- 缺失：无「风清扬审计」相关定时任务；审计仅靠老朱口头发起。

# 三、方案：每日审计轮（两段）

## 段① 定时抽数（黄药师，脚本，零 LLM token）

新建 `daily-audit-digest.py`（kdo-tools），每天定时一次（06:00，老朱已拍板），聚合四样原料落一份 digest：
1. 胶囊事件增量：`activity_log.db` 自上次审计以来的新事件；
2. 各角色 daily-context：当日/最新文件清单 + 差异摘要；
3. friction-log：新增行；
4. production-queue：状态变更（领单/提审/终审/新立项）。

落盘：`D:\KDO-memory\L2-digest\YYYY-MM-DD.md`（D 盘，与 L1-full/L1-backup 同区；不落 60_feedback/diagnosis，避免王语嫣误扫成建议书）。

挂 scheduled task：`kdo-daily-audit-digest`（每日一次，Ready 态，失败可见 stderr 不静默，沿用 #471/#434 口径）。

## 段② 风清扬审（判断层，每日一轮）

风清扬读 digest + L1 原文 → 产审计建议书（今日形态见 `diag_20260824_fengqingyang-capsule-audit-08-24.md`），交王语嫣。

# 四、触发方式（先不 headless）

- 抽数（段①）全自动定时。
- 风清扬审（段②）由老朱每日一句话触发（或固定时间喊）——**暂不 headless 跑 Codex**，理由：L2 是判断层需在场；headless 自动会稳定烧 token（老朱 08-24 已关注 token）。

# 五、已拍板（老朱 08-24）

- 抽数锚点时间：**06:00**（覆盖凌晨场；每日 06:00 抽数，风清扬白天审）。

# 六、验收标准

- `daily-audit-digest.py` 跑通，产出含四样原料且增量正确（不重不漏）。
- `kdo-daily-audit-digest` scheduled task Ready，失败有可见日志。
- 风清扬能只读 digest 快速出审（不再翻全量），且不额外烧 LLM token。

# 七、建议汇总

| # | 动作 | 对象 | 优先级 |
|:--|:--|:--|:--|
| 1 | 建 daily-audit-digest.py + 定时任务 | 黄药师 | P1 |
| 2 | 抽数锚点时间 06:00 | 已拍板（老朱 08-24） | P1 |
| 3 | 风清扬每日一轮审（老朱触发） | 风清扬 | P1 |