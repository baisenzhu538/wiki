---
id: dk-c9-batch-trigger-garbage
title: C-9：批处理脚本提取 query_triggers→格式合法但语义垃圾，真 trigger 被淹没
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: 欧阳锋
source_context: Sprint 6 终审发现，2026-05-13
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- [[framework-ci-operating-model]]
- [[tool-ci-implement-phase]]
- [[dk-c8-format-complete-mind-empty]]
- [[master-decision-hygiene]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 脚本把 `### ` 标题当作搜索词，不区分语义；这些词是文章结构标记，不是真实用户搜索意图
  follow_up_question: 这条 trigger 是否对应一个真实用户会输入的中文搜索词？如果不会，删除并手动重写
- signal: src_unknown
  framework_lens: 格式门禁只检查字段存在性和语法，不检查语义质量；query_triggers 作为 Graph RAG 检索入口，垃圾 trigger
    直接降低卡片可发现性
  follow_up_question: 抽检 3 张卡的 query_triggers，逐条问'你会这样搜吗？'，有一条不合格就返工# C-9：批处理脚本提取 query_triggers→格式合法但语义垃圾，真 trigger 被淹没

## 原始表述/核心洞察

> Batches 3-4（entrepreneur + personal 卡）的 `query_triggers` 包含大量无意义的 section headers 和 critique 句子：
>
> ```
> query_triggers:
>   - 与一堂方法论的关系          ← 文章段落名，没人会搜
>   - 从知道到做到的鸿沟          ← critique 句子，没人会搜
>   - 核心定位                   ← 通用标签
>   - 关联卡片                   ← 导航词
>   - 学习建议                   ← 文章结构名
>   - 方法论的前提假设需要检验     ← critique 句子
> ```
>
> 真正能用的 trigger 只有工具名本身（"融资认知"）——但被淹没在一堆垃圾词里。
>
> 根因：脚本规则是"提取所有 `### ` 级标题作为 query_triggers"。这个规则在 panproduct 卡上碰巧可用（标题本身就是方法名："惊喜公式""五要素模型"），但在 entrepreneur/personal 卡上，标题是文章结构标记和 critique 文本——脚本不区分语义，全量灌入。

核心洞察：

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **禁止脚本自动提取 query_triggers**：这个字段必须**手动写**，任何"提取 `###` 标题""提取关键词""提取标签"的脚本都不准碰这个字段
2. **模拟真实搜索场景**：想象一个需要这张卡的用户，他会输入什么中文搜索词？聚焦在**工具名、方法名、场景描述、痛点关键词**
3. **写 5-10 个真实搜索词**：
   - src_unknown
   - src_unknown
4. **抽检验证**：审查者随机抽 3 张卡，对每条 trigger 问"你会这样搜吗？"——有一条答不上来，整张卡返工
5. **定期人工审计**：已有卡片的 `query_triggers` 需要周期性清理，删除导航词、章节标题、critique 句子等语义垃圾

## 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 适用 | 所有需要写 `query_triggers` 的 **KDO 知识卡片** |
| ❌ 不适用 | 标签/分类的自动生成：标签是结构化分类，不需要模拟用户搜索意图 |
| 特殊场景 | 结构化数据卡片（配置模板、代码片段）的 trigger 可以是字段名或技术术语 |
| 抽检约束 | 理解门禁的抽检率是底线要求，不能替代"人工写 triggers"的质量——抽检只能发现问题，不能保证覆盖面 |
| 多语言约束 | 多语言卡片（中英混合）需要为每种语言写对应的搜索词，不能只写一种 |

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复动作 |
|---|---|---|---|
| 章节标题混入 triggers | triggers 包含"与一堂方法论的关系""核心定位"等 | 脚本提取 `### ` 标题时不做语义过滤 | 删除，改写成真实搜索词 |
| critique 句子当 trigger | "从知道到做到的鸿沟""方法论的前提假设需要检验" | 脚本把 critique 文本当作关键词 | 删除，聚焦方法名/痛点词 |
| 导航词填充 | "关联卡片""学习建议""适用边界"出现在 triggers 中 | 为凑字段数量，用结构标签充数 | 全部删除，每条 trigger 必须通过"你会这样搜吗"测试 |
| 真 trigger 被淹没 | 有用的工具名/方法名混在一堆垃圾词里 | 没有 prioritization 或 manual curation | 人工精选 5-10 条，把真 trigger 置顶 |
| 抽检流于形式 | 审查者看一眼就过，没有逐条验证 | 缺少"你会这样搜吗"的硬性规则 | 随机抽 3 张卡，每条 trigger 必须能给出真实搜索场景 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
