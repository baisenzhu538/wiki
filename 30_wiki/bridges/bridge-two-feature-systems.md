---
id: bridge-two-feature-systems
title: 「澄清：两套 Feature 体系——KDO 工程 Feature vs AI 能力 Feature」
type: bridge
status: reviewed
confidence: 0.9
trust_level: high
domain:
- ai-basic
- kdo
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-08-25'
updated_at: '2026-08-25'
source_refs:
- 60_feedback/tasks/task_20260825_laowantong-feature-domain-signpost-batch.md
- cap_hub/features.json
- 10_raw/sources/feature-periodic-table-v1.0.json
aliases:
- 两套Feature体系
- Feature澄清
- KDO工程Feature
- AI能力Feature
discoverable_by:
- 两套Feature
- Feature体系区别
- features.json
- 周期表
related:
- '[[bridge-dual-track-feature-system]]'
- '[[framework-truman-feature-layered-system]]'
- '[[framework-truman-feature-thinking-core]]'
- '[[concept-kdo-feature-registry]]'
tags:
- audience:general
- scene:reference
- skill-level:beginner
- Feature
- 澄清
- 路标
---

# 澄清：两套 Feature 体系

> 本卡是**入口路标**（#526 盲测修复批）：防止 grep「feature」时两套体系互相污染。完整双轨论述见 `bridge-dual-track-feature-system`。

## 一句话区分

| 体系 | 本体 | 回答的问题 | 谁用 |
|:--|:--|:--|:--|
| **KDO 工程 Feature** | `cap_hub/features.json` | 这个知识工厂**系统**有什么能力开关（工具/门禁/管线特性） | KDO 开发者/黄药师 |
| **AI 能力 Feature** | `10_raw/sources/feature-periodic-table-v1.0.json`（100 项周期表，L0-L5） | 用 AI 解题时**人**要练哪些原子能力 | 一堂学员/AI 基本功教练 |

**互指**：查工程能力开关 → `cap_hub/features.json` + `concept-kdo-feature-registry`；查 AI 能力刻意练习 → `framework-truman-feature-layered-system` + `kdo-tools/feature_menu.py`（点菜式查询）。

## 为什么值钱

盲测实证（2026-08-25 老朱自然语言 4 问，小昭检测报告）：问「feature 有哪些怎么分类」时，grep 先命中工程 Feature 文件，检索者拿到 30% 答案自以为完整——**无声的错误**。本卡把两个体系的边界钉死在入口层。

## 与其他知识的关联

- `bridge-dual-track-feature-system`：双轨体系完整论述（quality-gate vs capability）
- `framework-truman-feature-layered-system`：AI 能力 Feature 的 L0-L5 分层框架卡
- `concept-kdo-feature-registry`：KDO 工程 Feature 注册表概念卡
