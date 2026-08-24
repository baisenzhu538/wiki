---
id: diag-freeze-enforcement
title: 落盘文件冻结机械化建议书（任务单+建议书：L7 已就位，任务单 L10 缺口）
type: proposal
doc_id: D-20260824-003
version: v1.0
author: huangyaoshi
created_at: '2026-08-24T21:30:00+08:00'
updated_at: '2026-08-24T21:30:00+08:00'
audience: 王语嫣
status: pending_orchestration
---

# 落盘文件冻结机械化（任务单+建议书，用户 2026-08-24 指令"已落盘必须冻结，后续只能新增"）

## 现象一句话

冻结纪律已立（#449 规范 §6.1 已交冻结/§6.2 上板冻结）——**建议书侧已机械化（L7 无状态 git diff），任务单侧无机器检查**：上板（queued）后正文改动无拦截，靠自觉。

## 在哪发现

2026-08-24 占位节事件（任务单执行报告节 append 被五字段门禁拦——例外内正常操作，但暴露正文改动无检查）+ 用户指令"已落盘任务文件及建议书必须冻结，后续只能新增"。现状：file-flow-check L7 只覆盖 PROPOSAL-PENDING 段建议书；任务单（60_feedback/tasks/）上板冻结零机器检查。

## 建议方向

①**file-flow-check 加 L10「任务单正文冻结检测」**：queued/claimed/pending_review/reviewed 状态任务单 git diff HEAD——三类豁免（frontmatter 状态字段=queue_transition 独占 / 执行报告节=complete 前可填 / 终审记录节=欧阳锋写入），其余正文改动（追加/删节/修改）→ 报警"上板冻结禁止回头改"；②**挂 health-check 每日自动**（与 L7 同机制）；③**建议书侧确认**：L7 已覆盖登记后冻结，补"落盘即冻结"窗口口径（落盘→登记 ≤10min 内改动属登记前，文档注明）；④只报不自动改（检查器纪律）。

## 边界

- 豁免清单精确（节级识别：执行报告节/终审记录节按标题到下一 `##`；frontmatter 状态字段行级）
- 不拦 queue_transition 流转（状态字段独占不受影响）；不自动改文件
- 与 F-036 门禁互补：冻结管"落盘后不许改"，落点管"发现问题必须给去向"

## 待讨论点

1. 任务单"执行报告节"豁免是否收严——complete 前可填（规范口径）vs 提审后冻结（当前 append 实践）？
2. L10 报警等级：error（拦流转）还是 warning（报告）？建议 warning+health-check 报警（冻结违反应由人处置，不机械拦流转）
