---




id: skill-纪浩-识别AI不可维护代码
title: 技能：识别AI不可维护代码
type: "tool"
domain:
  - ai-collaboration
  - yitang- ai-saas
status: draft
author: 纪浩
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.6
trust_level: low
source_refs:
  - src_20260609_8c00cb42-ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01
source_context: （原 legacy，已从 title/context/filename 推断为 src_20260609_8c00cb42）
updated_at: '2026-06-16'
related:
  - '[[skill-纪浩-新手心态启动法]]'
  - '[[skill-纪浩-项目启动五问法]]'
  - '[[skill-纪浩-线上问题应急值守]]'
  - '[[skill-纪浩-评估AI从零写UI的可行性]]'
  - '[[skill-纪浩-问题导向备课法]]'

---
# 技能：识别AI不可维护代码

- **纪浩体系**：[[concept-ji-hao-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲

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
