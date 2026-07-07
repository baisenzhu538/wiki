---
id: case-yitang-model-asset-inventory
title: 案例：一堂用 AI 扫描内容资产，把三四百个模型归集到二三十个范式
type: case
status: reviewed
problem_domains:
- src_unknown
- src_unknown
industry: 在线教育
scale: 公司
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
wiki_refs:
- src_unknown
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
related_cases:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-15'
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-16'
confidence: 0.8
trust_level: medium
domain:
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- lens: 模型资产黑箱
  follow_up: 用 AI 扫描全部交付内容，按形态（清单/SOP/雷达图/漏斗/象限/冰山图/三角图/段位图/画布）做一遍强制分类，看 95% 是否能落入
    20-30 个范式
- lens: 模型可发现性差
  follow_up: 建立武器库索引，每个范式标注适用问题、典型案例、边界条件和使用 checklist
- lens: 重复发明轮子
  follow_up: 在立项评审环节强制要求“先查武器库，说明现有范式为何不适用”才能申请新模型
- lens: 伪创新
  follow_up: 新模型上线前做一次“范式匹配审查”，要求证明它无法被已有 20-30 个范式表达
related:
- "[[case-yitang-model-valuation-flywheel]]"
- "[[tool-从案例中学习]]"
- "[[tool-月白-设计师AI资产四类型沉淀]]"
- "[[ocr-一堂-案例拆解-课程清单]]"
- "[[ocr-一堂-科学决策-深度-案例02]]"
- "[[case-科学决策-深度案例06]]"
- "[[ocr-一堂-科学决策-roi决策评估画布-案例02]]"
- "[[case-科学决策-深度案例02]]"
- "[[tool-纪浩-案例池构建法]]"
- "[[case-科学决策-ROI案例03]]"
- "[[tool-马易-业务问题AI化拆解-餐饮设计案例法]]"
- "[[ocr-一堂-科学决策-深度-案例04]]"
---

# 案例：一堂用 AI 扫描内容资产，把三四百个模型归集到二三十个范式

## 原始表述

> 我们让 AI 去尝试着去进行全面扫描了一下，我们过去做的，这个我们过去至少沉淀了三四百个模型资产，然后高质量资产至少也有 200 个。我们过去见过 57 个案例、107 个小时……16 个雷达、19 个逻辑链、21 条线索、29 个本质、14 套塔台、14 个双三角模型、10 个创新三角、44 个武器库、13 张画布。

## Background

一堂过去五年沉淀了大量模型资产，但团队对“到底有多少、属于哪类、能否复用”没有清晰台账。人工统计三四百个资产成本极高，且容易遗漏；新人和外部合作方也很难快速找到已有范式，导致重复发明轮子。更隐蔽的问题是：许多“新模型”其实只是旧范式换了新名字，组织却在为伪创新支付额外的认知和维护成本。

## What Happened

Truman 团队让 AI 对一堂全部交付内容做 ASR/OCR 扫描与全面盘点，把案例、雷达图、逻辑链、本质、画布等资产按形态分类，归集到约二三十个基础范式（武器库）中。具体做法：

1. **全面扫描**：用 AI 读取一堂内部知识库、课程资料、音视频讲义；
2. **形态分类**：按模型形态（清单/SOP、N 步法、雷达图、漏斗、象限、冰山图、三角图、段位图、画布、武器库等）打标签；
3. **范式归集**：把同类资产归集到 20-30 个基础范式，统计每类资产的数量和占比；
4. **人工校验**：对 AI 的归类结果做抽检和校正，确保分类标准稳定；
5. **沉淀武器库**：把最常用的范式整理成组织级“武器库”，供后续建模直接调用；
6. **接入流程**：把“先查武器库”写入建模/课程立项评审环节。

## 结果

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 可迁移

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 诊断信号

| 信号 | 镜头 | 跟进问题 |
|:-----|:-----|:---------|
| 团队内部已有大量“方法论”“模型”“清单”，但没人说得清总数、分类和复用情况 | 模型资产黑箱 | 用 AI 扫描全部交付内容，按形态做一遍强制分类，看 95% 是否能落入 20-30 个范式 |
| 新人或外部合作方反复问“这类问题我们有没有现成模型” | 模型可发现性差 | 建立武器库索引，每个范式标注适用问题、典型案例、边界条件和使用 checklist |
| 每次做新课/新产品都从零开始画新模型，旧模型很少被复用 | 重复发明轮子 | 在立项评审环节强制要求“先查武器库，说明现有范式为何不适用”才能申请新模型 |
| 团队热衷于创造新名词、新框架，但底层逻辑与旧模型高度相似 | 伪创新 | 新模型上线前做一次“范式匹配审查”，要求证明它无法被已有 20-30 个范式表达 |

## Constraints & Boundaries

### 适用边界 / 可迁移场景

| 场景 | 说明 |
|:-----|:------|
| ✅ 知识型/内容型组织，已沉淀 50+ 个模型/清单/框架 | 样本量足够，AI 扫描和范式归集才有统计意义 |
| ✅ 有数字化知识库或课程资料可供 AI 扫描 | 资产以文本/图片/音视频形式存在，ASR/OCR 可处理 |
| ✅ 组织愿意接受“95% 模型都是旧范式变形”的结论 | 若管理层把“创新数量”当 KPI，盘点会被抵触 |
| ✅ 已有人工归纳的模型形态分类标准 | AI 需要人定的范式框架，否则容易按关键词乱聚类 |
| ✅ 有固定交付/评审节点可接入武器库检查 | 如立项评审、课程终审，能把盘点结果变成流程约束 |

#| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| **AI 扫描完就束之高阁** | 盘点报告很厚，但建模时还是随手画；半年后模型数量又翻倍 | 把盘点结果接入立项评审，强制先查武器库并记录“为何不适用” |
| **分类标准由 AI 自定，人不做判断** | 同一模型被分到多个类别，或关键范式被拆碎 | 人工先定 20-30 个范式框架，AI 只做匹配、计数和查漏补缺 |
| **为追求归集率硬把模型塞进已有范式** | 模型被归类后逻辑变形，使用时发现不适用 | 允许 5% 保留为创新模型，设置“不适用”申诉通道 |
| **只盘点不更新** | 武器库很快与新交付脱节，新人拿到过时索引 | 每次交付后 24h 内把新模型/改动同步回资产库 |
| **把范式库当成 creativity 限制** | 团队抱怨“老板不让创新”，开始抵触 | 明确“先匹配再创新”，并把创新模型定价（参考 [[case-yitang-model-valuation-flywheel]]） |

## 落地模板：AI 辅助模型资产盘点 SOP

在启动组织级模型资产盘点前，按以下 SOP 执行：

### 第一步：划定扫描范围（1-2 天）

- src_unknown
- src_unknown
- src_unknown

### 第二步：AI 全面扫描（3-7 天）

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 第三步：形态分类（3-5 天）

- src_unknown
- src_unknown
- src_unknown

### 第四步：范式归集（5-7 天）

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 第五步：建立武器库索引（3-5 天）

| 字段 | 填写要求 |
|:-----|:---------|
| 范式名称 | 统一命名，避免同范式多名 |
| 模型形态 | 从形态分类表中选择 |
| 适用问题 | 一句话描述解决什么问题 |
| 边界条件 | 至少 2 条不适用场景 |
| 使用 checklist | 3-5 个关键检查项 |
| 典型案例 | 1 个内部使用案例 |
| 相关范式 | 链接到同形态或同问题域范式 |

### 第六步：接入流程与迭代（持续）

- src_unknown
- src_unknown
- src_unknown

## Checklist：模型资产盘点验收单

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

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 可迁移场景

| 场景 | 如何套用 | 关键组件/关联卡片 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |

---

## 教训

- src_unknown
- src_unknown
- src_unknown

---

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |
