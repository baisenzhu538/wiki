---
id: dk-p13-long-session-token-blackhole
title: "P-13：长会话 = token黑洞 — 一晚上烧掉80元"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-13"
source_refs:
  - .agent/pitfalls.md#P-13
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p14-zombie-process-burn-money
  - master-systems-thinking
---

# P-13：长会话 = token黑洞 — 一晚上烧掉80元

## 原始表述

> **症状**：黄药师从晚上开始跑 Dogfood → Sprint 2 → Sprint 3 → Sprint 4，一个会话跑到上下文爆掉再续第二个会话。共 ~100轮+，DeepSeek 账单 ~80元。单晚消耗超过过去10天总和。
>
> **根因（三重叠加）**：
> 1. 每轮重发全量上下文 — 后期每轮 input 100-150k tokens，其中 90% 是历史对话和工具结果
> 2. CLAUDE.md 很大 — 每轮携带 ~4000 tokens 系统提示
> 3. 缓存 TTL 5分钟 — 超时后下一轮全量重新计费
>
> **反算**：总输入 ~14M tokens，缓存未命中 ~5.6M（占费用 80%）。
>
> **对策**：
> - **一个 Sprint 开一个会话** — 完成即 /new，通过 `.agent/context.md` 接力
> - 不要一口气跑 100轮——拆成 5个短会话，总 token 量降 70%+
> - CLAUDE.md 已精简（290→101行），CLI 速查移出到 `90_control/cli-reference.md`
> - 需要批量脚本任务的，写好脚本让用户本地跑，不用我一轮轮验证

## 使用场景

- 你的会话已经跑了很多轮（>50 轮），需要判断是否该结束当前会话开新的
- 你发现 API 账单意外高昂，需要排查是否是长会话导致的 token 浪费
- 你在规划一个大任务时，需要决定是放在一个会话还是拆成多个
- 你在设计 Agent 工作流时，需要考虑 token 效率和成本

## 操作方法

1. **设定轮数上限**：每个会话不超过 20 轮，超过后立即 `/new` 开新会话
2. **一个 Sprint 一个会话**：每个独立的 Sprint 或子任务单独一个会话，通过 `.agent/context.md` 传递状态
3. **监控账单**：每天/每周检查 API 账单，如果发现异常增长，立即排查会话长度
4. **减少上下文重复**：删陡对当前任务不必要的历史对话记录，减少每轮的 input tokens
5. **批量任务本地化**：需要大量计算或验证的任务，写成脚本让用户本地跑，而非通过 AI 一轮轮执行

## 适用边界

- 适用于所有使用按 token 计费的 LLM API 的场景
- 不适用于固定价格或本地部署的模型（如本地 llama.cpp）——这些没有 token 费用问题
- 缓存 TTL 是一个关键参数：如果你的提供商缓存 TTL 很短（如 5 分钟），长会话的成本惩罚更严重
- 系统提示（CLAUDE.md）的大小直接影响每轮的基础费用——精简系统提示是降低成本的有效手段
- 尽管会话分裂可以降低 token 消耗，但每次 `/new` 都会丢失上下文——需要在文件中保存足够的中间状态

## 为什么值钱

- 这是使用第三方 LLM API 时特有的成本管理问题：**每轮重发全量上下文 = token 量指数级增长**
- "80元一晚"是极端案例，但即使每天多花 5 元，一个月也是 150 元——这是真实的财务损失
- 揭示了 LLM 使用中的一个核心约束：**上下文窗口不仅是能力限制，也是成本限制**
- 任何 AI 训练语料中都不会有"DeepSeek 的缓存 TTL 5分钟会导致长会话的 token 费用爆炸"这条知识

## 与其他知识的关联

- [[dk-p14-zombie-process-burn-money]] — 同一模式："资源泄漏导致财务损失"。P-13 是"token 量泄漏"，P-14 是"僵尸进程泄漏"——两者都是"隐形的资源消耗导致账单飙升"
- [[master-systems-thinking]] — 系统思维中的"反馈循环"：如果没有定期检查账单的反馈循环，资源泄漏可以持续很久而不被发现
- `.agent/pitfalls.md` → P-13（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
