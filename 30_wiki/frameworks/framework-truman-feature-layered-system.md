---
id: framework-truman-feature-layered-system
title: 「框架：Feature分层体系——L0-L5六层+分层自洽」
type: framework
status: draft
confidence: 0.93
trust_level: high
domain:
  - ai-basic
  - methodology
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（上）-口述.txt
  - 00_inbox/AI基本功/OCR_周期表_M3重试_按层整理.md
  - 10_raw/sources/feature-periodic-table-v0.8.json
source_person: Truman
reviewed_by: 待审
aliases:
  - Feature分层
  - L0-L5
  - 分层自洽
  - Feature周期表
discoverable_by:
  - Feature分层
  - L0-L5
  - 分层自洽
  - 周期表
  - AI能力体系
  - truman的feature分类
  - feature有哪些
  - feature怎么分
  - 周期率表
related:
  - framework-truman-feature-thinking-core
  - concept-truman-feature-four-scenarios
  - concept-truman-feature-six-stages
  - tool-Truman-Feature特性层训练法
  - agent-spec-复盘教练
  - framework-一堂-关键假设
  - '[[bridge-coaching-leadership-feature-layered]]'
  - '[[bridge-dual-track-feature-system]]'
  - '[[case-live258-europe-cold-email]]'
  - '[[case-live258-fact-spread-18-bridges]]'
  - '[[case-live258-livestream-prompt-v1-v5]]'
  - '[[case-live258-zhihu-content-acquisition]]'
  - '[[case-truman-ai-image-workflow-evolution]]'
  - '[[case-truman-investment-daily-report]]'
  - '[[case-truman-temperature-parameter]]'
  - '[[concept-yihang-dual-triangle-core]]'
  - '[[dk-ai-does-not-question-your-mistake]]'
  - '[[concept-yihang-ai-feature-thinking]]'
  - '[[dk-demand-feature-stacking]]'
  - '[[dk-feature-pieces-not-recognized-as-cards]]'
  - '[[framework-coaching-leadership-core]]'
  - '[[framework-leadership-five-ladders]]'
  - '[[agent-spec-basic-skills-coach]]'
  - '[[tool-ai-feature-inventory]]'
  - '[[tool-feature-review-five-step]]'
  - '[[tool-leadership-consensus-goal-escalation]]'
tags:
  - method:feature-thinking
  - method:architecture
  - scene:ai-learning
  - audience:general
  - content-format:framework
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - principle
  - cited
diagnostic_signals:
  - signal: "在高层Feature（Agent）上花了很多时间但效果不好"
    lens: 可能违反分层自洽——下层能解决的不应上上层
    follow_up: 检查：这个问题在L1提示词层能不能解决？能→不要上L3 Agent层
  - signal: "不知道该从哪一层开始学Feature"
    lens: L2提示词层是最佳入口——门槛最低、覆盖面最广
    follow_up: 从L2的"最终意图/负面限制/Few-shot"三个Feature开始
---

> 本卡属于AI基本功域——Feature分层体系L0-L5六层+分层自洽原则。完整周期表见 `10_raw/sources/feature-periodic-table-v0.8.json`（100 个 Feature）。

# Feature分层体系：L0-L5六层+分层自洽

> 一句话：Feature从底层的"选模型、调温度"到顶层的"组织AI化设计"，分为六层。核心原则：能在下层解决，不上上层——"如无必要，勿增实体"。

---

## 六层总览

## 发现过程的诚实标注

这套分层体系不是自上而下设计的——Truman的原始过程是反的（口述上L324-364）：

> "我过去1到2年的时间，我解决过的各种还不错的问题，我开始一个两个去找那些长期不变的零件。赋予角色好使、思维链分步好使、分层自洽好使、参考案例好使、反向确认好使……找着找着发现好像真的有很多这种元器特性。后来我开始提一个大胆设想——有没有可能在中间插一层特性层？没有底层那么难、数量没有那么多（几十到一百这个量级）、正常人的智商可以理解。"

**真实路径：2年实践积累约49个原子 → 春节回溯总结 → 归纳为L0-L5六层。不是先有框架再填内容，是先有内容再长出框架。**

| 层 | 名称 | 核心问题 | Feature数 | 典型Feature |
|:---|:---|:---|:---|:---|
| **L0** | 基础模型 | 用什么模型？ | 3 | 模型选择/模型组合/模型调优 |
| **L1** | 模型调优 | 怎么调参数？ | 14 | 温度/Top-K/换模型/微调 |
| **L2** | 提示词层 | 怎么写提示词？ | 34 | 最终意图/负面限制/Few-shot/状态机 |
| **L3** | 能力流程 | 怎么封装成可复用能力？ | 14 | Skill封装/Workflow/API调用 |
| **L4** | Agent层 | 怎么让AI自主工作？ | 18 | 角色配置/长期记忆/ReAct/心跳 |
| **L5** | 组织层 | 团队怎么AI化？ | 13 | 角色分工/共享资源/Agent编排 |

---

## 分层自洽原则

> "能在下一层实现的功能，优先选择下一层实现——避免过度复杂化。"（口述上 L330-334，Skill分层自洽概念）

| 原则 | 含义 | 反例 |
|:---|:---|:---|
| 下层优先 | L1能解决的不上L2，L2能解决的不上L3 | 最终意图就能对齐的需求，不需要建一个Agent |
| 最小复杂度 | 每上一层的成本（开发/维护/理解）指数增长 | 一个Agent需要角色+记忆+工具+监控——而一个提示词只需要一段文本 |
| 自洽验证 | 选错层的症状：过度设计（上层解决下层问题）或力不从心（下层解决上层问题） | 用Agent做一个固定格式的摘要→L2就够了 |

**最佳入口**：L2提示词层——门槛最低、覆盖面最广、学习成本最低。从"最终意图/负面限制/Few-shot"三个Feature开始。

---

## 层间桥接

| 本体系层 | KDO对应 | 说明 |
|:---|:---|:---|
| L2 提示词 | KDO提示词模板/Skill参数 | Feature是原子能力，Skill是封装后的可调度单元 |
| L3 能力流程 | KDO Skill/workflow | "用自然语言封装Skill"=KDO Skill的定义方式 |
| L4 Agent | KDO agent-spec | Agent=角色+记忆+工具+协作的完整封装 |
| L5 组织 | KDO编排/多Agent系统 | 王语嫣编排=组织层Feature的实战 |

---

## Critique

分层自洽的风险：过度机械套用会导致"能用L2但硬上L3"的炫耀性复杂化。判断标准——不是"能不能用更高层做"，是"用更高层做是否带来了足够多的额外价值"。如果L3的Agent只比L2的提示词多了"自动保存对话记录"——不值。

## When NOT to Use
- 一次性任务——不需要建分层体系
- 团队还没有L2基础时不要跳L3/L4——"下层没练熟，上层站不稳"

---

## 终审记录（#544 批次 · 2026-08-26 · 欧阳锋）

**结论：退回补内容（不升 reviewed）**

**通过维度**：发现过程诚实标注溯源命中（口述上 L324-364 特性层设想 / L394「四十九个」/ L436-452 春节分层）✅；related 25 条；diagnostic_signals 已填；定位声明在（L82）。

**P1-1 六层表数字与源不符（L100-107）**：L2 提示词层记 34，源 `10_raw/sources/feature-periodic-table-v0.8.json` 实测 L2=38（json 统计：L0=3/L1=14/L2=38/L3=14/L4=18/L5=13，合计 100）。卡片六层合计 96，与 L82 自述「100 个 Feature」自相矛盾。

**P1-2 引语行号误植（L113）**：「能在下一层实现的功能，优先选择下一层实现——避免过度复杂化。（口述上 L330-334）」——L330-334 实文仅「Skill有一个非常重要的特性叫分层自洽很好使」（L334），无此句。该原则真实出处=口述上 L1300（ASR 原文「如果能在下一实现的东西呢，一定要跟在上一层做实现」）。

**期望形态**：① L2 改 38（或注明与 v0.8 的版本差异及依据）；② L113 引语改正确行号+原文，或去引号改述；③ 修复后复审走对照法（逐项 grep 验证）。
