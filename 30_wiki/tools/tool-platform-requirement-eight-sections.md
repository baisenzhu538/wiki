---
id: tool-platform-requirement-eight-sections
title: 平台需求梳理 8 节模板：解决什么/用户场景/界面/成功标准/边界/依赖/不做/优先级
type: tool
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.88
trust_level: medium
language: zh-CN
created_at: 2026-08-21
updated_at: 2026-08-21
domain:
- ai-collaboration
- product
aliases:
- 需求八节模板
- 平台需求梳理模板
- 调研模板8节
- 需求梳理八段
- src_20260821_digital-employee-transcript
tags:
  - audience:manager
  - scene:planning
  - skill-level:intermediate
  - 协作
  - 工具
  - 方法
  - 边界
  - 迭代
source_person: OpenClaw 数字员工搭建者（龙虾员工本人）
source_context:
  - AI经验分享-数字员工搭建-口述（2026-08，978 行）+ 平台需求梳理模板 PNG③
  - 口述
source_refs:
- 00_inbox/龙虾员工实践/AI经验分享-数字员工搭建-口述.txt
related:
- '[[case-openclaw-selfbuilt-agent-platform]]'
- '[[tool-local-search-repo-datasource-engineering]]'
- '[[dk-rule-not-system-capability]]'
- '[[framework-一堂-机会预判]]'
- '[[dk-ai-capability-illusion]]'
- '[[tool-ai-adapted-workflow-design]]'
---
# 平台需求梳理 8 节模板

> **定位**：属于 AI 协作平台/工具建设的需求梳理模板——"定好调研模板"（口述 L218-220）的具体化，解决"AI 调研产出太粗糙"（L218）的问题。PNG③（平台需求梳理模板截图）为一等证据。

## 1. 工具定义

平台需求梳理 8 节模板：解决什么 / 用户场景 / 界面 / 成功标准（2-5 条）/ 边界情况 / 依赖前提 / 明确不做的事 / 优先级——用于让 AI 做平台/工具调研与建设时输出结构化需求文档。

## 2. 为什么需要

> 「最开始的一个调研是很粗糙的，后面跟他们谈了几轮之后，我决定给他们定好一些调研的模板。然后我这个模板是需要有同类型的产品效果，还有实现的方案，还有做最小技术验证的成果，工作量预估等等。」（口述 L218-222）

AI 调研产出粗糙→定模板约束→调研质量提升（"最后我还是把这个协作平台成功自己做了出来"，L222）。模板化=把"调研方法"封装成系统能力（同 dk-rule-not-system-capability 规律）。

## 3. 使用步骤

1. **定 8 节模板**（PNG③）：解决什么 / 用户场景 / 界面 / 成功标准 2-5 条 / 边界情况 / 依赖前提 / 明确不做的事 / 优先级
2. **给 AI 下发模板**：让 AI 按模板做调研/需求梳理（L218-220 先例：同类型产品效果/实现方案/最小技术验证成果/工作量预估）
3. **逐节验收**：每节缺失/粗糙→退回重写（模板=验收清单）
4. **迭代模板**：谈几轮后模板进化（L218）

## 4. When NOT to Use

- 一次性小需求（模板化成本大于收益）
- 已有成熟需求模板的团队流程（避免双套标准）

## 5. 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| 模板空泛 | AI 每节都写"待确认" | 每节给示例（成功标准 2-5 条量化） |
| 缺"不做的事" | 范围蔓延 | "明确不做的事"必填（模板第 7 节） |
| 优先级缺失 | 全部 P0 | 优先级节强制排序 |

## 6. Action Triggers

- 让 AI 调研/建设平台类需求 → 先发 8 节模板
- AI 调研产出粗糙 → 定模板约束（L218-220）
- 需求范围蔓延 → 补"明确不做的事"

## 7. 与其他知识的关联

- `case-openclaw-selfbuilt-agent-platform`：协作平台（模板的产出物）
- `tool-local-search-repo-datasource-engineering`：数据源工程（同实践域）
- `dk-rule-not-system-capability`：规则封装（模板=系统能力）
- `framework-一堂-机会预判`：需求判断（跨域 yitang）
- `dk-ai-capability-illusion`：方法把关（模板=方法）
- `tool-ai-adapted-workflow-design`：AI 适配化工作流（模板=工作流约束）
