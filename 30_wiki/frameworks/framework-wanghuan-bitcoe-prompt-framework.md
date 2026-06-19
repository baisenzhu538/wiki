---
id: framework-wanghuan-bitcoe-prompt-framework
title: 王欢BITCOE提示词框架
type: framework
status: draft
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
updated_at: '2026-06-19'
author: 王语嫣
reviewed_by: pending
confidence: 0.84
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
source_refs:
- "00_inbox/王欢AI实践心法/_ocr_output/王欢-AI实战分享-BTICOE框架-示意图.md"
- "00_inbox/王欢AI实践心法/王欢-AI实战分享-从任务到产品再到系统-逐字稿.md"
related:
- '[[human-ai-collaboration-double-triangle]]'
- '[[framework-wanghuan-actor-director-mode]]'
- '[[tool-wanghuan-ai-business-profile]]'
tags:
- 王欢
- BITCOE
- 提示词工程
- prompt
- 人机协作
- 消灭模糊
---

# 王欢BITCOE提示词框架

> **Burn line**: BITCOE 不是公式，是消灭模糊的思维习惯。
>
> **来源**：王欢 AI 实战分享（2026-06-18）  
> **原名差异**：图片中写为 BTICOE，笔记中写为 BTICME（M = Method），用户统一命名为 **BITCOE**。

---

## 一、用一句话讲清楚

BITCOE 是一个六槽位提示词框架，通过强制填写**背景、指令、任务、约束、输出、示例**，把模糊需求变成 AI 可精确执行的指令。

---

## 二、六个槽位

```
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│  B  │ │  I  │ │  T  │ │  C  │ │  O  │ │  E  │
│背景 │ │指令 │ │任务 │ │约束 │ │输出 │ │示例 │
└─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘
```

| 槽位 | 英文 | 问题 | 作用 |
|:---|:---|:---|:---|
| **B** | Background | 你是谁？你的处境是什么？ | 让 AI 理解上下文 |
| **I** | Instruction | 按什么逻辑做？ | 规定思考路径和方法 |
| **T** | Task | 这次做什么？ | 明确具体目标 |
| **C** | Constraint | 不要做什么？ | 划定红线，避免跑偏 |
| **O** | Output | 什么格式？ | 规定输出形式 |
| **E** | Example | 什么风格？ | 提供参考样例 |

> **C（约束）是王欢特别强调的“最致命”槽位**——多数 AI 输出跑偏，不是因为任务没说清，而是因为约束没说清。

---

## 三、与传统 prompt 的区别

| 维度 | 传统 prompt | BITCOE |
|:---|:---|:---|
| 结构 | 自由文本 | 六槽位强制填空 |
| 重点 | 告诉 AI 做什么 | 同时告诉 AI 不要做什么 |
| 上下文 | 常被忽略 | 必填背景 |
| 输出控制 | 较弱 | 明确格式和示例 |
| 适用场景 | 简单任务 | 复杂、需要稳定输出的任务 |

---

## 四、使用模板

```markdown
## Background（背景）
- 我的角色：
- 业务场景：
- 目标用户：

## Instruction（指令）
- 思考逻辑：
- 分析方法：
- 优先顺序：

## Task（任务）
- 本次目标：
- 需要产出的核心内容：

## Constraint（约束）
- 不要做的事：
- 避免的风格/词汇：
- 红线：

## Output（输出）
- 格式：
- 长度：
- 结构：

## Example（示例）
- 参考样例：
```

---

## 五、应用示例

### 示例：让 AI 写一份 wiki 卡片

```markdown
## Background
我是知识工厂的质量负责人，正在把王欢的 AI 实战分享整理成 wiki 卡片。目标读者是团队内部的 content producer 和 reviewer。

## Instruction
按照“用一句话讲清楚 → 核心框架 → 应用场景 → 常见走偏 → Action Triggers”的结构组织内容。

## Task
写一张关于 BITCOE 提示词框架的 concept/tool 卡片。

## Constraint
- 不要泛泛而谈 prompt engineering
- 不要抄袭原始课件原文，要提炼和结构化
- 必须包含六槽位的具体定义和示例

## Output
Markdown 格式，约 2000 字，使用表格和代码块增强可读性。

## Example
参考 `[[framework-wanghuan-actor-director-mode]]` 的卡片风格。
```

---

## 六、与 AI 业务档案的关系

BITCOE 用于单次任务的精确描述，而 `[[tool-wanghuan-ai-business-profile]]` 用于定义长期稳定的角色和输出标准。两者结合使用效果更佳：

1. 先用 AI 业务档案定义“我是谁、我服务谁、我的输出标准”。
2. 再用 BITCOE 描述每次具体任务。

---

## 七、常见走偏模式

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **B 缺失** | AI 不理解上下文，输出泛泛 | 先说明角色和场景 |
| **I 缺失** | AI 按默认逻辑执行，不符合预期 | 明确思考路径和方法 |
| **T 缺失** | AI 不知道要产出什么 | 一句话说清任务 |
| **C 缺失** | 输出跑偏或包含不该有的内容 | 明确约束和红线 |
| **O 缺失** | 输出格式不稳定 | 规定格式、长度、结构 |
| **E 缺失** | 风格不符合要求 | 提供参考样例 |

---

## 八、Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| AI 输出不符合预期 | 检查 BITCOE 六槽位是否填全 |
| 同一个任务要反复调试 prompt | 把它固化成 BITCOE 模板 |
| 团队协作时 prompt 效果不一致 | 用 BITCOE 统一标准 |
| 复杂任务 AI 总是跑偏 | 重点检查 Constraint 槽位 |

---

*基于王欢 2026-06-18 AI 实战分享整理。原名 BTICOE/BTICME，入 wiki 统一为 BITCOE。*
