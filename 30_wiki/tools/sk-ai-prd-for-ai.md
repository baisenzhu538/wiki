---
id: sk-ai-prd-for-ai
title: 技能：把PRD写成AI能执行的指令
type: tool
status: reviewed
domain:
- src_unknown
- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地分享，2026-06
aliases:
  - 半肥猫
  - 技能
  - 技能：把PRD写成AI能执行的指令
  - 把PRD写成AI能执行的指令
  - 能执行的指令
  - 行的指令
source_refs:
- 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md
wiki_refs:
- src_unknown
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tags:
- src_unknown
- src_unknown
- src_unknown
- audience:executor
- scene:execution
- skill-level:intermediate
created_at: '2026-06-06'
updated_at: '2026-06-28'
tools_required:
- src_unknown
prerequisite_skills: null
related:
- '[[tool-ai-prd-for-ai]]'
- '[[prd-as-ai-instruction]]'
- '[[tool-纪浩-Agent技能市场设计法]]'
- '[[case-truman-prd-checklist-evolution]]'
- '[[tool-月白-AI改图指令精细化]]'
- '[[tool-ban-fei-mao-jiang-xue-xi-cheng-guo-chen-dian-wei-prd-wen-dang]]'
- '[[dk-ai-builder-illusion]]'
- '[[agent-spec-codex-teammate]]'
author: 半肥猫
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- framework_lens: source-fidelity
  follow_up_question: 请提供半肥猫分享中关于PRD作为AI可执行指令的具体原文，或补充另一份来源以支撑该主张？
- framework_lens: authorship-attribution
  follow_up_question: 是否需要将source_person更正为纪浩，或找到半肥猫对应分享的原始记录？
- 时代要不要练笔记
- 需要练那个
---

# 技能：把PRD写成AI能执行的指令

## 用一句话讲清楚

把需求写成结构化、带验收标准和上下文的PRD，让AI能够按步骤执行并自检，从而减少返工、提升输出质量。

## 核心要点

| 维度 | 说明 |
|---|---|
| **核心目标** | 让PRD从"给人读"变为"给AI执行" |
| **关键输入** | 产品背景、市场需求、目标用户、核心场景、约束边界 |
| **关键输出** | 一份结构化的PRD：用户流程 + 验收标准 + 成功指标 + 风险与验证计划 |
| **结构化语言** | 用Markdown、表格、清单取代大段自然语言描述 |
| **验收标准** | 每步输出明确"什么算对"，AI执行后可自检 |
| **人的角色** | 定义边界、把控审美、指出具体缺陷、最终确认关键假设 |
| **AI的角色** | 按PRD执行、输出草案、自查是否满足验收标准 |

## 边界

| 边界 | 说明 |
|---|---|
| **适用任务** | 可被分解为步骤的开发/设计/分析类任务 |
| **不适用** | 高度创意发散、无明确验收标准、需实时人工判断的任务 |
| **版本范围** | 第一期只做最小可用范围，避免大而全 |
| **来源约束** | 必须基于已验证的业务场景和真实需求 |
| **不替代人工终审** | PRD再结构化，关键假设和P0级问题仍需人确认 |

## 失败模式

| 失败模式 | 典型症状 | 原因 | 修复/预防 |
|---|---|---|---|
| 用自然语言写需求 | AI输出偏离预期 | 缺少结构化约束和验收标准 | 改用Markdown/表格/清单，明确每步输出 |
| 缺少上下文 | AI无法判断业务背景 | 未提供产品背景、目标用户、市场依据 | 在PRD开头补齐背景与约束 |
| 跳过验收标准 | AI输出"看起来对但不好用" | 未定义"什么算对" | 每步必须写明验收标准和成功指标 |
| 第一版做太全 | 项目越做越偏，无法落地 | 边界不清，贪多 | 先交付最小可用版本，验证后再迭代 |
| 把AI结论当事实 | AI给出很顺的推理但缺证据 | 未要求引用信源和标注出处 | 强制AI标注来源，并人工复核关键数据 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

**Martin Fowler**（软件架构大师，《重构》作者）会质疑：把 PRD 写成"AI 能执行的指令"本质上是把需求文档退化为"伪代码"——这违背了 PRD 的核心价值：沟通"为什么做"而非"怎么做"。当 PRD 变成执行指令，业务上下文和用户洞察会被结构化格式挤出。

- **具体假设**：该技能假设"把 PRD 写成结构化指令就能让 AI 可靠执行"，但当前大模型在处理超长结构化指令时存在注意力衰减——PRD 越详细，AI 对末尾要求的遵从率反而下降。
- **边界**：适用于可分解为明确步骤的开发/分析任务，但对需要跨文档推理、多轮交互演进的复杂任务（如架构设计、用户研究），结构化 PRD 可能过度约束 AI 的探索能力。
- **反例**：高度创意类任务（如品牌命名、广告创意）如果用结构化 PRD 约束，反而会限制 AI 的发散能力——验收标准越明确，输出越平庸。
- **前提**：框架假设"每步可以定义验收标准"，但在探索性任务中（如"找到新的增长机会"），验收标准本身就是未知的——该前提在探索阶段失效。
