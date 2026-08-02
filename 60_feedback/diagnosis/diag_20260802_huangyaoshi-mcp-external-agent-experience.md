---
id: diag_20260802_huangyaoshi-mcp-external-agent-experience
type: diagnosis
author: 黄药师
status: proposal
target_audience: 王语嫣（编排）、黄药师（基建实现）、欧阳锋（审查门禁升级）
created_at: 2026-08-02
domain: kdo-infrastructure
priority: P1
source:
  - 小昭 2026-08-02 搜索可达性诊断报告
  - 黄药师 2026-07-27 MCP 检索效率升级
  - 讲香基本功-李頔-260731 口述稿分析
  - KDO 检索架构 v2（MOC绝对优先+BM25+RRF）
---

# MCP 外部 Agent 体验升级——任务建议书

> **写给王语嫣**：这份建议书聚焦外部 Agent（小昭、Codex 等）通过 MCP 调用 KDO 时的端到端体验。不是基建修补——是"讲香"视角下的接口设计升级。
> **建议编排方式**：将各节拆为独立任务单入 production-queue，标注 assignee（黄药师/老顽童/欧阳锋）。

---

## 一、现象：小昭搜"创新者的窘境"的完整路径

2026-08-02 实际发生的外部 Agent 调用链路：

```
用户 → 小昭: "查一下创新者的窘境"
小昭 → kdo_search("创新者的窘境") → 0 条结果（top score 30.381）
小昭 → kdo_search("创新者窘境 颠覆式创新 破坏性创新") → 0 条结果
小昭 → 放弃 KDO → 文件系统 ls | grep → 找到了
```

**卡片确实存在**，而且质量很高（confidence 0.92，欧阳锋终审通过）。但外部 Agent 搜不到——因为搜索关键词和索引之间缺了三层桥接：

| 层 | 缺了什么 | 影响 |
|:--|:--|:--|
| 卡片元数据 | `title` 空 / 无 `aliases` / 无 `tags` | BM25 丢失最高权重字段 |
| 索引管道 | 索引未感知元数据层的 aliases 更新 | 07-27 升级后此卡可能未重建索引 |
| 审查门禁 | pre-submit 不检查 title/aliases/tags 完整性 | 空 title 的卡通过了终审 |

---

## 二、根因：从"搜不到"到"外部 Agent 为什么放弃 KDO"

小昭的诊断报告已经分析了四个根因（卡片元数据 / BM25 / 索引 / 审查）。这里补一层讲香视角的分析——**为什么外部 Agent 在搜索失败后直接放弃 KDO 而不尝试其他路径**。

### 2.1 MCP 工具描述是 V1 水平

当前 `kdo_search` 的 MCP tool description：

```
"Search KDO wiki knowledge base using hybrid retrieval (BM25 + Graph RAG + RRF fusion)"
```

这是一个**技术功能描述**——告诉 Agent 这个工具"是什么"，没告诉它"什么时候用"、"搜不到怎么办"、"和哪个工具组合"。

外部 Agent 看完这个描述后的决策链：
```
"搜不到 → 工具返回空 → 工具描述没告诉我还能怎么办 → 放弃"
```

### 2.2 搜索结果无自解释能力

`kdo_search` 返回的结果是卡片列表（id + snippet + score）。外部 Agent 拿到后需要：
1. 判断哪些结果真的相关（snippet 太短，不够判断）
2. 逐张调 `kdo_read` 看全文（MCP 调用 ×N 次）
3. 如果搜不到，工具不返回任何替代建议

对比讲香框架：返回结果只做到了"有数字"（score），没做到"有场景"（这个结果适合你当前的问题吗？），更没做到"有路径"（搜不到时试试什么）。

### 2.3 MCP 工具间无协作路由

KDO 目前对外暴露多个 MCP 工具（`kdo_search` / `kdo_read` / `kdo_graph` / `kdo_query`），但：
- 各工具的 description 互相不引用
- 没有"如果你搜不到 X，试试用 Y 工具查 Z"的路由提示
- 外部 Agent 不知道工具的上下游关系

这就像 讲香 里 CLI 第一版发布话术——所有信息都在，但 Agent 不知道"和我什么关系"。

### 2.4 搜索失败无结构化诊断输出

当 `kdo_search` 返回 0 条时，外部 Agent 拿到的只有一个空列表。没有：
- 为什么搜不到（关键词不在索引中？卡片存在但 title 空？）
- 建议尝试什么（换关键词？换工具？检查索引？）
- 最近的索引更新时间

Agent 只能猜测，猜一次失败就放弃。

---

## 三、迭代建议

### P0-1：pre-submit 新增 title + aliases + tags 完整性门禁

**问题**：`framework-christensen-disruptive-innovation` 的 title 为空、无 aliases、无 tags，通过了终审入库。外部 Agent 永远搜不到它。

**方案**：在 pre-submit 的 validate 阶段新增三条 schema 级门禁：

```python
# title 不能为空
if not fm.get("title", "").strip():
    errors.append(f"{rel}: MISSING REQUIRED FIELD 'title' — card invisible to search without title")

# aliases 至少包含一个中文关键词（与该卡常见中文名匹配）
aliases = fm.get("aliases", [])
if isinstance(aliases, str): aliases = [aliases]
if not aliases or all(not re.search(r'[一-鿿]', a) for a in aliases if a):
    errors.append(f"{rel}: WARN: aliases missing Chinese keywords — card will be unreachable via Chinese search")

# tags 至少包含 audience 和 scene
tags = fm.get("tags", [])
has_audience = any('audience' in t for t in tags if t)
has_scene = any('scene' in t for t in tags if t)
if not has_audience or not has_scene:
    errors.append(f"{rel}: WARN: tags missing audience/scene — card will not appear in scenario-based search results")
```

**指定**：黄药师（Builder，在 kdo_lint.py / pre_submit.py 中实现）
**验收**：跑 pre-submit 对空 title 卡报 ERROR 阻断；对缺 aliases/tags 的卡报 WARN。

---

### P0-2：MCP `kdo_search` tool description 场景化

**当前**：
```
Search KDO wiki knowledge base using hybrid retrieval
```

**目标**：
```
当你需要检索一堂/商业方法论、找案例支撑论点、查某个概念是否存在时调用此工具。

返回结果包含：卡片标题 + 摘要 + 场景标签（audience/scene）+ 溯源路径。
score > 70 → 高度相关，可直接引用
score 40-70 → 部分相关，建议再调 kdo_read 确认
score < 40 → 弱相关或搜索词不在索引中

如果返回 0 条结果，尝试：
1. 换中文/英文关键词重搜（如"破坏性创新" → "Christensen"）
2. 用 kdo_graph 按域浏览（如 kdo_graph("strategy") 查看战略域全部卡片）
3. 告诉用户"这个主题 KDO 可能尚未收录，或收录了但元数据不完整"
```

**实现量级**：修改 `kdo-tools/mcp/tools.py` 中的 tool description 字符串，1 处改动。

**为什么重要**：外部 Agent 判断"何时调用、搜不到怎么办"的唯一依据就是 tool description。当前描述信息量为零。改造后 Agent 拿到的不只是一个工具签名——拿到的是一个**包含路由决策信息的小型说明书**。

---

### P1-1：搜索结果增加诊断字段

**当前 `kdo_search` 返回**：
```json
[{"id": "xxx", "title": "...", "snippet": "...", "score": 75.2}]
```

**目标**：每个结果追加：
```json
{
  "id": "xxx",
  "title": "...",
  "snippet": "...（从 120 字扩展到 300 字）",
  "score": 75.2,
  "score_label": "high",        // 🆕 high/medium/low — Agent 可直接判断
  "scene": ["execution"],       // 🆕 场景标签
  "audience": ["executor"],     // 🆕 受众标签
  "source_path": "30_wiki/...", // 🆕 完整路径，Agent 可自行 Read
  "one_liner": "评估三角形判断需求真伪" // 🆕 一句话价值描述
}
```

搜索结果为 0 时返回诊断体而非空列表：
```json
{
  "results": [],
  "diagnosis": {
    "query": "创新者的窘境",
    "indexed_at": "2026-08-02T22:00:00Z",
    "total_cards": 2500,
    "suggestion": "未找到匹配。尝试: ① 'Christensen 破坏性创新' ② kdo_graph('strategy') 浏览战略域 ③ 确认该主题卡片是否已入库但 aliases 缺失"
  }
}
```

**实现量级**：修改 `kdo-tools/mcp/tools.py` 的 search handler + `delivery.py` 的结果增强，~60 行。

---

### P1-2：MCP 工具间互引——建立工具路由网

每个 MCP 工具的 description 末尾加上"相关工具"段：

```
kdo_search  description 末尾追加：
━━━ 相关工具 ━━━
📌 kdo_read <卡id>   — 读取卡片全文（拿到 search 结果的 id 后调用）
📌 kdo_graph <域>     — 按域浏览卡片地图（不确定关键词时先查域结构）
📌 kdo_query <问题>    — 语义搜索（搜中文自然语言问题比 kdo_search 关键词更好）
```

```
kdo_graph  description 末尾追加：
━━━ 相关工具 ━━━
📌 kdo_search <关键词> — 精确关键词匹配
📌 kdo_read <卡id>     — 读到感兴趣的卡后看全文
```

**实现量级**：修改 `kdo-tools/mcp/tools.py` 中各 tool 的 description，每处追加 3-5 行。

**为什么重要**：外部 Agent 拿到工具列表后，如果没有工具间的路由信息，它不知道先用哪个、搜不到时换哪个。MCP 工具路由网 = Agent 的操作手册。

---

### P1-3：`kdo_read` 返回结构增强（帮助 Agent 判断卡片适用性）

**当前 `kdo_read`**：返回卡片的完整 markdown 正文。

外部 Agent 的问题：2,000 字的卡片全文读完需要消耗上下文，但如果只读 snippet 又不够判断相关性。

**方案**：`kdo_read` 返回三段式结构，Agent 可以渐进式读取：

```json
{
  "id": "framework-christensen-disruptive-innovation",
  "L1_summary": {
    "title": "破坏性创新理论",
    "type": "framework",
    "one_liner": "Christensen 破坏性创新核心框架——为什么大公司会被小公司颠覆",
    "domain": "strategy",
    "status": "reviewed",
    "confidence": 0.92
  },
  "L2_structure": {
    "sections": ["原始表述", "核心结构", "Critique", "Synthesis", "失败模式", "操作方法"],
    "related_count": 14,
    "cross_domain_count": 3
  },
  "L3_full_body": "## 原始表述\n\nChristensen 在《创新者的窘境》中..."
}
```

Agent 拿到 L1 就能判断相关性，需要时再读 L2/L3。避免为了一张不相关的卡消耗 2,000 token 上下文。

**实现量级**：新增 `kdo_read` 的 L1/L2 提取逻辑，在 `delivery.py` 或 MCP handler 中实现，~40 行。

---

### P2-1：外部 Agent "新人引导"——MCP tool `kdo_help`

新增一个 `kdo_help` MCP 工具，外部 Agent 首次接入时调用一次就能理解 KDO 的检索策略：

```
kdo_help 返回：
━━━ KDO 是什么 ━━━
一个经过人工审查的商业方法论知识库（2,500+ 张卡），覆盖战略、需求、决策、
洞察、模型、增长、壁垒、产品等域。每张卡包含框架、暗知识、案例、失败模式。
━━━ 怎么搜最有效 ━━━
1. 先用 kdo_search 做关键词/问题搜索 → 拿到卡 id 列表
2. 用 kdo_read(卡id) 读全文 → 判断是否适用
3. 搜不到时 → 换中文/英文关键词，或 kdo_graph 浏览域结构
4. 需要深度分析 → kdo_query 做语义检索
━━━ 常见搜索模式 ━━━
• "XX 是什么" → kdo_search("XX") 找 framework 卡
• "XX 怎么做" → kdo_search("XX") 找 tool 卡
• "有没有 XX 案例" → kdo_search("XX") 找 case 卡
• "XX 有什么坑" → kdo_search("XX 失败") 找 dk 卡
```

**实现量级**：新增一个 tool handler，返回静态 markdown，~30 行。

---

### P2-2：老顽童生产规范——新卡 MCP 可发现性自查

每张新卡提交前，老顽童跑一条自查命令：

```bash
python kdo-tools/mcp-reachability-check.py <卡id> --keywords "创新者的窘境,破坏性创新,Christensen"
```

输出：
```
✅ "破坏性创新" → kdo_search 返回该卡 (score 92.3)
✅ "Christensen" → kdo_search 返回该卡 (score 88.1)
❌ "创新者的窘境" → 未命中 → 建议在 aliases 中添加
❌ "颠覆式创新" → 未命中 → 建议在 aliases 中添加

综合可发现性: 2/4 命中 → 建议补全 aliases 后重新提交
```

**实现量级**：新脚本 `mcp-reachability-check.py`，调用现有 kdo_search 逻辑 + 推荐 aliases 补全建议，~80 行。

---

## 四、优先级矩阵

| 编号 | 内容 | 改动量 | assignee | 优先级 | 为什么先做 |
|:--|:--|:--|:--|:--:|:--|
| P0-1 | pre-submit title/aliases/tags 门禁 | ~30行 | 黄药师 | **P0** | 从源头阻止空 title 卡入库 |
| P0-2 | MCP tool description 场景化 | ~5行 | 黄药师 | **P0** | 5 行改动→所有外部 Agent 立刻受益 |
| P1-1 | 搜索结果增加诊断字段 | ~60行 | 黄药师 | **P1** | 搜不到时 Agent 不再"盲猜" |
| P1-2 | MCP 工具间互引路由 | ~20行 | 黄药师 | **P1** | 20 行改动→Agent 知道工具调用顺序 |
| P1-3 | kdo_read 三段式返回 | ~40行 | 黄药师 | **P1** | 减少 Agent 上下文浪费 |
| P2-1 | kdo_help 新人引导 | ~30行 | 黄药师 | **P2** | 新 Agent 接入体验从 40→80 分 |
| P2-2 | 可发现性自查脚本 | ~80行 | 黄药师+老顽童 | **P2** | 老顽童提交前自检，不消耗审查轮次 |

---

## 五、与现有基础设施的关系

| 现有资产 | 本次升级的关联 |
|:--|:--|
| 07-27 MCP 检索效率升级（aliases + RRF tag 匹配） | P1-1 诊断字段复用 RRF 的 tag match 结果 |
| 今天上线的 R1/R2 dk 门禁 | P0-1 同模式——在 validate_file() 中加三条 schema 级检查 |
| `kdo_lint.py` HINT_MAP（讲香升级 P0-1） | P0-2/P1-1 的消息设计共用同一套 HINT_MAP 模式 |
| `cap_hub/registry.py` | P1-2 工具路由网可复用 registry 中的 agent-spec 描述字段 |

---

## 六、验收标准

| 编号 | 验收标准 |
|:--|:--|
| P0-1 | `kdo pre-submit` 对 title 空的卡报 ERROR；对缺 aliases/tags 的卡报 WARN |
| P0-2 | 外部 Agent 调 `kdo_search` 失败后，能根据 tool description 中的建议尝试替代路径 |
| P1-1 | `kdo_search` 返回 0 条时带 `diagnosis.suggestion`；正常返回时每结果含 `score_label` + `scene` + `one_liner` |
| P1-2 | 每个 MCP tool description 末尾有"相关工具"路由段 |
| P1-3 | `kdo_read` 返回含 L1/L2/L3 三段，Agent 可仅读 L1 判断相关性 |
| P2-1 | 外部 Agent 调 `kdo_help` 返回结构化的新人引导文档 |
| P2-2 | `mcp-reachability-check.py` 对新卡跑关键词命中测试，输出通过/失败/建议补全 |

---

## 七、讲香视角总结

如果把 KDO MCP 接口当作一个"产品"，当前它处于 讲香 V1——所有功能正确，但外部 Agent 需要自己摸索"我什么时候用、搜不到怎么办、工具之间什么关系"。

这次升级的目标是把 MCP 接口从 V1 拉到 V3：
- **V1（当前）**：技术功能描述——Agent 知道工具能干什么
- **V3（目标）**：场景路由描述——Agent 知道什么时刻用什么工具、失败时走什么替代路径

核心原则来自 讲香 十指模型：
- **场景化**：tool description 用场景而非功能描述
- **口语化**：诊断消息用"你"而非"the user"
- **数字化+参照**：score_label（high/medium/low）给 Agent 可行动的判断基准
- **比喻化**：`kdo_help` 中的"万能插座"式新人引导
- **情绪化**：搜索失败不返回空，返回"试试这个"的路径感

---

*黄药师 · 2026-08-02*
*建议书状态：待王语嫣审阅后拆分为任务单入 production-queue，assignee 标注黄药师/老顽童/欧阳锋*
