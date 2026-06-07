---
id: "dk-纪浩-newbie-can-validate"
title: "暗知识：新手也可以用四要素验证——因为验证用的是工具，不是眼光"
type: "dark-knowledge"
dark_knowledge_type: "insight"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享——四要素验证法的补充说明"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/not-for-beginners"
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/ai-collaboration"
  - "#scene/ai-collaboration/problem-validation"
  - "#scene/hardware-debugging/prototyping"
  - "#source_type/dark-knowledge"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "concept-纪浩-ai-collaboration-methodology"
  - "skill-纪浩-four-elements-validation"
---

# 暗知识：新手也可以用四要素验证

## 原始表述

> 纪浩讲完四要素后自己反问："我们都是新手，我们的眼光也没有专家独到，这一点做不好怎么办？" 然后他自己回答："其实我们可以在课里找一些方法——我们可以去假设、可以做调研、可以做访谈、可以问 AI、也可以做实验。"

## 使用场景

- 你是新手，不确定自己的判断是否准确
- 你面对一个想法，不确定是"真需求"还是"兴奋的幻想"
- 你担心"四要素验证需要专家眼光才能判断"

## 操作方法

**五种新手验证工具**：

1. **假设**：先假设一个 Before-After，不要求准确——"我猜现在的问题是 X，解决后是 Y"。带着假设去找证据
2. **调研**：搜一下有没有人做过类似的事。结果如何？为什么不做了？
3. **访谈**：找 3-5 个目标用户问——"如果你有这个，你会用吗？你现在怎么解决的？"
4. **问 AI**：让 AI 帮你分析因果链——"如果我要解决 X，需要哪些条件？哪些我目前不具备？"
5. **做实验**：最小成本做一个原型（甚至不需要代码——一个截图、一段描述都可以），给人看反应

**关键心态**：你不是在"用专家眼光判断"，你是在"用工具收集证据"。证据够了就是够了，不够就是不够——不需要天才也能判断。

## 适用边界

- 适用于有具体目标用户或使用场景的问题
- 不适用于"没有人知道答案"的前沿研究——这时没有访谈对象，实验代价极高
- 验证工具的质量取决于你找的人/数据——如果访谈了 5 个错误的人，结论也是错的

## 为什么值钱

讲"要深度思考"、"要有判断力"的人很多——但这对新手是废话。新手没有判断力。

纪浩的价值在于他说了实话：**新手不需要判断力，需要的是验证工具。** 你不是在"判断这个需求真不真"，你是在"用这五个工具收集证据，看证据够不够"。

这个区别不是语义游戏——它是"这事只有专家能做"和"这事新手也能做"的分界线。前者让新手觉得"我够不到"，后者让新手觉得"我能开始"。

KDO 的 lint 规则就是这个哲学的基础设施化——不是让 Builder 自己判断"这里有没有 typo"，而是让一个自动工具去收集证据。新手 Builder（任何一个第一天用 KDO 的人）不需要有黄药师的眼光——lint 规则替他做了验证。
