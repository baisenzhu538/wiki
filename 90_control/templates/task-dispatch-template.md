---
id: task_<YYYY-MM-DD>_<执行角色>-<slug>
title: "<一句话任务标题（含任务号 #seq）>"
seq: <队列序号>
status: queued
assignee: <角色名——文档署名单一口径，#444>
created_by: <编排角色名>
created_at: <YYYY-MM-DD>
decision_source: <谁在什么场景拍板 / 审计建议来源>
reviewer: 欧阳锋
instance: <执行角色名>
# #679 初判=待证命题（小昭审计建议 2）：派单前对「任务前提」的一句话判断 + 存在性核查锚。
# 派单前必核——前提与盘上现状不符 = 初判失真（实证 5/5 命中：黄药师 4 场 + 老顽童 #668）。
# 锚点三选一：文件:行 / git rev / grep 命中数。占位符原样提交会被 claim 门禁按缺失处理。
initial_assessment: 待证命题（附存在性核查锚）
updated_at: '<YYYY-MM-DDTHH:MM:SS+08:00>'
---

# <任务标题>（<执行角色>）

## 实证
<!-- 任务前提的现状核查，逐条附锚点（宪法第二条：负向判词必附存在性核查锚 #433） -->

## 任务
1. …

## 验收
- …

## 边界
<!-- 不做什么 / 已知限制，防终审者把已知限制当遗漏 -->

> **使用说明（编排侧王语嫣，#679）**：
> 1. 复制本模板 → 替换全部 `<>` 占位符与本注释 → 队列行入 `70_product/tasks/production-queue.md`（四件套：任务单+队列行+dashboard+commit，编排产出四件套 charter §3.2）。
> 2. `initial_assessment` 是**待证命题不是结论**：写"我判断盘上现状是 X，依据=锚点"，执行者以实证推翻或确认——执行报告须回填核验结果（证实/证伪）。
> 3. 缺字段/占位符原样的新派任务（created_at ≥ HARD 生效日，默认 2026-09-14，env `KDO_INITIAL_ASSESSMENT_HARD_DATE` 可提前）会被 claim 门禁硬拦；存量任务 WARNING 台账放行（charter §3.10：存量不回改，新格式仅对生效日后生效）。
