---
id: tool-agent-white-paper-five-elements
title: Agent 白皮书五要素：名字/职责/能力/数据库/虚拟人格（可复制 Agent 的定义模板）
type: tool
status: pending_review
author: 老顽童
reviewed_by: pending
confidence: 0.9
trust_level: medium
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- ai-collaboration
- knowledge-management
aliases:
- Agent白皮书五要素
- 白皮书模板
- 数字员工定义
- 名字职责能力数据库虚拟人格
- AI落地Live86
- AI落地Live86-龙虾员工实践-逐字稿
- kinda龙虾
tags:
  - audience:manager
  - scene:planning
  - skill-level:beginner
  - 数字员工
  - Agent
  - 工具
  - 实证
  - 迭代
source_person: kinda
source_context:
  - 一堂 AI 俱乐部落地 Live86·龙虾员工实践（2026-08-19）——Agent 创建（L207-214）
  - 口述
source_refs:
- 00_inbox/AI落地Live86-龙虾员工实践-逐字稿.md
related:
- '[[agent-spec-ouyangfeng-reviewer]]'
- '[[framework-truman-agent-team-architecture]]'
- '[[tool-agent-whitepaper-full-lifecycle-template]]'
- '[[case-kinda-digital-employees-fullview]]'
- '[[dk-context-patching-recipe]]'
---
# Agent 白皮书五要素：名字/职责/能力/数据库/虚拟人格（可复制 Agent 的定义模板）

> **定位**：属于 [[framework-truman-agent-team-architecture]] 的实战模板——Truman 有龙虾配置模版，kinda 的 Agent 白皮书是个人版可复制定义

## 1. 工具定义

Agent 白皮书 = 创建 Agent 前写的定义文档，包含五个要素：**①基本信息（名字/职责/一句话介绍）②具体职责和需要解决的问题 ③能力 ④需要配备的数据库和资料库 ⑤虚拟人格**（L208-213）。

## 2. 为什么需要

- 创建 Agent 前先定义清楚——"写一个你关于这个 Agent 的要求、能力、想要解决的问题"（L179）
- 白皮书=Agent 的可复制性（kinda 从"每次都问"到"写白皮书直接生成"）
- 模板给 GPT → AI 老师帮你生成初始 Agent 文件 → 给 OpenClaw 生成可用 Agent（L180-181）

## 3. 使用步骤

1. **写白皮书**（五要素全）：
   - 基本信息：名字、职责、一句话介绍（L208）
   - 具体职责和需要解决的问题（L209）
   - 能力（L210）
   - 需要配备的数据库和资料库（L211）
   - 虚拟人格（L212）
2. **喂给 AI 老师**：白皮书+Truman 模版一起给 GPT，生成初始 Agent 文件（L180）
3. **给 OpenClaw 生成**：初始 agent 接收并生成可用 Agent（L181）
4. **迭代培训**：新 Agent 由架构师"培训"（L205）——多轮迭代
5. **按需配库**：给每个 Agent 配资料库（L199"创建多个 Agent 和给每个 Agent 充足的资料库"）

## 跨案例实证（#400 补强 · 变体对照）

> OpenClaw 数字员工搭建者（口述 L160-168）

- 「白皮书里面会包括基本信息，包括它的名字、职责、介绍……还有它的能力，它需要配置的数据库、资料库，还有它虚拟人格。」（L160-168）——他的白皮书 **7 要素**（名字/职责/介绍/能力/数据库/资料库/虚拟人格）对照五要素：多出"介绍"与"资料库"拆分——"这样设定之后，整个单独 AI 就能对应创建出来了"（L168）同五要素"可复制 Agent 定义"宗旨（变体补充，非推翻）


## 4. When NOT to Use

- **一次性任务**——不需要定义 Agent，直接对话（L627-628 复杂长期问题才用 Agent）
- **成熟问题**（Excel 公式/查错别字）——直接问豆包（L627）
- Agent 数量少、一人能记住所有角色时——白皮书可简化

## 5. 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| 白皮书过简 | Agent 行为不符合预期 | 补职责/能力细节 |
| 缺数据库定义 | Agent 没资料可用 | 五要素里数据库必填 |
| 虚拟人格缺失 | Agent 风格不符 | 补人格设定（对话风格/红线） |
| 白皮书=形式 | 创建后不再更新 | Agent 迭代时同步更新白皮书 |

## 6. Action Triggers

- 新 Agent 立项 → 先写白皮书五要素（与"先写需求文档"同构，L492）
- Agent 行为飘忽 → 检查白皮书是否缺要素
- 需要复制 Agent（新业务线复用）→ 白皮书即复制模板

## 7. 与其他知识的关联

- `agent-spec-ouyangfeng-reviewer`：KDO 五绝角色画像（agent-specs 同构，诊断文件 KDO 照镜子确认）
- `framework-truman-agent-team-architecture`：Truman 龙虾配置模版（方法论源）
- `dk-ai-efficiency-and-management-radius`：白皮书定义 Agent 可复用性（人效前提）
- `dk-rule-not-system-capability`：白皮书里的规则=封装成 Skill 的起点
- `case-kinda-digital-employees-fullview`：白皮书让 7+ Agent 长出（案例）
- `dk-context-patching-recipe`：配库/配上下文=白皮书第④要素的操作化
