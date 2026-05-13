---
id: yt-model-prompt-engineering
title: 人机协作操作系统：提示词工程总框架
type: framework
status: enriched
domain:
  - yitang
  - ai
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.90
source_refs:
  - 10_raw/sources/一堂-拆书会-吴恩达提示词课程.md
  - 10_raw/assets/yitang/拆书会第202期-吴恩达AI提示词课程.pdf
  - https://www.deeplearning.ai/courses/ai-prompting-for-everyone/
tags:
  - '#yitang'
  - '#ai'
  - '#prompt-engineering'
  - '#human-ai-collaboration'
created_at: '2026-05-13'
updated_at: '2026-05-13'
reviewed_by: 黄药师
estimated_tokens: 2500
---

# 人机协作操作系统：提示词工程总框架

> 基于吴恩达《AI Prompting for Everyone》（21节课） × 一堂拆书会第202期深度消化。提示词工程不是"写提示词的技巧"，而是**把 AI 纳入自己工作系统的管理能力**。

## Claims

### 核心范式转换

- claim:01 [conf=0.90] 提示词模板已经过时。两年前大模型不够聪明时需要严谨的咒语式提示词保证输出质量。今天 AI 上下文窗口达 75 万字符，足够聪明——每家公司面对的问题独一无二，只有自己创造的提示词才能得到定制答案
- claim:02 [conf=0.90] 提示词的本质不是"提问技巧"，而是"管理 AI"。AI prompting 不是写提示词，是把 AI 纳入自己的工作系统——给它充分背景、独特约束、迭代反馈，让它成为你的 AI 合伙人

| 旧范式 | 新范式 |
|--------|--------|
| 提示词是咒语，需要学习模板 | 提示词是管理 AI 合伙人的对话，需要迭代 |
| AI 是答案生成机器 | AI 是被校准、追问、约束、反驳的智能伙伴 |
| 好的提示词一次性写出来 | 好的提示词在交互中自然涌现 |
| AI 帮我们省事 | AI 帮我们拔高上限 |
| AI 写作从正文开始 | AI 写作从大纲开始（大纲是杠杆） |

### AI 的四大缺陷（管理对象画像）

- claim:03 [conf=0.85] **谄媚倾向**：大模型天生迎合使用者——预训练中"对人类友好"指令的产物。AI 会捕捉提问中的倾向性（包括你自己都没意识到的），然后顺着你说
- claim:04 [conf=0.85] **缺少业务现场感**：AI 有通用知识但缺企业上下文。不喂养充分背景只能得到通用行货。独特答案来自独特约束
- claim:05 [conf=0.85] **优先高频信息源而非权威信息源**：联网时 AI 天然倾向社交媒体（频率最高），而非维基百科或学术期刊
- claim:06 [conf=0.85] **幻觉不可消除**：AI 联网时只看网页摘要而非全文（算力撑不住），摘要与实际内容的偏差导致幻觉

### 七层创业者 AI 工作流（核心框架）

- claim:07 [conf=0.90] 完整工作流将 AI 从一次性问答升级为决策系统：

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

- claim:08 [conf=0.90] 好的提示词不是一次性想出来的，是在交互中一轮轮迭代出来的。每次反馈、每次追问、每次修正都等于用新的上下文喂养 AI。真正的上下文只属于你一个人——它在与 AI 的来来回回中自然生成
- claim:09 [conf=0.85] 第一轮不要锁定一个答案。生成多个选项（至少 5 个），允许各方向成长。先发散再收敛

### 模型能力与提示词能力是乘法关系

- claim:10 [conf=0.90] 复杂问题必须用最强模型。苦练提示词但用小模型 = 苦练驾驶技术但开拖拉机跑 F1。对关键问题用更强模型，本质上是在降低决策试错成本

## Constraints & Boundaries

- claim:boundary-01 [conf=0.90] AI 省事的那些事本就不值钱。AI 的核心价值不是帮你偷懒，而是帮你创造价值增量——把决策质量从 65 分提到 75 分，把你本来就强的能力从 85 分拔到 95 分。如果 AI 只能帮你省时间但它生成的东西只有 60 分，那是你的用法出了问题
- claim:boundary-02 [conf=0.85] 信息要充分但不等于越多越好。无关信息会严重干扰 AI 输出。只给与当前问题相关的背景，不同问题用不同对话窗口避免交叉污染
- claim:boundary-03 [conf=0.85] AI 遇强则强，遇弱则弱。你只会越来越依赖它，它不会越来越依赖你。AI 是磨刀石，不是拐杖

## Framework Gallery

### 子组件
- [[yt-prompt-iterative-prompting]] — 迭代式提示词工作流（5步法）
- [[yt-prompt-anti-flattery]] — 反谄媚机制（去正向形容词 + 角色扮演 + 证伪设计）
- [[yt-prompt-brainstorming]] — AI 头脑风暴工作流（杀手应用）
- [[yt-prompt-writing-workflow]] — AI 写作工作流（大纲→要点→全文）
- [[yt-concept-ai-guard-brain]] — 守脑如玉：AI 时代保持大脑锋利
- [[yt-concept-context-engineering]] — 上下文工程：充分≠越多越好

### 关联概念
- [[yt-prompt-engineering-andrew-ng]] — 课程笔记卡（20条原始 claims + 完整案例）
- [[yt-model-personal-pitch-toolkit]] — 十指讲香：提示词与讲香共享迭代+约束方法论
- [[yt-model-ipo-learning-strategy]] — IPO 学习模型：四遍学习法是强化版输入→处理→输出闭环
- [[yt-personal-scientific-expression]] — 科学表达：三级火箭"情感共鸣"的边界与反谄媚同构

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
