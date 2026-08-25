---
id: tool-oral-spray-into-doc-not-chatbox
title: 喷文档里不喷聊天框：口喷出素材、AI 出结构（含配套提示词原文）
type: tool
status: reviewed
confidence: 0.9
trust_level: high
domain:
- ai-collaboration
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-08-25'
updated_at: '2026-08-25'
source_refs:
- 00_inbox/AI口喷能力训练全阶指南-口述.txt:A1622-A1672
aliases:
- 喷文档不喷聊天框
- 口喷到文档
- 黄金建议喷文档
discoverable_by:
- 口喷没逻辑怎么办
- 喷文档
- 口喷聊天框
related:
- '[[dk-oral-spray-newcomer-blockers]]'
- '[[tool-ai-oral-spray-input]]'
- '[[tool-oral-spray-demo-prompts-3samples]]'
- '[[framework-oral-spray-cultivation-map]]'
- '[[concept-oral-spray-multi-agent-parallel]]'
tags:
- audience:general
- scene:execution
- skill-level:beginner
- 口喷
- 文档
- 顶层文档
- 防丢稿
- 工具
---

# 喷文档里不喷聊天框

> 本卡属于口喷卡组（Live260 体系）L1→L2 段的操作卡——新人四难中「没逻辑」与「不稳定（丢稿）」两大卡点的**同一个操作解**。

## 一句话

口喷不要喷在 AI 聊天框里——喷进一篇文档（飞书/Notion/Obsidian），然后让 AI 读文档整理：**你出素材，AI 出结构**，原稿留附录一个字不删。

## 为什么（口述 A1622-1672）

聊天框口喷有两个天然缺陷：①长文本在输入框里难写难改，喷长了自己看着乱；②AI 输入法/聊天框可能压缩或丢失长输入（丢稿事故实证=智谱输入法大几千字压成两三百字，原文找不回）。文档环境天然解决两个：随便喷多长、原文永远在。

> 配套提示词原文（A1642-1644，对 AI 说一句即可）：
> 「这个顶喷，那你帮我看一下，然后下面帮我把这个文案留到最后当附录不要删。然后帮我整理成顶层方案，不要做太多的扩展，保留我的内容不要丢，帮我整理成一个 agent 阅读友好的版本。」

## 操作步骤

1. 打开一篇长文档（飞书/Notion/md），把语音输入法光标放进文档里喷
2. 想到哪喷到哪，不管逻辑——「没写干净就再喷一截」，直到想说的话说完了
3. 给 AI 发配套指令：整理成顶层方案/顶层文档 + **原文留附录不要删** + 不要太多扩展 + agent 阅读友好
4. 拿到的顶层文档即为项目 00 文档（多 Agent 协作的共享上下文，见 concept-oral-spray-multi-agent-parallel）

## 判断标准

- 整理后的文档你**认得出来全是自己的内容**（没被 AI 扩写稀释）=合格
- 原文附录还在=合格；AI 把原文删了=指令没喷全，补「不要删」重跑

## 失败模式

- **AI 默认清空原文**：没喷「保留在最后附录」→原始素材灭失。修复：配套指令里「不要删/保留我的内容不要丢」两句都带
- **AI 过度扩写**：顶层文档掺了 AI 的发挥→后续 Agent 读到假上下文。修复：指令带「不要做太多的扩展」
- **在聊天框里长喷**：几千字喷进输入框→又乱又可能丢。修复：长喷一律走文档

## When NOT to Use

- 一两句的短指令（直接在聊天框喷完事）
- 即兴闲聊/探索性对话（不需要沉淀顶层文档的场景）

## 实证

「三小时挑战手搓百万访谈操盘手」项目：全程约 10 分钟喷完+整理出顶层文档；手写同样几千字文档需一个晚上（A1636-1656）。

## 与其他知识的关联

- `dk-oral-spray-newcomer-blockers`：本卡是四难中「没逻辑」「不稳定」两难的操作解
- `concept-oral-spray-multi-agent-parallel`：产出的顶层文档=多 Agent 并行的 00 文档
- `tool-oral-spray-demo-prompts-3samples`：样本三的「顶层文档+原文附录」即本法实战形态
