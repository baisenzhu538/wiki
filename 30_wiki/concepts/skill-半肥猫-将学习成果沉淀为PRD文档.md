---
id: "skill-半肥猫-将学习成果沉淀为PRD文档"
title: "技能：将学习成果沉淀为 PRD 文档"
type: "skill"
status: "draft"
domain:
  - "ai-collaboration"
  - "learning"
source_person: "半肥猫"
source_context: "AI俱乐部-AI学习落地 分享"
source_refs:
  - "00_inbox/半肥猫-AI学习落地-口述.md"
tools_required:
  - "AIGC大模型"
  - "文档编辑工具"
prerequisite_skills:
  - "skill-半肥猫-边学边练边沉淀的AI学习法"
related:
  - "concept-半肥猫-ai-learning-toolification-methodology"
  - "skill-半肥猫-课程Skill化的八步工作流"
  - "skill-半肥猫-用YAML格式做知识库原子化标签"
  - "dk-半肥猫-atomic-no-standard"
created_at: "2026-06-07"
updated_at: "2026-06-07"
tags:
  - #domain/ai-collaboration
  - #domain/learning
  - #scene/ai-collaboration
  - #scene/business-analysis/conversion-rate
  - #scene/knowledge-management/atomization
  - #scene/knowledge-management/tagging
  - #scene/learning-methodology/feedback-loop
  - #scene/note-taking
  - #scene/skill-engineering/course-to-skill
pipeline:
  - #boundary/not-for-creative
  - confidence-draft
  - confidence-source-cited
  - confidence-verified-by-case
---

# 技能：将学习成果沉淀为 PRD 文档

## Summary

半肥猫强调的"沉淀习惯"是从"消耗品式学习"到"资产式学习"的核心转化。**工具会经常变，能力才是追求的终极目标**——但能力必须沉淀在可复用的文档里，才能被复用和传承。PRD（Product Requirement Document）不仅仅是产品文档，它是一种把"我知道了"变成"我可以用"的结构化方法。

## Claims

- claim:01 [conf=0.88] **沉淀是学习的终极目标，而不是副产品**。半肥猫的观察：大多数人学完一门课后，知识存在脑子里，两周后忘掉 80%。只有把学习成果沉淀为文档/工具/SOP/技能，才能让知识变成**可复利用的资产**

- claim:02 [conf=0.85] **PRD 是"能力外化"的最佳载体**。半肥猫强调不是写"笔记"，而是写"可以被别人用的产品说明书"。PRD 的结构（问题定义、目标用户、使用场景、功能描述、边界条件）能强制你把"我懂了"变成"别人能用"

- claim:03 [conf=0.82] **每次 AI 对话到阶段性成果时，就让 AI 写一份备忘录**。这不是额外工作，而是对话的自然延伸——"这一页我们聊到这里，请帮我整理一份备忘录"。这份备忘录就是沉淀

## 操作步骤

1. 完成学习/项目后整理全过程记录
2. 与 AI 讨论产品化可能性
3. 确定目标用户和使用场景
4. 让 AI 帮忙写 PRD 结构：问题定义、目标用户、使用场景、功能描述、边界条件
5. 对 PRD 做三轮检查：是否可执行、是否可复用、是否有边界

## 适用场景

- ✅ 学完一门方法论课程后需要落地
- ✅ 完成一个项目后需要复盘
- ✅ 希望将个人经验变成团队可复用的资产

## 不适用场景

- ❌ 纯消耗性学习（如阅读、听书）无需落地时
- ❌ 学习内容本身就是通用知识（如汉字、数学公式）
- ❌ 时间极度紧张，只能"学完就走"

## 工具/环境

- AIGC 大模型（用于协助整理 PRD 结构）
- 文档编辑工具（Notion、飞书、Obsidian 等）

## 常见失败模式

- 沉淀变成"记录流水账" → 没有产品化思维 → **用 PRD 结构强制产品化**
- 只沉淀了"做了什么"没沉淀"为什么这么做" → 无法复用 → **沉淀必须包含决策逻辑**
- 沉淀后不复盘、不更新 → 文档过时 → **定期回顾并更新沉淀**

## 为什么有效

沉淀是将"隐性知识"（在脑子里的）变成"显性知识"（在文档里的）的过程。PRD 的结构化形式确保了沉淀的质量——它不仅记录了"做了什么"，还记录了"为什么这么做"、"什么时候不该这么做"。

## Critique

### 内部局限

- **PRD 本身不保证质量**。半肥猫强调写 PRD，但如果 PRD 的作者对课程理解不深，那么 PRD 就是一份"粗糙的传声筒"——把错误的理解固化了。需要有一个质量门来审查 PRD

- **沉淀的维护成本被严重低估**。写一份 PRD 可能只需要 1 小时，但保持 PRD 最新、反馈最新业务变化，需要持续投入。大多数人写完 PRD 就不再看了

- **PRD 只是"文档"，不是"能力"。半肥猫说"工具会经常变，能力才是追求的"，但 PRD 不等于能力。能力需要反复练习才能内化，PRD 只是辅助工具

### 外部攻击

#### David Graeber 的"无意义工作"与"文档冒险"

**David Graeber**（*Bullshit Jobs* / *Debt: The First 5,000 Years* 作者）从社会学和组织行为学角度质疑这个沉淀流程：

- **你可能在制造无意义的文档**：Graeber 在 *Bullshit Jobs* 中描述了大量"看起来很忙但完全无用"的工作。"把学习成果沉淀为 PRD"可能就是这种工作的典型代表——你花了大量时间写文档，但这些文档可能永远不会被打开

- **PRD 可能是"仪式性的安全感"而非"真实的贡献"**：Graeber 会说，写 PRD 让人觉得自己"很专业"、"很系统化"，但如果这个 PRD 没有人用、没有人看、没有人更新，那它就是一种"让人觉得安心的仪式"

- **文档化本身可能是创造性的敌人**：当你把一个灵活的、流动的学习过程固化成 PRD 时，你可能在杀死那些尚未形成的、纤细的、非线性的理解。文档是"死的"，而学习是"活的"

> **Graeber 的拷问**："你说'工具会经常变，能力才是追求的'。那我问你：你沉淀的这些 PRD，有多少份被打开过？有多少份被人用过？有多少份被更新过？如果答案是'没有几份'，那你不是在沉淀能力——你是在制造文档垃圾。"

#### Seymour Papert 的"建构主义"与"玩耍的消亡"

**Seymour Papert**（*Mindstorms* 作者，MIT 媒体实验室联合创始人）从学习理论角度质疑这个沉淀流程：

- **沉淀可能在消灭玩耍的空间**：Papert 的核心观点是，深层学习发生在"玩耍"和"无目的探索"中。半肥猫的"每次对话到阶段性成果时就写份备忘录"，这可能把学习变成了一种"产出导向"的活动——每次都要产出"成果"，而没有空间让人"只是玩玩"

- **PRD 的结构可能是认知的监狱**：当你用 PRD 的固定结构来约束自己的思考时，你可能会错过那些"不符合结构但有价值"的观察。Papert 设计的 Logo 语言让孩子自由探索，而不是执行固定程序

- **真正的能力可能在 PRD 之外**：Papert 会说，能力不是存储在文档里的，而是通过持续的实践和探索建立的。一个从来不看 PRD 但经常实践的人，可能比一个写了 100 份 PRD 但从不实践的人更有能力

> **Papert 的拷问**："你的沉淀流程要求每次对话都产出一份文档。但你知道什么时候人们学得最好吗？是他们不知道自己在学习的时候。当你每次都要产出'成果'，就没有空间让人'只是玩玩'了。而'只是玩玩'恰恰是所有创造性发现的来源。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|----------|------|
| 上位 | [[concept-半肥猫-ai-learning-toolification-methodology]] | 沉淀是三层方法论的核心转化——消耗品变资产 |
| 下位 | [[skill-半肥猫-课程Skill化的八步工作流]] | 沉淀后的产品化路径 |
| 并行 | [[skill-半肥猫-用YAML格式做知识库原子化标签]] | 沉淀后的知识库管理方法 |
| 案例 | [[case-半肥猫-conversion-hacker-skill]] | 沉淀的完整实侍——转化率黑客 Skill |
| 暗知识 | [[dk-半肥猫-atomic-no-standard]] | 原子化没有固定标准——沉淀的切分需要灵活 |

## 来源

- 半肥猫，AI 俱乐部 AI 学习落地分享

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
