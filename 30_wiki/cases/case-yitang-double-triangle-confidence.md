---



id: case-yitang-double-triangle-confidence
title: 案例：一堂把双三角模型变成 AI 难题的通用解题底盘
type: case
status: enriched
problem_domains:
- src_unknown
- src_unknown
industry: 在线教育/AI 产品
scale: 公司
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
source_refs:
- src_20260614_8269ccdb-一堂-建模能力培训-truman-口述
- src_20260614_42f1e977-一堂-建模能力培训-truman-笔记
wiki_refs:
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tags:
- src_unknown
- src_unknown
related_skills:
- src_unknown
related_concepts:
- src_unknown
- src_unknown
related_cases: []
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
created_at: '2026-06-15'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
domain:
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- lens: 缺乏统一完备框架，各自迷信单一工具或 prompt
  follow_up: 让业务负责人用双三角模型把任务拆成六维检查清单，定位缺失的是哪一角
- lens: 把工具当答案，而不是把框架当底盘
  follow_up: 在动手前先回答：这个任务的六维要素是否已覆盖？里程碑是什么？
- lens: 体系/里程碑成为最大卡点，而非基本功或数据
  follow_up: 用双三角做前置筹备，把“六词空壳”往下推两层变成具体检查项和动作
---# 案例：一堂把双三角模型变成 AI 难题的通用解题底盘

## 原始表述

> 双三角模型给了我们极大的笃定感和信心，和解决问题的无限的机会……我们内部在使用双三角这件事情上，已经足够笃定到没有双三角，有些活已经不敢做了。

## 问题

进入 AI 时代后，团队面对复杂 AI 难题时缺乏统一、完整的分析框架。一年前问“做 partner/AI 项目的最大难点”，团队会回答“基本功不会用”；半年前回答“审美不够、数据不够”；现在排名第一的答案是“体系不行、没有里程碑”。

没有完备框架时，具体症状表现为：

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 方案

把“双三角模型”作为所有复杂 AI 任务的通用筹备与整理框架：

1. **先拆风险与要素**：用双三角的六个角覆盖 AI 难题的关键维度；
2. **再组合资源**：把 AI、数据、审美、体系、里程碑等维度组合使用；
3. **避免迷信单一工具**：任何一角缺失都可能导致交付偏差；
4. **反复训练**：让基层业务负责人每人找一个真实案例练习双三角。

### 落地机制：从“六个词”到“两层推导”

Truman 强调，双三角不能直接用六个词干活，必须往前推两层：

| 层级 | 做什么 | 示例：用双三角做一个“AI 选课系统” |
|:-----|:------|:--------------------------------|
| L1 框架词 | 列出双三角六维 | 创造力、审美、体系 × 场景、数据、基本功 |
| L2 问题定义 | 把六维翻译成任务关键问题 | 学员选课的真实决策链是什么？需要哪些课程标签数据？LLM 能否处理约束排序？ |
| L3 检查清单 | 每个维度变成可执行检查项 | 场景：覆盖新/老学员两类决策路径；数据：课程标签结构化到可检索；基本功：提示词能稳定输出带约束的推荐 |

### 从双三角到一堂五步法

一堂内部已经把五步法第二步调整为“梳理双三角模型”：在给出具体方案之前，先用双三角把问题空间摊开来，确认六维覆盖、定义里程碑，再进入后续推导。这让双三角从“个人修炼工具”变成了“团队解题底盘”。

## 结果

- src_unknown
- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
- src_unknown
- src_unknown

## 可迁移

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 诊断性问题（何时参考本案例）

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Constraints & Boundaries

### 可迁移场景 / 适用边界

| 场景 | 说明 |
|:-----|:------|
| ✅ 复杂 AI 任务交付前筹备 | 任务涉及多维度组合（场景、数据、基本功、审美、体系、创造力），需要统一语言 |
| ✅ 团队交付质量波动大 | 用双三角把隐性经验显性化，减少对个人手感的依赖 |
| ✅ 需要把业务经验封装成 AI skill / partner | 双三角是 feature 封装的基础结构之一 |
| ✅ 已有 1–2 个真实案例可练手 | 抽象框架必须落在具体案例上，否则沦为六个词 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| **把六个词当答案** | 汇报时画个双三角，但每个角只说一句话，无法落地 | 强制往下推两层：每个角至少列出 3 个检查项和 1 个里程碑 |
| **缺一角硬上** | 基本功或数据明显不足，却直接让 AI 生成最终交付物 | 用双三角做前置检查，缺哪角先补哪角，或降低任务难度 |
| **只套壳不推导** | 做一个“出海双三角”“IP 双三角”，但内容只是换关键词 | 每个角必须有该场景特有的定义和判断标准，不能复用通用解释 |
| **把框架当汇报装饰** | 双三角只出现在 PPT 里，实际执行仍按老习惯 | 要求执行文档里先写双三角检查清单，再写具体动作 |

## 行动清单：AI 难题双三角筹备 Checklist

在启动一个复杂 AI 任务前，业务负责人先完成以下检查：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关键标签

- src_unknown
- src_unknown
- src_unknown

## 关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown
- src_unknown
