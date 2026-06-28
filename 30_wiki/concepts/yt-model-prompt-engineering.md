---

id: yt-model-prompt-engineering
title: 人机协作操作系统：提示词工程总框架
type: framework
source_refs:
- 10_raw/sources/一堂-拆书会-吴恩达提示词课程.md
status: enriched
domain:
- src_unknown
- src_unknown
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.9
related:
  - [[yt-model-personal-pitch-toolkit]]
  - [[yt-model-ipo-learning-strategy]]
  - [[yt-panproduct-demand-motivation-resistance]]
  - [[yt-prompt-iterative-prompting]]
  - [[yt-prompt-anti-flattery]]
  - [[yt-prompt-brainstorming]]
  - [[yt-prompt-writing-workflow]]
  - [[yt-concept-ai-guard-brain]]
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-05-13
reviewed_by: 黄药师
estimated_tokens: 2500
pipeline:
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: 停留在技巧层
  follow_up_question: 你的工作中有多少环节已经用AI工作流替代或增强？如果<20%，还停留在技巧层
- framework_lens: 人类判断力缺失
  follow_up_question: 你最近一次对AI输出说了"这个不对，因为..."是什么时候？
updated_at: '2026-06-16'
author: 老顽童
trust_level: medium-high

---

# 人机协作操作系统：提示词工程总框架

> 基于吴恩达《AI Prompting for Everyone》（21节课） × 一堂拆书会第202期深度消化。提示词工程不是"写提示词的技巧"，而是**把 AI 纳入自己工作系统的管理能力**。

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 愿意把AI纳入工作系统 | 有开放心态 |
| ✅ 能保持人类判断 | 不外包思考 |
| ✅ 有具体使用场景 | 能落地 |
| ❌ 完全不想思考 | 大脑外包 |
| ❌ 没有具体工作场景 | 学了用不上 |
| ❌ 期待AI替代一切 | 不现实 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| **"只学技巧"** | 只写prompt | 设计AI工作流 |
| **"人类判断力缺失"** | AI说什么信什么 | 保留最终判断 |
| **"不迭代prompt"** | 一次成型 | 根据输出反馈迭代 |
| **"不看上下文工程"** | 忽视背景信息 | 系统管理上下文 |
## Claims

### 核心范式转换

- src_unknown
- src_unknown

| 旧范式 | 新范式 |
|--------|--------|
| 提示词是咒语，需要学习模板 | 提示词是管理 AI 合伙人的对话，需要迭代 |
| AI 是答案生成机器 | AI 是被校准、追问、约束、反驳的智能伙伴 |
| 好的提示词一次性写出来 | 好的提示词在交互中自然涌现 |
| AI 帮我们省事 | AI 帮我们拔高上限 |
| AI 写作从正文开始 | AI 写作从大纲开始（大纲是杠杆） |

### AI 的四大缺陷（管理对象画像）

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 七层创业者 AI 工作流（核心框架）

- src_unknown

| 层级 | 动作 | 一句话要点 |
|:---:|------|---------|
| 1. 背景层 | 把业务背景、用户、资源、约束、历史尝试、失败原因完整喂给 AI | 没有背景，只能得到通用建议 |
| 2. 选项层 | 要求 AI 生成多个不同方向的方案，不是唯一答案 | 先打开选择空间，再收敛 |
| 3. 假设层 | 要求 AI 说明每个方案依赖的关键假设 | 没有假设拆解，就不知道要验证什么 |
| 4. 反驳层 | 让 AI 扮演客户、竞品、投资人、财务、运营、失败复盘者来质疑 | 没有反驳机制，AI 就是认知泡泡放大器 |
| 5. 标准层 | 制定评分标准，分维度判断 | 没有标准之前，判断只是情绪和偏好 |
| 6. 实验层 | 把结论转化为最小验证行动 | 创业不需要完美答案，需要可验证的行动 |
| 7. 复盘层 | 把实验结果重新喂给 AI，分析、总结、调整下一步 | 完成闭环，AI 才真正进入创业决策系统 |

### 迭代是第一性原理

- src_unknown
- src_unknown

### 模型能力与提示词能力是乘法关系

- src_unknown

## Critique

### 外部攻击

#### Gary Marcus：批判

**Gary Marcus**（NYU，"Rebooting AI"作者）对深度学习/LLM架构局限的持续批评构成对提示词工程"范式转换"叙事的根本挑战。七层AI工作流（背景→选项→假设→反驳→标准→实验→复盘）把AI当作"可以被管理的智能合伙人"，但Marcus会反驳：AI没有合伙人级别的理解——它是在做模式匹配，不是在做推理。当你在"假设层"要求AI"说明每个方案依赖的关键假设"时，AI生成的假设是模仿训练语料中的"假设陈述格式"，而非基于因果推理的真假设。七层工作流可能把随机生成的"听起来像假设的内容"当作分析——而且框架越精密，这种自我欺骗越不容易被察觉。
#### Emily Bender：批判

**Emily Bender**（UW语言学教授，"On the Dangers of Stochastic Parrots"合著者）的"随机鹦鹉"论证是最著名的LLM能力边界声明。Bender论证：LLM是"随机鹦鹉"——它们缝合训练数据中的语言模式，不进行任何意义上的理解或意图推理。提示词工程的"AI合伙人"叙事赋予AI一个它并不具备的心智模型，这可能导致用户过度信任AI输出。Bender会质问七层工作流的"反驳层"：让一个随机鹦鹉扮演"竞品"来反驳你的方案——它生成的"反驳"和真实的竞品威胁之间有多大关系？
## Framework Gallery

### 子组件
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 关联概念
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 互补概念 | [[yt-model-personal-pitch-toolkit]] | 十指讲香：提示词设计和讲香共享底层逻辑——独特输入→迭代打磨→饱满输出。反谄媚机制对应冲突化（制造认知反差打破 AI 的迎合惯性），7层工作流对应场景化+数字化 |
| 互补概念 | [[yt-model-ipo-learning-strategy]] | IPO 学习模型：四遍学习法是强化版输入→处理→输出闭环。AI 时代的学习不是更快而是更深 |
| 互补概念 | [[yt-panproduct-demand-motivation-resistance]] | 动力阻力：AI 对创业者是双刃剑——增强动力（更快出方案）的同时可能增加阻力（过度自信、认知泡泡）。反谄媚机制本质上就是降低 AI 使用中的"阻力" |
| 子框架 | [[yt-prompt-iterative-prompting]] | 迭代提示词——第一性原理的执行工具 |
| 子框架 | [[yt-prompt-anti-flattery]] | 反谄媚——AI 四大缺陷中"谄媚倾向"的系统对策 |
| 子框架 | [[yt-prompt-brainstorming]] | 头脑风暴——最高价值场景的执行工作流 |
| 子框架 | [[yt-prompt-writing-workflow]] | AI 写作——最高频场景的正确工作流 |
| 子框架 | [[yt-concept-ai-guard-brain]] | 守脑如玉——边界条件的系统论述 |
| 子框架 | [[yt-concept-context-engineering]] | 上下文工程——背景层的系统论述 |

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 需要精确事实/数据的决策（如法律、医疗、财务） | LLM本质上是语言模型而非知识库——七层工作流再精密也无法消除幻觉。在法律/医疗/财务决策中用AI工作流替代专业判断可能产生有结构但内容错误的输出 | 用AI辅助检索和草拟，不做最终判断。关键数据/法条/诊断必须通过权威来源（数据库/专家）交叉验证 |
| 对话对象是无法提供高质量反馈的人（如自己也不太懂的领域） | 七层工作流中最关键的是第4层（反驳层）和第7层（复盘层）——让AI扮演客户/竞品/投资人。但如果你自己无法判断AI生成的"反驳"是否合理，这个反驳层只是制造了"有批判性思考"的幻觉 | 在该领域找到≥1个真人专家做反驳者——AI的反驳是训练数据中的模式拼接，真人的反驳基于实际经验。在你不熟悉的领域，AI反驳的质量你判断不了 |
| 极短决策窗口的危机场景（秒-分钟级） | 七层工作流不是为速度设计的——走完背景→选项→假设→反驳→标准→实验→复盘需要的时间远超危机场景的决策窗口 | 用OODA循环（Observe-Orient-Decide-Act, John Boyd）——一个为秒-分钟级决策设计的快速认知循环，追求速度而非完备性 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 开始用AI解决一个复杂问题 | 走"背景层"——先花5-10分钟把所有相关背景喂给AI（不是一句prompt），包括：业务是什么、用户是谁、资源约束、历史尝试了什么、为什么失败了。不喂背景直接提问=接受通用回答 | 背景描述≥200字，含≥3个具体约束条件。AI的回答中引用了至少1个你提供的背景信息（证明它读了你的背景） |
| AI给你一个听起来很对的答案 | 立即启动第4层"反驳层"——让AI扮演竞品/客户/反对者来攻击这个答案，然后扮演你自己来回应攻击。只接受"辩论后的幸存方案" | 至少走完1轮"AI攻击→你或AI回应→AI再攻击→你或AI再回应"的辩论，方案在辩论中至少修改了1处 |
| 用AI做头脑风暴/寻找创意方向 | 走第2层"选项层"——要求AI生成≥5个不同方向的方案，每个方向有自己的逻辑起点。不锁定第一个听起来不错的方向 | 产出≥5个方向不同的选项，每个选项有≥1句话的逻辑起点的描述（不是"选项A做X"而是"选项A的逻辑起点是相信用户会因为Y而做X"） |
| AI辅助做完一个决策或方案后 | 走第7层"复盘层"——把实际执行结果（或决策后的新信息）重新喂给AI，问"基于这些新信息，原始方案中哪些假设被验证了？哪些被推翻了？下一步调整什么？" | 复盘输出至少标注1条"被验证的假设"和1条"被推翻的假设"，并据此产生≥1个下一步调整动作 |
