---
id: framework-multi-agent-collab-chain-six
title: 多 Agent 协作链六环节：管理读写关系，让上下文一轮轮变厚
type: framework
status: pending_review
author: 老顽童
reviewed_by: 待审
confidence: 0.88
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- knowledge-management
- ai-collaboration
aliases:
- 多Agent协作链
- 协作链六环节
- 管理读写关系
- 上下文一轮轮变厚
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- OCR_批注 2026-08-15 215606
- OCR_批注 2026-08-15 215606.md
- AI知识库
tags:
- audience:executor
- scene:execution
- skill-level:advanced
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——Skill 封装实战（批注 215606 已人工核验）
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
- 00_inbox/AI知识库/OCR_批注 2026-08-15 215606.md
related:
- '[[framework-truman-agent-team-architecture]]'
- '[[concept-session-vs-memory-vs-document]]'
- '[[framework-dual-center-feishu-obsidian]]'
- '[[framework-knowledge-five-leaps]]'
- '[[framework-knowledge-compound-rocket-six]]'
- '[[tool-nine-character-mantra-14-strategies]]'
- '[[dk-research-important-things-must-do]]'
- '[[bridge-how-to-know-person-to-business]]'
---

# 多 Agent 协作链六环节：管理读写关系，让上下文一轮轮变厚

> 本卡属于「AI×知识管理」体系（楚门探索营第三次飞跃·Skill 封装实战，批注 215606 图已人工核验，L1132-1144）：多 Agent 协作的核心不是管理 Agent，而是**管理每一步的读写关系，让上下文一轮轮变厚**（金句 13）。六个 Agent 各司其职，共享一个知识库，全程对文档工作不对窗口工作。

## 1. 核心洞察

传统方式=传纸条（TCP-R 传文档复制粘贴低效工作，L1144）；上下文模式=一堆 AI 专家坐在一圈桌子上，面对一个知识库工作（L1122）。六环节协作链：**Antigravity（搜学）→Trae（翻译改写）→Antigravity+Claude（建模）→YAI（封装纠偏）→OpenClaw（影子分身学习）→Truman+Stella（报告沉淀）**——每个环节把成果写进知识库，下一环节基于文档继续，上下文一轮轮变厚。

## 2. 六环节读写关系

| 环节 | Agent | 读什么 | 写什么 | 口述锚点 |
|:--|:--|:--|:--|:--|
| ① 搜学 | Antigravity | 网上最佳实践 | 原始案例文档 | L1136-1138 |
| ② 翻译改写 | Trae | 原始文档 | 翻译+解读文档（10 层解读） | L1138-1139 |
| ③ 建模 | Antigravity+Claude | 翻译解读文档 | 建模文档（指南/框架） | L1140 |
| ④ 封装纠偏 | YAI | 建模文档 | Skill 文档（10 ToDo+10 NoToDo） | L1142 |
| ⑤ 学习执行 | OpenClaw（龙虾） | Skill 文档 | 调研报告/作业 | L1074-1096 |
| ⑥ 沉淀 | Truman+Stella | 报告 | 私人文档/技能库/项目库 | L1126-1130 |

## 3. 全程对文档工作

- 核心动作：下载官方 skill-creator → Trae 翻译 → Antigravity+Claude 建模萃取 → YAI 纠偏（改十几轮：优先级/SBC/完备性）→ 交叉打分验证（权威阅读+思维启蒙双 Agent）→ 封装 YAI → 龙虾现场学 → 产出报告（咨询公司达不到的水平，L1088）
- 金句："别老盯着 Agent 干活，你等的是文档——下属去调研，你会盯着他喝水打印吗？"（金句 12）
- 全程几乎没手输内容，全是 AI 生成+AI 读写（L1110）

## 4. When NOT to Use

1. **单 Agent 任务**——一个 Agent 能完成的不需要六环节链。
2. **无知识库基础**——六环节依赖共享知识库（没有它就退化为传纸条）。
3. **流程未成熟**——前几次用最贵模型+人工改十几轮（L1024-1038），成本高，适合重要任务。

## 5. 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| 传纸条模式 | 复制粘贴文档来回传 | 建共享知识库，管理读写关系 |
| 环节漏写 | 上下文没变厚/各环节脱节 | 每环节强制"写进知识库"再交接 |
| 不纠偏 | Skill 质量差 | YAI 改十几轮+10 ToDo+10 NoToDo+交叉打分 |
| 盯窗口 | 人一直盯着 Agent 对话 | 盯文档交付物（报告/指南） |

## 6. Action Triggers

- 搭建多 Agent 流水线 → 按六环节分工（搜学/翻译/建模/封装/学习/沉淀）
- 多个 AI 工具协作低效 → 检查是否共享知识库（没有=传纸条）
- Skill 封装 → 全程对文档工作：下载→翻译→建模→纠偏→验证→封装

## 7. 与其他知识的关联

- `framework-truman-agent-team-architecture`：六环节=Agent 团队的单次任务流水线
- `concept-session-vs-memory-vs-document`：文档中心=六环节的载体（不依赖 Session）
- `framework-dual-center-feishu-obsidian`：Obsidian=六环节共享的知识库中心
- `framework-knowledge-five-leaps`：六环节=第三次飞跃（Skill 封装）的实战
- `framework-knowledge-compound-rocket-six`：协作化引擎=六环节的机制
- `tool-nine-character-mantra-14-strategies`：人主导多 Agent 的对话控制（纠偏）
- `dk-research-important-things-must-do`：饱和式输出——调研环节的纪律
- `bridge-how-to-know-person-to-business`：理解人与企业——调研目标（跨域）
