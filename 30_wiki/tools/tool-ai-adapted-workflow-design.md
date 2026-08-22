---
id: tool-ai-adapted-workflow-design
title: AI 适配化工作流设计：四员分工+占位符防魔改+规则文件前置（十指讲香）
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
- AI适配化工作流
- 十指讲香工作流
- 四员分工
- 占位符防魔改
- 规则文件前置
- AI落地Live86
- AI落地Live86-龙虾员工实践-逐字稿
- kinda龙虾
tags:
- audience:manager
- scene:execution
- skill-level:advanced
source_person: kinda
source_context: 一堂 AI 俱乐部落地 Live86·龙虾员工实践（2026-08-19）——AI 适配化能力（L500-535）
source_refs:
- 00_inbox/AI落地Live86-龙虾员工实践-逐字稿.md
related:
- '[[framework-一堂-个人表达力]]'
- '[[dk-rule-not-system-capability]]'
- '[[dk-ai-capability-illusion]]'
- '[[case-kinda-digital-employees-fullview]]'
- '[[tool-anti-ai-bs-three-moves]]'
- '[[framework-multi-agent-collab-chain-six]]'
- 'tool-platform-requirement-eight-sections'
- '[[dk-ai-efficiency-and-management-radius]]'
---
# AI 适配化工作流设计：四员分工+占位符防魔改+规则文件前置（十指讲香）

> **定位**：属于 [[framework-一堂-个人表达力]] 的 AI 化落地——把人类工作流程改造成 AI 能稳定执行的工作流，核心解决 LLM 魔改问题

## 1. 工具定义

AI 适配化 = 将人类的工作流程变成适合 AI 的工作流程（L500）。十指讲香工作流是最佳案例：把"人类优化一篇稿子"的过程，拆成 AI 可稳定执行的流水线，用**四员分工+占位符防魔改+规则文件前置**三件套解决 LLM 魔改（捏造事实/内容顺序变化）问题（L504-505）。

## 2. 为什么需要

- LLM 直接优化文本会**魔改**：捏造不存在的事实、内容顺序变化（L504-505）
- 让 AI 自己设计工作流（建模专家提的方案）解决不了问题（L507）
- 人类先想"人怎么做"再翻译成 AI 流程=设计思路（L509-515）

## 3. 使用步骤

**第一步：人类流程还原**（L509-515）——人怎么做十指优化：
1. 按十指讲香标准筛查，分需要/不需要优化
2. 需要优化的套用造句结构（套上就有 70-80 分）
3. 整体检查

**第二步：翻译成 AI 工作流**（L516-535）：
1. 建立足够多的句式结构库（L517）
2. 根据句式筛选需要/不需要优化的内容（L518）
3. **拆分成多文件**：文档 1=不需要修改的内容+需要修改的内容用占位符占位；文档 2/3…=需要优化的各部分（L519-523）——**占位符防魔改**
4. 需要优化的文稿用句式库固定句式优化（L524）
5. **质检**：防止 LLM 魔改（L525）
6. 质检通过后给修改建议和评分（L526）
7. **规则文件前置**：环节开始前先推送规则文件再让 LLM 修改（L527）——skill 设计思路

**第三步：四员分工**（L529-534）——每个环节一个专人：
- **调查员**：拿指引做内容划分（需要/不需要优化）
- **填空员**：拿优化指引做填空优化
- **质检员**：拿质检标准检查违规
- **评分员**：评分+输出优化建议

## 4. When NOT to Use

- **短内容**（一两句话）——直接对话即可，不需要工作流
- **AI 魔改风险低**的场景（结构化数据整理）——规则前置即可，不必四员分工
- **创意性任务**（需要 AI 自由发挥）——强流程会扼杀创意

## 5. 失败模式

| 失败模式 | 信号 | 修复 |
|:--|:--|:--|
| 魔改漏网 | 质检过了但仍有捏造 | 质检标准更严+人终审（L383 有些建议要人判断修改） |
| 流程过重 | 简单任务套大工作流 | 按内容长度/风险分级 |
| 句式库不足 | 优化卡住/套用生硬 | 扩充句式结构库 |
| 优化≠内容质量 | 用户误以为工作流=质量 | 明确工作流只解决表达，内容质量靠人（L385） |

## 6. Action Triggers

- LLM 直接改文本出现魔改/顺序乱 → 用占位符拆分+规则前置
- 需要批量统一风格的内容（演讲稿/产品描述/简历）→ 十指讲香工作流+衍生版本（L386）
- 团队 AI 产出格式不一致 → 四员分工+规则文件前置

## 7. 与其他知识的关联

- `framework-一堂-个人表达力`：十指讲香方法论（本 tool 的 AI 化落地）
- `dk-rule-not-system-capability`：规则封装成 Skill/MCP（规则前置的延伸）
- `dk-ai-capability-illusion`：工作流只解决效率，方法对错人把关
- `case-kinda-digital-employees-fullview`：十指讲香项目全景
- `tool-anti-ai-bs-three-moves`：质检环节=防忽悠的延伸
- `framework-multi-agent-collab-chain-six`：四员分工=协作链微观版
