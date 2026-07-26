---
id: framework-yihang-knowledge-data-decoupling
title: 知识层与数据层解耦：核心词 + data pack 插件式组合
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-05
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-05
updated_at: 2026-07-05
domain:
- ai-collaboration
- yitang
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[tool-aesthetic-library-builder]]'
- '[[method-dual-triangle-flywheel-engine]]'
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---

# 知识层与数据层解耦：核心词 + data pack 插件式组合

> **一句话定义**：Truman 在 YAI 架构设计中将系统核心词（审美+体系）与 data pack（数据+场景+基本功）分开生产、插件式组合——核心词稳定变化慢，data pack 需要频繁更新。这是双三角人类三角和 AI 三角在 Agent 架构层的直接落地。

---

## 一、解耦模型

```
系统核心词层（审美+体系）      ← 人类三角，稳定、变化慢
    +
data pack 层（数据+场景+基本功） ← AI 三角，随场景更新
    ↓ 插件式组合
完整 Agent prompt
```

**核心词**：Agent 的"操作系统"——定义了它如何判断好坏（审美）、如何拆解任务（体系）。这部分是长期积累的，不随具体任务变化。

**data pack**：Agent 的"应用程序"——每个 data pack 对应一类具体场景的知识包。需要频繁更新（新案例、新数据、新场景），挂载到核心词上即可运行。

---

## 二、为什么解耦

Truman 的口述稿 L5025-5078 解释了关键动机：

| 不分开放一起 | 分开后的效果 |
|:---|:---|
| 每次更新数据都要重写整个 prompt | 只更新对应的 data pack，核心词不动 |
| prompt 越来越长、越来越乱 | 按需挂载——需要什么场景就挂什么 data pack |
| 改一个参数影响全局 | 每个 data pack 独立维护、独立测试 |
| Agent 不能快速适配新场景 | partner 聊宏观不行→挂人生观 data pack；聊单元模型不行→挂单元模型 data pack |

核心洞察：**把不变的判断力（审美+体系）和频繁变化的知识数据（场景+数据+基本功）放在一起，是 Agent prompt 越来越臃肿且难以维护的根本原因。**

---

## 三、操作步骤

| 步骤 | 动作 | 产出 |
|:---|:---|:---|
| 1 | 识别 Agent 需要哪些"不变的核心判断"——审美标准和体系框架 | 核心词文档 |
| 2 | 识别哪些知识需要随场景/用户/数据变化 | 待拆分的 data pack 清单 |
| 3 | 每个 data pack 按主题独立生产——像建审美库一样建 data pack | 独立 data pack 文件 |
| 4 | 建立 data pack 的挂载/更新机制——Agent 启动时按需组合 | 挂载规则 |
| 5 | 组合编译成最终 prompt → 测试 → 迭代 data pack | 可运行的 Agent prompt |

---

## 四、对 KDO Agent 设计的启示

- **KDO 的 card = data pack 的原材料**。每张卡编译后就是一个最小数据包——方法论卡提供体系、案例卡提供数据、工具卡提供操作步骤
- **Agent 不应该是巨大 system prompt**——应该是核心词 + 按需挂载的 data pack
- **直接对接** #59（Prompt 编译器——把核心词+data pack 编译为可注入 prompt）和 #73（Agent 执行模式——按任务类型挂载不同 data pack）

---

## 五、与双三角的关系

| 双三角要素 | 在解耦模型中的位置 | 更新频率 |
|:---|:---|:---|
| **审美** | 核心词 | 低——审美标准是长期沉淀的 |
| **体系** | 核心词 | 低——方法框架相对稳定 |
| **场景** | data pack | 高——不同场景需要不同数据 |
| **数据** | data pack | 高——新案例、新数据持续产生 |
| **基本功** | data pack | 中——新工具/新 Feature 出现时需要更新 |

---

## 六、Critique

**[Monolithic Advocate]**
> "核心词+data pack 的架构增加了复杂度。一个大而全的 system prompt 虽然不好维护，但至少不会出现挂载错误的 data pack 导致 Agent 行为异常。"

**回应**：大而全的 prompt 在 Agent 数量少、场景单一时确实更简单。但当你有 10 个 Agent、每个需要适配 5 种场景时，不分层的维护成本是指数级的。解耦是有成本的——只有当你确实有多个 Agent 或多个场景需要管理时，这个成本才值得付。

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| Agent prompt 超过 2000 字且每次改一小段都要重新测试 | 拆——哪些是核心词（永远不变）？哪些是 data pack（随任务变）？ |
