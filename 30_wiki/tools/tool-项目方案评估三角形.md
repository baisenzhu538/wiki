---
id: tool-项目方案评估三角形
title: 项目方案评估三角形：收益×成本×风险三维对比
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.78
trust_level: medium
language: zh-CN
domain:
- yitang
- decision-science
source_refs:
- 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-项目方案评估三角形_vlm_desc.md
related:
- '[[yitang-domain-digest]]'
- '[[decision-science-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
---

# 项目方案评估三角形

## 一句话定义

用**收益、成本、风险**三个维度对比多个项目方案，找出最优解的评估工具 [conf=0.78, source=原图/VLM描述]。

## 三维评估矩阵

对每个方案在三个维度打分（1-5）：

| 方案 | 收益 | 成本 | 风险 | 综合 |
|:---|:---:|:---:|:---:|:---:|
| 方案A | | | | |
| 方案B | | | | |

**综合 = 收益 - 成本 - 风险**（越高越好）

## 操作步骤

1. 列出所有可行方案（包括"什么都不做"）
2. 每个方案在三个维度打分，标注置信度
3. 如果两个方案综合分接近——选风险更低的
4. 如果最优方案「高风险高收益」——问：失败后能否承受？

## 关键洞察

> 多数人只比「收益」和「成本」，忘比「风险」。而风险是唯一可能让一个"看起来最优"的方案直接归零的因素 [conf=0.70, source=一堂原创]。

## 失败模式

| 失败 | 修复 |
|:---|:---|
| 方案数太少 | 至少列3个（含"不做"），2个只是二选一不是评估 |
| 风险低估 | 对每个方案问：最坏情况是什么？概率多大？ |
| 打分全凭直觉 | 每个分后面必须跟一句理由 |

---

*基于 VLM 描述生产。*
