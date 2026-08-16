---
id: retrospective-moc
title: "复盘主题域 MOC：知识库的复盘知识网络"
type: index
domain:
  - system
  - management
  - personal-growth
status: draft
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-06
confidence: 0.85
trust_level: observed
source_refs:
  - 60_feedback/tasks/task_20260806_huangyaoshi-retrospective-moc.md
  - 60_feedback/diagnosis/diag_20260806_wangyuyan-deep-review.md
created_at: 2026-08-06
updated_at: 2026-08-06
tags:
  - audience:ouyangfeng
  - audience:wangyuyan
  - audience:laowantong
  - scene:reference
  - skill-level:intermediate
aliases:
  - 复盘MOC
  - 复盘索引
  - 复盘知识网络
  - 复盘主题域
discoverable_by:
  - 复盘MOC
  - 复盘索引
  - 复盘知识
  - 复盘有哪些
diagnostic_signals:
  - signal: '复盘卡散落四个目录——无MOC时导航靠grep碰运气'
    severity: high
    implication: '王语嫣诊断时靠grep才发现项目复盘卡——没命中就漏。B6/W8两张牌全部退化为碰运气'
  - signal: '横向主题无域归属——复盘跨管理/个人成长/项目管理三个域'
    severity: high
    implication: '按domain字段归类时复盘卡散落在不同域下——结构必然'
  - signal: 'MOC节点中有#233/#234新建卡——状态标注避免导航到未完成卡'
    severity: medium
    implication: 'MOC标注了queued/reviewed状态——用户知道哪些卡已可用哪些待生产'
related:
  - '[[framework-一堂-复盘本质与三要素]]'
  - '[[framework-一堂-四象限复盘法]]'
  - '[[framework-一堂-团队复盘四阶段12策略]]'
  - '[[tool-复盘浪费九宗罪自检清单]]'
  - '[[dk-借假修真与黑盒白盒]]'
  - '[[yt-model-deep-review-iceberg]]'
  - '[[framework-yitang-project-retrospective]]'
  - '[[tool-复盘推演法]]'
  - '[[tool-复盘推演练习]]'
  - '[[case-一堂-优秀转化率复盘合集]]'
  - '[[case-一堂-A加社失败归因→一堂诞生]]'
  - '[[case-一堂-迷你访谈五周迭代]]'
  - '[[case-一堂-教材品控事故]]'
  - '[[case-莹莹-before-after复盘]]'
  - '[[case-duanwangye-self-iteration-closed-loop]]'
  - '[[bridge-个人复盘×知识管理W-Z-K-P]]'
  - '[[yt-personal-deep-review]]'
  - human-insights-domain-digest
---

# 复盘主题域 MOC

> **定位**：复盘是跨域横向能力——知识散落在 concepts/frameworks/tools/cases 四个目录。此 MOC 是导航入口，回答"知识库的复盘知识有哪些、各自什么关系、怎么选"。

## 一句话

被问到"复盘"相关的任何问题时，先来这——不用 grep 碰运气。

## 使用导航

| 你问的是 | 看这里 |
|:--|:--|
| 复盘到底是什么、值不值得做 | [[framework-一堂-复盘本质与三要素]] |
| 不同情况该用哪种复盘 | [[framework-一堂-四象限复盘法]] |
| 怎么带团队养成复盘习惯 | [[framework-一堂-团队复盘四阶段12策略]] |
| 复盘常见的坑有哪些 | [[tool-复盘浪费九宗罪自检清单]] |
| 复盘能挖多深 | [[yt-model-deep-review-iceberg]] |
| 项目收尾怎么做复盘 | [[framework-yitang-project-retrospective]] |
| 事前怎么推演 | [[tool-复盘推演法]] |
| 有没有真实案例 | [[case-一堂-优秀转化率复盘合集]] 等 4 张 |
| 复盘跟学习/知识管理什么关系 | [[yt-personal-deep-review]] / [[bridge-个人复盘×知识管理W-Z-K-P]] |

## 知识网络

```
复盘主题域 MOC（本卡）
│
├── 底层能力层（#233 新建）
│   ├── framework-一堂-复盘本质与三要素    ← 判定+ROI规律+三原则。复盘第一课
│   ├── framework-一堂-四象限复盘法        ← 场景选择：决策/执行×成败
│   ├── framework-一堂-团队复盘四阶段12策略 ← 以身作则→挂嘴边→提要求→做流程
│   ├── tool-复盘浪费九宗罪自检清单        ← 意识/姿势/深度三分类
│   └── dk-借假修真与黑盒白盒              ← 事情是假的，认知才是真的
│
├── 深度标尺层（已有 reviewed）
│   └── yt-model-deep-review-iceberg       ← 冰山五层+五飞跃。Edmondson/Argyris 双攻击者
│
├── 应用场景层（已有）
│   ├── framework-yitang-project-retrospective ← 项目复盘 16 字诀（美团）。一个环节
│   ├── tool-复盘推演法 / tool-复盘推演练习     ← 事前推演。另一个环节
│   └── case-一堂-优秀转化率复盘合集           ← 已有案例
│
├── 案例层（#234 新建）
│   ├── case-一堂-A加社失败归因→一堂诞生  ← 20元获客→9.9崩塌→四维归因→47坟
│   ├── case-一堂-迷你访谈五周迭代          ← 感觉→事实→原因→模型逐层调参
│   ├── case-一堂-教材品控事故              ← 归因到能力层全链路
│   ├── case-莹莹-before-after复盘          ← 吸收率 3%→50%，before/after 实证
│   └── case-duanwangye-self-iteration-closed-loop ← Agent自迭代：五绝首例（#252试点后）
│
├── 桥接层（#233 新建 + 预留）
│   ├── bridge-个人复盘×知识管理W-Z-K-P    ← 复盘=知识萃取起点
│   └── 预留：复盘×教练式领导力（等素材）
│
└── 相邻体系（已有）
    └── yt-personal-deep-review             ← 周子敬 IPO/科学学习，元认知层
```

## 核心关系

| 卡 | 角色 | 一句话 |
|:--|:--|:--|
| 复盘本质与三要素 | 入门 | 什么是复盘、值不值得、什么时候做 |
| 四象限复盘法 | 场景路由 | 不同情况该用哪种 |
| 12 策略 | 能力建设 | 怎么带团队养成 |
| 九宗罪 | 自查清单 | 3×3 自检 |
| 借假修真 dk | 心法 | 高阶认知：黑盒变白盒 |
| 冰山图 | 深度标尺 | 挖多深（五层+五飞跃） |
| 16 字诀 | 项目场景 | 一个环节——项目收尾流程 |
| 推演法 | 事前场景 | 另一个环节——事前模拟 |
| IPO 课 | 元认知 | 复盘=从经验中学=IPO 第一策略 |

**区分关键**：项目复盘 16 字诀=一个环节（项目收尾流程）；深度复盘=一种能力（一切经验学习的底层方法）；冰山图=深度标尺（挖多深）；四象限=场景选择（挖什么）；12 策略=能力培养（怎么带团队）。

## MOC 建设模板（可复制到其他横向主题）

1. 扫描全库相关卡（按关键词 grep + domain 字段）
2. 按层级组织：底层能力层 → 深度标尺层 → 应用场景层 → 案例层 → 桥接层 → 相邻体系
3. 核心关系一句话（每张卡在本主题中的角色）
4. 使用导航表（"你问的是 X → 看 Y"）
5. 节点 related 双向闭合
6. ⚠️ MOC 状态联动：MOC 标注了各节点的 status（queued/draft/reviewed）——卡状态变化时需同步更新 MOC。建议在 card_review_checklist 或 pre-submit 中加"若卡在 MOC 中，提交时提醒更新 MOC 状态标注"
