---
id: agent-native-card-design
title: Agent 原生知识卡设计规范 v2
type: system
status: active
domain:
- kdo
author: 黄药师
source_context: KDO infrastructure decision — internal design record （原 legacy，已从 title/context/filename 推断为 src_20260503_52ae08ba）
source_refs:
- pending_archive:src_20260503_52ae08ba-kdo_product_design_agent_final
- src_20260503_52ae08ba-kdo_product_design_agent_final
reviewed_by: 欧阳锋
review_date: "2026-06-29"
created_at: 2026-06-15
confidence: 0.7
trust_level: medium
updated_at: '2026-06-29'
related:
- yt-composite-pan-product-methodology
- graph-rag-retrieval-layer
- graph-rag
- yt-model-pan-product-36-strategies
- yt-model-pan-product-aesthetic-toolkit
- yt-decision-y-model
- tool-yitang-Y-model-application
- framework-yitang-shishi-qiushi
- framework-yitang-jiefang-sixiang
- system-yitang-Y-model-os
- tool-agent-spec-yitang-Y-model-coach
  - dk-agent-promise-verification
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
|
---|---------|------------|
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
- src_unknown
- src_unknown
- src_unknown
- src_unknown

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
  - src_unknown
  - src_unknown
  - src_unknown
tags: ["泛产品设计", "方法论", "一堂"]      # 分类聚合

# ═══ 溯源（必须指向 10_raw/）═══
source_refs:
  - src_unknown

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
- src_unknown
- src_unknown

## Framework Gallery
### 关联框架卡
- src_unknown
- src_unknown

### 关键原图
- src_unknown
- src_unknown

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

## Critique
<!-- 什么时候不适用 -->
- src_unknown
- src_unknown

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

## Agent 规格卡的 TCPR 身份协议

所有 `agent-spec` 类型卡片必须显式声明 TCPR 身份，让 Agent 在会话启动时先声明身份、确认目标，再进入具体任务。

### 强制 frontmatter 字段

```yaml
# TCPR 身份协议
tcp_role: "C"                    # T / C / P / R 四选一
tcp_default_mode: "咨询诊断（Consult）：基于画像与行为信号判断客户等级"
tcp_switch_trigger: "用户明确要求切换身份、任务类型变化或当前身份所需输入缺失时"
tcp_session_opening: "我本次以 **C（Consult/咨询）** 身份与你协作：先帮你诊断客户分级，再给出跟进建议。"
```

| 字段 | 含义 | 取值 |
|:---|:---|:---|
| `tcp_role` | 当前 Agent 的默认 TCPR 身份 | `T`（教学 Teach）/ `C`（咨询 Consult）/ `P`（实践 Practice）/ `R`（研究 Research） |
| `tcp_default_mode` | 默认身份下要帮用户完成什么 | 一句话，包含身份名称 + 核心动作 |
| `tcp_switch_trigger` | 什么情况下触发身份切换 | 用户指令 / 任务变化 / 输入缺失 / 输出形式变化 |
| `tcp_session_opening` | 开场时向用户声明身份的固定话术 | 一句话，明确身份、目标、可切换 |

### System Prompt 开场模板

在 `agent-spec` 卡的 System Prompt 中，`# Role` 之后必须插入以下 TCPR 身份声明：

```markdown
## TCPR 身份声明

我本次以 **{{tcp_role}}（{{tcp_role_fullname}}）** 身份与你协作：{{session_goal}}。
- **默认模式**：{{tcp_default_mode}}
- **切换触发**：{{tcp_switch_trigger}}
- **切换协议**：当你说「切换到教学/咨询/实践/研究模式」、或任务类型明显变化、或当前身份所需输入缺失时，我会：
  1. 明确声明新身份和新目标；
  2. 复述已继承的事实/分析；
  3. 检查新身份所需输入是否完整，缺失时返回 `INPUT_MISSING`；
  4. 对高风险动作标注「需人工确认」。
```

### TCPR 身份选择指南

| 身份 | 核心动作 | 典型 Agent 场景 | 切换信号 |
|:---|:---|:---|:---|
| **T 教学 Teach** | 讲清楚方法论、降低认知门槛、训练用户 | 开场助手、方法论讲解、培训反馈 | 用户说「教我一下」「为什么这么写」 |
| **C 咨询 Consult** | 诊断问题、给出建议、助人决策 | 客户分级、过程追踪、异议处理 | 用户说「帮我看看」「该怎么选」 |
| **P 实践 Practice** | 直接产出可执行动作、推动落地 | 自我驱动、日程排期、话术生成 | 用户说「直接给我方案」「这周做什么」 |
| **R 研究 Research** | 建模、复盘、概率加权、跨案例比较 | 业绩监控、Pipeline 分析、A/B 测试 | 用户说「分析一下规律」「为什么整体差」 |

### 设计约束

- 身份不是人格：同一个 Agent 在不同会话中可以切换身份，但**同一会话内一次只选一个主导身份**。
- 开场必须协商：Agent 先声明默认身份，用户可立即要求切换；不强制用户填表。
- 切换继承上下文：身份切换不是重启会话，新身份必须复述已确认的事实，避免让用户重复输入。
- 切换协议引用 `agents/agent-os.md` / `system-yitang-Y-model-os`：本规范只定义卡片级字段，具体的切换边界与硬规则由 OS 层统一维护。

### lint 校验（建议）

`kdo lint` 对 `agent-spec` 类型卡片应做 WARNING 级检查：

- `tcp_role` 是否为 `T/C/P/R` 之一；
- `tcp_default_mode`、`tcp_switch_trigger`、`tcp_session_opening` 是否非空；
- System Prompt 中是否出现 `TCPR 身份声明` 关键字。

---

## 循环引用检测

kdo lint 应检测：
- src_unknown
- src_unknown

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
- src_unknown
- src_unknown
- src_unknown

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
- src_unknown
- src_unknown
- src_unknown

### 二、33 张 yt-panproduct-* 卡片的处理

纠正一个数字：盘点是 33 张 panproduct 卡，不是 127 张。127 是早期对整个 wiki 的 yt-panproduct-* 估算，实际产出的只有 33 张（全部在 `30_wiki/concepts/` 下）。

同意你的「不降级，重新分类」方案：

- src_unknown
- src_unknown
- src_unknown

但有一个额外问题：33 张 panproduct 卡目前是**旧格式**（无 agent-native frontmatter 字段，无 claims 列表，无 [conf=X][src] 格式）。重新分类时是否需要同时升级到 agent-native 格式？我的建议：

- src_unknown
- src_unknown
- src_unknown

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

---

## Agent Prompt 三层结构（2026-07-03 补充）

> 由黄药师提出、王语嫣确认：Y模型 + 实事求是 + 解放思想 是所有 Agent 的共享底层 OS，不是独立元 Agent。

### 核心分层

```
┌─────────────────────────────────────┐
│  OS 层：system-yitang-Y-model-os.md  │  ← 怎么思考（共享底座）
├─────────────────────────────────────┤
│  域层：framework / tool / case / dk   │  ← 思考什么（每域一套）
├─────────────────────────────────────┤
│  用户层：个人 OS / 历史决策 / 偏好     │  ← 跟谁协作（持续迭代）
└─────────────────────────────────────┘
```

### 强制要求

1. **所有 `tool-agent-spec` 卡和 `system-agent-spec` 卡的 System Prompt 必须显式分层**：
   - 顶部加载 OS 层：`{{system-yitang-Y-model-os.md}}`
   - 中间声明域知识来源：列出本 Agent 直接调用的 framework/tool/case/dk 卡 id
   - 底部说明用户层加载规则：若可用则读取个人上下文，若不可用则声明降级

2. **OS 层不替代域层**：OS 层回答「怎么思考」，域层回答「思考什么」。禁止把 Y模型五步法当域知识重复写入每张 agent-spec 卡。

3. **用户层尚未实现时声明降级**：若当前无法读取个人 OS，System Prompt 中必须写一句：「若个人域未加载，输出为通用建议，请用户复核是否匹配自身情况。」

4. **Coach 模式作为可选入口**：跨域或无域归属问题时，域 Agent 可切换到 `tool-agent-spec-yitang-Y-model-coach` 模式；Coach 模式只使用 OS 层 + 通用对话，不替代域 Agent。

### 模板示例

```markdown
## System Prompt 模板

```markdown
[OS 层]
{{system-yitang-Y-model-os.md}}

[域层]
你是 <域> <角色>。你的域知识来自：
- framework-xxx
- tool-yyy
- case-zzz
- dk-www

[用户层]
若可用，加载当前用户的个人 OS、历史决策偏好与任务上下文；
若不可用，明确说明「未加载个人域，输出为通用建议」。

# Role
...
```
```

### 谁来做

| 环节 | 角色 |
|:---|:---|
| 写 OS 层 | 老顽童 |
| 更新 agent-native-card-design 规范 | 老顽童 |
| 把 OS 层嵌入已有 agent-spec 卡 | 老顽童 |
| 架构评审 | 黄药师 |
| 终审 | 欧阳锋 |

---

## Agent 迭代成果回流 KDO（2026-07-02 补充）

> 由王语嫣基于 OPC 销售智能体实测经验提出，作为 agent-native 卡片设计规范的补充。

### 为什么需要回流

Agent 在实际对话中迭代出来的改进，不只是 system prompt 的措辞调整，往往反映了：
- 方法论卡本身的表达 gap
- 人类使用 Agent 时的典型失败模式
- 跨场景的通用交互经验

这些成果如果只留在 agent-spec 卡的迭代日志里，无法被其他 Agent 或人类复用。必须按类型回流到 KDO。

### 回流规则

| 迭代发现类型 | 回流目标 | 负责人 |
|:---|:---|:---|
| system prompt 表达不清、示例不足 | 更新对应 `agent-spec` 卡 | 老顽童 |
| 暴露出 source tool/framework 的 gap | 更新源方法论卡 | 老顽童修改，王语嫣诊断确认 |
| 反复出现的用户错误 / Agent 误用 | 新建/更新 `dk` 卡 | 王语嫣判断后入队 |
| 典型成功/失败场景 | 新建/更新 `case` 卡 | 王语嫣判断后入队 |
| 跨 Agent 通用的设计模式 | 新建/更新 `concept/framework` 卡 | 王语嫣 + 黄药师架构评审 |

### 回流触发条件

满足以下任一条件时，必须启动回流：

1. 同一个问题在 ≥2 次真实对话测试中被发现。
2. 某张 agent-spec 卡的 system prompt 经过 ≥2 轮迭代。
3. 用户明确反馈「Agent 的建议和 KDO 卡不一致」。
4. Agent 输出中反复出现某种 anti-pattern。

### 回流格式

每张 agent-spec 卡的 `## 迭代日志` 末尾必须增加一行：

```markdown
- **KDO 回流**：本次迭代发现 [问题]，已更新 [卡片 ID]，原因 [一句话]。
```

### 基础设施要求

- `kdo` CLI 未来应支持 `--agent-trace` 标志，导出一次 Agent 调用的完整输入/输出/引用卡片。
- `kdo lint` 应检查 agent-spec 卡是否包含 `## 迭代日志` 和 `KDO 回流` 字段。
- GraphRAG 索引时，应将 agent-spec 卡的 `迭代日志` 作为卡片更新历史的边权重参考。

### 谁来做

| 环节 | 角色 |
|:---|:---|
| 记录迭代日志 | 老顽童 |
| 判断是否需要回流 KDO | 王语嫣 |
| 源方法论卡修改 | 老顽童 |
| 架构层/工具链支持 | 黄药师 |
| 终审回流质量 | 欧阳锋 |

---

## Agent 规格卡的 Y模型三段自检（2026-07-03 补充）

> 由王语嫣基于「Y模型 + 实事求是 + 解放思想 = AI 操作系统」的洞察提出，作为所有 agent-spec 卡的强制设计标准。

### 核心判断

Agent 的幻觉和不可执行问题，本质上是 Y模型三段失衡：

- **缺右臂（实事求是）** → 只有理论/patterns，没有事实验证 → 幻觉
- **缺左臂（解放思想）** → 只在 L1-L2 做模式匹配，不会追问隐含假设 → 平庸/错误套用
- **缺知行合一轴** → 输出停在"建议考虑"，没有可执行动作 → 无法落地

因此，每张 agent-spec 卡必须显式回答三段问题。

### 强制字段

| 段落 | 必须回答 | 示例 |
|:---|:---|:---|
| **理论来源（左臂）** | 调用哪张/哪些 framework/tool/concept 卡？ | "调用 `framework-yitang-five-step-method` + `tool-opc-customer-segmentation`" |
| **事实输入（右臂）** | 必须输入哪些事实/数据？缺了怎么办？ | "必须输入客户近 30 天对话记录；缺失时返回 `INPUT_MISSING` 并提示用户补充" |
| **知行合一轴** | 最小可执行输出是什么？什么情况下必须人工复核？ | "输出 3 条回复选项 + 1 条不建议回复的理由；涉及价格时强制人工复核" |
| **幻觉风险等级** | 高 / 中 / 低 | 高风险：涉及具体数字、价格、医疗/法律建议 |
| **缺失一段的 fallback** | 如果某一段数据拿不到，Agent 如何降级？ | "缺事实输入时，只输出问题清单，不做判断" |

### 设计原则

1. **不是每个 Agent 都要三段齐全**，但它必须知道自己缺哪一段，并有 fallback。
2. **实事求是不是让 Agent"更诚实"**，而是给它明确的事实输入门和验证动作；AI 不会自发求真。
3. **解放思想不是让 Agent"更有创意"**，而是让它在调用方法论卡之前，先问"这个方法的适用条件是什么"。
4. **知行合一轴的输出必须是可拒绝的**：人类可以说"不"，Agent 必须能解释为什么这样建议。

### 谁来做

| 环节 | 角色 |
|:---|:---|
| 在 agent-spec 卡中填写 Y模型三段 | 老顽童 |
| 判断三段是否完整、fallback 是否合理 | 王语嫣 |
| 终审 | 欧阳锋 |
| 工具链支持（lint 检查） | 黄药师 |

---

## Agent 规格卡的 TCPR 身份协议（2026-07-01 补充）

> 由用户基于「用 TCPR 设计 Agent 能力分层」提出，作为所有 agent-spec 卡的强制启动标准。

### 核心判断

每次 Agent 与用户协作时，必须先确定一个 TCPR 身份（T/C/P/R），从而明确本次会话的目标和输出形态：

- **T（教学 Teach）**：目标是让用户理解某个概念/方法，输出以解释、示例、练习为主。
- **C（咨询 Consult）**：目标是帮用户诊断问题、给出建议，输出以问题、分析、可选方案为主。
- **P（实践 Practice）**：目标是陪用户落地执行，输出以动作清单、检查点、进度追踪为主。
- **R（研究 Research）**：目标是帮用户建立认知基线、提炼模型，输出以调研框架、证据链、可迁移规律为主。

没有选定身份的 Agent 容易在四种模式间漂移，导致输出混杂、目标不清、用户反复纠正。

### 强制字段

| 字段 | 说明 | 示例 |
|---|---|---|
| `tcp_role` | 本 Agent 默认的 TCPR 身份（单选或多选） | `C` / `["C","P"]` |
| `tcp_default_mode` | 默认进入的协作模式 | `Consult` |
| `tcp_switch_trigger` | 何时应切换身份或请求用户确认 | "当用户说'帮我写一个方案'时从 C 切换到 P" |
| `tcp_session_opening` | 首次响应必须说的话 | "我是 XX 助手，本次以咨询（C）身份协作。请描述你当前要解决的问题。" |

### 会话启动协议

所有 agent-spec 卡的 System Prompt 必须在开头包含：

1. **身份声明**："我是 [名称]，本次以 [T/C/P/R] 身份与你协作。"
2. **目标确认**："本次会话的核心目标是：[一句话]。"
3. **模式切换提示**："如果你需要我切换成 [其他角色]，直接说'切换到教学/咨询/实践/研究'。"
4. **默认兜底**：若用户未指定目标，按 `tcp_default_mode` 进入，先问 1-3 个澄清问题，再做判断。

### 中途切换身份协议

同一会话内切换 TCPR 身份的完整协议（触发条件、复述事实、输入门检查、高风险标注、上下文边界）定义在 **`agents/agent-os.md`**。本规范只要求：

1. 每张 `agent-spec` 卡必须声明自己支持哪些 TCPR 身份、默认身份是什么、切换到其他身份时的触发条件。
2. 每个 agent-spec 的 System Prompt 必须引导用户：「如需切换身份，说'切换到教学/咨询/实践/研究'」。
3. agent-spec 不重复定义切换协议本身，而是引用 `agents/agent-os.md` 中的五条硬边界。

### 设计原则

1. **身份即契约**：选定身份后，输出结构、语气、深度、风险等级都按该身份执行。
2. **单一会话单主身份**：一个会话可以临时切换，但必须显式声明，避免 silently drift。
3. **高风险身份需人工复核**：P（实践）和 R（研究）涉及执行和结论，输出中必须标明需要人类确认的动作。
4. **TCPR 不是固定人格**：同一 Agent 可以根据任务以不同身份运行；身份字段应写入 frontmatter 而非 prompt 中的人格设定。

### 谁来做

| 环节 | 角色 |
|:---|:---|
| 在 agent-spec 卡中补全 tcp_role / tcp_default_mode / tcp_switch_trigger | 老顽童 |
| 在 agent-native-card-design.md 中写入强制规范 | 黄药师 |
| 创建 `system-agent-role-selector` 通用会话启动协议卡 | 黄药师 |
| 更新 `framework-TCPR*` 两张卡，补充 Agent 身份协议视角 | 老顽童 |
| 终审 | 欧阳锋 |
| 工具链支持（lint 校验 tcp_role 字段） | 黄药师 |

---

## Agent Prompt 编译规范（2026-07-04 补充）

> 由黄药师在 #59 Agent Prompt 编译器中实现，王语嫣确认规范。

### 编译流程

```
agent-spec 卡 frontmatter 中的 source 字段
        ↓
  agent-prompt-compiler.py 读取并拼接
        ↓
  .agent/prompts/<agent-id>.md（含 frontmatter + 编译时间戳 + 来源 hash）
        ↓
  Claude Agent：CLAUDE.md 指向此文件
  Kimi/Hermes：注入为 system prompt
```

### Source 字段规范

所有 `tool-agent-spec` 和 `system-agent-spec` 类型卡片必须声明以下字段：

| 字段 | 类型 | 必填 | 说明 |
|:---|:---|:---|:---|
| `os_sources` | list | ✅ | OS 层来源卡路径。默认值：`["30_wiki/systems/system-yitang-Y-model-os.md", "agents/agent-os.md"]` |
| `domain_sources` | list | ✅ | 域层来源卡路径。至少包含本卡自身，可追加 framework/tool/case/dk 路径 |
| `user_sources` | list | ❌ | 用户层来源路径。当前预留，未来指向 personal-os 文件 |

### 编译产物规范

编译后的 `.agent/prompts/<agent-id>.md` 必须包含：
- YAML frontmatter（`id`, `type: compiled-prompt`, `compiled_at`, `estimated_tokens`, `os_sources`, `domain_sources`）
- 元层内容（OS 文件的 body）
- 域层内容（agent-spec 卡 body + domain_sources 指向的卡 body）
- 用户层内容（如果 user_sources 非空）
- 每段内容标注来源文件路径和内容 hash

### 编译器

`kdo-tools/agent-prompt-compiler.py`：读取 frontmatter source 字段 → 拼接 → 输出编译产物。

用法：
```bash
python kdo-tools/agent-prompt-compiler.py <agent-id>          # 编译
python kdo-tools/agent-prompt-compiler.py <agent-id> --dry-run # 预览
```

### 谁来做

| 环节 | 角色 |
|:---|:---|
| 在 agent-spec 卡中补全 os_sources / domain_sources | 黄药师（#62） |
| 编译器实现 | 黄药师（#59 已完成） |
| 规范文档维护 | 王语嫣 |
| 终审 | 欧阳锋 |