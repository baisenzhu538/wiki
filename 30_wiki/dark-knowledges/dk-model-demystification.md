---
id: dk-model-demystification
title: 模型祛魅：上下文完备度 >> 模型差距
type: dk
status: pending_review
author: 老顽童
reviewed_by: 待审
confidence: 0.88
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- ai-collaboration
- knowledge-management
aliases:
- 模型祛魅
- 上下文完备度大于模型差距
- 模型差距感觉不到
- Prompt优先级高于模型
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- AI知识库
tags:
- audience:executor
- scene:planning
- skill-level:intermediate
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——上下文体感（L1746-1770）；#277/309 独立佐证
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[concept-session-vs-memory-vs-document]]'
- '[[framework-dual-center-feishu-obsidian]]'
- '[[dk-one-sentence-handover]]'
- '[[framework-multi-agent-collab-chain-six]]'
- '[[tool-skill-packaging-eight-steps]]'
- '[[framework-baozhashidiaochan-five-step]]'
- '[[dk-ai-judgment-human-responsibility]]'
- '[[case-cross-xingangwan-pharma]]'
---
# 模型祛魅：上下文完备度 >> 模型差距

> **定位**：属于 [[concept-session-vs-memory-vs-document]] 的推论——上下文完备度决定协作质量

## 原始表述

> 「当我用了这套体系，这套上下文的体系之后，我发现不同模型的差别非常小，甚至我已经感觉不到……不管我怎么换模型，我怎么换 Chatcode xPlus 的，或者我换 FB 的 LLaMA 2，换 GPT-4，换最贵的模型 Claude 3，我怎么换在我这都差不多。」（口述 L1752-1760）
> 「从双三角的角度来说，模型作为一个 Feature 跟你的 Prompt 比，它的优先级远远低于 Prompt。」（L1764）
> 「我给他这三扇门是最重要的，这个才是为什么我们鼓励大家，你们如果问协作，你们要有意识的给他配最重要的 Prompt。」（L1770）

## 使用场景

- 纠结"换哪个模型"而忽视上下文设计时——提醒自己模型差距被上下文抹平
- AI 输出不稳定时——先查上下文完备度（Prompt），再考虑换模型
- 团队选型/采购讨论——避免唯模型论（Feature 心态）

## 操作方法

1. **先配上下文**：目标/边界/参考/素材——把"最重要的 Prompt"配齐（三扇门：我是谁/项目文档/设计宪法）
2. **再选模型**：模型作为 Feature，在上下文完备后选性价比合适的
3. **对比实验**：同一任务换不同模型——上下文够强时差距几乎感觉不到（L1752-1760 实证）
4. **补上下文优先**：输出差→先补上下文（文档/示例/约束），不是先换模型

## 适用边界

- 适用于**上下文可配齐**的场景（知识库/文档体系已建立）；零上下文时模型差距确实存在
- 极限推理任务（数学证明/复杂代码）模型差距仍显著——"上下文抹平"主要针对专业分析/商业推理/内容（L1756-1758）
- 多模态/特殊能力（作图/语音）——模型本身能力仍是瓶颈（L1768"除非是这个多模态的模型"）
- GPT 之前的老模型除外（L1756"之前的模型可能还不行"）

## 为什么值钱

- **资源再分配**：把"换模型"的预算转向"配上下文"——ROI 更高
- **祛魅决策**：不迷信最贵模型（楚门"甚至忘了它是什么东西"L1760）——Feature 心态
- **协作基础**：上下文完备度=协作质量的地基（四棒接力/多 Agent 全依赖它）

## Critique

- **反驳**：换模型真的没区别吗？可能是楚门判断力不足（L1760"有可能是我判断力不够"）——诚实标注：体感来自特定场景（上下文完备的专业分析），极限任务仍看模型。
- **反驳**：配上下文也要成本（token/文档维护）——对，但一次性配齐长期复用（资产化），比持续为模型溢价付费划算。
- **条件**：此 dk 前提=上下文体系已建立（文档知识库）；没有知识库时"上下文完备度"无从谈起。
- **注意**：祛魅≠不用好模型——"最重要的是工作我选了最贵的模型"（Skill 封装 L1026）——重要任务仍用好模型，但别以为模型是唯一变量。

## 与其他知识的关联

- `concept-session-vs-memory-vs-document`：上下文=文档知识库（完备度的载体）
- `framework-dual-center-feishu-obsidian`：Obsidian=配上下文的中心
- `dk-one-sentence-handover`：一句话交接=上下文在库里不在交接里
- `framework-multi-agent-collab-chain-six`：多 Agent 共享上下文（完备度=协作质量）
- `tool-skill-packaging-eight-steps`：最贵模型用于重要任务（祛魅的边界）
- `framework-baozhashidiaochan-five-step`：上下文=搜索⇄建模的输入
- `dk-ai-judgment-human-responsibility`：判断力仍在人（模型祛魅的终点）
- `case-cross-xingangwan-pharma`：决策域实证（跨域）

> 互链说明：任务单 C5↔framework-kdo-context-design——该卡尚未建（KDO 上下文设计卡），本卡以纯文本标注互链目标，建议另立项建卡后补链。
