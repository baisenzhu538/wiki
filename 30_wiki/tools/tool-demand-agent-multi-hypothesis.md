---
id: tool-demand-agent-multi-hypothesis
title: Agent L3多假设并行：5个核心任务同时推演
type: tool
status: reviewed
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
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tool-yitang-amazon-bestseller
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

- **具体假设**：该工具假设"5 个并行假设能覆盖核心任务的可能性空间"，但 5 个假设都来自同一个 LLM——它们可能共享相同的"认知盲点"。真正的"不同视角"需要不同模型、不同训练数据、不同推理范式，而非同一个 LLM 用不同 prompt 生成的变体。
- **边界**：当核心任务的本质是"情感需求"（如归属感、认同感）时，5 个假设的并行推演价值有限——因为情感需求的表达方式有限，5 个假设可能高度收敛。
- **前提**：该工具的前提是"交叉对比能选出最佳假设"，但交叉对比本身缺少"地面真相"——没有用户验证，5 个假设之间的比较只是"内部一致性检查"，不是"准确性验证"。

**Nassim Taleb**（纽约大学理工学院杰出教授，《黑天鹅》作者）会质疑：多假设并行的本质是"用更多模型对抗不确定性"，但这假设了"真相在候选假设之中"（候选空间是闭集）。真正的突破性需求洞察往往是"没人想到的假设"——它不在 5 个候选中。并行推演可能制造"覆盖了所有可能性"的错觉，让人放松对"未知未知"的警觉。
