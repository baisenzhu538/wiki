---
id: "skill-马易-工作流优先于AIGC的决策方法"
title: "技能：工作流优先于AIGC的决策方法"
type: skill
status: needs-review
domain:
  - ai-collaboration
  - business-strategy
source_person: "马易"
source_context: "AI落地场景识别"
source_refs: 
wiki_refs: 
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required: 
prerequisite_skills: 
created_at: 2026-06-07
updated_at: 2026-06-12
pipeline:
  - confidence-draft
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: medium-low
---

# 技能：工作流优先于AIGC的决策方法

## 原始表述

工作流优先于AIGC的决策方法是马易在AI落地场景识别中提出的实操方法。

## 操作步骤

1. 评估场景使用频率和稳定性需求
2. 判断是否有能力封装标准化工作流（SOP写得较好）
3. 计算成本：工作流成本约为AIGC的1/10到1/100
4. 确认输出稳定性要求：工作流输出更可控
5. 能用工作流封装则优先工作流，不能再用AIGC补充

## 适用场景

- 业务场景反复使用、密度高
- 已有成熟的SOP或操作流程
- 对输出稳定性要求高
- 成本敏感的项目

## 不适用场景

- 创意生成、需要高度发散性的内容
- SOP尚未建立、流程极不稳定的探索期
- 单次或极低频任务

## 工具/环境

- 工作流引擎
- SOP文档
- 成本测算表

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

工作流通过预定义节点实现确定性输出，避免大模型的随机性和高token消耗，在标准化业务中性价比极高

## 关联技能

- 待补充

## 来源

- 马易，AI落地场景识别

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
