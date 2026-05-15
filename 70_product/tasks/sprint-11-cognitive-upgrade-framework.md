---
id: sprint-11-cognitive-upgrade-framework
title: "Sprint 11：AI思维卡素材 ingest + 认知升级十步框架萃取"
status: pending
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

### 2b. tool：`yt-tool-peas-agent-analysis`（PEAS 智能体分析工具）

从 AI 思维卡内容中提取 PEAS 四元组 + 5 层 Agent 架构作为一张可操作的自我诊断工具卡。

核心内容：
- PEAS 四元组定义 + 自我反思问题
- 5 种 Agent 架构层级（Simple Reflex → Learning Agent）
- 场景速查：接新项目时、反复做不好时、做重要决定时

Constraints 至少 2 条：
- PEAS 在 P 本身有争议的领域（养育/艺术/关系）会卡住
- 5 层架构不完全适用于神经网络时代（LLM 是混合体）

## Phase 3：跨域图边

| 卡片 | 操作 |
|------|------|
| `yt-model-ipo-learning-strategy` | `related` 新增认知升级框架（IPO 在深度阅读场景的强化版） |
| `yt-model-prompt-engineering` | `related` 新增认知升级框架（AI 作为阅读伙伴嵌入 EVIDENCE/CONTRAST 环节） |
| `yt-concept-ai-guard-brain` | `related` 新增认知升级框架（十步框架是守脑如玉的操作系统实现） |

## 不做

- ❌ 不建 PEAS 相关的全套卡片树（其余 tool 卡后续按需）

## 质量门禁

- [ ] `kdo lint` → 0 errors
- [ ] 2 张新卡 source_refs 指向 `10_raw/`
- [ ] 每张新卡 Constraints ≥ 2 条，满足理解门禁
- [ ] 每张新卡 query_triggers 为真实搜索词（非 section headers）
- [ ] 3 张关联卡 `related` 已更新
- [ ] framework 卡含 Burn line
