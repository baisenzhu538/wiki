---

id: dk-yb5-style-asset-archive
title: AI绘图降本的前提：风格资产工程化归档
type: dark-knowledge
dark_knowledge_type: workflow
status: enriched
domain:
- design
- ai-collaboration
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- 10_raw/sources/src_20260604_design-ai-basics-01.md
created_at: 2026-06-04
updated_at: '2026-06-19'
related:
  - '[[dk-yb1-aigc-mvp-before-ps]]'
  - '[[dk-yb29-prompt-migrate-copy-first]]'
  - '[[dk-yb31-style-first-controlnet]]'
  - '[[dk-yb27-pseudo-layer-evasion]]'
  - '[[dk-yb23-ai-pre-screen-three-minutes]]'
  - '[[dk-yb1-aigc-mvp-before-ps]]'
  - '[[dk-yb8-file-naming-eight-elements]]'
  - '[[dk-yb7-design-demand-80-10-10]]'
pipeline:
- confidence-source-cited
author: 月白
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
diagnostic_signals:
- signal: 团队引入AI绘图工具后，产出效率提升了但风格一致性下降了——同一个品牌的视觉每次都不一样
  framework_lens: 资产债——AI降本的前提是可结构化的风格资产，没有这个前提，AI反而会放大风格混乱
  follow_up_question: 在引入AI之前，你的历史风格规范文档、PS工程文件、配色/笔触/构图规则是否已整理？如果没有，AI降本是一句空话。
- signal: 每次做新项目都从零开始写prompt，不利用历史项目的完整工程文件
  framework_lens: 资产复用缺失——不逆向工程历史项目就无法建立可复用的结构体系
  follow_up_question: 最近一个和历史项目风格类似的新项目，是否直接复用了历史PS工程和prompt模板？如果没有，你正在浪费最重要的资产。
---
# AI绘图降本的前提：风格资产工程化归档

## 原始表述

> 前提是你的风格规范整理甚至PS工程文件都要整理好，要完整，你才有可能反推出后续可复用的结构体系。

## 使用场景

插画工作室/品牌设计团队负责人，在引入AI降本前需要做的前置资产整理工作。

## 操作方法

1. 将历史项目的风格规范文档化（配色/笔触/构图规则）
2. 保留完整的PS分层工程文件（含命名规范、图层组结构、调整图层）
3. 按项目类型建立可检索的资产库
4. 用已整理的完整案例训练/微调AI或作为参考图结构
5. 基于完整工程反推提示词模板和可复用的生成结构

## 适用边界

| 边界 | 说明 |
|:-----|:-----|
| **不适用于从零开始的个人创作者** | 无历史资产可整理时，先积累项目，再归档。 |
| **不适用于追求风格随机性的探索性创作** | 工程化归档与创意探索是两种不同的工作模式。 |
| **与"直接堆提示词试出图"的粗放模式相混淆** | 不归档就直接进入AI生成，虽快但不可持续。 |
| **需要PS工程文件的完整性** | 分层文件缺失、命名混乱、图层合并过的项目无法有效归档。 |

## 常见失败模式

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| AI先行，资产后补 | 先用AI出了半年图，回头看历史项目工程文件散落各处无法归档 | 每完成一个项目立刻归档，不要等"以后统一整理" |
| 只归档最终稿 | 只保留了输出JPG/PNG，丢失了分层PSD和调整图层 | 归档标准：必须包含源文件+prompt+参考图+设计决策记录 |
| 归档不检索 | 资产库建了但没人能找到需要的参考 | 建立统一的命名规范和关键词索引（参考dk-yb8） |
| 以为有了AI就不需要归档 | "反正AI能重新生成"——但风格一致性需要参照物 | AI生成是输出，归档是输入——没有规范输入就无法稳定输出 |

## 行动 Checklist

- [ ] 历史项目是否已按风格规范、工程文件、prompt模板三类归档？
- [ ] PS工程文件是否包含完整的分层结构和命名规范？
- [ ] 是否建立了可检索的资产索引？
- [ ] 新项目完成后，是否已将资产纳入归档体系？

## 为什么值钱

公开讨论只强调"AI让画图变便宜"，几乎不提及"便宜的前提是企业已有可结构化的风格资产"。PS工程文件的完整性要求、"反推结构体系"这一逆向工程思路，属于一线管理者的隐性经验，未被AI教程覆盖。

## 与其他知识的关联

- [[dk-yb1-aigc-mvp-before-ps]] — 设计师AIGC工作流：先跑MVP再开PS
- [[dk-yb8-file-naming-eight-elements]] — 文件命名八要素体系
