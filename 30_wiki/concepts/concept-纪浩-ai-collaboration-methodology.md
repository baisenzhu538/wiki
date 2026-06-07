---
id: "concept-纪浩-ai-collaboration-methodology"
title: "纪浩 AI 协作方法论：从判断到规模复用的五层体系"
type: "concept"
status: "draft"
domain:
  - "ai-collaboration"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享（第三次分享，2026-06）"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-笔记.txt"
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-提示词案例01.txt"
  - "00_inbox/AI俱乐部-人和AI协作-纪浩-提示词案例02.txt"
tags:
  - "#boundary/not-for-creative"
  - "#boundary/requires-human-judgment"
  - "#boundary/single-use-only"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#confidence/verified-by-case"
  - "#domain/ai-collaboration"
  - "#domain/yitang"
  - "#scene/agent-infrastructure"
  - "#scene/ai-collaboration/human-ai-division"
  - "#scene/ai-collaboration/pdca-execution"
  - "#scene/ai-collaboration/problem-validation"
  - "#scene/ai-collaboration/prompt-engineering"
  - "#scene/ai-collaboration/skill-market"
  - "#scene/ai-collaboration/workspace-design"
  - "#scene/knowledge-management"
  - "#scene/learning-methodology/deliberate-practice"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/learning-methodology/mental-models"
  - "#scene/note-taking/checklist-method"
  - "#scene/product-design/focus-workbench"
  - "#scene/skill-engineering/course-to-skill"
  - "#scene/skill-engineering/eval-testing"
  - "#scene/skill-engineering/publish-deploy"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "skill-纪浩-four-elements-validation"
  - "skill-纪浩-agent-workspace"
  - "skill-纪浩-dofirst-pdca"
  - "skill-纪浩-dual-triangle"
  - "skill-纪浩-progressive-disclosure"
  - "dk-纪浩-pdca-starts-from-do"
  - "dk-纪浩-ai-cant-design-structure"
  - "dk-纪浩-newbie-can-validate"
  - "case-纪浩-skills-market"
  - "case-纪浩-focus-prompt-design"
---

# 纪浩 AI 协作方法论

> 纪浩是一堂的后端工程师。他在 AI 俱乐部的第三次分享中，用两小时讲述了自己过去四个月高强度 AI 协作的完整方法论——不是几个孤立技巧，而是一个从"判断该不该做"到"规模复用"的完整闭环。他的方法论和 Truman 的 AI Partner 设计哲学是同一套模式在不同场景下的应用：Truman 讲"为什么"，纪浩讲"怎么做"。

## Summary

纪浩的 AI 协作方法论是一个五层体系：L1 四要素验证（判断真需求）→ L2 Agent Workspace 设计（搭建 AI 的工作环境）→ L3 Do-first PDCA（从行动开始的迭代循环）→ L4 双三角模型（人让 AI 变强 ≠ AI 让人变强）→ L5 Skills Market（规模复用）。五层不是孤立的，是一条链——每一层是下一层的前提。贯穿始终的底层哲学：必要难度 + A+1 原则 + 保持手感 + "选择不用 AI 的权利"。

## Claims

### 五层体系全景

- claim:01 [conf=0.90] **L1 四要素验证**是入口门禁。Question（疑问）满足好奇心，Problem（问题）需要行动改变现实。四个要素：Before-After 状态变化、真实锚点（具体场景非想象）、受益人（有人实打实受益）、可解性（有因果链和能力支撑）。四个要素不够，不要下场动手

- claim:02 [conf=0.88] **L2 Agent Workspace**是 AI 的工作环境。AI 是模式匹配系统，不会自己搞结构设计。必须由人帮它搭五个模块：系统自述/领域知识/Agent 服务文档(导诊台+工作手册+工具集+经验模式库)/任务管理/日志。信息按场景聚合，不按分类聚合

- claim:03 [conf=0.85] **L3 Do-first PDCA**逆转了传统认知。所有 PDCA 流程不是从 Plan 开始的，一定是从 Do 开始的——先动手解决具体问题，在过程中加检查（Check），根据问题制定小计划（Plan），再调整（Act）。循环从一步变成八步，Skill 在循环中自然长出来

- claim:04 [conf=0.85] **L4 双三角模型**区分了两件事：人让 AI 变强（人当 manager）≠ AI 让人变强（AI 当教练鞭策人走出舒适区）。前者不会自然导致后者——只有自己挑战自己才能变强

- claim:05 [conf=0.82] **L5 Skills Market**是规模复用的基础设施。给 Agent 用的，不是给人用的——Agent 按分类+capability 匹配 → 自己下载安装 → 自己上报反馈。写描述不要人写，人跟 AI 说清楚，AI 去补全

- claim:06 [conf=0.85] **信息组织原则：渐进式披露**。导诊台→工作手册→经验库→领域知识，知识越来越深。不是一次性把全部上下文扔给 AI，是按需一层层深入。一次对话只围绕一个任务

- claim:07 [conf=0.80] **贯穿始终的认知哲学**：必要难度（学习的本质是摩擦）+ A+1 原则（步子不要太大，走出舒适区一点点）+ 保持手感（不能用 AI 替代所有执行）+ 选择不用 AI 的权利（当 AI 搞不定的时候你能搞定，才有权利不用它）

### 和 Truman AI Partner 的对位

- claim:08 [conf=0.85] 纪浩五层和 Truman AI Partner 设计是同一套模式在不同场景下的应用。Truman 讲"为什么"（设计哲学），纪浩讲"怎么做"（工程方法）。对位关系：L1 四要素验证 ↔ P 角色+L1-L2 硬边界（做之前先约束）→ L2 Agent Workspace ↔ 1500 篇清单体笔记注入上下文（给 Agent 结构化信息环境）→ L3 Do-first PDCA ↔ Agent 封装循环迭代（从词这一层到单元模型层）→ L4 双三角 ↔ 约束即能力+磨刀石不是拐杖 → L5 Skills Market ↔ AI Partner 封装售卖

- claim:09 [conf=0.80] 纪浩的体系可以作为 KDO 建设 Agent 的标准作业程序——用四要素判断"要不要做"，用 Workspace 搭环境，用 PDCA 迭代，最后用 Skill 封装规模复用。note-coach 就是按这套流程走出来的第一个产品

## Critique

### 内部局限

- **五层的前提是"已经有明确的工作领域"**。纪浩的方法论对于已有明确工作方向的人（如他自己有四个战场：软件重构/电子/机械/推广）是高效的。但对于还在探索"我要做什么"的人，四要素验证的前提（能想象 Before-After）就不成立——你不知道解决前是什么状态，也不知道解决后想要什么状态

- **Agent Workspace 的维护成本被低估**。五大模块需要持续更新，尤其是经验模式库和任务管理——这两个模块会随着 AI 使用量增加而膨胀。纪浩自己承认"AI 接手任务变多后会出现混乱行为"，但给出的方案（目录结构设计）只是延缓膨胀，不是解决膨胀

- **Do-first PDCA 的隐含前提是"Do 的成本可接受"**。纪浩的 UI 设计例子中，从一步变成八步的 PDCA 是多次迭代的结果——但如果第一次 Do 就做错了方向，后续的 Check 和 Plan 可能都在错误的方向上加深。四要素验证作为前置门禁部分解决了这个问题，但不完全

### 外部攻击

#### Andy Matuschak 的"知识工作的隐性成本"

**Andy Matuschak**（*Why Books Don't Work* 作者，独立研究者，专注于学习和知识工具设计）对"把 AI 整合到知识工作流"提出了一个深层质疑：

- **隐性迁移成本**：Matuschak 会说，纪浩的 Agent Workspace 五大模块是一个复杂的知识管理系统。每次 AI 执行任务时，它需要从五个模块中提取和重组信息——这个提取过程的认知成本隐藏在"AI 帮我做了"的便利之下。当 AI 提取信息的方式和人类处理信息的方式不一致时（AI 是模式匹配，人是因果推理），产出的质量会系统性下降

- **知识的外化悖论**：Matuschak 的核心论点是：知识必须内化才能被有效使用。把知识全部外化到 Agent Workspace 的五个模块中，表面上增加了"AI 可访问的知识量"，但代价是减少了人的内化机会。Truman 的"新人的灾难"在这里以另一种形式出现——不是依赖 AI 记笔记，而是依赖 AI 管理所有知识

- **结构设计的不可外包性**：纪浩说"AI 不会自己搞结构设计，必须人帮它搭"。Matuschak 会追问：**人帮 AI 搭的结构，是人理解的结构吗？** 还是人在帮 AI 搭一个"AI 理解但人可能不理解"的结构？如果是后者，当 AI 按照这个结构执行任务时，人失去了对过程的可见性——你只知道输出质量如何，不知道中间逻辑是否正确

对纪浩体系的直接挑战：Matuschak 会说——**你的 Agent Workspace 是一个知识管理系统，但不是你的知识系统。** 你设计它让 AI 更好地工作，但它可能让你自己更不熟悉你本来应该熟悉的知识。你过去四个月高强度的 AI 协作中，有多少知识是从"AI 帮我处理"变成"我真的掌握了"的？

> **Matuschak 的拷问**："你给 AI 建了一个完美的 Workspace，五个模块、导诊台、渐进式披露。但我问你：你建完这个 Workspace 之后，你自己对这四个战场的知识理解——是更深了，还是更依赖 AI 了？如果明天 AI 不能用了，你还能用手和脑重新搭出这个 Workspace 里的核心知识吗？"

#### Don Norman 的"自动化悖论"

**Don Norman**（*The Design of Everyday Things* 作者，认知科学家，UX 之父）的研究揭示了自动化的深层矛盾：

- **自动化让人变钝**：Norman 的研究表明，当系统高度自动化时，操作者的技能会**系统性退化**——不是因为他们偷懒，而是因为系统替他们做了所有的微决策。微决策是维持技能敏感度的关键——每次你"决定该怎么记""判断该分几点""选择什么用词"都是在做微决策，而 AI 拿走这些微决策的那一刻，你的技能敏感度就开始退化

- **"恰到好处"的自动化才是最难的**：Norman 区分了三种自动化：完全自动化（人完全不用参与）、半自动化（人监督、必要时介入）、辅助增强（人主导、AI 辅助）。纪浩的体系在 L1-L2 层倾向于半自动化（AI 执行，人验证），但问题在于——验证是比执行更低的认知活动。你让 AI 写代码，你只做 code review——你的编码能力不会因为你 review 得多而变强

- **技能退化的不可逆性**：Norman 警告，技能的退化不仅难以检测（你无法感知自己正在变差），而且难以逆转。因为退化的不是知识（你知道什么是好代码），是**执行的神经回路**（你的手和脑如何协同写出好代码）。纪浩说"保持手感"，但 Norman 会说——如果你 80% 的执行交给 AI，你的手感是在衰减的，不是"保持"就能保持的

对纪浩体系的直接挑战：Norman 会说——**你的方法论让 AI 执行得太好了。** 正因为执行得好，人才会越来越依赖，技能才越来越退化。这不是设计缺陷，是自动化固有的悖论——系统越好用，人越退化。你的方法让 AI 高效执行，但有没有给"人必须自己执行"留出足够的空间？

> **Norman 的拷问**："你设计的 Agent Workspace 让 AI 工作得越来越顺。但你在设计的时候，有没有专门留出一些 AI **不能碰**的区域——不是因为它做不好，而是因为它做了你就会退化？如果你没有留，你的系统就是一个完美的退化加速器。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|----|---|
| 技能落地 | [[skill-纪浩-four-elements-validation]] | L1 四要素验证——真需求的判断门禁 |
| 技能落地 | [[skill-纪浩-agent-workspace]] | L2 Agent Workspace 搭建——五大模块的搭建方法 |
| 技能落地 | [[skill-纪浩-dofirst-pdca]] | L3 Do-first PDCA——从行动开始的迭代流程 |
| 技能落地 | [[skill-纪浩-dual-triangle]] | L4 双三角协同——人让AI变强 vs AI让人变强 |
| 技能落地 | [[skill-纪浩-progressive-disclosure]] | 渐进式披露——按场景聚合、四层递进 |
| 暗知识 | [[dk-纪浩-pdca-starts-from-do]] | "PDCA 从 Do 开始不是从 Plan 开始" |
| 暗知识 | [[dk-纪浩-ai-cant-design-structure]] | "AI 不会自己搞结构设计，必须帮它搭" |
| 暗知识 | [[dk-纪浩-newbie-can-validate]] | "新手也可以用四要素验证——工具是假设、调研、访谈、问AI、做实验" |
| 案例 | [[case-纪浩-skills-market]] | Skills 市场——给 Agent 用的分发平台 |
| 案例 | [[case-纪浩-focus-prompt-design]] | /focus 设计——结构化 prompt 的产品设计实例 |
| 对位 | [[case-truman-ai-partner]] | Truman AI Partner——同一套模式的哲学层表述 |
| 对位 | [[yt-note-ai-human-division]] | AI 时代笔记分工——纪浩的"人让AI变强≠AI让人变强"和 Truman 的分工边界是同构的 |
