---
id: diag_20260825_fengqingyang-automation-cost-audit
title: 审计：时钟与自动化工作流消耗评估（脚本层零 token 设计正确；LLM 层 token 无计量=消耗管理缺口）
type: proposal
status: pending_orchestration
author: 风清扬（观察者 / 审计者）
audience: 王语嫣
date: 2026-08-25
---

# 时钟与自动化工作流消耗评估

> 触发：老朱 08-25 令「评估时钟的消耗，评估自动化工作流的消耗」。
> 口径：建议稿，待王语嫣裁决（charter §3.18）。消耗分两层评：时钟脚本层（可实测）与 LLM 会话层（有工作量数、无 token 计量）。

## 一、结论先行

1. **时钟脚本层消耗可忽略，设计正确**：7 个定时任务全是零 LLM token 的 Python 脚本，日执行约 340 次，单次秒级；磁盘增量实测约 26MB/天（归档改造后活跃层稳态 121MB）。**「抽数/巡检机器化、判断留在会话层」的路线在成本上成立**。
2. **LLM 会话层是消耗主体，但全厂无 token 计量**——工作量有数（今日 50+ 事件、黄药师约 10 单全链、欧阳锋 29 场终审、王语嫣 6+ 裁定），**token 消耗无数据源**（统一同一执行引擎后，旧工具的 usage 记录链路已随采集面重构消失）。**消耗不可观测 = 无法管理**——老朱 08-24 已关注 token，此缺口直接挡在「单均成本」优化前面。
3. **建议**：建全厂 token 计量（会话级 usage 落事件层或日汇总），作为 #514 基线的第五指标「单均 token 成本」；实施归黄药师，口径我可出建议稿。

## 二、时钟脚本层（实测，零 token）

| 任务 | 频率 | 单日次数 | 性质 | 消耗 |
|:--|:--|--:|:--|:--|
| kdo-conveyor-probe | 10min | 144 | 读队列+写登记+飞书 webhook | 秒级 CPU，零 token |
| kdo-inbox-watch | 10min | 144 | 读 inbox 目录 | 秒级，零 token |
| kdo-l1-capture | 30min | 48 | 增量复制+hash+verify | 磁盘 26MB/天（改造后更低），零 token |
| kdo-daily-audit-digest | 06:00 | 1 | 聚合落 digest | 秒级，零 token |
| kdo-l1-archive | 06:00 | 1 | zip 归档+移出活跃层 | 周增约 500MB zip（D 盘），零 token |
| kdo-health-daily / KDO-Health-Check | 每日 | 2 | 9 项检查脚本 | 秒级，零 token |

**合计**：约 340 次/天脚本执行，**零 LLM token**，磁盘日增 26MB（活跃层稳态后增长主要来自 archive zip，存储成本可忽略）。

## 三、LLM 会话层（工作量有数，token 无计量）

**工作量（事件库+git 实测，08-25）**：
- 事件库 109 条（今日 +50）：review_saved 63 / queue_transition 32 / decision 11 / error 2；
- 黄药师约 10 单全链（claim→complete→review 成组，含 #511/#514 解锁后领单）；
- 欧阳锋 29 场终审（单场可多单）；
- 王语嫣 6+ 建议书裁定 + charter v1.1-v1.3 三连 + #525 立项；
- 会话原文采集：今日 kimi 源 13MB + hermes 源 16MB（采集面已收敛为两源，去工具化生效）。

**token 计量缺口（实测排查）**：
- `~/.kimi/` 下无 usage/token 计量文件（仅 daimon/kimi-claw 两个目录，kimi-claw 为 IM connector 日志，375k 行中 token 均为 auth 语义非用量）；
- 旧执行引擎的 `usage_record.jsonl`/`token-usage-2026-08.jsonl` 链路已随 L1 采集面重构（归档 zip）不再更新；
- 后果：无法回答「今天烧了多少 token」「单均 token 成本」「哪个角色/环节最贵」——**阶段 2 降档（机器换人）恰以成本为动机，却没有成本基线**。

## 四、建议（待王语嫣裁决）

| # | 建议 | 对象 | 优先级 |
|:--|:--|:--|:--|
| 1 | 全厂 token 计量：会话级 usage 落事件层新事件类型（或日汇总文件），统一引擎只此一源、计量一处 | 黄药师 | P2 |
| 2 | 「单均 token 成本」纳入 #514 质量基线第五指标（口径：角色归一 token 总量 ÷ 同期完成单数，按周聚合） | 黄药师实施 + 风清扬出口径建议稿 | P2 |
| 3 | 阶段 2 降档评估时，成本对照（人工会话 vs 机器预审）以计量数据为准，不凭感觉 | 王语嫣（届时引用） | P3 |

## 五、边界声明

- 本件为审计建议稿（charter §3.18），audience 唯一=王语嫣；消耗数字均为实测/可算，token 缺口为排查实录（负向断言附排查路径，非凭印象）。

---

*风清扬（观察者 / 审计者）· 2026-08-25 · 只审计、不实施、不催复盘*
