---
id: tool-demand-agent-case-match
title: Agent L4案例匹配：以历史摩擦点为起点填充8步地图
type: tool
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- yitang
- five-step-method
- ai-collaboration
aliases:
  - AgentL4案例匹配：以历史摩擦点为起点填充8步地图
  - L4案例匹配
  - 以历史摩擦点为起点填充
  - 以历史摩擦点为起点填充8步地图
  - 史摩擦点为起点填充
  - 步地图
source_refs: null
related:
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'
- tool-yitang-amazon-bestseller
- tool-yitang-ai-monitoring-alert
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# Agent L4案例匹配

> 开始一张空白的8步地图很难。Agent可以检索案例库中相似任务的8步地图作为起点——不必从零发明。

## 方法

1. Agent根据L3的核心任务在案例库中检索相似案例
2. 提取相似案例的8步地图作为模板
3. 标记模板中与当前任务"相同/不同/需验证"的步骤
4. 人工确认后作为定制化8步地图的起点

## Agent执行指令

**具体工具引用**：`search_files`（检索30_wiki/cases/下相关案例）、`tool-demand-iceberg-l4-job-map`（提取8步地图模板）

```python
similar_cases = agent.search_cases(
    job_statement="{CORE_JOB}",
    domain="yitang-demand",
    top_k=5
)
template_map = agent.extract_job_map(similar_cases[0])
agent.highlight_diff(template_map, current_context)
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 模板生搬 | 不同品类的8步地图完全不同 | 只提取"步骤结构"，不提取具体内容 |
| 案例太少 | 找不到相似案例 | 回退到从头构建8步地图 |

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

- **具体假设**：该工具假设"历史案例的 8 步地图可作为新任务的推演起点"，但案例匹配的最大风险是"表面相似、深层不同"——两个看似类似的业务（如社区生鲜 vs 社区药品配送）在用户心理、决策链条、履约逻辑上可能完全不同。
- **边界**：当案例库中的案例数量少于 20 个时，匹配结果过于依赖少数案例，容易产生"以偏概全"的推演偏差。
- **前提**：该工具的前提是"案例库中的摩擦点标注是准确的"，但案例的撰写者可能只记录了"自己认为重要的"摩擦点——真正的瓶颈可能被遗漏。

**Roger Schank**（AI 研究者，案例推理理论创始人）会质疑：案例匹配的质量完全取决于"索引方案"——即用什么维度来判断"相似"。当前的工具用关键词匹配来检索案例，但真正的案例推理需要"结构化相似"——不仅关键词匹配，还要匹配"用户的心理状态、决策约束、资源条件"。关键词匹配只会找到"表面相似"的案例，而非"深层可迁移"的案例。
