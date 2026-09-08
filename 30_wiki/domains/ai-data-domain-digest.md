---
id: ai-data-domain-digest
title: 域摘要：ai-data（AI数据）
type: index
domain:
- ai-data
- system
status: reviewed
author: 黄药师
reviewed_by: 欧阳锋
review_date: 2026-09-08
confidence: 0.8
trust_level: medium
source_refs:
- 60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md
- 60_feedback/tasks/task_20260908_huangyaoshi-ai-data-domain-infra.md
created_at: 2026-09-08
updated_at: 2026-09-08
tags:
  - audience:huangyaoshi
  - scene:reference
  - skill-level:intermediate
  - AI数据
  - 数据飞轮
  - 数据资产
  - 数据治理
  - 数据标注
  - 数据判断力
  - DIKW
aliases:
- AI数据域
- ai-data
- 数据判断力域
discoverable_by:
- AI数据域
- ai-data
- 数据判断力域
diagnostic_signals:
- signal: '新域注册——P0 八张已产毕待终审（#683），P1 Live258 六案例候选未产（#681 拍板范围）'
  severity: medium
  implication: MOC 路标已立；P0 终审通过后路标状态回填（二次补）
related:
- '[[master-moc]]'
- '[[kdo-moc]]'
- '[[ai-basic-domain-digest]]'
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-adaptive-data-flywheel]]'
- '[[concept-data-three-constants-three-shifts]]'
- '[[concept-aducit-six-step]]'
- '[[ai数据理解第一课]]'
- '[[数据标注维度最佳实践调研报告]]'
- '[[case-yihang-dual-triangle-AI三角-数据]]'
---
# ai-data 域摘要

> **定位**：AI数据域（ai-data）= AI 商业能力域之一，主题为"数据判断力"——什么数据值得攒、数据资产价值怎么估、数据 ROI 怎么判、数据怎么治理与飞轮化。本卡是域入口 MOC（骨架参照 `ai-basic-domain-digest`，#686 补建）。

> **来源**：王语嫣诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md`（#681，57 件素材 100% 落判）+ 一堂「AI数据必修课·认知篇」三段口述（01/02/03）。
> **状态**：骨架已立，路标覆盖存量散卡 13 张 + P0 新产 8 张（#683 终审中）。

## 本域核心资产路标

### 方法论主干（#683 P0 新产，终审中）

- 数据飞轮框架卡（6+1 模型+Adaptive 双轮）：`30_wiki/frameworks/framework-adaptive-data-flywheel.md`
- 三不变三聚变概念卡（DIKW/IPO/ROI + 评估六问）：`30_wiki/concepts/concept-data-three-constants-three-shifts.md`
- L1-L6 数据成熟度自评：`30_wiki/tools/tool-data-maturity-l1-l6.md`
- 治理四层+控下限+容错率：`30_wiki/tools/tool-data-governance-four-layers.md`
- 睡前故事四阶段数据包（个人级体感教材）：`30_wiki/cases/case-truman-bedtime-story-datapack.md`
- 徐建发票 1480 标签数据资产（案例）：`30_wiki/cases/case-xujian-invoice-data-asset.md`
- AI 叠加 AI 投毒（dk）：`30_wiki/dark-knowledges/dk-ai-on-ai-data-poisoning.md`
- 及时复盘「等 30 秒」心法（dk）：`30_wiki/dark-knowledges/dk-data-timely-review.md`

### 存量散卡（此前散挂 ai-collaboration/kdo/yihang 域下，#686 注册归位）

- 概念 ×2：`30_wiki/concepts/ai数据理解第一课.md`（五层次+五类型，溯源链断裂待补挂）；`30_wiki/concepts/concept-aducit-six-step.md`（ADUCIT 六步数据飞轮，一堂数据飞轮 6+1 概念版）
- 工具 ×7（马易族执行层 6 + 半肥猫 1）：`30_wiki/tools/tool-马易-数据存储架构选择.md`、`tool-马易-数据标注正确法.md`、`tool-马易-RPA数据整合法.md`、`tool-马易-减少输入噪音法.md`、`tool-马易-视频转化关键要素标注校验.md`、`tool-马易-低置信度样本黄金漏斗处理.md`、`tool-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian.md`（YAML 原子化标签）
- 案例 ×3（双三角数据族）：`30_wiki/cases/case-yihang-dual-triangle-AI三角-数据.md`（主卡，AI数据卡已并入）、`case-yihang-dual-triangle-一堂双三角-AI企业经营数据分析.md`、`case-yihang-dual-triangle-AI数据.md`（redirect → 主卡）
- 报告 ×1：`30_wiki/concepts/数据标注维度最佳实践调研报告.md`（标注维度调研）

## 域定义

ai-data = AI 数据判断力。上游是一堂「AI数据必修课·认知篇」方法论（数据三聚变/6+1 飞轮/治理四层/成熟度段位），存量层是马易族执行层技能（标注/存/整合/降噪）与双三角数据角案例。与 KDO 自身实践同构——本厂数据飞轮（capture→ingest→enrich→produce→validate→ship→feedback）即域方法论的活体样本。

## 与其他域的关系

- **ai-basic（AI基本功）**：姊妹域，同属 AI 三角能力层（基本功=Feature 思维，数据=数据判断力）
- **yihang（双三角）**：数据角案例的原始归属域；ADUCIT 概念卡同源（一堂数据飞轮 6+1）
- **ai-collaboration**：马易族执行层卡与 ai数据理解第一课的旧挂靠域
- **调研（yitang-research）**：边界——调研域的数据工具（yitang-*data* 族）是"从外部拿数据"，本域是"把自己的业务过程攒成数据资产"，不混收
- **kdo**：KDO 数据飞轮实践与本域方法论互为印证

## 子主题

1. 数据资产价值观（三不变三聚变 / 攒牌心态）
2. 数据飞轮（6+1 管线 / Adaptive 双轮 / ADUCIT 概念版）
3. 数据治理（四层 / 控下限 / 容错率匹配 / 三防）
4. 数据成熟度自评（L1-L6 段位图）
5. 数据标注执行层（马易族 6 技能 / YAML 原子化标签）

## 在产与待产

- #683 P0 八张：已产毕，欧阳锋终审中（通过后本卡路标状态二次回填）
- #681 P1 候选：Live258 六案例卡（按可用度排序，老朱拍板范围），产毕后补路标
- 溯源债：`ai数据理解第一课` 溯源链断裂待补挂（诊断报告 P2 已登记，非本单范围）
