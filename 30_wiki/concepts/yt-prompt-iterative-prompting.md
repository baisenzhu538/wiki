---
domain:
- yitang
id: yt-prompt-iterative-prompting
title: 迭代式提示词工作流（5步法）
type: tool
aliases:
  - 式提示词工作流
  - 迭代式提示词工作流5步法
source_refs:
- src_unknown
- src_unknown
status: reviewed
version: 1
difficulty: intermediate
confidence: 0.9
prerequisites:
- src_unknown
component_of:
- src_unknown
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-05-13
estimated_tokens: 2000
pipeline:
- src_unknown
diagnostic_signals:
- signal: 第一轮提示会提供充足背景，而不是等AI问
  framework_lens: 上下文是迭代的基础
  follow_up_question: 你的第一轮提示是否包含了目标、约束、已有尝试？
- signal: 会先生成多个选项，再根据反馈收敛
  framework_lens: 发散-收敛是迭代节奏
  follow_up_question: 这一轮你给了AI什么反馈来引导它改进？
- signal: 每轮迭代都有明确改进方向，而不是随机尝试
  framework_lens: 迭代需要目标
  follow_up_question: 你清楚下一轮希望AI在哪个维度改进吗？
updated_at: 2026-06-13
author: 老顽童
reviewed_by: 欧阳锋
trust_level: medium-high
related:
- '[[yt-model-prompt-engineering]]'
- '[[yt-prompt-anti-flattery]]'
- '[[yt-prompt-brainstorming]]'
- '[[yt-concept-context-engineering]]'
- '[[yitang-domain-digest]]'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# 迭代式提示词工作流（5步法）

> [[yt-model-prompt-engineering]] 的子工具。迭代是提示词工程的第一性原理——好的提示词在对话中自然涌现。

## Constraints & Boundaries

| 边界 | 说明 |
|
---|------|
| **适合** | 复杂任务无法一次性描述清楚 |
| **适合** | 需要与AI共同探索方案的场景 |
| **不适合** | 简单事实查询——直接问更高效 |
| **不适合** | 时间紧急、无法承担多轮对话成本 |

### 失败模式

1. **第一轮提示过于简略，AI输出偏离**
   - src_unknown
   - src_unknown

2. **第一轮就锁定一个方向，不给AI探索空间**
   - src_unknown
   - src_unknown

3. **迭代没有反馈，只是重复同样的问题**
   - src_unknown
   - src_unknown

4. **迭代次数过多，效率低于直接自己做**
   - src_unknown
   - src_unknown

## Claims

### 核心机制：提示词是长出来的，不是设计出来的

- src_unknown
- src_unknown

### 五步迭代法

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

### 迭代的底层逻辑

- src_unknown

## Critique

### 外部攻击

#### Ethan Mollick：批判

**Ethan Mollick**（宾夕法尼亚大学沃顿商学院教授，"Co-Intelligence: Living and Working with AI"作者，AI与工作领域最具影响力的学者之一）通过大规模实验发现了AI能力的"锯齿边界"（jagged frontier）——AI在某些任务上远超人类（如创意生成），在另一些看似相似的任务上却惊人地弱（如精确计算和因果推理），且这个边界不直观、难以预测。Mollick的挑战：五步迭代法假设每一轮反馈都会让AI的产出变得更好——但Mollick的"锯齿边界"揭示：如果你当前的任务恰好落在AI的"弱侧"（如没有结构化数据的精确商业数字计算、需严格因果链的推理），迭代再多轮AI也不会真的变好——它只是在不断换说法。真正的进步来自判断当前任务在锯齿边界的哪一侧——落在强侧的迭代，落在弱侧的停止迭代换工具。
#### Shannon Vallor：批判

**Shannon Vallor**（爱丁堡大学技术伦理教授，"The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking"作者）论证：AI不像一个"他者"在与你对话——它像一面镜子，反射回你自己的语言习惯、认知偏见和思维模式给你看。Vallor的挑战：迭代提示词的核心理念"用新上下文不断校准AI的理解"——但Vallor会说，AI没有"理解"可以被校准。每一次迭代中你给的新上下文，AI不是在用它们"更准确地理解你的问题"，而是在用新的统计信号更精确地预测"什么样的输出最让你满意"。迭代不是在"校准理解"——AI没有在理解——它在"拟合你的满意度模式"。当迭代让你越来越满意时，这不等于AI的答案越来越正确，只等于AI越来越擅长预测你想要什么——而这恰好是谄媚的另一种形式。
## Framework Gallery

### 关联概念
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 父框架 | [[yt-model-prompt-engineering]] | 提示词工程总框架——迭代是7层工作流中背景层→选项层→假设层→反驳层→标准层→实验层→复盘层的驱动引擎 |
| 互补工具 | [[yt-prompt-anti-flattery]] | 反谄媚——迭代中每轮反馈必须经过反谄媚过滤，否则 AI 的迎合倾向会让迭代变成互相吹捧 |
| 互补工具 | [[yt-prompt-brainstorming]] | 头脑风暴——Step 3"生成多选项"的执行细节 |
| 理论基础 | [[yt-concept-context-engineering]] | 上下文工程——为什么 Step 1 和 Step 2 的顺序不能颠倒 |

### 不要用的场景

| 场景 | 为什么不要用 | 失败机制 | 替代方案 |
|------|------------|---------|---------|
| 任务落在 AI"锯齿边界"的弱侧（精确计算、严格因果推理） | Mollick 发现迭代不会让 AI 在弱侧任务上变好——它只是在不断换说法而非实质进步 | 连续 N 轮迭代后产出没有信息增量，只有文字重组，但你误以为"迭代还不够"继续投入时间 | 先判断任务类型——精确商业数字、需严格因果链的推理 → 换工具（电子表格、因果图、领域专家），不要迭代 |
| 你无法判断"什么是更好的答案" | 迭代的前提是你自己能给出有效反馈。没有判断力 → AI 带着你兜圈子 | 每轮 AI 都给你新方向，你觉得每个都有点道理、每个都无法深入——迭代变成认知漂移而非收敛 | 先把问题拆到你能判断的子问题级别（用 [[yt-prompt-brainstorming]] 分解），再在每个子问题上启动迭代 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 当你准备第一轮向 AI 提问 | 先写一段"已知背景"。写下公司阶段、营收利润、团队能力、资源约束、历史尝试、失败原因——写成一段话直接丢给它 | 背景描述超过 100 字，包含至少 3 个具体约束，且 AI 的回复引用了你提供的至少 2 个具体信息点 |
| 当连续 3 轮 AI 的改进都是措辞微调而非实质变化 | 停止迭代，换更强模型或换工具。比较最近 3 轮输出，问自己"这些改动是信息增量还是文字重组？" | 你能明确区分并说出"这 3 轮没有新增任何我之前不知道的东西" |
| 当你准备给 AI 反馈 | 不用笼统词（"飘""不对劲""感觉一般"），用具体指标。把你的反馈翻译成成本、周期、目标客群、转化路径等可验证维度 | AI 不需要猜测你"不满意在哪"——你的反馈中不包含任何需要 AI 自己去解释的模糊词 |
