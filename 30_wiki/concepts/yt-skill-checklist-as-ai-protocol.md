---
id: yt-skill-checklist-as-ai-protocol
title: 清单体作为AI的I/O协议——用笔记替代prompt工程
type: concept
status: reviewed
domain: src-unknown
language: zh-CN
version: 1
confidence: 0.9
aliases:
  - 体作为
  - 协议用笔记替代
  - 清单体作为AI的I/O协议
  - 清单体作为AI的I/O协议用笔记替代prompt工程
  - 用笔记替代prompt工程
  - 记替代
source_refs:
- 10_raw/sources/src_20260606_575627a4-一堂-AI时代清单体笔记-Truman-口述-01.md
- 10_raw/sources/src_20260606_db4fc211-一堂-AI时代请单体笔记-Truman-口述-02.md
discoverable_by:
  - 清单体作为AI的I/O协议——用笔记替代prompt工程
  - 清单体作为AI的I/O协议
  - 用笔记替代prompt工程
related:
- '[[yt-prompt-engineering-andrew-ng]]'
- '[[case-纪浩-focus-prompt-design]]'
- '[[meta-prompt-eng]]'
- '[[tool-prompt-iceberg-demand-analysis]]'
- '[[视觉prompt三层操作系统-srom-visual-os]]'
- '[[yt-model-prompt-engineering]]'
- '[[framework-wanghuan-bitcoe-prompt-framework]]'
- '[[proposal-prompt-injection-infrastructure]]'
- '[[tool-prompt-jtbd-scenario-coach]]'
- '[[yt-prompt-brainstorming]]'
- '[[framework-TCPR底层网络协议]]'
- '[[tool-马易-成为首位F工程师]]'
- '[[yt-skill-p-role-prompt-design]]'
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-06-10
updated_at: '2026-06-28'
estimated_tokens: 2500
pipeline:
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: 清单体降低AI理解成本
  follow_up_question: 你的笔记如果直接发给AI，它能否快速识别结构和优先级？
- framework_lens: 结构化输出实现无缝循环
  follow_up_question: AI的输出是否需要你重新整理才能使用？
- framework_lens: 协议有适用范围
  follow_up_question: 这个任务是信息整理还是创意策略？
author: unknown
reviewed_by: 欧阳锋
trust_level: medium
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
- 时代清单体笔记
- 时代请单体笔记
---
# 清单体作为AI的I/O协议——用笔记替代prompt工程

## 用一句话讲清楚
将清单体笔记同时作为AI的输入（prompt + context）和输出格式，使人在L1-L2任务中无需额外翻译层即可与AI多轮迭代。

## 核心要点
1. **笔记即prompt**：你写的清单体就是给AI的指令，不需要额外的prompt翻译层。
2. **笔记即context**：笔记中的每个分点、每个层级，都是context的结构化呈现。
3. **输出即笔记**：AI的输出不是大段文字，而是结构化的清单体，可以直接接入下一次输入。
4. **没有中间层**：清单体是人类认知和AI数据结构之间的适配层，双方都能直接使用，无需二次翻译。
5. **倒逼输入质量**：协议有效的前提是人的笔记足够清晰独立；输入垃圾，输出必然垃圾。

**为什么清单体适合作为I/O协议？** 因为AI的核心能力是在大量文本中提取模式和结构。大段文字对AI是“需要解构的数据”，清单体是“已经结构化的数据”，能显著降低理解成本并减少误差。

## 边界

| 边界 | 说明 |
|------|------|
| **适合** | L1-L2任务：信息整理、清单化、数据提取、格式转换 |
| **适合** | 需要与AI多轮交互、反复迭代的场景 |
| **不适合** | L3+任务：创意思考、策略推演、情感共鸣 |
| **不适合** | 一次性、非结构化的简单聊天 |

## 失败模式

| 失败模式 | 原因 | 修复 |
|---|---|---|
| 把复杂创意任务硬套清单体协议 | 协议滥用、层级错配 | 判断任务层级，L3+任务允许自然语言输出 |
| 笔记本身质量差导致AI输出差 | 输入 garbage in | 先提升清单体笔记的分层、分点、独立性 |
| 完全依赖AI输出不做人工判断 | 责任让渡（abdication） | 人对清单体的场景使用和最终决策负责 |
| 把清单体协议当成唯一交互方式 | 过度结构化 | 保留自然语言作为探索和高复杂度任务的备用方式 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
