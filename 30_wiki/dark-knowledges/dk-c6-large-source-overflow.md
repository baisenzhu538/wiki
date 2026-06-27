---

id: dk-c6-large-source-overflow
title: C-6：大源文件导致 session 容量超载→produce 骨架生成但内容填不进去
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: Builder
source_context: 2026-05-03
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
  framework_lens: '大文件编译已耗尽当前 session 的 context window，produce 阶段没有足够 token 填充内容'
  follow_up_question: '检查源文件大小是否超过 100KB；如是，启动新 session 仅执行 produce，并将编译结果结构化传入'
- src_unknown
  framework_lens: '混淆了"骨架生成"与"内容填充完成"两个不同里程碑'
  follow_up_question: '人工检查 draft 是否有案例、数字、关联说明；如只有标题/模板，则回到新 session 重新 produce'
- src_unknown
  framework_lens: 'Agent 手动编译模式下，编译与产出两阶段叠加超出 LLM context window 物理上限'
  follow_up_question: '强制分 session：当前 session 只完成编译和 angle 确认，新 session 负责 produce 填充'
---# C-6：大源文件导致 session 容量超载→produce 骨架生成但内容填不进去

## 原始表述

> 一堂原文 207KB（~10 万字+），三步编译法用掉大部分 session 容量。概念卡完成后 `kdo produce` 只生成了骨架，artifact 没有空间填充。
>
> 根因：当前模式（Agent 手动编译）下，大文件的编译和 artifact 填充在同一 session 内无法完成。
>
> 修正：大文件编译后，artifact 填充应放在新 session 中执行，或先确认角度/方向再启动填充 session。produce 骨架生成不算完成，draft 非空才算。

## 核心洞察

C-6 的本质不是"文件太大"，而是**把两个高消耗阶段硬塞进同一 session 导致的系统性失败**。三步编译法（浓缩→质疑→对标）本身就要吃大量 context；produce 阶段又需要足够的 token 来生成结构化、有案例、有论证的 artifact。两者叠加后，大文件场景下必然发生"前端吃饱了、后端饿死了"的截断。这一规律在任何 Agent 手动编译、单 session 执行的 LLM 工作流中都成立：context window 是硬约束，不能绕，只能重新切分阶段。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **评估文件大小**：处理前先看源文件体积——超过 100KB 即视为大文件，需要分 session 策略
2. **第一阶段：编译（当前 session）**：完成三步编译法（浓缩→质疑→对标），产出概念卡的核心观点、关键证据和结构
3. **确认角度/方向**：编译完成后，先明确卡片的核心 angle 和关键结论——不要直接进入 produce
4. **第二阶段：填充（新 session）**：启动新 session，将编译结果（核心观点、结构、关键证据）作为输入，执行 `kdo produce`
5. **判定完成标准**：produce 骨架生成 ≠ 完成。必须人工检查 draft 非空、内容有实质填充（案例、数字、关联说明），才算完成

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:-----|:-----|
| 单 session 内编译+produce 超载 | `kdo produce` 只生成标题骨架，正文为空或严重 truncated | 编译完成后开新 session，将结构化编译结果传入再 produce |
| 未确认 angle 就进入 produce | 新 session 中 produce 方向漂移，填充内容与原始源文件重点不符 | produce 前先明确核心结论、关键证据、卡片 angle，并写入结构化笔记 |
| 误判"骨架生成 = 完成" | 卡片状态标记为完成，但 draft 无实质内容 | 建立完成标准：draft 必须含案例/数字/关联说明，骨架 alone 不算 |
| 小文件盲目套用分 session | <50KB 文件也分 session，增加上下文切换成本 | 小文件直接单 session 完成；仅 100KB+ 或 context 消耗过半时才分 session |
| context window 很大就忽视两阶段分离 | 200K+ 模型处理大文件时仍可能因长对话历史导致后续 produce 空间不足 | 无论窗口多大，保持"编译→确认→produce"三阶段心智模型，必要时清历史重开 session |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
