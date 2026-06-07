---
id: "dk-c9-batch-trigger-garbage"
title: "C-9：批处理脚本提取 query_triggers→格式合法但语义垃圾，真 trigger 被淹没"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "欧阳锋"
source_context: "Sprint 6 终审发现，2026-05-13"
source_refs:
  - "20_memory/corrections.md#C-9"
tags:
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/knowledge-management/tagging"
  - "#scene/learning-methodology"
  - "#scene/skill-engineering/eval-testing"
  - "#source_type/error"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c8-format-complete-mind-empty"
  - "master-decision-hygiene"
---

# C-9：批处理脚本提取 query_triggers→格式合法但语义垃圾，真 trigger 被淹没

## 原始表述

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
>
> 本质是 C-8 的另一个变体：批处理输出在格式上合法（字段非空、格式正确、lint 通过），但语义上是垃圾。格式门禁完全检测不到——只有人读了内容才能判断"这个词不会有人搜"。
>
> 修正：
> 1. `query_triggers` 字段**禁止脚本自动提取**。必须手动写 5-10 个真实用户会输入的中文搜索词
> 2. 验证方法：欧阳锋抽检 3 张卡，每条 trigger 问"你会这样搜吗？"——有一条答不上来就返工
> 3. 关联原则：见 `operating-principles.md` 第 7 条

## 使用场景

- 你准备给一批卡片写 `query_triggers`， tempted 用脚本自动提取标题或关键词填充
- 你审查卡片时发现 triggers 里充斥着"核心定位""关联卡片""学习建议"这类导航词
- 你设计自动化管线时，需要决定哪些 frontmatter 字段可以脚本生成、哪些必须人工写
- 你使用 `kdo query` 检索卡片时发现返回结果相关性差，需要排查是否是 trigger 质量问题

## 操作方法

1. **禁止脚本自动提取 query_triggers**：这个字段必须**手动写**，任何"提取 ### 标题""提取关键词""提取标签"的脚本都不准碰这个字段
2. **模拟真实搜索场景**：想象一个需要这张卡的用户，他会输入什么中文搜索词？聚焦在**工具名、方法名、场景描述、痛点关键词**
3. **写 5-10 个真实搜索词**：
   - ✅ 合格：`惊喜公式`、`峰值体验设计`、`用户留存率提升方法`
   - ❌ 垃圾：`与一堂方法论的关系`、`从知道到做到的鸿沟`、`核心定位`
4. **抽检验证**：审查者随机抽 3 张卡，对每条 trigger 问"你会这样搜吗？"——有一条答不上来，整张卡返工
5. **定期人工审计**：已有卡片的 `query_triggers` 需要周期性清理，删除导航词、章节标题、critique 句子等语义垃圾

## 适用边界

- 适用于所有需要写 `query_triggers` 的 **KDO 知识卡片**
- **不适用于标签/分类的自动生成**：标签（tags）可以用脚本辅助生成，因为标签是结构化分类，不需要模拟用户搜索意图
- 如果卡片是结构化数据（如配置模板、代码片段）而非知识内容，trigger 的写法标准不同——此时 trigger 可以是字段名或技术术语
- 理解门禁的抽检率是底线要求，不能替代"人工写 triggers"的质量——抽检只能发现问题，不能保证写得好的 trigger 覆盖面足够
- 多语言卡片（中英混合）需要为每种语言写对应的搜索词，不能只写一种

## 为什么值钱

- C-9 是 **C-8 的深层变体**，揭示了"格式合法但语义垃圾"这一模式的另一个切面：C-8 是内容空洞，C-9 是 trigger 垃圾——两者都是"脚本填满了字段，但字段里没有价值"
- **query_triggers 是 Graph RAG 检索的入口**：如果 trigger 全是垃圾，用户永远搜不到这张卡——这张卡就等于不存在
- 这个坑的隐蔽性极高：lint 通过、validate 通过、字段非空、格式正确——所有机器检查都绿灯，只有人读了内容才能判断"这个词不会有人搜"
- 任何 AI 训练语料中都不会有"KDO 的 query_triggers 不能脚本提取"这条知识——这是知识管理领域的具体实践约束，不是通用软件工程原则

## 与其他知识的关联

- [[dk-c8-format-complete-mind-empty]] — 同一模式的变体：批处理输出在格式上合法但语义上是垃圾。C-8 是"内容从未被填入"，C-9 是"trigger 被垃圾淹没"——两者共同构成"格式门禁 ≠ 内容合格"的完整证据链
- [[master-decision-hygiene]] — 决策卫生的 Step 3（独立评估）：不能让写脚本的人审自己的输出质量。C-9 的 triggers 如果由脚本作者自己验收，永远发现不了问题——必须引入外部审查者
- `20_memory/corrections.md` → C-9（原始记录）
- `90_control/failure-modes.md` → 批处理三连坑（C-8、C-9、C-10）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
