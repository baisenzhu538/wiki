---
id: tool-demand-iceberg-l6-hypothesis
title: L6需求假设：机会卡片+最危险假设(RAT)
type: tool
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
updated_at: '2026-06-29'
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- yitang
- five-step-method
aliases:
  - L6需求假设
  - L6需求假设：机会卡片+最危险假设RAT
  - 最危险假设
  - 机会卡片
  - 机会卡片+最危险假设RAT
  - 需求假设
source_refs:
- 00_inbox/五步法之需求分析/AI场景推演教练提示词.txt
related:
- '[[yitang-domain-digest]]'
- '[[tool-strategy-ksf]]'
- '[[case-strategy-practice-11-third-place]]'
- '[[kdo-input-channel-strategy-2026-06-16]]'
- '[[case-strategy-failure-06-phone-n]]'
- '[[case-strategy-m-brand-profit-model]]'
- '[[case-strategy-practice-12-zero-loss]]'
- '[[sk-ai-narrative-test]]'
- '[[concept-smart-medicine-cabinet-platform-cooperation-validation]]'
- '[[dk-strategy-stage-leverage-mismatch]]'
- '[[yt-model-liberate-thinking-layers]]'
- '[[case-strategy-failure-04-appliance]]'
- '[[framework-strategy-pyramid]]'
- '[[framework-yitang-channel-exploration-4step]]'
- '[[case-strategy-retailer-activity-scope]]'
- '[[tool-demand-chai-tui-ping-suan-guide]]'
- '[[tool-demand-iceberg-l5-forces]]'
- '[[tool-demand-micro-experience-script]]'
- '[[tool-demand-option-explorer]]'
- '[[tool-demand-rat-generator]]'
- '[[tool-demand-report-template]]'
- tool-yitang-research-validate-assumption
tags:
- audience:executor
- scene:execution
- skill-level:advanced
- 五步法之需求分析
- 场景推演教练提示词
---

# L6需求假设

> L1-L5是深挖问题空间，L6是提出可验证的赌注。目标不是设计功能——是找到那个值得投入的假设，以及"什么情况下这个假设是错的"。

## 机会卡片模板

| 字段 | 说明 |
|:---|:---|
| **机会名称** | 切入点 + 核心价值（一句话） |
| **逻辑来源** | 基于L4的哪个崩溃环节 / L5的哪种力量洞察 |
| **建议产品形态** | MVP长什么样——最小可验证版本 |
| **最危险假设(RAT)×3** | 如果这些假设不成立，机会就不存在 |

## 最危险假设(RAT)

不是"所有风险"，是"如果这3条中有任何一条不成立，整个机会就不成立"的假设。

| # | RAT | 验证方法 | 验证成本 |
|:---|:---|:---|:---|
| 1 | 用户确实有这个痛点且愿意付费解决 | 5个用户访谈 | 2天 |
| 2 | 用户当前的替代方案足够痛苦到愿意切换 | 观察现有行为+追问 | 1天 |
| 3 | 我们的方案比替代方案好到用户愿意承担切换成本 | 低保真原型测试 | 3天 |

## Agent执行指令

```python
# 引自 AI场景推演教练 Step 5
prompt = """基于L4和L5的洞察，生成3-5张机会卡片。每张含：
- **适用**：前五层分析完成，需要形成可验证的机会假设
- **不适用**：用户自己还无法清晰描述问题——先回L1-L3补充
- **适用**：前五层分析完成，需要形成可验证的机会假设
- **不适用**：用户自己还无法清晰描述问题——先回L1-L3补充

最后用「评估三角形」（普遍性×频次×刚性）给每张机会打分。
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| RAT太弱 | "竞争对手可能跟进"——这是必定的 | RAT必须是"如果错了机会就不存在"级别 |
| 跳过L5直接L6 | 机会卡片看起来很好但没有深层洞察支撑 | 回溯：这个洞察来自L4/L5的哪个具体分析 |

## 适用边界

- **适用**：前五层分析完成，需要形成可验证的机会假设
- **不适用**：用户自己还无法清晰描述问题——先回L1-L3补充


## 口述案例

需求评估口述稿 L476-L536：Truman强调"机会假设必须有RAT（Riskiest Assumption Test）——不是验证你对的地方，是找最容易错的地方"

---

## 策略清单（9条）

| # | 策略 | 核心 | 来源 |
|:--|:---|:---|:---|
| 1 | 关键机会 | 有机会突破、满足更好的需求 | OCR |
| 2 | 关键风险RAT | 最危险假设测试——"如果这几条不成立，机会不存在" | OCR |
| 3 | 机会点A-E五原型 | A=摩擦点/B=替代方案/C=四种力量/D=隐性需求/E=微观体感 | OCR |
| 4 | Demo-Sell-Build倒序 | 先卖再建——用landing page测付费意愿，有付费再开发 | Lean Startup |
| 5 | 通过标准前置 | 写RAT前先定义"如果_____发生，假设被验证/被推翻" | — |
| 6 | 时间盒 | 每个RAT设定验证时间上限——超时未验证=自动标记"高风险" | CRV 2026 |
| 7 | 双重验证 | 同一RAT用两种方法验证（访谈+数据/定性+定量） | — |
| 8 | AI加速验证 | Agent自动搜索竞品数据/评论/趋势——RAT预验证 | — |
| 9 | 价值RAT | 在"可行性RAT"之外增加"价值RAT"——"即使能做，用户会付多少钱？" | — |

## 全网调研补强（2026 最佳实践）🆕

| # | 策略 | 来源 | 操作 |
|:--|:--|:--|:--|
| 1 | **五类假设分类** | Lean Startup 2026 | 将假设分五类：问题假设/客户假设/方案假设/渠道假设/经济假设——RAT 必须从交叉点（高致命+低证据）选 |
| 2 | **Demo-Sell-Build 倒序** | CRV 2026 | 先 Demo（做原型给人看）→ Sell（拿到预购/意向书）→ 再 Build（写代码）。大部分创始人跳进 Build |
| 3 | **通过标准前置** | User Intuition 2026 | 定义 RAT 时同步定义通过标准："≥60% 受访者主动描述痛点"——防止事后改标准 |
| 4 | **时间盒实验** | 2026 共识 | 每个 RAT 实验 ≤3 周、预算 $500-5000——超时说明实验设计太复杂 |
| 5 | **行为+定性双重验证** | Umbrex 2025 | 行为数据（点击/购买）告诉你 What，访谈告诉你 Why——只用一种会被误导 |
| 6 | **AI 加速循环** | 2026 新兴 | AI 主持的客户访谈可以把验证周期从月压缩到天——但 AI 不能替代真人对"情绪信号"的捕捉 |
| 7 | **最危险≠最有趣** | User Intuition | 不要把"最想验证的假设"和"最危险的假设"混淆——先杀死能杀死你的，再验证有趣的 |
| 8 | **价值 RAT** | Keenethics 2026 | 不是所有 RAT 都是商业模型级的——"用户会为这个功能付多少钱"本身的假设也应该被 RAT 检验 |

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

- **具体假设**：该工具假设"每个需求假设都有一个'最危险假设'(RAT)可以被识别和优先验证"，但 RAT 的识别本身就是一个主观判断——不同人可能识别出不同的 RAT。更关键的是，真正的"最危险假设"可能是"所有人都没意识到的那个"——它不在候选列表中。
- **边界**：在多变量交互的复杂场景中（如平台型业务），不存在单一的"最危险假设"——整个商业模式的可行性依赖于多个假设的同时成立，单独验证任何一个都无法反映系统性风险。
- **前提**：该工具的前提是"验证 RAT 的结果能快速决定 Go/No-Go"，但有些假设的验证需要数月甚至数年的市场数据——"用户是否愿意付费"不是一周能验证的。

**Eric Ries**（精益创业方法论创始人，《The Lean Startup》作者）会质疑：RAT 的概念与他的"最小可行产品"(MVP) 理念一致，但实践中团队常犯的错误是"把 RAT 验证当作二元判断"（验证通过=Go，验证失败=No-Go）。真正的学习不是"假设对不对"，而是"我们对用户的理解需要怎么修正"。RAT 验证失败后应该问的不是"放弃还是继续"，而是"我们之前漏掉了什么"——这才是"经证实的认知"（validated learning）。
