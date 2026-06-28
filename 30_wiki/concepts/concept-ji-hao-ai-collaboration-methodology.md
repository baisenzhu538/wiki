---
id: concept-ji-hao-ai-collaboration-methodology
title: 纪浩 AI 协作方法论：从判断到规模复用的五层体系
type: concept
status: enriched
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论 分享（第三次分享，2026-06）
source_refs:
- 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
- 10_raw/sources/src_20260617_50e2866a-ai俱乐部-人和ai协作-纪浩-五层结构-结构化.md
- 10_raw/sources/src_20260617_15ca3bb2-ai俱乐部-人和ai协作-纪浩-参考案例-结构化.md
created_at: 2026-06-07
updated_at: '2026-06-28'
related:
- pending_unknown
- pending_unknown
- pending_unknown
- pending_unknown
- pending_unknown
pipeline:
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: L1 四要素验证缺失
  follow_up_question: 你能用一句话描述 Before-After 吗？受益人是谁？有没有真实锚点？
- framework_lens: L2 Agent Workspace 不完整
  follow_up_question: 你的领域知识、导诊台、工作手册、经验模式库、任务管理、日志是否都齐备？
- framework_lens: L5 Skills Market 未建立
  follow_up_question: 你的 Skill 描述是按 Agent 可自安装的方式写的，还是只给人看的说明？
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: low

---
# 纪浩 AI 协作方法论

> 纪浩是一堂的后端工程师。他在 AI 俱乐部的第三次分享中，用两小时讲述了自己过去四个月高强度 AI 协作的完整方法论——不是几个孤立技巧，而是一个从"判断该不该做"到"规模复用"的完整闭环。他的方法论和 Truman 的 AI Partner 设计哲学是同一套模式在不同场景下的应用：Truman 讲"为什么"，纪浩讲"怎么做"。

## Summary

纪浩的 AI 协作方法论是一个五层体系：L1 四要素验证（判断真需求）→ L2 Agent Workspace 设计（搭建 AI 的工作环境）→ L3 Do-first PDCA（从行动开始的迭代循环）→ L4 双三角模型（人让 AI 变强 ≠ AI 让人变强）→ L5 Skills Market（规模复用）。五层不是孤立的，是一条链——每一层是下一层的前提。贯穿始终的底层哲学：必要难度 + A+1 原则 + 保持手感 + "选择不用 AI 的权利"。

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 已有明确工作领域或真实问题 | L1 四要素验证要求能清晰描述 Before-After；探索阶段连问题都没有时，四要素无从验证 |
| ✅ 任务可重复、可结构化 | Agent Workspace 和 Skills Market 对一次性创意任务 ROI 低，更适合有重复执行场景的工作 |
| ✅ 执行错误的成本可接受 | Do-first PDCA 允许在行动中修正，但如果第一次 Do 的方向完全错误，后续迭代会加深错误 |
| ✅ 团队有持续维护意愿 | Workspace 五模块和 Skills Market 会随使用膨胀，没有维护预算会退化为信息坟场 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| **四要素凑数但无真实锚点** | 四要素表填满了，但 Before-After 来自想象，找不到具体用户、场景或可验证的数据 | 强制每个要素附一个可验证的事实或访谈记录；任意一项缺失即停止，先补调研 |
| **Workspace 变成资料坟场** | 导诊台、工作手册越写越长，AI 开始"找不到信息"或输出幻觉，同一条规则反复问 | 按"一次对话一个任务"做渐进式披露；每两周用日志驱动排查删除失效模块 |
| **PDCA 循环空转** | 从一步拆成八步，但每次 Check 只改提示词，不改 Workspace 结构或 Skill | 每次 Check 必须输出一个要改的结构（文档/规则/模板）；Act 阶段只改结构，提示词由结构自动生成 |
| **Skills Market 给人看而不是给 Agent 用** | Skill 描述写得像操作说明，Agent 无法按 capability 匹配、自安装或自上报 | 用"输入-能力-输出-反馈"四元组写描述；让 AI 根据描述自动生成安装说明和调用示例 |

## Claims

### 五层体系全景

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

### 和 Truman AI Partner 的对位

- src_unknown

- src_unknown

## Critique

### 内部局限

- src_unknown

- src_unknown

- src_unknown

### 外部攻击

#### Andy Matuschak 的"知识工作的隐性成本"

**Andy Matuschak**（*Why Books Don't Work* 作者，独立研究者，专注于学习和知识工具设计）对"把 AI 整合到知识工作流"提出了一个深层质疑：

- src_unknown

- src_unknown

- src_unknown

对纪浩体系的直接挑战：Matuschak 会说——**你的 Agent Workspace 是一个知识管理系统，但不是你的知识系统。** 你设计它让 AI 更好地工作，但它可能让你自己更不熟悉你本来应该熟悉的知识。你过去四个月高强度的 AI 协作中，有多少知识是从"AI 帮我处理"变成"我真的掌握了"的？

> **Matuschak 的敲命**："你给 AI 建了一个完美的 Workspace，五个模块、导诊台、渐进式披露。但我问你：你建完这个 Workspace 之后，你自己对这四个战场的知识理解——是更深了，还是更依赖 AI 了？如果明天 AI 不能用了，你还能用手和脑重新搭出这个 Workspace 里的核心知识吗？"

#### Don Norman 的"自动化悖论"

**Don Norman**（*The Design of Everyday Things* 作者，认知科学家，UX 之父）的研究揭示了自动化的深层矛盾：

- src_unknown

- src_unknown

- src_unknown

对纪浩体系的直接挑战：Norman 会说——**你的方法论让 AI 执行得太好了。** 正因为执行得好，人才会越来越依赖，技能才越来越退化。这不是设计缺陷，是自动化固有的悖论——系统越好用，人越退化。你的方法让 AI 高效执行，但有没有给"人必须自己执行"留出足够的空间？

> **Norman 的敲命**："你设计的 Agent Workspace 让 AI 工作得越来越顺。但你在设计的时候，有没有专门留出一些 AI **不能碰**的区域——不是因为它做不好，而是因为它做了你就会退化？如果你没有留，你的系统就是一个完美的退化加速器。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 技能落地 | [[tool-纪浩-真需求四要素验证法]] | L1 四要素验证——真需求的判断门禁 |
| 技能落地 | [[tool-纪浩-AI工作空间与导诊台设计法]] | L2 Agent Workspace 搭建——五大模块的搭建方法 |
| 技能落地 | [[tool-纪浩-Do-first-PDCA渐进迭代法]] | L3 Do-first PDCA——从行动开始的迭代流程 |
| 技能落地 | [[tool-纪浩-Agent技能市场设计法]] | L5 Skills Market——给 Agent 用的分发平台 |
| 技能落地 | [[tool-纪浩-日志驱动排查法]] | L5 日志驱动排查——规模复用的排查方法 |
| 暗知识 | [[dk-ji-hao-ai-cant-design-structure]] | "AI 不会自己搞结构设计，必须帮它搭" |
| 暗知识 | [[dk-ji-hao-simple-complex-routing]] | "简单系统跳过导诊台，复杂系统必须路由" |
| 暗知识 | [[dk-ji-hao-pdca-starts-from-do]] | "PDCA 从 Do 开始不是从 Plan 开始" |
| 暗知识 | [[dk-ji-hao-logs-fastest-ignored]] | "日志增长最快但最容易被忽视" |
| 案例 | [[case-纪浩-from-zip-to-five-layers]] | Skills 市场——给 Agent 用的分发平台 |
| 案例 | [[case-纪浩-focus-prompt-design]] | 聚焦提示词设计——四要素验证与导诊台的具体应用 |
| 对位 | [[case-truman-ai-partner]] | Truman AI Partner——同一套模式的哲学层表述 |
| 对位 | [[yt-note-ai-human-division]] | AI 时代笔记分工——纪浩的"人让AI变强≠AI让人变强"和 Truman 的分工边界是同构的 |

## 落地工具：纪浩五层体系项目启动检查清单

| 层级 | 检查项 | 通过标准 |
|:---:|:---|:---|
| L1 | 四要素是否都有真实锚点？ | 能说出至少一个具体用户/场景/数据，而非"应该会更好" |
| L1 | Before-After 能否一句话说清？ | 用"从 __ 变成 __"格式描述，且受益人可命名 |
| L2 | Agent Workspace 五模块是否已命名？ | 系统自述、领域知识、Agent 服务文档、任务管理、日志均有对应文档/目录 |
| L2 | 导诊台是否按场景而非分类组织？ | 一个入口对应一类高频任务，而非按"文档/代码/数据"分类 |
| L3 | 第一次 Do 是否有可验证的最小输出？ | 能在 30 分钟内得到一次 AI 产出，并据此做 Check |
| L3 | Check 是否指向结构改进而非提示词微调？ | 每次 Check 产出至少一条"要改的文档/规则/模板" |
| L4 | 是否明确人让 AI 变强的 manager 动作？ | 列出本任务中必须由人判断/验收的 3 个关键点 |
| L4 | 是否预留 AI 让人变强的挑战动作？ | 至少保留一个"不用 AI、手动完成"的子步骤以保持手感 |
| L5 | Skill 描述是否按 Agent 可自安装格式写？ | 包含输入、能力、输出、反馈四元组，AI 能据此生成安装说明 |
| L5 | 是否有复用路径（分类+capability+匹配规则）？ | 其他 Agent 能根据任务特征找到并调用该 Skill |

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|---|---|---|
| 创意发散阶段 | 五层体系是收敛工具，会把创意过早钉死在框架上 | 先用自由文本或脑图发散，待方向明确后再应用体系 |
| 个人无目标探索 | 连 Before-After 都想象不出来，四要素验证的前提不成立 | 先做快速原型，在行动中发现问题 |
| 紧急故障排查 | 先解决后验证，四要素会延误时机 | 先恢复服务，事后补充验证 |

## Action Triggers

| 触发条件 | 行动 | 预期结果 |
|---|---|---|
| 你准备让AI执行一个新项目时 | 先用四要素验证需求真实性，再搭建Workspace | 避免在假需求上浪费AI算力 |
| AI产出质量不稳定时 | 检查Workspace五大模块是否完整 | 快速定位问题的结构性根源 |
| 需要在团队内部复用AI配置时 | 把工作空间当作标准交付物 | 降低交接成本，确保团队成员能按图索骥 |
| 你发现AI在无效重复时 | 启动PDCA循环，从Do开始迭代 | 用循环代替盲目调参 |

## Feedback Path

- src_unknown
