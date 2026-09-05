---
id: task_20260906_huangyaoshi-graph-index-stall-rootfix
title: "graph_index 停拍根因+重建+哨兵复查（infra-liveness 六拍连续增长实证，#622 复发）"
seq: 648
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（infra-liveness 09-04 23:47→09-05 04:17 六拍 48h→53h 连续增长，真实故障非回声）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T00:50:00+08:00'
---

# #648 graph_index 停拍根因+重建+哨兵复查（黄药师）

## 背景
infra-liveness 报警（conveyor_probe）：graph_index 陈旧（落后 search_index）从 09-04 23:47 起六拍连续增长 48h→49h→50h→51h→52h→53h。此前五拍被值守划销为「回声」（09-06 王语嫣复核：误判——回声是同一事件重复登记，这是持续恶化的单一故障）。#622 曾做 graph_index 重建+哨兵，本次为复发或哨兵未覆盖此面。

## 任务
1. **根因**：graph_index 生成/刷新链路为何停摆 53h+（计划任务没跑？跑了失败？哨兵为何没自愈没升级？）——结论落执行报告，附证据（日志/时间戳）。
2. **重建**：graph_index 重建至最新（落后 search_index 回落到阈值内）。
3. **哨兵复查**：#622 哨兵为何没拦住本次停摆；修复为「停拍超阈值→自动重建或升级报警」二选一，想犯错也犯不了。

## 验证
- 重建后 infra-liveness 下一拍不再报 graph-index 陈旧（或时差回落 <阈值）。
- 哨兵回归：模拟停拍场景验证自动重建/升级路径。

## 交付
- 根因结论+重建 diff/日志+哨兵修复+回归证据+执行报告（F-034 五字段全）。
- claim/complete 走 `queue_transition.py`（claim 648 / complete 648）。

## 边界
- 依赖 #646 终审后开工（同角色排队，不并行施工）；根因若指向 #622 交付缺陷，如实记入（不甩锅不隐匿）。
