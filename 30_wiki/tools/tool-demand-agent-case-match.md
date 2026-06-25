---

id: tool-demand-agent-case-match
title: Agent L4案例匹配：以历史摩擦点为起点填充8步地图
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain: [yitang, five-step-method, ai-collaboration]
source_refs:
- web: ODI framework cross-case comparison
related:
  - '[[agent-external-brain-design]]'
  - '[[tool-demand-agent-multi-hypothesis]]'
  - '[[tool-demand-agent-auto-verify]]'
  - '[[tool-demand-agent-signal-substitute]]'
  - '[[five-step-domain-digest]]'
- "[[tool-demand-iceberg-l4-job-map]]"
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

- **适用**：案例库中有相关案例时
- **不适用**：全新品类无人做过类似分析

---

*卡片类型：tool | 审核状态：待审*
