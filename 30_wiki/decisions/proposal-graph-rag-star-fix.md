---

id: "proposal-graph-rag-star-fix"
title: "Graph RAG 放射状图谱修复提案"
type: "improvement-plan"
status: "draft"
domain:
  - "infrastructure"
  - "knowledge-graph"
created_at: 2026-06-11
author: "legacy"
source_context: "KDO improvement plan — internal process record"
source_refs: []
reviewed_by: "pending"
confidence: 0.6
trust_level: "low"
---

# Graph RAG 放射状图谱修复提案

## 问题

知识图谱关系可视化呈现**放射状星形结构**——所有卡片指向少数几个中心节点（index/log/目录类卡片），而非形成互相交织的复杂网络。

## 根因

两层原因，需要不同角色处理：

### 原因 A（黄药师修）: Graph RAG 未过滤元页面

`graph.py` 中 `_collect_all_wiki_pages` → `_collect_wiki_pages` 扫描 `30_wiki/concepts/` 下所有 `.md` 文件，**包括** `yt-system-course-catalog.md`（一堂全课程目录索引，含 21 条 claims，几乎链接全部卡片）。

对比：`search_index.py` 的 `SearchIndex.build()`（line 88-90）明确过滤了 `index.md`、`log.md`、`contradictions.md` 和 `decisions/` 目录，但 `graph.py` 的 `_collect_wiki_pages` 没有做任何过滤。

**现象**：课程目录卡被摄入为图实体，它拥有指向几乎所有卡片的出边 → 它在图里成为引力中心 → 所有路径最短都经过它 → 放射状。

### 原因 B（老顽童改）: 卡片间互链稀疏

每张卡 Synthesis 节平均只有 3-5 个 wikilink，相对于指向目录卡的链接数量，卡片间互链被淹没。

## 修复方案

### A 部分：黄药师（代码，低风险，建议立即做）

**A1**：在 `_collect_wiki_pages`（graph.py line 78-99）中增加过滤逻辑：

```
跳过以下文件：
1. 文件名匹配 index.md, log.md, contradictions.md
2. 文件名以 yt-system- 开头（系统级索引卡）
3. decisions/ 目录下所有文件（决策记录非知识实体）
```

**A2**：在前端 Graph RAG 可视化入口（如果有）标注节点类型，区分"知识实体"和"元页面"。

**A3**（可选）：Graph RAG 构建后跑一个健康检查——检测是否存在"一个节点的出边/入边数量超过总节点数 30%"的情况，如果是则发警告。

**代码位置**：
- `graph.py`：`_collect_wiki_pages()`（line 78-99）和 `_build_custom_kg()`（line 102-210）
- 参考已有实现：`search_index.py` line 88-90 的过滤逻辑

**工作量估计**：约 0.5-1 小时

**完成标志**：
1. 重建索引 `kdo graph rebuild --full` 后，`kdo graph stats` 的节点数明显下降（去掉系统卡片）
2. 在下游可视化中图谱不再是单中心放射状

### B 部分：老顽童（内容规范，逐步推进，建议从新卡开始）

**B1**：新卡（MECE / Issue Tree / Hypothesis-Driven 等桥接卡）的 Synthesis 节从"3-5 个"提升到"5-10 个"，重点是卡间互链，不只是"指向目录/入口卡"。

**B2**：`related` frontmatter 字段从可选提升为推荐填写。

**B3**：桥接卡（MECE 等）必须通过 `bridges_to` 字段建立跨域链接，增加不同域之间的图密度。

## 优先级

| 部分 | 优先级 | 谁做 | 工作量 | 建议 |
|:----|:-----:|:----|:-----:|:----|
| A1 | P0 | 黄药师 | 0.5h | 修了就能改善图谱，不依赖老顽童 |
| A2-A3 | P2 | 黄药师 | 可选 | 先做 A1 再说 |
| B1-B3 | P1 | 老顽童 | 持续 | 从桥接卡试点开始，逐步推进 |

## 注意

A 部分修复后，图谱会有明显改善——去掉目录中心节点后，图会变稀疏但更真实。卡间链接密度由老顽童的 B 部分逐步提升，这是一个持续过程，不追求一次性修完。
