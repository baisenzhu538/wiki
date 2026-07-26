---
id: framework-一堂-关键假设-ABCD模型
title: 一堂关键假设 ABCD 模型（YitangABCDStrategyModel）：四场景 × 成败/效率定位器
type: framework
status: pending_review
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-09
updated_at: 2026-07-13
domain:
- yitang
- key-assumptions
source_refs:
- 00_inbox/一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt
- 00_inbox/一堂-关键假设课-truman-口述.txt L364-L402,L1064-L1074
related:
- '[[framework-一堂-关键假设]]'
- '[[tool-一堂-关键假设-ABCD场景分类器]]'
- '[[framework-一堂-关键假设-三板斧]]'
- '[[framework-一堂-业务公式拆解-总纲]]'
- '[[framework-lean-abcd-model]]'
- '[[yt-decision-abcd-model]]'
- '[[framework-yitang-project-abcd-classification]]'
- '[[concept-一堂-key-assumptions]]'
- '[[yt-business-formula-hypothesis-management-playbook]]'
- '[[case-yitang-shipinhao-ads-l1-l6]]'
- '[[yt-business-formula-abc-model]]'
- '[[yt-business-formula-ten-paradigms]]'
- '[[business-formula-domain-digest]]'
- '[[conversion-rate-domain-digest]]'
- '[[framework-business-formula-dual-triangle-bridge]]'
- '[[framework-business-formula-fundamentals-bridge]]'
- '[[framework-business-formula-y-model-bridge]]'
- '[[dk-yitang-business-formula-cd-loop-undo-key]]'
diagnostic_signals:
- signal: 团队说"我们有个关键假设"，但说不清它属于哪类问题
  lens: 缺场景定位——成败问题和效率问题要用不同工具
  follow-up: 先问"这是能不能成（成败），还是能不能更好（效率）？"再归到 A/B/C/D
- signal: 把"增长怎么做更好"当成"业务能不能成"在争论
  lens: C/D 效率问题被误当 A 成败问题
  follow-up: 先确认业务假设已成立，再谈增长/转化优化，别用效率工具解决成败问题
quality_labels:
- principle
- framework
- cited - framework-yitang-thought-liberation-lightning
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---

# 一堂关键假设 ABCD 模型（YitangABCDStrategyModel）

> **一句话**：关键假设 ABCD 模型是「场景定位器」——把一个关键假设先按**成败问题（能不能成）/ 效率问题（能不能更好）**分两行，再按**宏观—微观**分列，落到 **A 商业 / B 决策 / C 增长 / D 转化** 四个场景之一；不同场景匹配不同的验证工具与决策策略。来源：`一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt`（YitangABCDStrategyModel）。

---

## 一、模型结构

OCR 原文（极简）：

```
成败问题
  A. 商业场景     B. 决策场景
        宏观  —  微观
  C. 增长场景     D. 转化场景
效率问题
```

读作一个二维定位器：

|  | **宏观（方向/全局）** | **宏观—微观（决策点）** | **微观（动作/节点）** |
|---|---|---|---|
| **成败问题（能不能成）** | **A 商业场景** | **B 决策场景** | — |
| **效率问题（能不能更好）** | — | **C 增长场景** | **D 转化场景** |

> 说明：OCR 中 B 决策场景旁标注「宏观—微观」，表示决策场景横跨方向层到动作层（一个关键决策可能既有方向性也有动作性）；A 偏宏观成败，C/D 偏效率，D 最微观（具体转化节点）。这是课程图的视觉表达，按图还原，不与下方「同名卡区分」冲突。

---

## 二、四场景定义与匹配工具

| 场景 | 维度 | 核心问题 | 典型关键假设 | 优先匹配工具/卡 |
|---|---|---|---|---|
| **A 商业场景** | 成败·宏观 | 这个业务/赛道本身成不成？ | 「这个人群愿意为 X 付费」「单元模型能跑通」 | [[framework-一堂五步法]]、[[concept-一堂-business-prediction]]、[[framework-一堂-关键假设-三板斧]] |
| **B 决策场景** | 成败·宏观—微观 | 这个关键决策点成不成？ | 「投产比 ROI 能为正」「这个定价用户接受」 | [[tool-key-assumptions-check]]、[[framework-一堂-业务公式拆解-总纲]]（L5 定量做 ROI） |
| **C 增长场景** | 效率 | 能不能规模化、更好？ | 「获客成本能随规模下降」「留存能支撑复购」 | [[yt-business-formula-ten-paradigms]]、[[framework-一堂五步法]]（Step 5 增长） |
| **D 转化场景** | 效率·微观 | 这个关键转化节点能不能更高？ | 「详情页→下单转化能到 X%」「试听到付费能到 Y%」 | [[yt-business-formula-six-level-logic]]（L4 漏斗）、业务公式 L4 拆转化 |

**两条铁律**：

1. **先成败后效率**：A/B（成败）没验证成立，禁止跳到 C/D（效率）优化——在错误的业务上提高转化，只是把损失放大。
2. **场景决定工具**：成败问题用五步法/三板斧/证伪实验，效率问题用业务公式 L4-L6/漏斗优化。用效率工具（优化转化）去解决成败问题（业务根本不成立），是最常见的错配。

---

## 三、与同名 ABCD 卡的显式区分（防误用）

wiki 中另有 3 张含「ABCD」的卡，含义与本卡**不同**，不可混用：

| 卡 | 域 | ABCD 含义 | 与本卡关系 |
|---|---|---|---|
| **本卡** `framework-一堂-关键假设-ABCD模型` | yitang·关键假设 | A 商业/B 决策/C 增长/D 转化（场景分类视角，YitangABCDStrategyModel） | — |
| [[framework-lean-abcd-model]] | strategy·精益创业 | A 商业成败（→五步法）/B 关键决策（→ROI）/C 业务提升（→业务公式）/D 关键转化（→动力阻力触点）；宏观/微观×成败/效率矩阵 | **最相似但来源不同**：精益创业 OCR，策略映射更细；本卡源自关键假设课，定位更轻。两卡互链，处理同一二维的不同侧重 |
| [[yt-decision-abcd-model]] | yitang·决策科学 | 与 Y 模型/五步法/业务公式并列为「假设思维四套操作系统之一」 | 决策科学视角，391 行大卡；本卡是入口层的轻量场景定位，不替代 |
| [[framework-yitang-project-abcd-classification]] | yitang·管项目 | A 口头/B 简单/C 跨部门/D 战略 = **项目复杂度分级** | **完全不同的 ABCD**：那是项目管理复杂度，不是关键假设场景。仅名字相似 |

> 调用规则：用户问「我的关键假设属于哪类」→ 用本卡；问「项目该用多重流程管」→ 走 project-abcd；问「精益创业的宏观/微观验证策略」→ 走 lean-abcd；问「决策科学里 ABCD 与 Y 模型关系」→ 走 yt-decision-abcd。

---

## 四、案例演示：一个业务问题走四场景 + 顺序闸门

> 口径：以下数字为**假设演示 / 课程经验值**，仅演示分类逻辑，不作事实断言。

**问题**：「我的在线课程完课率只有 30%，怎么提升？」

- **第一刀（成败 / 效率）**：业务已成立、有付费用户，只是完课率低——这是**效率问题**（能不能更好），不是成败问题 → 进 C/D。
- **第二刀（宏观 / 微观）**：完课率是一个具体转化节点（开课 → 完课），偏微观动作 → 落 **D 转化场景**。
- **输出标签**：`D 效率·微观`。
- **匹配工具与路径**：用 [[yt-business-formula-six-level-logic]] L4 拆漏斗（开课 → 看 1 节 → 看 5 节 → 完课），定位断点（如「看 1 节 → 看 5 节」流失最大）针对优化；可执行 5 步见 [[tool-一堂-关键假设-ABCD场景分类器]]。

**顺序闸门（反例）**：若同一团队同时在吵「这课程方向根本没人需要」（A 商业场景·成败），必须**先验 A 再谈 D**。方向没成立时优化完课率，只是把错误业务的损失放大——把 D 当 A 解决，是最常见错配（见 Failure Modes「成败 / 效率倒置」）。

**同名卡边界演示**：同样是「完课率」，若有人问「这门课项目该用多重流程管」→ 那是 [[framework-yitang-project-abcd-classification]]（复杂度分级），不是本卡 D 场景；别拿 D 转化去给项目分级。

---

## 五、与三板斧、业务公式的衔接

- **定位是收敛的前提**：用 [[framework-一堂-关键假设-三板斧]] 做减法前，先用本卡给每条假设标场景——成败类假设优先于效率类假设被验证。
- **定位是定量化的入口**：A/B 成败类假设落到 [[framework-一堂-业务公式拆解-总纲]] 的 A 目标/B 参数；C/D 效率类假设落到 L4 漏斗与十大范式（[[yt-business-formula-ten-paradigms]]）。
- **操作化**：把业务问题分到四场景、并标成败/效率的可执行步骤，见 [[tool-一堂-关键假设-ABCD场景分类器]]。

---

## When NOT to Use

- **已经清楚问题类型**：若已明确是「转化优化」（D），直接用业务公式 L4，不必再走一遍 ABCD 分类。
- **从 0 到 1 新品类**：四场景基于已知商业结构，新品类可能四场景都不完全适用，先用设计思维。
- **拿它当项目复杂度分级**：那是 [[framework-yitang-project-abcd-classification]] 的用途，本卡不管项目流程轻重。

## Failure Modes

| 失败模式 | 症状 | 修复 |
|---|---|---|
| **成败/效率倒置** | 业务假设未成立就在优化转化（D） | 先回到 A：业务能不能成？成立再谈 C/D |
| **与同名卡混用** | 用本卡去给项目分级，或用 project-abcd 给假设分类 | 按第三节调用规则选卡 |
| **场景标签空转** | 给每条假设贴了 A/B/C/D 但不影响下一步 | 标签必须改变工具选择：成败→证伪实验，效率→公式下钻 |
| **宏观/微观硬切** | 纠结 B 决策到底宏观还是微观 | B 本就横跨宏观—微观，按当前决策的主要层面归类即可 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---|---|---|
| 拿到一条关键假设，不知用何工具 | 先判成败/效率，再归 A/B/C/D | 每条假设有场景标签 + 匹配工具 |
| 团队在「增长」和「能不能成」之间扯皮 | 喊停：先确认 A 商业场景是否成立 | 共识回到成败问题 |
| 要把定性假设变可验证 | A/B 走证伪实验，C/D 走业务公式 L4-L6 | 每条假设有验证路径 |

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 总纲 | [[framework-一堂-关键假设]] | 本卡是其「场景」柱 |
| 操作化 | [[tool-一堂-关键假设-ABCD场景分类器]] | 把问题分到四场景的可执行步骤 |
| 收敛 | [[framework-一堂-关键假设-三板斧]] | 定位后用三板斧做减法与验证 |
| 贯通 | [[framework-一堂-业务公式拆解-总纲]] | 定位后落到 ABC/L1-L6 定量化 |
| 同名·精益 | [[framework-lean-abcd-model]] | 精益创业视角的 ABCD，策略映射更细 |
| 同名·决策 | [[yt-decision-abcd-model]] | 决策科学视角，与 Y 模型并列 |
| 同名·项目 | [[framework-yitang-project-abcd-classification]] | 项目复杂度 A/B/C/D，含义不同 |

> 核心心法：**先问「能不能成」，再问「能不能更好」。** 成败问题用证伪，效率问题用下钻；用错工具，越努力错得越远。
