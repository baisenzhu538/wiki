---
id: "skill-纪浩-AI工具脚本化约束"
title: "技能：AI工具脚本化约束"
type: "skill"
status: "draft"
domain: ""
source_person: "纪浩"
source_context: "AI协作方法论"
source_refs:
  - "00_inbox/纪浩-AI协作方法论-口述.md"
wiki_refs: ""
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tags:
  - "#confidence/draft"
  - "#domain/AI"
  - "#domain/collaboration"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology/feedback-loop"
tools_required: ""
prerequisite_skills: ""
related: ""
created_at: "2026-06-07"
updated_at: "2026-06-07"
---

# 技能：AI工具脚本化约束

## 原始表述

AI工具脚本化约束是纪浩在AI协作方法论分享中提出的具体方法，用于AI工具脚本化约束。

## 操作步骤

1. 识别AI执行中的重复操作（如查目录、找文件、读表格、查数据库、验证结果）
2. 将这些操作写成确定性脚本，而非让AI随机执行
3. 将脚本纳入Agent工具集
4. 要求AI优先调用工具而非自主分析

## 适用场景

- AI执行结果不稳定、随机性高时
- 需要与外部系统（数据库、飞书等）交互时
- 有重复性验证步骤时

## 不适用场景

- 完全开放性的创意任务

## 工具/环境

- Shell脚本/Python脚本
- 数据库查询工具
- API接口
- 飞书等协作平台接口

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

AI不脚本化则行为随机，脚本化可确保操作确定性和结果可验证

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
