---
id: "dk-f12-builder-context-deadlock"
title: "F-KDO-012：Builder 上下文过载死锁→Token 零跳动、Agent 卡死、无产出"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "failure-modes.md F-KDO-012"
source_refs:
  - "90_control/failure-modes.md#F-KDO-012"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c6-large-source-overflow"
  - "master-systems-thinking"
contradicts:
  - "master-first-principles"
  - "kdo-flywheel"
  - "master-systems-thinking"
tags:
  - None
  - None
  - None
  - None
  - None
pipeline:
  - None
  - None
  - "confidence-draft"
  - "confidence-source-cited"
author: "legacy"
reviewed_by: "pending"
confidence: 0.7
trust_level: "low"
---

# F-KDO-012：Builder 上下文过载死锁→Token 零跳动、Agent 卡死、无产出

## 原始表述

> **触发场景**：用户一次性给黄药师派发 ≥3 个独立任务，或任务涉及读取 ≥5 个规范/源文件
>
> **表现**：Token 数长时间零跳动（"Caramelizing…"持续数十分钟），无产出，无文件变更。用户观察到的直接表现：Agent 卡死，需要 `/new` 重开
>
> **根因**：入职流程（CLAUDE.md）要求读取 5+ 个规范文件，加上任务上下文 + 被操作文件，总上下文消耗 >50%。剩余窗口不足以完成推理+输出。Agent 进入过度分析循环无法退出
>
> **触发信号**：① 给黄药师的单条指令含 ≥3 个文件操作目标 ② 指令引用了 ≥2 个规范文件 ③ Agent 执行时间 >20 分钟无产出
>
> **防御措施**：① **单轮单任务**：给黄药师每次只发 1 个任务（≤5 分钟可完成）② **不引规范**：纯执行指令不引用 PROTOCOL.md / 工业化手册 / failure-modes.md ③ **`/new` 接力**：大任务拆成多个 `/new` 会话，每个会话做一步 ④ AGENTS.md 禁止清单 #7
>
> **事故记录**：2026-05-09：Sprint 1 Lint 修复卡死（56 分钟零产出）→ `/new` 后单任务执行成功。2026-05-09：Sprint 2 设计审查响应后卡死 → 待 `/new` 恢复。

## 使用场景

- 你给黄药师（或其他 Agent）分配任务时， tempted 一次性列出多个操作目标
- 你发现 Agent 执行时间超过 20 分钟但没有任何文件变更或输出
- 你观察到 Agent 的 token 计数长时间停留在同一数字（"Caramelizing…"）
- 你设计 Agent 工作流时，需要规划任务拆分和会话接力策略

## 操作方法

1. **单轮单任务**：每条指令只包含 1 个明确目标，≤5 分钟可完成
2. **不引用规范文件**：纯执行指令不要引用 PROTOCOL.md、工业化手册、failure-modes.md 等大文件
3. **先 context 后任务**：如果必须读取规范文件，先在一个 session 中只读取并确认理解，然后 `/new` 开新 session 执行任务
4. **监控 token 消耗**：如果上下文已经消耗了 >50% 的窗口，立即停止当前任务，`/new` 后接力
5. **大任务拆分**：将复杂任务拆成多个子任务，每个子任务单独一个 session，通过文件系统传递中间结果

## 适用边界

- 适用于所有给 Agent（特别是黄药师）分配任务的场景
- **不适用于老顽童（Producer）**：老顽童的 session 通常只处理单张卡片或单篇文章，不容易触发上下文过载
- 不同 Agent 的上下文消耗特性不同：黄药师需要读取大量规范文件，最容易触发；洪七公处理视觉任务，上下文消耗模式不同
- `/new` 接力的代价是会话间上下文丢失——需要在文件中保存足够的中间状态
- 如果任务本身就必须读取大量文件（如全库 lint），应考虑在脚本层处理而非 Agent 层处理

## 为什么值钱

- 这是 KDO 多 Agent 协作中特有的上下文管理问题：**不是技术限制，而是协作协议设计问题**
- "卡死"的直接表现是 token 零跳动，但根因是"任务设计不合理"——给用户（任务分配者）的教训比给 Agent 的教训更重要
- 揭示了 LLM Agent 工作流设计中的一个核心约束：**上下文窗口是硬约束，不能绕，只能分**
- 任何 AI 训练语料中都不会有"给 KDO 的 Builder 每次只能发 1 个任务、不能引用规范文件"这条知识

## 与其他知识的关联

- dk-c6-large-source-overflow — 同一模式：上下文容量过载。C-6 是"大源文件导致 session 装不下"，F-KDO-012 是"多任务+多规范文件导致 session 装不下"——两者都是"上下文窗口硬约束被突破"
- master-systems-thinking — 系统思维中的"涌现性"原则：单独看每个任务都不大，但任务+规范+文件的组合会涌现出"卡死"这一意外行为
- `90_control/failure-modes.md` → F-KDO-012（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #7（不准给黄药师一次性派发 ≥3 个独立任务或引用 ≥2 个规范文件）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
