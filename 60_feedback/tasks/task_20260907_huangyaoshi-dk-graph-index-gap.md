---
id: task_20260907_huangyaoshi-dk-graph-index-gap
title: "graph_index 补录 dark-knowledges 族 332 张（0/332 实证——dk 卡图检索通道系统性失明，检索失明第三层根因）"
seq: 671
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋建议书 diag_20260907_ouyangfeng-dark-knowledges-graph-index-gap（0/332 path_map 实证）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T18:48:15.931973+00:00'
---

# #671 graph_index 补录 dk 族（黄药师）

## 实证（欧阳锋 #668 终审时独立复测发现）
graph_state.json path_map 含 frameworks/concepts/cases/tools/decisions 等，但 **dark-knowledges 0/332**——dk 卡在 kdo query 的 graph 检索通道系统性失明（hybrid RRF 的 graph 分量缺失使 dk 语义排序沉底；BM25 分量有命中但被稀释）。

## 修法
1. graph_index 构建脚本排查 dark-knowledges 目录被排除的原因（glob 漏/过滤规则误伤）
2. 补录 332 张 dk 入 graph index
3. **防复发**：索引覆盖率检查进 channel_health 或独立探针（30_wiki 各子目录卡数 vs 索引内数，缺口>0 报警）

## 验收
path_map dk 命中 332/332；kdo query 抽 5 张 dk 标题均召回；探针上线；回归不红。
