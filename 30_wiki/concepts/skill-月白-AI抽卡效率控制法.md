---
id: "skill-月白-AI抽卡效率控制法"
title: "技能：AI抽卡效率控制法"
type: "skill"
status: draft
domain:
  - "design"
source_person: "月白"
source_context: "AI设计师实操"
source_refs: ""
wiki_refs: ""
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
tags:
  - #domain/AI
  - #domain/design
  - #scene/ai-collaboration/prompt-engineering
  - #scene/learning-methodology/feedback-loop
pipeline:
  - #boundary/not-for-creative
  - confidence-draft
author: legacy
reviewed_by: pending
---

# 技能：AI抽卡效率控制法

## 原始表述

AI抽卡效率控制法是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 明确单轮抽卡目标，控制数量在10张以内（'一抽流'适用范围）
2. 超过10张未出满意结果时，返回检查提示词而非继续盲抽
3. 记录每轮抽卡的提示词与结果，建立个人'有效描述词库'
4. 对接近目标的图片进行人工干预（P图/局部重绘），而非追求纯AI直出
5. 复杂人物/场景接受多轮迭代，设定合理预期（如案例中第一轮50+张，最终基底仍需手工调整）

## 适用场景

- AI出图结果不稳定，需要筛选
- 追求特定风格或特定人物辨识度
- 时间有限，需要控制AI协作成本

## 不适用场景

- 探索性创作，享受随机惊喜
- 已有成熟工作流和固定提示词

## 工具/环境

- AI绘图工具
- 图片管理软件（按轮次分类）
- 提示词记录表格

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI生成有随机性，但盲目增加数量收益递减；'抽卡'本质是快速验证描述精准度，提示词质量>>抽卡数量；接受'AI出基底+人工精修'的协作现实

## 关联技能

- 待补充

## 来源

- 月白，AI设计师实操

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
