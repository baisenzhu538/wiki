---
id: dk-doc-numbering-business-logic
title: 文档编号=业务推理逻辑+里程碑依赖：编号不是 123，是谁决定谁
type: dk
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- management
aliases:
- 文档编号业务逻辑
- 编号不是123
- 里程碑依赖编号
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- AI知识库
tags:
- audience:manager
- scene:planning
- skill-level:advanced
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——文档编号逻辑（L1160-1174）
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[tool-top-level-document]]'
- '[[framework-knowledge-five-leaps]]'
- '[[framework-multi-agent-collab-chain-six]]'
- '[[dk-future-backward-knowledge-tree]]'
- '[[tool-yitang-hypothesis-marginal-roi]]'
- '[[dk-decision-value-overrides-roi]]'
- 'framework-knowledge-naming-systems-comparison'
---
# 文档编号=业务推理逻辑+里程碑依赖：编号不是 123，是谁决定谁

> **定位**：属于 [[tool-top-level-document]] 的下层机制——编号是项目的推理地图，不是排序流水号

## 原始表述

> 「编号本质上取决于你对于业务的推理逻辑和里程碑依赖关系。我理解他不是单纯的变成 123，他是谁决定谁决定谁，然后是一个推导的过程。」（口述 L1172-1174）

> 「首先顶层，这是真实项目的目录……一开头的文档都是关于拆解的基本思路，然后二开头就是市场的最佳实践，然后三开头的文档基本上就是建模和来回测评。四开头的文档就是记那个报告，来回打磨。然后五开头的文档就是封装成 Y 模型要用到的支持四个数据包，最后还有什么复盘文档……技能是封装完了放到一个技能池里面，然后 AI 就可以学了。」（口述 L1114-1118，#396 补强——数字前缀=工作流顺序的完整实证：1 拆解→2 最佳实践→3 建模测评→4 报告打磨→5 封装数据包→复盘+技能池）

## 使用场景

- 项目文档需要编号组织时（顶层文档/项目文件夹/官网文档接力）
- 团队文档"散在 40 个文件夹里"找不到入口时（L786）
- 需要让 AI/新人按项目逻辑浏览文档时

## 操作方法

1. **先画推理链**：项目的核心推导是什么——谁决定谁（00 目标 → 10 需求 → 20 设计 → 30 技术 → 40 萃取 → 90 复盘，L1114-1118 造物笔记示例）
2. **编号按依赖不按顺序**：数字代表"阶段/依赖层级"，不是"第几篇文档"
3. **里程碑锚定**：每个编号对应一个里程碑（目标/需求/设计/技术/萃取/复盘）
4. **顶层文档统揽**：所有编号从顶层文档索引出来（L684-686）——编号是地图，顶层文档是入口
5. **接力可续**：官网文档 00-20 楚门写、30-40 志钊写（L2298）——编号让接力者知道从哪继续

## 适用边界

- 适用于**复杂项目**（多阶段/多依赖）；简单项目（一次性能做完）不需要编号体系
- 编号体系需要团队共同理解（谁决定谁）——没有共识的编号=另一种混乱
- 编号粒度随项目复杂度调整（大项目 00-90，小项目 1-3 即可）

## 为什么值钱

- **推理可视化**：编号把"业务推理逻辑"显性化——打开目录就知道项目怎么思考的
- **依赖可管理**：里程碑依赖关系一目了然——改 10 需求知道要动 20 设计
- **接力/迁移低成本**：新人和 AI 按编号顺序理解项目，不用问"文档在哪儿"

## Critique

- **反驳**：编号太重，小项目用不上——对，粒度自适应；但"先定推理链再编号"的习惯永远适用。
- **反驳**：谁决定谁的判断有主观性——对，需要团队讨论定稿（楚门说"我们内部也不大会"，L1170）。
- **条件**：此 dk 前提=项目有可识别的阶段/依赖；纯事务型项目（无推导）不适用。
- **注意**：编号是工具不是目的——别为了编号而编号，核心是"业务推理逻辑清晰"。

## 与其他知识的关联

- `tool-top-level-document`：编号体系挂载在顶层文档之下
- `framework-knowledge-five-leaps`：造物笔记 00-90 编号=第五阶段实践
- `framework-multi-agent-collab-chain-six`：编号=协作链的读写顺序
- `dk-future-backward-knowledge-tree`：知识树按未来目标分目录（编号是项目级同构）
- `tool-yitang-hypothesis-marginal-roi`：业务推理（跨域 yitang）
- `dk-decision-value-overrides-roi`：推理优先于便利（跨域 decision）
