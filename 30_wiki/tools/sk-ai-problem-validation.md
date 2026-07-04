---

id: sk-ai-problem-validation
title: 技能：问题验证三维度法
type: tool
status: enriched
domain:
- ai-collaboration
- yitang- ai-collaboration
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论分享，2026-06
source_refs:
- 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md
wiki_refs:
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tags:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- src_unknown
- src_unknown
prerequisite_skills: []
related:
  - "[[ai-collaboration-domain-digest]]"
  - "[[tool-纪浩-Agent技能市场设计法]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown

---

# 技能：问题验证三维度法

## 用一句话讲清楚

在向 AI 派任务前，用「前后对比、真实锚点、受益对象、可解性」四要素验证这是一个值得解决的**真问题**，而非伪需求。

## 核心要点

一个真正的 problem 需要同时满足四个要素，缺一不可：

| 要素 | 填写问题 | 示例（好） | 示例（坏） |
|------|--------|---------|---------|
| **前后对比** | 解决前是什么状态？解决后希望是什么状态？ | 之前每天花 2 小时写报告，之后希望压缩到 30 分钟 | 提高写报告效率 |
| **真实锚点** | 这个问题在真实世界中有具体场景吗？ | 每周一的销售数据报告 | 企业数字化转型 |
| **受益对象** | 解决后谁会受益？ | 销售主管每周节省 30 分钟 | 全体员工 |
| **可解性** | 你相信这个问题是可解的吗？有因果链和能力支撑吗？ | 有报告模板+数据来源+验证过的方法 | 希望 AI 帮我思考 |

## 边界

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

- src_unknown
  - src_unknown
  - src_unknown

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败信号 | 根因 | 纠偏动作 |
|----------|------|----------|
| 四要素中任意一栏填不出来 | 问题本身定义模糊，仍是愿望陈述 | 回退到问题定义，用更具体的场景和指标重新描述 |
| 「受益对象」写成「全体员工」「公司」 | 受益者泛化，无法衡量价值 | 聚焦到具体岗位、具体人的具体动作 |
| 「可解性」写成「希望 AI 帮我思考」 | 缺乏因果链与能力支撑 | 先人工梳理已知方法、数据、模板，再交给 AI |
| 跳过验证直接让 AI 执行 | 把 AI 当万能解药 | 强制先填表，填不完不进入执行 |
| 表格填完但不作为上下文提交给 AI | AI 缺少问题边界，输出偏离 | 将填好的表格作为 system/user 上下文的一部分加载 |

## 相关卡/互链

- src_unknown
- src_unknown

## 来源

- src_unknown
- 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

**Steve Blank**（精益创业之父，客户开发方法论创始人）会质疑：四要素要求"可解性"作为真问题的必要条件，但创业的本质恰恰是"在不确定能否解决时仍然推进"——如果要求"可解性"才能开始，大多数真正的创新永远不会发生。

- **具体假设**：四要素模型假设"真问题必须同时满足前后对比、真实锚点、受益对象、可解性"，但许多突破性创新（如 iPhone 的诞生）在初期无法明确回答"可解性"——它们恰恰是在"不确定能否解决"的情况下推进的。
- **边界**：该框架适用于已有业务场景的 AI 任务筛选，对从零到一的创新探索不适用——创新本身就是在"可解性未知"的领域工作。
- **反例**：有些受益对象泛化的问题（如"提升全体员工效率"）虽然不符合框架建议的"聚焦到具体岗位"，但在组织级数字化转型中恰恰是正确的问题定义。
- **前提**：框架假设"能写出 before/after 就是真问题"，但 before/after 的可写性可能只是反映了问题描述者的分析能力，而非问题本身的真实性。
