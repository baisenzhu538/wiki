---
id: tool-lean-minimum-test-volume
title: 只测试最小数量
type: tool
status: enriched
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: medium
language: zh-CN
domain:
- strategy
- yitang
- product
source_refs:
- 00_inbox/精益创业/一堂DOC-20260622212431_ocr_text.md
- 00_inbox/精益创业/一堂DOC-20260622212431_vlm_desc.md
- 00_inbox/精益创业/一堂DOC-20260622212440_ocr_text.md
- 00_inbox/精益创业/一堂DOC-20260622212440_vlm_desc.md
related:
- '[[case-lean-electric-scooter-mvp]]'
- '[[framework-lean-six-wastes]]'
- '[[strategy-domain-digest]]'
- '[[yitang-domain-digest]]'
- '[[pending_unknown]]'
---

# 只测试最小数量

> 把“验证范围”压缩到单次实验真正需要的最小规模，用更少的用户、更少的库存、更少的门店、更少的 SKU 验证同一个关键假设。

## 一句话定义

只测试最小数量是一种降低试错成本的规模控制工具，验证的核心假设是：**关键假设能否在极小的真实用户/交易/运营样本中得到有效信号**，从而避免为了“看起来像正式业务”而过早扩大测试规模 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md]。

## Purpose

- src_unknown
- src_unknown
- src_unknown

## 操作步骤

### 第一步：识别本次实验要验证的关键假设

- src_unknown
- src_unknown

### 第二步：在五个维度上压缩测试规模

| 维度 | 最小化做法 | 验证什么问题 |
|:---|:---|:---|
| **用户维度** | 只测试最疼的种子用户 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md] | 核心用户是否真的有痛点 |
| **采购维度** | 只采购最小的测试数量 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md] | 小批量采购能否跑通供应链和履约 |
| **门店维度** | 只做一家体验门店 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md] | 单店模型是否成立 |
| **SKU 维度** | 只做一个 SKU 开始测试 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md] | 单一产品价值主张是否被接受 |
| **用户规模维度** | 只招 100 个体验用户上课 [conf=0.85, source=一堂DOC-20260622212431_ocr_text.md] | 课程/服务在小样本中是否产生真实价值 |

### 第三步：设定“最小数量”的判定标准

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 第四步：执行并记录真实行为数据

- src_unknown
- src_unknown

### 第五步：根据信号决定放大、调整或停止

- src_unknown
- src_unknown

## 成本 / 周期 / 样本量

| 维度 | 经验参考 | 说明 |
|:---|:---|:---|
| 周期 | 1 天到 2 周 | 海报/单页测意向可 1-3 天；单店/摆摊可 1-2 周；单 SKU 试销可 1-4 周 [conf=0.70, source=讲师案例推演 + 案例卡数据] |
| 成本 | 几十元到数万元 | 仅招募种子用户可接近 0 成本；单店/小批量试销约数千到数万元 [conf=0.70, source=讲师案例推演] |
| 用户样本 | 6-100 人 | 深度访谈/陪跑 6-10 人；体验课程/社群约 100 人 [conf=0.70, source=一堂DOC-20260622212431_ocr_text.md] |
| 采购/库存 | 最小可交付批次 | 以“验证完即可用完/退完”为原则，避免压货 [conf=0.75, source=framework-lean-four-principles] |
| 门店 | 1 家体验店或 1 个摊位 | 单点验证成功后，再考虑复制 [conf=0.80, source=framework-lean-false-model] |

> 以上数字为经验区间，实际受产品形态、获客成本、客单价、转化率影响较大，不应作为刚性标准。

## 适用边界

### 最适合

- src_unknown
- src_unknown
- src_unknown

### 需要调整

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## When NOT to Use

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **为了少而少，样本失真** | 只找 3 个朋友测试，结果全是正向反馈 | 明确目标用户画像，引入陌生用户或真实付费场景 |
| **把最小数量当成最终数量** | 100 人体验课跑完就认为是产品市场匹配 | 设定升级标准，通过后再扩大样本验证 |
| **压缩数量但不压缩假设** | 一次小实验想同时验证需求、定价、渠道、SKU | 每次只验证一个关键假设，其他变量固定 |
| **忽视负面信号的统计意义** | 因为样本小，把明显的负向反馈解释为“偶然” | 提前定义“不通过”标准，达到即停止或调整 |
| **只压缩用户数量，不压缩运营复杂度** | 只招 100 人，却搭建完整会员、营销、履约系统 | 同步压缩系统、流程和团队投入，保持整体最小化 |

## Critique

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 案例映射

### 正例：共享电动滑板车 C/D 版验证

在 [[case-lean-electric-scooter-mvp]] 中，D 版用一张海报/落地页测意向，C 版只买 20 台普通滑板车在地铁口摆摊验证，2 周、约 2 万元完成核心假设验证 [conf=0.70, source=transcript_低成本验证实操1_剥离假设篇.md]。

- src_unknown
- src_unknown

### 反例：过早扩张的线下业务

在 [[framework-lean-six-wastes]] 覆盖的“过早扩张”案例中，部分创业者在单店模型未跑通前就开多家店、铺多个 SKU，最终发现核心假设不成立时，库存、租金、人员成本已经难以收回 [conf=0.70, source=讲师案例]。

- src_unknown
- src_unknown

---

*老顽童 · 2026-06-23 · 源：一堂精益创业 FALSE 模型讲义*
