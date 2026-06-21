---
id: tool-demand-agent-multi-hypothesis
title: Agent L3多假设并行：5个核心任务同时推演
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, five-step-method, ai-collaboration]
source_refs:
- web: Swarm multi-agent architecture (LangGraph)
related:
- "[[tool-demand-iceberg-l3-core-job]]"
- "[[tool-agent-research-swarm]]"
---

# Agent L3多假设并行

> L3的传统做法是"选一个核心任务深挖"。Agent可以生成5个不同视角的核心任务假设，用Swarm模式并行推演，交叉对比后选出最精准的。

## 方法

1. Agent基于L1/L2信号生成5个核心任务假设
2. Swarm模式：5个Worker并行推演各自的假设
3. 交叉对比：哪个假设更准确地覆盖了L1/L2的信号？
4. 输出最佳核心任务陈述+备选方案

## Agent执行指令

**具体工具引用**：`tool-agent-research-swarm`（Swarm模式推演）、`tool-demand-iceberg-l3-core-job`（核心任务定义模板）

```python
hypotheses = agent.generate_hypotheses(user_segment, scenario, n=5)
swarm = SwarmOrchestrator()
for h in hypotheses:
    swarm.spawn(f"推演核心任务: {h}", tool="tool-demand-iceberg-l3-core-job")
results = swarm.collect()
best = cross_compare(results, criteria=["方案中立", "可测量", "覆盖度"])
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 假设雷同 | 5个假设其实是一个意思的不同表达 | 强制不同视角：抽象/中观/具体/功能/情感 |
| 交叉对比失真 | Swarm的Agent互相影响 | 独立推演，推演完毕后再交叉 |

## 适用边界

- **适用**：L1/L2完成后，需要从多个角度定义核心任务
- **不适用**：需求非常明确的场景

---

*卡片类型：tool | 审核状态：待审*
