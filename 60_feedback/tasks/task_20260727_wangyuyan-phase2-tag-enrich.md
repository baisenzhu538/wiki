---
id: task_20260727_wangyuyan-phase2-tag-enrich
task_id: 211
assignee: laowantong
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-07-27
created_at: 2026-07-27
domain: system
priority: P1
source: 60_feedback/diagnosis/diag_20260726_huangyaoshi-tag-system-phase2-3.md (黄药师Phase
  2建议书)
updated_at: '2026-07-26T17:32:58.913652+00:00'
---

# Phase 2：高价值卡人工精标

## 目标

前50张高价值卡标上5个关键维度，让外部Agent只看tags就能判断"这张卡我能用吗"。

## 最少标签集（5维）

| 维度 | 作用 | 示例 |
|:--|:--|:--|
| method | 什么方法论家族？ | decision-framework / thinking-tool / collaboration |
| scene | 什么时候用？ | diagnose / execute / reference |
| audience | 给谁用的？ | ceo / designer / builder |
| content-format | 产出什么？ | checklist / canvas / framework / case-study |
| source-person | 谁的方法论？ | Truman / 月白 / 半肥猫 / 老朱 |

## 标准

小昭搜"CEO怎么设计分钱规则"→返回5张卡→只看tags不需要kdo_read→选对→够了。

## 标的优先级

| 优先级 | 对象 | 数量 | 需标维度 |
|:--|:--|:--:|:--|
| P0 | framework卡 | ~30张 | **5维全标** |
| P0 | domain-digest/MOC卡 | ~10张 | **5维全标** |
| P0 | agent-spec卡 | 8张 | **5维全标** |
| P1 | 新域首卡（近30天） | ~15张 | **5维全标** |

## 执行

- 不批量返工——该卡因其他原因返工时顺手加
- 王语嫣新任务单加"建议标签"列（已在#206规范中）
- 4周自然覆盖，达标(>80%)后激活Phase 3 lint门禁

## 执行记录（2026-07-27 Batch 1 · 精标修订版）

| # | 卡片 | 标签（逗号分隔） |
|:--|:--|:--|
| 1 | tool-private-board-facilitation-sop | peer-advisory, meeting-facilitation, structured-meeting, run-meeting, meeting-host, checklist, 徐里 |
| 2 | case-wangfei-newyear-event-diagnosis | five-step-diagnosis, business-review, business-owner, case-study, 王非 |
| 3 | dk-sponsor-three-tier-pricing | sponsorship-pricing, event-monetization, pricing-strategy, monetize-event, business-owner, playbook, 罗意 |
| 4 | framework-kdo-modeling-methodology | kdo-modeling, knowledge-engineering, component-extraction, build-knowledge-system, knowledge-engineer, framework, 黄药师 |
| 5 | framework-yitang-shishi-qiushi | evidence-based-decision, reality-check, assumption-validation, decision-check, decision-maker, framework, Truman |
| 6 | framework-yitang-thought-liberation-lightning | structured-innovation, four-step-method, hypothesis-driven, generate-ideas, decision-maker, framework, Truman |
| 7 | framework-kdo-self-attack | adversarial-testing, red-team, pre-mortem, pre-ship-review, knowledge-engineer, framework, 王语嫣 |
| 8 | framework-ai-accelerated-strategy-cycle | ai-strategy, acceleration, strategic-analysis, plan-cycle, decision-maker, framework, Truman |

**原则：method 从「学术分类」改为「用户会怎么搜」。** 例如 `epistemology→evidence-based-decision+reality-check+assumption-validation`。Agent 搜「怎么判断对不对」命中 reality-check，不会搜 epistemology。

| | #207 P3长程 | #211 Phase 2精标 |
|:--|:--|:--|
| 范围 | 全部存量卡 | 前50张高价值卡 |
| 触发 | 碎片时间 | 该卡返工时顺手 |
| 维度 | 补齐基础标签 | method+industry+value-tier |
| 目标 | 消灭null | Agent只看tags可判断 |
