---
id: framework-multi-agent-research-architecture
title: 多智能体调研架构：四种模式的对比与选择
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain: [yitang, research, ai-collaboration]
source_refs:
- web: LangGraph multi-agent patterns (LangChain docs)
- web: Paiteq multi-agent architecture guide
- web: Lushbinary agent architecture patterns
related:
- "[[tool-agent-native-overview]]"
- "[[tool-agent-research-supervisor]]"
- "[[tool-agent-research-swarm]]"
- "[[tool-agent-research-pipeline]]"
- "[[concepts/kimi-深度调研集群方法论-deep-research-swarm]]"
- "[[concept-harness-cattle-not-pets]]"
---

# 多智能体调研架构

> 一个Agent做调研有上限。多个Agent分工协作——不同Agent执行武器库的不同策略，自动交叉验证，并行加速。LangChain benchmark：Swarm比Supervisor少40% token，但Supervisor更可靠。

## 四种模式对比

| 模式 | 结构 | 适用场景 | Token效率 | 可靠性 | 灵活性 |
|:---|:---|:---|:---:|:---:|:---:|
| **Supervisor** | 一个主Agent分配任务给Worker | 合规、审计、需质量控制 | 中 | ⭐⭐⭐⭐⭐ | 低 |
| **Swarm** | 多个Agent自发协同 | 探索性调研、多源并行 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Pipeline** | 串行流水线 | 步骤依赖明确的任务 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 低 |
| **Hybrid** | 前三种的组合 | 复杂项目 | 中 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 选择决策树

```
调研任务特征：
├─ 步骤有严格先后依赖？
│  ├─ 是 → Pipeline
│  └─ 否 → 下一步
├─ 需要审计追踪/高可靠性？
│  ├─ 是 → Supervisor
│  └─ 否 → 下一步
├─ 需要广泛探索/多源并行？
│  ├─ 是 → Swarm
│  └─ 否 → Supervisor（兜底）
└─ 项目特别复杂？
   └─ Hybrid
```

## 生产级失败模式

| 模式 | 主要风险 | 缓解措施 |
|:---|:---|:---|
| Supervisor | 单点故障——Supervisor挂了全停 | Supervisor状态持久化+重启恢复 |
| Swarm | 无限循环——Agent之间重复传递任务 | 设置max_rounds上限+去重机制 |
| Pipeline | 错误传播——Step 2的输出错误导致Step 3崩 | 每步输出前加验证门禁 |
| Hybrid | 复杂度爆炸——难以调试 | 先单独验证每个子模式再组合 |

## Agent执行指令

```python
# 架构选择模板
def select_architecture(task):
    if task.has_sequential_dependencies():
        return "Pipeline"
    if task.requires_audit_trail():
        return "Supervisor"
    if task.requires_broad_exploration():
        return "Swarm"
    return "Supervisor"  # 默认兜底
```

## 适用边界

- **适用**：大型调研项目、需要多源并行搜索、需要审计追踪的企业场景
- **不适用**：简单问答、单一数据源的调研
- **学习曲线**：Swarm最简单（自发协同），Supervisor需要设计Worker分工

---

*卡片类型：framework | 审核状态：待审*
