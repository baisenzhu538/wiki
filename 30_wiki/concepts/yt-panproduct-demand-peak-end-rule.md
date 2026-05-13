---
id: yt-panproduct-demand-peak-end-rule
title: 泛产品设计·用户卡片：峰终定律
type: tool
status: enriched
domain:
- yitang
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.8
prerequisites:
- yt-composite-pan-product-methodology
component_of:
- yt-model-pan-product-demand-toolkit
related:
- yt-panproduct-demand-surprise-formula
- yt-panproduct-demand-motivation-resistance
- yt-model-conversion-optimization
contradicts: []
query_triggers:
- 峰终定律
- 泛产品设计
- 泛产品设计·用户卡片：峰终定律
- 用户卡片
- 用户研究
- 用户需求
- 需求分析
- 需求洞察
tags:
- '#yitang'
- '#pan-product-design'
- '#user-experience'
- '#peak-end-rule'
yitang:
  map: personal
  module: 泛产品设计
  course_type: card
  level: intermediate
source_refs:
- 10_raw/assets/yitang/泛产品设计-用户卡片-峰终定律.png
created_at: '2026-05-11'
updated_at: '2026-05-13'
estimated_tokens: 2500
reviewed_by: 黄药师
---

# 峰终定律：用户体验的二八定律

> 需求工具箱第 9 张卡片。[[yt-model-pan-product-demand-toolkit]] | [[yt-model-pan-product-36-strategies]] | [[一堂]]

## Claims

### 核心机制：记忆≠平均

- claim:01 [conf=0.85] 峰终定律（Kahneman, 1999）的核心洞察：用户对一段体验的记忆不是所有时刻的平均值，而是由峰值时刻（最好或最差的那个点）和终值时刻（体验结束时的感受）决定的。一堂将框架扩展为四要素：峰值 + 终值 + 初值 + 底线值。初值和底线值是峰终定律在中国产品实践中的补充——初值决定用户是否进入体验，底线值决定体验是否崩盘

| 时刻 | 含义 | 设计策略 |
|------|------|---------|
| **峰值 (Peak)** | 体验最高/最低点 | 设计一个 wow moment |
| **终值 (End)** | 体验结束时的感受 | 设计一个温暖的结尾 |
| **初值** | 第一印象 | 降低入门摩擦 |
| **底线值** | 体验最低可接受线 | 避免致命失误 |

### 精选案例

- claim:02 [conf=0.90] **迪士尼的排队体验**：排队本身是负面体验，但迪士尼在排队过程中设计了互动装置、角色巡游（峰值），离园时的烟花秀是精心设计的终值。用户离开时记住的不是"排了2小时队"，而是"烟花太好看了"——峰值和终值覆盖了平均体验。即使平均等待时间和其他游乐园一样长，峰终设计让迪士尼的满意度评分高出竞品 30% 以上

- claim:03 [conf=0.85] **一堂训练营的结营仪式**：训练营的日常学习体验是平稳的（中等峰值），但结营仪式被设计为情绪终值——学员互写卡片、教练逐一告别、结营证书颁发。很多学员对训练营的记忆锚定在结营那一刻的感受上，"不舍"和"成长"成为整个训练营的记忆标签，而非"每天打卡挺累的"

- claim:04 [conf=0.85] **反面案例：某在线教育产品的 wow moment 陷阱**：产品花重金设计了开课第一天的惊喜体验（峰值极高），但日常答疑响应慢、作业批改质量参差（底线值塌了）。结果用户评价是"开头很好但后面不行"——因为底线值持续低于用户最低可接受线，峰值的高光反而反衬了日常的落差。用户离开时的终值不是惊喜，而是失望

### 与相邻工具的区分

- claim:05 [conf=0.80] 峰终定律解决"用户记住什么"——它是体验的记忆过滤器。惊喜公式解决"怎么制造超出预期的瞬间"——它是峰值的具体设计方法之一。动力阻力解决"用户为什么卡住了"——它是转化路径的诊断工具。三者协同的典型路径：先用动力阻力找到最值得优化的触点 → 用峰终定律确定这个触点上应该设计峰值还是终值 → 用惊喜公式实现那个时刻的具体体验设计

## Constraints & Boundaries

- claim:boundary-01 [conf=0.90] 峰终定律在**重复性高频场景**下可能失效。当用户体验足够多次后，记忆曲线被拉平——用户不再用"峰值"和"终值"评价，而是用"平均水平"。企业 IM 工具每天用 8 小时、外卖 App 每天打开 3 次——这类产品的用户评价靠的是底线值稳定性而非某个 wow moment。判断标准：用户对体验的记忆是"事件式回忆"（如"那次旅行"）还是"统计式评价"（如"这个 App 还行"）——前者适用峰终定律，后者适用平均值逻辑

- claim:boundary-02 [conf=0.90] 资源有限时，**先保底线值再做峰值**。底线值塌了，峰值再高也无意义——用户根本走不到那个 wow moment 就已经离开了。这是峰终定律被滥用时最常见的失败模式：把资源砸在峰值设计上，但基础体验烂到用户在峰值之前就已流失。正确的资源分配顺序：(1) 底线值覆盖全链路，(2) 初值降低进入摩擦，(3) 峰值和终值做关键触点。如果资源只够做一步，先修底线

- claim:boundary-03 [conf=0.80] 终值设计有一个常见误区——**把"没有终值"误认为"体验自然结束"**。产品如果不主动设计体验的结束方式，用户会自己找——通常以负面事件（遇到 Bug、厌倦了、有更好替代品）为终值。不设计终值 = 让负面事件成为默认终值。判断标准：检查用户离开产品的最后三个交互是什么——如果其中任何一个是被动结束（而非主动完成），终值大概率是负面的

## Visual Analysis

卡片用 PEAK/END 两个英文词作为主视觉锚点，下方配上 EXPERIENCE 和 TIME——暗示用户体验是时间维度上的曲线而非点状评估。峰值被图形化呈现为体验曲线的最高点。初值和底线值被补充标注在曲线两端，形成四要素框架。"二八定律"的类比被用来传达核心洞察：20% 的关键时刻决定 80% 的用户记忆。

## Framework Gallery

### 关联框架卡
- [[yt-model-pan-product-demand-toolkit]] — 所属工具箱总指南
- [[yt-model-pan-product-36-strategies]] — 泛产品36计总框架
- [[yt-composite-pan-product-methodology]] — 泛产品设计方法论总纲

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 互补工具 | [[yt-panproduct-demand-surprise-formula]] | 惊喜公式——峰值设计的具体执行方法。峰终定律告诉你"需要一个峰值"，惊喜公式告诉你"怎么制造这个峰值"。但惊喜只在"期望≤实际"的场景有效，峰终定律的峰值不一定要靠惊喜——高稳定性也能成为峰值（如"这个产品的客服居然每次都5分钟内响应"） |
| 互补工具 | [[yt-panproduct-demand-motivation-resistance]] | 动力阻力——确定峰终设计的目标触点。组合路径：动力阻力分析找到转化路径上的 S 级触点 → 在 S 级触点上设计峰终体验。不是每个触点都需要峰终设计，只在动力阻力标记的关键转化节点上做 |
| 关联框架 | [[yt-model-conversion-optimization]] | 转化率优化——S/A/B/C 触点分级与峰终四要素的对应：S 级触点值得做峰值+终值设计，A/B 级保底线值，C 级只保底线值 |
| 父框架 | [[yt-model-pan-product-demand-toolkit]] | 需求工具箱总指南——第9张卡片 |
| 实体页 | [[一堂]] | 一堂实体页 |
