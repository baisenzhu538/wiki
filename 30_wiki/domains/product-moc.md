---
id: product-moc
title: "Product 主题域 MOC：产品方法论与精益验证"
type: index
domain:
  - system
  - product
status: draft
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-06
confidence: 0.85
trust_level: observed
source_refs:
  - 30_wiki/domains/retrospective-moc.md
created_at: 2026-08-06
updated_at: 2026-08-06
tags:
  - audience:laowantong
  - audience:ouyangfeng
  - scene:reference
  - skill-level:intermediate
aliases:
  - product MOC
  - 产品索引
  - 产品方法论
  - 精益验证
discoverable_by:
  - product MOC
  - 产品索引
  - 产品方法论
  - 精益验证
diagnostic_signals:
  - signal: 'Product 域 89 张卡——产品内核/精益验证/泛产品设计三个子主题无导航'
    severity: high
    implication: '老顽童查产品方法论时需要逐个 grep ——MOC 缺位意味着导航靠碰运气'
  - signal: 'Product 域以 tool(40)和 case(15)为主——实操卡碎片化程度高'
    severity: medium
    implication: '没有 MOC 聚合时，用户不知道"产品内核"和"精益验证"的关系'
related:
  - '[[concept-一堂-product-kernel]]'
  - '[[concept-一堂-kernel-iteration]]'
  - '[[concept-一堂-kernel-validation]]'
  - '[[yt-product-kernel-iteration]]'
  - '[[yt-product-kernel-validation]]'
  - '[[yt-product-kernel-aesthetic]]'
  - '[[yt-product-kernel-failure-modes]]'
  - '[[yt-product-kernel-cost-sensitive-default-no]]'
  - '[[yt-product-kernel-do-without-belief]]'
  - '[[yt-product-kernel-overpromise-trap]]'
  - '[[yt-composite-pan-product-methodology]]'
  - '[[case-lean-genki-forest-toolkit]]'
  - '[[case-milktea-five-step]]'
  - '[[concept-一堂-product-kernel]]'
  - '[[concept-一堂-business-prediction]]'
---

# Product 主题域 MOC

> **定位**：Product 域涵盖一堂的产品方法论体系——产品内核、精益验证、泛产品设计。89 张卡，此 MOC 回答"产品域有什么、内核和精益什么关系、从哪开始"。

## 一句话

做产品相关决策时，先来这——知道产品内核和精益验证的边界，知道从哪张卡入手。

## 使用导航

| 你问的是 | 看这里 |
|:--|:--|:--|
| 产品内核是什么 | [[concept-一堂-product-kernel]] |
| 怎么找到产品内核 | [[concept-一堂-kernel-iteration]] — 迭代方法论 |
| 怎么验证内核对不对 | [[concept-一堂-kernel-validation]] — 三维验证 |
| 产品内核的审美 | [[yt-product-kernel-aesthetic]] |
| 内核会怎么失败 | [[yt-product-kernel-failure-modes]] |
| 泛产品设计全景 | [[yt-composite-pan-product-methodology]] |
| 精益创业怎么落地 | [[case-lean-genki-forest-toolkit]] — 元气森林案例 |
| 产品内核迭代实操 | [[yt-product-kernel-iteration]] + [[yt-product-kernel-validation]] |
| 商业预判怎么做 | [[concept-一堂-business-prediction]] |

## 知识网络

```
Product 主题域 MOC（本卡）
│
├── 产品内核层（一堂核心方法论）
│   ├── concept-一堂-product-kernel            ← 内核定义：用户愿付费的最小可行产品
│   ├── concept-一堂-kernel-iteration          ← 迭代方法：静态→动态，假设驱动演化
│   ├── concept-一堂-kernel-validation         ← 三维验证 + 低成本测试
│   └── yt-product-kernel-aesthetic            ← 审美：内核的"味道"和"温度"
│
├── 内核暗知识层（dk 系列）
│   ├── yt-product-kernel-failure-modes        ← 内核会怎么失败
│   ├── yt-product-kernel-cost-sensitive       ← 成本敏感陷阱
│   ├── yt-product-kernel-do-without-belief    ← "没有也行"的信念
│   ├── yt-product-kernel-overpromise-trap     ← 过度承诺陷阱
│   └── dk-ai-builder-illusion                 ← Builder 幻觉：AI 辅助≠从 0 到 1
│
├── 精益验证层（cases + tools）
│   ├── case-lean-genki-forest-toolkit         ← 元气森林试错工具箱
│   ├── case-lean-electric-scooter-mvp         ← 电动滑板车 A/B/C/D 四级 MVP
│   ├── case-lean-2b-gray-test                 ← 2B 灰度测试
│   ├── case-lean-wrong-demand                 ← 需求错误案例
│   ├── case-lean-perfectionism-traps          ← 完美主义陷阱
│   └── case-milktea-five-step                 ← 奶茶五步法案例
│
├── 泛产品设计层
│   ├── yt-composite-pan-product-methodology   ← 泛产品设计方法论综述
│   ├── case-panproduct-top135-selection       ← Top 1/3/5 筛选打磨
│   └── case-panproduct-yitao-project          ← 项目背景分析
│
└── 商业预判层
    └── concept-一堂-business-prediction       ← 15字诀+光谱模型
```

## 核心关系

| 子主题 | 角色 | 入门卡 |
|:--|:--|:--|
| 产品内核 | 方法论核心 | concept-一堂-product-kernel |
| 内核迭代 | 怎么找内核 | concept-一堂-kernel-iteration |
| 内核验证 | 怎么验证 | concept-一堂-kernel-validation |
| 内核暗知识 | 坑在哪 | yt-product-kernel-failure-modes |
| 精益验证 | 怎么试 | case-lean-genki-forest-toolkit |
| 泛产品设计 | 全景视角 | yt-composite-pan-product-methodology |

## Product 域特色

- **三层结构清晰**：内核（what）→ 迭代验证（how）→ 精益案例（prove it）
- **内核相关卡密集**：一堂产品内核是整个域的基石——大部分 tool/case 卡围绕内核展开
- **与精益域桥接**：精益验证层大量引用 lean-startup 域卡片——product 和 lean-startup 有天然交叉
