---
title: "Graph RAG — Knowledge-Graph-Powered Retrieval"
type: concept
status: enriched
<<<<<<< HEAD
=======
domain: ['ai-saas']
>>>>>>> origin/main
source_refs:
  - "src_20260502_7d7c1b7c"
created_at: "2026-05-03"
updated_at: "2026-05-03"
related:
  - "[[KDO Protocol]]"
  - "[[Wiki Index — Knowledge Graph Entrypoint]]"
  - "[[Kimi 深度调研集群方法论 (Deep-Research-Swarm)]]"
tags:
  - #ai
  - #rag
  - #knowledge-graph
  - #retrieval
trust_level: medium
reviewed_by: "Claude"
review_date: "2026-05-03"
---

# Graph RAG — Knowledge-Graph-Powered Retrieval

## Core Points

1. **Graph RAG (Retrieval-Augmented Generation)** 是一种将**知识图谱拓扑结构**与**大语言模型生成能力**结合的技术。它不仅在文本层面检索相关内容，还利用实体之间的关系来增强上下文理解。
2. **与传统 RAG 的区别**：传统 RAG 把知识库切成文本块，靠向量相似度找相关内容；Graph RAG 先把知识解析成**节点（概念）和边（关系）**，检索时沿着关系网络遍历，找到语义上相关但文本上不一定相似的内容。
3. **一堂课程的核心洞察**：笔记系统中的 `[[双向链接]]` 天然构成了一张知识图谱，但当前 AI（包括 Claude）读取时是**线性扫描文本**，无法利用这些链接关系做推理。Graph RAG 就是要把这些隐式链接变成**显式图索引**。
4. **对 KDO 的直接影响**：KDO 的 `30_wiki/` 层已经有大量 `[[双向链接]]`，但 AI 回答"和 X 相关的所有知识"时仍需逐页搜索。Graph RAG 能让 AI 直接遍历概念网络，显著提升检索深度和召回率。
5. **技术实现路径**：从 Obsidian/KDO 的 Markdown 文件中提取 `[[链接]]`，构建图数据库（Neo4j/NetworkX）或图索引（JSON/GraphML），在检索时先走图、再走向量，两层叠加。

### [Critique]

- **Assumption**: 假设笔记中的 `[[链接]]` 质量足够高，能真实反映概念之间的关系。如果链接是随意添加的（比如为了链接而链接），图谱会引入噪声，反而降低 RAG 质量。
- **Boundary**: Graph RAG 对**结构化知识**（概念、实体、决策）效果显著，对**叙事性文本**（随笔、日记、情感记录）提升有限。KDO 的 `00_inbox/` 和 `10_raw/` 层不适合做图索引。
- **Reliability: Medium** — 理由：Graph RAG 是 2024-2025 年的前沿方向（Microsoft Research 的 GraphRAG 论文、Neo4j 的 LLM 集成），但具体落地到个人笔记系统的案例还不多。一堂正在探索，说明行业还在早期。
- **Anti-pattern risk**: 不要为了建图而建图。如果笔记量很小（< 100 页），传统 RAG 或全文搜索已经足够，Graph RAG 的维护成本可能大于收益。

### [Synthesis]

- **Links to**: [[KDO Protocol]] — Protocol 定义了目录结构和链接规则，是 Graph RAG 的**输入契约**；Graph RAG 是 Protocol 的**检索增强层**。
- **Links to**: [[Wiki Index — Knowledge Graph Entrypoint]] — Index 的 Mermaid 图是 Graph RAG 的**人工可视化版本**；Graph RAG 是它的**机器可计算版本**。
- **Links to**: [[Kimi 深度调研集群方法论 (Deep-Research-Swarm)]] — 深度调研需要跨概念关联推理，Graph RAG 是支撑这种推理的基础设施。
- **Complements**: 一堂课程中提到的"将课程体系拉入知识图谱"——KDO 的 `30_wiki/` 层正在做类似的事，但用 Markdown + 双向链接而非专门的图数据库。
- **Conflicts with**: Obsidian 的"自由哲学"——Graph RAG 要求链接有语义价值，可能抑制用户随意创建链接的自由度。
- **Transferable to**: 任何基于 Markdown 的双向链接系统（Notion、Logseq、Roam Research + LLM 集成）。
- **Gap**: KDO 目前只有文本层面的 `[[链接]]`，没有显式的图索引文件（如 `30_wiki/.graph/index.json`）。这是 P2 阶段的实施目标。

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

- [ ] Extract all `[[...]]` links from `30_wiki/`
- [ ] Build graph index (JSON/GraphML format)
- [ ] Define edge semantics (enables, requires, contradicts, derives-from)
- [ ] Integrate with `kdo query` command: graph traversal + vector search hybrid
- [ ] Visualize graph in `30_wiki/index.md` (replace static Mermaid with dynamic graph)

---

## References

- Microsoft Research: *From Local to Global: A Graph RAG Approach to Query-Focused Summarization* (2024)
- Neo4j LLM Knowledge Graph Builder
- 一堂课程：AI-Native 知识管理与 Graph RAG 应用
