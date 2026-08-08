---
id: case-truman-investment-daily-report
title: 「案例：招商日报30→90分——不是换工具，是叠Feature」
type: case
status: draft
confidence: 0.90
trust_level: high
domain:
  - ai-basic
  - ai-collaboration
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
source_person: Truman/伟强
source_context: Truman口述下 L596-690（伟强招商日报优化过程）
reviewed_by: 待审
aliases:
  - 招商日报
  - 30到90分
  - 伟强
discoverable_by:
  - 招商日报
  - 30到90
  - 伟强
  - Feature叠加
related:
  - framework-truman-feature-thinking-core
  - framework-truman-feature-layered-system
  - case-truman-ai-image-workflow-evolution
  - case-truman-temperature-parameter
  - 10_raw/sources/feature-periodic-table-v0.8.json
tags:
  - method:feature-thinking
  - method:optimization
  - scene:ai-automation
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
  - signal: "AI自动化输出质量差但不知道怎么改"
    lens: 可能只换工具不叠Feature——"不是工具不好，是Feature不够"
    follow_up: 像伟强一样——先加信息源，再加判断规则，再加模型切换
---

> 本卡属于 [[framework-truman-feature-layered-system]] 的案例层——从30分到90分的Feature叠加路径。

# 招商日报30→90分：不是换工具，是叠Feature

> 一句话：伟强用Cubox做招商日报——初期30分。没有换工具，而是叠了信息源+判断规则+模型切换+周榜+二次筛选五个Feature，最终90分，成本降10倍。

---

## 四阶段

| 阶段 | 叠了什么Feature | 分数 | 行号 |
|:---|:---|:---|:---|
| **初始** | Cubox自动抓取→原始输出 | 30分 | L596-610 |
| **+信息源+规则** | 金融早报信息源 + 最终意图（明确读者/标准）+ 判断规则（加分/扣分/分类） | 50分 | L614-636 |
| **+模型切换** | 换巨米模型——从1元/次→0.1元/次，成本降10倍 | 70分 | L642-646 |
| **+周榜+二次筛选** | 每日推Cubox→加周榜规则→二次筛选 | 90分 | L648-652 |

---

## 初始状态为什么只有30分

"Cubox抓过来很快很按时——但是离想要的信息十万八千里，数量质量完全不合格"（L608-610）。纯工具思维：以为"有工具=问题解决"。

## 关键转折：建判断规则

伟强做的关键一步（L628-636）：把"审美"翻译成加分规则——一级加几分、湖北加几分、软文扣四分。规则化了判断标准。同时定下保底规则：国际5条、国内8条。

"不是用了什么工具，而是打破了多少壁垒"（口述下 L654-656）——原文：不是简单换工具，是叠了更多Feature。

---

## Feature叠加清单

| 步骤 | Feature | 层 |
|:---|:---|:---|
| 1 | Cubox自动抓取 | L3 |
| 2 | +信息源（金融早报项目） | L2 |
| 3 | +最终意图（明确读者+标准） | L2 |
| 4 | +判断规则（加分/扣分/分类） | L2 |
| 5 | +模型切换（巨米→成本1/10） | L1 |
| 6 | +周榜规则 | L2 |
| 7 | +二次筛选 | L2 |

---

## 关键数字

| 数据 | 来源 | 状态 |
|:---|:---|:---|
| 初期30分 | 口述下 L610 | ✅ 可核实 |
| 换巨米模型后成本降10倍（1元→0.1元/次） | 口述下 L644 | ✅ 可核实 |
| 最终90分，一周下100+条 | 口述下 L648-652 | ✅ 可核实 |

## 教训

1. **工具只是载体——Feature才是提升质量的手段**
2. **判断规则化=把隐性审美变成显性Feature**
3. **成本也是一个Feature——模型切换不只是"更好"，可以是"更便宜"**

## 可迁移场景

| 场景 | 迁移 |
|:---|:---|
| AI自动化日报/周报 | 先看当前质量→按"信息源→规则→模型→筛选"顺序叠Feature |
| 任何AI输出质量不满意 | 不换工具——先问"还能叠什么Feature？" |

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 只换工具不叠Feature | 换了一个AI工具→还是不满意→再换一个 | 在现有工具里叠Feature——信息源→规则→模型→筛选 |
| 叠了Feature但不打分 | 不知道哪个Feature有效 | 每个阶段打分（30→50→70→90）——数字是Feature有效性的证据 |
| 判断规则太主观 | "这个新闻重要"——人说了算，AI不知道 | 把主观判断翻译成可量化的加分/扣分规则 |
