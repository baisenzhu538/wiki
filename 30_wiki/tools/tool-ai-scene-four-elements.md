---
id: tool-ai-scene-four-elements
title: 技能：AI落地场景四要素评估法
type: tool
status: draft
domain:
- ai-collaboration
- yitang- AI
- 落地
- 评估
source_person: 马易
source_context: AI俱乐部-AI落地场景识别-口述，2026-06-06
source_refs:
- src_20260606_ef4877d0-所以90的核心问题
wiki_refs:
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
prerequisite_skills:
- src_unknown
related: null
created_at: 2026-06-11
updated_at: '2026-06-16'
tags: []
pipeline:
- src_unknown
reviewed_by: laowantong
author: unknown
confidence: 0.7
trust_level: low
# 技能：AI落地场景四要素评估法

> **来源**：马易（AI俱乐部-AI落地场景识别-口述）
> **核心**：评估一个场景是否适合AI落地，看四个要素：有容错、有方法、有数据、有判断。缺一不可。

---

## 原始表述
> "一个场景适合AI落地的前提是：有容错、有方法、有数据、有判断。"
> —— 马易

> **暗知识**："这四要素是一个循环，而非简单检查清单。如果'有方法'但'没有数据'，需要先用人工积累数据——这意味着AI落地往往需要'先做一段时间的人工工作'。"

---

## 操作步骤

### 四要素检查清单（强制逐条回答）

| # | 要素 | 检查问题 | 回答格式 | 最低标准 |
|:--:|:----|:---------|:---------|:--------:|
| 1 | **有容错** | 这个场景允许一定错误吗？ | "容错率：_____%，错误后果：_____" | 容错率 > 5% |
| 2 | **有方法** | 你知道怎么做这件事吗？ | "方法：_____，步骤：_____" | 能写出至少3步 |
| 3 | **有数据** | 有历史数据可供训练/参考吗？ | "数据类型：_____，数据量：_____" | 有 ≥ 100 条样本 |
| 4 | **有判断** | 你能判断结果好坏吗？ | "判断标准：_____，判断频率：_____" | 人类能复核 |

### 关键规则

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 评分标准

| 得分 | 判断 | 行动 |
|:----:|:-----|:-----|
| 4/4 | 适合AI落地 | 进入落地流程 |
| 3/4 | 谨慎推进 | 补足缺失要素后再推进 |
| ≤2/4 | 不适合AI落地 | 先人工积累，待条件成熟 |

---

## 适用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

- src_unknown
- src_unknown
- src_unknown

---

## 为什么有效

AI落地的失败率超过90%，其中大部分不是因为"技术不行"，而是"场景选错了"。四要素评估法是**第一道筛选器**——在投入任何技术资源之前，先确认场景本身是否适合AI。

**暗知识**："找老的干小的"——从熟悉的、规模小的场景入手。因为AI只能干你会的事，你越会AI干得越好。

---

## 工具/环境

- src_unknown
- src_unknown

---

## 常见失败模式

| 失败现象 | 原因 | 解决方案 |
|---------|------|---------|
| "有方法"但实际不会 | 对"会"的定义过于宽泛 | 要求"能写出至少3步具体操作" |
| "有数据"但数据质量差 | 数据没有标注、不一致 | 先做数据清洗，再评估 |
| "有容错"但错误后果严重 | 低估错误的实际影响 | 做错误后果分析（FMEA） |
| 四要素全通过但项目失败 | 忽略了时间成本 | 追加"时间成本"评估 |
| 评估完一个场景都不敢做 | 过度评估导致 paralysis | 设定"评估时间上限"（10分钟） |

---

## 关联技能

- src_unknown
- src_unknown
- src_unknown

---

## 来源

- src_unknown
- src_unknown

---

## Feedback Path

- src_unknown
