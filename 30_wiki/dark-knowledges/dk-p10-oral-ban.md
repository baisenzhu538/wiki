---

id: dk-p10-oral-ban
title: P-10：口头禁令 vs 书面约束——审查意见必须落笔到任务文件
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: 欧阳锋
source_context: pitfalls.md P-10，老顽童 Batch 2+3 审查，2026-06-03
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- [[dk-skill-market-agent-self-install]]
- [[ai-native-im-multi-agent]]
- [[case-truman-ai-partner]]
- [[dk-f12-builder-context-deadlock]]
- [[dk-p15-unverified]]
- [[dk-p15-unverified]]
- [[dk-f9-generic-critique]]
- [[master-decision-hygiene]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown# P-10：口头禁令 vs 书面约束——审查意见必须落笔到任务文件
---
## 原始表述/核心洞察

> **症状**：欧阳锋在审查老顽童 Batch 2+3 时口头说"后续 Batch 全面封禁 Kahneman 和 Taleb"。用户问"禁令指什么？"——任务文件里根本没有这条。口头意见与书面指令脱节，造成执行者和决策者之间的信息不对称。
>
> **根因**：审查者在对话中产出了约束性意见，但没有同步写入任务文件（唯一真相源）。口头指令在换会话后丢失，且执行者无法核实。
>
> **对策**：
> - **所有约束性指令必须写入任务文件，口头审查只能是讨论**
> - 审查意见要分"观察"和"指令"两类，指令类必须当场写入 task 文件
> - 任务文件是唯一真相源——如果任务文件里没有，就等于不存在
> - 具体案例：最终改为写入任务文件的软约束"同一域内，每5张卡至少引入1位新攻击者"

核心洞察：

- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **审查者：当场落笔**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **执行者：没有书面就不算**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **任务文件 = 唯一真相源**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **软约束的写法**：
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
- src_unknown

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 防御措施 |
|
|---|---|---|
| 口头禁令未落笔 | 审查者说"全面禁止 X"，任务文件无记录 | 审查者把对话当作已生效指令 | 当场打开任务文件写入约束，并复述确认 |
| 绝对化禁令 | "不要出现任何 Kahneman""完全禁止 Taleb" | 约束不可量化，执行者无法判断是否合规 | 改写为可验证的软约束，如"每5张卡至少1位新攻击者" |
| 执行者依赖口头印象 | "我记得欧阳锋说过……" | 执行者未要求书面确认 | 没有书面就不算；主动提醒写入任务文件 |
| 跨会话失忆 | 换会话后 nobody 记得禁令具体内容 | Agent 无记忆，口头信息未持久化 | 所有约束性指令必须在任务文件中可追溯 |
| 观察与指令混淆 | 审查者说"这张卡有问题"，执行者理解为"以后都不许做" | 未区分"观察"与"指令" | 明确标注"这是观察"或"这是指令，请写入任务文件" |

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

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
