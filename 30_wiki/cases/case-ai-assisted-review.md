---
id: case-ai-assisted-review
title: 案例：一堂用 AI 做复盘——从 Before/After 对比到 AI 自己复盘自己
type: case
source_refs:
- src_20260614_8269ccdb
status: enriched
domain:
- yitang
- modeling
- ai
source_person: Truman
source_context: 一堂高阶建模能力培训（AI 辅助复盘案例） （单一 source 为完整长文档，内容充分支撑 high trust）
created_at: '2026-06-14'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
review_date: '2026-06-14'
trust_level: high
confidence: 0.85
related:
- '[[case-ai-agent-milestone-design]]'
- '[[case-truman-ai-skill-engineering-guide]]'
- '[[dk-modeling-ai-iterative-prompting]]'
tags:
- '#modeling'
- '#case'
- '#ai'
- '#review'
- '#feedback'
---
# 案例：一堂用 AI 做复盘——从 Before/After 对比到 AI 自己复盘自己

> **Burn line**: AI 不仅能帮人复盘，还能自己复盘自己，把一次经验变成下一次的基础。

这是 Truman 在课上分享的最近实践。一堂把 AI 引入复盘流程，发现 ROI 比人工高很多。

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

## 教训

- **AI 擅长对比和合并**：人做耗时，AI 做很快。
- **人必须二次判断**：AI 输出后还要人确认、建模。
- **及时性是关键**：拖久了信息就丢了。
- **指定扫描范围**：不指定边界，AI 会大海捞针。

---

## 失败模式

| 失败模式 | 表现 | 避免方法 |
|---|---|---|
| **直接接受 AI 复盘** | 不二次判断 | 人做最终确认 |
| **复盘不及时** | 信息丢失 | 当天或隔天就做 |
| **不封装** | 每次重新复盘 | 把复盘结果变成 Skill/清单 |
| **扫描范围太宽** | AI 输出杂乱 | 指定主题和工具 |

---

## Sources

- `00_inbox/建模能力/一堂-建模能力培训-truman-口述.txt:1148-1218`

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）*
