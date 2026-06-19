---
id: dk-ji-hao-problem-vs-question
title: 暗知识：Problem vs Question —— AI时代大部分人在用AI回答Question而非解决Problem
type: dark-knowledge
dark_knowledge_type: principle
status: enriched
domain:
- ai-collaboration
- yitang
source_person: 纪浩
source_context: AI俱乐部·AI协作方法论分享（2026年）
source_refs:
- 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
created_at: 2026-06-09
updated_at: '2026-06-19'
related:
- '[[case-ji-hao-skill-market-problem-validation]]'
- '[[skill-纪浩-problem-validation-four-checks]]'
wiki_refs:
- '[[case-ji-hao-skill-market-problem-validation]]'
- '[[skill-纪浩-problem-validation-four-checks]]'
pipeline:
- confidence-published
- confidence-source-cited
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 用 AI 做了很多事，但团队或用户感受不到实际改变
  lens: Question 替代 Problem
  follow_up_question: 这件事解决前后，具体场景里的 Before/After 是什么？谁会因为解决而开心？
- signal: 接到需求时第一反应是 AI 能不能做 XX
  lens: 问题定义前置
  follow_up_question: 这个需求是我想知道/试试（Question），还是每次花 X 时间做 Y（Problem）？
- signal: Agent 执行得很顺，但结果没人用
  lens: 伪需求加速
  follow_up_question: 有没有真实受益人和从头讲到尾的因果链？如果中间靠 AI 自己发挥，链是否断裂？
---
# 暗知识：Problem vs Question

## 用一句话讲清楚

AI 时代的大部分人在用 AI 回答 Question（满足好奇心），而非解决 Problem（真实痛点、实际益处、可执行）；当 AI 进入 Agent 时代，真正的价值来自解决有真实锚点和清晰因果链的 Problem。

## 核心洞察

纪浩的原话："大部分人在用 AI 回答 Question 而非解决 Problem。在只能回答 Question 的时代（ChatGPT、DeepSeek），AI 满足好奇心。当 AI 拥有执行能力（Agent 时代），真正的价值在于解决 Problem：真实痛点、实际益处、可执行。"

如果需求是伪需求——没有真实锚点、无人受益、因果链不通——AI 执行得越好，浪费越大。

这个区分的本质是价值上限的差异：**回答 Question 产生知识，解决 Problem 产生改变**。当 AI 能执行时，人的角色必须从"提问者"升级为"问题定义者"：Agent 会忠实执行你让它做的事，问题定义错了，执行越高效越浪费。

这也意味着，AI 时代最稀缺的能力不是"会写 prompt"，而是**能区分 Question 和 Problem**——这个能力和具体 AI 工具无关，和人的判断力有关。

## 边界 / 适用场景

| 场景 | 是否适用 | 说明 |
|---|---|---|
| 评估是否要做某个 AI 工具/Agent | ✅ 适用 | 投入前先确认是 Problem 而非 Question |
| 判断别人提出的"如果有一个 XX 功能就好了" | ✅ 适用 | 区分是好奇心（Question）还是真实痛点（Problem） |
| 评估 AI 项目 ROI | ✅ 适用 | Question 的价值上限是"知道了"，Problem 的价值上限是"改变了" |
| 纯探索性学习、了解新领域 | ❌ 不适用 | 满足好奇心是合法使用，但要明确自己在"探索模式"而非"交付模式" |
| 时间窗口极窄必须立刻下场 | ⚠️ 部分适用 | 至少花 5 分钟做四问法第一问（Before & After） |

## 失败模式 / 常见错觉

| 失败模式 | 常见错觉 | 纠正方式 |
|---|---|---|
| 把"AI 能不能做 XX"当成需求本身 | "功能越全，价值越大" | 回到具体场景：谁、每次花多久、做什么 |
| 用 AI 做了很多产出，但没人觉得被改变 | "信息变多了就是价值" | 明确 Before/After 和真实受益人 |
| 因果链中间有一步"靠 AI 自己发挥" | "AI 够聪明，会自动补上" | 把因果链从头讲到尾，确认每一步可执行 |
| 认为 Problem 必须很大 | "小问题不值得用 AI" | 好的 Problem 可以很小，"每次省 5 分钟"就是好 Problem |

## 行动 Checklist

- [ ] 接到需求时，先问：这是 Question（我想知道/试试）还是 Problem（每次花 X 时间做 Y）？
- [ ] 找到真实场景：把"如果有一个 XX 就好了"转成"我每次都要花 X 时间做 Y"
- [ ] 定义 Before/After：明确现状与理想状态，能量化尽量量化
- [ ] 检查因果链：确认解决方案路径可执行，没有"靠 AI 自己发挥"的断点
- [ ] 用四问法快速验证（详见 [[skill-纪浩-problem-validation-four-checks]]）：
  1. Before & After：解决前后是什么状态？
  2. 真实锚点：具体场景在哪？
  3. 受益人：谁会觉得开心？
  4. 因果链与能力支撑：问题是否可解？

## 相关卡 / 互链

- [[case-ji-hao-skill-market-problem-validation]] — 展示了如何用四问法将模糊需求转化为可验证的真实 Problem。关键转折点是找到了"微信传 zip 的痛点"这个真实场景
- [[skill-纪浩-problem-validation-four-checks]] — 可复制的检查清单，用于快速判断需求是 Question 还是 Problem
- [[case-ji-hao-ui-design-constraint-evolution]] — 纪浩从 Question（"AI 能帮我做 UI 吗？"）转到 Problem（"每次做 UI 花极高成本，怎么把设计规范沉淀为可复用资产？"），最终产出可复用方案
- [[concept-ji-hao-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲
