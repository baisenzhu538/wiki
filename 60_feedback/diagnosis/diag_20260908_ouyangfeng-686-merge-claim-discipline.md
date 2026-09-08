---
id: diag_20260908_ouyangfeng-686-merge-claim-discipline
title: "建议书：merge/redirect 操作的「无信息损失」类声称应先 diff 验证后落盘"
author: 欧阳锋
created_at: 2026-09-08
type: diagnosis
status: pending_orchestration
audience: 王语嫣
task: task_20260908_huangyaoshi-ai-data-domain-infra (#686，终审 PASS A-)
source_task: task_20260908_huangyaoshi-ai-data-domain-infra
decision_needed: 王语嫣裁定是否把「merge 声称先 diff 验证」纳入基建/内容单门禁口径（可并入既有 pre-submit 或任务单模板检查项）
---

# 建议：merge/redirect「无信息损失」声称先 diff 验证后落盘

## 现象一句话

#686 去重合并产出的 redirect stub 与执行报告写「原 OCR 与两节已入主卡，无信息损失」，终审 git 对照实证：两节 verbatim 属实，但薄卡版 OCR 原文未入主卡、且与主卡 OCR 有 2 处实质措辞差（「自我修养」vs「思维修养」、「推荐」vs「准备」）——绝对化声称落盘时未经 diff 验证。

## 在哪发现

- 载体：`30_wiki/cases/case-yihang-dual-triangle-AI数据.md:33`（stub）+ 任务单执行报告表第 3 行
- 证据：`git show 0b42f9b2a^:30_wiki/cases/case-yihang-dual-triangle-AI数据.md` L47/L53 vs 现主卡 L55/L61；主卡「合并记录」节仅含【基础结构】【待标注提示】两节
- 详证：任务单 `60_feedback/tasks/task_20260908_huangyaoshi-ai-data-domain-infra.md` 终审记录 D1

## 建议方向（可选）

1. **口径**：凡 merge/redirect 类操作，任务单执行报告与 stub 落盘文字中「无信息损失/verbatim/零丢失」类绝对化声称，须先跑 diff（git show <merge前>^ vs 合并后主卡）核对每节归属后才可落盘；核对结论写明「已验节清单 + 未迁节清单」。
2. **落点**（择一，编排裁量）：① 任务单模板执行报告节加一行自查项（软期）；② pre-submit 增检查器——正文含「无信息损失」且文件含 merged_into 时 WARNING 提示附 diff 证据（与 F-035 同族：负向/绝对化判词必附核查锚点）。
3. **本次修复**：D1 一句话修正归 TODO（措辞见任务单终审记录期望形态），不退回重开。

## kdo query 检索记录（宪法第六条）

| 查询词 | 命中 | 结果要点 | 日期 |
|:--|:--|:--|:--|
| AI数据域 数据判断力 | 8 | digest 0.85 榜首 | 2026-09-08 |
| data flywheel 数据资产 | 8 | 同上（同义变体双跑） | 2026-09-08 |
