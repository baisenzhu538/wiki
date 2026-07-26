---
id: method-yihang-agent-hr-role
title: Agent HR 角色（元 Agent）——专门盯着其他 Agent 表现的监督者
type: method
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-06
updated_at: 2026-07-06
domain:
- ai-collaboration
- yitang
source_refs:
- 对话记录：2026-07-05 老朱 Agent 纠察队/HR 角色实践
related:
- '[[method-yihang-ai-self-xray-iteration]]'
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[concept-yihang-dual-triangle-core]]'
tags:
- audience:general
- scene:diagnosis
- skill-level:advanced
---

# Agent HR 角色（元 Agent）——专门盯着其他 Agent 表现的监督者

> **一句话定义**：老朱实践——专门设计一个 Agent 来关注其他 Agent 的行为表现并评估。不是做事的 Agent，是看其他 Agent 做得怎么样的元 Agent。类似纠察队或 HR 角色。与 #97（AI 自我 X 光）互补——一个是"自己拆自己"，一个是"第三方盯着看"。

---

## 一、与复盘 Agent 的区别

| 维度 | #97 AI 自我 X 光 | 本卡 HR Agent |
|:---|:---|:---|
| 视角 | 第一人称——自己拆自己 | 第三人称——第三方盯着看 |
| 时机 | 任务开始前 | 任务执行中 + 事后 |
| 优势 | AI 最了解自己的设计过程 | 第三方没有盲区——"自己看不到的问题别人能看到" |
| 劣势 | 自我评估可能美化自己 | 需要额外定义一个 Agent |

---

## 二、设计框架

| 要素 | 内容 |
|:---|:---|
| **审美** | 怎么判断一个 Agent "表现好"还是"表现差"？——幻觉频率、放弃模式（错误笃定）、上下文丢失、执行偏离 |
| **体系** | 监控频率——实时 or 事后复盘？什么情况下叫停？——关键任务实时监控，常规任务事后抽查 |
| **场景** | 适用于多 Agent 协作场景（≥3 个 Agent 同时工作） |
| **数据** | 记录 Agent 行为日志——错误模式、注意力衰减节点、上下文溢出信号 |
| **基本功** | HR Agent 本身也是 AI——需要配置监控维度和评估标准 |

---

## 三、老朱实战案例

老朱在多 Agent 协作中设置了一个"纠察队" Agent，专门观察其他 Agent 的行为。发现：有 HR Agent 在场时，其他 Agent 的放弃模式（错误笃定）显著减少——不是因为 Agent 变聪明了，而是 HR Agent 在它们"放弃"时立即标记并上报。

---

## 四、Critique

**[Overhead Skeptic]**
> "加一个 HR Agent 等于多一倍的计算和 API 成本。这在小任务上完全是 overkill。"

**回应**：HR Agent 不是每个任务都要启用——只在多 Agent 协作且任务复杂度高时使用。单 Agent 简单任务不需要。

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 多 Agent 协作时感觉某个 Agent 输出质量在下降 | 启一个 HR Agent 盯着——让它专门记录"异常行为"日志 |
