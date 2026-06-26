---

id: tool-demand-agent-signal-substitute
title: Agent L5信号提取：替代微观体感的非结构化数据分析
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
- web: Qualz.ai 2026 LLM-based user interview analysis
related:
  - '[[tool-demand-agent-signals]]'
  - '[[tool-yitang-18-strategy-tool-mapping]]'
  - '[[tool-demand-agent-case-match]]'
  - '[[tool-demand-four-forces]]'
  - '[[tool-demand-agent-auto-verify]]'
  - "[[tool-demand-iceberg-l5-forces]]"
---

# Agent L5信号提取

> L5的"微观体感推演"需要人的共情能力——Agent做不到。但Agent可以替代另一个维度：从非结构化数据中提取四种力量和三种任务的信号模式。

## 方法

1. Agent收集竞品的用户评价/访谈记录/社区讨论
2. 用LLM自动标注：哪些内容属于推力/拉力/焦虑/习惯
3. 统计四种力量的出现频率和强度
4. 输出"四种力量热力图"——哪些力量在用户叙述中最突出

## Agent执行指令

**具体工具引用**：`research-web-scraping`（批量抓取竞品用户评价）、Firecrawl API（`/v1/scrape` 提取结构化文本）、`research-cross-validation`（标注结果抽样验证）

```python
reviews = agent.collect_reviews(competitor="X", n=500)
analysis = agent.analyze_forces(reviews)
# 输出：{push: 23%, pull: 15%, anxiety: 42%, habit: 20%}
# 结论：焦虑是最大阻力——用户担心数据安全，不是不认可产品价值
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 标注不准 | LLM把"我觉得还行"标为推力 | 人工抽查标注质量 |
| 信号≠微观体感 | 统计告诉我们推力占23%，但不告诉我们"推力的具体感觉" | Agent做定量统计，人做定性共情 |

## 适用边界

- **适用**：有大量用户评价/访谈数据时，Agent做定量分析
- **不适用**：微观体感的共情推演——这部分仍是人的主场

---

*卡片类型：tool | 审核状态：待审*
