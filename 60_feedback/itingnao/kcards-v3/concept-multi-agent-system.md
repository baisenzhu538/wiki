---
id: "concept-multi-agent-system"
title: "概念卡：多智能体协作系统（Multi-Agent System）"
type: "concept-card"
status: "draft"
confidence_score: 0.78
trust_level: "high"
source_refs:
  - "itingnao-5549882 AI原生IM与多Agent协作"
  - "itingnao-5549864 AI原生IM与多Agent协作"
  - "Wooldridge (2009) An Introduction to MultiAgent Systems"
  - "Shoham & Leyton-Brown (2008) Multiagent Systems"
  - "Malone & Crowston (1994) Coordination Theory"
  - "arXiv (2025) Multi-Agent Coordination across Diverse Applications"
  - "OpenAI/Anthropic Agent 技术文档"
related:
  - "kcard-ai-methodology-tools-draft"
  - "six-layer-validation-ai-native-im-multi-agent.md"
tags:
  - #concept
  - #multi-agent
  - #ai-collaboration
  - #llm
  - #agent-orchestration
---

# 概念卡：多智能体协作系统（Multi-Agent System）

## 一句话定义

多智能体协作系统（Multi-Agent System, MAS）是由多个独立交互的决策主体（Agent）组成，通过分工、通信和协调共同完成复杂任务的系统。

## 学术定义

| 来源 | 定义 |
|------|------|
| Wooldridge (2009) | MAS 中的核心问题是协调（coordination），即多个 Agent 如何有效协作。 |
| Shoham & Leyton-Brown (2008) | MAS 是多个自主 Agent 的集合，这些 Agent 具有共同或冲突的利益和信息。 |
| Russell & Norvig (2021) | 从 Agent 视角看，一个 Agent 的性能依赖于其他实体，这些实体可被视为 Agent。 |
| Malone & Crowston (1994) | 协调是管理活动之间的依赖关系（coordination is managing dependencies between activities）。 |

## MAS 中的核心问题：协调

协调（Coordination）是 MAS 的核心机制，涉及四个基本问题：

1. **What is coordination?** 协调是什么？
2. **Why coordination?** 为什么需要协调？
3. **Who to coordinate with?** 与谁协调？
4. **How to coordinate?** 如何协调？

## 与单 Agent 的区别

| 维度 | 单 Agent | 多 Agent 系统 |
|------|---------|--------------|
| 能力边界 | 一个 Agent 负责全流程 | 多个 Agent 各自负责子任务 |
| 专业性 | 通用但浅 | 每个 Agent 可深度专精 |
| 可扩展性 | 受限于单个模型上下文 | 可动态增减 Agent |
| 复杂度 | 适合线性任务 | 适合并行、交互复杂任务 |
| 失败风险 | 单点失败 | 可隔离和恢复 |

## 典型角色分工

| 角色 | 职责 |
|------|------|
| 规划 Agent | 拆解目标、制定计划 |
| 执行 Agent | 调用工具完成具体任务 |
| 检索 Agent | 搜索和整理外部信息 |
| 校验 Agent | 检查输出质量和一致性 |
| 协调 Agent | 管理 Agent 间通信和冲突 |

## 协调机制分类

| 机制 | 说明 | 示例 |
|------|------|------|
| 涌现式（Emergent） | Agent 追求各自目标，通过环境交互产生协调行为 | 交通流、市场定价 |
| 意图式（Intentional） | Agent 主动通信以避免冲突、协调任务 | 多数企业 MAS |
| 市场式（Market-Based） | 通过拍卖/定价机制分配任务 | 云计算资源调度 |
| 层级式（Hierarchical） | 严格层级结构，角色和任务集中定义 | 传统组织、CrewAI hierarchical mode |
| 社交网络式（Social Networks） | 基于信任和社会关系协调 | 去中心化自治组织 |

## 协作模式

### 1. 流水线模式（Pipeline）

- Agent 按固定顺序传递任务。
- 例：写作 Agent → 编辑 Agent → 校验 Agent。
- 优点：结构清晰，易于监控。
- 缺点：灵活性低。

### 2. 评审模式（Review）

- 多个 Agent 分别生成方案，再由一个 Agent 汇总评审。
- 例：三个 Agent 分别提出营销方案，由一个 Agent 综合最优解。
- 优点：提升质量和多样性。
- 缺点：成本和延迟增加。

### 3. 辩论模式（Debate）

- 多个 Agent 扮演不同立场，相互质询。
- 例：正方 Agent 和反方 Agent 辩论一个战略决策。
- 优点：暴露盲点和风险。
- 缺点：需要设计好停止条件，避免无限循环。

## 技术挑战

1. **通信协议**：Agent 之间如何交换信息？
2. **任务分配**：如何把任务分配给最合适的 Agent？
3. **冲突解决**：Agent 意见不一致时怎么办？
4. **状态管理**：如何维护全局上下文和中间结果？
5. **成本控制**：多 Agent 调用的 token 和计算成本显著增加。

## 当前落地现状

- 理论研究丰富，工程落地仍在早期。
- 多数企业级应用采用"工作流 + 有限 Agent"的混合架构。
- 真正自主协作的多 Agent 系统在开放性、稳定性、可控性上仍有挑战。

## 对决策的启示

1. **不要为了多 Agent 而多 Agent**：单 Agent 能解决的不要拆。
2. **明确角色和边界**：每个 Agent 的能力和责任要清晰。
3. **设计好协调机制**：没有协调的多 Agent 会变成混乱。
4. **从简单模式开始**：先跑通流水线，再尝试评审、辩论等复杂模式。
