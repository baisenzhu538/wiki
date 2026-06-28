---

id: tool-yitang-signup-statistics
title: 线上签约统计：通过自增ID推算用户/订单量
type: tool
status: enriched
author: 老顽童
reviewed_by: 待审
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
  - yitang
  - research
source_refs:
- 00_inbox/调研专题/调研超级武器库_ocr_text.md
related:
  - [[tool-yitang-anonymous-roundtable]]
  - [[tool-yitang-bidding-analysis]]
  - [[tool-yitang-shareholder-analysis]]
  - [[tool-yitang-security-guard-intel]]
  - [[tool-yitang-bp-analysis]]
  - [[tool-yitang-reverse-data-analysis]]
  - [[tool-yitang-weapon-product-reverse]]
---
# 线上签约统计

> 如果竞对的用户ID/订单号是自增的，通过观察ID变化推算用户量和订单量。

**做法**：注册一个账号→看自己的用户ID→隔一段时间再注册一个→看ID差值→推算日均新增用户。同理，下单后看订单号→隔几天再下一单→推算日均订单量。

**价值**：这是逆向数据分析中最简单但最有效的一招。不需要爬虫、不需要技术能力——只需要注册两个账号。

**坑**：不是所有系统都用自增ID（有些用随机ID/UUID）；ID差值可能包含取消订单和测试数据。

---

*卡片类型：tool | 审核状态：待审*
