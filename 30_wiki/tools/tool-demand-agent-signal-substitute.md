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
domain:
- yitang
- five-step-method
- ai-collaboration
source_refs:
- src_unknown
related:
  - "[[yitang-domain-digest]]"
  - "[[ai-collaboration-domain-digest]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
updated_at: '2026-06-29'
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

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
