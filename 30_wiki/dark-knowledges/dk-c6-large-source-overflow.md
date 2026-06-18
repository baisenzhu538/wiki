---
id: dk-c6-large-source-overflow
title: C-6：大源文件导致 session 容量超载→produce 骨架生成但内容填不进去
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- 20_memory/corrections.md#C-6
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[dk-c10-batch-tool-no-dry-run]]'
- '[[master-first-principles]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: '`kdo produce` 只输出章节标题和空段落，draft 字段无实质内容'
  framework_lens: '大文件编译已耗尽当前 session 的 context window，produce 阶段没有足够 token 填充内容'
  follow_up_question: '检查源文件大小是否超过 100KB；如是，启动新 session 仅执行 produce，并将编译结果结构化传入'
- signal: '审查者反馈卡片"内容空洞"，但作者认为 produce 已成功运行'
  framework_lens: '混淆了"骨架生成"与"内容填充完成"两个不同里程碑'
  follow_up_question: '人工检查 draft 是否有案例、数字、关联说明；如只有标题/模板，则回到新 session 重新 produce'
- signal: '同一 session 内先跑三步编译法再跑 produce，大源文件（>100KB）必然出现产出 truncated'
  framework_lens: 'Agent 手动编译模式下，编译与产出两阶段叠加超出 LLM context window 物理上限'
  follow_up_question: '强制分 session：当前 session 只完成编译和 angle 确认，新 session 负责 produce 填充'
---
# C-6：大源文件导致 session 容量超载→produce 骨架生成但内容填不进去

## 原始表述

> 一堂原文 207KB（~10 万字+），三步编译法用掉大部分 session 容量。概念卡完成后 `kdo produce` 只生成了骨架，artifact 没有空间填充。
>
> 根因：当前模式（Agent 手动编译）下，大文件的编译和 artifact 填充在同一 session 内无法完成。
>
> 修正：大文件编译后，artifact 填充应放在新 session 中执行，或先确认角度/方向再启动填充 session。produce 骨架生成不算完成，draft 非空才算。

## 核心洞察

C-6 的本质不是"文件太大"，而是**把两个高消耗阶段硬塞进同一 session 导致的系统性失败**。三步编译法（浓缩→质疑→对标）本身就要吃大量 context；produce 阶段又需要足够的 token 来生成结构化、有案例、有论证的 artifact。两者叠加后，大文件场景下必然发生"前端吃饱了、后端饿死了"的截断。这一规律在任何 Agent 手动编译、单 session 执行的 LLM 工作流中都成立：context window 是硬约束，不能绕，只能重新切分阶段。

## 使用场景

- 你要处理 100KB+ 的大源文件（如长篇报告、完整课程文稿、大型调研文档），准备用三步编译法生成概念卡
- 你运行三步编译法（浓缩→质疑→对标）后，发现 session 的 context window 已消耗大半
- 你紧接着运行 `kdo produce` 生成 artifact，结果只得到一个空有标题和章节结构、没有实质内容的骨架
- 你判定一张卡片"已完成"，但审查者反馈"内容空洞"——需要确认是编译质量差还是 produce 阶段没填进去

## 操作方法

1. **评估文件大小**：处理前先看源文件体积——超过 100KB 即视为大文件，需要分 session 策略
2. **第一阶段：编译（当前 session）**：完成三步编译法（浓缩→质疑→对标），产出概念卡的核心观点、关键证据和结构
3. **确认角度/方向**：编译完成后，先明确卡片的核心 angle 和关键结论——不要直接进入 produce
4. **第二阶段：填充（新 session）**：启动新 session，将编译结果（核心观点、结构、关键证据）作为输入，执行 `kdo produce`
5. **判定完成标准**：produce 骨架生成 ≠ 完成。必须人工检查 draft 非空、内容有实质填充（案例、数字、关联说明），才算完成

## 适用边界

- 适用于**Agent 手动编译模式**：人在 loop 中，需要分阶段操作
- **不适用于全自动管线**：如果管线设计为单 session 完成全部操作，大文件需要特殊处理（如预切分、摘要提取），不能直接套用 C-6 的分 session 方案
- session 分割会增加上下文切换成本——小文件（<50KB）不需要分 session，直接一次完成更高效
- 如果 LLM context window 足够大（如 200K tokens+），100KB 的阈值可以上调，但"编译→产出"两阶段分离的原则仍然成立
- 分 session 策略的前提是"编译结果可以结构化传递"——如果编译产出是自由文本而非结构化数据，新 session 可能丢失关键上下文

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:-----|:-----|
| 单 session 内编译+produce 超载 | `kdo produce` 只生成标题骨架，正文为空或严重 truncated | 编译完成后开新 session，将结构化编译结果传入再 produce |
| 未确认 angle 就进入 produce | 新 session 中 produce 方向漂移，填充内容与原始源文件重点不符 | produce 前先明确核心结论、关键证据、卡片 angle，并写入结构化笔记 |
| 误判"骨架生成 = 完成" | 卡片状态标记为完成，但 draft 无实质内容 | 建立完成标准：draft 必须含案例/数字/关联说明，骨架 alone 不算 |
| 小文件盲目套用分 session | <50KB 文件也分 session，增加上下文切换成本 | 小文件直接单 session 完成；仅 100KB+ 或 context 消耗过半时才分 session |
| context window 很大就忽视两阶段分离 | 200K+ 模型处理大文件时仍可能因长对话历史导致后续 produce 空间不足 | 无论窗口多大，保持"编译→确认→produce"三阶段心智模型，必要时清历史重开 session |

## 为什么值钱

- 这是 KDO 工作流与 LLM context window 物理限制**碰撞产生**的约束：三步编译法 + produce 两阶段叠加，对大文件必然超载
- 通用项目管理不会告诉你"207KB 的文件要分两个 session 处理"——这个阈值和策略是 KDO 在 一堂素材 上踩出来的具体数字
- **"produce 骨架生成不算完成，draft 非空才算"** 是一条判定标准，不是通用原则。很多 Producer 会误以为"结构有了 = 快完成了"，实际上内容填充才是大头
- 任何 AI 训练语料中都不会有"KDO 的大文件编译需要分 session，阈值约 100KB"这条知识——这是具体工具链、具体模型、具体工作流三者叠加的产物

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一深层模式：流程设计缺陷导致内容损失。C-10 是"跳过验证步骤导致内容被覆盖"，C-6 是"压缩步骤到单 session 导致内容填不进去"——两者都是"流程设计没有尊重系统硬约束"
- [[master-first-principles]] — 第一性原理：LLM context window 是物理硬约束，不能绕，只能分。C-6 是"回到物理约束重新设计流程"的具体实践
- `20_memory/corrections.md` → C-6（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
