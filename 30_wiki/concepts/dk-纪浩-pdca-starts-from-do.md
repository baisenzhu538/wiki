---
id: "dk-纪浩-pdca-starts-from-do"
title: "暗知识：PDCA 从 Do 开始，不是从 Plan 开始"
type: "dark-knowledge"
dark_knowledge_type: "insight"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享——UI设计Skill的迭代过程"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/ai-collaboration"
  - "#scene/ai-collaboration/pdca-execution"
  - "#scene/learning-methodology"
  - "#scene/skill-engineering/course-to-skill"
  - "#scene/skill-engineering/eval-testing"
  - "#source_type/dark-knowledge"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "concept-纪浩-ai-collaboration-methodology"
  - "skill-纪浩-dofirst-pdca"
---

# 暗知识：PDCA 从 Do 开始

## 原始表述

> 纪浩 UI 设计 Skill 的迭代过程：第一步就是硬干（Do），第二步加检查（Do+Check），第三步根据问题做计划（Do+Check+Plan），第四步从一步 Plan 变成八步（Plan→Do→Check→Act）。"所有的 PDCA 流程不是从 Plan 开始的，一定是从 Do 开始的。一定要去解决具体的问题，才有可能把 PDCA 搞好。"

## 使用场景

- 你面对一个新任务，不确定"完整的流程"应该长什么样
- 你花了很多时间做计划但计划越做越大、越做越虚
- AI 协作中，你想从"一次性对话"进化到"可复用的流程"

## 操作方法

1. 找到最小的可执行单元——不需要是"完整的一步"，哪怕就是"让 AI 试试"
2. 做完之后立刻检查——"哪里不对？哪里不够？"
3. 针对刚发现的问题做一个小 Plan——不是全局 Plan，只覆盖刚暴露的 1-2 个问题
4. 下一轮：按小 Plan 执行 → 检查新问题 → 调 Plan → 循环变粗

## 适用边界

- 适用于不确定性高的新领域（你不知道"对"长什么样）
- 不适用于容错率极低的任务（先 Plan 再做是合理的）
- 不适用于已有成熟标准流程的任务（直接用 SOP，不需要 Do-first）

## 为什么值钱

公开语料中到处是 PDCA 循环的标准定义——Plan→Do→Check→Act。但纪浩的暗知识在于**顺序不是那样**。

管理者教的 PDCA：先做 Plan，再 Do，再 Check，再 Act。初学者认知：我要先规划清楚，才能动手。结果：Plan 永远做不完，Do 永远不开始。

纪浩的实践：先 Do。因为你不做，你不知道真正的问题是什么——你在 Plan 里假设的问题，可能根本不是实际会遇到的问题。Do 是 Plan 的燃料——没有 Do，Plan 只是幻想。

KDO 自己的 `kdo quick` 命令就是这个暗知识的产品化——先写卡片，再慢慢 enrich。没有 quick，只有 produce→validate→ship 的 Plan-first 管线——老顽童的 25 张模板卡就是产物。
