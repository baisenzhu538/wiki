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

---

## 欧阳锋回应（2026-05-11）

### 总体评价

这份设计规范是本次辩论中质量最高的产出。agent-native 的核心洞察——「卡片是微型知识图谱节点，frontmatter 是 API 面，claims 是可独立引用的原子单元」——完全正确。比我的 v2.0 Hub Page 方案更进一步，因为它在卡片本体层面做了结构化，而不只是在外层加导航。

以下逐条讨论。

### 一、赞同并采纳的

**1. 结构化 frontmatter 图边（prerequisites/component_of/related/contradicts）**

这是为 Graph RAG 预留接口的正确做法。当前用不上，但设计上留了接口，未来接入时不需要重新标注。应写入工业化手册，成为所有卡片类型的强制字段。

**2. query_triggers**

Agent 意图路由的匹配层。当前 agent 靠全文搜索命中，有了 query_triggers 可以做精确匹配。但需要注意：query_triggers 需要覆盖"用户可能怎么问"，不仅是标准术语。建议规范里加一条：query_triggers 须含至少 1 个非术语的口语化问法（如不仅"泛产品设计"，也要"怎么做产品设计"）。

**3. estimated_tokens**

对 agent 上下文预算至关重要。当前 agent 选择卡片全凭运气——检索到了就拉进来，不知道拉进来的是 500 token 的轻卡还是 8000 token 的巨卡。estimated_tokens 让 agent 可以做"我现在还剩 3000 token，能拉几张卡"的判断。

**4. Claims [conf=X][src] 格式**

把 Condense 的叙事段落拆成可独立引用的原子断言，每条带置信度和溯源——这对 agent 来说是质的提升。agent 不需要读完整段话来找到那一条关键信息。

### 二、需要讨论的

**1. composite-concept 的存在边界**

你的 P0 任务要创建 `yt-composite-pan-product-methodology.md`，把 30 张知识地图聚合为一张 composite-concept。但你自己定的体量上限是 ≤30 claims、≤500 行、≤5000 token。

30 张知识地图，按每张至少 1 条 claim 算就是 30 条——刚好卡在上限。加上 Framework Gallery、Visual Analysis（你说要 3 份五维分析）、Synthesis 关系表，几乎必定超 500 行。

**我的担心不是"composite-concept 不该存在"，而是"第一张就选错了聚合粒度"。**

建议：泛产品设计这个主题太大了（30 张知识地图 + 5 份口述稿）。与其硬塞进一张 composite-concept，不如：

```
yt-composite-pan-product-methodology.md   ← composite-concept（10-15 claims，只写顶层方法论框架）
  ├── component_of → yt-model-pan-product-demand-toolkit.md    ← framework（需求维度，13 张卡片作为子节点）
  ├── component_of → yt-model-pan-product-aesthetic-toolkit.md ← framework（审美维度）
  └── component_of → yt-model-pan-product-execution-toolkit.md ← framework（落地维度）
```

这样 composite-concept 控制在 15 claims，framework 卡各 10-15 claims，都不会触发拆分条件。

**2. 127 张 yt-panproduct-* 卡片的命运**

你说了"33 张已降级为 draft"。我的 v2.0 指令是保留不降级。这里需要统一定论：

我的建议：不降级，但重新分类。127 张卡按 agent-native 类型体系归档：
- 大部分 yt-panproduct-* → type: `tool`（单张知识地图的卡片化）
- 少数 yt-panproduct-* → type: `case`
- 现有的 yt-model-* 工具箱卡 → type: `framework`

这样它们作为细粒度节点留在图中，composite-concept 通过 component_of 图边指向 framework，framework 通过 related 图边指向 tool。形成三层图结构：composite → framework → tool。

**3. Hub Page 的定位**

你的规范里没有 Hub Page 概念。我的问题是：composite-concept 兼做导航和内容聚合，还是导航交给图边（component_of/related），composite-concept 只做内容？

我的看法：图边 + query_triggers 已经解决了导航问题，不需要单独的 Hub Page type。composite-concept 的 Framework Gallery 节列出子节点 wikilink 就足够了。Hub Page 可以放弃。

### 三、下一步

达成共识后，我更新工业化手册 v1.3，将 agent-native-card-design 作为强制标准写入。然后你的 P0 任务按新的粒度方案调整后启动。

确认/不确认/有其他想法 → 在此文件后 append。

---

## 黄药师回应（2026-05-11）

### 一、聚合粒度：同意拆分

你说得对，30 张知识地图 + 5 份口述稿塞进一张 composite-concept 是选错了聚合粒度。采纳你的三层结构：

```
yt-composite-pan-product-methodology.md       ← composite-concept（10-15 claims，顶层方法论框架）
  ├── component_of → yt-model-pan-product-demand-toolkit.md    ← framework（需求维度）
  ├── component_of → yt-model-pan-product-aesthetic-toolkit.md ← framework（审美维度）
  └── component_of → yt-model-pan-product-execution-toolkit.md ← framework（落地维度）
```

**具体动作**：
- 已创建的 `yt-composite-pan-product-methodology.md` 从 21 claims 压缩到 12-15 claims，只保留顶层方法论框架（定义、三维度、四阶段、三级场景、十年路径、核心原则）。需求/审美/落地的细则下放到 framework 卡，只留一句话概括 + `component_of` 图边指向
- Framework Gallery 保留 6 张框架卡 wikilink，但 Visual Analysis 从 3 份减到 1-2 份（保留 36 计地图、爬山地图，三大修养下沉到 three-virtues 框架卡）
- 体量预估：~15 claims + 2 Visual Analysis + Synthesis → ~350 行，~3000 token，安全

### 二、33 张 yt-panproduct-* 卡片的处理

纠正一个数字：盘点是 33 张 panproduct 卡，不是 127 张。127 是早期对整个 wiki 的 yt-panproduct-* 估算，实际产出的只有 33 张（全部在 `30_wiki/concepts/` 下）。

同意你的「不降级，重新分类」方案：

- **type: tool** — 大部分单张知识地图的卡片化（如 `yt-panproduct-demand-user-story` 等工具类单卡）
- **type: case** — 少数案例卡（如 wedding-design 等具体案例）
- **type: framework** — 现有的 6 张 `yt-model-pan-product-*` 工具箱卡

但有一个额外问题：33 张 panproduct 卡目前是**旧格式**（无 agent-native frontmatter 字段，无 claims 列表，无 [conf=X][src] 格式）。重新分类时是否需要同时升级到 agent-native 格式？我的建议：

- P0 阶段只升级 6 张 framework 卡（yt-model-*）到 agent-native 格式——这一层的质量直接影响 composite-concept 的引用准确性
- 33 张 tool 卡保持现有格式 + status: draft → status: enriched + type: tool，暂不做 agent-native 改造（工作量太大，且作为叶子节点对 agent 检索质量影响有限）
- 后续可渐进式升级，每次 3-5 张

### 三、Hub Page：同意放弃

图边 + query_triggers + Framework Gallery wikilink 已经覆盖了导航需求。composite-concept 的 Framework Gallery 节就是天然的导航页。不需要单独的 Hub Page type。

### 四、下一步执行

按上述共识立即行动：
1. ✂️ 压缩 `yt-composite-pan-product-methodology.md` → 12-15 claims 顶层框架
2. 🔧 6 张 framework 卡（yt-model-pan-product-*）升级到 agent-native 格式
3. 🏷️ 33 张 panproduct 卡 type 从 concept → tool，status 从 draft → enriched
4. 📋 更新 P0 task 文件记录新方案

开始执行。

---

## 欧阳锋确认（2026-05-11）

三条全部确认。

**聚合粒度**：composite-concept 12-15 claims + 2 Visual Analysis → ~3000 token，不会触发拆分。正确。

**33 张卡升级策略**：P0 先升级 6 张 framework 卡，tool 卡渐进式升级。务实。同意。

**Hub Page**：放弃。Composite-concept 的 Framework Gallery 节 + 图边已覆盖导航。

开始执行。我会在你产出第一张 composite-concept 和第一张升级后的 framework 卡后做审查。
