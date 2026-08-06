---

id: dk-f9-generic-critique
title: F-KDO-009：无质疑接受→Critique 段全是万能废话，可粘贴到任何卡片上
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-009
aliases:
  - FKDO009：无质疑接受→Critique段全是万能废话，可粘贴到任何卡片上
  - system
  - 可粘贴到任何卡片上
  - 无质疑接受
  - 无质疑接受→Critique
  - 段全是万能废话
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-19'
discoverable_by:
  - F-KDO-009：无质疑接受→Critique 段全是万能
  - 无质疑接受→Critique
  - 段全是万能废话，可粘贴到任何卡片上
related:
- '[[kdo-input-channel-strategy-2026-06-16]]'
- '[[kdo-protocol]]'
- '[[modeling-to-kdo-toolchain]]'
- '[[kdo-batch-produce-req014]]'
- '[[kdo-15-dimension-label-spec]]'
- '[[obsidian-kdo-内容产出工作流-产品设计大纲]]'
- '[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]'
- '[[kdo-watch-health-check-layer]]'
- '[[framework-kdo-self-attack]]'
- '[[kdo-yaml-frontmatter-safety]]'
- '[[kdo-priority-checklist]]'
- '[[kdo_product_design_agent_final]]'
- '[[proposal-kdo-flywheel-infrastructure]]'
- '[[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown# F-KDO-009：无质疑接受→Critique 段全是万能废话，可粘贴到任何卡片上
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---

## 原始表述/核心洞察

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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **拒绝万能废话**：删除所有可以原封不动粘贴到任何卡片上的句子，如"本卡片基于目录提取，默会知识未完全转化"
2. **指名具体假设**：每条 Critique 必须指向当前卡片的**具体主张**——"该工具假设用户有稳定的网络环境"、"该框架假设市场是可预测的"
3. **给出边界条件**：写明"在什么情况下这个方法会失效"——不是泛泛地说"不是所有场景都适用"
4. **引用具体反例**：如果可能，给出具体数字或案例——"在 2024 年 Q3，使用该框架的 3 个项目中有 2 个因假设不成立而失败"
5. **跨卡对比验证**：将当前卡的 Critique 与另一张不同主题的卡的 Critique 对比——如果相似度 >50%，说明是无质疑接受

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型表现 | 预警信号 | 修正方向 |
|
|---|---|---|
| 模板化质疑 | Critique 段出现"默会知识未完全转化""从知道到做到有鸿沟"等可粘贴到任意卡片的句子 | 单条 Critique 不指名任何具体假设、边界、反例 | 删除万能句，替换为针对当前卡片具体主张的攻击 |
| 只描述不攻击 | 重复卡片标题或优点，如"该方法强调用户洞察，但可能忽略其他因素" | 读完 Critique 后不知道具体反对什么 | 每条 Critique 必须指名一个具体假设或边界条件 |
| 跨卡雷同 | 多张不同主题卡片的 Critique 段相似度 >50% | 用 diff 工具查看，差异仅在于主语名词 | 强制跨卡对比，要求至少一条反例或数字 |
| 模糊情感词 | 使用"有点理想化""不够落地"等模糊评价 | 没有具体数字、案例或条件 | 将情感词转化为可验证的条件或反例 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
