---

id: sk-ai-old-small-checklist
title: 技能："找老的干小的"场景评估清单
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 马易
source_context: AI俱乐部-AI落地场景识别分享，2026-06
source_refs:
- 10_raw/sources/src_20260614_071928f4-AI场景落地方法分享.md
wiki_refs:
- '[[sk-ai-landing-five-steps]]'
- '[[ai-landing-scene-selection]]'
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 数据管理工具（Notion / Airtable 等）
prerequisite_skills: null
related:
- '[[sk-ai-landing-five-steps]]'
- '[[ai-landing-scene-selection]]'
author: 马易
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 团队讨论AI落地时，提出的场景大而全或过于新颖
- 候选AI场景缺少历史数据或明确验收指标
- 试点效果需要数月才能验证

---
# 技能："找老的干小的"场景评估清单

## 用一句话讲清楚

用一张清单快速筛选出"熟悉、规模小、可验证"的AI首批落地场景，避免选错场景导致试点失败。

## 核心要点

- **找老的**：优先选择你熟悉的业务场景，能写出SOP，才能判断AI做得对不对。
- **干小的**：选择影响范围小、2周内可验证的子任务，降低试错成本。
- **你会的**：AI只能干你会的事，不要指望AI解决你也没搞懂的问题。
- **可拆分**：大而全的场景必须拆成3步以内的小任务，才能快速迭代。

## 边界

- **适用**：AI落地初期的场景筛选、团队头脑风暴后的优先级排序、老板要求快速试点时。
- **不适用**：已经明确的成熟AI项目、需要全链路重构的复杂场景、缺乏任何业务背景判断的新领域。
- **规模**：适合1-3人小组在1小时内完成初步评估。

## 失败模式

| 失败模式 | 触发信号 | 应对措施 |
|---|---|---|
| 步骤跳过或省略 | 清单打分不完整、关键维度空着 | 严格按步骤执行，每步必须验收后进入下一步 |
| 单人操作忽视团队协作 | 只有一个人打分、团队对结果不认可 | 步骤1就征求团队意见 |
| 惯性思维干扰 | 凭感觉打分、跳过某步 | 按清单逐条打勾，不要靠感觉 |
| 场景过大不可控 | 影响全链路、拆分超过3步 | 强制拆分为更小场景，先选影响面最小的1个环节 |

## 行动 Checklist

- [ ] 列出所有候选AI落地场景
- [ ] 对每个场景按5个维度逐项打分（+1/0/-1）
- [ ] 选择总分最高的1-2个场景作为首批试点
- [ ] 记录"为什么选这个"的决策理由
- [ ] 在2周内完成试点并验证before/after指标

## 场景评估表

| 维度 | 评估问题 | 加分项（选老的） | 扣分项（不要选） |
|------|--------|---------------|---------------|
| **熟悉度** | 你是否清楚这个场景的每个步骤？ | 你能写出SOP | 你也没搞明白这个流程 |
| **数据可得** | 是否有历史数据或现有方法？ | 有现成的模板/数据/规则 | 从零开始建数据 |
| **规模可控** | 出问题影响面多大？ | 只影响1-2个人或一个环节 | 一错就影响全链路 |
| **可验证** | 2周内能验证效果吗？ | 有明确的before/after指标 | 需要3个月才能看效果 |
| **可拆分** | 能拆成更小的子任务吗？ | 可以拆成3步以内 | 大而全，拆不动 |

## 相关卡/互链

- [[sk-ai-landing-five-steps]]
- [[ai-landing-scene-selection]]

## 来源

- 马易，AI俱乐部-AI落地场景识别分享，2026-06

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
