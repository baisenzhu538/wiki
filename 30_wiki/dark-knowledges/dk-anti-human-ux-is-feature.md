---
id: dk-anti-human-ux-is-feature
title: 反人性工具设计是特性：给 AI 用的笔记不需要人好写
type: dk
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.87
trust_level: medium
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
aliases:
- 反人性工具设计是特性
- AI优先笔记不需要人好写
- Obsidian难用是正常的
- red light别往里打字
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- AI知识库
tags:
  - audience:manager
  - scene:planning
  - skill-level:intermediate
  - 知识库
  - Agent
  - 协作
  - 框架
  - 工具
  - 方法
  - 边界
source_person: 楚门
source_context:
  - AI×知识管理探索营（2026-08-15 晚直播）——Obsidian 定位（L902-914）
  - 口述
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[framework-dual-center-feishu-obsidian]]'
- '[[concept-ai-style-knowledge-docs]]'
- '[[dk-occhams-knife-tool-migration]]'
- '[[framework-multi-agent-collab-chain-six]]'
- '[[concept-yihang-ai-feature-thinking]]'
- '[[dk-ai-builder-illusion]]'
---
# 反人性工具设计是特性：给 AI 用的笔记不需要人好写

> **定位**：属于 [[framework-dual-center-feishu-obsidian]] 的 AI 侧认知前提——Obsidian 的"难用"不是缺陷，是目标用户变了

## 原始表述

> 「OCA 是非常难用的，如果你们用它是非常难用的。我们内部也有人现在还觉得什么 OCA 又不好看，什么编辑什么各种出错，各种各样的问题。但是要注意，你们要理解 OCA 真正好用的地方根本就不是给你用的。」（口述 L902-906）
> 「我们最近起了一个非常牛的名字叫 red light……你就别往里打字，打字就是你的不对，这个笔记就没打字，让你打字。」（L908-914）

## 使用场景

- 团队抱怨 Obsidian/本地 Markdown 工具"不好用/不好看/没法协作"时
- 个人从"给人用的笔记"（印象笔记/Notion）切到"给 AI 用的笔记"（Obsidian）时
- 评估 AI 时代的工具时，用"人好不好用"当唯一标准

## 操作方法

1. **先问目标用户**：这个工具是给人用的还是给 AI 用的？（L906——Obsidian 真正好用不是给你）
2. **区分评价维度**：给人用的看协作/编辑/美观；给 AI 用的看本地文档/Agent 可读/可调用
3. **理解设计目标**：Obsidian=本地 Markdown 编辑器，天然 Agent 友好（L954-956）——写作体验差是特性
4. **人机分工**：人别往里打字（red light 精神），让 AI 写，人只读交付物（L908-914）
5. **配套双中心**：人协作留在飞书（好写好看好协作），AI 协作用 Obsidian（本地可调）——不互相迁移（L2366-2408）

## 适用边界

- 适用于**给 AI 用**的知识库场景；人的知识库（人写人读）仍需好用的编辑体验
- "难用是特性"不是万能借口——如果 AI 也读不了/调不了，那就是真缺陷
- 单人场景可全用 Obsidian；团队场景按双中心分工

## 为什么值钱

- **评价框架升级**：从"人好不好用"升级为"目标用户用得好不好"——避免用旧标准否定新工具
- **人机分工落地**：人别打字=人从"生产内容"变成"读交付物+补判断"——与"盯文档不盯窗口"互锁
- **Feature 思维延伸**：用工具的长处（Feature），不要求一个工具全能（与 concept-yitang-ai-feature-thinking 互锁）

## Critique

- **反驳**：Obsidian 连人机都做不好，团队推不动——对，所以双中心（人用飞书）；硬推见 dk-tool-adoption-by-force。
- **反驳**：难用=门槛高=排斥新手——门槛是真实的，楚门也承认"特别难用"；但门槛换来 AI 可调用是值得的（成本收益）。
- **条件**：此 dk 前提=你的 AI 真的在读写这个库；如果 AI 不用，Obsidian 确实不如飞书。
- **注意**：别把"反人性"当挡箭牌——工具的基本可用性（不崩溃/不丢数据）仍是底线。

## 与其他知识的关联

- `framework-dual-center-feishu-obsidian`：AI 侧认知前提（飞书给人/Obsidian 给 AI）
- `concept-ai-style-knowledge-docs`：AI 用的文档类型生态（技能/DataPack/角色文档）
- `dk-occhams-knife-tool-migration`：理解设计目标后再决定迁移
- `framework-multi-agent-collab-chain-six`：Agent 读写库=协作链前提
- `concept-yitang-ai-feature-thinking`：Feature 思维——用长处不要求全能（跨域 yitang）
- `dk-ai-builder-illusion`：AI 基建≠知识资产（跨域 ai-collaboration）
