---
id: "skill-马易-AI落地四阶段验证法"
title: "技能：AI落地四阶段验证法"
type: "skill"
status: "draft"
domain: ""
source_person: "马易"
source_context: "AI落地场景识别"
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
  - #domain/scene-analysis
  - #scene/knowledge-management/atomization
  - #scene/learning-methodology/feedback-loop
pipeline:
  - #boundary/requires-human-judgment
  - confidence-draft
---

# 技能：AI落地四阶段验证法

## 原始表述

AI落地四阶段验证法是马易在AI落地场景识别中提出的实操方法。

## 操作步骤

1. 拆场景：将业务拆解为可独立评估的最小单元
2. 做判断：用自有标准判断是否符合AI化条件（调性、可行性）
3. 做验证：小范围测试验证效果
4. 搞开发：基于验证结果进行开发
5. 上线平行：新旧系统并行运行，持续校验对比

## 适用场景

- 任何AI项目从0到1启动
- 需要降低落地风险
- 大规模项目（几十人到上千人）需要稳妥推进
- 需要向客户交付AI咨询方案

## 不适用场景

- 已验证成熟的场景可直接规模化复制
- 时间压力极大无法接受并行验证期

## 工具/环境

- 场景拆分模板
- 判断标准文档（可用Cubox快速撰写）
- A/B测试框架
- 平行运行监控系统

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

平行验证降低替换风险，四阶段法将不确定性逐层过滤；百亿级项目同样适用，核心是通过校验迭代而非一步到位

## 关联技能

- 待补充

## 来源

- 马易，AI落地场景识别

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
