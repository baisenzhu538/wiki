---

id: dk-yb7-design-demand-80-10-10
title: 中国设计需求的80-10-10分层法则
type: dk
dark_knowledge_type: insight
status: enriched
domain:
- design
- yitang
- business-strategy
source_person: 月白
source_context: '口述稿: AI设计-AI设计基础01'
source_refs:
- 10_raw/sources/src_20260604_design-ai-basics-01.md
created_at: 2026-06-04
updated_at: '2026-06-19'
related:
  - '[[dk-yb30-ecommerce-channel-version]]'
  - '[[dk-yb21-ecommerce-pricing-independent-model]]'
  - '[[dk-yb10-theory-moat-designer]]'
  - '[[dk-yb25-solution-driven-visual-design]]'
  - '[[dk-yb6-midjourney-chinese-text-fix]]'
  - '[[dk-yb21-ecommerce-pricing-independent-model]]'
  - '[[dk-yb25-solution-driven-visual-design]]'
  - '[[dk-yb1-aigc-mvp-before-ps]]'
pipeline:
- confidence-source-cited
author: 月白
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
diagnostic_signals:
- signal: 设计团队编制规划时，把所有需求混在一起评估，导致"要不要用AI替代设计师"变成非黑即白的争论
  framework_lens: 需求分层缺失——80%模板化需求、10%强创意需求、10%弹性缓冲需要完全不同的工具和人力策略
  follow_up_question: 过去一个月的设计需求中，有多少比例是节日海报/朋友圈素材/日常运营物料？这些是否已模板化或AI化？
- signal: 团队引入AI工具后，资深设计师被拉去做大量运营素材，创意产出反而下降
  framework_lens: 人力资源错配——高端人才被低端需求消耗
  follow_up_question: 你团队里最贵的设计师上周有多少时间花在"调风格"而非"做设计"上？
---# 中国设计需求的80-10-10分层法则

## 原始表述

> 本质上中国80%的设计需求都是常规的运营需求。海报、节日朋友圈素材，这些完全可以模板化风格用ROI去调或者由AI生成初稿之后，剩下的10%需要强创意的部分，才需要专业设计师深入用PS或者AIGC介入。

## 使用场景

设计公司老板、设计团队负责人、甲方市场部负责人，在做设计团队编制规划或AI工具采购决策时参考。

## 操作方法

1. 梳理历史设计需求，按"节日海报/朋友圈/日常运营物料" vs "品牌campaign/视觉体系/创意概念"分类
2. 前者用Canva/稿定设计/AI生成工具+固定模板库解决，考核ROI（产出速度、修改轮次）
3. 后者保留资深设计师，用PS/AIGC深度介入，考核创意突破性
4. 中间10%作为弹性缓冲，根据业务周期动态调配人力

## 适用边界

| 边界 | 说明 |
|:-----|:-----|
| **不适用奢侈品/高端时尚/艺术策展** | 审美门槛极高的行业，每一张图都需要深度创意。 |
| **不适用超大型品牌年度视觉战略项目** | 战略级项目不适合模板化。 |
| **不适用设计师个人IP工作室** | 个人风格是核心资产，模板化会稀释品牌。 |
| **易混淆：AI生成≠替代设计师** | 80%用AI初稿+人工品控，10%深度人工，始终需要品牌调性校准和最终品控。 |

## 常见失败模式

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| 一刀切AI化 | 所有需求都推给AI，品牌视觉同质化严重 | 按80-10-10分层：运营类→AI+模板，创意类→人+AIGC深度介入 |
| 高端人力做低端活 | 资深设计师被节日海报/朋友圈素材占满时间 | 将80%运营需求模板化，解放资深设计师做10%的创意突破 |
| 忽视中间10%弹性缓冲 | 模板化和深度创意之间没有过渡带，需求波动时人手不足或闲置 | 中间10%根据业务周期动态调配，旺季支援运营，淡季投入创意 |
| AI初稿直接交付 | AI生成后不经过品牌调性校准就发出去 | AI初稿→人工品牌检查（字体/配色/调性）→交付 |

## 行动 Checklist

- [ ] 是否已统计过去3个月设计需求的类型分布（运营 vs 创意 vs 其他）？
- [ ] 80%的运营类需求是否已建立模板库和AI生成流程？
- [ ] 资深设计师的时间分配：创意占比是否≥50%？如果不是，什么在消耗他们？

## 为什么值钱

这个数据化的分层判断（80%+10%）来自一线设计服务市场的真实体感，而非行业报告的理论推演。公开语料中要么是"AI将取代设计师"的焦虑叙事，要么是"设计师不可替代"的防御姿态，极少出现这种基于中国本土市场结构（运营驱动、高频低客单价）的务实分层策略。ROI导向的"调风格"而非"做设计"的表述，是服务过大量中小客户的从业者才会有的精准措辞。

## 与其他知识的关联

- [[dk-yb21-ecommerce-pricing-independent-model]] — 电商定价：线上价格带需独立建模
- [[dk-yb25-solution-driven-visual-design]] — 解决方案驱动视觉设计
