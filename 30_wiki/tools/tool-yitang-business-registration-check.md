---
id: tool-yitang-business-registration-check
title: 工商查询：社保人数+股权穿透+关联公司
type: tool
status: enriched
author: 老顽童
reviewed_by: pending
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- yitang
- research
source_refs:
- 00_inbox/调研专题/调研超级武器库_ocr_text.md
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[tool-yitang-database-index]]'
- '[[tool-yitang-shareholder-analysis]]'
- '[[tool-yitang-weapon-public-official-info]]'
- '[[tool-yitang-weapon-third-party-database]]'
updated_at: '2026-06-30T16:07:51+00:00'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
aliases:
- 调研专题
- 调研超级武器库
---

# 工商查询

> 天眼查/企查查/爱企查——免费的情报数据库。

**三大查询维度**：
1. **社保人数变化**：最诚实的公司规模指标（连续下降=裁员/衰退）
2. **股权穿透**：实控人是谁、有没有代持、有没有关联交易
3. **司法风险**：官司多不多、什么类型的官司（劳动仲裁多=管理问题；合同纠纷多=履约问题）

**坑**：社保数据可能有滞后（1-3个月）；部分公司通过派遣规避社保显示。

*卡片类型：tool | 审核状态：待审*

## Purpose

工商查询用于在开展深度调研、投资评估或合作尽职调查前，快速建立对目标公司的“公共信息基线”。通过免费的企业信息平台，判断一家公司是否真实存在、规模是否在扩张、实际控制人是否稳定，以及是否存在高风险的司法或经营异常记录，从而为后续访谈、现场调研和财务分析提供可验证的事实锚点。

## Protocol

1. **锁定主体**：在天眼查/企查查/爱企查输入目标公司全称，核对统一社会信用代码、成立时间、注册资本、实缴资本、法定代表人及经营范围，确认查询对象无误。
2. **看社保人数趋势**：进入“参保人员”或类似页面，导出近12–24个月的社保人数曲线，标记连续下降、骤减或长期为零的异常拐点。
3. **做股权穿透**：利用股权穿透图识别实际控制人、主要股东、境外架构及关联企业，绘制核心利益关系网。
4. **查司法与行政风险**：检索立案信息、裁判文书、被执行人、经营异常、行政处罚、股权质押与知识产权出质，按风险类型与金额分类标注。
5. **交叉验证**：将工商快照与一手访谈、现场照片、招聘数据、财报或行业报告进行比对，形成经多源验证的结论。

## When NOT to Use

| 场景 | 不宜原因 | 替代工具/方法 |
|---|---|---|
| 目标为未注册个体户或初创团队 | 工商库中无记录或信息极少 | `[[tool-yitang-social-media-interview]]`、实地走访 |
| 需要判断真实竞争力或战略意图 | 工商数据只反映静态结构，不反映能力 | `[[framework-yitang-research-weapon-system]]`、专家访谈 |
| 涉及家族代持、VIE或隐性关联交易 | 公开股权结构可能被设计隔离 | `[[tool-yitang-shareholder-analysis]]`、律师/会计师尽调 |
| 需要精确实时财务数据 | 社保与注册资本信息存在滞后 | `[[tool-yitang-financial-report-intelligence]]`、审计报告 |

## 质疑

工商查询的可靠性建立在若干容易被忽略的前提之上。首先，**具体假设**之一是“社保人数真实反映在职规模”，但外包、劳务派遣、异地缴纳、子公司拆分都会让这一指标失真。其次，**边界**在于工商平台只收录已登记、已公示的信息，对未诉讼的私下纠纷、口头协议、灰色资金往来无能为力。**反例**也很常见：某些公司为掩盖裁员，会在年末突击补缴社保，使曲线出现假性回升；或者通过多层SPV与代持协议，让实际控制人躲在公开股东之后。

从外部反对者视角看，**Michael Porter** 会指出：公开工商数据充其量只是产业结构快照，它无法告诉你企业的真实竞争优势来源，也无法替代对价值链、客户结构与战略定位的深度分析。因此，使用工商查询时必须明确其**前提**：它适合验证“有没有”“大不大”“稳不稳”，而不适合回答“强不强”“值不值”。

## Synthesis

- [[tool-yitang-shareholder-analysis]]
- [[tool-yitang-court-record-search]]
- [[framework-yitang-six-layer-cross-validation]]
- [[case-yitang-luckin-field-research]]
