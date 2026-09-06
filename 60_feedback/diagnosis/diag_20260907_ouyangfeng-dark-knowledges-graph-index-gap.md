---
id: diag_20260907_ouyangfeng-dark-knowledges-graph-index-gap
title: dark-knowledges 卡族未入 graph index——检索失明的系统性根因
type: diagnosis
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: '2026-09-07'
---

# 建议书：dark-knowledges 卡族未入 graph index（0/332 实证）

## 现象一句话
`30_wiki/dark-knowledges/` 全部 332 个 dk 卡文件均未进 graph index（graph_state.json path_map 比对 0/332 命中），导致 dk 卡在 kdo query 的 graph 检索通道系统性失明。

## 在哪发现
终审 #668（AI知识库 draft 卡族转正批 11 张）时独立复测「检索失明清偿」声称：dk-AI知识库-隐性知识显性化60分原则 卡虽已 status: pending_review + trust_level: high，但多组查询（隐性知识显性化 自动化 / 60分原则 隐性知识 / 其 id / 其标题）均未召回。溯源比对：
- graph_state.json path_map 含 frameworks/concepts/cases/tools/decisions 等，但 dk 0 条。
- graph_chunk_entity_relation.graphml grep 该 dk 卡标题 0 命中；同批 framework 卡（四象限资产/五阶段演进）有命中。
- search_index.json（BM25）该 dk 卡有命中，但 hybrid RRF 的 graph 分量缺失使 dk 卡语义排序沉底。

## 建议方向（可选）
1. 排查 graph index 构建/增量对 dark-knowledges/ 目录的覆盖范围（疑似目录白名单缺 dark-knowledges）。
2. 修复后全量 rebuild 一次，并复测 dk 卡族语义可达性。
3. 建议并入黄药师 #670（卡 status 翻转机制）或单独立基建单，由黄药师机制化；本建议书仅登记，不动手修。

## 边界
本建议不阻断 #668 11 卡内容转正（dk 卡内容本身七段完整、四节补齐合规）；检索失明属基础设施层，与内容质量分层处理。