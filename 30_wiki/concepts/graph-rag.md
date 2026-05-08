---
title: "Graph RAG — Knowledge-Graph-Powered Retrieval"
type: concept
status: enriched
domain: ['ai-saas']
aliases: ["Graph RAG"]
source_refs:
  - "src_20260502_7d7c1b7c"
created_at: "2026-05-03"
updated_at: "2026-05-03"
related:
  - "[[kdo-protocol]]"
  - "[[index]]"
  - "[[kimi-深度调研集群方法论-deep-research-swarm]]"
tags:
  - #ai
  - #rag
  - #knowledge-graph
  - #retrieval
trust_level: medium
reviewed_by: "黄药师"
review_date: "2026-05-04"
---

# Graph RAG — Knowledge-Graph-Powered Retrieval

## [Condense] 核心观点

1. **Graph RAG 是检索范式的升维**：传统 RAG 把知识库切成文本块，靠向量相似度找相关内容；Graph RAG 先把知识解析成**节点（概念）和边（关系）**，检索时沿着关系网络遍历，找到语义相关但文本不一定相似的内容。

2. **双向链接 天然就是知识图谱**：KDO 的 `30_wiki/` 层已经有大量双向链接，但 AI 读取时是线性扫描文本，无法利用这些链接关系做推理。Graph RAG 就是要把隐式链接变成**显式图索引**——让 AI 能沿 1-hop → 2-hop 遍历概念网络。

3. **两层检索叠加优于单层**：先走图找关系路径（语义覆盖），再走向量找相似文本（精确匹配），两层叠加可以同时提升**召回率**（不漏掉间接相关的内容）和**精确度**（不被表面相似但实质无关的内容干扰）。

4. **Gateway 质量决定 Graph RAG 上限**：不是所有 `链接` 都有语义价值。如果链接是随意添加的（为了链接而链接），图谱会引入噪声反而降低质量。Graph RAG 要求链接有明确的语义关系（enables/requires/contradicts/derives-from）。

5. **不要为了建图而建图**：如果笔记量 < 100 页，传统 RAG 或全文搜索已经足够。Graph RAG 的维护成本（建索引 + 定义边语义）在笔记量超过临界值后才值得投入。KDO 当前 23 张概念卡正接近这个临界点。

### [Critique]

- **Assumption**: 假设笔记中的 `链接` 质量足够高，能真实反映概念之间的关系。如果链接是随意添加的（比如为了链接而链接），图谱会引入噪声，反而降低 RAG 质量。
- **Boundary**: Graph RAG 对**结构化知识**（概念、实体、决策）效果显著，对**叙事性文本**（随笔、日记、情感记录）提升有限。KDO 的 `00_inbox/` 和 `10_raw/` 层不适合做图索引。
- **Reliability: Medium** — 理由：Graph RAG 是 2024-2025 年的前沿方向（Microsoft Research 的 GraphRAG 论文、Neo4j 的 LLM 集成），但具体落地到个人笔记系统的案例还不多。一堂正在探索，说明行业还在早期。
- **Anti-pattern risk**: 不要为了建图而建图。如果笔记量很小（< 100 页），传统 RAG 或全文搜索已经足够，Graph RAG 的维护成本可能大于收益。

### [Synthesis]

- **Links to**: [[kdo-protocol]] — Protocol 定义了目录结构和链接规则，是 Graph RAG 的**输入契约**；Graph RAG 是 Protocol 的**检索增强层**。
- **Links to**: [[index]] — Index 的 Mermaid 图是 Graph RAG 的**人工可视化版本**；Graph RAG 是它的**机器可计算版本**。
- **Links to**: [[kimi-深度调研集群方法论-deep-research-swarm]] — 深度调研需要跨概念关联推理，Graph RAG 是支撑这种推理的基础设施。
- **Complements**: 一堂课程中提到的"将课程体系拉入知识图谱"——KDO 的 `30_wiki/` 层正在做类似的事，但用 Markdown + 双向链接而非专门的图数据库。
- **Conflicts with**: Obsidian 的"自由哲学"——Graph RAG 要求链接有语义价值，可能抑制用户随意创建链接的自由度。
- **Transferable to**: 任何基于 Markdown 的双向链接系统（Notion、Logseq、Roam Research + LLM 集成）。
- **Gap**: KDO 目前只有文本层面的 `链接`，没有显式的图索引文件（如 `30_wiki/.graph/index.json`）。这是 P2 阶段的实施目标。

---

## How Graph RAG Works in KDO

### Current State (Text RAG)

```
User asks: "和 KDO 相关的概念有哪些？"
AI action: 线性搜索所有 .md 文件，找包含 "KDO" 的文本
Problem:   可能漏掉间接相关的内容（如 "知识操作系统"、"Obsidian 工作流"）
```

### Target State (Graph RAG)

```
User asks: "和 KDO 相关的概念有哪些？"
AI action: 
  1. 找到 "KDO" 节点
  2. 遍历图谱：直接邻居（1-hop）→ 邻居的邻居（2-hop）
  3. 按关系权重排序
  4. 返回关联概念 + 关系路径
Result:   不仅找到提到 "KDO" 的页面，还找到通过 "Obsidian"、"AI 工作流"、"知识图谱" 间接关联的内容
```

### KDO-Specific Graph Schema

```yaml
# 30_wiki/.graph/index.json (proposed)
nodes:
  - id: "kdo-protocol"
    label: "KDO Protocol"
    type: system
    path: "30_wiki/systems/kdo-protocol.md"

edges:
  - from: "kdo-protocol"
    to: "obsidian-workflow"
    relation: "enables"
    weight: 0.9

  - from: "kdo-protocol"
    to: "graph-rag"
    relation: "requires"
    weight: 0.8
```

---

## Implementation Checklist (P2 Phase)

- [ ] Extract all `...` links from `30_wiki/`
- [ ] Build graph index (JSON/GraphML format)
- [ ] Define edge semantics (enables, requires, contradicts, derives-from)
- [ ] Integrate with `kdo query` command: graph traversal + vector search hybrid
- [ ] Visualize graph in `30_wiki/index.md` (replace static Mermaid with dynamic graph)

---

## References

- Microsoft Research: *From Local to Global: A Graph RAG Approach to Query-Focused Summarization* (2024)
- Neo4j LLM Knowledge Graph Builder
- 一堂课程：AI-Native 知识管理与 Graph RAG 应用
