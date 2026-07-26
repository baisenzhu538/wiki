---
id: framework-demand-ceiling-four-lines
title: 需求天花板四层线：TAM/SAM/SOM/CR1/BEL
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-08
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- yitang
- demand-analysis
source_refs:
- 00_inbox/五步法之需求分析/一堂-需求分析-空间测算-口述.txt L322-L344,L1308-L1870,L2252-L2278,L2348
- 00_inbox/五步法之需求分析/一堂-需求分析-需求评估-口述.txt L1720-L1796,L1962-L1976
related:
- '[[tool-demand-assessment-triangle]]'
- '[[tool-demand-iceberg-l6-hypothesis]]'
- '[[tool-demand-ceiling-coach]]'
- '[[yt-market-size-estimation]]'
- '[[framework-demand-opportunity-spectrum]]'
- '[[domain-demand-analysis-index]]'
- '[[yt-entrepreneur-unit-model]]'
diagnostic_signals:
- signal: 创始人说"我们的市场是万亿级的"但无法说清SOM是多少
  lens: 天花板估算跳跃——从TAM直接跳到"我们能做到XX%"
  follow-up: 用四层线逐层收紧，从TAM→SAM→SOM→CR1→BEL
- signal: 融资BP里的市场规模数字和内部经营计划对不上
  lens: 融资版vs经营版未区分——两套算法混用
  follow-up: 明确当前场景是融资版还是经营版，用对应算法
quality_labels:
- principle
- actionable
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---

# 需求天花板四层线：TAM/SAM/SOM/CR1/BEL

> **一句话**：大多数创业者把"天花板"讲成一个数，但在五步法的需求分析里，天花板不是算出来的——是"一层层紧"出来的。TAM→SAM→SOM→CR1→BEL，五层收紧，融资版和经营版算法不同。

---

## 一、五层线定义

| 层 | 全称 | 含义 | 典型数字 | 用途 |
|:---|:---|:---|:---|:---|
| **TAM** | Total Addressable Market | 理论上所有可能需要你产品的人 | 万亿级/千亿级 | 融资BP的"第一页数字" |
| **SAM** | Serviceable Available Market | 你的产品形态能触达的 | 百亿级 | 证明"这不是一个小赛道" |
| **SOM** | Serviceable Obtainable Market | 你在可见未来能拿到的 | 十亿/几亿 | 经营版的核心指标 |
| **CR1** | Category Revenue Year 1 | 第一年在这个品类能做的收入 | 千万/百万级 | 经营版的第一年目标 |
| **BEL** | Baseline Existence Line | "活下去"的最低线 | 几百万/几十万 | 创始人自己心里清楚，不对外说 |

---

## 二、融资版 vs 经营版

| 维度 | 融资版 | 经营版 |
|:---|:---|:---|
| **重点层** | TAM、SAM | SOM、CR1、BEL |
| **数字特征** | 大、好看、引用第三方报告 | 小、务实、自己算/验证过的 |
| **常见错误** | TAM说得太大（万亿市场）但SOM说不清 | SOM用TAM的1%来算——这是懒人算法 |
| **正确做法** | TAM引用第三方；SAM说清"为什么是这个数" | SOM从底往上算：CR1×增速×拓展系数=BEL→SOM |
| **谁看** | 投资人 | 创始人自己、合伙人、核心团队 |

> 口述稿 L1308-L1320：Truman强调"融资看TAM/SAM，经营看SOM/CR1/BEL——两套算法不混用。"

---

## 三、SOM的正确算法

**错误做法**（L1720-L1732）：
> "中国XX市场有1000亿，我们拿1%就是10亿"——这叫"1%拍脑袋法"。

**正确做法**（L1732-L1796）：从底往上算

```
Step 1: BEL = 你确认"死活都能做到"的收入
       → 不是预估，是已经验证过的或者有合同背书的

Step 2: CR1 = BEL × (1 + 增速系数)
       → 增速系数基于：渠道能力×产品差异化×团队执行力（1.2-3x）

Step 3: SOM = CR1 × (1 + 拓展系数)²
       → 拓展系数基于：品类增速×竞争格局×复制能力
       → 不是线性外推，第二年通常比第一年难

Step 4: SAM = SOM × 品类适配系数
       → 你在当前品类的SOM，能不能适配到相邻品类？

Step 5: TAM = SAM × 场景泛化系数（融资版用，经营版跳过）
       → 融资BP里才需要这一步
```

---

## 四、空间测算口述稿核心原则（L322-L344）

| 原则 | Truman原话 | 实践含义 |
|:---|:---|:---|
| **空间≠需求** | "空间是你算出来的市场容量，需求是用户真正愿意为之付费的东西" | 算完TAM后问：这里面有多少人真的会付钱？ |
| **从底往上算** | "不要从TAM往下拆，要从BEL往上垒" | 先确认BEL，一层层往上垒 |
| **每年重新算** | "去年算的空间今年可能已经变了" | 天花板不是一次性计算 |
| **算三遍** | "乐观/中性/悲观各算一遍" | 单一数字不可靠 |

---

## 五、失败模式

| 模式 | 症状 | 修复 |
|:---|:---|:---|
| TAM虚高 | "万亿市场"但引用的报告是5年前的 | 用最近12个月的第三方数据 |
| 1%拍脑袋 | "市场X亿，我们拿1%"——为什么是1%？ | 从BEL往上垒，不要从TAM往下拆 |
| 融资经营混用 | BP里TAM的数字和内部SOM对不上 | 明确标注"融资版"和"经营版" |
| BEL不诚实 | 自己心里知道BEL其实没达到但对外说达到了 | BEL是给自己看的——骗自己最贵 |
| 增速系数拍脑袋 | "第二年翻3倍"——没有依据 | 增速系数必须基于渠道/产品/团队的实际能力估算 |

---

## Action Triggers

| 触发 | 动作 | 指标 |
|:---|:---|:---|
| 准备融资BP | 算完整的TAM→SAM→SOM（融资版） | TAM有第三方来源，SAM有"为什么" |
| 制定年度经营计划 | 从BEL往上垒到SOM | SOM不是TAM的1%算出来的 |
| 被问到"天花板在哪" | 不报一个数——报五层 | 每层有独立算法 |
| 市场环境变了 | 重新算一遍天花板 | 每条线至少更新SOM |
