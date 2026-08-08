---
id: case-truman-ai-image-workflow-evolution
title: 「案例：Truman作图工作流进化——从3小时一张到日产30-40张」
type: case
status: draft
confidence: 0.92
trust_level: high
domain:
  - ai-basic
  - ai-collaboration
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
source_person: Truman
source_context: Truman口述下 L446-552（作图工作流三阶段进化）
reviewed_by: 待审
aliases:
  - 作图工作流
  - Feature叠加
  - 日产30张
discoverable_by:
  - 作图
  - 工作流
  - Feature叠加
  - 日产30张
related:
  - framework-truman-feature-thinking-core
  - framework-truman-feature-layered-system
  - concept-truman-feature-four-scenarios
  - 10_raw/sources/feature-periodic-table-v0.8.json
  - case-truman-investment-daily-report
tags:
  - method:feature-thinking
  - method:workflow
  - scene:ai-image
  - audience:practitioner
  - content-format:case
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - cited
  - validated
diagnostic_signals:
  - signal: "AI作图质量不稳定，一张图要花几个小时"
    lens: 可能只用了一个Feature（提示词）→ 需要叠Feature
    follow_up: 先加换模型+版本管理，稳定后再加抽卡+Skill+多Agent
---

> 本卡属于 [[framework-truman-feature-layered-system]] 的案例层——L1→L2→L3 Feature叠加的完整实证。

# Truman作图工作流进化：从3小时一张到日产30-40张

> 一句话：一年前3小时出不了一张60分的图，抽卡成功率仅10%。叠了换模型+版本管理+抽卡+Skill+多Agent后，成功率50-70%，日产30-40张。不是换了更好的工具，是叠了更多Feature。

---

## 三阶段

| 阶段 | Feature | 效果 | 行号 |
|:---|:---|:---|:---|
| **第一阶段** | 只有提示词（超长手敲提示词→AIGC） | 3小时出一张，连60分都达不到 | L454-460 |
| **第二阶段** | +换模型（换Moderna）+Prompt版本管理（V1→V2→V3→V4） | 能用了——一定程度上拿得出手 | L468-488 |
| **第三阶段** | +抽卡测试+模型组合+先澄清再执行+Skill封装×3（品位/设计宪法/复盘）+多Agent分工（5个设计师并行） | 成功率50-70%，日产30-40张 | L504-524 |

---

## 为什么第一阶段不行

"只用了这一层的功能，而且非常原始，非常差"（L464）。纯提示词工程的瓶颈：AIGC出图不稳定、文字无法控制、流程跑偏。抽卡成功率仅10%——"可能得搞20张图才能勉强有一张有用的"（L490）。

## 第二阶段的关键：换模型+版本管理

两个Feature的叠加：①换模型——换Moderna，"蹭的一下就上去了"（L468）；②版本管理——不反复重写提示词，而是在一个版本上持续迭代V1→V2→V3→V4（L472-474）。

## 第三阶段：工业化

从"能做"到"能批量做"。叠了5个Feature（L504-524）：模型组合（Bruna 1-2）、抽卡测试、先澄清再执行、Skill封装×3、5个Agent并行出图。

**成功率从10%→50-70%，日产30-40张**（L522-524）。

---

## Feature叠加清单

| 步骤 | Feature | 来源 |
|:---|:---|:---|
| 1 | 提示词工程 | L1 |
| 2 | 换模型 | L1 |
| 3 | Prompt版本管理 | L2 |
| 4 | 模型组合+抽卡测试 | L1+L3 |
| 5 | 先澄清再执行 | L2 |
| 6 | Skill封装×3 | L3 |
| 7 | 多Agent分工 | L4 |

---

## 关键数字

| 数据 | 来源 | 状态 |
|:---|:---|:---|
| 初期3小时/张，成功率10% | 口述下 L456/L490 | ✅ 可核实 |
| 第三阶段成功率50-70%，日产30-40张 | 口述下 L522-524 | ✅ 可核实 |

## 教训

1. **一个Feature不够就叠——不是换工具，是叠Feature**
2. **版本管理是工业化的第一步**——从"重写提示词"到"迭代版本"
3. **Skill封装=把验证有效的Feature组合冻结为可复用资产**

## 可迁移场景

| 场景 | 迁移 |
|:---|:---|
| 任何AI生成任务（文案/代码/设计） | 先看你在第几阶段——如果还只靠提示词，叠Feature |
| B2B内容批量生产 | 从"能做一个"到"能批量做"=Feature叠加的工业化路径 |

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 跳过第二阶段直接上多Agent | 基础不稳定→Agent协作更乱 | 先做到"换模型+版本管理"稳定后再上Agent |
| 叠了Feature但没测成功率 | 不知道哪个Feature有效 | 每加一个Feature记录成功率变化 |
