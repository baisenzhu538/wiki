---
id: "case-truman-ai-partner"
title: "案例：Truman AI Partner（阿蕊老师）——从十年笔记到可售卖的 Agent"
type: "case"
status: "draft"
domain:
  - "agent-infrastructure"
  - "yitang"
source_person: "Truman"
source_context: "一堂《AI时代清单体笔记》课程"
source_refs:
  - "00_inbox/一堂-AI时代清单体笔记-Truman-口述-01.txt"
  - "00_inbox/一堂-AI时代请单体笔记-Truman-口述-02.txt"
  - "00_inbox/Truman的个人成长五步法.png"
  - "00_inbox/truman的选择：两条职业成长路线.png"
tags:
  - "#boundary/not-for-creative"
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#confidence/verified-by-case"
  - "#domain/agent-infrastructure"
  - "#domain/yitang"
  - "#scene/agent-infrastructure/skill-registry"
  - "#scene/ai-collaboration/problem-validation"
  - "#scene/ai-collaboration/workspace-design"
  - "#scene/hardware-debugging/prototyping"
  - "#scene/knowledge-management"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/note-taking/checklist-method"
  - "#scene/note-taking/training-plan"
  - "#scene/skill-engineering/publish-deploy"
  - "#type/case"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "case-纪浩-skills-market"
  - "yt-note-ai-human-division"
  - "30_wiki/decisions/truman-ai-partner-design-analysis.md"
author: "legacy"
reviewed_by: "pending"
confidence: 0.7
trust_level: "low"
---

# 案例：Truman AI Partner（阿蕊老师）

> Truman 用十年时间积累 1500+ 篇清单体模型笔记，将其编译为领域知识库，封装成一个 P 角色的 AI agent，在一堂内部使用并计划单独售卖。

## 场景

Truman 在一堂教"清单体笔记"课程，学生在练习过程中需要反馈和指导。他对学生的笔记质量有明确的审美标准，但无法一对一辅导所有人。于是他把自己十年的笔记方法论、1500+ 篇模型笔记、以及对学生笔记的评判标准，封装成了一个 AI Partner。

## 四要素验证

### Before-After

| | Before | After |
|:---|:---|:---|
| 学生笔记反馈 | 无反馈，靠自己悟 | AI Partner 即时结构化整理 + 诊断 + 训练计划 |
| 方法论传播 | 靠上课讲，听完就忘 | 封装为 Agent，学生随时可用 |
| Truman 的时间 | 一对一辅导，不可规模化 | Agent 自动化 L1-L3，Truman 只做 L4-L5 |
| 知识资产化 | 笔记躺在 Obsidian 里 | 编译为可售卖产品 |

### 真实锚点

一堂真实学员的需求。Truman 看到学生在课程后"知道但做不到"，需要一个能在日常练习中持续提供反馈的工具。不是"AI 很火所以做一个"——是自己学生真需要。

### 受益人

- **学生**：有即时反馈，不用等 Truman 一对一
- **Truman**：知识资产化，从"卖时间"到"卖 Agent"
- **一堂**：课程附加值提升，AI Partner 作为课程的延伸产品

### 可解性

因果链：
1. 十年的结构化笔记（清单体格式）天然是 AI 可消费的知识格式
2. 明确的审美标准（分点/分层/独立行/原创占比）可转化为校验规则
3. P 角色 + L1-L2 边界的约束设计让 Agent 不会越界替人判断
4. "在词这一层就能把活干差不多"——从最浅层开始迭代

## 核心设计洞察：约束即能力

Truman 的设计有三个"反直觉"的约束：

| 约束 | 直觉反应 | 实际效果 |
|:---|:---|:---|
| **P 角色**（只管执行不探讨） | "AI 应该越聪明越好" | 防止越界替人思考，逼迫人保持 L3+ |
| **L1-L2 硬边界**（不建模不建议） | "AI 能做就应该让它做" | 输出是半成品，人必须亲手完成内化 |
| **清单体 I/O**（输入输出都是清单体） | "自然语言更灵活" | 强制结构化输入 → 倒逼人提高笔记质量 |

**每个约束看起来在"限制" AI，实际上在"保护"人。** 这是和"做个最强 AI"完全不同的设计哲学。

## 可迁移场景

1. **任何有明确方法论的领域专家**：律师的判断标准、医生的诊断流程、设计师的审美体系——只要有 100+ 案例积累，就可以按这个模式封装为 Agent
2. **教育培训产品**：不是卖课，是卖"能陪你练的 AI 教练"。课程是知识输入，Agent 是技能输出
3. **个人知识资产化**：黄药师的广冷调试经验（E-FM-001~004）、老顽童的卡片量产方法——只要有足够的操作记录，就可以编译为可复用的 Agent

## 反例

**什么时候不应该学这个案例**：
- 方法论还在探索阶段，没有 50+ 已验证的案例积累——知识基础不够，Agent 输出不可靠
- 领域需要强现场判断（如外科手术、面对面谈判）——Agent 无法获取现场的非语言信息
- 只是为了"做一个 AI 产品"而不是解决真实的使用问题——四要素验证不通过时不做

## 对 KDO 的启发

Truman 的 AI Partner 和纪浩的 Skills 市场是**同一模式的两个实例**：

| | Truman | 纪浩 |
|:---|:---|:---|
| 核心产品 | 单一 Agent（阿蕊老师） | Agent 分发平台 |
| 知识格式 | 清单体笔记 | 不限格式 |
| 方法论语料 | 1500+ 篇个人积累 | 团队协作积累 |
| KDO 等价物 | `kdo encapsulate` 编译单个 skill | `kdo skill list` + registry |

KDO 已经能走通 Truman 的单 Agent 路径（note-coach）。纪浩的平台模式是下一步——先把单个 skill 做扎实，再做分发层。
