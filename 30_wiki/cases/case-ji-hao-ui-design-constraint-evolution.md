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
updated_at: 2026-06-19
related:
  - '[[skill-纪浩-problem-validation-four-checks]]'
  - '[[dk-ji-hao-novice-mindset-advantage]]'
  - '[[concept-纪浩-ai-collaboration-five-layer]]'
  - '[[skill-纪浩-Problem与Question区分法]]'
  - '[[dk-ji-hao-constraint-beats-talent]]'
  - '[[dk-ji-hao-constraint-beats-talent]]'
  - '[[dk-ji-hao-novice-mindset-advantage]]'
  - '[[skill-纪浩-problem-validation-four-checks]]'
wiki_refs:
- '[[dk-ji-hao-constraint-beats-talent]]'
- '[[dk-ji-hao-novice-mindset-advantage]]'
- '[[skill-纪浩-problem-validation-four-checks]]'
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 原始正文使用"原始表述/问题/方案/关键证据"等非案例标准章节，已映射为案例卡片规范结构
- source_refs原指向00_inbox路径，现按规范清空并补充一句话摘要与互链
definition_of_done:
- 案例有明确的原始表述、问题、方案和反馈路径
- 案例有可迁移条件和失败模式
- 案例区分度≥2类型（成功/失败/边界/反常识）
pipeline:
- confidence-published
- confidence-source-cited
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
   - P1：理解用户、任务、现有系统
   - P2：定义真实问题、目标、成功标准
   - P3：建立用户旅程和信息架构
   - P4：生成方案并做多路径比较
   - P5：做用户旅程校验脚本
   - P6：组件化设计指导编码

6. **最终固定协作模式**
   流程稳定后，交互变成固定模式："参考设计规范，先做P1到P4，我看完文档告诉你哪些不行，你调整后再继续P5-P6。"

## 结果

- **Before**：后端工程师 + 模糊指令"求你把样式好好搞一下" → 红配绿、间距不一、信息密度低。
- **After**：后端工程师 + 1100行约束文档（AI自写） → 纯裸写前端，质量吊打自己此前花了极高成本（注意力、时间、token）做出来的页面。
- **核心差异**：约束文档由AI在约束框架内自我生成，证明AI在规范驱动下能够自我规范，而不依赖用户具备该领域的专业能力。

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
- 需要用AI完成超出自己专业能力范围的任务（如后端工程师做UI、产品经理写代码）。
- AI首轮输出质量不达标，需要多轮迭代。
- 任务涉及多个阶段或多个组件，存在"新信息带偏"或"旧代码带偏"风险。

**不适用条件：**
- 任务极其简单（如单行CSS修改），单点纠偏即可解决。
- 有成熟的模板或框架可直接复用，不需要重新设计规范。
- 时间压力极大，无法承受多轮迭代。

**可检验性：**
检查你最近一次AI协作的迭代次数。如果同一问题超过5轮对话还没收敛——你需要约束文档而非更多对话。

## 失败模式/教训

- **单点纠偏陷阱（Point-fix Trap）**：发现问题后逐点修复，但缺乏系统性规范，导致AI在修复A时破坏B，最终陷入50条对话的死循环。
- **信息权重失衡（Information Weight Imbalance）**：AI被最新信息或旧代码带偏，用户给出的抽象目标信息权重不足以压制旧实现或新调研方案。
- **混合交付陷阱（Mixed-delivery Trap）**：让AI一次性交付全部组件和页面，缺乏阶段性验证，导致前期错误被放大到后期。

## 相关卡/互链

- [[dk-ji-hao-constraint-beats-talent]]
- [[dk-ji-hao-novice-mindset-advantage]]
- [[skill-纪浩-problem-validation-four-checks]]

---

**反馈路径：** 使用本案例后有反馈，提交至 `60_feedback/cases/case-ji-hao-ui-design-constraint-evolution`。
