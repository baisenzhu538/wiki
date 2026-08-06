---
id: tool-纪浩-识别AI不可维护代码
title: 技能：识别AI不可维护代码
type: tool
domain:
  - ai-collaboration
  - yitang
  - ai-saas
status: draft
author: 纪浩
reviewed_by: pending
created_at: '2026-06-15'
confidence: 0.6
trust_level: low
aliases:
  - 技能
  - 技能：识别AI不可维护代码
  - 识别AI不可维护代码
source_refs:
- 10_raw/sources/src_20260609_8c00cb42-ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md
source_context: （原 legacy，已从 title/context/filename 推断为 src_20260609_8c00cb42）
updated_at: '2026-06-16'
discoverable_by:
  - 技能：识别AI不可维护代码
  - 识别AI不可维护代码
related:
- '[[tool-纪浩-新手心态启动法]]'
- '[[tool-纪浩-项目启动五问法]]'
- '[[tool-纪浩-线上问题应急值守]]'
- '[[tool-纪浩-评估AI从零写UI的可行性]]'
- '[[tool-纪浩-问题导向备课法]]'
- '[[tool-纪浩-多视角切换思考法]]'
- '[[tool-纪浩-案例池构建法]]'
- '[[tool-纪浩-里程碑验证法]]'
tags:
- audience:executor
- scene:execution
- skill-level:beginner
- 五层结构
- 俱乐部
---
# 技能：识别AI不可维护代码

- src_unknown

## 原始表述

识别AI不可维护代码是纪浩在AI协作方法论分享中提出的具体方法，用于识别AI不可维护代码。

## 操作步骤

1. 检查代码是否包含字符串拼接的HTML+script标签
2. 评估后续拆分/重构的可行性
3. 判断AI是否能在提示下不跑偏地完成维护

## 适用场景

- src_unknown
- src_unknown

## 不适用场景

- src_unknown

## 工具/环境

- src_unknown
- src_unknown

## 判断标准

| 标准 | 自检问题 |
|:-----|:---------|
| 操作步骤执行到位 | 每个操作步骤都有明确的产出物和验证标准吗？ |
| 数据/事实支撑 | 操作结论有具体的数据或用户反馈支撑，而非个人感觉吗？ |
| 失败模式排查 | 本次操作中有没有触发常见失败模式中的某一条？ |
| 迭代闭环完整 | 这次的结果是否引导了下一步的明确动作？ |

## 为什么有效

字符串拼接HTML内嵌script会导致高耦合、难拆分，AI和人类都难以维护

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 质疑

- **具体假设**：该工具假设现有方法论框架能指导实践，但框架的有效性依赖于'环境稳定性'——当环境发生颠覆性变化时，旧框架不仅无效，还可能误导。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Clayton Christensen**（哈佛商学院教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
