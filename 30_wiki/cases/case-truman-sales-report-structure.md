---
id: case-truman-sales-report-structure
title: 案例：Truman 重构销售失利汇报——把 10 个散点升级成逻辑链
type: case
status: reviewed
problem_domains:
- src_unknown
- src_unknown
industry: 通用
scale: 团队
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
aliases:
  - Truman
  - 个散点升级成逻辑链
  - 案例
  - 案例：Truman重构销售失利汇报把10个散点升级成逻辑链
  - 重构销售失利汇报
  - 销售失利汇报
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
wiki_refs:
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tags:
- src_unknown
- src_unknown
- audience:general
- scene:reference
- skill-level:intermediate
related_skills:
- src_unknown
related_concepts:
- src_unknown
- src_unknown
- src_unknown
related_cases:
- src_unknown
created_at: '2026-06-15'
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
domain:
- 工作汇报
- 复盘结构化
related:
- '[[tool-Truman-提示词优化底层方法]]'
- '[[tool-Truman-Skill全生命周期管理]]'
- '[[yt-model-truman-career-routes]]'
- '[[tool-从案例中学习]]'
- '[[tool-Truman-人在环渐进自动化策略]]'
- '[[tool-Truman-双三角模型应用]]'
- '[[truman-perspective-skill]]'
- '[[tool-Truman-AI能力分层学习路径]]'
- '[[tool-纪浩-案例池构建法]]'
- '[[tool-Truman-信息输入持续补全（防AI错误累积）]]'
- '[[case-科学决策-ROI案例03]]'
- '[[tool-马易-业务问题AI化拆解-餐饮设计案例法]]'
- '[[case-科学决策-深度案例06]]'
- 建模能力培训
---

# 案例：Truman 重构销售失利汇报——把 10 个散点升级成逻辑链

## 原始表述

> 我真的见过下属连换行都不给我加的，就长成这样的一个一大坨给我……如果做成优先级，这是 P0 的三个，这是 P1 的三个，这是 P2 的三个，有没有好一点？……如果有一个完整的逻辑顺序，就是输入的部分，然后旧的是怎么样，新的是怎么样的，这个处理的部分……每个人都可以找到自己的位置，每个人都知道自己可能谁依赖谁。

## 问题

下属汇报销售失利经验时，把内容写成“一大坨”或不排序的 10 个要点。领导既无法判断遗漏，也无法决策；团队也看不清各因素之间的依赖关系。

## 方案

用逻辑洁癖把汇报从 L1/L2 升级到 L3/L4/L5：

1. **排优先级**：把 10 个点分成 P0/P1/P2；
2. **MECE 拆分**：按“总分总 + 问题与机会 + 输入信息 + 讨论定位 + 决策 + 链条回顾”重新组织；
3. **形成逻辑链**：用“输入 → 优化空间 → 处理 → 输出”的严格顺序表达因果关系；
4. **显性化依赖**：让团队每个人都知道自己处在链条的哪一环。

## 结果

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 可迁移

- src_unknown
- src_unknown
- src_unknown

## 结构演进前后对比

Truman 把同一份销售失利汇报从 L1 改到 L5，不是堆内容，而是改结构：

| 段位 | 结构特征 | 示例（销售失利汇报） | 领导能否一眼判断 |
|---|---|---|---|
| L1 散点 | 一大段不换行，直接贴回访文章 | “上次失利原因如下：客户预算紧缩、竞品降价、我们跟进慢、话术没到位、 demo 出问题……” | ❌ 无法判断遗漏 |
| L2 清单 | 每行一个要点，共 10 条 | 1. 预算误判<br>2. 竞品降价<br>3. 跟进慢<br>4. 话术弱<br>5. demo 出问题…… | ❌ 看不出主次 |
| L3 优先级 | 10 条按 P0/P1/P2 分三组 | P0：预算误判、竞品降价、决策链缺人；P1：跟进节奏、话术；P2： demo 细节 | ⚠️ 知道先看哪三条 |
| L4 MECE | 总分总 + 问题与机会 + 输入信息 + 讨论定位 + 决策 + 链条回顾 | 先给结论“输在人”，再分会前/会中/会后三部分，每部分有输入、动作、输出 | ✅ 能判断结构完整 |
| L5 逻辑链 | 输入 → 旧状态/新状态 → 处理/优化空间 → 输出 | 输入质量差（客户画像不准）→ 处理策略错（报价方案单一）→ 输出结果差（丢单） | ✅ 因果显性，责任可定位 |

## 诊断信号

出现以下信号，说明这份汇报/复盘需要往右升级：

1. **下属把汇报写成一大段，连换行都没有**
   - src_unknown
   - src_unknown

2. **清单超过 7 条，但没有优先级或分类**
   - src_unknown
   - src_unknown

3. **有结论，但看不出“输入 → 处理 → 输出”的因果链**
   - src_unknown
   - src_unknown

## 可迁移场景与使用边界

| 可迁移场景 | 使用边界 |
|---|---|
| 销售/项目失利复盘 | 需要多人协作、有明确失败事实的场景 |
| 会议纪要/周报复盘 | 结论需要被后续执行调用，而非一次性汇报 |
| 团队经验沉淀 / SOP 初稿 | 经验可复现、错误模式有共性 |
| 向上管理 / 跨部门汇报 | 受众时间有限，需要快速定位问题和决策 |

| 失败模式 | 典型症状 | 可执行修复 |
|---|---|---|
| 把 Word / 回访文章直接贴进汇报 | 一大坨不换行，领导直接拒看 | 强制换行，每行只承载一个信息点 |
| 10+ 条平铺无优先级 | 讨论时每条都想抓，结果都没抓透 | 先按 P0/P1/P2 或 SABC 分级，再逐组讨论 |
| MECE 分类但无逻辑链 | 分类漂亮，但不知道先做哪个、谁依赖谁 | 在分类后补“输入 → 处理 → 输出”严格顺序 |
| 过度追求形式完美 | 简单清单硬拉成 L5，效率低 | 按决策价值和调用频次定目标段位：临时分析 L3，复用模型 L4/L5 |

## 快速自检清单

写完汇报/复盘后，用这 5 个问题自检：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关键标签

- src_unknown
- src_unknown
- src_unknown

## 关联

- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 教训

- src_unknown
- src_unknown
- src_unknown

---

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |
