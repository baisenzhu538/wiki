---

id: tool-agent-research-supervisor
title: Supervisor模式：一个主Agent调度多个Worker
type: tool
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
- web: LangGraph Supervisor pattern (LangChain)
related:
  - '[[tool-agent-crawl4ai]]'
  - '[[tool-agent-research-swarm]]'
  - '[[framework-multi-agent-research-architecture]]'
  - "[[framework-multi-agent-research-architecture]]"
---

# Supervisor模式

> 一个Supervisor Agent接收调研任务→分解成子任务→分配给不同Worker Agent→收集结果→做最终合成和质量控制。适合需要可靠性保障的调研场景。

## 操作步骤

```
Human: "调研竞对A的定价策略"
  ↓
Supervisor: 拆解
  - Worker1: 抓取A的官网定价页 + Wayback Machine历史价格
  - Worker2: 搜索A的客户评价中的价格反馈
  - Worker3: 社保/招聘数据分析A的团队规模和成本
  ↓
Worker1/2/3 并行执行 → 返回结果
  ↓
Supervisor: 质量检查
  - 三个Worker的结果一致吗？
  - 有没有明显缺失的维度？
  - 需要补充搜索吗？
  ↓
Supervisor: 合成最终报告
```

## Agent执行指令

```python
# LangGraph Supervisor示例
from langgraph import StateGraph, Supervisor

workflow = StateGraph()

# 定义Worker
@workflow.worker
def pricing_scraper(url: str) -> dict:
    """抓取并分析定价信息"""
    pass

@workflow.worker  
def review_analyzer(company: str) -> dict:
    """分析用户评价中的价格反馈"""
    pass

# Supervisor协调
supervisor = Supervisor(workers=[pricing_scraper, review_analyzer])
result = supervisor.run("调研竞对A的定价策略")
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| Supervisor瓶颈 | 其他Worker空闲等Supervisor分配 | 预分解任务，减少Supervisor干预 |
| Worker结果不一致 | 两个Worker对同一个问题给出矛盾答案 | Supervisor做交叉验证+请求第三个Worker仲裁 |
| 合成质量差 | 最终报告像拼凑而非整合 | 给Supervisor明确的合成模板 |

## 适用边界

- **适用**：合规分析、报告生成、需要审计追踪的任务
- **不适用**：高并发探索、低延迟要求

---

*卡片类型：tool | 审核状态：待审*
