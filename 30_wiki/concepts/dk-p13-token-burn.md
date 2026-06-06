---
id: dk-p13-token-burn
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
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-p14-zombie
contradicts:
  - master-systems-thinking
  - master-decision-hygiene
---

# P-13：长会话 = token黑洞 — 一晚上烧掉80元

## 原始表述

> **症状**：黄药师从晚上开始跑 Dogfood → Sprint 2 → Sprint 3 → Sprint 4，一个会话跑到上下文爆掉再续第二个会话。共 ~100轮+，DeepSeek 账单 ~80元。单晚消耗超过过去10天总和。
>
> **根因**（三重叠加）：
> 1. **每轮重发全量上下文** — 后期每轮 input 100-150k tokens，其中 90% 是历史对话和工具结果
> 2. **CLAUDE.md 很大** — 每轮携带 ~4000 tokens 系统提示
> 3. **缓存 TTL 5分钟** — 超时后下一轮全量重新计费
>
> **反算**：总输入 ~14M tokens，缓存未命中 ~5.6M（占费用 80%）。
>
> **对策**：
> - **一个 Sprint 开一个会话** — 完成即 /new，通过 `.agent/context.md` 接力
> - 不要一口气跑 100轮——拆成 5个短会话，总 token 量降 70%+
> - CLAUDE.md 已精简（290→101行），CLI 速查移出到 `90_control/cli-reference.md`
> - 需要批量脚本任务的，写好脚本让用户本地跑，不用我一轮轮验证

## 使用场景

- 你准备在一个会话中连续处理多个独立任务（如多个 Sprint、多批卡片）
- 你注意到单轮 input tokens 已经超过 100k
- 你查看账单发现单次会话费用异常高
- 你设计 Agent 工作流，需要优化 token 消耗

## 操作方法

1. **一个 Sprint 一个会话**：
   - 完成一个 Sprint 后立即 `/new` 开新会话
   - 通过 `.agent/context.md` 传递状态，而非通过对话历史
   - 不要在一个会话中串多个 Sprint

2. **拆分长任务**：
   - 100 轮拆成 5 个 20 轮的短会话
   - 每个会话只处理一个明确的子任务
   - 总 token 消耗可降低 70%+

3. **减少上下文负担**：
   - 精简 CLAUDE.md（已做：290→101 行）
   - 将 CLI 速查移出到独立文件
   - 批量任务写脚本让用户本地跑，不用 Agent 一轮轮验证

4. **监控 token 消耗**：
   - 每完成一批任务检查一次账单
   - 关注"缓存命中率"——缓存未命中是费用大头
   - 设置费用告警（如单会话超过 $5 自动提醒）

5. **不要做的事**：
   - 不要一个会话跑 100+ 轮
   - 不要让上下文膨胀到 100k+ tokens 还在继续
   - 不要等积累了高额账单才发现问题

## 适用边界

- 适用于所有按 token 计费的 LLM API 调用场景
- 不适用本地模型或按请求计费的服务
- **与 P-14 的区别**：P-13 是"主动运行中的高消耗"，P-14 是"后台僵尸进程的静默消耗"
- 如果缓存 TTL 足够长（如 30 分钟），问题会减轻——但仍需控制单会话轮数

## 为什么值钱

- 这是**token 经济学**的实战教训：上下文长度与费用呈非线性关系
- 极具隐蔽性：用户不会实时感知 token 消耗，直到账单到来
- 揭示了"短会话接力"vs"长会话连续"的成本差异——不是 5 倍而是 10 倍
- **AI 训练语料中不会有这条**：没有任何文档会写"Agent 会话超过 50 轮后 token 费用呈指数增长"

## 与其他知识的关联

- dk-p14-zombie — P-13 和 P-14 是账单的两大来源：主动高消耗 + 僵尸进程消耗
- dk-p15-unverified — P-15 的"虚假完工报告"可能掩盖了 P-13 的高消耗
- `90_control/AGENTS.md` — Agent 会话管理规范
- `.agent/pitfalls.md` → P-13（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
