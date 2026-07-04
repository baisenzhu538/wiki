---
id: task_20260704_wangyuyan-ai-feature-inventory-research
title: AI 工具特性清单全网调研与建设
type: task
status: queued
assignee: 王语嫣
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: null
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - 60_feedback/annotations/annotation-ai-feature-inventory-research.md
related:
  - '[[concept-yihang-ai-feature-thinking]]'
  - '[[tool-ai-feature-inventory]]'
  - '[[task_20260704_laowantong-ai-feature-thinking-concept]]'
---

# 任务 #75：AI 工具特性清单全网调研与建设

## 任务目标

基于 Truman 在双三角课程中提出的 **Feature 思维**，系统建设一张**可维护的 AI 工具特性清单（Feature Inventory）**，把上下文工程、提示词工程、Codex、Hermes、龙虾/OpenClaw 等领域的热门工具按**最小可操作技术特性**原子化拆解。

**核心原则**：
1. 不追热点工具卡，只沉淀底层 Feature 卡。
2. 每个 Feature 必须有定义、适用场景、不适用边界、可验证方式。
3. 公开工具用 web research，内部工具用内部访谈/文档梳理。

---

## 调研范围

| 领域 | 公开/内部 | 关键问题 | 目标产出 |
|:---|:---:|:---|:---|
| **上下文工程** | 公开 | 长上下文 vs RAG vs 记忆分层各自的边界是什么？有哪些可操作的特性？ | 特性清单 + 选型决策树 |
| **提示词工程** | 公开 | Zero-shot / Few-shot / CoT / ReAct / ToT / 结构化输出等特性的适用场景是什么？ | 特性清单 + 选择流程图 |
| **Codex** | 公开 | Codex Agent 的核心特性有哪些？与其他编程 Agent 的 Feature 差异是什么？ | Codex 特性工具卡 |
| **Hermes** | 内部 | 作为 KDO 工厂运行环境，Hermes 支持哪些 Agent 运行特性？ | Hermes 特性工具卡 |
| **龙虾 / OpenClaw** | 内部/公开 | 龙虾的核心特性是什么？与 OpenClaw 是什么关系？ | 龙虾/OpenClaw 特性工具卡 |

---

## 已掌握素材

1. 王语嫣入口标注：`60_feedback/annotations/annotation-ai-feature-inventory-research.md`
2. 双三角口述稿：行 1210、1386-1468
3. 龙虾口述稿：`00_inbox/人机协作双三角/_processed/龙虾和skills训练的口述_page001-004_vlm.md`
4. Hermes 相关信息：`.agent/context.md`、任务文件、`00_inbox/ideas/`

---

## 任务分解

| 子任务 | 负责人 | 输出 | 依赖 |
|:---|:---|:---|:---|
| 1. 公开领域 web research | 王语嫣/老顽童 | 上下文工程、提示词工程、Codex 的公开特性清单（带来源） | 无 |
| 2. 内部工具特性梳理 | 王语嫣/黄药师/老顽童 | Hermes、龙虾/OpenClaw 特性清单（需访谈确认） | 无 |
| 3. 特性去重与边界定义 | 王语嫣 | 统一的 Feature 分类框架 + 每条特性的适用/不适用场景 | 子任务 1、2 |
| 4. 卡片生产 | 老顽童 | `tool-ai-feature-inventory` + 至少 2 张领域特性卡 | 子任务 3 |
| 5. 欧阳锋终审 | 欧阳锋 | 通过/不通过 | 子任务 4 |

---

## 验收标准

- 产出 `tool-ai-feature-inventory` 并 `kdo pre-submit` 通过。
- 至少产出 2 张领域特性方法/工具卡（建议：上下文工程 + 提示词工程，或 Codex + 上下文工程）。
- 每个 Feature 必须有：定义、适用场景、不适用场景、可验证方式、来源链接。
- 内部工具（Hermes、龙虾/OpenClaw）特性清单必须经过至少一位实际使用者（黄药师/老顽童）确认。
- 所有新卡必须反向更新 `concept-yihang-ai-feature-thinking` 和相关双三角卡 `related`。
- 欧阳锋终审通过。

---

## 依赖

- 无强阻塞。
- 建议与 #74 `concept-yihang-ai-feature-thinking` 协同：#74 定义 Feature 思维，#75 提供可查询的特性清单。

---

## 备注

本任务直接回应用户追问：「上下文工程、提示词、Hermes、龙虾、Codex 都有特性，是否需要建设特性列表并全网调研深挖？」

王语嫣已先做一轮公开资料扫描并写入 `annotation-ai-feature-inventory-research.md`，但完整深挖需要专门任务推进。
