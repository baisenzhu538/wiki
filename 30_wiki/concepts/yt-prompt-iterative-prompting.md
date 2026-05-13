---
id: yt-prompt-iterative-prompting
title: 迭代式提示词工作流（5步法）
type: tool
status: enriched
domain:
  - yitang
  - ai
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.90
prerequisites:
  - yt-model-prompt-engineering
component_of:
  - yt-model-prompt-engineering
source_refs:
  - 10_raw/sources/一堂-拆书会-吴恩达提示词课程.md
  - 10_raw/assets/yitang/拆书会第202期-吴恩达AI提示词课程.pdf
query_triggers:
  - 迭代提示词
  - 五步迭代法
  - 提示词迭代
  - 多轮对话
  - AI反馈
  - 连续对话
  - 提示词工作流

tags:
  - '#yitang'
  - '#ai'
  - '#prompt-engineering'
  - '#iteration'
created_at: '2026-05-13'
updated_at: '2026-05-13'
estimated_tokens: 2000
---

# 迭代式提示词工作流（5步法）

> [[yt-model-prompt-engineering]] 的子工具。迭代是提示词工程的第一性原理——好的提示词在对话中自然涌现。

## Claims

### 核心机制：提示词是长出来的，不是设计出来的

- claim:01 [conf=0.90] 好的提示词不是一次性想出来的，是在交互中一轮轮迭代出来的。每次反馈、每次追问、每次修正都等于用新的上下文喂养 AI。这些上下文只属于你一个人，你在任何地方都抄不到
- claim:02 [conf=0.85] 第一轮不要锁定一个答案。生成多个选项（至少 5 个），允许各方向成长。看起来不起眼的方案迭代几轮后可能变靠谱。先发散再收敛

### 五步迭代法

- claim:03 [conf=0.85] **Step 1 — 穷尽已知背景**：不要一上来就问"我需要给你什么信息"——先把你已经想到的写出来。公司阶段、营收利润、团队能力、资源约束、历史尝试、失败原因。写成一段话直接丢给它

- claim:04 [conf=0.85] **Step 2 — 对齐理解**："请先复述你对我的业务背景、关键约束和当前问题的理解。然后告诉我，你还缺少哪些关键信息，才能给出更有针对性的建议。"这一步能及时发现 AI 有没有理解错——如果背景理解已经偏差了，后面的分析越完整越危险

- claim:05 [conf=0.80] **Step 3 — 生成多选项**：要求 AI 一次生成 5 个方案，不要只给 1 个。5 个里面可能有 3 个一看就不行，1 个有局部价值，1 个值得深挖。给每一个有潜力的方向都留成长空间

- claim:06 [conf=0.80] **Step 4 — 诚实反馈**：不要笼统说"这个方案感觉有点飘"——"飘"是你很难定义的词。直接说：成本太高、周期太长、不适合我们的目标客群、缺少转化路径、需要更轻量的版本

- claim:07 [conf=0.85] **Step 5 — 持续迭代**：重复 10 轮、20 轮。一堂拆书会案例：创业者为了跨学科商业难题（需要同时懂化学、品牌、用户心理），跟 AI 连续对话 20 小时，迭代了不知道多少轮，最后 AI 设计出 4 个实验室可验证的实验方案，其中 2 个完全落地。那个问题困扰了团队一个月

### 迭代的底层逻辑

- claim:08 [conf=0.85] 迭代的本质是用新上下文不断校准 AI 的理解。每轮反馈都在缩小 AI 的"理解偏差"——从通用知识逐渐聚焦到你的独特约束。提示词的质量 = 迭代轮数 × 每轮反馈的信息密度

## Constraints & Boundaries

- claim:boundary-01 [conf=0.85] 迭代不是无限循环。当连续 3 轮 AI 的改进都是微调措辞而非实质变化时，说明当前模型能力已达到天花板——此时换更强模型比继续迭代更有效。判断标准：看改进是"信息增量"还是"文字重组"

- claim:boundary-02 [conf=0.80] 迭代的前提是你自己清楚"什么是更好的答案"。如果你对问题本身没有判断力，迭代会变成 AI 带着你兜圈子——你无法给出有效反馈，AI 无法收敛。症状：每轮 AI 都给你新方向，但你觉得每个都有点道理、每个都无法深入。对策：先把问题拆解到你可以判断的子问题级别

## Framework Gallery

### 关联概念
- [[yt-model-prompt-engineering]] — 父框架：提示词工程总框架
- [[yt-prompt-anti-flattery]] — 反谄媚：迭代中最关键的校准机制
- [[yt-prompt-brainstorming]] — 头脑风暴：Step 3 的详细展开
- [[yt-concept-context-engineering]] — 上下文工程：Step 1 的理论基础

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 父框架 | [[yt-model-prompt-engineering]] | 提示词工程总框架——迭代是7层工作流中背景层→选项层→假设层→反驳层→标准层→实验层→复盘层的驱动引擎 |
| 互补工具 | [[yt-prompt-anti-flattery]] | 反谄媚——迭代中每轮反馈必须经过反谄媚过滤，否则 AI 的迎合倾向会让迭代变成互相吹捧 |
| 互补工具 | [[yt-prompt-brainstorming]] | 头脑风暴——Step 3"生成多选项"的执行细节 |
| 理论基础 | [[yt-concept-context-engineering]] | 上下文工程——为什么 Step 1 和 Step 2 的顺序不能颠倒 |
