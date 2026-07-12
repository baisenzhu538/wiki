---

id: dk-ji-hao-problem-vs-question
title: 暗知识：Problem vs Question —— AI时代大部分人在用AI回答Question而非解决Problem
type: dk
dark_knowledge_type: principle
status: reviewed
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
  - "[[yt-demand-fake-demand-detection]]"
  - "[[dk-ai-judgment-human-responsibility]]"
  - "[[dk-wanghuan-spec-trap]]"
  - "[[yt-five-step-method]]"
  - "[[dk-tool-as-phased-validator]]"
  - "[[ai-collaboration-domain-digest]]"
  - "[[yitang-domain-digest]]"
wiki_refs:

pipeline:

author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  lens: Question 替代 Problem
  follow_up_question: 这件事解决前后，具体场景里的 Before/After 是什么？谁会因为解决而开心？
- signal: src_unknown
  lens: 问题定义前置
  follow_up_question: 这个需求是我想知道/试试（Question），还是每次花 X 时间做 Y（Problem）？
- signal: src_unknown
  lens: 伪需求加速
  follow_up_question: 有没有真实受益人和从头讲到尾的因果链？如果中间靠 AI 自己发挥，链是否断裂？

---

# 暗知识：Problem vs Question

## 原始表述

AI 时代的大部分人在用 AI 回答 Question（满足好奇心），而非解决 Problem（真实痛点、实际益处、可执行）；当 AI 进入 Agent 时代，真正的价值来自解决有真实锚点和清晰因果链的 Problem。

纪浩的原话："大部分人在用 AI 回答 Question 而非解决 Problem。在只能回答 Question 的时代（ChatGPT、DeepSeek），AI 满足好奇心。当 AI 拥有执行能力（Agent 时代），真正的价值在于解决 Problem：真实痛点、实际益处、可执行。"

如果需求是伪需求——没有真实锚点、无人受益、因果链不通——AI 执行得越好，浪费越大。

## 使用场景

- **评估 AI 工具/Agent 投入**：投入前先确认是 Problem 而非 Question
- **判断功能需求真伪**：区分"如果有一个 XX 功能就好了"是好奇心还是真实痛点
- **评估 AI 项目 ROI**：Question 的价值上限是"知道了"，Problem 的价值上限是"改变了"
- **团队需求评审**：用四问法过滤伪需求，避免资源浪费
- **个人 AI 使用**：明确自己在"探索模式"还是"交付模式"

## 操作方法

1. **四问法区分 Question 和 Problem**：
   - Before & After：解决前后是什么状态？
   - 真实锚点：具体场景在哪？
   - 受益人：谁会觉得开心？
   - 因果链与能力支撑：问题是否可解？
2. **Question 的特征**：
   - 满足好奇心，想知道/试试
   - 没有真实受益人
   - 因果链断裂或靠 AI 自己发挥
3. **Problem 的特征**：
   - 真实痛点，每次花 X 时间做 Y
   - 有明确 Before/After
   - 因果链从头到尾可执行
4. **价值上限判断**：
   - Question：价值上限是"知道了"
   - Problem：价值上限是"改变了"

## 适用边界

| 场景 | 是否适用 | 说明 |
|:
|:---|:---|
| 评估是否要做某个 AI 工具/Agent | ✅ 适用 | 投入前先确认是 Problem 而非 Question |
| 判断别人提出的"如果有一个 XX 功能就好了" | ✅ 适用 | 区分是好奇心（Question）还是真实痛点（Problem） |
| 评估 AI 项目 ROI | ✅ 适用 | Question 的价值上限是"知道了"，Problem 的价值上限是"改变了" |
| 纯探索性学习、了解新领域 | ❌ 不适用 | 满足好奇心是合法使用，但要明确自己在"探索模式"而非"交付模式" |
| 时间窗口极窄必须立刻下场 | ⚠️ 部分适用 | 至少花 5 分钟做四问法第一问（Before & After） |

## 为什么值钱

1. **防止伪需求加速**：AI 执行得越好，伪需求浪费越大，区分能力是底线
2. **价值上限差异**：回答 Question 产生知识，解决 Problem 产生改变
3. **Agent 时代必备**：Agent 会忠实执行你让它做的事，问题定义错了执行越高效越浪费
4. **判断力稀缺**：区分 Question 和 Problem 的能力和具体 AI 工具无关，和人的判断力有关

## 与其他知识的关联

- [[yt-demand-fake-demand-detection]]——伪需求识别，Question 可能是伪需求
- [[dk-ai-judgment-human-responsibility]]——人做判断 AI 做生产，问题定义是判断
- [[dk-wanghuan-spec-trap]]——王欢 Spec 陷阱，方向定义的重要性
- [[yt-five-step-method]]——一堂五步法，系统化问题定义框架
- [[dk-tool-as-phased-validator]]——分阶段校验器，问题验证方法

---

## 失败模式 / 常见走偏

| 失败模式 | 常见错觉 | 纠正方式 |
|:---|:---|:---|
| 把"AI 能不能做 XX"当成需求本身 | "功能越全，价值越大" | 回到具体场景：谁、每次花多久、做什么 |
| 用 AI 做了很多产出，但没人觉得被改变 | "信息变多了就是价值" | 明确 Before/After 和真实受益人 |
| 因果链中间有一步"靠 AI 自己发挥" | "AI 够聪明，会自动补上" | 把因果链从头讲到尾，确认每一步可执行 |
| 认为 Problem 必须很大 | "小问题不值得用 AI" | 好的 Problem 可以很小，"每次省 5 分钟"就是好 Problem |
