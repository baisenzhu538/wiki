---
id: "dk-modeling-ai-self-retrospection"
title: "AI 也会重复犯同样的错：每次漂亮交付后，必须让它当场总结一个自查清单"
type: "dark-knowledge"
dark_knowledge_type: "workflow"
status: "draft"
domain:
  - "yitang"
  - "ai-saas"
source_person: "Truman"
source_context: "一堂建模能力培训（AI 辅助建模案例），2026-06-12"
source_refs:
  - "src_20260614_8269ccdb"
  - "src_20260614_42f1e977"
created_at: "2026-06-14"
updated_at: "2026-06-14"
related:
  - "modeling-capability-for-kdo"
  - "modeling-capability-system"
  - "dk-modeling-ai-without-judgment"
  - "ai-collaboration"
tags:
  - "#source_type/process"
  - "#domain/yitang"
  - "#domain/ai-saas"
  - "#method/ai-collaboration"
  - "#method/retrospective"
trust_level: "high"
reviewed_by: "老顽童"
review_date: "2026-06-14"
---

# AI 也会重复犯同样的错：每次漂亮交付后，必须让它当场总结一个自查清单

## 原始表述

> 我最近建议所有一堂的同学要尝试养成一个习惯：让 AI 学会自己复盘自己。不是 AI 帮助人复盘，而是它帮助自己复盘。你做了一个工作，做得很漂亮，过去人要总结这个经验是非常难的，ROI 很低。现在你要习惯性地让 AI 当场立刻就总结一个自查清单，把这一次的经验自动化地变成下一次的基础。这个工作其实还挺重要的。比如我当时跟好几个平台去做课程插图和 PPT，过程中不断纠偏：这个图颜色不对、这个图流程不对、这个图缺了个什么东西。交完活之后，我让一个 agent 扫描所有对话窗口，把所有反馈合并同类项，封装了一个叫 Design Taste 的技能。下一次再做的时候，它会基于这个再去做，明显聪明很多。AI 自己干活，AI 自己复盘，AI 下次自己吸收，这个循环会越来越快。

## 使用场景

- 你和 AI 反复掰扯一个任务，终于把它做对了。
- 你发现 AI 在不同 session 里重复犯同样的风格/格式/逻辑错误。
- 你有一套内部审美/标准，想固化成 AI 可复用的检查清单。
- 你在用 AI 做设计、写文案、拆里程碑、生成代码、整理模型。
- 你想把一次成功交付变成可复用的 skill/partner/prompt。

## 操作方法

1. **只在“漂亮交付”后做**
   复盘的对象必须是一次你满意的输出。失败的交付也能复盘，但优先把成功经验固化。

2. **当场立刻做**
   在对话上下文还热乎的时候做，不要等几天。因为：
   - 记忆会衰减
   - 原始 prompt、中间版本、纠偏记录可能散落在多个窗口
   - 有些反馈是口头/临时发的，错过窗口就找不回来

3. **指定扫描范围**
   让 AI 扫描：
   - 本次对话的全部历史
   - 同一任务的其他 parallel session
   - 相关参考文件/数据库（如 Cubox、飞书文档、本地知识库）
   明确关键词，避免扫进无关内容。

4. **强制输出一个自查清单**
   不要让它泛泛总结“要注意设计”。要让它输出：
   - 10 条 To Do（必须做）
   - 10 条 Not To Do（不能做）
   - 按 P0/P1/P2 分级
   - 每条背后标注来源：哪一次反馈催生了这条规则

5. **封装成可复用资产**
   把清单变成：
   - 一个 skill 文件（`40_outputs/capabilities/skills/`）
   - 一个 system prompt 片段
   - 一个 eval case
   下次同类任务先加载这个资产。

6. **下次任务先自查**
   交付前让 AI 用上次总结的技能给自己打分，而不是等人来喷。

## 适用边界

- **适用于有规律、可重复的任务**。创意一次性任务复盘价值低。
- **需要人有判断力**。AI 自己总结可能会遗漏真正关键的标准，或者把错误归因归错。人要审一遍。
- **不要过早封装**。如果样本量只有 1，清单可能过拟合。最好有 2–3 次成功/失败样本后再固化。
- **技术限制**：扫描跨平台对话记录需要工具支持（如 Cubox、本地数据库）。不是所有 AI 工具都能做到。

## 为什么值钱

- 人的复盘成本很高：要整理聊天记录、提炼规则、写成文档、教给下一个协作者。AI 做这件事边际成本接近零。
- 没有复盘的 AI 协作，本质是“每次都从头教一个新实习生”。有复盘的 AI 协作，才是“越用越顺手的老员工”。
- 这是 AI 时代才有的工作流：AI 不只是执行者，还是自己的教练。人只负责审美和终审。
- Truman 的 Design Taste 案例证明，一次 3 小时的插图/PPT 任务，可以沉淀出一个复用很多次的设计品控 skill。

## 与其他知识的关联

- [[dk-modeling-ai-without-judgment]] —— AI 可以自动化很多工作，但人必须守住判断和审美。
- [[modeling-capability-system]] —— 建模能力在 AI 时代的价值：把经验变成可复用资产。
- [[ai-collaboration]] —— AI 协作不只是 prompt 工程，更是反馈循环和资产沉淀。
- `src_20260614_8269ccdb#1178-1216` —— Truman 口述原文：AI 自己复盘自己的 Design Taste 案例。
