---
id: skill-纪浩-progressive-disclosure
title: "技能：渐进式披露——按场景聚合、四层递进的信息组织法"
type: skill
status: draft
domain: [ai-collaboration, yitang]
source_person: 纪浩
source_context: "AI俱乐部-AI协作方法论 分享"
source_refs: [00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt]
tags: ["#domain/ai-collaboration"]
created_at: 2026-06-07
updated_at: 2026-06-07
related: [concept-纪浩-ai-collaboration-methodology, skill-纪浩-agent-workspace]
---

# 技能：渐进式披露

> 信息按场景聚合，不按分类聚合。导诊台→工作手册→经验库→领域知识，知识越来越深。不是一次性把全部上下文扔给 AI——是按需一层层深入。

## Purpose

解决两个问题：① 一次性注入全部知识导致 AI token 浪费和信息迷失 ② AI 在不同任务间切换时不知道用哪套知识。

## Protocol

### 第一步：按场景聚合信息

**错误做法**（按分类）：
```
设计规范/ 组件文档/ 品牌规范/ → 三个目录，AI 分别找
```

**正确做法**（按场景）：
```
UI设计/ 下面放这个场景需要的全部信息
```

### 第二步：四层递进

| 层 | 名称 | 什么时候用 | 内容 |
|:--:|:---|:---|:---|
| L1 | 导诊台 | Agent 进入时默认加载 | 任务分类路由——"你是做什么的" |
| L2 | 工作手册 | 匹配到具体任务时加载 | 这一步怎么做——标准流程、检查点、交付物 |
| L3 | 经验库 | 遇到失败模式时加载 | 踩过的坑、已知的失败模式 |
| L4 | 领域知识 | 概念不清楚时加载 | 底层原理、术语定义、规则 |

### 第三步：一次对话只围绕一个任务

不混合多个任务在一个对话里。AI 的上下文窗口是有限的——混合任务 = 污染上下文。

## When to Use

- Agent 需要处理多种不同类型的任务
- 你想减少 AI 的 token 浪费和幻觉
- 多个任务间的知识和流程差异较大

## When NOT to Use

- 只有一个类型的任务——不需要分流
- 任务极其简单，不需要多步流程

## Critique

### 内部局限

- **四层的分类边界在实践中是模糊的**。某个知识可能既有"工作手册"成分又有"经验库"成分——放哪层？
- **导诊台的路由逻辑需要人设计和维护**。如果任务类型增加了，导诊台需要更新——否则新任务会被分到错误的路线

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|----|---|
| 上层框架 | [[concept-纪浩-ai-collaboration-methodology]] | L2 子技能——Workspace 的信息组织方式 |
| 配套技能 | [[skill-纪浩-agent-workspace]] | 渐进式披露是 Workspace 内信息的层级结构 |
