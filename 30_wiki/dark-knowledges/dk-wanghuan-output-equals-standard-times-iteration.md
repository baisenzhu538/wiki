---

id: dk-wanghuan-output-equals-standard-times-iteration
title: 王欢暗知识：输出质量 = 标准 × 迭代
type: dk
dark_knowledge_type: insight
status: enriched
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
updated_at: '2026-06-20'
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享课后问答（2026-06-18）
source_refs:
- 10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt
- 10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt
related:
  - '[[dk-modeling-ai-judgment-limit]]'
  - '[[dk-wanghuan-ai-lifts-personal-ceiling]]'
  - '[[framework-wanghuan-bitcoe-prompt-framework]]'
  - '[[dk-wanghuan-standard-by-iteration]]'
  - '[[dk-wanghuan-creativity-in-description-and-taste]]'
  - human-ai-collaboration-double-triangle
  - dk-wanghuan-standard-by-iteration
  - framework-wanghuan-actor-director-mode
  - framework-wanghuan-ooda-loop
diagnostic_signals:
- signal: "用户写了很详细的prompt，但只看一版结果"
  framework_lens: 输出=标准×迭代——标准高但迭代少，输出质量不高
  follow_up_question: "你强制至少3轮迭代了吗？每轮迭代都有明确的验收标准吗？"
- signal: "用户反复让AI改，但说不出具体哪里不对"
  framework_lens: 输出=标准×迭代——迭代多但标准不提升，输出质量不高
  follow_up_question: "每轮迭代前，你明确验收标准了吗？标准是否在迭代中提升？"
- signal: "用户说'AI输出总是60-70分'"
  framework_lens: 输出=标准×迭代——检查是标准不够还是迭代不够
  follow_up_question: "你的标准维度有几个？迭代次数是多少？两个乘数哪个更低？"
- signal: "用户迭代20轮还没满意"
  framework_lens: 输出=标准×迭代——迭代成本失控，需要设定终止条件
  follow_up_question: "你设定迭代上限了吗？连续两轮无重大问题就应该终止。"
- signal: "用户团队产出质量参差不齐"
  framework_lens: 输出=标准×迭代——团队需要统一最低迭代次数和验收标准
  follow_up_question: "团队有统一的最低迭代次数和验收标准吗？"
tags:
- 王欢
- 暗知识
- 输出质量
- 标准
- 迭代
- 人机协作
---
# 王欢暗知识：输出质量 = 标准 × 迭代

> **Burn line**: 不要追求一次写对。输出的追踪指标 = 你的标准 × 迭代次数。
>
> **来源**：王欢 AI 实战分享课后问答（2026-06-18）

---

## 一、核心洞察

王欢在课后闲聊中给出一个简洁公式：

```
输出质量 = 标准 × 迭代
```

这意味着：
- **标准越高，单次输出质量越高**；
- **迭代次数越多，最终输出质量越高**；
- **标准低 + 迭代少 = 平庸**；
- **标准高 + 迭代多 = 卓越**。

> 很多人只优化提示词（想一次写对），但忽略了**迭代次数**这个乘数。

---

## 二、为什么这个公式重要

### 2.1 纠正两个误区

| 误区 | 表现 | 正确理解 |
|:---|:---|:---|
| **提示词崇拜** | 花大量时间打磨一个“完美 prompt” | 标准可以在迭代中提升，不必一开始就完美 |
| **一次验收** | AI 出结果后只改一次就结束 | 多轮迭代才是质量杠杆 |

### 2.2 两个变量都可干预

- **标准**：可以通过 BITCOE、AI 业务档案、最佳实践调研来提升。
- **迭代**：可以通过对抗式生成、OODA 闭环、导演式验收来增加。

---

## 三、公式的三层应用

### 3.1 第一层：个人任务

| 标准 | 迭代 | 结果 |
|:---|:---|:---|
| 低（只说“写得好一点”） | 1 次 | 60 分 |
| 中（用 BITCOE 定义） | 3 次 | 80 分 |
| 高（有业务档案 + 最佳实践对照） | 5-8 次 | 90+ 分 |

### 3.2 第二层：团队流程

把“标准 × 迭代”设计成工作流：
- 每个任务默认至少 3 轮迭代；
- 每轮迭代必须有明确的验收标准；
- 高难度任务引入多模型评审，提升标准维度。

### 3.3 第三层：产品系统

把迭代固化成系统能力：
- 版本管理：每次迭代的输入/输出可追溯；
- 反馈闭环：用户反馈自动进入下一轮迭代；
- A/B 测试：多个版本并行迭代，择优上线。

---

## 四、与导演模型的关系

导演的核心工作就是不断提升两个变量：
- **提升标准**：通过定义、约束、示例让 AI 更清楚“好”是什么。
- **增加迭代**：通过验收、反馈、返工让输出逼近标准。

> 导演不是一次把话说清楚，而是**在一次次的“发现不对 → 精确描述 → 要求修改”中把标准磨清楚**。

---

## 五、适用边界

| 适用 | 不适用 |
|:---|:---|
| 创意、设计、内容、方案类任务 | 需要实时响应、单次必须正确的任务 |
| 标准可以逐步清晰的探索性任务 | 有硬性合规、安全红线的任务 |
| 个人或小团队学习期 | 大规模标准化生产（需控制迭代成本） |

---

## 六、常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **只追标准不迭代** | 写了很详细的 prompt，但只看一版结果 | 强制至少 3 轮迭代 |
| **只追迭代不提升标准** | 反复让 AI 改，但说不出具体哪里不对 | 每轮迭代前先明确验收标准 |
| **迭代无记录** | 不知道哪一版比上一版好在哪里 | 建立版本对比和反馈记录 |
| **成本失控** | 迭代 20 轮还没满意 | 设定迭代上限和终止条件 |

---

## 七、Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| AI 输出总是 60-70 分 | 检查是标准不够还是迭代不够 |
| 一个任务反复返工 | 把“不满意”翻译成下一轮的具体标准 |
| 团队产出质量参差不齐 | 统一最低迭代次数和验收标准 |
| 想做出 90+ 分作品 | 同时提升标准维度和迭代次数 |

---

*基于王欢 2026-06-18 AI 实战分享课后问答整理。*
