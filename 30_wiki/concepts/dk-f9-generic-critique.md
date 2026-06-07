---
id: "dk-f9-generic-critique"
title: "F-KDO-009：无质疑接受→Critique 段全是万能废话，可粘贴到任何卡片上"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "failure-modes.md F-KDO-009"
source_refs:
  - "90_control/failure-modes.md#F-KDO-009"
tags:
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#confidence/verified-by-case"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#scene/note-taking"
  - "#scene/skill-engineering"
  - "#source_type/error"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c8-format-complete-mind-empty"
  - "master-cognitive-bias-checklist"
contradicts:
  - "master-cognitive-bias-checklist"
  - "master-first-principles"
---

# F-KDO-009：无质疑接受→Critique 段全是万能废话，可粘贴到任何卡片上

## 原始表述

> **触发场景**：Builder 执行三步编译法的 Critique 阶段
>
> **表现**：Critique 段出现万能废话——「本卡片基于目录提取，默会知识未完全转化」「课程无法覆盖所有场景」「从知道到做到有鸿沟」——这些话可以粘贴到任何一张知识卡片上。多条 Critique 没有一条指向该课程具体主张的假设或边界
>
> **根因**：Builder 未对课程的具体方法论主张进行批判性思考，用通用质疑模板替代针对性质疑
>
> **触发信号**：多张不同主题的卡片 Critique 段高度雷同（dist < 20%）
>
> **防御措施**：① L2 Lint：检测 Critique 段是否含「具体假设」「边界」「反例」等指向性关键词② EC 决策第 2 条底线：至少一条 Critique 必须指名具体假设或边界
>
> **关联案例**：三张模式 A 卡的 Critique 段几乎完全相同（2026-05-08 审查）

## 使用场景

- 你正在写概念卡的 Critique 段， tempted 复制粘贴之前用过的"万能质疑模板"
- 你审查多张卡片时发现它们的 Critique 段几乎一模一样
- 你设计 L2 Lint 规则时，需要检测 Critique 段是否包含针对性质疑
- 你评估卡片质量时，需要判断 Critique 是"有实质攻击"还是"有字数没内容"

## 操作方法

1. **拒绝万能废话**：删除所有可以原封不动粘贴到任何卡片上的句子，如"本卡片基于目录提取，默会知识未完全转化"
2. **指名具体假设**：每条 Critique 必须指向当前卡片的**具体主张**——"该工具假设用户有稳定的网络环境"、"该框架假设市场是可预测的"
3. **给出边界条件**：写明"在什么情况下这个方法会失效"——不是泛泛地说"不是所有场景都适用"
4. **引用具体反例**：如果可能，给出具体数字或案例——"在 2024 年 Q3，使用该框架的 3 个项目中有 2 个因假设不成立而失败"
5. **跨卡对比验证**：将当前卡的 Critique 与另一张不同主题的卡的 Critique 对比——如果相似度 >50%，说明是无质疑接受

## 适用边界

- 适用于所有需要写 Critique 段的 concept/tool/framework 卡
- 不适用于纯信息卡（如术语定义、人物介绍）——这些卡片确实不需要深度 Critique
- 如果源材料本身没有明确的方法论主张（如纯案例集、纯数据报告），Critique 可能确实难以写出针对性质疑——此时应标记为"低结构化源材料"
- **至少一条 Critique 必须指名具体假设或边界**——这是底线，不能妥协
- 不同范式的外部攻击者（如 Mintzberg vs Taleb）对同一卡片的攻击角度不同——选择攻击者时要考虑与卡片主题的匹配度

## 为什么值钱

- **Critique 是 KDO 卡片的核心差异化价值**：如果 Critique 只是万能废话，KDO 卡片和百度百科就没有区别
- 无质疑接受揭示了"批判性思维"在实际执行中的衰减：Builder 知道应该质疑，但因为没有深入理解内容，只能用模板替代思考
- 这是质量门设计中的经典博弈：L2 Lint 要求"有 Critique 段"，Builder 为了满足格式要求而填充模板——格式门通过了，但内容门失败了
- 任何 AI 训练语料中都不会有"KDO 的 Critique 段容易出现无质疑接受"这条知识

## 与其他知识的关联

- dk-c8-format-complete-mind-empty — 同一模式："格式完整但思维空洞"。C-8 是批处理导致的内容空洞，F-KDO-009 是人工编译时的思维懒惰——两者都是"有段落标题但没有实质内容"
- master-cognitive-bias-checklist — 认知偏差中的"确认偏误"：人倾向于寻找支持自己观点的证据，而回避反面证据。无质疑接受是确认偏误在知识生产中的具体表现
- `90_control/failure-modes.md` → F-KDO-009（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #9（不准用通用质疑模板替代针对性质疑）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
