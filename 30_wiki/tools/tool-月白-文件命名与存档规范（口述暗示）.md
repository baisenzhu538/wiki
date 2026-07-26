---
id: tool-月白-文件命名与存档规范（口述暗示）
title: 技能：文件命名与存档规范（口述暗示）
type: tool
status: reviewed
domain: design
source_person: 月白
source_context: AI设计基础 （原 legacy，已从 title/context/filename 推断为 src_20260522_38173b48）
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
- '[[tool-月白-课程问题预埋法]]'
- '[[tool-月白-提示词长度控制法]]'
- '[[tool-月白-背景消除与分辨率修复]]'
- '[[tool-月白-用一堂方法论找最佳实践并拉满执行]]'
- '[[tool-月白-三步作业反馈法]]'
- '[[tool-Truman-本地记忆与云端记忆管理]]'
tags:
- audience:executor
- scene:execution
quality_labels:
- cited
diagnostic_signals:
- "存档文件夹越堆越多无法检索→未按日期+项目分层"
- "旧版本覆盖新版本→存档命名缺时间戳"
discoverable_by: "月白存档规范、设计文件存档、版本管理、文件命名存档"
---

# 技能：文件命名与存档规范（口述暗示）

## 原始表述

文件命名与存档规范（口述暗示）是月白在AI设计基础中提出的实操方法。

## 操作步骤

1. 将提示词按用途分类保存（如：反推模板、海报模板、电商模板）
2. 标注版本有效期（建议6-12个月迭代一次）
3. 建立个人'武器库'集中管理

## 适用场景

- src_unknown
- src_unknown
- src_unknown

## 不适用场景

- src_unknown

## 工具/环境

- src_unknown

## 为什么有效

提示词是长在自己身上的核心能力，系统化存档才能实现能力的沉淀和迭代

## 关联技能

- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown

## 目的

解决AI设计师的"提示词资产流失"问题。很多设计师每次做图都从零写提示词，之前跑通的好提示词散落在聊天记录里再也找不到，重复试错消耗大量时间。方法通过按用途分类保存提示词（反推模板/海报模板/电商模板）、标注版本有效期（6-12个月迭代）、建立个人"武器库"集中管理三步，将提示词从一次性消耗品升级为可积累、可迭代的个人知识资产。适用于频繁使用AIGC工具的专业设计师、需要团队共享和传承提示词资产的团队、刚入门希望通过复用优质提示词快速提升出图质量的新手。

## 质疑

- **具体假设**：该工具假设结构化方法论本身能产生正确结论，但方法论只是框架——结论质量取决于输入数据的质量和执行者的判断力。
- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效——工具的有效性高度依赖场景的稳定性。
- **反例**：一个团队完整执行了所有步骤，产出了漂亮的文档，但核心假设从一开始就是错的——流程的完整性掩盖了判断的缺陷。
- **前提**：使用者已具备该领域的基础认知，能正确理解和执行工具规则，且数据来源具有代表性。

**Margaret Clarke**（信息架构研究者）会指出：提示词版本管理的假设过于乐观。方法建议每6-12个月迭代一次提示词，但AI模型更新频率远高于此——Midjourney、DALL-E等模型每季度甚至每月都有显著变化，同一提示词在不同版本间效果差异巨大。6-12个月的迭代周期在实际操作中意味着大部分存档提示词已经过时，建立武器库的维护成本被严重低估。

**Gary Klein**（自然决策理论家）会批评：提示词存档隐含了一个危险假设——好的设计可以复用过去成功的提示词模板。但实际设计工作中，每次需求都有独特的语境和约束，过度依赖武器库调用容易形成"模板化思维"，抑制了针对新场景的创新性提示词探索。方法鼓励的是效率，但设计最需要的是适切性而非效率。
