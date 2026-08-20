---
id: case-openclaw-selfbuilt-agent-platform
title: OpenClaw 自建协作平台：排飞书微信→Matrix 失败→A2A 直连→项目空间隔离上下文
type: case
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
- knowledge-management
aliases:
- OpenClaw自建协作平台
- 自建AI协作平台
- 项目空间隔离上下文污染
- A2A撤项目经理
- 数字员工协作平台
- src_20260821_digital-employee-transcript
tags:
- audience:manager
- scene:execution
- skill-level:intermediate
source_person: OpenClaw 数字员工搭建者（龙虾员工本人）
source_context: AI经验分享-数字员工搭建-口述（2026-08，978 行）
source_refs:
- 00_inbox/龙虾员工实践/AI经验分享-数字员工搭建-口述.txt
related:
- '[[dk-project-manager-agent-failure]]'
- '[[dk-ai-efficiency-and-management-radius]]'
- '[[case-kinda-digital-employees-fullview]]'
- '[[dk-rule-not-system-capability]]'
- '[[dk-three-context-formula]]'
- '[[dk-best-datasource-is-floor]]'
- 'tool-local-search-repo-datasource-engineering'
- 'tool-platform-requirement-eight-sections'
---
# OpenClaw 自建协作平台：排飞书微信→Matrix 失败→A2A 直连→项目空间隔离上下文

## 事迹

> 「我就问了运维专家，我要做一个协作平台，有没有现成的工具可以推荐，排除了飞书跟微信……要求是电脑和手机都可以用的，要有群聊功能、文件上传、聊天记录持续保存。」（口述 L202-204）
> 「最开始给我推荐了 Matrix……配置构建的时候发现致命问题：我的 OpenCloud 消息没有办法在这些工具上正常分发。」（L206-210）
> 「飞书跟微信本身是给人用的，我在上面每天有一大堆信息要处理，不想再接入 AI 让信息量增加。」（L214）
> 「既然医生之间可以互相去沟通，为什么我还需要一个项目经理帮我去沟通这个事情？关键这个项目经理他还不能百分之百懂我的想法……所以还不如我自己来管这个项目。」（L256-264）

OpenClaw 数字员工搭建者（龙虾员工本人）在搭建 AI 协作平台时的完整决策链：**不用现成 IM（飞书/微信信息过载）→ Matrix 分发失败 → 自己创建平台 → A2A 让 AI 直连（撤掉项目经理传话层）→ 项目空间隔离上下文污染**。与楚门案例（#379）同一批规律，不同人/不同工具（OpenClaw）/独立证实。

## 背景

- 搭建者用 OpenClaw 平台（口述中"OpenCloud/open cloud"均为 OpenClaw 的 ASR 变体，**产品名标"口述待独立核实"**）管理多个 AIGC（架构师/运维专家/建模专家等数字员工）
- 需要协作平台的原因：AI 之间要协作（AIGC 工作需要与其他 AIGC 协作，L198）
- 飞书/微信排除理由：给人用的工具信息过载（L214）
- Matrix 失败：OpenClaw 消息无法正常分发（L206-210）

## 关键证据表

| 环节 | 原文 | 行号 |
|:--|:--|:--|
| 不用飞书/微信 | "这两个工具本身是给人用的，我在上面每天有一大堆信息要处理，不想再接入一些 AI 让信息量又增加" | L214 |
| Matrix 失败 | "发现有一个比较致命的问题……消息没有办法在这些工具上正常分发" | L206-208 |
| A2A 直连 | "既然医生之间可以互相去沟通，为什么我还需要一个项目经理" | L256 |
| 撤项目经理 | "他还不能百分之百懂我的想法……还不如我自己来管这个项目" | L258-264 |
| 项目空间 | "单独的项目空间……大量的上下文，如果跟日常其他短期任务的上下文混在一起，可能会产生污染" | L278-280 |
| 聊天记录本地持久化 | "我把我所有的聊天记录都是没有做压缩的，都是保存在本地电脑上" | L318 |

## 可迁移场景

- **多 Agent 协作平台选型**：先问"这个工具是给人用的还是给 AI 用的"——给人用的 IM 接 AI 会信息过载（L214）
- **Agent 间协作架构**：能直连（A2A）就别设传话层（项目经理负资产，L256-264）
- **上下文隔离**：长期复杂项目用独立项目空间（知识库/工作流隔离，L278-280、L726-730）
- **聊天记录持久化**：不压缩全量本地保存（区别于 Obsidian 上下文压缩，L310-318）
- 局限：自建平台需技术能力（搭建者让 AI 写了 70K 技术文档，L224）；消息分发兼容性问题（Matrix 失败）是通用坑

## 与其他知识的关联

- `dk-project-manager-agent-failure`：传话层负资产（本卡=第二案例实证）
- `dk-ai-efficiency-and-management-radius`：管理半径同理 AI（项目空间=管理 3 个对话即可）
- `case-kinda-digital-employees-fullview`：数字员工体系全景（同实践域 #379）
- `dk-rule-not-system-capability`：规则封装（协作平台工作流化）
- `dk-three-context-formula`：三上下文（A2A 直连=上下文直达）
- `dk-best-datasource-is-floor`：数据源下限（平台文档区=知识库雏形，L288-294）
