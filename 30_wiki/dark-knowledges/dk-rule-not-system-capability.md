---
id: dk-rule-not-system-capability
title: 靠提醒=规则没变成系统能力：规范必须封装成 Skill/MCP 才生效
type: dk
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
- 靠提醒规则没变成系统能力
- 规范封装成Skill
- AI自觉不可行
- 规则前置
- AI落地Live86
- AI落地Live86-龙虾员工实践-逐字稿
- kinda龙虾
tags:
  - audience:manager
  - scene:execution
  - skill-level:intermediate
  - 工作流
  - 数字员工
  - MCP
  - 工具
  - 方法
  - 边界
  - 实证
  - 口述
source_person: kinda
source_context: 一堂 AI 俱乐部落地 Live86·龙虾员工实践（2026-08-19）——建模专家规则失效（L341-357、L542-546）
source_refs:
- 00_inbox/AI落地Live86-龙虾员工实践-逐字稿.md
related:
- '[[tool-ai-adapted-workflow-design]]'
- '[[tool-agent-white-paper-five-elements]]'
- '[[dk-aesthetic-redline-doc]]'
- '[[case-kinda-digital-employees-fullview]]'
- '[[dk-ai-self-evolution-prompt]]'
- '[[framework-multi-agent-collab-chain-six]]'
- 'dk-agent-parallel-design-system'
- 'case-openclaw-selfbuilt-agent-platform'
- 'tool-local-search-repo-datasource-engineering'
- 'tool-platform-requirement-eight-sections'
- '[[dk-best-datasource-is-floor]]'
---
# 靠提醒=规则没变成系统能力：规范必须封装成 Skill/MCP 才生效

> **定位**：属于 [[tool-ai-adapted-workflow-design]] 的认知前提——"提醒 AI 遵守规则"是幻觉，规则只有封装进系统才真正生效

## 原始表述

> 「好用是好用，但是建模专家总是不按照已经定好的规则和流程来提炼，每次都要提醒。这时候我又遇到了一个很典型的问题：如果每次都靠我提醒 AI 遵守规则，那这个规则其实没有真正变成系统能力。」（L341-343）
> 「结果实测下来发现全靠 AI 自觉是不可行的，他们还是很喜欢自由发挥。有时候即使你提醒了他们还是不想按照你要求做的。这个事情其实最好的解决方法是什么？把这个规范封装成 Skill，甚至可以做成 MCP 里面的工作流。」（L542-546）

## 使用场景

- AI 反复不遵守既定规则/格式要求时（每次都要人提醒）
- 团队需要 AI 产出保持一致格式/标准时
- 规则是"约定俗成"但没进系统（靠口头/文档提醒）时

## 操作方法

1. **识别"提醒依赖"**：同一规则被提醒 2 次以上=提醒依赖信号（L341）
2. **别修行为，修系统**：不靠"再提醒一次"，把规则封装成 Skill/MCP 工作流（L545）
3. **dify 弯路与 MCP 正解**：kinda 先试 dify 可视化工作流（L347-353）失败→提炼专家自建 MCP（L357）——"万能插头"让 LLM 连接外部工具
4. **gateway 减负**：能剥离到 MCP 的功能都放 MCP（gateway 超 1GB 卡死，L363-372）
5. **规则前置**：工作流环节开始前先推送规则文件再让 LLM 修改（L527）

## 适用边界

- 适用于**可重复的标准动作**（格式/流程/红线）；开放创造性任务不需要强规则
- 需要 AI 具备 Skill/MCP 能力；纯对话式 AI 无法持久遵守
- "靠提醒"在个别低风险场景可容忍（kinda 也接受部分 BUG 不修，L272），但高频/高风险必须系统化

## 为什么值钱

- **规则从"人肉驱动"变"系统驱动"**：不靠提醒=解放人的注意力（L298 使用 AI 很费注意力）
- **KDO 同构**：诊断文件对照——kinda"靠提醒→封装 Skill"与 KDO"纪律文案→门禁脚本（#363/#375）"哲学完全同构——我们刚走完同样的路
- **防魔改**：规则文件前置=O0 零编造的系统化落地（十指讲香质检环节）

## 跨案例实证（#400 补强 · 第二案例+解法）

> OpenClaw 数字员工搭建者（口述 L348-370, L636-650）

- 「建模专家他总是不会按照自己定好的规则跟流程来做提炼……每次都要靠提醒他……如果每次都要靠提醒，这个规则没有真正变成系统能力。」（L348-352）——与楚门案例同规律
- 解法：「AI 全靠自身自觉是不行的……最好的解决方法把它封装成 Skill 或者 MCP/Workflow。」（L642-650）——规则封装为系统能力被第二案例证实（跨案例置信度上调）


## Critique

- **反驳**：封装成 Skill/MCP 成本高，小规则不值得？——按频率和风险分级：高频/高风险必须系统化，低频低风险可容忍提醒。
- **反驳**：MCP 也有 BUG（kinda 自己留了很多未修）？——对，但"基本可用"已远超"每次提醒"；迭代期接受不完美（L272）。
- **条件**：此 dk 前提=规则本身清晰可编码；规则模糊时先解决规则问题再封装。
- **注意**：封装不等于一劳永逸——规则会变，Skill/MCP 要迭代维护。

## 与其他知识的关联

- `tool-ai-adapted-workflow-design`：规则前置=工作流设计原则之一
- `tool-agent-white-paper-five-elements`：白皮书定义规则起点（虚拟人格/职责）
- `dk-aesthetic-redline-doc`：红线文档化+强制检查（楚门课同族）
- `case-kinda-digital-employees-fullview`：建模专家规则失效案例
- `dk-ai-self-evolution-prompt`：AI 自进化（系统化规则的延伸）
- `framework-multi-agent-collab-chain-six`：协作链中规则承载
