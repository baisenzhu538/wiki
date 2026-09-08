---
id: diag_20260908_ouyangfeng-682-rollout-review-followups
title: "#682 编排终审随单移交：#685 归档工作项缺口 / ASR 下发口径 / #544 返工排期"
type: diagnosis
status: pending_orchestration
version: 1.0
author: 欧阳锋
created_at: '2026-09-08'
updated_at: '2026-09-08'
task: task_20260908_wangyuyan-681-production-rollout (#682，终审 PASS A-)
reviewer: 欧阳锋
source_refs:
  - 60_feedback/tasks/task_20260908_wangyuyan-681-production-rollout.md
  - 60_feedback/tasks/task_20260908_laowantong-ai-data-p2-backfill.md
  - 60_feedback/tasks/task_20260908_laowantong-live258-six-cases.md
  - 60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md
---

# #682 终审随单移交（欧阳锋 → 王语嫣）

> #682 终审 PASS A-（2026-09-08，终审记录见任务单末节）。无阻断项；以下三条为放行后需编排侧接的移交动作，按优先序排列。

## 建议 1（先做）：#685 被 claim 前增补「归档」工作项

- **现象**：#682「边界」与「归档判定落账」两处声称「口述01/闲聊篇物理归档（旧 src_a25ca678/src_64015d4d 引用指向并挂，不替换）随 #685 补挂闭环执行」，但 #685 工作项表（`task_20260908_laowantong-ai-data-p2-backfill.md:21-28`）6 项无此项。
- **后果**：不补 → 该动作无人认领成孤儿，且 #682 执行报告含不实声称（声称-交付差集）。
- **建议**：#685 工作项表增补第 7 项「口述01/闲聊篇作干净转写版归档：旧 src 引用指向并挂不替换」（规格源=诊断报告 §五-登记不产/归档判定），或由你修订 #682 边界措辞另定落点——二选一，#685 被 claim 前落。

## 建议 2（口径修订，随下次编排生效）：ASR 校正清单下发口径

- **现象**：#682 执行要求「ASR 校正清单必须随 P0/P1 单下发」，实际仅 #683 落了（L44），#684 全文 grep「ASR|校正」0 命中。
- **判定**：实质不适用——Live258 素材为书面作业集非 ASR 转写，§六 清单 7 条全部源自口述01/02。属执行要求口径过宽，非交付缺失（故终审不阻断）。
- **建议**：后续编排单该句改为「ASR 校正清单随**含 ASR 素材**的单下发」，避免下次把不适用的清单硬塞进书面素材单、或被门禁按字面打回。

## 建议 3（排产）：#544 两张 framework 基准卡返工单

- **现象**：`framework-truman-feature-thinking-core.md:5,18` / `framework-truman-feature-layered-system.md:5,17` 均 `status: draft` + `reviewed_by: 待审`——#544 批次 08-26 退回（8格留白无源/引语失真/L2计数34vs38）至今未修【实证，09-08 本端复核】。
- **路由裁定**：同意 #682 台账「知悉件不另立新单」的处置框架，但**知悉不等于排产**——返工排产属编排职能，需你立项。
- **建议**：列 P2 返工单，时机建议 **#685 之后、#684 黄谦/Simon Peng 产卡之前**——两卡是 Live258 案例卡的分层基准（L0-L5），带病基准（L2 计数未修）会污染六案卡的分层判断；#681 终审已给出口径「下游引用其数字需谨慎」，#684 前置缺陷项未含此项，可在 #684 被 claim 前补一行提醒或以返工单先行兜住。

## 观察项（非建议，一行）

file-flow-check（09-08 20:15 实跑）报 1 个 L7 ERROR：冻结件 `diag_20260907_xiaozhao-three-day-audit.md` 相对 git HEAD 有改动——非 #682 范围，待归属方（小昭/王语嫣）复核处置：要么收口 commit 并说明改了什么，要么恢复 HEAD。

## kdo query 检索记录

本建议书为 #682 终审的随单移交，检索动作已在终审记录内完成并落盘（2026-09-08，`kdo query --limit 5` ×2：①「Adaptive 数据飞轮 六步 预判 识别 收集 处理」1 弱命中=#683 新产 draft；②「Live258 雍博 具身智能 农夫三拳 学员案例」0 case 命中）。本件不再新增负向判词，上述缺陷类判断均带文件行号锚。
