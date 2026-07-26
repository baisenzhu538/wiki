---
id: skill-demand-analysis
title: 需求分析 Skill：冰山推演全流程
type: skill
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-07-08
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- yitang
- demand-analysis
source_refs:
- 00_inbox/五步法之需求分析/AI场景推演教练提示词.txt
- 00_inbox/五步法之需求分析/需求分析提示词.txt
- 00_inbox/五步法之需求分析/AI辅助探讨需求选项的提示词.md
related:
- '[[agent-spec-demand-iceberg-coach]]'
- '[[framework-demand-iceberg]]'
- '[[framework-demand-ceiling-four-lines]]'
- '[[tool-demand-assessment-triangle]]'
- '[[tool-demand-chai-tui-ping-suan-guide]]'
- '[[case-demand-iceberg-few-shot]]'
- '[[knowledge-demand-2b-dictionary]]'
- '[[knowledge-demand-2c-dictionary]]'
- '[[domain-demand-analysis-index]]'
diagnostic_signals:
- signal: 接到需求分析任务时不知道从哪个工具开始
  lens: 缺工作流指引——工具齐全但不会组合
  follow-up: 加载本Skill，按触发场景选择入口
quality_labels:
- actionable
- principle
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---

# 需求分析 Skill：冰山推演全流程

> **一句话**：需求分析域所有工具和知识的统一入口。根据项目阶段自动路由到正确的工具组合——从0-1探索到融资准备，一套Skill全覆盖。

---

## 触发场景

| 场景 | 入口 | 工具组合 |
|:---|:---|:---|
| 刚有一个想法，需要搞清楚"这到底是谁的需求" | L1-L3冰山推演 | `agent-spec-demand-iceberg-coach` → `tool-demand-iceberg-l1~l3` |
| 用户和场景清楚了，需要判断"值不值得做" | 需求评估 | `tool-demand-assessment-triangle` + `tool-demand-rat-generator` |
| 准备融资，需要天花板数字 | 天花板测算 | `framework-demand-ceiling-four-lines` + `tool-demand-ceiling-coach` |
| 用户说已有一个方向，需要帮忙探讨 | 选项探讨 | `tool-demand-option-explorer` + `tool-demand-chai-tui-ping-suan-guide` |
| 需要写一份完整的需求分析报告 | 全流程 | 本Skill六步+`tool-demand-report-template` |

---

## 六步工作流

```
Step 1: L1-L3 冰山推演（谁+什么场景+什么任务）
  ├── 入：一个创业想法
  ├── 工具：agent-spec-demand-iceberg-coach
  └── 出：L1用户标签 + L2场景痛点 + L3核心任务

Step 2: L4-L5 深度拆解（任务链+力量分析）
  ├── 入：L3核心任务
  ├── 工具：tool-demand-iceberg-l4-job-map + l5-forces
  └── 出：L4任务地图8步 + L5四种力量

Step 3: L6 机会假设
  ├── 入：L4崩溃点 + L5力量
  ├── 工具：tool-demand-iceberg-l6-hypothesis
  └── 出：3-5个机会假设 + RAT清单

Step 4: 需求评估
  ├── 入：L6机会假设
  ├── 工具：tool-demand-assessment-triangle + tool-demand-rat-generator
  └── 出：Go/No-Go判断

Step 5: 天花板测算（如需）
  ├── 入：通过评估的假设 + 项目阶段
  ├── 工具：framework-demand-ceiling-four-lines + tool-demand-ceiling-coach
  └── 出：融资版/经营版天花板报告

Step 6: 出报告
  ├── 工具：tool-demand-report-template
  └── 出：融资版或经营版需求分析报告
```

---

## 调用清单

| 类别 | 卡片 | 路径 |
|:---|:---|:---|
| Agent | 冰山教练 | `.agent/prompts/agent-spec-demand-iceberg-coach.md` |
| 工具×6 | L1-L6冰山工具 | `30_wiki/tools/tool-demand-iceberg-l1~l6-*.md` |
| 工具×6 | 评估三角形/RAT/天花板/微观体感/选项/报告 | `30_wiki/tools/tool-demand-*.md` |
| 框架×1 | 天花板四层线 | `30_wiki/frameworks/framework-demand-ceiling-four-lines.md` |
| 案例×1 | 冰山Few-Shot案例库 | `30_wiki/cases/case-demand-iceberg-few-shot.md` |
| 知识×2 | 2B/2C需求字典 | `30_wiki/knowledges/knowledge-demand-2b/2c-dictionary.md` |
| 指南×1 | 拆推评算使用指南 | `30_wiki/tools/tool-demand-chai-tui-ping-suan-guide.md` |

---

## 核心纪律

1. **L4/L5前禁止产品方案**：在搞清楚"用户真正要完成什么"和"为什么还没完成"之前，不讨论任何产品形态
2. **数字降级**：所有口述课程数字标注为"课程经验值"，不用作外部引用的强证据
3. **方案中立**：核心任务描述中不得出现任何产品/技术/品类名词
4. **够评估就好**：不是所有项目都需要五层天花板全算——判断是否需要融资版数字再启动
