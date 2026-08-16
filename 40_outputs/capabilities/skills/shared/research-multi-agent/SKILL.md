---
name: research-multi-agent
description: 多Agent协作调研——Supervisor/Swarm/Pipeline/Hybrid四种架构
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [多智能体, multi-agent, Supervisor, Swarm, Pipeline, CrewAI]
    related_skills: [research]
---

# 多 Agent 协作调研

当一个 Agent 不够时——四种多 Agent 架构模式，按任务复杂度、依赖关系、可靠性要求选择。

## Constraints

<hard_limits>
- Swarm 模式标注：2026 年中快速演化领域，最佳实践可能半年后过时（欧阳锋条件）
- 多 Agent 增加协调成本——先用单 Agent 跑通，再考虑并行
- 每个 Agent 必须有明确的职责边界，避免"两个 Agent 做同一件事"
</hard_limits>

## 四种架构模式

### 模式 1: Supervisor（一主多 Worker）

```
         Supervisor
        /    |    \
     W1     W2     W3
```

| 维度 | 说明 |
|:--|:--|
| **适用** | 任务可拆为独立子任务，需统一汇总 |
| **优点** | 结构清晰，Supervisor 把关质量 |
| **缺点** | Supervisor 是单点瓶颈 |
| **Agent 数** | 3-5 个 |
| **示例** | 调研一个行业：W1=市场，W2=竞对，W3=用户，Supervisor 汇总 |

### 模式 2: Swarm（自发协同）

```
    A1 ←→ A2
     ↕    ↕
    A3 ←→ A4
```

| 维度 | 说明 |
|:--|:--|
| **适用** | 探索性调研，任务边界模糊 |
| **优点** | 灵活，Agent 自主发现和分工 |
| **缺点** | 质量不可控，可能重复劳动 |
| **⚠️ 注意** | 2026 年中快速演化，最佳实践可能半年后过时 |
| **Agent 数** | 3-10+ 个 |

### 模式 3: Pipeline（流水线）

```
    A1 → A2 → A3 → A4
```

| 维度 | 说明 |
|:--|:--|
| **适用** | 任务有明确的先后依赖 |
| **优点** | 与 OSCAR 天然匹配，每阶段可独立优化 |
| **缺点** | 串行慢，前序错误后序全错 |
| **Agent 数** | 2-5 个 |
| **示例** | O:定义目标 → S:缩范围 → C:列清单 → A:获取情报 → R:归因 |

### 模式 4: Hybrid（混合）

```
    Supervisor
    /         \
  Pipeline    Swarm
  A1→A2→A3   A4↔A5↔A6
```

| 维度 | 说明 |
|:--|:--|
| **适用** | 大型综合调研，部分结构化+部分探索 |
| **优点** | 灵活度高，不同子任务用不同模式 |
| **缺点** | 设计复杂度高，调试困难 |
| **Agent 数** | 5-10+ 个 |

## 架构选择决策树

```
调研任务特征
├── 任务可拆为独立子任务 + 需汇总？ → Supervisor
├── 探索性、边界模糊？ → Swarm（⚠️ 标注意外风险）
├── 有明确先后依赖？ → Pipeline（推荐——与OSCAR匹配）
├── 部分结构化+部分探索？ → Hybrid
└── 不确定？ → 先用单 Agent 跑一遍，再判断要不要多 Agent
```

## Pipeline + OSCAR 实现（推荐首选）

```python
# 伪代码：用 Pipeline 实现 OSCAR 五步调研
pipeline = Pipeline([
    Agent("O", "定义目标", prompt=O_PROMPT),
    Agent("S", "缩范围", prompt=S_PROMPT),
    Agent("C", "列清单", prompt=C_PROMPT),
    Agent("A", "获取情报", tools=[WebSearch, WebFetch]),
    Agent("R", "归因总结", prompt=R_PROMPT)
])
result = pipeline.run(topic="调研XX行业")
```

## 常见失败

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 多 Agent 产出比单 Agent 还差 | 协调成本 > 并行收益 | 回退到单 Agent，先跑通 |
| Agent 之间产出重复 | 职责边界不清 | 每个 Agent 加"只做XX，不要做YY" |
| Pipeline 前序错误后序全错 | 缺少中间验证 | 每阶段输出加验证步骤 |
| Swarm 跑偏 | 自主度过高 | 加 Supervisor 约束 |

## 相关 wiki 卡片
- `framework-multi-agent-research-architecture`
- `tool-agent-research-supervisor`
- `tool-agent-research-swarm` ⚠️
- `tool-agent-research-pipeline`
- `framework-yitang-oscar-research` — OSCAR 五步法（Pipeline 天然匹配）
