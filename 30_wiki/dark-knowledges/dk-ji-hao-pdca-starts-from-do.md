---

id: dk-ji-hao-pdca-starts-from-do
title: 暗知识：PDCA从Do开始不是从Plan开始
type: dk
status: enriched
domain:
- ai-collaboration
- yitang
source_person: 纪浩
source_context: AI俱乐部·人和AI协作（第三次分享，2026-06）
source_refs:
- 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
- 10_raw/sources/src_20260617_50e2866a-ai俱乐部-人和ai协作-纪浩-五层结构-结构化.md
related:
  - '[[dk-ji-hao-logs-fastest-ignored]]'
  - '[[tool-纪浩-低成本输出验证法]]'
  - '[[tool-纪浩-Do-first-PDCA渐进迭代法]]'
  - '[[tool-纪浩-处理AI生成代码运行异常]]'
  - '[[tool-纪浩-Agent开工检查单制作法]]'
  - [[concept-ji-hao-ai-collaboration-methodology]]
created_at: 2026-06-08
updated_at: 2026-06-19
pipeline:
- confidence-draft
- confidence-source-cited
- format-enriched
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: '团队反复在"想清楚再动手"和"边做边改"之间争论'
  lens: 执行模式
  follow_up_question: '这个任务是否有经过验证的SOP或极高的失败成本？'
- signal: '计划写得很厚，但执行时第一步就卡住'
  lens: 计划有效性
  follow_up_question: '计划里的关键假设是否已经在真实场景中做过最小验证？'
---
# 暗知识：PDCA从Do开始不是从Plan开始

## 用一句话讲清楚

在不确定性高的AI协作场景中，PDCA循环应该从"做"（Do）开始，而不是从"计划"（Plan）开始：先动手解决具体问题，在行动中建立检查点、发现偏差、生成小计划，再调整。循环是从行动中长出来的，Skill也在循环中自然沉淀。

## 核心洞察

- **传统管理学的"先计划后执行"在这里失效**：任何计划都建立在假设上，而假设在真正动手之前很难被验证。先Do给出一个具体的批判对象，后续的Check和Plan才有依据。
- **循环从一步演化为八步**：不是 P→D→C→A，而是 D→C→A→P 的小循环嵌套，在做的过程中不断长出检查、调整和计划能力。
- **Skill在循环中自然生长**：不是先学会完整方法再执行，而是在一次次"做-看-调"中沉淀出可复用的技能。

> **纪浩的原话**："最开始我也是先Plan再Do。但发现这样不行——你计划得再好，到了实际做的时候一定会有偏差。所以就先Do，先做出一版，然后看问题在哪里，再去加Check、加Plan。循环是从Do长出来的。"

## 边界/适用场景

| 场景 | 是否适用 | 判断依据 |
|---|---|---|
| 高不确定性、新问题频发、没有现成SOP | ✅ 高度适用 | 计划无法提前覆盖未知，必须用行动验证假设 |
| AI协作中的快速迭代任务 | ✅ 高度适用 | 生成结果成本低，反复试错能快速收敛 |
| 已被验证多次的标准操作 | ❌ 不适用 | 如飞机起降检查单，必须先Plan再Do |
| 失败成本极高的任务 | ❌ 不适用 | 如线上生产环境变更，必须先风险评估 |
| 有严格安全规范或法律法规限制 | ❌ 不适用 | 合规要求前置，不能边做边定规则 |
| 需要多人协作、提前协调资源的项目 | ⚠️ 有限适用 | 资源协调部分需先Plan，执行细节可Do-first |

## 失败模式/常见错觉

| 失败模式 | 为什么发生 | 纠正信号 |
|---|---|---|
| "计划崇拜"——不写满十页PPT不敢动手 | 把计划完整度误当成确定性 | 计划越厚，执行第一步卡得越死 |
| "做了再说"变成"做了白做" | 只有Do，没有Check和Act | 重复犯同样的错，没有沉淀 |
| 把Do-first当成"不要计划" | 误解为反计划，而非反"计划先行" | 每次调整后没有形成下一轮小Plan |
| 在稳定流程里强行Do-first | 忽略了边界条件 | 执行结果稳定偏离预期，却仍在"试错" |

## 行动 Checklist

- [ ] 判断当前任务是否有已知SOP或极高失败成本——有则先Plan，无则Do-first
- [ ] 用最小行动做出第一版可观察的结果，而不是先写完整计划
- [ ] 在第一版结果上建立Check点：偏差是什么？假设哪里错了？
- [ ] 根据Check结果生成下一轮小Plan，而不是推翻重来
- [ ] 完成一个循环后，把可复用的判断和步骤沉淀为Skill或SOP

## 相关卡/互链

- [[tool-纪浩-Do-first-PDCA渐进迭代法]]
- [[concept-ji-hao-ai-collaboration-methodology]]
