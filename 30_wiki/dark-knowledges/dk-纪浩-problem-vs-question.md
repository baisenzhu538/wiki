---
id: "dk-纪浩-problem-vs-question"
title: "暗知识：Problem vs Question —— AI时代大部分人在用AI回答Question而非解决Problem"
type: "dark-knowledge"
dark_knowledge_type: "principle"
status: draft
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部·AI协作方法论分享（2026年）"
source_refs:
  - "00_inbox/纪浩-AI协作方法论-口述.md"
created_at: "2026-06-09"
updated_at: "2026-06-09"
related:
  - "case-纪浩-skill-market-problem-validation"
  - "skill-纪浩-problem-validation-four-checks"
wiki_refs:
  - "case-纪浩-skill-market-problem-validation"
  - "skill-纪浩-problem-validation-four-checks"
tags:
  - #domain/ai-collaboration
  - #problem-identification
  - #agent-capability
pipeline:
  - confidence-published
  - confidence-source-cited
author: legacy
reviewed_by: pending
---

# 暗知识：Problem vs Question

## 原始表述

> 纪浩：大部分人在用AI回答Question而非解决Problem。在只能回答Question的时代（ChatGPT、DeepSeek），AI满足好奇心。当AI拥有执行能力（Agent时代），真正的价值在于解决Problem：真实痛点、实际益处、可执行。

> 如果需求是伪需求（没有真实锚点、无人受益、因果链不通），AI执行得越好，浪费越大。

## 使用场景

- 你想做一个AI工具/AI Agent，但不确定这个需求是"真问题"还是"听起来不错"
- 有人跟你说"如果有一个XX功能就好了"——你需要判断这是Question（好奇心）还是Problem（真实痛点）
- 你发现团队在用AI做了很多事但产出感不强——可能都在回答Question而非解决Problem
- 你在评估一个AI项目的ROI——Question类项目的价值上限是"知道了"，Problem类项目的价值上限是"改变了"

## 操作方法

**判断需求是Question还是Problem：**

| Question | Problem |
|---------|---------|
| "AI能写保险配置Skill吗？" | "每次配置保险花两小时，如何缩短到五分钟？" |
| "AI能说说怎么用Cursor吗？" | "后端项目每次上线都要手动配置，如何自动化？" |
| "如果有XX就好了" | "我每次都要花X时间做Y" |

**将Question转化为Problem的三步法：**

1. **找到真实场景**：从"如果有XX就好了"转到"我每次都要花X时间做Y"。关键词：**每次**、**花时间**、**具体场景**
2. **定义Before/After**：明确现状（Before：每次花两小时手动配置保险）与理想状态（After：五分钟内完成）
3. **检查因果链**：确认有可执行的解决方案路径，故事能否从头讲到底。如果中间有一步"靠AI自己发挥"——因果链断裂

**用四问法验证（详见 [[skill-纪浩-problem-validation-four-checks]]）：**
1. Before & After：解决前后是什么状态？
2. 真实锚点：具体场景在哪？（不是"如果……"）
3. 受益人：谁会觉得开心？
4. 因果链与能力支撑：问题是否可解？

## 适用边界

- **适用于**：需要投入时间/资源去做的AI项目、工具、Agent——投资前先确认这是Problem不是Question
- **不适用于**：纯探索性学习——用AI了解一个领域、满足好奇心也是合法使用，不需要每次都用Problem框架。但要知道自己在"探索模式"而非"交付模式"
- **不适用于**：时间窗口极窄必须立刻下场的场景——但在下场前至少花5分钟做四问法的第一问（Before & After）
- **关键区分**：好的Problem可以很小。"每次省五分钟"就是好Problem——因为它有真实锚点、有具体受益场景、因果链清晰

## 为什么值钱

- 这个区分决定了AI协作的价值上限：**回答Question → 产生知识**，**解决Problem → 产生改变**
- 当AI能执行时，人的角色必须升级为"问题定义者"——Agent会忠实执行你让它做的事，问题定义错了，执行越高效越浪费
- 纪浩的经验说明：AI时代最稀缺的能力不是"会写prompt"，而是**能区分Question和Problem**——这个能力和AI工具无关，和判断力有关
- 大多数AI课程教的是"怎么用好AI"（术），没教"用AI解决什么问题"（道）。这条暗知识填补了这个空缺

## 与其他知识的关联

- [[case-纪浩-skill-market-problem-validation]] — 展示了如何用四问法将模糊需求转化为可验证的真实Problem。关键转折点是找到了"微信传zip的痛点"这个真实场景
- [[skill-纪浩-problem-validation-four-checks]] — 可复制的检查清单，用于快速判断需求是Question还是Problem
- [[case-纪浩-ui-design-constraint-evolution]] — 纪浩从Question（"AI能帮我做UI吗？"）转到Problem（"每次做UI花极高成本，怎么把设计规范沉淀为可复用资产？"），最终产出可复用方案

## Synthesis

- **纪浩体系**：[[concept-纪浩-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲
