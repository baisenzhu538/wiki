---
id: "skill-纪浩-dofirst-pdca"
title: "技能：Do-first PDCA——从行动开始的迭代循环"
type: "skill"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/ai-collaboration"
  - "#scene/ai-collaboration/pdca-execution"
  - "#scene/ai-collaboration/problem-validation"
  - "#scene/learning-methodology"
  - "#scene/skill-engineering/course-to-skill"
  - "#scene/skill-engineering/publish-deploy"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "concept-纪浩-ai-collaboration-methodology"
  - "dk-纪浩-pdca-starts-from-do"
---

# 技能：Do-first PDCA

> 所有 PDCA 流程不是从 Plan 开始的，一定是从 Do 开始的。先动手解决具体问题，在过程中加检查，根据问题制定计划，再调整。循环从一步变成八步，Skill 在循环中自然长出来。

## Purpose

取代"先做完美计划再执行"的传统 PDCA 模式。Do-first PDCA 的核心逻辑：如果你没有真实的 Problem，你做不出 Plan——你只能在原地空转。先 Do，让真实问题暴露，再 Plan。

## Protocol

### 五阶段迭代路径

| 阶段 | 做什么 | 典型现象 | 例子（纪浩 UI 设计） |
|:---|:---|:---|:---|
| **阶段 1：纯 Do** | 直接让 AI 干活，不设约束 | "能做出来吗？" | 让 AI 生成 UI→能用但质量差 |
| **阶段 2：Do+Check** | 做完后检查，发现问题 | "做出来了但哪不对" | 发现 AI 不听话、UX 逻辑差 |
| **阶段 3：Do+Check+Plan** | 根据问题制定小计划 | "需要加约束" | 写 1100 行约束文档 |
| **阶段 4：Plan→Do→Check→Act** | 从一步 Plan 拆成多步 | "约束不够细" | 从一步 Plan 拆成八步 |
| **阶段 5：Skill 化** | 流程稳定后封装为 Skill | "可以复用了" | 封装为 UI design skill |

### 关键操作

1. **先 Do**：找到最小的可以动手的点。不需要是完整的——一个命令、一次对话、一个实验都算 Do
2. **在 Do 的过程中记录问题**：不是"做完总结了再想问题"，是做的时候发现什么就记什么
3. **根据问题做 Plan**：Plan 不需要覆盖全局。只针对刚暴露的 1-2 个问题
4. **循环放大**：每轮 Plan 都比上一轮更细。从一步到三步、从三步到八步

## When to Use

- 开始一个新领域，不知道完整流程长什么样
- AI 的输出质量不稳定，靠"多试几次"碰运气
- 想从一次性 prompt 进化到可复用的 Skill

## When NOT to Use

- 已经有成熟的标准操作流程——直接用，不需要 Do-first
- 时间极紧迫必须一次做到位——Do-first 的迭代需要时间
- 任务的容错率极低（如金融交易）——必须先 Plan

## Critique

### 内部局限

- **阶段 1 的"纯 Do"如果不加时间限制，可能无限延长**。没有 Check 的 Do 是盲目的——需要给纯 Do 设一个时间或轮次上限（如"最多试 3 轮，没进展就切换到 Do+Check"）
- **Do-first 对有完美主义倾向的人有反向作用**。他们会在"做出来的东西不够好"的焦虑中反复推翻重做

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|----|---|
| 上层框架 | [[concept-纪浩-ai-collaboration-methodology]] | L3——从行动开始的迭代 |
| 前置技能 | [[skill-纪浩-four-elements-validation]] | 通过四要素验证确认是 Problem 后 → Do-first |
| 暗知识 | [[dk-纪浩-pdca-starts-from-do]] | 从 Do 开始的内在逻辑 |
