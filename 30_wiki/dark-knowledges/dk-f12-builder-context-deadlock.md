---
id: dk-f12-builder-context-deadlock
title: F-KDO-012：Builder 上下文过载死锁→Token 零跳动、Agent 卡死、无产出
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-012
source_refs:
- 90_control/failure-modes.md#F-KDO-012
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[dk-c6-large-source-overflow]]'
- '[[master-first-principles]]'
- '[[kdo-flywheel]]'
- '[[master-systems-thinking]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: "给黄药师单条指令包含 ≥3 个独立文件操作目标，或引用 ≥2 个规范文件后，Agent 进入 'Caramelizing…' 状态超过 20 分钟"
  framework_lens: "入职规范（CLAUDE.md）要求读取 5+ 个规范文件，加上多任务上下文和被操作文件，总上下文消耗突破 50% 窗口，剩余空间不足以完成推理+输出"
  follow_up_question: "立即停止当前 session，用 `/new` 重开；将原指令拆成单轮单任务，并删除对 PROTOCOL.md / 工业化手册 / failure-modes.md 的引用"
- signal: "Agent 执行过程中 token 计数长时间停留在同一数字，同时没有任何文件变更或输出"
  framework_lens: "LLM 进入过度分析循环：上下文窗口被规范和任务目标占满，无法有效生成输出，表现为 token 零跳动"
  follow_up_question: "检查当前上下文消耗比例；若 >50%，强制 `/new` 接力，并在新 session 中只带一个子任务和必要的最小上下文"
- signal: "Sprint 迭代中 Builder 连续处理 lint/设计审查/多文件修改后，产出突然中断"
  framework_lens: "多轮累积导致上下文碎片化和规范文件重复加载， session 在最后一步被压垮"
  follow_up_question: "将大任务按文件或按步骤切分，每个子任务用独立 session，通过文件系统传递中间结果"
tags:
- '#source_type/error'
- '#domain/master'
- '#agent/builder'
- '#context-window'
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

## 深度洞察

- **这不是 LLM "变慢"，而是上下文窗口硬约束被突破后的结构性失能**：规范文件 + 多任务 + 被操作文件叠加后，留给推理和生成的 token 空间不足，Agent 被迫在过度分析中循环。
- **静默卡死比报错更危险**：没有 error 日志，唯一的信号是 token 数不跳动、时间拉长——在批量或异步执行时极易被误判为"还在跑"。
- **根因在任务分配者，不在 Agent**：黄药师的入职规范要求读取大量文件是固定成本，任务设计者如果同时塞入多个目标，等于在已知瓶颈上继续加压。
- **`/new` 不是失败，而是协议的一部分**：把大任务拆成多个 session 是 KDO 多 Agent 工作流中管理上下文的基本操作，不是绕路或补救。

## 使用场景

- 你给黄药师（或其他 Builder Agent）分配任务时，忍不住一次性列出多个操作目标
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

| 边界 | 说明 |
|:-----|:------|
| ✅ 适用 | 所有给 Builder Agent（特别是黄药师）分配任务的场景 |
| ❌ 不适用 | 老顽童（Producer）session：Producer 通常只处理单张卡片或单篇文章，不容易触发上下文过载 |
| 注意 | 不同 Agent 的上下文消耗特性不同：黄药师需要读取大量规范文件，最容易触发；洪七公处理视觉任务，上下文消耗模式不同 |
| 代价 | `/new` 接力的代价是会话间上下文丢失——需要在文件中保存足够的中间状态 |
| 例外 | 如果任务本身就必须读取大量文件（如全库 lint），应考虑在脚本层处理而非 Agent 层处理 |

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| 多任务过载 | 单条指令含 ≥3 个文件操作目标，Agent 执行 >20 分钟无产出 | 拆分为单轮单任务，每条指令只含 1 个目标 |
| 规范文件叠加 | 指令引用 ≥2 个规范/手册文件，token 数快速上涨后停滞 | 删除规范引用，纯执行；如需理解规范，先开独立 session |
| 上下文窗口突破 | token 消耗 >50% 后进入零跳动/卡死 | 立即 `/new`，在新 session 中只带最小必要上下文 |
| 过度分析循环 | Agent 反复重读文件、重写计划、不落地修改 | 明确输出物和完成标准；必要时用 `/new` 重置上下文 |
| 接力状态丢失 | `/new` 后新 session 不记得上一步结论，重复劳动 | 在上一个 session 结束时把中间结果写入文件，新 session 先读文件 |

## 为什么值钱

- 这是 KDO 多 Agent 协作中特有的上下文管理问题：**不是技术限制，而是协作协议设计问题**
- "卡死"的直接表现是 token 零跳动，但根因是"任务设计不合理"——给用户（任务分配者）的教训比给 Agent 的教训更重要
- 揭示了 LLM Agent 工作流设计中的一个核心约束：**上下文窗口是硬约束，不能绕，只能分**
- 任何 AI 训练语料中都不会有"给 KDO 的 Builder 每次只能发 1 个任务、不能引用规范文件"这条知识

## 与其他知识的关联

- [[dk-c6-large-source-overflow]] — 同一模式：上下文容量过载。C-6 是"大源文件导致 session 装不下"，F-KDO-012 是"多任务+多规范文件导致 session 装不下"——两者都是"上下文窗口硬约束被突破"
- [[master-first-principles]] — 第一性原理：LLM context window 是物理硬约束，不能绕，只能分。F-KDO-012 是"在任务分配层面尊重硬约束"的具体实践
- [[kdo-flywheel]] — 知识飞轮运转依赖多 Agent 接力，F-KDO-012 定义了 Builder Agent 接力的上下文边界条件
- [[master-systems-thinking]] — 系统思维中的"涌现性"原则：单独看每个任务都不大，但任务+规范+文件的组合会涌现出"卡死"这一意外行为
- `90_control/failure-modes.md` → F-KDO-012（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #7（不准给黄药师一次性派发 ≥3 个独立任务或引用 ≥2 个规范文件）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
