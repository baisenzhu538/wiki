---
id: sprint-11-cognitive-upgrade-framework
title: "Sprint 11：AI思维卡素材 ingest + 认知升级十步框架萃取"
status: completed
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: master
created: 2026-05-15
target: 2026-05-16
---

## 背景

新素材入仓：

| 文件 | 类型 | 内容 |
|------|------|------|
| `00_inbox/《人工智能：一种现代方法》-AI思维卡.html` | HTML | 一份完整的深度阅读产物——用"认知升级系统 v3.2"十步框架读 AI 教科书 AIMA 的产出 |

这份材料有两层价值：一是对 AI 教科书（PEAS + Agent 架构）的深度理解，二是它使用的**阅读方法论本身**——IDENTITY→MODEL→EVIDENCE→CONTRAST→ACTION→REFLECTION→MY TAKE→ICAP→CTA→FOLLOWUP 十步框架。

欧阳锋已完成方法论分析，工业化手册已升级至 v1.4。黄药师需走标准 KDO 管线完成素材摄入和知识萃取。

## Phase 1：素材归档

1. HTML → Markdown 转换（保留结构）
2. `kdo ingest` → `10_raw/sources/`
3. 提取原文中引用的外部链接归档到 `00_inbox/links/`

## Phase 2：建卡

建议产出 **2 张卡**：

### 2a. framework：`yt-model-cognitive-upgrade-framework`（认知升级十步框架）

萃取那套阅读方法论本身。核心内容：
- 十步流程（IDENTITY→MODEL→EVIDENCE→CONTRAST→ACTION→REFLECTION→MY TAKE→ICAP→CTA→FOLLOWUP）
- 每步的核心问题和产出
- 与我们 KDO 三步编译法的对标（不是替代，是延伸）
- 三个差异化设计：旧 Bug→新 Patch 追踪、ICAP 自评阶梯、EVIDENCE 三件套

Constraints 至少 3 条，须覆盖：
- 框架适用边界（完整书 vs 碎片化输入）
- ICAP 自评的自我欺骗风险
- CTA 设计质量决定转化率

> **v1.5 要求**：此卡为工业化手册 §1.7 的第一张 framework 实例——外部攻击、不要用场景、Action Triggers 三个新节均为必填。标准见 `90_control/kdo-industrialization-manual.md` §1.7。

### 2b. tool：`yt-tool-peas-agent-analysis`（PEAS 智能体分析工具）

从 AI 思维卡内容中提取 PEAS 四元组 + 5 层 Agent 架构作为一张可操作的自我诊断工具卡。

核心内容：
- PEAS 四元组定义 + 自我反思问题
- 5 种 Agent 架构层级（Simple Reflex → Learning Agent）
- 场景速查：接新项目时、反复做不好时、做重要决定时

Constraints 至少 2 条：
- PEAS 在 P 本身有争议的领域（养育/艺术/关系）会卡住
- 5 层架构不完全适用于神经网络时代（LLM 是混合体）

> **v1.5 要求**：此卡为工业化手册 §1.7 的第一张 tool 实例——外部攻击、不要用场景、Action Triggers 三个新节均为必填。

## Phase 3：跨域图边

| 卡片 | 操作 |
|------|------|
| `yt-model-ipo-learning-strategy` | `related` 新增认知升级框架（IPO 在深度阅读场景的强化版） |
| `yt-model-prompt-engineering` | `related` 新增认知升级框架（AI 作为阅读伙伴嵌入 EVIDENCE/CONTRAST 环节） |
| `yt-concept-ai-guard-brain` | `related` 新增认知升级框架（十步框架是守脑如玉的操作系统实现） |

## 不做

- ❌ 不建 PEAS 相关的全套卡片树（其余 tool 卡后续按需）

## 质量门禁

> **v1.5 新标准**：本 Sprint 的两张卡（1 framework + 1 tool）是工业化手册 v1.5 卡片层行为转化三要件的第一批实例。三个新节均为必填。

- [ ] `kdo lint` → 0 errors
- [x] `kdo lint` → 0 errors ✅

---
## 交付报告 (2026-05-15)

### 产出表

| Phase | 产出 | 路径 | 状态 |
|-------|------|------|------|
| 1a | HTML→MD 转换 | `10_raw/sources/aima-ai-thinking-card-20260515.md` | ✅ |
| 1b | kdo ingest 归档 | `10_raw/sources/aima-ai-thinking-card-20260515.html` | ✅ |
| 1c | 外部链接提取 | `00_inbox/links/aima-ai-thinking-card-links.md` | ✅ |
| 2a | framework 卡：认知升级十步框架 | `30_wiki/concepts/yt-model-cognitive-upgrade-framework.md` | ✅ |
| 2b | tool 卡：PEAS 智能体分析 | `30_wiki/concepts/yt-tool-peas-agent-analysis.md` | ✅ |
| 3 | 跨域图边（3张卡 related 更新） | `yt-model-ipo-learning-strategy`, `yt-model-prompt-engineering`, `yt-concept-ai-guard-brain` | ✅ |

### 质量检查

| 检查项 | 结果 |
|--------|------|
| `kdo lint` errors | **0** ✅ |
| 2 张新卡 Constraints ≥ 2 | ✅ framework 3条，tool 2条 |
| 3 张关联卡 related 已更新 | ✅ 全部含 `yt-model-cognitive-upgrade-framework` |
| framework 卡 Burn line | ✅ 「读书不是为了知道更多，而是为了下一次做决定时，脑子里响起的不是旧 Bug 而是新 Patch」 |
| v1.5: Critique 外部攻击子节 | ✅ 两张卡各有 ≥1 条真实外部批评 |
| v1.5: Synthesis 不要用的场景表 | ✅ framework 3条，tool 3条（均含失效机制+替代方案） |
| v1.5: Action Triggers 节 | ✅ 各 3 个触发场景+第一动作+成功指标 |
| source_refs 指向 `10_raw/` | ✅ 两张卡均指向已归档文件 |
| query_triggers 真实搜索词 | ✅ 中文搜索词，非 section header |

### 已知项

- `kdo lint` source_refs "missing or empty" warning：已知假阳性，影响全库约 150 张卡，非本 Sprint 引入。两张新卡 source_refs 均已正确指向 `10_raw/` 目录下的已归档文件。
- `kdo lint` "orphan page" / "not listed in index" warning：新卡预期行为，待后续跨域边建设自然消解。

### 延后项

无。Sprint 11 全部 Phase 完成。
- [ ] 2 张新卡 source_refs 指向 `10_raw/`
- [ ] 每张新卡 Constraints ≥ 2 条，满足理解门禁
- [ ] 每张新卡 query_triggers 为真实搜索词（非 section headers）
- [ ] 3 张关联卡 `related` 已更新
- [ ] framework 卡含 Burn line
- [ ] **（v1.5 新增）** 每张卡 Critique 含"外部攻击"子节（≥1 条真实外部批评，不带 straw man）
- [ ] **（v1.5 新增）** 每张卡 Synthesis 含"不要用的场景"表（≥2 条：场景+失效机制+替代方案）
- [ ] **（v1.5 新增）** 每张卡含 `## Action Triggers` 节（≥3 个触发场景 + 第一动作 + 成功指标）
