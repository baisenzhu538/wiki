---
id: "dk-yb32-doubao-size-composition"
title: "豆包AIGC生图：尺寸是唯一关键排版影响因素"
type: "dark-knowledge"
dark_knowledge_type: "tool_usage"
status: draft
domain:
  - "design"
source_person: "月白"
source_context: "口述稿: AI设计-AI设计师实操培训01"
source_refs:
  - "00_inbox/design/AI设计-AI设计师实操培训01.txt"
created_at: 2026-06-04
updated_at: 2026-06-04
related:
  - "dk-yb23-ai-pre-screen-three-minutes"
contradicts: ""
tags:
  - #domain/design
  - #scene/ai-collaboration/prompt-engineering
pipeline:
  - #source_type/dark-knowledge
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
---

# 豆包AIGC生图：尺寸是唯一关键排版影响因素

## 原始表述

> AIGC生图他进行画面排版的时候，其中有一个也是唯一一个我测出来的最重要的影响因素就是尺寸。

## 使用场景

使用豆包等AIGC工具生成图片时，对画面构图/排版不满意的设计师、运营或普通用户。

## 操作方法

在豆包许愿抽卡后，利用调整画面比例裁图功能，通过修改尺寸而非提示词来直接控制画面排版效果。

## 适用边界

- 不适用于需要修改内容元素本身（如替换物体、改变风格）的场景
- 仅针对画面排版/构图问题
- 其他平台（Midjourney/SD等）的尺寸影响机制可能不同

## 为什么值钱

这是作者通过大量测试得出的反常识结论——通常用户会反复优化提示词来控制构图，但实际上尺寸才是"唯一最重要的影响因素"。这一经验未被官方文档强调，也不同于其他平台（如MJ的--ar参数主要影响比例而非排版逻辑），属于平台特有的隐性机制。

## 与其他知识的关联

- [[dk-yb23-ai-pre-screen-three-minutes]] — AI出图前置筛选：三分钟十套方案定风格
