---

id: dk-modeling-radar-model-not-result
title: 复杂评选别让 CEO 拍结果，只让 CEO 审模型
type: dark-knowledge
dark_knowledge_type: workflow
status: draft
domain:
- yitang
- ai-saas
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
source_refs:
  - src_20260614_8269ccdb-一堂-建模能力培训-truman-口述
confidence: 0.8
trust_level: medium
related:
- '[[dk-modeling-counterexample-driven]]'
- '[[dk-modeling-expert-consensus-five-percent]]'
- '[[tool-radar-chart-modeling]]'
tags:
- '#content-format/sop'
- '#domain/yitang'
- '#method/modeling'
- '#method/decision-quality'
author: 老顽童
reviewed_by: pending
created_at: '2026-06-15'
updated_at: '2026-06-16'
---
# 复杂评选别让 CEO 拍结果，只让 CEO 审模型

## 原始表述

> 你们要习惯性建模，你们带着模型过来跟我聊，我只聊模型不聊结果……我有一票否，但我没有一票通过权……我负责的是模型足够健康，且执行是 OK 的。

## 深度洞察

当组织规模变大、CEO 不可能熟悉每个候选人/项目时，“让 CEO 拍结果”会放大偏见和错误。Truman 的解法是**把评选结果从 CEO 手中拿掉，只保留对评选模型的审查权和否决权**。团队先和 CEO 一起画出 4-6 个关键维度的雷达图，作为共同工作公式；CEO 只负责两件事：模型是否科学、执行是否到位。这是一种把“建模”嵌入组织治理的反直觉设计。

## 使用场景

- 公司人数超过 500，CEO 无法对每个评选结果负责。
- 团队内部对“谁上谁下”争吵不休，缺乏共同标准。
- 你想把招聘、晋升、项目立项、供应商选择等决策从“人治”转向“模型治”。
- 你担心 CEO 个人偏好影响组织公平。

## 操作方法

1. **把决策拆成“模型”和“结果”**
   模型 = 评选维度 + 权重 + 评分规则；结果 = 按模型跑出来的排序。

2. **让 CEO 只参与模型设计**
   拉着有判断力的人一起定义 4-6 个关键角，CEO 只确认“这个模型是否科学”。

3. **CEO 保留一票否决，不保留一票通过**
   可以拦住高风险选项，但不能直接指定谁通过。

4. **持续打补丁**
   每次评选后复盘：哪些维度失真？哪些权重需要调？模型本身要迭代。

## 适用边界

- **适用于可结构化、多维度、高频的评选决策**。战略级、非结构化决策仍需要 CEO 直接判断。
- **需要团队具备基础建模能力**。如果连 L3/L4 的雷达图都画不出，模型会流于形式。
- **CEO 必须愿意放权**。如果 CEO 舍不得放弃拍板权，机制会失效。
- **模型质量必须过硬**。模型有漏洞时，甩锅给模型比人治更危险。

## 常见失败模式

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| CEO 口头放权实则拍板 | 模型跑完，CEO 还是凭印象推翻 | 明文写进决策流程，谁否决谁记录原因 |
| 维度定义不清晰 | 评分时各打各的，无法横向比较 | 每个角给出 3-5 级具体定义和案例 |
| 模型一成不变 | 早期有效，后期被团队钻空子 | 每季度/半年复盘一次模型 |
| 把模型当挡箭牌 | 结果不好就怪模型，没人负责执行 | 明确执行 owner，模型只负责筛选 |

## 为什么值钱

- 公开管理书讲“授权”，但很少讲“CEO 放弃结果拍板权、只审模型”这种具体治理机制。
- 这是 Truman 在一堂从几百人到更大规模时摸索出来的内部规则。
- 它把组织公平从“靠 CEO 人品”变成“靠模型+流程”。

## 与其他知识的关联

- [[dk-modeling-counterexample-driven]] —— 模型设计阶段要以推翻为目标验证。
- [[dk-modeling-expert-consensus-five-percent]] —— 模型维度需要专家共识输入。
- [[tool-radar-chart-modeling]] —— 雷达图建模工具。
- `src_20260614_8269ccdb#1320-1353` —— Truman 口述原文：只聊模型不聊结果。
