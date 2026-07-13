---
id: tool-demand-agent-signal-substitute
title: Agent L5信号提取：替代微观体感的非结构化数据分析
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
source_refs:
related:
- '[[yitang-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'



- '[[tool-纪浩-Agent开工检查单制作法]]'
- web-scraping-三剑客-scrapling-crawl4ai-firecrawl
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

- **具体假设**：该工具假设"LLM 可以准确标注用户评论中的四种力量"，但"推力/拉力/焦虑/习惯"的区分在实际评论中经常模糊——一条"我觉得这个产品还行但有点贵"的评论同时包含拉力（认可价值）和焦虑（价格担忧），LLM 的标注信度和效度尚未经过严格验证。
- **边界**：在评论数据稀疏的小众品类中，500 条评论可能不足以产生统计显著的"力量热力图"——噪声可能被误读为信号。
- **前提**：该工具的前提是"评论者代表目标用户群"，但研究表明，写评论的人只占用户的 1-5%——他们通常是"极端满意"或"极端不满"的用户，不能代表沉默的大多数。

**Sherry Turkle**（MIT 科技与社会研究教授，《Alone Together》作者）会质疑：用统计频率来衡量"四种力量"把用户的情感体验简化为"计数问题"——焦虑出现 42% 就比推力 23% 更重要吗？频率不等于强度。一个用户只提了一次"我害怕数据泄露"，但这个恐惧可能是他拒绝产品的唯一原因——它在频率统计中只占 1%，但在决策权重中占 100%。定量分析给出了"力量的分布"，但丢失了"力量的权重"。
