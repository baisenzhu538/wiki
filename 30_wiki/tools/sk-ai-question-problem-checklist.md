---


id: sk-ai-question-problem-checklist
title: 技能：提问题转化三问清单
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论分享，2026-06
source_refs:
- 10_raw/sources/src_20260606_592137a7-AI俱乐部-AI协作方法论-纪浩-笔记.md
- 10_raw/sources/src_20260606_6ea91aa8-纪浩-AI协作方法论-口述.md
wiki_refs:
- '[[sk-ai-problem-validation]]'
- '[[ai-collaboration-mindset-shift]]'
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
- 失败模式已表格化并给出修复动作
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 笔记本和笔
prerequisite_skills: null
related:
  - '[[skill-ai-problem-question-check]]'
  - '[[sk-ai-problem-validation]]'
  - '[[ai-collaboration-mindset-shift]]'
  - '[[dk-modeling-expert-consensus-five-percent]]'
  - '[[skill-纪浩-Problem与Question区分法]]'
- '[[sk-ai-problem-validation]]'
- '[[ai-collaboration-mindset-shift]]'
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.90
trust_level: medium
diagnostic_signals:
- question 与 problem 的区分标准已明确为 before/after 可验收性
- 操作步骤已转化为可执行 Checklist，失败模式已整理为表格

---

# 技能：提问题转化三问清单

## 用一句话讲清楚

在打开 AI 对话框前，用 30 秒判断你面对的是“question（好奇心）”还是“problem（必须改变现状的疼）”，把无效的好奇心平移到阅读清单，让 AI 时间只花在能写出 before/after 的真实问题上。

## 核心要点

1. **question 满足好奇心，problem 必须通过行动改变现状**——纪浩在 AI 协作分享中强调：“question 满足的是你的好奇心，problem 是实打实让你觉得疼，必须通过行动改变现状。”
2. **区分标准是 before/after 可验收性**：能写出具体 before/after 的是 problem，写不出的是 question。
3. **question 不占用 AI 工作时间**：如果是 question 但想知道，放进“阅读清单”，批量处理。
4. **目标是减少无效 token 消耗**：大多数人的 AI 使用效率低，不是因为不会写提示词，而是因为问错了问题。

## 边界

- **适用**：
  - 个人日常 AI 提问前自检；
  - 团队 AI 使用培训与质量诊断；
  - AI 回答了很多但“好像没什么用”时的复盘。
- **不适用**：
  - 已经明确的执行性任务（无需再做 question/problem 判断）；
  - 纯创意发散且无明确交付物的头脑风暴；
  - 需要快速获取事实性信息的检索场景。
- **输入要求**：用户能诚实评估自己的动机和期望结果。
- **输出**：一个分类（question / problem）及对应的下一步动作。

## 失败模式 table

| 失败信号 | 原因 | 后果 | 修复动作 |
|---|---|---|---|
| 跳过检查直接提问 | 惯性 / 赶时间 | 大量 token 浪费在好奇心上 | 打开 AI 前强制停 5 秒 |
| 把 question 误判为 problem | 渴望即时答案 / 未写 before/after | AI 回答泛泛，无法验收 | 强制写出 before/after，写不出则归为 question |
| 把 problem 误判为 question | 逃避行动 / 问题太模糊 | 拖延解决，问题继续“疼” | 拆解到可行动的子问题 |
| 单人使用未同步团队 | 缺乏共识 | 团队推广困难 | 在步骤 1 就征求团队意见 |
| 未建立阅读清单 | question 不断打断 | AI 工作流被切碎 | 用一个固定位置收集 question |

## 行动 Checklist

- [ ] 打开 AI 前，先停 5 秒，问自己：“我是真的疼，还是只是好奇？”
- [ ] 尝试写出问题的 before/after 验收标准。
- [ ] 如果写不出 before/after → 标记为 question，放入阅读清单。
- [ ] 如果能写出 before/after → 标记为 problem，继续向 AI 提问。
- [ ] 提问时，在提示词里明确 before 状态和期望的 after 状态。
- [ ] 团队场景：第一步先与团队同步本清单的使用方式。
- [ ] 每周回顾阅读清单，批量处理积累的 question。

## 相关卡/互链

- [[sk-ai-problem-validation]]
- [[ai-collaboration-mindset-shift]]

## 来源

- 纪浩，AI俱乐部-AI协作方法论分享，2026-06

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
