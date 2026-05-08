---
title: "Kimi 深度调研集群方法论 (Deep-Research-Swarm)"
type: "concept"
status: "enriched"
domain: ['ai-saas']
source_refs: ["src_20260502_7d7c1b7c"]
created_at: "2026-05-01T18:49:20+00:00"
updated_at: "2026-05-04T00:00:00+00:00"
---

# Kimi 深度调研集群方法论 (Deep-Research-Swarm)

> **核心理念**：多智能体认知三角测量（Epistemic Triangulation）——在不同研究维度上发散，检测重叠与矛盾，深度验证，再收敛为经过验证的综合结论。集群并行服务于认知鲁棒性，而非仅仅追求速度。

---

## [Condense] 核心观点

1. **四路自适应路由（Phase 0）**：所有调研任务首先经过意图路由器，根据任务特征自动分类——Route A 广域搜索（宽泛主题）、Route B 聚焦搜索（具体问题）、Route C 纯文件研究（零外部搜索）、Route D 文件增强研究（文件为主+外部补充）。路由信号来自文件存在性和用户措辞。

2. **认知重置规则（Epistemic Reset Rule）**：假设内部知识可能过时，始终先获取当前时间。时间敏感性约束为硬约束。外部证据优先于内部知识。禁止先搜索后叙事——在搜索输出前不得生成任何事实性声明。

3. **两阶段集群架构（Route A）**：Phase 1W 广域探索（≥5 Agent，每 Agent ≥10 次搜索）追求覆盖广度 → Phase 3 并行深度挖掘（≥10 Agent，每 Agent ≥20 次搜索）追求深度。搜索预算梯度：Route A ≥250 次 / Route B ≥200 次 / Route D ≥150 次 / Route C 0 次。

4. **维度分解规则**：≥10 个强制性维度，从截然不同的角度切入，≥30% 概念重叠创造交叉验证压力。每个维度覆盖当前状态、关键证据、张力与反论。

5. **四层置信度体系（Phase 4）**：High（≥2 Agent 独立确认）、Medium（1 Agent 权威来源）、Low（薄弱来源）、Conflict Zone（统计/解释分歧，显式记录不压制）。

6. **文件优先原则（Route C/D）**：Route C 严格零外部搜索（保真度至上），Route D 以文件为主+外部搜索填补空白，外部来源不掩盖用户提供的材料。

7. **洞察提取（Phase 6）**：洞察是从跨维度比较中涌现的高层推论——非现有发现的重复。体裁感知：报告优先战略洞察，学术论文优先研究空白与理论张力。最低 5 条洞察。

---

## [Critique] 批判性评估

### 前提假设
- 假设子 Agent 能自主执行 ≥20 次独立搜索并区分权威来源与内容农场。【可靠性：低】中文搜索生态中内容农场和 SEO 污染严重，弱 Agent 无法有效过滤噪音，可能系统性降低研究质量。
- 假设 ≥15 Agent 并行 + ≥250 次搜索的预算在实际部署中可接受。【可靠性：中】——Kimi API 的定价模型下，一次完整 Route A 调研的 API 调用费用可能达到数十元甚至上百元。对高频使用场景成本不可忽视。
- 假设维度分解中 ≥30% 概念重叠可被"编排器主观判断"有效管理。【可靠性：低】——当前缺乏自动化重叠度度量方法，人工判断无法规模化。

### 边界与反例
- 最适合：需要多维度交叉验证的复杂主题研究（政策分析、行业调研、学术文献综述）。
- 不适合：简单事实查询（用搜索引擎更快）、时效性极高的事件（集群编排的延迟不适合突发新闻）。
- Route C 的"零外部搜索"在实际执行中难以监督——Agent 可能"偷偷"依赖训练数据中的外部知识而声明"来自文件"。

### 可靠性评估
**整体可靠性：中高。** 方法论设计严密，路由体系覆盖了主要的调研场景类型。认知三角测量的思想在认识论上有坚实基础。主要风险在执行层——Agent 质量、搜索生态噪音、成本控制。需要对 Agent 能力建立持续的 eval 基准，而非假设 Agent 每次都能正确执行。

### 关键未解决问题
- 引用溯源链路断裂风险：子Agent 输出的 `[^number^]` 引用在 Phase 4-6 的综合重写中如何保持完整可追溯？跨文档引用合并时的编号冲突如何解决？
- 输出文件的长期管理：多次研究任务产生的 `/mnt/agents/output/research/` 文件如何被索引、复用、避免知识沉淀流失？这恰是 KDO 可以解决的问题——将 Deep Research 的输出对接 KDO 的 inbox 入口。

---

## [Synthesis] 对标与迁移

### 关联概念
- [[graph-rag]] — Deep Research 的跨维度交叉验证需要 Graph RAG 作为知识导航层。集群输出的 dim/cross_verification/insight 文件如果接入 KDO wiki，就是天然的 Graph RAG 数据源。
- [[kdo-protocol]] — Deep Research 的 7-Phase 管线可以与 KDO 的 9 步循环对接：Research Phase 6-7 的输出 → KDO inbox → ingest → wiki → produce。
- [[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]] — Software Factories 模式在调研领域的完美实例：人定义研究问题+维度（写 spec），AI 集群执行搜索+交叉验证（生成实现），人做洞察确认和方向修正（测试验证）。

### 互补与冲突
- 互补：KDO 的三步编译法（Condense→Critique→Synthesize）与 Deep Research 的 Phase 4-6（交叉验证→冲突解决→洞察提取）在逻辑上高度对应。KDO 是"慢知识"的结构化沉淀，Deep Research 是"快研究"的深度探索。
- 差距：当前 Deep Research 的输出是临时文件（`/mnt/agents/output/research/`），缺少与 KDO 知识库的结构化对接。每次研究的成果无法累积为可复用的 wiki 概念卡——这正是 P2 阶段需要建的"Research → Inbox"连接器。

### 可迁移到 KDO 的改进
- 把 Phase 0 的"意图路由"逻辑应用到 KDO 的 `kdo query` 命令——根据查询特征自动选择检索深度和 wiki 遍历范围。
- 把四层置信度体系引入概念卡的 trust_level 字段——当前只用 high/medium/low，可以细化为"独立确认/权威来源/薄弱/冲突区"。
- 建立 Deep Research → KDO inbox 的自动导入管道——研究完成后自动 `kdo capture` 关键发现。

---

## 四路路由速查

| 路线 | 场景 | 搜索预算 | 核心特点 |
|------|------|:------:|---------|
| Route A | 宽泛/探索性主题 | ≥250 次 | 两阶段：先广度后深度 |
| Route B | 具体/有界问题 | ≥200 次 | 标准 7-Phase 流程 |
| Route C | 仅基于上传文件 | 0 次 | 零外部搜索，保真度至上 |
| Route D | 文件参考+外部补充 | ≥150 次 | 文件为主，外部填补空白 |

## Source Refs

- `src_20260502_7d7c1b7c` -> `10_raw/sources/src_20260502_7d7c1b7c-kimi-深度调研集群方法论-deep-research-swarm.md`

## Open Questions

- ≥15 Agent并行+≥250次搜索的API调用费用和端到端延迟是否可接受？
- Route C（纯文件）中跳过Phase 5后，如何确保低置信度发现或文件间矛盾不被带入最终制品？
- 维度分解中≥30%概念重叠的"交叉验证压力"如何量化？
- Phase 1W的广域探索维度如何保证不遗漏关键视角？是否有回退机制？
- 中文搜索生态与英文搜索生态的来源质量差异如何处理？
- 输出文件的长期管理和检索机制是什么？

## Output Opportunities

- Content: 深度研究方法论对比分析报告（Kimi vs Perplexity vs Google Deep Research）
- Code: KDO 技能封装 — 将此方法论实现为 `kdo research` 命令的编排脚本
- Capability: deep-research agent swarm 编排器（可复用的研究技能）
