---
id: "dk-yb3-diffusion-stepwise-vs-human-holistic"
title: "AI生图'抽卡'本质：逐步拆解 vs 人类整体构思"
type: "dark-knowledge"
dark_knowledge_type: "insight"
status: "draft"
domain:
  - "design"
source_person: "月白"
source_context: "口述稿: AI设计-AI设计基础01"
source_refs:
  - "00_inbox/design/AI设计-AI设计基础01.txt"
tags:
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/design"
  - "#scene/ai-collaboration/prompt-engineering"
  - "#scene/learning-methodology"
  - "#source_type/dark-knowledge"
created_at: 2026-06-04
updated_at: 2026-06-04
related:
  - "dk-yb2-llm-muddy-clear-muddy"
contradicts: ""
---

# AI生图"抽卡"本质：逐步拆解 vs 人类整体构思

## 原始表述

> 它是直接粗暴的呈现出来...它不是像人类一样，我是构思这件事情，我是构思一个设计画面，我左边要放什么，右边要放什么。

## 使用场景

使用Midjourney/Stable Diffusion等文生图工具的设计师、产品经理，遇到提示词效果不稳定时需要理解底层机制。

## 操作方法

1. 放弃"精确控制画面布局"的预期
2. 将生图视为概率采样过程，同一提示词多次生成筛选
3. 如需控制构图，改用ControlNet/区域提示等强制干预手段，而非依赖语义描述

## 适用边界

- 不适用于传统设计软件（Figma/PS）或可控性强的AI工具（如PPT AI的模板模式）
- 与"提示词工程越精细越好"的误区易混淆——该洞察强调的是扩散模型架构性局限，而非提示词技巧不足

## 为什么值钱

公开资料多讲"抽卡"现象和提示词技巧，但极少有人从认知机制层面解释：扩散模型的逐步去噪过程与人类"先整体后局部"的构思方式存在根本性差异。这是模型架构决定的，不是用户操作问题。

## 与其他知识的关联

- [[dk-yb2-llm-muddy-clear-muddy]] — 大模型训练本质：浑水→清水→浑水
- [[dk-yb14-prompt-migrate-copy-first]] — AIGC提示词迁移：先照搬再微调
