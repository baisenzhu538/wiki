---
id: case-ji-hao-ui-design-constraint-evolution
title: 案例：纪浩从'求你了'到1100行约束文档的UI设计迭代
type: case
status: enriched
domain:
- ai-collaboration
- yitang
source_person: 纪浩
source_context: AI俱乐部·AI协作方法论分享（2026年）
source_refs:
- 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
- 10_raw/sources/src_20260617_15ca3bb2-ai俱乐部-人和ai协作-纪浩-参考案例-结构化.md
created_at: 2026-06-09
updated_at: 2026-07-02
related:
  - "[[ai-collaboration-domain-digest]]"
  - "[[yitang-domain-digest]]"
  - "[[pending_unknown]]"
  - "[[case-live81-ai-trademark-design]]"
  - "[[tool-ai-deliverable-polish-loop]]"
  - "[[dk-ai-design-pitfalls]]"
wiki_refs:
- src_unknown
- src_unknown
- src_unknown
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
---
# 案例：纪浩从"求你了"到1100行约束文档的UI设计迭代

## 一句话摘要

后端工程师纪浩在让AI生成UI页面时，因模糊指令陷入50条对话仍调不对的困境；最终通过"中间产物驱动"的六阶段约束流程，让AI自写出1100行设计约束文档，实现了零框架裸写前端且质量远超手动设计的结果。

## 背景

纪浩是一名后端工程师，对UI设计没有专业审美，原本认为"只要能用就行"。在使用AI协作生成页面时，他给出了一条极其模糊的指令——"求你把样式好好搞一下"。首轮产出却让他大跌眼镜：红配绿、间距不一、信息密度低、排版混乱。

这次失败开启了一段从"求你了"式prompt到系统化约束文档的迭代历程。

## 关键事件/决策点

1. **第一阶段：毫无约束（失败）**
   给AI模糊指令"求你把样式好好搞一下"，结果产出红配绿、信息密度低、排版混乱的页面。

2. **第二阶段：单点纠偏（陷阱）**
   发现问题后逐页纠偏——"你能不能改一下这个缩进和对齐？"。50条对话后，AI仍被新信息或旧代码带偏，始终无法收敛。

3. **第三阶段：规范迭代（转折）**
   意识到单点纠偏无效后，纪浩转向建立系统性规范：让AI先理解用户旅程、信息架构、任务流，再生成组件化设计。

4. **关键决策：冻结代码，先做分析**
   不再让AI直接修改代码，而是先让AI分析现有页面的问题，建立"北极星目标 > 场景心智 > 现有代码"的排序权威。

5. **建立六阶段门控流程**
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

6. **最终固定协作模式**
   流程稳定后，交互变成固定模式："参考设计规范，先做P1到P4，我看完文档告诉你哪些不行，你调整后再继续P5-P6。"

## 结果

- src_unknown
- src_unknown
- src_unknown

## 复盘与洞察

1. **"求你了"是最贵的prompt**
   模糊指令的代价不是首轮输出差，而是后续50条对话的沉没成本。一个精确约束 ≈ 省50条纠偏对话。

2. **单点纠偏是陷阱**
   发现一个问题修一个问题，AI在修复A时破坏B。必须从"逐点修复"升级到"系统性规范"。

3. **中间产物是质量的杠杆**
   不让AI直接生成最终输出，而是先生成约束文档、用户旅程、信息架构，验证后再生成最终页面。中间产物越扎实，最终输出越稳定。

4. **建立"排序权威"**
   明确"北极星目标 > 场景心智 > 现有代码"的优先级。没有排序权威，AI会被新信息或旧代码随机带偏。

5. **分阶段门控**
   P1-P4（分析+规划）验证通过才进入P5-P6（执行）。如果P1-P4阶段就发现方向不对，果断回头。

## 可迁移模式

**适用条件：**
- src_unknown
- src_unknown
- src_unknown

**不适用条件：**
- src_unknown
- src_unknown
- src_unknown

**可检验性：**
检查你最近一次AI协作的迭代次数。如果同一问题超过5轮对话还没收敛——你需要约束文档而非更多对话。

## 失败模式/教训

- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown

---

**反馈路径：** 使用本案例后有反馈，提交至 `60_feedback/cases/case-ji-hao-ui-design-constraint-evolution`。

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 可迁移场景

| 场景 | 如何套用 | 关键组件/关联卡片 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |

---

## 教训

- src_unknown
- src_unknown
- src_unknown
