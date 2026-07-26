---
id: tool-一堂-关键假设-ABCD场景分类器
title: 工具：关键假设 ABCD 场景分类器——把问题分到商业/决策/增长/转化并标成败·效率
type: tool
status: pending_review
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.84
trust_level: high
language: zh-CN
created_at: 2026-07-09
updated_at: 2026-07-09
domain:
- yitang
- key-assumptions
source_refs:
- 00_inbox/一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt
- 00_inbox/一堂-关键假设课-truman-口述.txt L1064-L1074
related:
- '[[framework-一堂-关键假设-ABCD模型]]'
- '[[framework-一堂-关键假设]]'
- '[[framework-一堂-关键假设-三板斧]]'
- '[[framework-一堂-业务公式拆解-总纲]]'
- '[[tool-一堂-hypothesis-validation-three-axe]]'
- '[[framework-lean-abcd-model]]'
- '[[yt-decision-abcd-model]]'
- '[[framework-yitang-project-abcd-classification]]'
quality_labels:
- actionable
- framework
tags:
- audience:executor
- scene:execution
- skill-level:advanced
aliases:
- 关键假设
- 关键假设课
---

# 工具：关键假设 ABCD 场景分类器

> **一句话**：拿到一个业务问题或一条关键假设，先用本工具分两刀——第一刀**成败/效率**，第二刀**宏观/微观**——落到 **A 商业 / B 决策 / C 增长 / D 转化** 之一，并直接给出匹配工具与验证路径。上位框架见 [[framework-一堂-关键假设-ABCD模型]]。

---

## 何时用

**适合用**：
- 拿到一条关键假设，不知道用哪个工具验证
- 团队在「能不能成」和「怎么做更好」之间扯皮，需要先对齐问题类型
- 进入 [[framework-一堂-关键假设-三板斧]] 减法之前，要先给每条假设标场景（成败类优先）

**不要用**：
- 已经清楚问题类型（如明确就是转化优化 D）→ 直接用 [[yt-business-formula-six-level-logic]] L4，不必再分类
- 想给项目分级流程轻重 → 那是 [[framework-yitang-project-abcd-classification]]（项目复杂度 A/B/C/D），不是本工具
- 从 0 到 1 新品类，四场景都不完全适用 → 先用设计思维

---

## 需要什么

| 输入 | 必需 | 说明 |
|:---|:---:|:---|
| 一条关键假设或一个业务问题 | 是 | 用「我们以为…」或「X 能不能成/能不能更好」句式 |
| 当前业务阶段 | 是 | 想法期/已验证/有产品/有收入——影响成败/效率判断 |
| 该假设在逻辑链的位置 | 否 | 越靠前越偏成败；靠后（转化节点）越偏效率 |

---

## 操作步骤

**Step 1：第一刀——成败还是效率？**

问：「如果这条假设不成立，是整个业务倒，还是只是做得更好/更差？」
- 整个业务倒 / 模式跑不通 → **成败问题**（进 A/B）
- 只是更好/更差、可优化 → **效率问题**（进 C/D）

**Step 2：第二刀——宏观还是微观？**

- 成败问题里：偏方向/全局（赛道、人群、单元模型）→ **A 商业场景**；偏某个关键决策点（定价、投产比、是否进入某渠道）→ **B 决策场景**（B 横跨宏观—微观，按决策主要层面归）
- 效率问题里：偏规模化/增长能力 → **C 增长场景**；偏具体转化节点（详情页→下单、试听→付费）→ **D 转化场景**

**Step 3：落场景 + 标维度**

输出格式：`[场景字母] [成败/效率] · [宏观/微观]`，例如 `A 成败·宏观`、`D 效率·微观`。

**Step 4：匹配工具与验证路径**

| 落到 | 匹配工具/卡 | 验证路径 |
|---|---|---|
| A 商业场景 | [[framework-一堂五步法]] + [[framework-一堂-关键假设-三板斧]] | 证伪实验：先验证「人群愿意付费/单元模型跑通」 |
| B 决策场景 | [[tool-key-assumptions-check]] + [[framework-一堂-业务公式拆解-总纲]]（L5） | 证伪实验 + ROI 定量：投产比能否为正 |
| C 增长场景 | [[yt-business-formula-ten-paradigms]] + [[framework-一堂五步法]]（Step 5） | 公式下钻：获客/留存/复购哪个低于基准 |
| D 转化场景 | [[yt-business-formula-six-level-logic]]（L4） | 漏斗拆解：定位断点，针对断点优化 |

**Step 5：顺序闸门**

- 若同一批假设里既有 A/B（成败）又有 C/D（效率），**强制先验 A/B**。A/B 未成立前，C/D 优化全部暂停。
- 输出每条假设的「场景标签 + 匹配工具 + 验证先后」，交给 [[framework-一堂-关键假设-三板斧]] 做减法收敛。

---

## 常见坑

| 坑 | 症状 | 修复 |
|---|---|---|
| **成败/效率倒置** | 业务假设（A）还没成立，就在优化转化（D） | 先回到 A：业务能不能成？成立再谈 C/D |
| **与同名卡混用** | 用本工具给项目分级，或用 project-abcd 给假设分类 | 本工具只管「关键假设场景」；项目分级走 [[framework-yitang-project-abcd-classification]]；精益策略映射走 [[framework-lean-abcd-model]]；决策科学走 [[yt-decision-abcd-model]] |
| **标签空转** | 贴了 A/B/C/D 但不影响下一步 | 标签必须改变工具选择：成败→证伪实验，效率→公式下钻；否则分类无意义 |
| **宏观/微观硬切** | 纠结 B 决策到底宏观还是微观 | B 本就横跨宏观—微观，按当前决策主要层面归即可，不必精确切分 |
| **跳过第一刀** | 直接争 A 还是 C，没先分成败/效率 | 永远先问「不成立是整个倒还是只是更差」，再分宏观/微观 |
| **把目标当假设来分类** | 拿「今年做到 1000 万」来分类 | 那是结果不是假设；先改写成依赖的前提条件再分类 |

---

## 自检

- [ ] 每条假设都过了第一刀（成败/效率）再过第二刀（宏观/微观）
- [ ] 输出含 `场景 + 维度 + 匹配工具 + 验证先后`
- [ ] A/B 成败类排在 C/D 效率类之前验证
- [ ] 没有与 lean/decision/project 三张同名 ABCD 卡混用

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 上位框架 | [[framework-一堂-关键假设-ABCD模型]] | 本工具是其操作化 |
| 总纲 | [[framework-一堂-关键假设]] | 分类器服务于关键假设入口 |
| 下一步收敛 | [[framework-一堂-关键假设-三板斧]] | 分类后做减法与验证 |
| 下一步定量 | [[framework-一堂-业务公式拆解-总纲]] | 定位后落到 ABC/L1-L6 |
| 同名区分 | [[framework-lean-abcd-model]] / [[yt-decision-abcd-model]] / [[framework-yitang-project-abcd-classification]] | 三张同名 ABCD，含义不同 |
