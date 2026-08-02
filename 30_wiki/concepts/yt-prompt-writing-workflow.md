---
domain:
- yitang
id: yt-prompt-writing-workflow
title: AI写作工作流：大纲→要点→全文
type: tool
aliases:
  - AI写作工作流
  - AI写作工作流：大纲→要点→全文
  - 写作工作流
  - 大纲→要点→全文
source_refs:
- src_unknown
- src_unknown
status: reviewed
version: 1
difficulty: intermediate
confidence: 0.85
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
- signal: 写作前会先磨大纲，并让AI出多版结构供选择
  framework_lens: 大纲有杠杆效应
  follow_up_question: 你的大纲改了之后，整篇文章的论证路径会不会变？
- signal: 大纲确认后逐段展开要点，再扩写为全文
  framework_lens: 分层写作避免空洞
  follow_up_question: 每一段的核心要点是否在你展开前就已经确定？
- signal: AI生成的全文会经过人工加入具体案例、判断和风格调整
  framework_lens: AI出骨架，人出灵魂
  follow_up_question: 你在这篇文章中加入的独家信息占多少比例？
updated_at: 2026-06-13
author: 老顽童
reviewed_by: 欧阳锋
trust_level: medium-high
related:
- '[[yt-model-prompt-engineering]]'
- '[[yt-prompt-brainstorming]]'
- '[[yt-concept-ai-guard-brain]]'
- '[[yt-model-personal-pitch-toolkit]]'
- '[[yitang-domain-digest]]'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# AI 写作工作流：大纲→要点→全文

> [[yt-model-prompt-engineering]] 的子工具。AI 写作最高频（24.5%），但也是最容易出"看起来完整、实际上空洞"的垃圾的地方。正确的流程从大纲开始——大纲有杠杆效应。

## Constraints & Boundaries

| 边界 | 说明 |
|
---|------|
| **适合** | 需要产出结构化长文（文章、报告、课程稿） |
| **适合** | 作者有独特观点和素材，需要提高效率 |
| **不适合** | 没有观点、素材和思考，期望AI出高质量原创内容 |
| **不适合** | 需要强烈个人风格或文学创作的文本 |

### 失败模式

1. **直接让AI写全文，结果空洞通用**
   - src_unknown
   - src_unknown

2. **AI写完后不修改，直接发布**
   - src_unknown
   - src_unknown

3. **大纲太 generic，文章没有差异化**
   - src_unknown
   - src_unknown

4. **过度打磨AI输出，时间成本超过收益**
   - src_unknown
   - src_unknown

## Claims

### 核心问题：AI 写作的最大陷阱

- src_unknown

- src_unknown

### 自上而下构建：大纲→要点→全文

- src_unknown

- src_unknown

- src_unknown

### 自下而上润色：逐段逐句

- src_unknown

- src_unknown

## Critique

### 外部攻击

#### John Warner：批判

**John Warner**（写作教育学教授，"Why They Can't Write: Killing the Five-Paragraph Essay and Other Necessities"和"The Writer's Practice"作者）通过25年写作教学经验论证：写作过程本身就是一个思考过程——不是在写作之前"想清楚"然后"写出来"，而是在"写"的过程中才真正"想清楚"。Warner的挑战：AI写作"大纲→要点→全文"三步法假设"想清楚"和"写出来"是两个可以分离的阶段——你先想好大纲和要点，AI负责填充。但Warner会说：大量关键思考发生在"填充"的过程中——你在把要点变成具体句子的那一刻才发现某个论点的薄弱之处、某个例子的不恰当、两个段落之间缺少了一个你没有预料到的论证桥梁。当你把"展开为全文"外包给AI时，你跳过了"在写作中发生的思考"——你得到了一篇跟大纲逻辑一致的完整文章，但你丢失了"如果我亲自动笔写，我会在写的过程中发现什么问题"这个认知收益。
#### Naomi Baron：批判

**Naomi Baron**（美利坚大学语言学荣休教授，"Who Wrote This? How AI and the Lure of Efficiency Threaten Human Writing"作者）通过研究AI辅助写作的心理效应揭示了：当作者使用AI"填充"自己的大纲和要点时，对文本的ownership（所有权感知）会发生微妙但深刻的转移——从"这是我的文章"逐渐变成"这是我和AI合作的文章"。Baron的挑战：AI写作工作流让你作为"作者"仍然选择大纲和要点——但你不再不确切地知道每一个句子为什么在这里。你选择了大纲A，AI根据大纲生成了段落，你觉得"这段可以"保留了它——但你无法像对自己亲笔写的每一个字那样，说出这个句子的论证功能和"为什么选这个表达而非另一个"。ownership的稀释不是因为你在偷懒——大多数使用这个工作流的人努力工作——而是因为"别人写的句子即使你改了也终究不是你生的"。当你在关键的商业/学术场景中需要为文章中的每一个claim负责时，这种ownership的稀释会在你最脆弱的时候暴露：被问到"这个数据来源你确认过吗？"如果你回答不了因为它来自AI填充而非你的核实。
## Framework Gallery

### 关联概念
- src_unknown
- src_unknown
- src_unknown

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 父框架 | [[yt-model-prompt-engineering]] | 提示词工程总框架——写作是最高频场景，但价值不如头脑风暴高 |
| 互补工具 | [[yt-prompt-brainstorming]] | 头脑风暴——写作和头脑风暴的边界：观点生成用头脑风暴，表达优化用写作工作流。交叉使用是常见错误 |
| 互补概念 | [[yt-concept-ai-guard-brain]] | 守脑如玉——如果你自己不保持写作能力，AI 写作工作流会用着用着让你失去对文字的判断力 |
| 方法关联 | [[yt-model-personal-pitch-toolkit]] | 十指讲香——讲香中的口语化/故事化/金句化等方法可以直接注入 AI 写作的润色环节 |

### 不要用的场景

| 场景 | 为什么不要用 | 失败机制 | 替代方案 |
|------|------------|---------|---------|
| 你还没想清楚要说什么（观点模糊、论据缺失） | AI 写作的前提是你已经想清楚了要说什么——如果连你都不清楚，AI 替你想出来的也是模糊的 | AI 会用自己的"填充本能"补上你缺失的观点和论据，产出一篇"看起来完整但实际上空洞"的文章——你无法为这些 AI 生成的 claim 负责 | 先用 [[yt-prompt-brainstorming]] 把观点和论据想清楚，确认"我到底要说什么"之后再启动写作工作流 |
| 你无法核实 AI 填充的具体例子/数据是否真实 | AI 在"展开为全文"阶段会自行添加例子、数据、引用——这些东西可能看起来合理但是编的 | 文章中不实的例子被读者发现后，整篇文章的信誉崩塌——而且你自己作为"作者"也无法回答"这个数据来源你确认过吗" | 要求 AI 只使用你提供的例子和数据，不要自行"丰富"——或者每收到一个 AI 填充的例子就去核实其真实性 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 当你准备让 AI"写一篇文章" | 先让它出 3 版不同结构的大纲。要求 AI 生成激进版、稳健版、反常规版 3 版大纲，你从中选最合适的并合并各版优点 | 你选中的大纲让你觉得"这个结构本身就已经在论证我的观点了"，而不仅仅是"把内容分成了几段" |
| 当你拿到 AI 生成的全文 | 逐段删除"看起来对但实际没信息量"的句子。逐段读，标记所有读完后你没有新增任何认知的句子，直接删除 | 删除后总字数至少减少 15%，且剩下的每句话都有明确的论证功能 |
| 当你准备润色 | 逐段润色而非全文润色，每段用功能性指令。对每一段明确"这一段的功能是[解释概念/提供证据/反驳异议/制造共鸣]，现在还不够好的地方是[具体问题]，只修改这一段，保持原文风格" | 润色后的段落仍然听起来像你写的——保留了你句长变化、用词偏好和语气特征 |
