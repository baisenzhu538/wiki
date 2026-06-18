---
id: sk-ai-prd-for-ai
title: 技能：把PRD写成AI能执行的指令
type: tool
status: enriched
domain:
- ai-collaboration
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地分享，2026-06
source_refs:
- 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md
wiki_refs:
- '[[sk-ai-problem-validation]]'
- '[[prd-as-ai-instruction]]'
- '[[sk-ai-question-problem-checklist]]'
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/prompt'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 笔记本和笔
prerequisite_skills: null
related:
- '[[sk-ai-problem-validation]]'
- '[[prd-as-ai-instruction]]'
- '[[sk-ai-question-problem-checklist]]'
author: 半肥猫
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 原始来源未明确支持"PRD不是给人看的，是给AI看的"及"3-5倍输出质量提升"等核心表述
  framework_lens: source-fidelity
  follow_up_question: 请提供半肥猫分享中关于PRD作为AI可执行指令的具体原文，或补充另一份来源以支撑该主张？
- signal: source_person（半肥猫）与来源文件演讲者（季浩/纪浩）不一致，作者归属存疑
  framework_lens: authorship-attribution
  follow_up_question: 是否需要将source_person更正为纪浩，或找到半肥猫对应分享的原始记录？
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

- [ ] 已明确产品背景、市场需求与业务目标
- [ ] 已定义目标用户和核心使用场景
- [ ] 已把需求拆分为可执行的步骤/用户流程
- [ ] 每步都写明了验收标准（什么算对）
- [ ] 已列出成功指标、潜在风险和验证计划
- [ ] 已用Markdown/表格结构化呈现PRD
- [ ] 已和关键利益方对齐PRD边界（避免第一版过大）
- [ ] 已让AI按PRD执行并对比输出是否符合预期

## 相关卡/互链

- [[sk-ai-problem-validation]] —— 先验证问题是否值得交给AI
- [[prd-as-ai-instruction]] —— PRD作为AI指令的专门卡片
- [[sk-ai-question-problem-checklist]] —— 把模糊需求澄清为可执行问题

## 来源

- `10_raw/sources/src_20260606_90b44191-没有人呀现在.md:438-568`

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
