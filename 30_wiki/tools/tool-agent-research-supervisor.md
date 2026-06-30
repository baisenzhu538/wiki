---
id: "tool-agent-research-supervisor"
title: "Agent 调研 Supervisor 模式工具"
type: "tool"
domain:
  - "AI"
  - "research"
  - "agent"
tags:
  - "多智能体"
  - "Supervisor模式"
  - "LangGraph"
  - "可靠性优先"
source_person: "LangChain Team（Will Fu-Hinthorn）+ Truman（一堂）"
source_context: "LangChain 官方 Supervisor 模式 benchmark + 优化方案"
source_refs:
  - "https://www.langchain.com/blog/benchmarking-multi-agent-architectures"
  - "https://github.com/langchain-ai/langgraph-supervisor-py"
related:
  - "[[framework-yitang-oscar-research]]"
  - "[[case-demand-travel-agent]]"
  - "[[case-ji-hao-skills-market]]"
  - "[[case-truman-ai-partner]]"
  - "[[case-ban-fei-mao-from-assignment-to-tool]]"
status: reviewed
reviewed_by: 欧阳锋
review_date: "2026-06-28"
quality_labels:
  - actionable
  - cited
  - validated
created_at: "2026-06-28"
updated_at: '2026-06-28'
confidence: 0.78
trust_level: "medium"
---

# Agent 调研 Supervisor 模式工具

## 原始表述

> "Supervisor 架构的核心优势是可靠性，但代价是 token 消耗和'翻译层'误差。"
> ——LangChain Multi-Agent Benchmark（2025-06）

**Supervisor 模式**是多智能体研究架构中**可靠性优先**的选择——中央协调者（Supervisor）接收用户输入，分配子任务给 Worker Agents，Worker 的响应必须经过 Supervisor 才能返回给用户。

**适用场景**：报告生成、合规分析、需要严格收敛的研究任务。

---

## 使用场景

### 适合使用 Supervisor 模式的情境

- 研究任务需要**严格收敛**（报告必须完整，不能发散）
- **可靠性优先**于速度和成本（合规分析、财务报告）
- 需要**中央质量控制**（Supervisor 可以审核 Worker 输出）
- Worker Agents 是第三方（不方便让它们直接回复用户）

### 不适合的情境

- **探索优先**的研究任务（Supervisor 的"翻译层"会拖慢速度）
- Token 预算紧张（Supervisor 比 Swarm 多用 token）
- 需要**并行搜索**多个信息源（Swarm 模式更适合）

---

## 操作方法

### LangChain `langgraph-supervisor` 标准操作步骤

#### 第一步：定义 Supervisor 的 prompt 和工具

**Supervisor 的 prompt 必须明确**：
1. **任务目标**（要回答什么问题？）
2. **可用 Worker 列表**（每个 Worker 的专长和工具）
3. **收敛条件**（什么时候算"任务完成"？）
4. **输出格式**（报告结构、引用要求）

**示例 Supervisor prompt**：
```
你是研究总指挥。
你的目标是回答：{核心研究问题}。
你可以调用以下 Workers：
- worker_search：并行搜索多个信息源
- worker_extract：从搜索结果提取结构化信息
- worker_analyze：分析提取的信息，生成洞见
收敛条件：所有 Workers 已完成任务，且你已经合成最终报告。
```

#### 第二步：优化 Supervisor（关键！）

**LangChain 的 3 个优化选项**（必须开启，否则性能很差）：

| 优化选项 | 作用 | 效果 |
|:---|:---|:---|
| `remove_handoff_messages` | 从 Worker 状态中移除 handoff 消息 | 减少 Worker 的上下文噪音，性能提升 ~25% |
| `forward_message` 工具 | Supervisor 可以直接转发 Worker 响应给用户 | 避免"翻译层"误差，性能提升 ~25% |
| Tool naming | 用 `delegate_to_<agent>` 而非 `transfer_to_<agent>` | 更明确的委托语义，减少路由错误 |

#### 第三步：定义 Worker Agents

**每个 Worker 必须明确**：
1. **专长领域**（只做一类任务，不做"万能 Worker"）
2. **工具列表**（只给它需要的工具，减少上下文噪音）
3. **输出格式**（结构化输出，方便 Supervisor 合成）

**示例 Worker 定义**：
```
worker_search：
- 工具：web_search、web_fetch
- 专长：并行搜索 3-5 个信息源
- 输出：结构化搜索结果（标题、URL、摘要、可信度）

worker_extract：
- 工具：无（只读输入）
- 专长：从搜索结果提取关键信息
- 输出：结构化信息表（字段、值、来源、可信度）

worker_analyze：
- 工具：无（只读输入）
- 专长：交叉验证、识别矛盾、生成洞见
- 输出：分析报告（洞见、证据、矛盾点、置信度）
```

#### 第四步：运行和监控

**监控指标**：
- **收敛时间**（从任务开始到 Supervisor 输出最终报告）
- **Worker 调用次数**（是否某个 Worker 被过度调用？）
- **"翻译层"误差**（Worker 输出被正确转发了吗？）

**常见失败模式**：
| 失败模式 | 症状 | 根因 | 修正方法 |
|:---|:---|:---|:---|
| **"翻译层"误差** | Worker 输出被正确执行，但 Supervisor 的摘要漏掉了关键信息 | Supervisor prompt 没有要求"完整转发 Worker 输出" | 开启 `forward_message` 工具 |
| **Worker 失控** | 某个 Worker 被反复调用，任务不收敛 | 没有明确的收敛条件 | 在 Supervisor prompt 中明确"收敛条件" |
| **上下文溢出** | Worker 收到 Supervisor 的路由逻辑，上下文噪音大 | 没有开启 `remove_handoff_messages` | 开启该优化选项 |

---

## 与 Swarm 模式的对比

| 维度 | Supervisor | Swarm |
|:---|:---|:---|
| **可靠性** | ⭐⭐⭐⭐⭐（中央质量控制） | ⭐⭐⭐（无中央协调） |
| **速度/成本** | ⭐⭐（多"翻译层"，token 消耗高） | ⭐⭐⭐⭐（直接回复，token 消耗低） |
| **适用场景** | 报告生成、合规分析、需要严格收敛 | 并行探索、多源搜索、探索优先 |
| **LangChain benchmark** | Single domain 最优；Multi-domain 需优化 | 性能略优于 Supervisor，token 使用更少 |

**选择决策树**：
```
任务需要严格收敛？
├─ 是 → Supervisor（优化版）
└─ 否（探索优先）→ Swarm
```

---

## 为什么值钱

1. **可靠性优先场景的唯一选择**：报告生成、合规分析等任务不能"发散"，Supervisor 的中央质量控制是刚需。
2. **与一堂 OSCAR 天然对接**：Supervisor = OSCAR 的"总指挥"，Workers = OSCAR 的各步骤执行者。
3. **LangChain 优化方案已成熟**：`langgraph-supervisor` 包已包含性能优化选项，不需要自己踩坑。

---

## 与其他知识的关联

- **[[framework-multi-agent-research-architecture]]**

← 本工具是四种架构模式中「Supervisor」模式的工具化实现

- **[[tool-agent-research-swarm]]**

→ Swarm 是探索优先的替代方案，和 Supervisor 互补

- **[[framework-yitang-oscar-research]]**

← OSCAR 五步法的"总指挥"角色 = Supervisor；各步骤执行者 = Workers

- **[[tool-agent-research-pipeline]]**

→ Pipeline 是串行版本，Supervisor 是（可并行）版本

---

## 适用边界

### 有效使用的条件

- 任务需要**严格收敛**（报告必须完整）
- 有能力**定义清晰的 Supervisor prompt**（这是成功的关键）
- 使用 LangGraph 或其他支持 Supervisor 模式的编排框架

### 常见误用

- **"所有任务都用 Supervisor"** → 错误。探索优先的任务用 Swarm 更快更省。
- **"Supervisor 不需要优化"** → 错误。Naive Supervisor 性能很差，必须开启优化选项。
- **"Worker 越多越好"** → 错误。Worker 越多，Supervisor 的路由逻辑越复杂，错误率越高。

---

## 失败模式

| 失败模式 | 症状 | 根因 | 修正方法 |
|:---|:---|:---|:---|
| **"翻译层"误差** | Worker 输出被正确执行，但 Supervisor 摘要漏掉关键信息 | 没有开启 `forward_message` | 开启该工具 + 在 prompt 中要求"完整转发" |
| **Worker 失控** | 任务不收敛，无限循环 | 没有明确的收敛条件 | 在 Supervisor prompt 中明确"收敛条件"和"最大 Worker 调用次数" |
| **上下文溢出** | Worker 性能下降 | Worker 收到了 Supervisor 的路由逻辑（噪音） | 开启 `remove_handoff_messages` |

---

## Action Checklist

- [ ] **定义 Supervisor prompt**：明确任务目标、可用 Workers、收敛条件、输出格式
- [ ] **开启优化选项**：`remove_handoff_messages` + `forward_message` 工具
- [ ] **定义 Workers**：每个 Worker 明确专长、工具、输出格式
- [ ] **运行小规模测试**：用简单任务验证 Supervisor + Workers 是否按预期工作
- [ ] **监控收敛时间**：如果收敛时间太长，检查是否是 Worker 失控或上下文溢出

---

## 来源与验证

| 断言 | 来源 | 可信度 |
|:---|:---|:---|
| Supervisor 模式操作步骤和优化方案 | LangChain 官方博客 + `langgraph-supervisor` 文档 | A（官方文档） |
| "翻译层"误差是 Supervisor 的核心问题 | LangChain Multi-Agent Benchmark（2025-06） | A（实验数据） |
| 优化选项提升性能 ~50% | 同上 | A（实验数据） |

---

## 口述数据标注

> 来源：LangChain 官方文档和 benchmark 报告。Supervisor 模式的操作步骤和优化方案有官方来源，可信度 A。
>
> ⚠️ "性能提升 ~50%"——此为 LangChain 在特定 benchmark 上的结果，实际提升取决于任务复杂度和优化选项的使用方式。

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
