---
id: "tool-agent-research-pipeline"
title: "Agent 调研 Pipeline 模式工具"
type: "tool"
domain:
  - "AI"
  - "research"
  - "agent"
tags:
  - "多智能体"
  - "Pipeline模式"
  - "OSCAR五步法"
  - "串行流程"
source_person: "Truman（一堂）+ LangChain Team"
source_context: "OSCAR 五步法的 Agent 自动化版本"
source_refs:
  - "60_feedback/diagnosis/diag_20260621_外部知识探索_三个新盲区.md"
  - "https://www.langchain.com/blog/benchmarking-multi-agent-architectures"
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

# Agent 调研 Pipeline 模式工具

## 原始表述

> "如果调研任务的步骤依赖关系明确——先搜→再提取→再分析——Pipeline 模式比 Swarm 更可靠。"
> ——Multi-Agent Architecture Survey（2026-04）

**Pipeline 模式**是多智能体调研架构中**依赖明确**场景的选择——串行：A→B→C 流水线，前一步的输出是后一步的输入。

一堂 OSCAR 五步法的天然 Agent 自动化版本。

---

## 使用场景

### 适合使用 Pipeline 模式的情境

- 调研任务步骤依赖关系明确（搜→提→分→报）
- 前一步的输出质量直接影响后一步（需要**阶段门控**）
- 需要**可预测的执行时间**（Pipeline 的耗时 = 各步之和，可提前估算）
- 串行任务用 Swarm 反而增加协调复杂度

### 不适合的情境

- 步骤间依赖不明确（用 Swarm 并行探索）
- 需要快速响应（Pipeline 比 Swarm 慢 2-3 倍）
- 某一步可能失败，需要**动态路径调整**（Pipeline 的刚性是劣势）

---

## 操作方法

### 第一步：把 OSCAR 五步法翻译成 Pipeline

| OSCAR 步骤 | Pipeline 阶段 | Agent 角色 | 输出物 |
|:---|:---|:---|:---|
| **O（Objective）** | 阶段 0：目标定义 | 协调者 Agent | 研究目标 + KIQs（Key Intelligence Questions） |
| **S（Source）** | 阶段 1：信息搜集 | 搜索 Agent（并行） | 原始素材包（带可信度标签） |
| **C（Capture）** | 阶段 2：信息提取 | 提取 Agent | 结构化信息表 |
| **A（Analyze）** | 阶段 3：分析综合 | 分析 Agent | 洞见报告草稿 |
| **R（Report）** | 阶段 4：报告生成 | 编写 Agent | 最终报告（带 Action Triggers） |

### 第二步：设计阶段间契约（Contract）

**核心原则**：每个阶段的输出必须**结构化**，才能成为下一个阶段的可靠输入。

**契约模板**（YAML 格式）：
```yaml
stage_1_output:
  raw_sources:
    - url: "..."
      snippet: "..."
      credibility: "A"
      timestamp: "..."
  coverage_gaps: ["...", "..."]
  next_stage_instructions: "优先验证 X，因为..."
```

### 第三步：设置阶段门控（Gate）

**门控规则**（防止"垃圾进，垃圾出"）：

| 门 | 检查点 | 不通过时的动作 |
|:---|:---|:---|
| **门 1→2** | 信息源 ≥3 个独立来源？覆盖率 ≥70%？ | 触发阶段 1 重新搜索（换关键词） |
| **门 2→3** | 结构化信息表非空？关键字段无缺失？ | 触发阶段 2 重新提取（换提取 prompt） |
| **门 3→4** | 洞见 ≥3 条？每条有证据支撑？ | 触发阶段 1 补充搜索（针对缺失证据） |

### 第四步：处理失败和异常

**Pipeline 的 Achilles  heel**：某一步失败，整个流水线停止。

**容错设计**：
1. **每阶段设置 timeout**（避免某个 Agent 卡死）
2. **每阶段设置 fallback**（主 Agent 失败 → 换备用 Agent 或降级处理）
3. **保存中间状态**（某步失败后，从最近的成功状态恢复）

---

## 与"人手动 OSCAR"的差异

| 维度 | 人手动 OSCAR | Agent Pipeline |
|:---|:---|:---|
| **速度** | 天级 | 分钟级 |
| **一致性** | 依赖个人状态 | 每次相同质量标准 |
| **规模** | 一次一个课题 | 同时跑 10+ 个 Pipeline |
| **代价** | 人力成本 | Token 成本 + 调试成本 |
| **适用场景** | 深度课题（需要人的判断） | 例行性调研（周度竞品追踪、月度行业扫描） |

**关键认知**：Pipeline 不是替代人的判断，而是**把人的判断固化到阶段门控中**。

---

## 为什么值钱

1. **可预测**：Pipeline 的耗时 = 各步之和，可以提前告诉用户"报告将在 8 分钟后生成"——Swarm 做不到（可能 2 分钟，也可能 20 分钟）。
2. **可调试**：某步输出质量差 → 精准定位到某个 Agent → 只改这个 Agent 的 prompt。
3. **可扩展**：同样的 Pipeline，换一个研究课题 → 直接跑，不需要重新设计架构。

---

## 与其他知识的关联

- **[[framework-multi-agent-research-architecture]]**

← 本工具是四种架构模式中「Pipeline」模式的工具化实现

- **[[framework-yitang-oscar-research]]**

← Pipeline 阶段设计直接对应 OSCAR 五步法，是一堂方法论的 Agent 自动化版本

- **[[tool-agent-research-supervisor]]**

→ Pipeline 可以嵌入 Supervisor 架构中（Supervisor 协调多个 Pipeline）

- **[[tool-agent-research-swarm]]**

→ 如果 Pipeline 的阶段 1 需要并行搜索多个来源 → 阶段 1 内部用 Swarm

---

## 适用边界

### Pipeline 模式生效的前提

- **步骤依赖关系明确**：如果步骤间依赖经常变化 → Pipeline 太刚性
- **每阶段的输出可以结构化**：如果某步的输出是"灵感"或"直觉"（无法结构化）→ Pipeline 会丢失价值
- **有足够 volume 支撑开发成本**：如果一年只跑 2 次调研 → 手动 OSCAR 更划算

### 常见误用

- **"Pipeline = 全自动"** → 错误。阶段门控需要人的判断（至少前 2 次运行）
- **"阶段越多越好"** → 错误。阶段越多，协调成本越高，失败概率越大。推荐 3-5 个阶段。
- **"Pipeline 比 Swarm 慢，所以不用"** → 错误。慢是特性，不是 bug——可预测的耗时在很多场景下比"可能快也可能慢"更有价值。

---

## 失败模式

| 失败模式 | 症状 | 根因 | 修正方法 |
|:---|:---|:---|:---|
| **"垃圾进垃圾出"** | Pipeline 跑完了，但报告质量差 | 阶段 1 的信息源质量差，门控没拦住 | 加严门控规则（信息源 ≥3 个独立来源） |
| **"卡死症"** | Pipeline 跑了一半，卡在某个阶段 | 某个 Agent 进入死循环或 timeout 设置太长 | 每阶段设置 timeout（推荐 2 分钟）+ fallback |
| **"刚性断裂"** | 实际调研中发现"需要先做步骤 5 才能做步骤 2"，但 Pipeline 不允许 | Pipeline 设计太刚性 | 用"条件跳转"增强 Pipeline（允许回跳） |

---

## Action Checklist

- [ ] 把当前最例行化的调研任务（周度竞品追踪？月度行业扫描？）翻译成 OSCAR 五步法
- [ ] 为每个步骤设计结构化输出契约（YAML 或 JSON Schema）
- [ ] 设置阶段门控规则（每步的输出质量检查）
- [ ] 先手动跑一遍完整 Pipeline（人扮演每个 Agent），确认流程可行
- [ ] 再用 Agent 跑一遍，对比结果差异，调优 prompt

---

## 来源与验证

| 断言 | 来源 | 可信度 |
|:---|:---|:---|
| Pipeline 模式对应 OSCAR 五步法 | 一堂 OSCAR 方法论 + 诊断报告 | A（方法论同源） |
| Pipeline 的可预测性优于 Swarm | LangChain benchmark（2025-06） | A（实验数据） |
| 阶段门控是 Pipeline 质量保障核心 | Agentic Workflow 最佳实践 | B（行业共识，无具体实验数据） |

---

## 口述数据标注

> 来源：一堂 OSCAR 方法论 + LangChain benchmark + 多智能体架构综述。Pipeline 模式的可预测性优势有实验数据支撑，可信度 A。
>
> ⚠️ "Pipeline 比 Swarm 慢 2-3 倍"——此为经验估计，具体倍数取决于阶段数量和每阶段的 Token 消耗，建议标注为"待验证"。
> ⚠️ "阶段门控需要人的判断"——此为前 2 次运行的要求，后续可以训练 Agent 自动判断门控，但当前（2026 年中）AI 自动门控的可靠性尚无充分验证。

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：Pipeline 模式假设"调研步骤可以严格串行排列"，但实际研究中经常出现"分析阶段发现需要回头补搜索"的情况——Pipeline 的刚性是**边界**，在探索性研究中反而不如 Swarm。
- **反例**：调研进行到分析阶段时发现某个关键假设无数据支撑，但 Pipeline 不允许回跳——要么继续生成有缺陷的报告，要么丢弃已有成果从头开始。

**Harrison Chase**（LangChain 创始人）会质疑：Pipeline 模式的"阶段门控"看似是质量保障，但实际工程中，门控规则往往是硬编码的阈值（如"信息源不少于 3 个"），而真正的研究质量判断需要语义理解——门控越严格，Pipeline 越容易卡住；门控越宽松，垃圾进垃圾出。
