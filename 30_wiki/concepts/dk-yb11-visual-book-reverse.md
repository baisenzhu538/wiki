---
id: "dk-yb11-visual-book-reverse"
title: "不训练模型锁定风格的逆向视觉书法"
type: "dark-knowledge"
dark_knowledge_type: "workflow"
status: "draft"
domain:
  - "design"
source_person: "月白"
source_context: "口述稿: AI设计-AI设计师实操培训01"
source_refs:
  - "00_inbox/design/AI设计-AI设计师实操培训01.txt"
tags:
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/design"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#source_type/dark-knowledge"
created_at: 2026-06-04
updated_at: 2026-06-04
related:
  - "dk-yb13-zero-shot-style-transfer"
  - "dk-yb12-ai-image-analysis-replace-training"
contradicts:
---

# 不训练模型锁定风格的逆向视觉书法

## 原始表述

> 必须要解决的问题是不训练模型也能锁定风格。我的核心解法是先逆向，然后再进行风格描述三要素。什么叫做先逆向？就是你先让大家分析一堆你喜欢的参考图，根据这一堆的参考图自动生成一份视觉书。

## 使用场景

需要为AI生图模型（如Midjourney/Stable Diffusion/FLUX等）稳定复现特定视觉风格，但缺乏训练资源或不想进行模型微调的设计师、AI艺术指导、品牌方。

## 操作方法

1. 收集目标风格的参考图（10-50张）
2. 组织团队/自己逐图分析视觉特征（色彩、构图、质感、光影、笔触等维度）
3. 将分析结果结构化汇总为"视觉书"（视觉规范文档）
4. 从视觉书中提炼"风格描述三要素"（通常指主体描述+风格关键词+技术参数的组合）
5. 将三要素作为prompt模板复用，实现无需训练的风格锁定

## 适用边界

- 不适用需要像素级一致性的角色/IP场景（仍需LoRA/模型训练）
- 参考图风格混杂导致视觉书矛盾
- 团队缺乏基础视觉分析能力时逆向阶段会失真

## 为什么值钱

公开语料中充斥的是"怎么写prompt"或"怎么训练LoRA"，但"不训练模型时如何通过组织化的人类视觉分析来替代模型训练"这一中间路径极少被系统化总结。大多数人要么硬写prompt碰运气，要么直接走训练路线，忽略了"逆向生成视觉规范文档"这个可复用的工程化方法。

## 与其他知识的关联

- [[dk-yb13-zero-shot-style-transfer]] — 零训练风格迁移：三要素描述法
- [[dk-yb12-ai-image-analysis-replace-training]] — AI图像分析替代模型训练
