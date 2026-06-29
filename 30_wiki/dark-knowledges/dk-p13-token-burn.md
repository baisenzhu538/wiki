---

id: dk-p13-token-burn
title: P-13：长会话 = token黑洞 — 一晚上烧掉80元
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-13
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - [[tool-月白-Token智甲比控制法]]
  - [[tool-月白-Token效价比决策公式]]
  - [[tool-月白-Token效价比决策法]]
  - [[tool-月白-烧Token快速积累体感]]
  - [[pending_unknown]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown# P-13：长会话 = token黑洞 — 一晚上烧掉80元

---

## 原始表述/核心洞察

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

核心洞察：**长会话会让 input tokens 随轮数非线性膨胀，缓存命中率断崖式下降，最终导致 token 费用远超任务本身价值。** 控制会话长度、减少每轮携带的上下文、把批量验证交给本地脚本，是 token 经济学的核心操作。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **一个 Sprint 一个会话**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **拆分长任务**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **减少上下文负担**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **监控 token 消耗**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 一个会话串多个 Sprint | 同一会话中出现 Dogfood → Sprint 2 → Sprint 3 → Sprint 4 | 每轮都重发前面所有 Sprint 的上下文 | 每完成一个 Sprint 立即 `/new`，通过 `.agent/context.md` 接力 |
| 忽视缓存 TTL | 账单中缓存未命中占费用 80% | 缓存 5 分钟超时后下一轮全量重新计费 | 控制单会话轮数，或在超时前主动结束会话 |
| 系统提示过大 | 每轮固定 4k+ tokens 来自 CLAUDE.md | 系统提示文件臃肿，塞进大量非必要内容 | 精简 CLAUDE.md，CLI 速查移出到独立文件 |
| 批量任务手动逐轮验证 | 100 轮里大量时间花在"帮我检查这一批" | Agent 反复读取并验证中间结果 | 写好脚本，让用户在本地批量跑，Agent 只负责最终验收 |
| 等到账单爆炸才发现 | 单次会话费用异常高 | 没有实时监控 | 每完成一批任务检查一次账单，设置费用告警 |

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

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
