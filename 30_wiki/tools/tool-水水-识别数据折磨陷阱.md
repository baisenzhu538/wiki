---
id: tool-水水-识别数据折磨陷阱
title: 技能：识别数据折磨陷阱
type: tool
domain:
status: needs-review
author: unknown
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.7
trust_level: medium-low
aliases:
  - audience:executor
  - scene:execution
  - skill-level:intermediate
  - 技能
  - 技能：识别数据折磨陷阱
  - 识别数据折磨陷阱
source_refs:
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-16'
related:
tags:
---
# 技能：识别数据折磨陷阱

## 原始表述

识别数据折磨陷阱是水水在拆书会-偶然中提出的实操方法。

## 操作步骤

1. 预先设定假设和检验标准
2. 避免事后数据挖掘
3. 区分验证性分析和探索性分析
4. 要求可证伪的预测

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown

## 工具/环境

- src_unknown
- src_unknown
- src_unknown

## 为什么有效

人类确认偏误导致选择性使用数据支撑预设结论

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决研究者在数据分析中通过反复试探不同变量组合直到获得统计显著的 p<0.05 结果、实质上是 p-hacking 的「数据折磨」问题。这种做法产生的结论不可复制，是学术可重复性危机的核心原因之一。工具要求预先设定假设和检验标准、区分验证性分析和探索性分析、要求可证伪的预测，以防止事后数据挖掘产生虚假发现。适用于 A/B 测试设计、用户研究数据分析、学术研究方法论审查，以及任何依赖统计推断做决策的场景。

## 质疑

本工具的内在局限在于「预先设定假设」与「探索性发现」之间的张力——许多重要发现恰恰来自事后探索（如青霉素、宇宙微波背景辐射），完全禁止事后分析会扼杀 serendipity。前提假设是研究者能事先列出所有有意义的假设，但反例是在新兴领域（如 AI 行为研究）研究者根本不知道该问什么问题。边界在于：当数据量极大时（如大数据场景），即使不做 p-hacking，多元比较的假阳性率也会飙升。**Andrew Gelman** 批评道，p 值本身就是有缺陷的统计工具，识别数据折磨而不抛弃 p 值框架，就像戒酒但继续泡在酒吧里。**John Ioannidis** 指出，即使严格遵守预注册，研究者的利益冲突（发表压力、资助方偏好）仍会通过假设选择、变量定义等方式扭曲结论，方法论层面的修补无法解决结构性的激励扭曲。
