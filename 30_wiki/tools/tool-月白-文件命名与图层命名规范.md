---
id: tool-月白-文件命名与图层命名规范
title: 技能：文件命名与图层命名规范
type: tool
status: reviewed
domain: design
source_person: 月白
source_context: AI设计师实操 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
aliases:
  - PS图层命名规范
  - 命名与图层命名规范
  - 图层命名规范
  - 技能
  - 技能：文件命名与图层命名规范
  - 文件命名与图层命名规范
  - 月白
  - 月白图层命名
source_refs:
- 10_raw/sources/src_20260522_38173b48-design-ai-image-generation.md
wiki_refs: null
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-07-26'
pipeline:
- src_unknown
author: 月白
reviewed_by: 老顽童
confidence: 0.80
trust_level: observed
related:
- '[[tool-月白-印刷DPI标准设置]]'
- '[[tool-月白-控制产品画面尺寸比例]]'
- '[[tool-月白-AI图片印刷落地预处理]]'
- '[[tool-月白-眼高手低训练法]]'
- '[[tool-月白-PS图层规范管理]]'
tags:
- audience:executor
- scene:execution
- skill-level:beginner
quality_labels:
- cited
diagnostic_signals:
- "PS图层命名混乱找不到→检查是否跳过统一规范"
- "协作方打开文件发现字体缺失→命名未标注字体依赖"
discoverable_by: "月白图层命名、文件命名规范、PS图层管理、设计文件图层命名"
---
# 技能：文件命名与图层命名规范

## 原始表述

文件命名与图层命名规范是月白在AI设计师实操中提出的实操方法。

## 操作步骤

1. 项目名_版本号_日期_修改内容，如'Leo小人_v2_0315_调眼睛'
2. 图层命名：主体部位_具体元素_状态，如'面部_眼睛_放大版'
3. 同类元素编组，如'【人物】/【背景】/【产品】'
4. 保留'最终输出'和'源文件'双版本

## 适用场景

- **PS/AI大型源文件管理**：一个项目可能包含几十个图层，不规范的图层命名让后续修改变成"找图层游戏"
- **设计团队协作**：设计师之间互相接手文件时，图层命名是唯一不需要额外沟通的上下文
- **AIGC+手动精修混合流程**：AI生成初稿后手动调图层，命名让精修阶段能快速定位

## 不适用场景

- **单人一次性设计**：只做一次、不需要复用的设计，图层命名的时间成本可能超过收益
- **纯AI生成不需手动修改**：如果AI直出成品且满意，命名图层的ROI为零

## 工具/环境

- Photoshop（主力，图层命名和管理）
- Illustrator（矢量图层命名）
- Figma / Sketch（协作场景的图层管理）

## 为什么有效

设计是解题过程，规范的命名让'应用题数字变了'时能快速定位修改点

## 关联技能

- [[tool-月白-设计文件八要素命名法]] — 文件级命名是图层命名的上一层
- [[tool-月白-PS图层规范管理]] — 图层管理的完整规范
- [[concept-structured-naming-as-infrastructure]] — 命名即基础设施，图层命名是其原子单元

## 来源

- 10_raw/sources/src_20260522_38173b48-design-ai-image-generation.md — 月白AI设计师实操课程
- 00_inbox/半肥猫月白老朱线下聚会/AI应用研讨-半肥猫月白老朱-交流录音.txt#L2046-2072 — 图层命名被逼出来的实战经验

## Feedback Path

- 新接手他人PSD时如果发现图层命名混乱→记录为反面案例
- 每月抽查自己的PSD文件图层命名率

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 质疑

- **具体假设**：该工具假设现有方法论框架能指导实践，但框架的有效性依赖于'环境稳定性'——当环境发生颠覆性变化时，旧框架不仅无效，还可能误导。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Clayton Christensen**（哈佛商学院教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
