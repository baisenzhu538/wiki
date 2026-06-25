---


id: case-ai-assisted-review
title: 案例：一堂用 AI 做复盘——从 Before/After 对比到 AI 自己复盘自己
type: case
source_refs:
  - "10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md"
status: enriched
domain:
- yitang
- modeling
- ai
source_person: Truman
source_context: 一堂高阶建模能力培训（AI 辅助复盘案例） （单一 source 为完整长文档，内容充分支撑 high trust） （单一 source，P1
  收尾时从 high 降为 medium，待补充第二来源或充分验证后再升回 high）
created_at: '2026-06-14'
updated_at: '2026-06-18'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-18'
trust_level: medium
confidence: 0.88
related:
  - '[[dk-modeling-ai-judgment-limit]]'
  - '[[dk-modeling-ai-compound-leverage]]'
  - '[[dk-wanghuan-ai-lifts-personal-ceiling]]'
  - '[[dk-modeling-ai-without-judgment]]'
  - '[[dk-wanghuan-standard-by-iteration]]'
- '[[case-ai-agent-milestone-design]]'
- '[[case-truman-ai-skill-engineering-guide]]'
- '[[dk-modeling-ai-iterative-prompting]]'
tags:
- '#method/modeling'
- '#content-format/case-study'
- '#domain/ai'
- '#method/evaluation-method'
- '#method/learning-method'
diagnostic_signals:
- signal: 团队有大量反馈、纠偏、复盘工作，人工整理慢且容易遗漏
  framework_lens: AI 辅助对比与合并可显著降低复盘成本
  follow_up_question: 你是否经常需要对比 Before/After 版本，或从大量协作记录中提炼 checklist？
- signal: 同一类工作反复踩坑，每次都要重新沟通纠偏
  framework_lens: 缺少把经验封装成可复用 Skill 的习惯
  follow_up_question: 你做完一个项目后，会不会让 AI 立刻扫描协作记录并封装成自查清单？
- signal: 复盘不及时，过几天关键信息就找不回来
  framework_lens: 记忆衰减和信息丢失是隐性成本
  follow_up_question: 你的复盘是在工作完成后 24 小时内完成，还是等到下次再做类似工作时才想起？
- signal: AI 输出后没有二次判断，直接当成最终结论
  framework_lens: 人必须负责审美判断和建模
  follow_up_question: 你拿到 AI 的复盘结果后，是否会基于自己的判断力做二次总结和边界修正？
---
# 案例：一堂用 AI 做复盘——从 Before/After 对比到 AI 自己复盘自己

> **Burn line**: AI 不仅能帮人复盘，还能自己复盘自己，把一次经验变成下一次的基础。

---

## 用一句话讲清楚

把 AI 当成复盘助手：先让它对比 Before/After 提炼洞察，再让它扫描协作记录并封装成可复用 Skill；人只做审美判断和最终建模，从而把一次性经验转化为持续复利。

---

## 核心要点

1. **AI 复盘有两个层次**：第一层是 AI 帮助人复盘（Before/After 对比）；第二层是 AI 自己复盘自己（扫描协作记录并封装 Skill）。
2. **Before/After 对比是低垂果实**：把上一版和最终版同时丢给 AI，它能发现人容易忽略的差异、洞察和可复用 tips。
3. **AI 自己复盘自己需要指定边界**：告诉 AI 扫描哪些工具/数据库、合并哪些反馈、封装成什么形式的 Skill。
4. **及时性决定复盘质量**：做完立刻复盘，否则记忆衰减、聊天记录和文档信息可能找不回来。
5. **人始终负责审美判断**：AI 提炼，人做二次总结、建模和最终决策。

---

## 诊断信号

| 信号 | 镜头 | 追问 |
|:-----|:-----|:-----|
| 团队有大量反馈、纠偏、复盘工作，人工整理慢且容易遗漏 | AI 辅助对比与合并可显著降低复盘成本 | 你是否经常需要对比 Before/After 版本，或从大量协作记录中提炼 checklist？ |
| 同一类工作反复踩坑，每次都要重新沟通纠偏 | 缺少把经验封装成可复用 Skill 的习惯 | 你做完一个项目后，会不会让 AI 立刻扫描协作记录并封装成自查清单？ |
| 复盘不及时，过几天关键信息就找不回来 | 记忆衰减和信息丢失是隐性成本 | 你的复盘是在工作完成后 24 小时内完成，还是等到下次再做类似工作时才想起？ |
| AI 输出后没有二次判断，直接当成最终结论 | 人必须负责审美判断和建模 | 你拿到 AI 的复盘结果后，是否会基于自己的判断力做二次总结和边界修正？ |

---

## Background

- **场景**：团队日常大量反馈、纠偏、复盘工作
- **问题**：人工复盘慢、有盲区、成本高
- **目标**：用 AI 加速复盘，把经验沉淀为可复用资产
- **来源**：`src_20260614_8269ccdb#1148-1218`

---

## What Happened

### 实践 1：AI 帮助人复盘

- **对象**：直播通知文案
- **方法**：把 Before（上一版）和 After（最终版）丢给 AI
- **AI 输出**：自动发现两版区别、提炼洞察、总结成 checklist
- **人再加工**：基于 AI 洞察二次总结和建模

效果：人能看出很多区别，AI 能发现更多隐藏洞察。

### 实践 2：AI 自己复盘自己

- **对象**：Truman 两周前让多个平台做课程插图和 PPT 的过程
- **方法**：
  1. 让 AI 扫描多个工具/数据库中的协作记录
  2. 合并同类项所有反馈
  3. 自动封装成一个 Skill："Design Case"
- **Skill 内容**：
  - 使用场景
  - 审美底盘
  - 协作流程（先发散再收敛、先看懂参考、每轮只搞一个主问题）
  - 评审表
  - 不同类型图的注意事项
  - 常见硬性坑

### 关键原则

- **及时**：做完立刻复盘，否则记忆会丢失、信息会消失
- **指定边界**：告诉 AI 主题和扫描范围
- **人只负责审美判断**：AI 干活，人拍板

---

## 关键证据

- **证据 1 [conf=0.9]**：Truman 说"AI 帮助人复盘"和"AI 自己复盘自己"是两个层次。——来源：`src_20260614_8269ccdb#1176-1180`。
- **证据 2 [conf=0.85]**：AI 扫描协作记录后封装出的 Design Case Skill 比 Truman 想象的好。——来源：`src_20260614_8269ccdb#1194-1202`。
- **证据 3 [conf=0.8]**：Truman 强调要及时复盘，因为过几天信息就找不回来了。——来源：`src_20260614_8269ccdb#1206-1208`。

---

## 可迁移场景

| 场景 | 如何套用 |
|---|---|
| 文案迭代 | Before/After 对比 → AI 提炼洞察 → 人确认 |
| 设计反馈 | 扫描协作记录 → AI 合并同类项 → 封装成 Design Skill |
| 项目复盘 | 让 AI 扫描文档/聊天记录 → 生成复盘报告 |
| 个人成长 | 把一段工作经历丢给 AI → 生成自查清单 |

---

## 边界/适用条件

| 边界 | 说明 |
|---|---|
| **有明确 Before/After 或大量协作记录** | AI 复盘需要可对比的素材或可扫描的文本记录。 |
| **任务可被结构化描述** | 审美标准、协作流程、评审要点能够被写成 checklist 或 Skill。 |
| **人有判断力和审美** | AI 只能提炼和合并，不能替代人做最终决策和建模。 |
| **不适用于一次性、无复用价值的任务** | 复盘封装需要 ROI，临时、不会再做的任务直接完成即可。 |
| **需要可访问的明文记录** | AI 扫描依赖文档、数据库、聊天记录等可被读取的格式。 |

---

## 教训

- **AI 擅长对比和合并**：人做耗时，AI 做很快。
- **人必须二次判断**：AI 输出后还要人确认、建模。
- **及时性是关键**：拖久了信息就丢了。
- **指定扫描范围**：不指定边界，AI 会大海捞针。

---

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|---|---|---|
| **直接接受 AI 复盘** | 不二次判断，把 AI 输出当最终结论 | 人做最终确认和建模 |
| **复盘不及时** | 记忆模糊、聊天记录过期、信息丢失 | 当天或隔天就做 |
| **不封装** | 每次重新复盘，经验无法复用 | 把复盘结果变成 Skill/清单 |
| **扫描范围太宽** | AI 输出杂乱、无关信息多 | 指定主题、工具和关键词边界 |
| **缺少对比素材** | AI 无法发现 Before/After 差异 | 保留原始版本和最终版本 |
| **审美门槛不足** | 看不出 AI 输出哪里不对 | 先练判断，再让 AI 批量执行 |

---

## 行动 Checklist

### 准备阶段
- [ ] 明确复盘主题和边界
- [ ] 收集 Before/After 版本或协作记录
- [ ] 确认 AI 可访问的数据源

### AI 帮助人复盘
- [ ] 把 Before 和 After 同时喂给 AI
- [ ] 让 AI 列出差异、洞察和可复用 tips
- [ ] 人基于 AI 输出二次总结、建模、写 checklist

### AI 自己复盘自己
- [ ] 指定 AI 扫描的工具/数据库和关键词范围
- [ ] 让 AI 合并同类项反馈
- [ ] 要求 AI 封装成 Skill：场景、审美底盘、协作流程、评审表、注意事项、硬性坑
- [ ] 人做审美判断，修正边界和优先级

### 收尾阶段
- [ ] 当天或隔天完成复盘
- [ ] 把 Skill/checklist 写入可复用库
- [ ] 下次同类任务先调用 Skill 再执行

---

## 相关卡/互链

- [[case-ai-agent-milestone-design]]：Truman 用 AI Agent 设计里程碑方法论，可与本案例的"封装 Skill"方法结合使用。
- [[case-truman-ai-skill-engineering-guide]]：高阶 AI Skill 工程指南，提供 Skill 封装和审计标准。
- [[dk-modeling-ai-iterative-prompting]]：AI 迭代提示策略，支持复盘中的多轮反馈拉齐。

---

## Sources

- `10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md:1148-1218`

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）· 精修于 2026-06-18*
