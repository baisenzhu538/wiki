---

id: tool-ai-problem-validation
title: 技能：问题验证三维度法
type: tool
domain:
- ai-collaboration
- yitang
- ai-saas
status: needs-review
author: unknown
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.7
trust_level: medium-low
aliases:
  - 技能
  - 技能：问题验证三维度法
  - 问题验证三维度法
  - 验证三维度法
source_refs: null
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-16'
discoverable_by:
  - 技能：问题验证三维度法
  - 问题验证三维度法
related:
- '[[ai-collaboration-mindset-shift]]'
- '[[sk-ai-problem-validation]]'
- '[[tool-ai-four-elements-validation]]'
- '[[tool-ai-problem-question-check]]'
- '[[tool-ai-evidence-check]]'
- '[[tool-纪浩-problem-validation-four-checks]]'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---
# 技能：问题验证三维度法

## 原始表述

纪浩提出，一个真正的problem需要同时满足四个要素：前后对比（before/after）、真实锚点、受益对象、可解性。缺一不可。

## 操作步骤

1. 在向AI提出需求前，填写这个表格：
2. | 要素 | 填写问题 | 示例（好） | 示例（坏） |
3. |------|--------|---------|---------|
4. | **前后对比** | 解决前是什么状态？解决后希望是什么状态？ | 之前每天花2小时写报告，之后希望压缩到30分钟 | 提高写报告效率 |
5. | **真实锚点** | 这个问题在真实世界中有具体场景吗？ | 每周一的销售数据报告 | 企业数字化转型 |
6. | **受益对象** | 解决后谁会受益？ | 销售主管每周节省30分钟 | 全体员工 |
7. | **可解性** | 你相信这个问题是可解的吗？有因果链和能力支撑吗？ | 有报告模板+数据来源+验证过的方法 | 希望AI帮我思考 |
8. 使用流程
1. 把任务描述填进表格
2. 如果任意一栏填不出来 → 这不是一个好的problem，先回去定义
3. 3. 如果四栏都能填满 → 这个problem可以交给AI，并给出验收标准
4. 4. 把这个表格作为上下文的一部分加载给AI

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 工具/环境

- src_unknown
- src_unknown

## 为什么有效

很多AI项目失败不是因为技术，而是因为从一开始就在解决一个"假需求"。这个清单能让你在投入之前就发现问题。

## 关联技能

- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：四要素模型假设"真问题必须同时满足前后对比、真实锚点、受益对象、可解性"，但许多突破性创新（如 iPhone 的诞生）在初期无法明确回答"可解性"——它们恰恰是在"不确定能否解决"的情况下推进的。
- **边界**：在基础研究领域，"受益对象"往往是未来某个未知的群体，强制要求当下明确受益对象会过滤掉长期价值极高的探索性研究。
- **反例**：Google 的 PageRank 算法最初只是一个学术 question（如何衡量网页重要性），不满足"可解性"和"受益对象"，但最终成为价值万亿美元产品的核心。

**Clayton Christensen**（哈佛商学院教授，"颠覆式创新"理论创始人）会质疑：四要素模型隐含的假设是"问题定义越清晰，解决方案越可靠"，但他的研究表明，真正改变行业格局的创新往往来自"问题定义不清晰但行动迅速"的团队。过度验证 problem 的"真实性"可能导致"完美定义了一个已经过时的问题"。
