---
id: tool-osint-maltego
title: Maltego：实体关系图谱——画出目标公司的隐藏网络
type: tool
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- research
aliases:
  - Maltego：实体关系图谱画出目标公司的隐藏网络
  - 关系图谱
  - 实体关系图谱
  - 画出目标公司的隐藏网络
  - 目标公司的隐藏网络
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- proposal-prompt-injection-infrastructure
- tool-agent-spec-yitang-objection-handler
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# Maltego：实体关系图谱

> 输入一个域名、人名、公司名或邮箱，Maltego自动搜索并绘制关联网络——谁控股谁、谁认识谁、谁和谁有共同利益。

## 核心能力

| 输入 | 能画出什么 |
|:---|:---|
| 公司域名 | 子公司/母公司、关联域名、DNS记录、SSL证书 |
| 人名+公司 | 社交媒体账号、关联公司、共事过的人 |
| 邮箱地址 | 绑定的社交账号、出现过的数据泄露 |
| IP地址 | 托管了什么服务、地理位置、关联域名 |

## Agent执行指令

```bash
# Maltego 需要桌面客户端（Community版免费）
# 安装后通过 Transform Hub 安装需要的数据转换器
# CLI 自动化可选 maltego-trx (Python库)
pip install maltego-trx
# 编写自定义 Transform 后通过 Maltego 客户端调用
```

## 实战场景

**场景**：调研一家公司的真实背景
1. 输入公司域名 → 发现3个未公开的关联域名
2. 通过关联域名的WHOIS → 发现同一个注册人
3. 该注册人还注册了另一家公司 → 发现潜在竞品或子公司
4. 通过SSL证书 → 发现他们最近部署的新服务（新业务线）

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 关联过度解读 | 两个人出现在同一个活动就推断"有关系" | 区分"已知关联"和"推断关联"，标注置信度 |
| 数据过时 | WHOIS/SSL信息未更新 | 标注每条数据的时间戳 |
| 被图形误导 | 图太复杂反而看不清核心关系 | 先聚焦1-2个关键节点，再逐步展开 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"实体关系图谱能揭示隐藏的网络结构"，但 Maltego 的图谱质量完全取决于"数据源的质量"——如果数据源（如公开注册信息、社交媒体 API）不完整或过时，图谱呈现的"隐藏网络"只是"部分网络"。
- **边界**：在隐私保护日益加强的环境中（GDPR、数据删除权），Maltego 能获取的公开数据在持续减少——图谱的"可画性"在下降。
- **前提**：该工具的前提是"关系图谱中的连接 = 真实关系"，但两个实体出现在同一地址、同一域名、同一时间线上，不等于它们有实质性的业务关系——相关性不等于因果性。

**Valdis Krebs**（社会网络分析专家，OrgNet 创始人）会质疑：Maltego 的可视化效果让人产生"看到了全貌"的错觉——但图谱只是"数据源能看到的部分"。真正的隐藏网络（如地下经济、利益输送）不会出现在公开数据源中。更危险的是，图谱中的"空缺"——两个实体之间没有连接——可能不是"没有关系"，而是"关系被刻意隐藏了"。有经验的情报分析师会告诉你："最危险的连接是你看不到的那条"。
