---
id: tool-数据分层供给
title: 技能：数据分层供给
type: tool
domain:
- learning-methodology- kdo
- product
- design
- yitang
status: draft
source_person: Truman
source_context: src_20260609_03491271
source_refs:
- 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: 欧阳锋
reviewed_at: 2026-07-04
confidence: 0.7
trust_level: low
related:
- '[[tool-多轮确认防偏差]]'
- '[[tool-主动摘要压缩上下文]]'
- '[[tool-反向提示获取优化建议]]'
- '[[tool-渐进式披露上下文]]'
- '[[tool-提示词结构化迭代]]'
- tool-ai-prd-for-ai
tags:
- audience:executor
- scene:execution
- skill-level:beginner
aliases:
- 自用的
---
# 技能：数据分层供给

## 原始表述
> 8.数据分层

## 操作步骤
1. 将数据按重要性/时效性/敏感度分层
2. 设计不同层级的接入策略（核心层直接注入、扩展层RAG检索、公开层联网搜索）
3. 根据任务需求动态组合数据层

## 适用场景
- src_unknown
- src_unknown
- src_unknown

## 为什么有效
优化token使用效率，保证核心信息优先触达，灵活扩展信息边界

## 工具/环境
- src_unknown
- src_unknown
- src_unknown

## 关联技能
- src_unknown

## 来源
- src_unknown

## Feedback Path
- src_unknown

## 目的

在构建 AI 应用时，将提供给模型的数据按重要性、时效性和敏感度分层管理——核心层直接注入系统提示保证必达、扩展层通过 RAG 按需检索节省 token、公开层联网搜索补充实时信息。解决"把所有数据塞进上下文"导致的 token 浪费和关键信息淹没问题。

## 不要用的场景

- 任务所需数据总量很小（几百字级别），分层管理开销得不偿失
- 数据层之间的优先级难以清晰界定，导致分层混乱反而降低信息触达率
- 当核心数据本身质量差或含噪声时，优先注入反而会把错误放大

## 质疑

**Yann LeCun**: 分层策略暗含了一个强假设——你能提前知道哪些数据对当前任务"更重要"。但在开放式推理任务中，重要性是任务相关且动态变化的，静态分层可能导致关键信息恰好被归入低频层而漏掉。这本质上是一个信息检索的 recall 问题，分层降低了 recall。

**Lilian Weng**: RAG 的核心挑战是检索质量，数据分层在此基础上又加了一层分类质量的问题——你需要在两个环节都做得对才能让最终答案受益。如果检索这层已经很难做到 90% 准确率，叠加分类会形成误差级联。

进一步审视该方法的四类关键术语：
- **具体假设**：任务数据的重要性、时效性和敏感度可以在任务执行前被静态划分。
- **边界**：适用于数据量大、检索与分类成本能被 token 节省覆盖的场景；不适用于数据量小或数据重要性动态变化的任务。
- **反例**：在开放式推理或创意写作中，关键信息可能在不同层级间动态转移，静态分层反而降低 recall。
- **前提**：前提是检索层和分类层都具备足够准确率，且团队有能力维护分层策略和权限控制。
