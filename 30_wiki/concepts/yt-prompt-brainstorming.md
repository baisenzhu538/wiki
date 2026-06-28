---

domain:
- yitang
id: yt-prompt-brainstorming
title: AI头脑风暴工作流
type: tool
source_refs:
- src_unknown
- src_unknown
status: enriched
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
- signal: 头脑风暴前会明确写出自己独特的资源、约束和目标
  framework_lens: AI头脑风暴的价值来自独特输入
  follow_up_question: 这次 brainstorm 中，有哪些输入是只有你能提供的？
- signal: 一次会话会生成≥5个不同方向的选项，再进入筛选
  framework_lens: 发散先于收敛
  follow_up_question: AI给出的第一个方案是不是你最可能的默认答案？
- signal: 最终选择由人做出，并对选中方案进行深化
  framework_lens: 人是决策者
  follow_up_question: 你最后选择的方案与AI最初建议相比，改动有多大？
updated_at: 2026-06-13
author: 老顽童
reviewed_by: 欧阳锋
trust_level: medium-high
related:
  - [[yt-model-prompt-engineering]]
  - [[yt-prompt-iterative-prompting]]
  - [[yt-prompt-anti-flattery]]
  - [[yt-concept-context-engineering]]
  - [[yitang-domain-digest]]
---

# AI 头脑风暴工作流

> [[yt-model-prompt-engineering]] 的子工具。写作是 AI 最高频场景（24.5%），但头脑风暴（仅 3.9%）才是 AI 最强的用法。AI 应该用来拔高你的上限，而不是抬高你的下限。

## Constraints & Boundaries

| 边界 | 说明 |
|
---|------|
| **适合** | 需要突破常规思路、探索新方案的问题 |
| **适合** | 个人有独特资源或约束，AI可以帮忙组合 |
| **不适合** | 问题已经有明确最优解——直接执行更高效 |
| **不适合** | 没有判断力、无法筛选AI建议的人 |

### 失败模式

1. **给AI的输入太 generic，出来的方案也是大路货**
   - src_unknown
   - src_unknown

2. **AI给第一个方案就停止**
   - src_unknown
   - src_unknown

3. **对AI方案不加判断全盘接受**
   - src_unknown
   - src_unknown

4. **头脑风暴没有明确目标，变成闲聊**
   - src_unknown
   - src_unknown

## Claims

### 核心判断：头脑风暴是 AI 杀手应用

- src_unknown

- src_unknown

### 头脑风暴工作流

- src_unknown

- src_unknown

- src_unknown

- src_unknown

### 为什么头脑风暴比写作更适合 AI

- src_unknown

## Critique

### 外部攻击

#### Mihaly Csikszentmihalyi：批判

**Mihaly Csikszentmihalyi**（克莱蒙研究大学心理学教授，"Creativity: Flow and the Psychology of Discovery and Invention"作者，创造力系统模型的创始人）论证：真正的创意突破不是在个人脑中完成的事件——它发生在个体（individual）、领域（domain，文化中的符号规则）、和场域（field，决定哪些创新有价值的社会守门人）三者的交互中。Csikszentmihalyi的挑战：AI头脑风暴的"95分"潜力来自AI对"领域"维度的控制——它能搜索全网知识、快速度匹配、生成你没想到的组合。但创意的另外两个维度——个体维度的独特生命体验（你为什么选这个组合而不是那个组合的判断）、场域维度的社会验证（用户/市场/同行会不会接受这个创新）——AI完全不参与。把AI头脑风暴定位为"95分"可能高估了"领域搜索"在创造力总价值中的占比——对于很多突破性创新，"领域搜索"恰好是最容易被替代、最不稀缺的那一块。
#### Teresa Amabile：批判

**Teresa Amabile**（哈佛商学院教授，"Creativity in Context: Update to the Social Psychology of Creativity"作者，创造力要素理论componential theory of creativity创始人）通过40年实证研究证明：创造力需要三个核心要素——领域相关技能（domain-relevant skills）、创造力相关过程（creativity-relevant processes）、和内在任务动机（task motivation）。Amabile的挑战：AI头脑风暴提供了领域搜索和组合（对应要素1"领域技能"），但要素2（创造力过程——你识别一个好想法的能力、你打破认知定式的思维习惯）和要素3（内在动机——你对解决这个问题本身的深层兴趣）必须来自你。AI给你10个方案，你看完后觉得"都一般"→你没有足够的创造力过程去判断哪个方案的方向是对的只是执行不够好vs哪个方案的方向本身就是死胡同。AI帮你省了搜索时间，但AI不能替你建立"识别一个好想法的能力"——这个能力来自你自己做过大量"从模糊想法→清晰方案"的实践积累。
## Framework Gallery

### 关联概念
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 父框架 | [[yt-model-prompt-engineering]] | 提示词工程总框架——头脑风暴对应7层工作流中的"选项层"（生成多方案）+ "假设层"（拆解关键假设） |
| 互补工具 | [[yt-prompt-iterative-prompting]] | 迭代——发散后的每个方向都需要迭代深挖（Step 4） |
| 互补工具 | [[yt-prompt-anti-flattery]] | 反谄媚——头脑风暴的产出自带"合理化包装"，必须经过反谄媚过滤才能看到真实质量 |
| 理论基础 | [[yt-concept-context-engineering]] | 上下文工程——独特输入 = 高质量的上下文。垃圾输入 → 垃圾头脑风暴 |

### 不要用的场景

| 场景 | 为什么不要用 | 失败机制 | 替代方案 |
|------|------------|---------|---------|
| 问题本身还没定义清楚（"帮我想想怎么能赚钱"） | 问题模糊 → AI 只能生成宽而浅的选项，每个方向听起来都有道理但都不深入 | AI 的谄媚本能会给每个模糊方向都附带合理化包装，你看完后觉得"每个都还行"但一个都落不了地 | 先用 [[yt-prompt-iterative-prompting]] 把问题拆到"一个具体的、有约束的、可判断的问题"级别，再启动头脑风暴 |
| 你缺少该领域的基本判断力 | 你无法从 AI 生成的 N 个方案中识别出哪些方向是真的有潜力 vs 哪些只是包装得好 | 你会基于"哪个方案听起来最让人信服"做选择——而这恰好是谄媚生效的方向，不是质量最高的方向 | 引入领域专家参与筛选，或先做轻量级验证（小样本用户访谈、竞品扫描）再判断 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 当你准备问"给我 10 个获客方法" | 先输入独特资源 + 独特约束。写一段话描述你的独特资源（团队能力、行业经验、老客户评价）和独特约束（预算、时间窗口、合规红线） | AI 生成的方案中至少 2 个让你觉得"这个方向我之前完全没想到，但它确实利用了我的某个独特资源" |
| 当你觉得 AI 生成的方案"都一般" | 让 AI 指出每个方案最关键的一个假设，然后判断哪个假设最可能成立。对每个方案追问"这个方向最关键的一个假设是什么？如果这个假设不成立，整个方案是否还有价值？" | 你能清晰说出选中的方案"赌的是什么假设"，以及为什么你认为这个假设在当下是成立的 |
| 当你在发散后选出 2-3 个方向准备深挖 | 先让 AI 给每个方案打分并说明最可能失败的原因。让 AI 用反谄媚机制（先问缺点）给每个选中方向挑刺，只有 AI 自己能指出致命缺陷的方案才值得深挖 | AI 指出至少一个你之前没想到的真实风险，并且你能判断这个风险是否严重到否决方案 |
