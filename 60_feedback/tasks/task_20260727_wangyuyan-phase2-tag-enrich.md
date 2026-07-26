---
id: task_20260727_wangyuyan-phase2-tag-enrich
task_id: 211
assignee: laowantong
status: pending_review
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

## 执行记录（2026-07-27 Batch 1）

| # | 卡片 | pre-submit |
|:--|:--|:--:|
| 1 | tool-private-board-facilitation-sop | PASS |
| 2 | case-wangfei-newyear-event-diagnosis | PASS |
| 3 | dk-sponsor-three-tier-pricing | PASS |
| 4 | framework-kdo-modeling-methodology | tags added |
| 5 | framework-yitang-shishi-qiushi | tags added |
| 6 | framework-yitang-thought-liberation-lightning | tags added |
| 7 | framework-kdo-self-attack | tags added |
| 8 | framework-ai-accelerated-strategy-cycle | tags added |

**8/8 5维标齐**（method/scene/audience/content-format/source-person）。前3张 pre-submit PASS，后5张只加tags不碰正文。

| | #207 P3长程 | #211 Phase 2精标 |
|:--|:--|:--|
| 范围 | 全部存量卡 | 前50张高价值卡 |
| 触发 | 碎片时间 | 该卡返工时顺手 |
| 维度 | 补齐基础标签 | method+industry+value-tier |
| 目标 | 消灭null | Agent只看tags可判断 |
