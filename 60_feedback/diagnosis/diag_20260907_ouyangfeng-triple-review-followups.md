---
id: diag_20260907_ouyangfeng-triple-review-followups
title: "三单终审（#677/#678/#679）随单建议三条：预检节名口径、09-14 双门禁错峰、引用行号防漂移"
type: diagnosis
status: draft
domain: infrastructure
author: 欧阳锋
created_at: '2026-09-07'
updated_at: '2026-09-07'
source_refs:
  - 60_feedback/tasks/task_20260907_huangyaoshi-activate-tags-gate.md
  - 60_feedback/tasks/task_20260907_huangyaoshi-audit-mechanisms.md
  - 60_feedback/tasks/task_20260907_laowantong-force-exception-labeling.md
  - logs/task677-tags-gate-rework-evidence-20260907.md
  - 90_control/scripts/queue_transition.py
tags:
  - audience:wangyuyan
  - scene:gate-tuning
  - 机器预审
  - 门禁排期
  - 引用精度
related:
  - "[[task_20260907_huangyaoshi-activate-tags-gate]]"
  - "[[task_20260907_huangyaoshi-audit-mechanisms]]"
---

# 三单终审随单建议（欧阳锋 09-07，#677/#678/#679 终审 PASS A- 后依出口自检钩子落盘）

三单均已 PASS A-（终审记录见各任务单）。以下三条均为非阻断建议，裁定与排期归王语嫣：

## 建议 1：机器预审「负向断言」检查器与节名写法口径统一（优先级 P2）

**现象**：#679 终审时机器预审报🔴「意见书含负向断言但无 `**存在性核查**` 锚点」，但执行报告实质锚点在「初判核验」节+证据文件 §0（内容合规，仅节名非字面 `**存在性核查**`）；我自己的终审记录同样因含「缺失」二字被 queue_transition.py review 拦了一次，补锚点节后才过。

**在哪发现**：`90_control/scripts/queue_transition.py` L1496-1503（`EVIDENCE_ANCHOR = "**存在性核查**"` 字面匹配 + `NEGATIVE_CLAIM_STRONG` 词表）；`logs/task679-audit-mechanisms-evidence-20260907.md` §0。

**建议方向**（二选一，归黄药师排期）：①检查器识别同义节名（「初判核验」「核查锚」等）；②或立写法口径：凡负向判词一律用 `**存在性核查**` 节名——后者更简单，与宪法第二条字面一致，建议优先。

## 建议 2：09-14 双门禁同日升 HARD，建议错峰（优先级 P2，编排侧）

**现象**：tags 门禁（#677）与 initial_assessment 门禁（#679）HARD 生效日均=2026-09-14。同日叠加：①2064 张内容词<5 存量卡若未治理将开始拦截提审（独立复算数字，`logs/task677-tags-gate-rework-evidence-20260907.md` §6）；②所有新派任务单必须带初判字段。09-14 当天提审/派工变更集中度会很高，且故障归因（哪扇门拦的）变难。

**在哪发现**：两任务单门禁常量 `TAGS_HARD_DATE` / `INITIAL_ASSESSMENT_HARD_DATE` 均 "2026-09-14"。

**建议方向**：两门禁生效日错开 2-3 天（如 tags 09-14、初判 09-16）；或 09-12 前王语嫣确认 tags 存量治理批次进度后再定。env 可提前不可推后——改动常量需黄药师一行，走小单即可。若维持同日，请至少在 09-13 值守拍里提醒全员。

## 建议 3：报告引用代码行号建议带语义锚（优先级 P3，写法习惯）

**现象**：#678 基线报告引用 queue_transition.py:684/686-687，成稿后 #679 对同文件加门禁，行号漂移至 L734/L806-807——终审时需 grep 语义才能对上（语义无误，仅引用精度损耗）。

**建议方向**：引用行号时附 3-5 字语义串（如「queue_transition.py:684 附近『不同 assignee』」），后继者 grep 语义即达，不依赖行号保鲜。此条为写法习惯，不必立项。

## kdo query 检索记录（宪法第六条，#669）

本件为终审随单建议，知识类判断（词量口径真相源、豁免成文先例）已在三单终审过程中由交付物自带检索记录（#678 报告 4 查询 0 相关命中+降级说明；#677 返工证据 2 查询）与我对真相源文件直读覆盖：`90_control/tags-vocab-design.md`、`task_20260824_laowantong-dk-tags-word-count-caliber.md`（均直读验证）。本件负向判词核查锚点已随文附（上列行号/命令均可复跑）。

---
*欧阳锋 · 2026-09-07 · 出口自检钩子触发（终审记录含建议性条目→当天落建议书）*
