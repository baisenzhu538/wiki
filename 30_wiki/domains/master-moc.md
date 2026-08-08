---
id: master-moc
title: "Master 主题域 MOC：KDO 知识工厂的自身运营知识"
type: index
domain:
  - system
  - master
status: reviewed
author: 黄药师
reviewed_by: 欧阳锋
review_date: 2026-08-06
confidence: 0.85
trust_level: observed
source_refs:
  - 30_wiki/domains/retrospective-moc.md
created_at: 2026-08-06
updated_at: 2026-08-06
tags:
  - audience:huangyaoshi
  - audience:ouyangfeng
  - audience:wangyuyan
  - scene:reference
  - skill-level:intermediate
aliases:
  - master MOC
  - KDO运营知识
  - 踩坑库索引
  - 工厂知识
discoverable_by:
  - master MOC
  - KDO运营知识
  - 踩坑库
  - 工厂知识
diagnostic_signals:
  - signal: 'Master 域 109 张卡 53 张 dk——KDO 的踩坑库散落，无 MOC 时重复踩坑'
    severity: high
    implication: 'Agent 遇到问题时不知道已有对应坑记录——P-42 核查缺位、E010 重复键检测等教训可能被再次触发'
  - signal: 'Master 域是唯一"自指"域——其他域是方法论，master 是 KDO 自身运营'
    severity: medium
    implication: '新 Agent 入职或黄药师失忆恢复时，没有 master MOC 导航 = 从零开始摸索工厂运作'
related:
  - '[[concept-kdo-component-library]]'
  - '[[framework-kdo-self-attack]]'
  - '[[framework-kdo-modeling-methodology]]'
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[dk-delivery-path-type-bug]]'
  - '[[dk-c8-format-complete-mind-empty]]'
  - '[[dk-c10-batch-tool-no-dry-run]]'
  - '[[dk-infrastructure-guardrails-over-checklist]]'
  - '[[dk-kdo-leaky-pipe-pressure]]'
  - '[[dk-tool-chain-naming-is-infrastructure]]'
  - '[[dk-state-residue-is-the-silent-killer]]'
  - '[[dk-publish-collapse-to-iterate]]'
  - '[[kdo-flywheel]]'
  - '[[master-decision-hygiene]]'
  - '[[master-systems-thinking]]'
---

# Master 主题域 MOC

> **定位**：Master 域是 KDO 的自身运营知识——跨所有域的通用方法论 + KDO 工厂踩坑库。109 张卡，53 张 dk。此 MOC 回答"工厂有什么问题被踩过、怎么避免、怎么运作"。

## 一句话

遇到任何 KDO 工厂问题（脚本 bug / 流程缺陷 / Agent 行为异常），先来这——大概率有人踩过同款坑。

## 使用导航

| 你问的是 | 看这里 |
|:--|:--|:--|
| KDO 工厂怎么运作 | [[kdo-flywheel]] |
| 批量操作怎么不出事 | [[dk-c10-batch-tool-no-dry-run]] / [[dk-c8-format-complete-mind-empty]] |
| Agent 遇到什么常见坑 | C 系列 / F 系列 / P 系列 dk 卡（53 张） |
| 怎么防止重复踩坑 | [[dk-E010-duplicate-key-detection]] / [[dk-P42-agent-fact-check-gap]] |
| 基础设施设计原则 | [[dk-infrastructure-guardrails-over-checklist]] / [[dk-tool-chain-naming-is-infrastructure]] |
| 决策方法论 | [[master-decision-hygiene]] |
| 系统思考 | [[master-systems-thinking]] |
| KDO 组件库 | [[concept-kdo-component-library]] |
| 知识工厂怎么建 | [[framework-kdo-modeling-methodology]] |

## 知识网络

```
Master 主题域 MOC（本卡）
│
├── 工厂运作层
│   ├── kdo-flywheel                ← KDO 飞轮：捕获→消化→生产→反馈
│   ├── framework-kdo-modeling-methodology  ← 建模方法论在 KDO 自身的应用
│   ├── concept-kdo-component-library       ← KDO 17 张建模牌组
│   └── dk-kdo-leaky-pipe-pressure          ← 管道漏水：流程堵了就硬塞
│
├── 踩坑库（53 张 dk，按系列组织）
│   ├── C 系列（10 张）— 内容质量坑：C-1 regex / C-8 格式空洞 / C-10 无 dry-run
│   ├── F 系列（14 张）— 工厂基础设施坑：F-3 竞态 / F-13 YAML 解析 / F-14 准确率
│   ├── P 系列（20+ 张）— 流程坑：P-1 切模型 / P-13 token 黑洞 / P-42 核查缺位
│   ├── E 系列（新）— 事故教训：E010 重复键 / P-42 争议裁决
│   └── dk 独立卡 — 设计原则：infrastructure-guardrails / tool-chain-naming / state-residue / publish-collapse-to-iterate（发布=知识迭代入口）
│
├── 方法论层（跨域通用）
│   ├── master-decision-hygiene              ← 决策卫生五步法
│   ├── master-systems-thinking              ← 系统思维：反馈循环+杠杆点
│   ├── master-ai-info-literacy              ← AI 时代信息素养
│   └── master-knowledge-compound            ← 知识复利：IPO+萃取+原子化
│
└── 基础概念层
    ├── concept-knowledge-delivery-os        ← KDO 概念总纲
    ├── concept-learning-thinking            ← 学习与思考
    └── concept-sprint-2-门禁验证报告        ← Sprint 2 验证
```

## 核心关系

| 子主题 | 角色 | 什么时候看 |
|:--|:--|:--|
| C 系列 dk | 内容生产坑 | 老顽童批量生产前 |
| F 系列 dk | 基础设施坑 | 黄药师写脚本前 |
| P 系列 dk | 流程坑 | 任何 Agent 遇到异常时 |
| E 系列 dk | 事故教训 | 事故处置后——防止复发 |
| 方法论层 | 通用能力 | 欧阳锋审查 / 王语嫣编排 |

## Master 域特色

- **自指性**：Master 域是唯一"关于 KDO 自身"的域——所有其他域是商业方法论，master 是工厂运作知识
- **dk 密集型**：53/109 是 dk 卡（48.6%）——对比 design 域 33/276（12%），master 的踩坑密度是 design 的 4 倍
- **新人导航价值最高**：新 Agent 入职或黄药师失忆恢复，读 master MOC → 了解工厂运作 + 避免复踩已知坑
- **与 pitfalls.md 互补**：pitfalls.md 是流水账，master MOC 是导航地图
