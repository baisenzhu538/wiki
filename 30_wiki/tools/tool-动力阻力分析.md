---
id: tool-动力阻力分析
title: 动力阻力分析：用户行为的推拉模型
type: tool
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.8
trust_level: medium-high
language: zh-CN
domain:
- yitang
- conversion-rate
aliases:
  - 动力阻力分析
  - 动力阻力分析：用户行为的推拉模型
  - 用户行为的推拉模型
source_refs:
- 00_inbox/Handle the business/conversion rate/转化率黑客-动力阻力触点-入门篇-口述.txt L3052-L3054
- 00_inbox/Handle the business/conversion rate/_vlm_output/images/转化率黑客的爬山地图_vlm.md
related:
- '[[framework-一堂-转化率黑客-总纲]]'
- '[[framework-一堂-动力三曲线]]'
- '[[framework-一堂-12种阻力总表]]'
- '[[framework-一堂-阻力方法论骨架]]'
- '[[framework-一堂-12触点SABC分级]]'
- '[[framework-一堂-转化率提升六步法]]'
- '[[framework-一堂-六大优化原则]]'
- '[[framework-一堂-十指模型]]'
- '[[tool-一堂-FAB说服法]]'
- '[[tool-一堂-名利权情动力法]]'
- '[[tool-一堂-影响力六原则]]'
- '[[tool-一堂-心理激励优先机制]]'
- '[[tool-一堂-阻力消除12策小抄]]'
- '[[tool-一堂-阻力挖掘方式]]'
- '[[tool-一堂-阻力三句话心法]]'
- '[[tool-一堂-马毅阻力消除四部曲]]'
- '[[tool-一堂-伏笔式消除法]]'
- '[[tool-一堂-不着急阻力两类消除]]'
- '[[tool-一堂-动嘴动手动钱成本纪律]]'
- '[[tool-一堂-七大转化场景自检]]'
- '[[conversion-rate-domain-digest]]'
- '[[case-yitang-dongyuan-dance-retention-c-vs-d]]'
- '[[case-yitang-yewenbin-archery-business-formula]]'
- '[[concept-一堂-脱离成本]]'
- '[[yt-business-formula-six-level-logic]]'
- '[[yt-business-formula-ten-paradigms]]'
- '[[yt-business-formula-peahd-roles]]'
- '[[framework-一堂-业务公式拆解-总纲]]'
- '[[tool-ai-prd-for-ai]]'
- '[[concept-X型Y型决策习惯]]'
- '[[case-yitang-innovative-metrics-collection]]'
- '[[case-yitang-fupanying-five-years-1000-hypotheses]]'
- '[[case-yitang-woqingke-referral-15-to-40]]'
- '[[case-yitang-laowenqi-huixiao-10x]]'
- '[[case-yitang-zhanglei-comic-booth]]'
- '[[case-yitang-zhanglei-gacha-points]]'
- '[[case-yitang-shipinhao-ads-l1-l6]]'
- '[[case-yitang-xingangwan-chess-room]]'
- '[[case-yitang-wenxiaozhang-driving-school]]'
- '[[case-yitang-wang-mcn-funnel]]'
- '[[case-yitang-panhonghai-entertainment]]'
- '[[case-yitang-marathon-ten-seasons]]'
- '[[yitang-domain-digest]]'
- '[[decision-science-domain-digest]]'
- '[[case-一堂-作业率20到50]]'
- '[[case-一堂-入职率50到80-100]]'
- '[[case-一堂-我请客推荐率5到40]]'
- '[[case-一堂-教研加微信率40到100]]'
updated_at: '2026-07-13'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
- conversion
- handle
---

# 动力阻力分析：用户行为的推拉模型

> **一句话**：用户为什么用（动力）和为什么不用（阻力）——两边的力量对比决定行为。转化率 = 动力 − 阻力 + 触点。

---

## Purpose

解决"只看到用户没转化，但说不清是动力不够还是阻力太大"的问题。把用户行为拆解为动力和阻力两个方向，帮助团队定位转化率瓶颈到底在"推"还是"拉"。

适用场景：
- 转化率诊断：先看动力侧还是阻力侧
- 产品/运营策略制定：决定是先提动力还是先降阻力
- 团队沟通：统一"转化率不是单一因素"的认知

---

## Protocol

### 第一步：列出当前转化场景

参考 `[[tool-一堂-七大转化场景自检]]`，确定当前要分析的场景（流量、一对多、一对一、门店、LTV、运营节点、组织内部）。

### 第二步：分别列出动力和阻力

| 方向 | 问题 | 示例 |
|---|---|---|
| **动力** | 用户为什么想行动？ | FAB 价值、名利权情、影响力 |
| **阻力** | 用户为什么不想/不敢行动？ | 12 种常见阻力 |
| **触点** | 用户在什么情境下被触发？ | SABC 分级触点 |

### 第三步：判断主要矛盾

- **动力明显不足**：先去 `[[tool-一堂-FAB说服法]]`、`[[tool-一堂-名利权情动力法]]`、`[[tool-一堂-影响力六原则]]`。
- **阻力明显过大**：先去 `[[tool-一堂-阻力挖掘方式]]`、`[[tool-一堂-阻力消除12策小抄]]`、`[[tool-一堂-阻力三句话心法]]`。
- **触点缺失/错位**：先去 `[[framework-一堂-12触点SABC分级]]`、`[[framework-一堂-触点本质论]]`。

### 第四步：量化力量对比

对每条动力和阻力按影响程度打分（1-5 分），计算：

```
转化倾向 = Σ动力 − Σ阻力 + 触点加成
```

触点加成：触点的质量、时机、频次是否放大了动力或削弱了阻力。

---

## Anti-patterns

| 反模式 | 症状 | 修复 |
|---|---|---|
| **只提动力不除阻力** | 营销很猛，但用户犹豫点没解决 | 同步做阻力挖掘 |
| **只降阻力不加动力** | 退款、分期都给了，用户还是没欲望 | 同步做 FAB/名利权情/影响力 |
| **动力和阻力混在一起说** | "用户没兴趣"说不清是动力还是阻力 | 强制分开列两张清单 |
| **忽略触点** | 动力和阻力都对，但触发时机不对 | 把触点作为独立变量分析 |

---

## When NOT to Use

- 数据完全缺失且无法快速获取时：动力阻力分析需要一定证据，不能纯靠脑补。
- 团队把工具当'算命'用时：它提供框架，不提供标准答案。
- 决策者拒绝接受'阻力可能大于动力'时：分析结果会被选择性忽视。

## Critique


**Daniel Kahneman**（诺贝尔经济学奖得主）会质疑：结构化流程本身可能制造'流程完成感'——执行者觉得走完了流程就等于做了好决策。
- 量化困难：动力和阻力的'打分'容易主观，不同人打分差异大。
- 触点的独立性被简化：触点的质量、时机、频次与动力/阻力相互影响，模型做了简化。
- 动态变化被忽略：用户动力和阻力会随时间、竞争、市场环境变化，分析结果会过时。


## Related

- `[[framework-一堂-转化率黑客-总纲]]`：转化率 = 动力 − 阻力 + 触点
- `[[framework-一堂-动力三曲线]]`：动力侧三层结构
- `[[framework-一堂-12种阻力总表]]`：阻力侧 12 种分类
- `[[framework-一堂-12触点SABC分级]]`：触点侧分级
- `[[conversion-rate-domain-digest]]`：D 域完整导航

---

## 案例区：动力阻力分析应用

### 案例 1：董原舞蹈培训——C 域 vs D 域的取舍

> 见 `[[case-yitang-dongyuan-dance-retention-c-vs-d]]`：通过动力阻力分析判断舞蹈培训的核心问题是留存（D 域）还是商业模式（C 域）。

### 案例 2：叶文彬射箭馆——业务公式与转化率的联动

> 见 `[[case-yitang-yewenbin-archery-business-formula]]`：先用业务公式找战场，再用动力阻力分析打转化节点。
