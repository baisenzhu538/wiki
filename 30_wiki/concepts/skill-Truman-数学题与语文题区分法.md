---



id: skill-Truman-数学题与语文题区分法
title: 技能：数学题与语文题区分法
type: "tool"
domain:
  - ai-collaboration
  - yitang- yitang
status: draft
author: 老顽童
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.6
trust_level: low
source_refs:
- source_unknown
source_context: （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
updated_at: '2026-06-16'
related:
  - '[[skill-Truman-AI工具选型决策]]'
  - '[[skill-Truman-短视频自动化上传工作流]]'
  - '[[skill-Truman-提示词优化底层方法]]'
  - '[[skill-Truman-开源模型与商业模型融合方案]]'
  - '[[skill-Truman-AI场景探索STAR模型]]'

---
# 技能：数学题与语文题区分法

## 原始表述

数学题与语文题区分法是Truman在AI工具应用AMA中提出的实操方法。

## 操作步骤

1. 识别AI任务类型：确定性逻辑任务（数学题）vs开放性生成任务（语文题）
2. 对数学题明确指令：要求写Python代码/脚本而非让AI直接推理
3. 对语文题可利用AI自由发挥能力
4. 持续优化避免AI用语文题方式解数学题

## 适用场景

- AI分析数据、执行确定性任务时结果不稳定
- 需要精确计算或逻辑处理
- Excel数据分析、自动化脚本等场景

## 不适用场景

- 创意写作、头脑风暴等开放性任务
- 需要AI发散思考时

## 工具/环境

- Python
- 代码解释器
- 各类AI编程工具

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI大模型擅长语文题式推理，但数学题需要精确逻辑；明确区分并指定代码执行能大幅提升准确性和稳定性

## 关联技能

- 待补充

## 来源

- Truman，AI工具应用AMA

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
