---
id: skill-半肥猫-设计Skill的评分规则与风险边界
title: 技能：设计Skill的评分规则与风险边界
type: skill
status: draft
domain: []
source_person: 半肥猫
source_context: AI学习落地
source_refs: []
wiki_refs: []
definition_of_done:
  - 操作步骤清晰可执行
  - 适用场景有正反例
  - 工具要求明确
tags:
  - "#domain/AI"
  - "#domain/design"
  - "#domain/learning"
tools_required: []
prerequisite_skills: []
related: []
created_at: '2026-06-07'
updated_at: '2026-06-07'
---

# 技能：设计Skill的评分规则与风险边界

## 原始表述

设计Skill的评分规则与风险边界是半肥猫在AI学习落地中提出的实操方法。

## 操作步骤

1. 为Skill输出设计量化评分规则
2. 定义适用场景边界（什么情况下用，什么情况下不用）
3. 建立风险分级体系（高/中/低容错场景）
4. 设定拒绝能力（能判断不该做的事并拒绝）
5. 确保有负面案例和反例支撑

## 适用场景

- ✅ 做决策支持类Skill
- ✅ 涉及安全、合规、医疗等高风险领域
- ✅ 需要客观建议而非讨好用户的场景

## 不适用场景

- ❌ 纯创意生成类工具
- ❌ 用户明确只需鼓励性反馈

## 工具/环境

- 评分标准设计
- 风险矩阵
- 正例/反例测试集

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

通用模型倾向于讨好用户，明确的评分规则和风险边界能让Skill给出客观、可验证、安全的建议

## 关联技能

- 待补充

## 来源

- 半肥猫，AI学习落地

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
