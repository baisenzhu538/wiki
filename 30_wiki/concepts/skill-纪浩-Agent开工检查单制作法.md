---
id: skill-纪浩-Agent开工检查单制作法
title: "技能：Agent开工检查单制作法"
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang
source_person: 纪浩
source_context: AI俱乐部-人和AI协作-纪浩-五层结构-图片01
source_refs:
  - src_20260609_8c00cb42-ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01
author: 纪浩
reviewed_by: 欧阳锋
created_at: "2026-06-15"
updated_at: "2026-06-17"
confidence: 0.75
trust_level: medium
related:
  - "[[concept-纪浩-ai-collaboration-methodology]]"
  - "[[skill-纪浩-AI工作空间与导诊台设计法]]"
  - "[[skill-纪浩-Do-first-PDCA渐进迭代法]]"
  - "[[skill-纪浩-日志驱动排查法]]"
  - "[[skill-纪浩-任务交付物标准化]]"
diagnostic_signals:
  - signal: "Agent执行任务时频繁出错，执行失控"
    lens: "执行失控"
    follow_up: "先和AI把任务做一遍，记录问题和决策点。把坑提前暴露，生成检查单"
  - signal: "每次启动相似任务都要重新交代注意事项，效率低下"
    lens: "重复交代"
    follow_up: "把历史经验沉淀为检查单，开工前按单执行。隐性经验显性化"
  - signal: "人工审核检查单时遗漏关键风险点"
    lens: "审核遗漏"
    follow_up: "检查单必须包含：输入验证、边界条件、异常处理、输出格式。逐项确认"
  - signal: "检查单过于冗长，Agent执行时跳过或忽略"
    lens: "检查单臃肿"
    follow_up: "检查单控制在10项以内，按优先级排序。关键项必须执行，次要项可选"
  - signal: "没有历史经验可参考，无法制作检查单"
    lens: "经验空白"
    follow_up: "先用Do-first法跑一遍任务，记录问题。没有经验就创造经验，不能跳过第一步"
---
# 技能：Agent开工检查单制作法

- **纪浩体系**：[[concept-纪浩-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲

## 原始表述

Agent开工检查单制作法是纪浩在AI协作方法论分享中提出的具体方法，用于Agent开工检查单制作法。

## 操作步骤

1. 先和AI把任务做一遍
2. 记录过程中出现的问题、决策点和风险
3. 把问题清单丢给AI
4. 让AI生成一份开工前检查单
5. 人工审核检查单，补充自己的判断
6. 在真实任务启动前按检查单执行

## 适用场景

- 准备让agent协作完成真实任务
- 希望降低agent执行失控风险
- 需要把隐性经验显性化

## 不适用场景

- 任务过于简单无需检查
- 没有历史经验可参考

## 工具/环境

- AI对话工具
- 检查单模板
- Markdown文档

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

通过先跑一遍再沉淀检查单，把执行中的坑提前暴露，提升agent协作的可控性。

## 关联技能

- 待补充

## 来源

- 纪浩，AI协作方法论

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
