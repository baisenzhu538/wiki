---
id: framework-wanghuan-bitcoe-prompt-framework
title: 王欢BITCOE提示词框架
type: framework
status: reviewed
domain:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-28'
author: 王语嫣
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
source_refs:
- src_unknown
- src_unknown
- src_unknown
related:
discoverable_by:
  - "王欢BITCOE提示词"
- '[[tool-wanghuan-ai-business-profile]]'
- '[[framework-wanghuan-ooda-loop]]'
- '[[framework-wanghuan-actor-director-mode]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[framework-ai-deconstruction-methodology]]'
- '[[framework-ai2041-critical-reading-os]]'
- '[[framework-wanghuan-three-tier-dev-architecture]]'
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- audience:ceo
- scene:diagnosis
- skill-level:intermediate
diagnostic_signals:
aliases:
  - 王欢BITCOE提示词框架
  - 王欢
  - 提示词
  - 提示词框架
aliases:
  - 王欢BITCOE提示词框架
  - 王欢
  - 提示词
- lens: 意图模糊
  follow_up: 用 BITCOE 六槽位逐条检查：背景、指令、任务、约束、输出、示例是否都已显式写出？
- lens: 约束缺失
  follow_up: Constraint 槽位是否写明了"不要做什么、不能碰什么、避免什么风格"？
- lens: 示例与格式缺位
  follow_up: Output 和 Example 槽位是否给出了可对照的格式样例和风格参考？
- lens: 上下文工程缺失
  follow_up: 高频任务是否已把稳定背景写进 [[tool-wanghuan-ai-business-profile]]，而非每次用 BITCOE 重复？
---

# 王欢BITCOE提示词框架

> **Burn line**: BITCOE 不是公式，是消灭模糊的思维习惯。
>
> **来源**：王欢 AI 实战分享（2026-06-18）  
> **原名差异**：图片中写为 BTICOE，笔记中写为 BTICME（M = Method），入 wiki 统一命名为 **BITCOE**。

---

## 用一句话讲清楚

BITCOE 是一个六槽位提示词框架，通过强制填写**背景、指令、任务、约束、输出、示例**，把"模糊需求"变成"AI 可精确执行、人可验收的指令"。

---

## 核心要点

### 1. 六槽位与各自消灭的模糊

```
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│  B  │ │  I  │ │  T  │ │  C  │ │  O  │ │  E  │
│背景 │ │指令 │ │任务 │ │约束 │ │输出 │ │示例 │
└─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘
```

| 槽位 | 英文 | 核心问题 | 消灭的模糊 |
|:---|:---|:---|:---|
| **B** | Background | 你是谁？处境是什么？ | AI 不知道上下文，只能给通用答案 |
| **I** | Instruction | 按什么逻辑做？ | AI 按默认逻辑执行，偏离你的方法 |
| **T** | Task | 这次做什么？ | AI 不知道具体产出目标 |
| **C** | Constraint | 不要做什么？红线是什么？ | AI 往错误方向走、碰不该碰的东西 |
| **O** | Output | 什么格式、多长、结构？ | AI 输出格式不稳定、无法直接使用 |
| **E** | Example | 什么风格、语气？ | AI 对"好"的理解与你不同 |

> **C（约束）是王欢标星的"最致命"槽位**——多数 AI 输出跑偏，不是因为任务没说清，而是因为约束没说清。

### 2. BITCOE 与传统 prompt 的区别

| 维度 | 传统 prompt | BITCOE |
|:---|:---|:---|
| 结构 | 自由文本 | 六槽位强制填空 |
| 重点 | 告诉 AI 做什么 | 同时告诉 AI 不要做什么 |
| 上下文 | 常被忽略 | 必填背景 |
| 输出控制 | 较弱 | 明确格式和示例 |
| 复用性 | 每次重新写 | 可固化为模板 |

### 3. 与 AI 业务档案的关系

BITCOE 负责"这次任务"，[[tool-wanghuan-ai-business-profile]] 负责"长期稳定的我"。两者组合使用效果更佳：

1. 先用 AI 业务档案注入"我是谁、我服务谁、我的输出标准"。
2. 再用 BITCOE 描述每次具体任务。

### 4. 案例支撑

王欢在课上对比了"丢了一个大客户，帮我分析原因"的三个版本：

- 待补充链接
- 待补充链接
- 待补充链接

这验证了 BITCOE 的核心价值：**不是让 AI 更聪明，而是逼你自己把模糊消灭干净**。

---

## 边界

| 适用 | 不适用 |
|:---|:---|
| 需要稳定、可复用输出的高频任务 | 一次性、临时、没有复用价值的问答 |
| 人已经想清楚"要什么"和"不要什么" | 人自己也没想清楚目标 |
| 需要团队协作、统一 prompt 标准 | 个人随意探索，不需要一致性 |
| 输出有明确格式、风格、质量红线 | 追求自由发散的创意探索 |
| 与 AI 业务档案配合，形成"长期角色 + 短期任务" | 没有长期协作需求，写档案成本过高 |
| 任务在 AI 当前能力边界内，可通过验收兜底 | 超出 AI 能力且无法验收的高风险任务 |

> **关键判断**：BITCOE 不能代替你思考，它只能把你已经想清楚的东西显式化。

---

## 失败模式 / 常见走偏

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **B 缺失** | AI 输出泛泛，像在对"平行宇宙里的你"说话 | 先写角色、业务场景、目标用户 |
| **I 缺失** | AI 按默认逻辑执行，不符合你的分析方法 | 明确思考路径、分析框架、优先顺序 |
| **T 缺失** | AI 不知道要产出什么，给出无关内容 | 用一句话写明本次具体目标 |
| **C 缺失** | 输出跑偏、包含不该有的内容、触犯红线 | 强制写"不要做什么、不能碰什么" |
| **O 缺失** | 格式不稳定，每次输出长度/结构不同 | 规定格式、长度、结构和交付物形态 |
| **E 缺失** | 风格不符合要求，"专业"理解不一致 | 提供参考样例，锁定语气和表达习惯 |
| **把格式当标准** | 只写"用表格输出"，没写质量红线 | 区分格式偏好与不可接受的内容错误 |
| **只写正面不写负面** | AI 不断加入你不想要的内容 | 每个槽位补一条"不要…"的否定约束 |

---

## 行动 Checklist

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接

---

## 相关卡 / 互链

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接

---

## Critique

**攻击者 1：提示词工程师 / 效率优先者**
> "每次写 prompt 都要填六个槽位，太慢了。日常问答用一句话就够了，BITCOE 过于繁琐。"
>
> **回应**：BITCOE 的目标不是让"随便聊聊"变复杂，而是让"重要且反复出现的任务"变稳定。对于高频、协作、质量敏感的任务，前期多花 2 分钟写约束，能节省后面几十分钟的反复调试。

**攻击者 2：建构主义学习理论（Piaget / Vygotsky）**
> "把提示词结构固定成六槽位，会限制探索式学习。很多问题是在与 AI 对话中逐步澄清的，提前写满六槽位反而可能把错误假设固化。"
>
> **回应**：BITCOE 适合"目标相对清晰、需要稳定输出"的任务；对于探索性、创造性、目标本身模糊的任务，应先用自由对话澄清，再用 BITCOE 固化。它不是万能公式，而是"消灭已知模糊"的工具。

**攻击者 3：组织行为学（Herbert Simon 有限理性）**
> "BITCOE 假设人能完整表达自己的目标和约束，但现实中人的认知有限，很多约束只有看到 AI 输出后才意识到。"
>
> **回应**：这正是 BITCOE 需要配合 [[framework-wanghuan-ooda-loop]] 迭代的原因。第一次写不完美是正常的，关键是用输出反推缺失的约束，把隐性的"不要"显性化。

**不要用**：
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接

---

## Synthesis

BITCOE 是王欢人机协作方法论中的"意图显式化"基础设施。它把一次 AI 协作中最重要的六类信息——背景、指令、任务、约束、输出、示例——强制结构化，从而把"模糊进、模糊出"的随机过程，变成"清晰进、可验收出"的可靠过程。它的最大价值不只在于让 AI 输出更好，更在于逼使用者在开口之前先把需求想明白：很多时候当你把 BITCOE 写完，答案已经清晰了一半。

在 KDO 知识工厂的工作流中，BITCOE 既是单张卡片生产的提示词模板，也是把个人隐性判断沉淀为团队可复用资产的桥梁。与 [[tool-wanghuan-ai-business-profile]] 搭配解决"长期角色"问题，与 [[framework-wanghuan-ooda-loop]] 搭配解决"持续迭代"问题，与 [[framework-wanghuan-actor-director-mode]] 搭配解决"人机分工"问题。它不能代替人的判断力，但能把判断力外化成 AI 可执行、可验收的标准。

---

*基于王欢 2026-06-18 AI 实战分享整理。原名 BTICOE/BTICME，入 wiki 统一为 BITCOE。*
