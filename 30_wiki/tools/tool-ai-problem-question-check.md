---
id: tool-ai-problem-question-check
title: 技能：Problem vs Question 区分法
type: tool
status: reviewed
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论-口述，2026-06-06
source_refs:
- 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md
wiki_refs:
- src_unknown
- src_unknown
related:
- "[[yt-note-problem-solving-capability]]"
- "[[tool-纪浩-problem-validation-four-checks]]"
- "[[yt-model-scientific-questioning-map]]"
- "[[yt-model-questioning-practice-canvas]]"
- "[[tool-纪浩-Problem与Question区分法]]"
- "[[tool-strategy-nine-problems]]"
- "[[framework-问题边界与Problem澄清五层结构]]"
- "[[dk-yitang-research-question-quality]]"
- "[[case-ji-hao-skill-market-problem-validation]]"
- "[[tool-纪浩-Agent技能市场设计法]]"
- "[[dk-ji-hao-problem-vs-question]]"
- "[[tool-一堂-kernel-three-questions]]"
- "[[sk-ai-problem-validation]]"
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
prerequisite_skills: null
created_at: '2026-06-11'
updated_at: '2026-06-17'
tags: []
pipeline:
- src_unknown
reviewed_by: 欧阳锋
author: 纪浩
confidence: 0.75
trust_level: medium
diagnostic_signals:
- lens: 纯学习心态
  follow_up: 先找一个微型项目，用项目驱动提问。没有problem的question是token浪费
- lens: 分类焦虑
  follow_up: 设定question预算（最多3个），允许有限的好奇心。分类是为了行动不是为了完美
- lens: 研究错配
  follow_up: 判断标准是是否有交付物而非是否有趣。研究问题也是problem，需要before/after
- lens: 前置缺失
  follow_up: 记录question并关联到具体problem。完全拒绝question会治标不治本
- lens: 分类即终点
  follow_up: 分类只是第一步，problem必须进入四要素验证或立即行动。分类不行动等于没分类
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
- src_unknown
  - src_unknown
  - src_unknown

### Step 2：对 problem 追问四要素
如果是 problem，继续追问：
1. **Before/After**：解决前是什么状态，解决后希望是什么状态？
2. **真实锚点**：在真实世界中有没有具体场景？
3. **受益对象**：谁受益？是我自己、团队、还是客户？
4. **可解性**：我相信这个问题可解吗？有因果链和能力支撑吗？

### Step 3：对 question 做"好奇心预算"
如果是 question，问自己：
- src_unknown
- src_unknown
- src_unknown

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
- src_unknown
- src_unknown
- src_unknown

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

#| 模式 | 症状 | 修复 |
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

- src_unknown
- src_unknown

---

## 关联技能

- src_unknown
- src_unknown
- src_unknown

---

## 来源

- src_unknown
- src_unknown

---

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"question 和 problem 可以通过 before/after 可验收性干净区分"，但实际中存在大量中间态——一个问题可能今天只是好奇心（question），但明天就演变成必须解决的痛点（problem），界限是动态的。
- **边界**：在纯探索性学习场景中，强制分类会扼杀好奇心驱动的发现；在紧急救火场景中，3 秒分类本身就是在浪费时间。
- **反例**：许多突破性创新（如青霉素的发现）恰恰源于"没有 problem 驱动的 question"——弗莱明只是好奇为什么培养皿长了霉菌，如果当时用 before/after 框架判断，这个问题会被归为 question 而被丢弃。

**David Allen**（GTD 时间管理方法论创始人）会质疑：把问题分为 question/problem 两类本身就制造了虚假的二元对立。GTD 的核心是"清空大脑、信任系统"——所有输入（无论 question 还是 problem）都应被捕获并进入统一处理流，而不是在入口处就做分类筛选。分类焦虑本身就是一种认知负担。
