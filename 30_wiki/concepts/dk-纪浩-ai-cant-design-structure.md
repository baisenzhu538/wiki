---
id: "dk-纪浩-ai-cant-design-structure"
title: "暗知识：AI 不会自己搞结构设计，必须帮它搭"
type: "dark-knowledge"
dark_knowledge_type: "insight"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享——Agent Workspace 五大模块的来源"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/ai-collaboration"
  - "#scene/learning-methodology"
  - "#source_type/dark-knowledge"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "concept-纪浩-ai-collaboration-methodology"
  - "skill-纪浩-agent-workspace"
---

# 暗知识：AI 不会自己搞结构设计

## 原始表述

> "AI 的本质就是一个模式匹配系统，它不会做结构设计。它所有的结构设计都是从自己的预训练当中去找相似的结构。你让它自己去创造一个好的结构，它是搞不定的。所以人需要去帮它规划。"

## 使用场景

- 你让 AI 自己管理自己的任务，结果越来越乱
- 你让 AI "自己优化工作流"，它改出来的东西实际上不能 work
- AI 接手多个任务后开始出现混乱行为——干 A 干了 B、重复犯错

## 操作方法

1. 不要期望 AI 能自己设计信息架构。所有目录结构、知识组织、任务分流——人先画好框架
2. 每一次 AI 执行任务前，确认它访问的知识来源是明确的（不是"它自己找的"）
3. 当 AI 出现混乱时，不要让它自己修——检查人设计的结构哪里出了问题

## 适用边界

- 适用于需要 AI 持续参与、且工作内容有结构的项目
- 不适用于一次性问答——不需要结构
- AI 的结构能力会随模型进步而提升，但"创造新结构"（不是模仿已有结构）目前仍是短板

## 为什么值钱

大多数人让 AI 做事时的心态是"AI 很聪明，让 AI 自己搞定"。然后发现 AI 搞不定、越搞越乱、最后放弃。

纪浩的暗知识是：**AI 的"结构设计"能力不是智能不足——是它的训练机制决定的。** 大模型是从大量已有结构中学会了模式匹配，但它不是从"理解问题域"来推导结构的。当你给它一个全新的问题域（你自己的项目），它没有训练数据可以参考——它只能从别的域借结构过来。这个借来的结构很可能不 fit。

所以"帮 AI 搭结构"不是临时需求——是 AI 能力边界的系统性特征。这条路不会因为模型升级而消失。
