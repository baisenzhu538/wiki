---
id: skill-纪浩-识别AI不可维护代码
title: 技能：识别AI不可维护代码
type: skill
status: draft
domain: ''
source_person: 纪浩
source_context: AI协作方法论
source_refs:
- 00_inbox/纪浩-AI协作方法论-口述.md
wiki_refs: ''
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required: ''
prerequisite_skills: ''
related:
- concept-纪浩-ai-collaboration-methodology
- skill-纪浩-真需求四要素验证法
created_at: '2026-06-07'
updated_at: '2026-06-07'
tags:
- null
- null
- null
- null
- null
pipeline:
- null
- confidence-draft
---
# 技能：识别AI不可维护代码

- **纪浩体系**：[[concept-纪浩-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲

## 原始表述

识别AI不可维护代码是纪浩在AI协作方法论分享中提出的具体方法，用于识别AI不可维护代码。

## 操作步骤

1. 检查代码是否包含字符串拼接的HTML+script标签
2. 评估后续拆分/重构的可行性
3. 判断AI是否能在提示下不跑偏地完成维护

## 适用场景

- 接手AI生成或他人代码时
- 代码包含动态拼接HTML和脚本

## 不适用场景

- 代码结构清晰、职责分离良好

## 工具/环境

- 代码审查工具
- 静态分析工具

## 判断标准

| 标准 | 自检问题 |
|:-----|:---------|
| 操作步骤执行到位 | 每个操作步骤都有明确的产出物和验证标准吗？ |
| 数据/事实支撑 | 操作结论有具体的数据或用户反馈支撑，而非个人感觉吗？ |
| 失败模式排查 | 本次操作中有没有触发常见失败模式中的某一条？ |
| 迭代闭环完整 | 这次的结果是否引导了下一步的明确动作？ |

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未先确认场景是否适用 → 方法无效 → **先对照“适用场景”确认本方法适用**

## 为什么有效

字符串拼接HTML内嵌script会导致高耦合、难拆分，AI和人类都难以维护

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
