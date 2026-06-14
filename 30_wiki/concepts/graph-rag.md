---
id: graph-rag
aliases:
  - "Graph RAG"
created_at: 2026-05-03
domain:
  - "['ai-saas']"
related:
  - "[[kdo-protocol]]"
  - "[[index]]"
  - "[[kimi-深度调研集群方法论-deep-research-swarm]]"
review_date: 2026-05-04
reviewed_by: "黄药师"
status: enriched
title: "Graph RAG — Knowledge-Graph-Powered Retrieval"
trust_level: medium
type: concept
updated_at: 2026-05-03
pipeline:
  - confidence-verified-by-case
author: legacy
confidence: 0.75
---

# Graph RAG — Knowledge-Graph-Powered Retrieval

## Claims

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
## Critique

#### Nassim Taleb — 过度结构化与黑天鹅风险

**Nassim Taleb** (《反脆弱性》《黑天鹅》作者) 对任何"将复杂现实编码为结构化框架"的尝试都持深切怀疑。他的核心论点：**我们过度估计了我们能理解的东西，而低估了我们理解不了的东西。** 任何模板、框架或方法论都是一种"确定性幻觉"——它们假设未来会像过去一样发展，忽视了那些不可预测、不可分类、不可量化的黑天鹅事件。

> **为什么应该让你睡不着**：如果你正在依赖这张卡片做出关键决策，你已经在暗中排除了那些不可被编码为"步骤"的风险。这些"残留风险"不在框架内，但它们可能在一夜之间彻底改变一切。

#### Herbert Simon — 有限理性与认知超载

**Herbert Simon** (诺贝尔经济学奖得主、"有限理性"理论提出者) 从认知科学角度攻击：人类决策者的大脑处理信息的能力是有限的——复杂框架要求同时综合考虑多个维度，这对人类的工作记忆来说是超载的。

> **为什么应该让你睡不着**：如果这张卡片的使用者无法在一次会议中保持全部维度的逻辑一致性，那么它的产出就是多个独立假设而非一个综合分析。这种"分裂式分析"会让团队产生"每个维度都对但整体不对"的错觉。

### 内部局限

## Synthesis

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
| 在无专业背景的情况下做出重大决策 | 框架是信息输入，不是决策代理 | 结合自身业务场景做二次判断 |


## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份框架/方法做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
| 结构化分析后感觉"都对但整体不对" | 停下来检查是否忽视了框架之外的因素——团队、时机、技术债务 | 能指出至少一个被框架排除但实际影响很大的因素 |
| 使用过程中感到信息过载 | 不要一次性尝试应用整个框架——选择其中一个最直接相关的模块先用 | 在一个具体项目中成功应用了≥1个模块 |
