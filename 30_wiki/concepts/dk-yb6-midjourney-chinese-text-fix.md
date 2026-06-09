---
id: "dk-yb6-midjourney-chinese-text-fix"
title: "Midjourney中文文字修复极简提示词"
type: "dark-knowledge"
dark_knowledge_type: "tool_usage"
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
  - "#source_type/dark-knowledge"
created_at: 2026-06-04
updated_at: 2026-06-04
related:
  - "dk-yb4-nano-banana-style-reproduction"
contradicts: ""
---

# Midjourney中文文字修复极简提示词

## 原始表述

> 用最高分辨率重新生成这张图，修改中文中的文字错误。没了这一句话能解决所有的问题，提示词太多，它容易模糊关键提示词。

## 使用场景

使用Midjourney/云巨米生成含中文文字的图像时，文字出现乱码、错字、渲染不清的设计师或AI绘图用户。

## 操作方法

1. 生成图像后发现中文文字效果差
2. 不添加冗余描述，仅使用固定提示词"用最高分辨率重新生成这张图，修改中文中的文字错误"进行重绘
3. 避免在提示词中堆砌过多其他指令，保持该句的权重不被稀释

## 适用边界

- 仅适用于需要保留/修正图中已有中文文字的场景
- 不适用于纯英文文字修复（英文在MJ中本身表现较好）
- 不适用于完全重新设计文字内容的场景
- 提示词过多时该指令效果会下降

## 为什么值钱

反直觉的极简策略——用户通常倾向于用更多描述词来"强化"需求（如"清晰的汉字""完美的排版""无错别字"），但Midjourney的提示词机制中冗余项会竞争注意力权重；"最高分辨率"触发特定的渲染路径，"修改中文中的文字错误"是社区反复测试后发现的精准触发语，这类经过实战压缩的极简公式不会出现在官方文档或公开教程中。

## 与其他知识的关联

- [[dk-yb4-nano-banana-style-reproduction]] — Nano Banana 在特定艺术风格稳定复现上优于 GPT-4o
