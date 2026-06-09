---
id: "dk-yb1-aigc-mvp-before-ps"
title: "设计师AIGC工作流：先跑MVP再开PS"
type: "dark-knowledge"
dark_knowledge_type: "workflow"
status: "draft"
domain:
  - "design"
source_person: "月白"
source_context: "口述稿: AI设计-AI设计基础01"
source_refs:
  - "00_inbox/design/AI设计-AI设计基础01.txt"
tags:
  - "#boundary/not-for-creative"
  - "#boundary/requires-human-judgment"
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/design"
  - "#scene/ai-collaboration/prompt-engineering"
  - "#scene/hardware-debugging/bom-management"
  - "#source_type/dark-knowledge"
created_at: 2026-06-04
updated_at: 2026-06-04
related:
  - "dk-yb5-style-asset-archive"
  - "dk-yb8-file-naming-eight-elements"
contradicts: ""
---

# 设计师AIGC工作流：先跑MVP再开PS

## 原始表述

> 打开ps就开始做，不能这样打开ps就开始做。你MVP先建起来先跑，他跟审美没有关系，你做这些都不需要审美，你找图不需要审美，你先找找到了，然后捞风格提示词，风格提示词捞完了之后再让AIGC跑，先确认方向再开始动作。

## 使用场景

传统设计背景、习惯直接打开PS/AI开始动手的设计师，在接入AIGC工具（Midjourney/SD等）时，需要转变工作流。

## 操作方法

1. **禁止第一步打开PS**
2. 先找参考图（无需审美判断，大量收集即可）
3. 从参考图中"捞"出风格提示词（prompt）
4. 用AIGC快速跑MVP验证方向
5. 方向确认后，再进入传统设计工具执行

## 适用边界

- 不适用纯传统手工设计项目（无AIGC参与）
- 不适用于审美本身就是核心交付物的阶段（如最终视觉精修）
- 易混淆："不需要审美"指前期探索阶段，非全程放弃审美

## 为什么值钱

公开语料中充斥"设计师要拥抱AI"的泛论，但极少有人明确指出"打开PS就做"这个具体肌肉记忆是最大障碍，以及"找图不需要审美"这种反直觉的操作顺序——传统设计教育强调每一步都要有审美判断，而AIGC时代需要先分离"方向验证"与"审美执行"。

## 与其他知识的关联

- [[dk-yb5-style-asset-archive]] — AI绘图降本的前提：风格资产工程化归档
- [[dk-yb8-file-naming-eight-elements]] — 文件命名八要素体系
- [[dk-yb15-prompt-length-constraint]] — 提示词长度即约束强度
