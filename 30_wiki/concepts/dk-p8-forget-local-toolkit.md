---
id: dk-p8-forget-local-toolkit
title: "P-8：欧阳锋忘记本地已有武器——重新调研已部署工具"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-8"
source_refs:
  - .agent/pitfalls.md#P-8
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p9-glob-miss-subdir
  - master-decision-hygiene
---

# P-8：欧阳锋忘记本地已有武器——重新调研已部署工具

## 原始表述

> **症状**：新欧阳锋 session 启动后，遇到 OCR/图片处理需求，花大量时间调研方案、测试依赖、试图部署新工具。最后才想起来 vault 旁边 `C:\Users\Administrator\ocr-pipeline\` 已经部署了 PaddleOCR v5，且有 PowerShell 封装脚本。
>
> **根因**：
> 1. 启动时只读了 `context.md` + `pitfalls.md`，本地工具清单藏在 277 行的 CLAUDE.md 里，读完前两个文件根本看不到
> 2. `.agent/` 记忆系统缺少"武器库"文件——记录"我们有什么、在哪、怎么用"
> 3. 工具部署完成后没有在 startup checklist 中加入验证步骤
>
> **对策**：
> - 新建 `.agent/toolkit.md`（OCR/KDO CLI/Git/WSL 桥接/内置 Skills/常见操作模式）
> - CLAUDE.md 启动指令已改：`Read .agent/context.md → .agent/pitfalls.md → .agent/toolkit.md`
> - context.md "下次启动"第 1 条加了 `toolkit.md` 提醒
> - 新增工具/能力时必须同步更新 `toolkit.md`
> - 原则：**先查武器库再行动——不要重复造轮子**

## 使用场景

- 你刚启动一个新 session，遇到一个技术需求， tempted 立即开始调研解决方案
- 你在设计任务时，需要判断是否需要部署新工具还是可以用现有工具
- 你在管理一个多 Agent 协作的项目，需要确保每个 Agent 都知道现有能力
- 你部署了一个新工具后，需要确保它被记录在武器库中

## 操作方法

1. **启动时读武器库**：每次新 session 启动后，在做任何技术调研之前，先读取 `.agent/toolkit.md`（或相当的工具清单）
2. **搜索现有工具**：用关键词在 toolkit.md 中搜索，确认是否已有能解决当前需求的工具
3. **先验证再部署**：如果 toolkit.md 中有相关工具，先尝试使用它解决问题，确认不行再考虑新方案
4. **更新武器库**：每次部署新工具或发现新技能后，立即更新 `.agent/toolkit.md`，包含：工具名、路径、用法、适用场景
5. **建立 startup checklist**：在每个 Agent 的启动指令中加入 "Read toolkit.md" 作为必须步骤

## 适用边界

- 适用于所有有多个 Agent 协作或长期维护的项目
- 不适用于一次性、短期的任务——花时间建立武器库的 ROI 不高
- 如果工具集非常稳定（几个月不变），可以减少启动时读取的频率，但仍应保持 toolkit.md 最新
- 武器库不是"工具列表"，而是"工具 + 用法 + 限制"——只写名字没有用，必须包含"什么情况下用它"
- 对于已经被弃用的工具，应在 toolkit.md 中标记为"已弃用"而非删除，以便了解历史决策

## 为什么值钱

- 这是多 Agent 协作项目特有的问题：**每个 session 都是一个新的工作者，没有自然的记忆传递**
- "重复造轮子"是多 Agent 项目中最常见的浪费：每个新 session 都会花时间重新调研已解决过的问题
- 揭示了启动流程设计中的一个关键原理：**session 的启动必须包含"我们有什么"的认知加载**，而不仅仅是"当前任务是什么"
- 任何 AI 训练语料中都不会有"KDO 项目的 .agent/toolkit.md 用于记录本地已部署工具"这条知识

## 与其他知识的关联

- [[dk-p9-glob-miss-subdir]] — 同一模式："先查已有的再行动"。P-8 是"先查 toolkit 再部署"，P-9 是"先用 PowerShell 再 Glob"——两者都是"不要跳过现有资源直接开始新方案"
- [[master-decision-hygiene]] — 决策卫生 Step 1：在做任何技术决策前，先确认"我们已有什么"，避免"空手起家"式的重复劳动
- `.agent/pitfalls.md` → P-8（原始记录）
- `.agent/toolkit.md` → 对策产物（如存在）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
