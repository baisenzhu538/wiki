---
id: "skill-月白-多语言提示词精准法"
title: "技能：多语言提示词精准法"
type: skill
status: draft
domain:
  - design
source_person: "月白"
source_context: "文创案例"
source_refs: 
wiki_refs: 
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required: 
prerequisite_skills: 
created_at: 2026-06-07
updated_at: 2026-06-07
pipeline:
  - confidence-draft
author: legacy
reviewed_by: pending
confidence: 0.6
trust_level: low
---

# 技能：多语言提示词精准法

## 原始表述

多语言提示词精准法是月白在文创案例中提出的实操方法。

## 操作步骤

1. 识别提示词中的关键概念和专业名词
2. 在该名词后附加英文术语
3. 如涉及艺术/建筑/音乐等领域，附加意大利语原词
4. 使用AI辅助生成多语言版本（底层指令：要求所有专业名词后生成英语）
5. 结合精准约束条件，双重策略降低幻觉

## 适用场景

- 使用国外模型（Midjourney、Stable Diffusion等）
- 涉及专业领域术语（艺术、医学、建筑等）
- 提示词幻觉严重，输出不稳定

## 不适用场景

- 使用国产模型处理国内常规图片需求（豆包等已足够）
- 非专业日常用语场景
- 团队无多语言能力，学习成本过高

## 工具/环境

- AI翻译辅助工具
- 专业术语词典
- Midjourney/Stable Diffusion/ChatGPT

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

英文语料库的视觉样本精度和专业丰富度远高于中文；意大利语保留大量艺术/设计源术语（如Bodoni/Baseline），能激活更精准的模型理解；多语言'撞词'策略可将近乎消除幻觉

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
