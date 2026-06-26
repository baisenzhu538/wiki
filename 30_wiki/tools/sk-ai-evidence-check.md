---


id: sk-ai-evidence-check
title: 技能：AI输出证据核查三问法
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
author: 半肥猫
reviewed_by: 欧阳锋
confidence: 0.88
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地分享，2026-06
source_refs:
- 10_raw/sources/src_20260606_90b44191-没有人呀现在.md
wiki_refs:
- '[[sk-ai-question-problem-checklist]]'
- '[[sk-ai-parallel-validation]]'
related:
  - '[[tool-ai-problem-validation]]'
  - '[[tool-ai-prd-for-ai]]'
  - '[[tool-ai-evidence-check]]'
  - '[[sk-ai-old-small-checklist]]'
  - '[[sk-ai-prd-for-ai]]'
  - '[[sk-ai-question-problem-checklist]]'
  - '[[sk-ai-parallel-validation]]'
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 数据管理工具（Notion / Airtable 等）
prerequisite_skills: null
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
trust_level: medium

---
# 技能：AI输出证据核查三问法

## 用一句话讲清楚

每次AI给出结论后，用“依据是什么、有无具体证据、是否来自上下文”三问，快速识别并阻断AI的编造风险。

## 核心要点

- **三问核查**：Q1 检查结论依据是否存在；Q2 检查证据是否具体；Q3 检查来源是否来自输入上下文。
- **预防性提示**：在初始 prompt 中要求AI列明支撑结论的具体依据，并标注非上下文来源。
- **动作闭环**：根据三问结果，要求AI重答、在上下文内寻找证据，或明确标注补充内容。

## 边界

- 适用于基于文本/数据的判断型AI输出，不适用于纯创意生成或开放性头脑风暴。
- 需要人类主动发起追问，不能替代对原始数据源的独立核验。
- 对实时性强、依赖外部权威数据或高风险的结论，仍需人工二次验证。

## 失败模式

| 失败信号 | 典型表现 | 应对动作 |
|---|---|---|
| Q1 无依据 | AI只给结论，无法说明来源 | 要求重新回答并给出依据 |
| Q2 证据模糊 | 只有概括描述，无具体数据/案例 | 要求在提供的上下文内寻找，或承认不确定 |
| Q3 来源混淆 | 把AI补充信息包装成输入事实 | 要求逐条标注“来自上下文”/“AI补充” |
| 跳步执行 | 只问一遍或没有后续动作 | 强制按 Checklist 逐项验收后再进入下一步 |

## 行动 Checklist

- [ ] AI输出结论后，立即提问 Q1：这个结论的依据是什么？
- [ ] 追问 Q2：有没有具体的数据或案例支撑？
- [ ] 追问 Q3：这个依据是否来源于我给的上下文，还是AI自己补充的？
- [ ] 根据回答执行对应动作：重答 / 上下文内找 / 标注来源
- [ ] 在初始 prompt 中加入证据声明要求：给出结论时必须同时列出具体依据，非上下文来源需明确标注
- [ ] 将核查结果记录到数据管理工具（Notion / Airtable 等）

## 相关卡/互链

- [[sk-ai-question-problem-checklist]]
- [[sk-ai-parallel-validation]]

## 来源

- 半肥猫，AI俱乐部-AI学习落地分享，2026-06
- 10_raw/sources/src_20260606_90b44191-没有人呀现在.md

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
