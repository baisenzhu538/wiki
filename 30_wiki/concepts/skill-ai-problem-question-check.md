---
id: skill-ai-problem-question-check
title: "技能：Problem vs Question 区分法"
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论-口述，2026-06-06
source_refs:
  - src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记
wiki_refs:
  - "[[ai-collaboration-mindset-shift]]"
  - "[[ai-landing-scene-selection]]"
related:
  - "[[skill-ai-four-elements-validation]]"
  - "[[ai-landing-scene-selection]]"
  - "[[skill-纪浩-真需求四要素验证法]]"
  - "[[dk-ai-judgment-human-responsibility]]"
definition_of_done:
  - 每次提问前能3秒内分类
  - 分类准确率>80%（自我评估）
  - 能说出"这道题是problem还是question"
tools_required:
  - 无（纯思维工具）
prerequisite_skills: null
created_at: "2026-06-11"
updated_at: "2026-06-17"
tags: []
pipeline:
  - None
reviewed_by: 欧阳锋
author: 纪浩
confidence: 0.75
trust_level: medium
diagnostic_signals:
  - signal: "所有问题都是question，没有真实业务场景"
    lens: "纯学习心态"
    follow_up: "先找一个微型项目，用项目驱动提问。没有problem的question是token浪费"
  - signal: "太纠结分类，反而不敢问，陷入paralysis"
    lens: "分类焦虑"
    follow_up: "设定question预算（最多3个），允许有限的好奇心。分类是为了行动不是为了完美"
  - signal: "把研究问题当成question，忽视研究本身需要产出"
    lens: "研究错配"
    follow_up: "判断标准是是否有交付物而非是否有趣。研究问题也是problem，需要before/after"
  - signal: "完全拒绝question，忽视question是problem的前置任务"
    lens: "前置缺失"
    follow_up: "记录question并关联到具体problem。完全拒绝question会治标不治本"
  - signal: "分类后没有后续行动，problem也停留在认知层面"
    lens: "分类即终点"
    follow_up: "分类只是第一步，problem必须进入四要素验证或立即行动。分类不行动等于没分类"
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

## 快速对照表

| 检查项 | Question（疑问） | Problem（问题） |
|:---|:---|:---|
| 触发点 | "我好奇" | "我疼" |
| 结果要求 | 知道就行 | 必须改变现状 |
| 时间敏感度 | 今天问和明天问没区别 | 今天不解决会有后果 |
| 行动要求 | 不需要做什么 | 需要一个具体动作 |
| 验收标准 | 满足好奇心 | 有 before/after 可验证 |

**一句话判断**：这个问题能不能写出具体的 before/after？
- 能 → 是 problem，继续提问
- 不能 → 是 question，问自己"我真的需要现在知道答案吗？"
- 如果是 question 但很想知道 → 放到"阅读清单"，不占用 AI 工作时间

---

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 准备向AI提问时，任何输入AI之前的3秒检查 |
| ✅ 适合 | 会议中讨论问题，判断是在解决问题还是在兜圈子 |
| ✅ 适合 | 写需求文档前，确认需求是真正的problem不是question伪装 |
| ✅ 适合 | 学习新领域时，区分了解背景（question）和掌握应用（problem） |
| ❌ 不适合 | 纯粹探索性学习 → 目标就是了解，不需要强制区分 |
| ❌ 不适合 | 创意发散阶段 → 过早收敛会扼杀灵感，question阶段是必要的 |
| ❌ 不适合 | 紧急救火场景 → 先灭火，事后复盘时再分类 |
| ❌ 不适合 | 日常闲聊或社交对话 → 不需要每句话都分类 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **纯学习心态** | 所有问题都是question，没有真实业务场景 | 先找一个微型项目，用项目驱动提问。没有problem的question是token浪费 |
| **分类焦虑** | 太纠结分类，反而不敢问，陷入paralysis | 设定question预算（最多3个），允许有限的好奇心。分类是为了行动不是为了完美 |
| **研究错配** | 把研究问题当成question，忽视研究本身需要产出 | 判断标准是是否有交付物而非是否有趣。研究问题也是problem，需要before/after |
| **前置缺失** | 完全拒绝question，忽视question是problem的前置任务 | 记录question并关联到具体problem。完全拒绝question会治标不治本 |
| **分类即终点** | 分类后没有后续行动，problem也停留在认知层面 | 分类只是第一步，problem必须进入四要素验证或立即行动。分类不行动等于没分类 |
| **伪装problem** | 把question包装成problem，逃避行动检验 | 用before/after检验：能不能写出具体的before/after？写不出就是question |
| **过度收敛** | 所有question都被拒绝，扼杀创意和探索 | 设定question时间窗口（如每周1小时），专门用于无目的探索 |
| **AI依赖** | 让AI帮分类，丧失自己的判断力 | 分类是思维训练，必须自己做。AI只能辅助，不能替代判断 |

## 为什么有效

人的大脑有"认知捷径"倾向——看到复杂问题就习惯性地"先了解"。但AI的输出能力放大了这个倾向：AI可以给你无限流畅的"解释"，让你以为自己"懂了"，但行为没有改变。

**区分problem/question的本质是：把"认知消费"转化为"行为生产"。**

---

## 工具/环境

- **工具**：无（纯思维工具）
- **备用方案**：如果无法自我判断，让AI反问"解决这个问题后，你的行为会改变吗？"

---

## 关联技能

- [[skill-ai-four-elements-validation]] — 确认是problem后，用四要素验证是否值得解决
- skill-ai-landing-scene-selection — 选具体场景落地
- [[dk-ai-judgment-human-responsibility]] — 人类负责最终判断，AI只提供信息

---

## 来源

- 纪浩，AI俱乐部-AI协作方法论-口述，2026-06-06
- 原始素材：`00_inbox/纪浩-AI协作方法论-口述.md`

---

## Feedback Path

- `60_feedback/comments/` — 使用此技能后有任何反馈，提交到这里
