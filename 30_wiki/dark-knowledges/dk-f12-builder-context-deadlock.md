---
id: dk-f12-builder-context-deadlock
title: F-KDO-012：Builder 上下文过载死锁→Token 零跳动、Agent 卡死、无产出
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-012
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[yt-tool-peas-agent-analysis]]'
- '[[tool-agent-research-pipeline]]'
- '[[kdo-input-channel-strategy-2026-06-16]]'
- '[[kdo-protocol]]'
- '[[case-ai-agent-milestone-design]]'
- '[[tool-agent-crawl4ai]]'
- '[[agent-external-brain-design]]'
- '[[dk-demand-pitfall-travel-agent]]'
- '[[framework-kdo-self-attack]]'
- '[[kdo-yaml-frontmatter-safety]]'
- '[[kdo-priority-checklist]]'
- '[[tool-demand-agent-signal-substitute]]'
- '[[tool-Truman-多Agent通信协作方案]]'
- '[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]'
- '[[kdo_product_design_agent_final]]'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 入职规范（CLAUDE.md）要求读取 5+ 个规范文件，加上多任务上下文和被操作文件，总上下文消耗突破 50% 窗口，剩余空间不足以完成推理+输出
  follow_up_question: 立即停止当前 session，用 `/new` 重开；将原指令拆成单轮单任务，并删除对 PROTOCOL.md / 工业化手册
    / failure-modes.md 的引用
- signal: src_unknown
  framework_lens: LLM 进入过度分析循环：上下文窗口被规范和任务目标占满，无法有效生成输出，表现为 token 零跳动
  follow_up_question: 检查当前上下文消耗比例；若 >50%，强制 `/new` 接力，并在新 session 中只带一个子任务和必要的最小上下文
- signal: src_unknown
  framework_lens: 多轮累积导致上下文碎片化和规范文件重复加载， session 在最后一步被压垮
  follow_up_question: 将大任务按文件或按步骤切分，每个子任务用独立 session，通过文件系统传递中间结果
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown# F-KDO-012：Builder 上下文过载死锁→Token 零跳动、Agent 卡死、无产出
- audience:executor
- scene:reference
- skill-level:intermediate
---

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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **单轮单任务**：每条指令只包含 1 个明确目标，≤5 分钟可完成
2. **不引用规范文件**：纯执行指令不要引用 PROTOCOL.md、工业化手册、failure-modes.md 等大文件
3. **先 context 后任务**：如果必须读取规范文件，先在一个 session 中只读取并确认理解，然后 `/new` 开新 session 执行任务
4. **监控 token 消耗**：如果上下文已经消耗了 >50% 的窗口，立即停止当前任务，`/new` 后接力
5. **大任务拆分**：将复杂任务拆成多个子任务，每个子任务单独一个 session，通过文件系统传递中间结果

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| ✅ 适用 | 所有给 Builder Agent（特别是黄药师）分配任务的场景 |
| ❌ 不适用 | 老顽童（Producer）session：Producer 通常只处理单张卡片或单篇文章，不容易触发上下文过载 |
| 注意 | 不同 Agent 的上下文消耗特性不同：黄药师需要读取大量规范文件，最容易触发；洪七公处理视觉任务，上下文消耗模式不同 |
| 代价 | `/new` 接力的代价是会话间上下文丢失——需要在文件中保存足够的中间状态 |
| 例外 | 如果任务本身就必须读取大量文件（如全库 lint），应考虑在脚本层处理而非 Agent 层处理 |

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| 多任务过载 | 单条指令含 ≥3 个文件操作目标，Agent 执行 >20 分钟无产出 | 拆分为单轮单任务，每条指令只含 1 个目标 |
| 规范文件叠加 | 指令引用 ≥2 个规范/手册文件，token 数快速上涨后停滞 | 删除规范引用，纯执行；如需理解规范，先开独立 session |
| 上下文窗口突破 | token 消耗 >50% 后进入零跳动/卡死 | 立即 `/new`，在新 session 中只带最小必要上下文 |
| 过度分析循环 | Agent 反复重读文件、重写计划、不落地修改 | 明确输出物和完成标准；必要时用 `/new` 重置上下文 |
| 接力状态丢失 | `/new` 后新 session 不记得上一步结论，重复劳动 | 在上一个 session 结束时把中间结果写入文件，新 session 先读文件 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
