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
domain:
- yitang
- five-step-method
- ai-collaboration
source_refs:
- src_unknown
related:
  - "[[yitang-domain-digest]]"
  - "[[ai-collaboration-domain-digest]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
updated_at: '2026-06-29'
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

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
