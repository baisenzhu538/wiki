---
id: case-truman-temperature-parameter
title: 「案例：温度参数——一个L0 Feature降成本10倍」
type: case
status: draft
confidence: 0.90
trust_level: high
domain:
  - ai-basic
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（上）-口述.txt
source_person: Truman
source_context: Truman口述上 L812-872（作业评查报告温度参数调优）
reviewed_by: 待审
aliases:
  - 温度参数
  - 2万到2千
  - 作业评查
discoverable_by:
  - 温度参数
  - 2万到2千
  - 作业评查
  - L0 Feature
related:
  - framework-truman-feature-layered-system
  - framework-truman-feature-thinking-core
  - case-truman-ai-image-workflow-evolution
  - case-truman-investment-daily-report
  - 10_raw/sources/feature-periodic-table-v0.8.json
tags:
  - method:feature-thinking
  - method:optimization
  - scene:ai-cost
  - audience:practitioner
  - content-format:case
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - cited
  - validated
diagnostic_signals:
  - signal: "AI批量任务的成本居高不下"
    lens: 可能在用默认参数跑——调温度/Top-K可以大幅降成本
    follow_up: 先查当前模型调用的参数配置——温度设了多少？能否降低？
---

> 本卡属于 [[framework-truman-feature-layered-system]] 的L0层案例——模型参数层Feature的杠杆效应。

# 温度参数：一个L0 Feature降成本10倍

> 一句话：作业评查报告生成——用最贵的模型一次2万元。调了一个参数（温度），成本降到一两千，准确率仍保持95%。一个L0层的Feature，撬动了10倍的成本杠杆。

---

## 过程

### 起点：2万元一次

Truman想在春节给学员生成个性化作业评查报告——每人2400字，结合所有学习记录（L812-816）。量大、模型贵。

"国外最贵的模型效果不错——一次2万块钱。做一次实验2万，做一次实验2万"（L832-836）。国内模型不好使，国外模型太贵。

### 卡点：财务不可持续

"本来想免费送大家个礼物，最后花一大笔钱"（L846）。团队面前摆着：时间成本高+财务成本高。差点黄了。

### 转折：调温度参数

"这个参数是可以调的——温度是可以调的"（L858）。

Truman调整温度参数后，"极低成本处理权重因素，与全球论文的重复度降低很多，准确率是95%"（L868）。

### 结果：2万→1-2千

"后来再去跑全量报告的时候，很便宜"（L870）。准确率保持95%，成本从2万降到一两千——降了10倍以上。

---

## Feature杠杆

| 参数 | 改动前 | 改动后 | 杠杆倍数 |
|:---|:---|:---|:---|
| 成本 | 2万/次 | 1-2千/次 | ~10-20倍 |
| 准确率 | 专家级 | 95% | 保持 |
| Feature层 | — | L0 温度参数 | 最底层 |

**为什么一个L0 Feature有这么大杠杆**：温度控制输出的随机性——高温=更多样但也更不稳定。调低温度让输出更确定、更可预测，在批量场景下一个参数的优化=海量成本的节约。（⚠️ 口述未解释具体机制，此处为推测）

---

## 关键数字

| 数据 | 来源 | 状态 |
|:---|:---|:---|
| 最贵模型一次2万元 | 口述上 L832 | ⚠️ Truman自述，未外部审计 |
| 调温度后成本降至1-2千 | 口述上 L870 | ⚠️ 同上 |
| 准确率保持95% | 口述上 L868 | ⚠️ 同上 |

## 教训

1. **L0层的Feature杠杆最大——因为所有上层Feature都依赖它**
2. **成本问题不只是"换便宜模型"——调参数也可以大幅降成本**
3. **批量场景下参数优化的ROI极高——一次调参，永久受益**

## 可迁移场景

| 场景 | 迁移 |
|:---|:---|
| AI批量生成（报告/摘要/翻译） | 先调温度——高温=多样，低温=确定 |
| 高成本AI任务 | 先看参数配置——可能不是模型贵，是参数没调 |

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 只用默认参数不调优 | "模型太贵"——但从来没看过参数配置 | 每次新任务先检查温度/Top-K/MaxTokens |
| 调参后不验证准确率 | 成本降了但质量也降了——得不偿失 | 调参后必须跑一轮质量验证（至少抽检10条） |
| 盲目调温度 | 高温→内容太发散，低温→太死板 | 按任务类型选：创意任务高温、事实任务低温 |
