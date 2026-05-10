---
id: "sys-agent-native-card-design"
title: "Agent 原生知识卡设计规范 v2"
type: "system"
status: "active"
domain: "kdo"
version: 2
created_at: "2026-05-11"
updated_at: "2026-05-11"
reviewed_by: "欧阳锋"
---

# Agent 原生知识卡设计规范 v2

## 定位

`30_wiki/` 是 agent 的知识基座。消费链路：

```
30_wiki（Agent 消费）──查询/遍历──▶ Agent ──生成──▶ 40_outputs（人类阅读）
         ▲
         │ 未来：GraphRAG 索引 / CLI / MCP Server
         │ 其他 agent 通过结构化 frontmatter 查询
```

**设计目标**：卡片是 agent 的"微型知识图谱节点"——结构化 frontmatter 是 API 面，claims 是可独立引用的原子知识单元，图边支撑未来 Graph RAG 遍历。

## 未来接入点

| 能力 | 当前状态 | 卡片设计预留 |
|------|---------|------------|
| Graph RAG 索引 | 规划中 | frontmatter 图边（prerequisites/component_of/related/contradicts）构成可索引图 |
| CLI 查询 | 规划中 | frontmatter 所有字段可通过 `kdo query --field=value` 检索 |
| MCP Server | 规划中 | 卡片作为 MCP resource，frontmatter → resource metadata，body → resource content |
| 第三方 Agent 调用 | 规划中 | `query_triggers` 作为意图路由表的训练数据 |

## 查询接口分层

```
Layer 1 (当前): Obsidian Dataview — frontmatter 字段过滤
Layer 2 (当前): ripgrep/grep — 全文搜索 fallback
Layer 3 (规划): kdo CLI — `kdo query 'domain:yitang type:composite-concept'`
Layer 4 (规划): kdo MCP — `mcp__kdo__search_cards({domain: "yitang", query_triggers: ["泛产品"]})`
Layer 5 (规划): Graph RAG — 图边遍历 + 语义向量检索
```

## 卡片类型

| type | 用途 | 典型大小 |
|------|------|---------|
| `composite-concept` | 复合概念卡——多源聚合 | 15-30 claims, ≤500行 |
| `framework` | 框架卡——知识地图的结构化描述 | 5-15 claims, ≤300行 |
| `case` | 案例卡 | 5-10 claims, ≤200行 |
| `tool` | 工具卡——检查清单/画布/模板 | 3-10 claims, ≤150行 |

### 拆分原则

一张 composite-concept 卡在以下任一条件触发时拆分：
- Claims > 30
- 单卡 > 500 行
- Visual Analysis > 5 份
- 估算 token > 5000

## Agent 原生 Frontmatter（完整版）

```yaml
---
# ═══ 标识 ═══
id: "yt-composite-pan-product-methodology"   # 唯一标识，不可变
title: "泛产品设计方法论"
type: "composite-concept"
status: "enriched"
domain: "yitang"
language: "zh-CN"
version: 1
difficulty: "intermediate"                  # beginner | intermediate | advanced

# ═══ 时间戳 ═══
created_at: "2026-05-11"
updated_at: "2026-05-11"
review_by: "2026-11-11"                    # 知识过期提醒

# ═══ 置信度 ═══
confidence: 0.8                            # 全局置信度

# ═══ 图遍历边 ═══
prerequisites: []                           # 理解本卡前需先掌握的卡片 id
component_of: []                            # 本卡是哪个更大概念的子集
related: []                                 # 相关卡片 id
contradicts: []                             # 与其他卡片有矛盾的主张

# ═══ 检索触发 ═══
query_triggers:                             # agent 意图匹配（≥3 个，含同义变体）
  - "泛产品设计"
  - "泛产品方法论"
  - "产品设计方法"
tags: ["泛产品设计", "方法论", "一堂"]      # 分类聚合

# ═══ 溯源（必须指向 10_raw/）═══
source_refs:
  - "10_raw/sources/xxx.md"

# ═══ 生命周期 ═══
superseded_by: ""                           # 被哪张新卡取代
deprecation_reason: ""                      # 废弃原因

# ═══ 元信息 ═══
estimated_tokens: 2500                      # 估算 token 数，帮助 agent 预算上下文
---
```

## Agent 原生 Body 结构

```markdown
## Claims
<!-- 核心断言。格式：claim:NN [conf=X][src] 内容 -->
- claim:01 [conf=0.9][src: 10_raw/sources/xxx.md] 泛产品设计包含三个核心维度：需求、审美、落地
- claim:02 [conf=0.8][src: 10_raw/sources/yyy.md] ...

## Framework Gallery
### 关联框架卡
- [[yt-model-pan-product-climbing-map]]
- [[yt-model-pan-product-36-strategies]]

### 关键原图
- ![[一堂泛产品设计36计-全套地图.png]]
- ![[一堂泛产品设计-十年修炼爬山地图.png]]

## Visual Analysis
<!-- 每份分析为表格，可机器解析 -->

### 36计全套地图
| 维度 | 分析 |
|------|------|
| 布局结构 | ... |
| 核心隐喻 | ... |
| 信息层级 | ... |
| 视觉锚点 | ... |
| 隐含假设 | ... |

## Constraints & Boundaries
<!-- 什么时候不适用 -->
- claim:boundary-01 [conf=0.7] 本方法论适用于 B2C 产品设计，B2B 场景需额外考虑采购决策链
- claim:boundary-02 [conf=0.8] 假设产品已过 PMF 阶段，不适用于 0-1 探索期

## Synthesis
<!-- 与其他节点关系表，可机器解析 -->
| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 前置 | [[yt-model-pan-product-three-virtues]] | 三大修养是方法论的前置心态 |
| 组件 | [[yt-model-pan-product-demand-toolkit]] | 需求工具箱是方法论的需求子集 |
| 组件 | [[yt-model-pan-product-aesthetic-toolkit]] | 审美工具箱是方法论的审美子集 |
| 组件 | [[yt-model-pan-product-execution-toolkit]] | 落地工具箱是方法论的落地子集 |
| 矛盾 | 无 | |
```

## 三步编译 → Agent 结构映射

| 旧（人类叙事） | 新（Agent 结构） |
|:--|:--|
| Condense 叙事段落 | Claims 列表，每条 [conf=X][src] 可独立引用 |
| Critique 推理过程 | Constraints & Boundaries + contradicts 字段 + per-claim conf |
| Synthesis 叙事整合 | Synthesis 关系表 + frontmatter 图边（可被 Graph RAG 索引） |
| 文章内 wikilink | frontmatter 图边 + Framework Gallery（wikilink 与图片嵌入分节） |

## 卡片体量约束

| 指标 | 上限 |
|:--|:--|
| Claims | ≤ 30 |
| Visual Analysis | ≤ 5 份 |
| Framework Gallery wikilink | ≤ 10 |
| 单卡总行数 | ≤ 500 |
| 估算 token | ≤ 5000 |

## 质量门禁

| 门禁 | 要求 |
|:--|:--|
| frontmatter 完整 | id、type、domain、confidence、query_triggers(≥3)、所有图边字段 非空 |
| source_refs → 10_raw/ | 不得指向 00_inbox/ |
| Claims ≥ 5 | 每条带 `claim:NN [conf=X][src]` 格式 |
| Visual Analysis | 每个嵌入原图都有表格化五维分析 |
| Constraints 非空 | 至少 1 条 boundary claim |
| 体量合规 | 不超过上限 |
| kdo lint 0 error | |

## 循环引用检测

kdo lint 应检测：
- A.prerequisites 包含 B 且 B.prerequisites 包含 A → 警告
- A.contradicts 包含 B 但 B.contradicts 不含 A → 警告（双向一致性）
