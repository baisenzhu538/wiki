---

id: dk-yb6-midjourney-chinese-text-fix
title: Midjourney中文文字修复极简提示词
type: dk
dark_knowledge_type: tool_usage
status: enriched
domain:
- design
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- 10_raw/sources/src_20260604_design-ai-basics-01.md
created_at: 2026-06-04
updated_at: '2026-06-19'
related:
  - '[[dk-yb1-aigc-mvp-before-ps]]'
  - '[[dk-yb12-ai-image-analysis-replace-training]]'
  - '[[dk-yb4-nano-banana-style-reproduction]]'
  - '[[dk-yb9-cubox-deployment-failure]]'
  - '[[dk-yb5-style-asset-archive]]'
  - '[[dk-yb4-nano-banana-style-reproduction]]'
  - '[[dk-yb3-diffusion-stepwise-vs-human-holistic]]'
pipeline:
- confidence-source-cited
author: 月白
reviewed_by: 欧阳锋
confidence: 0.80
trust_level: medium
diagnostic_signals:
- signal: 用MJ/SD生成了含中文的图，文字部分全是乱码/错字，用户堆砌大量"清晰汉字""完美排版"等描述词试图修复但无效
  framework_lens: 提示词权重稀释——冗余描述竞争注意力权重，关键指令被淹没
  follow_up_question: 在加任何描述词之前，先只用"用最高分辨率重新生成，修改中文文字错误"跑一次。效果好于堆砌版本吗？
- signal: 团队把AI中文文字修复问题当作"模型能力不足"，反复换模型而非换策略
  framework_lens: 工具策略错位——问题不在模型而在提示词的精准度和冗余度
  follow_up_question: 同样的修复目标，在不同模型（MJ/SD/DALL-E）上试过同一句极简提示词吗？
---# Midjourney中文文字修复极简提示词

## 原始表述

> 用最高分辨率重新生成这张图，修改中文中的文字错误。没了这一句话能解决所有的问题，提示词太多，它容易模糊关键提示词。

## 使用场景

使用Midjourney/云巨米生成含中文文字的图像时，文字出现乱码、错字、渲染不清的设计师或AI绘图用户。

## 操作方法

1. 生成图像后发现中文文字效果差
2. 不添加冗余描述，仅使用固定提示词"用最高分辨率重新生成这张图，修改中文中的文字错误"进行重绘
3. 避免在提示词中堆砌过多其他指令，保持该句的权重不被稀释

## 适用边界

| 边界 | 说明 |
|:-----|:-----|
| **仅适用于保留/修正图中已有中文文字** | 不适用于完全重新设计文字内容。 |
| **不适用于纯英文文字修复** | 英文在MJ中本身表现较好，不需要此策略。 |
| **提示词过多时该指令效果会下降** | 冗余描述会稀释关键指令的权重。 |
| **最佳配合：高分辨率模式** | "最高分辨率"触发特定渲染路径，两者配合效果最优。 |

## 常见失败模式

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| 堆砌描述词 | "清晰的汉字 完美的排版 无错别字 可读性强..."加了5个同义描述，效果反而不如极简版 | 只用一句"用最高分辨率重新生成，修改中文文字错误" |
| 反复换模型而不是换策略 | MJ不行换SD，SD不行换DALL-E，都不行 | 先在同一个模型上测试极简提示词 vs 冗余提示词的效果差异 |
| 把文字修复和画面重做混在一起 | 一边修文字一边改画面风格，两个目标互相干扰 | 文字修复和画面调整分开两步：先修复文字，再调整画面 |

## 行动 Checklist

- [ ] 遇到中文乱码时，是否先用了极简提示词而非立即堆砌描述词？
- [ ] 是否在同一个模型上对比过"极简版"和"堆砌版"的效果差异？
- [ ] 如果需要大量中文内容，是否考虑过后添加文字（如用PS叠加），而非依赖AI直接生成？

## 为什么值钱

反直觉的极简策略——用户通常倾向于用更多描述词来"强化"需求（如"清晰的汉字""完美的排版""无错别字"），但Midjourney的提示词机制中冗余项会竞争注意力权重；"最高分辨率"触发特定的渲染路径，"修改中文中的文字错误"是社区反复测试后发现的精准触发语，这类经过实战压缩的极简公式不会出现在官方文档或公开教程中。

## 与其他知识的关联

- [[dk-yb4-nano-banana-style-reproduction]] — Nano Banana 在特定艺术风格稳定复现上优于 GPT-4o
