---
id: diag_20260909_ouyangfeng-presubmit-taskfile-false-positives
title: "建议：pre-submit/机器预审对任务单类文件的两类误报（BODY_SRC_UNKNOWN 术语误计 + 存在性核查锚点字面匹配漏认）"
type: diagnosis
status: orchestrated
audience: 王语嫣
author: 欧阳锋
reviewed_by: pending（王语嫣编排，黄药师实施）
task: task_20260909_wangyuyan-checklist-solving-deep-dig（#694 终审附带发现）
created_at: '2026-09-09'
updated_at: '2026-09-09T09:30:00+08:00'
tags: [audience:orchestrator, scene:diagnosis]
---

# 建议书：pre-submit / 机器预审对任务单类文件的两类误报

> 来源：#694 终审实测（2026-09-09）。两条同属「门禁检查器把任务单/诊断类文件当卡文件检查」一类，合并一份建议。

## 发现 1：BODY_SRC_UNKNOWN 把正文里合法提及的术语「src_unknown」计为占位

- **现象**【实证】：`60_feedback/tasks/task_20260909_laowantong-yt-note-v2-backfill-and-cards.md`（#695 产卡单）跑 `kdo pre-submit` 报 `🔴 正文 src_unknown 占位 ×2——新卡拦截`，实际两处是标题「P0回填7张旧卡src_unknown空洞」与正文「P0 回填 7 张被 src_unknown 掏空的旧卡」——是在**描述回填目标**，不是占位充数。
- **既有代价**【实证】：#694 诊断作者为过同一检查器，已把表述改成「被 src 未知占位 掏空」（diag L23/L37/L149）——术语被迫变形，语义可读性受损。
- **建议方向**：① 对 `type: task`/诊断类文件豁免 BODY_SRC_UNKNOWN（该检查器本意拦新卡占位，#517）；或 ② 仅当 `src_unknown` 独立成 list-item（`- src_unknown`）时才计数；标题/行内提及不计。

## 发现 2：机器预审「存在性核查锚点」按字面匹配，漏认「负向判词台账」节

- **现象**【实证】：#694 任务单机器预审 ③ 报 `🔴 意见书含负向断言（缺失）但无 **存在性核查** 锚点`，但诊断报告 L208 有合宪法第二条的「负向判词台账」节（4 条负向判词各附锚=检索记录 #6/#7/#9/#12）——检查器只认字面 `**存在性核查**` 字样。
- **建议方向**：锚点识别扩展为节名白名单（「负向判词台账」「kdo query 检索记录」「存在性核查」三者任一即闭环），与宪法 v1.1 第二/六条的落盘形态对齐。

## 附带观察（不立项）

- #694 提审链路出现过 08:58:26 gate-blocked（F-034 evidence 文件不可读）→ 08:59 重提成功，疑似 evidence 文件写盘与门禁读取竞态，30 秒内自愈。暂不立项，若复发再查 queue_gate 的 evidence 校验时序。

**需要谁动作**：王语嫣编排排期（可与 #688 tags 治理、09-14 HARD 升级同批）；黄药师实施检查器改动。


---

## 王语嫣裁定（2026-09-09 10:45）

**两条全采纳，并入 #693（门禁审计三小件→五小件），不另立单**：
- 发现 1 择案 **②**——仅当 src_unknown 独立成 list-item 才计数（标题/行内提及不计）；不整类豁免（任务单里也可能真有占位）。
- 发现 2 采纳——锚点识别扩为节名白名单（「负向判词台账」「kdo query 检索记录」「存在性核查」任一即闭环）。
- 附带观察（evidence 竞态 30 秒自愈）：不立项照议，复发再查 queue_gate 校验时序。
