---
id: skill-ai-problem-question-check
title: "技能：Problem vs Question 区分法"
type: skill
status: draft
domain:
  - AI
  - 决策
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论-口述，2026-06-06
source_refs:
  - src_20260606_42e11f09
wiki_refs:
  - ai-collaboration-mindset-shift
  - ai-landing-scene-selection
definition_of_done:
  - 每次提问前能3秒内分类
  - 分类准确率>80%（自我评估）
  - 能说出"这道题是problem还是question"
tools_required:
  - 无（纯思维工具）
prerequisite_skills: []
related: []
created_at: 2026-06-11
updated_at: 2026-06-11
tags:
  - #domain/AI
  - #method/cognitive-check
  - #tool/brain
pipeline:
  - #skill-type/validation
---

# 技能：Problem vs Question 区分法

> **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
> **核心**：每次向AI提问前，先用3秒判断这是"需要行动改变的问题"还是"满足好奇心的疑问"。

---

## 原始表述
> "question满足好奇心，problem需要行动改变。这是AI时代最重要的认知分水岭。大多数人把question当做problem，结果是大量token浪费在'满足好奇心'上，而没有解决任何真实痛点。"
> —— 纪浩

---

## 操作步骤

### Step 1：提问前强制分类（3秒）
每次向AI输入问题前，先问自己：
- 这个问题解决后，**我的行为会改变吗**？
  - 会 → 这是 **problem**
  - 不会 → 这是 **question**

### Step 2：对 problem 追问四要素
如果是 problem，继续追问：
1. **Before/After**：解决前是什么状态，解决后希望是什么状态？
2. **真实锚点**：在真实世界中有没有具体场景？
3. **受益对象**：谁受益？是我自己、团队、还是客户？
4. **可解性**：我相信这个问题可解吗？有因果链和能力支撑吗？

### Step 3：对 question 做"好奇心预算"
如果是 question，问自己：
- 了解这个问题的答案，**对哪个具体problem有帮助**？
- 如果没有直接帮助，是否值得花token？
- 设定"好奇心预算"：最多3个question，然后必须回到problem。

### Step 4：记录分类（可选）
在笔记中记录当天的分类统计：
```
今日提问：Problem X个 / Question Y个
浪费token的question：_____
```

---

## 适用场景

- ✅ **准备向AI提问时** — 任何输入AI之前的3秒检查
- ✅ **会议中讨论问题时** — 判断讨论是"在解决问题"还是"在兜圈子"
- ✅ **写需求文档前** — 确认需求是真正的problem，不是question的伪装
- ✅ **学习新领域时** — 区分"了解背景"（question）和"掌握应用"（problem）

- ❌ **纯粹探索性学习** — 如果目标就是"了解"，不需要强制区分
- ❌ **创意发散阶段** — 过早收敛会扼杀灵感，question阶段是必要的
- ❌ **紧急救火场景** — 先灭火，事后复盘时再分类

---

## 为什么有效

人的大脑有"认知捷径"倾向——看到复杂问题就习惯性地"先了解"。但AI的输出能力放大了这个倾向：AI可以给你无限流畅的"解释"，让你以为自己"懂了"，但行为没有改变。

**区分problem/question的本质是：把"认知消费"转化为"行为生产"。**

---

## 工具/环境

- **工具**：无（纯思维工具）
- **备用方案**：如果无法自我判断，让AI反问"解决这个问题后，你的行为会改变吗？"

---

## 常见失败模式

| 失败现象 | 原因 | 解决方案 |
|---------|------|---------|
| 所有问题都是question | 没有真实业务场景，纯学习心态 | 先找一个微型项目，用项目驱动提问 |
| 过度区分导致 paralysis | 太纠结分类，反而不敢问 | 设定"question预算"，允许有限的好奇心 |
| 把"研究问题"当成question | 研究问题本身也是problem（需要产出） | 判断标准是"是否有交付物"而非"是否有趣" |
| question是problem的前置任务 | 完全拒绝question会治标不治本 | 记录question，关联到具体problem |

---

## 关联技能

- [[skill-ai-four-elements-validation]] — 确认是problem后，用四要素验证是否值得解决
- [[skill-ai-landing-scene-selection]] — 选具体场景落地
- [[dk-ai-judgment-human-responsibility]] — 人类负责最终判断，AI只提供信息

---

## 来源

- 纪浩，AI俱乐部-AI协作方法论-口述，2026-06-06
- 原始素材：`00_inbox/纪浩-AI协作方法论-口述.md`

---

## Feedback Path

- `60_feedback/comments/` — 使用此技能后有任何反馈，提交到这里
