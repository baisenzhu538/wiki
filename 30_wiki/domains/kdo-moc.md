---
id: kdo-moc
title: "KDO 主题域 MOC：KDO 自身的基建知识"
type: index
domain:
  - system
  - kdo
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
  - audience:huangyaoshi
  - audience:wangyuyan
  - scene:reference
  - skill-level:intermediate
aliases:
  - kdo MOC
  - KDO基建
  - KDO工具索引
  - 工厂基建
discoverable_by:
  - kdo MOC
  - KDO基建
  - KDO工具
  - 工厂基建
diagnostic_signals:
  - signal: 'KDO 域 52 张卡——基建知识、事故教训、工具脚本分散在各目录'
    severity: medium
    implication: '新黄药师会话启动时不知道有什么工具/教训可用——需要 MOC 做失忆恢复导航'
  - signal: 'KDO 域是唯一"工厂建设者"视角的域——其他域是方法论使用者视角'
    severity: low
    implication: '黄药师的专属域——其他角色偶尔查阅'
related:
  - '[[framework-kdo-modeling-methodology]]'
  - '[[framework-kdo-self-attack]]'
  - '[[concept-kdo-component-library]]'
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[dk-delivery-path-type-bug]]'
  - '[[dk-infrastructure-guardrails-over-checklist]]'
  - '[[dk-tool-chain-naming-is-infrastructure]]'
  - '[[dk-state-residue-is-the-silent-killer]]'
  - '[[dk-kdo-leaky-pipe-pressure]]'
  - '[[dk-publish-collapse-to-iterate]]'
  - '[[workflow-cross-agent-fact-dispute]]'
  - '[[tool-mcp-reachability-check]]'
  - '[[tool-kdo-help]]'
  - '[[graph-rag]]'
---

# KDO 主题域 MOC

> **定位**：KDO 域是黄药师的专属域——KDO 自身的基建知识、事故教训、工具脚本。52 张卡。此 MOC 是黄药师失忆恢复和新 Agent 入职的首选导航。

## 一句话

黄药师启动新会话，先来这——知道有什么工具、踩过什么坑、工厂怎么运作。

## 使用导航

| 你问的是 | 看这里 |
|:--|:--|:--|
| KDO 工厂怎么建 | [[framework-kdo-modeling-methodology]] |
| 怎么防止批量事故重演 | [[dk-E010-duplicate-key-detection]] |
| Agent 间事实争议怎么裁决 | [[workflow-cross-agent-fact-dispute]] |
| 搜索为什么坏了 | [[dk-delivery-path-type-bug]] |
| 基础设施设计原则 | [[dk-infrastructure-guardrails-over-checklist]] |
| 组件库有什么 | [[concept-kdo-component-library]] |
| 怎么自攻击 | [[framework-kdo-self-attack]] |
| 外部 Agent 怎么接入 | [[tool-kdo-help]] / [[tool-mcp-reachability-check]] |
| 检索架构 | [[graph-rag]] |

## 知识网络

```
KDO 主题域 MOC（本卡）
│
├── 工厂建设层
│   ├── framework-kdo-modeling-methodology    ← 建模方法论在 KDO 的应用
│   ├── framework-kdo-self-attack             ← 自攻击：四路 Agent 攻击卡片
│   ├── concept-kdo-component-library         ← KDO 17 张建模牌组
│   └── graph-rag                             ← 检索架构：Graph RAG + BM25 + RRF
│
├── 事故教训层（dk 系列）
│   ├── dk-E010-duplicate-key-detection       ← #222/#223 重复键事故
│   ├── dk-P42-agent-fact-check-gap           ← #224 核查缺位
│   ├── dk-delivery-path-type-bug             ← 搜索入口 Path 类型 bug
│   ├── dk-infrastructure-guardrails          ← 基础设施护栏 > 检查清单
│   ├── dk-tool-chain-naming-is-infrastructure ← 工具命名就是基础设施
│   ├── dk-state-residue-is-the-silent-killer ← 状态残留是隐形杀手
│   ├── dk-kdo-leaky-pipe-pressure            ← 管道漏水：堵了就硬塞
│   └── dk-agent-access-kdo-pitfalls          ← 外部Agent接入三连坑：审批门禁/cwd格式/检索规则过时
│
├── 工具与流程层
│   ├── tool-mcp-reachability-check           ← 可发现性自查
│   ├── tool-kdo-help                         ← 外部 Agent 新人引导
│   └── workflow-cross-agent-fact-dispute     ← 争议裁决协议
│
└── 改进计划层（17 张 improvement-plan）
    └── 历史改进计划存档——不展开，按需检索
```

## 核心关系

| 子主题 | 角色 | 什么时候看 |
|:--|:--|:--|
| 工厂建设 | 方法论 | 新基建项目启动前 |
| 事故教训 | 避坑 | 写批量脚本 / 修 bug 前 |
| 工具流程 | 执行 | 提交复审 / 外部 Agent 接入 |
| 改进计划 | 存档 | 查历史决策时 |

## KDO 域特色

- **黄药师专属**：52 张卡中大部分是 Builder 职责——基建、教训、工具。其他角色偶尔查阅
- **事故教训密集**：E010/P-42/delivery path bug 全部来自 8/3-8/4 事故窗口——KDO 域是"事故驱动进化"的活记录
- **与 master 域互补**：master 是跨域通用方法论，kdo 是 KDO 自身基建。两者有重叠但视角不同——master 看全局，kdo 看工厂
