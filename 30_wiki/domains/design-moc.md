---
id: design-moc
title: "Design 主题域 MOC：知识库的 AI 设计知识网络"
type: index
domain:
  - system
  - design
status: draft
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-06
confidence: 0.85
trust_level: observed
source_refs:
  - 60_feedback/tasks/task_20260806_huangyaoshi-design-moc.md
created_at: 2026-08-06
updated_at: 2026-08-06
tags:
  - audience:hongqigong
  - audience:laowantong
  - audience:ouyangfeng
  - scene:reference
  - skill-level:intermediate
aliases:
  - design MOC
  - 设计索引
  - 设计知识网络
  - AI设计导航
discoverable_by:
  - design MOC
  - 设计索引
  - AI设计导航
  - 设计域有哪些
diagnostic_signals:
  - signal: 'Design 是 276 张的大域——228 张 tool 卡散落 tools/ 目录，无 MOC 时找卡靠运气'
    severity: high
    implication: '洪七公生产视觉资产时不知道有哪些 AI 设计工具卡可用——B6/W8 两张牌退化为碰运气'
  - signal: 'Design 子主题跨度大——AIGC基础/口喷电商/泛产品/视觉/审美，无索引无法导航'
    severity: high
    implication: '按 domain 字段聚合只能列出卡名——不知道各卡的关系和分工'
  - signal: 'Design 域以 tool 卡为主(228/276)——MOC 的导航价值比 framework 域更大'
    severity: medium
    implication: 'Tool 卡天然碎片化——更需要 MOC 做聚合导航'
related:
  - '[[aigc设计基础01ai生图原理与提示词基本功]]'
  - '[[aigc设计师实操培训01口喷设计范式与电商ai设计全流程]]'
  - '[[aigc文创案例设计课leo文创ip从0到1全流程]]'
  - '[[视觉prompt三层操作系统-srom-visual-os]]'
  - '[[数据标注维度最佳实践调研报告]]'
  - '[[case-live81-ai-trademark-design]]'
  - '[[case-panproduct-top135-selection-polish]]'
  - '[[case-panproduct-yitao-project-background]]'
  - '[[case-yihang-dual-triangle-tianmo-design-delivery]]'
  - '[[yt-composite-pan-product-methodology]]'
  - '[[framework-一堂-表达力火箭模型]]'
---

# Design 主题域 MOC

> **定位**：Design 域是 KDO 最大的工具密集型域（276 张，228 张 tool）。此 MOC 是导航入口，按子主题组织，回答"设计域有什么、怎么选工具、从哪开始"。

## 一句话

做 AI 设计相关内容时，先来这——不用在 tools/ 目录里翻 228 张卡。

## 使用导航

| 你问的是 | 看这里 |
|:--|:--|
| AI 生图怎么入门 | [[concept-AIGC设计基础01-AI生图原理与提示词基本功]] |
| AI 辅助设计全流程怎么做 | [[concept-AIGC设计师实操培训01-设计品质控制与AI辅助全流程]] |
| 文创/IP 设计从 0 到 1 | [[concept-AIGC的文创设计课-Leo文创IP从0到1全流程]] |
| 视觉 Prompt 怎么写 | [[concept-视觉Prompt操作系统-SROM-Visual-OS]] |
| AI 设计怎么练习 | [[dk-设计师AIGC练习方式-MVP快速上手]] |
| AI 会取代设计师吗 | [[dk-AI时代设计师转型还是转行]] |
| 泛产品设计全貌 | [[framework-一堂-泛产品设计36计-全套地图]] |
| 设计落地工具箱 | [[dk-泛产品设计落地工具篇]] |
| 有没有真实案例 | [[case-一堂Live81-AI设计马拉松全流程拆解]] |
| 设计 x 表达力 | [[framework-一堂-表达力火箭模型]] |

## 知识网络

```
Design 主题域 MOC（本卡）
│
├── AIGC 基础层（concepts，月白域）
│   ├── concept-AIGC设计基础01               ← AI 生图原理 + 提示词基本功
│   ├── concept-AIGC设计师实操培训01          ← 设计品质控制 + AI 辅助全流程
│   ├── concept-AIGC的文创设计课              ← Leo 文创 IP 从 0 到 1
│   └── concept-视觉Prompt操作系统            ← SROM Visual OS 六层系统
│
├── AI 设计实操层（dk/tools，洪七公主力域）
│   ├── dk-设计师AIGC练习方式-MVP快速上手     ← 练习路径
│   ├── dk-AI时代设计师转型还是转行           ← 职业判断
│   ├── dk-AI图像生成模型训练                 ← 创意素材提取
│   ├── dk-AI设计-图片生产流程                ← 生产管线
│   └── concept-数据标注维度最佳实践          ← 标注方法论
│
├── 泛产品设计层（frameworks/concepts，一堂域）
│   ├── framework-一堂-泛产品设计36计-全套地图 ← 36 计总纲
│   ├── dk-泛产品设计落地工具篇               ← 落地工具箱
│   ├── dk-泛产品设计-审美工具箱指南          ← 审美建设
│   └── 泛产品设计-用户卡片/落地卡片系列       ← 12 张实操卡片
│
├── 案例层
│   ├── case-一堂Live81-AI设计马拉松          ← 全流程拆解
│   ├── case-设计域top1-top3-top5筛选打磨      ← 品控筛选
│   └── case-一堂双三角-设计域                 ← 双三角案例
│
└── 桥接层
    ├── framework-一堂-表达力火箭模型          ← 设计 x 表达力
    ├── 审美库 x 设计（预留）                  ← 洪七公审美资产
    └── 多模态 x 设计（预留）                  ← 洪七公多模态管线
```

## 核心关系

| 子主题 | 角色 | 从哪开始 |
|:--|:--|:--|
| AIGC 基础 | 入门三件套 | concept-AIGC设计基础01 |
| AI 设计实操 | 动手练习 | dk-设计师AIGC练习方式 |
| 泛产品设计 | 方法论全景 | framework-一堂-泛产品设计36计 |
| 视觉 Prompt | 高级技能 | concept-视觉Prompt操作系统 |
| 设计案例 | 验证参考 | case-一堂Live81-AI设计马拉松 |

## 设计域特色

- **工具密集型**：228/276 是 tool 卡——意味着 MOC 的导航价值比方法论域更高
- **月白 + 一堂双源**：AIGC 基础来自月白（一堂 AIGC 设计课口述 3 期），泛产品设计来自 Truman/一堂方法论
- **洪七公主力域**：视觉资产生产、OCR→结构化、图片→prompt 全部依赖 design 域卡片
- **子主题边界清晰**：AIGC 基础 ≠ 泛产品设计 ≠ 视觉 Prompt——MOC 帮洪七公判断"该用哪套工具"

## ⚠️ 状态联动提醒

MOC 节点状态（draft/reviewed）随卡状态变化。卡状态变化时需同步更新此 MOC 中的标注。当前状态基于 2026-08-06 队列。
