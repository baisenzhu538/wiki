---
id: task_20260907_huangyaoshi-pathmap-key-hardening
title: "graph_state path_map 改 path/id 键根除同标题撞车（13 张溯源丢失实证——KDO 仓 graph.py:424）"
seq: 674
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋建议书 diag_20260907_ouyangfeng-title-collision-pathmap-hardening（#671 探针首报警的根因定位）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T20:17:58.142479+00:00'
---

# #674 path_map 键硬化（黄药师，KDO 仓）

## 实证
graph_state.json path_map 以 title 为键（graph.py:424）→ 同标题卡后者覆盖前者，13 张溯源映射丢失（concepts 1/dk 1/frameworks 1/tools 10）。#671 探针报警的 concepts 524/525 缺口即撞车卡。

## 修法（根因硬化，优于逐张改名）
path_map 改按 path（或 id）键；title 保留为展示属性。KDO 仓改动（Knowledge Delivery OS 0.0.1/kdo/）。

## 验收
重建后 path_map 无 title 撞车（13 张全部可溯源）；#671 探针 concepts 缺口清零；回归不红。
