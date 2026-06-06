---
id: skill-半肥猫-用Skill做对比测试验证效果
title: 技能：用Skill做对比测试验证效果
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
  - "#domain/learning"
tools_required: []
prerequisite_skills: []
related: []
created_at: '2026-06-07'
updated_at: '2026-06-07'
---

# 技能：用Skill做对比测试验证效果

## 原始表述

用Skill做对比测试验证效果是半肥猫在AI学习落地中提出的实操方法。

## 操作步骤

1. 设计多维度评分标准（如触发范围、结论明确性、场景拆解、风险识别、拒绝能力等）
2. 设计正向测试集（典型适用场景）
3. 设计反向/高风险测试集（故意灌水、骗AI、不该做的场景）
4. 同一题目分别用带Skill和不带Skill的模型测试
5. 量化评分对比，设定通过阈值（如分差≥28分）
6. 输出测试报告，决定是否可用

## 适用场景

- ✅ 验证自研Skill是否有效
- ✅ 评估是否值得投入生产使用
- ✅ 向团队或客户证明工具价值

## 不适用场景

- ❌ 内部临时工具无需严谨验证
- ❌ 时间资源不允许完整测试

## 工具/环境

- 测试集设计文档
- 评分标准表
- AI开发环境（支持Skill安装）

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

量化对比测试能客观证明Skill价值，反向测试尤其能验证边界意识和拒绝能力，避免AI盲目讨好用户导致错误决策

## 关联技能

- 待补充

## 来源

- 半肥猫，AI学习落地

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
