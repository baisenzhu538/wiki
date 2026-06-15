---
id: case-truman-ai-skill-engineering-guide
title: 案例：Truman 如何用 3 小时做出高阶 AI Skill 工程指南
type: case
source_refs:
- src_20260614_8269ccdb
status: draft
domain:
- yitang
- ai-collaboration
- skill-engineering
source_person: Truman
source_context: 一堂高阶建模能力培训（AI 建模协作案例） （单一 source 为完整长文档，内容充分支撑 high trust）
created_at: '2026-06-14'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
review_date: '2026-06-14'
trust_level: high
confidence: 0.85
related:
- '[[tool-ai-skill-engineering-method]]'
- '[[dk-modeling-ai-iterative-prompting]]'
- '[[dk-modeling-ai-cross-validation]]'
- '[[dk-modeling-ai-self-retrospection]]'
tags:
- '#modeling'
- '#case'
- '#ai-skill'
- '#skill-engineering'
- '#ai-collaboration'
---
# 案例：Truman 如何用 3 小时做出高阶 AI Skill 工程指南

> **Burn line**: 不是让 AI 随便写个 Skill，而是用工程指南把 AI 的输出质量锁死在你的审美上限。

这是 Truman 在课程中分享的一个完整案例：他为了封装一堂内部高质量的 Skill，发现市面上（包括官方）的 Skill 创作指南都不够好，于是自己动手，用 3 小时做出了一份“高阶 Skill 工程指南”，并且后续拿它去审计和封装其他 Skill，显著提升了稳定性。

---

## Background

- **场景**：一堂内部需要大量封装高质量 AI Skill
- **问题**：市面上的 Skill 创作指南不够完备，AI 生成的 Skill 质量不稳定、故障率高
- **建模目标**：做出一份足够完备的工程指南，既能指导 AI 生成 Skill，又能作为审计标准
- **来源**：`src_20260614_8269ccdb#2406-2586`

---

## What Happened

Truman 在春节期间花 3 个小时，完成了一份高阶 Skill 工程指南。整个过程分为 6 个阶段：

### 阶段 1：找最佳实践

- 先问 AI 目前市场上有哪些 Skill 创作最佳实践
- 找到官方 Skill Creator（英文）和云巨米官方封装的十几个 Skill

### 阶段 2：翻译 + 解读

- 用两个 AI 同时工作：一个负责翻译，一个负责专业解读
- 把英文指南翻译成中文，并解释每段的含义和价值

### 阶段 3：合并生成 1.0

- 让 AI 把所有技巧和策略做一次大合集
- 加上 Truman 对建模的美好想象，生成“高阶 Skill 设计指南 1.0”

### 阶段 4：十几轮“喷”式迭代

- Truman 发挥逻辑洁癖，不断挑毛病：
  - 架构不完整
  - 模块有遗漏（要求 MECE）
  - 逻辑不严谨
  - 没有逻辑链
  - 优先级没排
- 连续迭代 10–15 轮，直到改不动为止

### 阶段 5：交叉验证

- 找两个外部标杆对照：
  - 云巨米官方行业指南
  - 花总春节写的基本功与 Skill 指南
- 从实用性、宽度、专业性三个维度打分
- 结果：官方 B+，花总 A，Truman 自己的 S
- 再让 AI 吸收两个外部标杆的优点，又改一轮

### 阶段 6：落地应用

- 用这份指南封装多个单元模型 Skill
- 用指南做审计，让 AI 自查新 Skill 的问题
- 发现多个 P0 级问题（如触发条件没写完整、示例模板丢失）

---

## 关键证据

- **证据 1 [conf=0.9]**：Truman 明确说整个过程只花了 3 小时，但产出显著超过两个外部标杆。——来源：`src_20260614_8269ccdb#2530-2536`。
- **证据 2 [conf=0.85]**：1.0 之后的核心工作不是生成，而是“喷”——连续 10–15 轮挑错、补遗漏、排优先级。——来源：`src_20260614_8269ccdb#2466-2516`。
- **证据 3 [conf=0.85]**：最终输出包含 7 个复杂度范式、P0/P1/P2 资源库、To Do List 十条、Not To Do List 十条。——来源：`src_20260614_8269ccdb#2498-2516`。
- **证据 4 [conf=0.8]**：用工程指南审计 Leo 的 Skill，发现多个 P0 级问题。——来源：`src_20260614_8269ccdb#2558-2566`。

---

## 可迁移场景

| 场景 | 如何用这个方法 |
|---|---|
| 封装 Prompt/Agent/Skill | 先找最佳实践，再翻译解读，再合并生成，再迭代审计 |
| 建立团队 AI 输出标准 | 把个人审美固化成工程指南，让 AI 按指南自查 |
| 快速产出高质量文档 | 用 AI 生成 1.0，再用逻辑洁癖迭代到上限 |
| 评估外部 AI 资产 | 拿工程指南当评分卡，量化评估质量 |

---

## 教训

- **不要直接让 AI 随机发挥**：没有指南约束，AI 会遗漏关键要素。
- **迭代比生成重要**：1.0 很快，但价值来自后面的 10–15 轮挑错。
- **要拿外部标杆撞自己**：避免自我陶醉，交叉验证才能接近真实质量。
- **工程指南必须可执行**：To Do / Not To Do 要具体、有优先级、能审计。

---

## 失败模式

| 失败模式 | 表现 | 避免方法 |
|---|---|---|
| **直接让 AI 一次成型** | 生成看似完整但漏洞百出 | 先生成 1.0，再系统挑错 |
| **缺少外部验证** | 自我感觉良好，实际不及行业标准 | 找 2–3 个标杆交叉打分 |
| **指南不可审计** | 写成原则性描述，没法检查 | 输出 To Do/Not To Do + P0/P1/P2 |
| **没有应用到后续工作** | 指南写完就存档 | 每次封装新 Skill 都让 AI 先自查 |

---

## Sources

- `src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md:2406-2586`

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）*
