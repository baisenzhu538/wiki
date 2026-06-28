---

id: tool-agent-research-swarm
title: Swarm模式：多Agent自发协同与交叉验证
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.82
trust_level: medium
language: zh-CN
domain:
  - yitang
  - research
  - ai-collaboration
source_refs:
- src_unknown
- src_unknown
related:
  - [[dk-skill-market-agent-self-install]]
  - [[tool-agent-research-pipeline]]
  - [[ai-native-im-multi-agent]]
  - [[case-truman-ai-partner]]
  - [[tool-demand-agent-multi-hypothesis]]
  - [[framework-multi-agent-research-architecture]]
  - [[concepts/kimi-深度调研集群方法论-deep-research-swarm]]
---
# Swarm模式

> ⚠️ **2026年中快速演化领域，最佳实践可能半年后过时。** Swarm模式：多个Agent自发分工探索→互相验证发现→自动合成。Token效率比Supervisor高40%，适合需要速度的探索性调研。

## 操作步骤

```
Human: "发现XX赛道的投资机会"
  ↓
Agent A: 搜索行业报告 → 发现3个细分方向
  ↓（自动广播给B/C）
Agent B: 深挖方向1 → 做出财务模型
Agent C: 交叉验证B的数据 → 发现方向1的毛利率假设过于乐观
  ↓（peer-to-peer通知B）
Agent B: 修正假设 → 重新计算
  ↓
自动合成：ABC各自输出+交叉验证记录 → 最终报告
```

## Agent执行指令

```python
# Swarm模式概念示例（实际实现随框架变化）
from langgraph import Swarm

swarm = Swarm(
    agents=[
        MarketResearchAgent(),
        FinancialModelAgent(),
        CrossValidationAgent()
    ],
    coordination="peer_to_peer",  # Agent之间直接沟通
    max_rounds=5,                  # 防止无限循环
    dedup=True                     # 防止重复劳动
)
result = swarm.run("发现XX赛道的投资机会")
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 无限循环 | Agent之间反复传递同一任务 | 设置max_rounds + 任务去重 |
| 重复劳动 | 两个Agent做了完全相同的搜索 | 共享任务队列 |
| 缺乏合成 | 各自产出但没有整合结论 | 最后一个Agent专门负责合成 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
