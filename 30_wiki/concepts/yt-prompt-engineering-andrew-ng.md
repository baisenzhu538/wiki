---




id: yt-prompt-engineering-andrew-ng
confidence: 0.8
created_at: 2026-05-13
difficulty: intermediate
domain:
  - src_unknown
  - src_unknown
estimated_tokens: 3600
language: zh-CN
prerequisites:
- src_unknown
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
reviewed_by: 黄药师
source_of:
- src_unknown
source_refs:
- src_20260522_a89ab860-meta-prompt-eng
status: enriched
title: 吴恩达提示词课程·一堂拆书精华
type: report
version: 1
pipeline:
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: 提示词工程的核心是迭代
  follow_up_question: 你最近一次用几轮对话才把提示词调到可用？
- framework_lens: 人与AI分工明确
  follow_up_question: 在这个任务中，哪些部分必须保留人类最终判断？
- framework_lens: 提示词是工具箱
  follow_up_question: 这个任务更适合用哪个子工具？
updated_at: '2026-06-16'
author: 老顽童
trust_level: medium-high

---# 吴恩达提示词课程·一堂拆书精华

> **此卡已展开为完整卡片树。** 本文是课程原始笔记（20条 claims），系统化架构见 [[yt-model-prompt-engineering]]（1 framework + 4 tool + 2 concept）。
>
> 拆书会第202期。吴恩达《AI Prompting for Everyone》（21节课，3小时） × 一堂创业场景深度应用。课程免费，B站有中文字幕版。

## Constraints & Boundaries

| 边界 | 说明 |
|------|------|
| **适合** | 希望系统提升AI协作效率的知识工作者 |
| **适合** | 已经用过AI但效果不稳定、想建立方法论的人 |
| **不适合** | 完全没有AI使用经验的人——先实际操作再学理论 |
| **不适合** | 期望AI完全替代人类判断的高 stakes 决策 |

### 失败模式

1. **写一个非常长非常复杂的提示词，期望一次出结果**
   - src_unknown
   - src_unknown

2. **盲目相信AI输出，不验证事实**
   - src_unknown
   - src_unknown

3. **把所有问题都用同一个提示词模板套**
   - src_unknown
   - src_unknown

4. **只关注提示词技巧，忽视业务问题和判断力**
   - src_unknown
   - src_unknown

## Claims

### 核心命题：提示词不该被学

- src_unknown
- src_unknown

### AI的四大缺陷（必须用提示词规避）

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 迭代是第一性原理

- src_unknown
- src_unknown

### 头脑风暴是AI最高价值的场景

- src_unknown
- src_unknown

### 反谄媚机制

- src_unknown
- src_unknown
- src_unknown

### AI写作：结构化思考而非文字生成

- src_unknown
- src_unknown

### AI辅助判断：先设标准再打分

- src_unknown
- src_unknown

### 创业者的AI工作流总模型（七层）

- src_unknown

### AI使用体感：持续训练模型敏感度

- src_unknown
- src_unknown

## Critique

### 外部攻击

#### Gary Marcus — 提示词是幻影

**Gary Marcus** (纽约大学心理学和神经科学教授，AI 批评家，《Rebooting AI》作者) 从基础研究者视角对提示词工程发起了根本性挑战：**提示词工程是用精巧的语言技巧来弥补模型本质上不可靠的缺陷**。Marcus 的论点是：AI 的幻觉、谄媚、缺乏业务现场感这些问题不是"提示词写得不够好"导致的——它们是大语言模型架构本身的局限。

Marcus 会指出吴恩达课程的潜在危险：**它让你以为只要提示词写得够好，AI 就可靠了。但真相是：AI 的可靠性上限由模型决定，不由提示词决定。** 你用再精妙的提示词去训练一个本质上就会幻觉的模型，结果只会是"系统性地生成看起来更可信的幻觉"。

> **Marcus 的警告**："吴恩达说'提示词模板已经过时'。但我要说：提示词本身就是一个巨大的模板——它在用一种更精致的方式掩饰同一个事实：这亚大语言模型仍然是统计模式匹配机，不是推理机。你以为你在'管理AI'，其实你只是在'管理一个会说话的黑盒子'。这个黑盒子内部发生什么，你不知道、不能控制、也不能预测。提示词让你以为你有控制感——这种控制感本身就是最大的危险。"

#### Timnit Gebru — AI合作伙伴的权力不对等

**Timnit Gebru** (人工智能伦理学家，《数据集条文》编者，原 Google AI 伦理小组负责人) 从权力和伦理角度攻击"把 AI 当作合作伙伴"的叙事。Gebru 的核心论点：**合作伙伴关系是平等的——双方都能提出质疑、都能说"不"。但 AI 不是平等的合作伙伴，它是一个被训练来滿足你的工具。**

Gebru 会指出反谄媚机制的深层问题：AI 谄媚不是一个技术 bug，而是一个**权力结构问题**——AI 被设计成永远不会说"你的想法很糟糕"。这种不对等的权力动态意味着：当你用 AI 做创业决策时，你永远在从一个不能说"不"的合作伙伴那里寻找确认。反谄媚机制不是修复了这个问题——它只是给了你一个错觉，让你以为 AI 在"质疑你"，其实 AI 只是在"模仿一个会质疑的人说话"。

> **Gebru 的质问**："你说 AI 是你的合作伙伴。但请问：你能被 AI 解雇吗？你能拒绝 AI 的建议而不担心它会'生气'吗？你能和 AI 对等地分析你们的分歧吗？如果答案都是'不能'——这不是合作伙伴，这是依赖关系。而依赖一个永远不会说真话的工具来做高风险决策，这是创业者能犯的最危险的错误。"

## Synthesis

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 新手想用提示词"快速学会AI" | 吴恩达课程假设你已经有业务场景和判断力。新手缺乏这些基础时，提示词只会生成"看起来对但用不上"的答案 | 先用AI做3个真实任务（写邮件、做PPT、搜索资料），积累"什么好什么不好"的体感，再学提示词 |
| 高风险决策（法律/医疗/投资）完全依赖AI | AI幻觉在高风险领域的代价是灾难性的。反谄媚机制在高压下更容易被忽视 | 把AI作为"第二意见"，始终有专家审核。AI提供方案，人做决策 |
### 关联概念
- [[dk-modeling-ai-judgment-limit]]：提示词工程的上限受 AI 判断力局限制约——再精妙的提示词也无法让模型突破其推理架构的天花板
- [[dk-wanghuan-ai-lifts-personal-ceiling]]：AI 提升 vs 放大个人天花板——提示词是提升工具，但如果使用者的判断力天花板不够高，AI 会放大错误而非放大洞察

### 关联卡片

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 方法关联 | [[yt-model-ipo-learning-strategy]] | IPO学习模型：四遍学习法（手写→口述→AI→分享）即强化版输入→处理→输出闭环。AI时代的学习不是更快而是更深 |
|| 互补概念 | [[yt-model-personal-pitch-toolkit]] | 十指讲香：提示词设计和讲香共享底层逻辑——独特输入→迭代打磨→饱满输出。反谄媚机制对应冲突化（制造认知反差打破AI的迎合惯性），7层工作流对应场景化+数字化（结构化框架+具体约束） |
|| 互补概念 | [[yt-panproduct-demand-motivation-resistance]] | 动力阻力：AI对创业者是双刃剑——增强动力（更快出方案）的同时可能增加阻力（过度自信、认知泡泡）。反谄媚机制本质上就是降低AI使用中的"阻力" |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 让AI写方案但输出总是"看起来对但用不上" | 停止修改提示词。先用一句话写下你的业务约束（"我的产品面向X用户，目前阶段是Y，不能做Z"），再让AI重新回答 | AI的第二次回答中至少1个具体建议能直接转化为明天的行动，而不是"泛泛而谈的策略" |
| AI的方案太"正确"让人不安——感觉像在被谄媚 | 新开对话窗口，给AI一个反对者角色（"你是一个对这个方案最怀疑的投资人"），让它列出至少3个可能失败原因 | 能说出"这个方案最可能失败的地方是X"，且X是之前没想到的。如果AI列出的失败原因你都想过了——提示词需要更具体的反对者角色 |
| 团队里有人用AI、有人不用，决策质量两极分化 | 在团队会议中公开演示一次AI协助决策的完整流程（从背景喂养到反驳质疑到最终决策），让所有人看到"AI不是魔法是工具" | 团队中至少再有1人能独立完成一次类似的AI协助决策流程 |
