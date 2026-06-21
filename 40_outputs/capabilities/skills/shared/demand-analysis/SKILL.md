---
name: demand-analysis
description: 需求分析总入口——USP快速拆解+冰山六层深挖+JTBD教练+评估三角形
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [需求分析, USP, 冰山, JTBD, 评估三角形]
    related_skills: [demand-analysis]
---

# Demand Analysis（需求分析总入口）

一堂需求分析方法论。Demand = User × Situation × Problem。

## Constraints

<hard_limits>
- 方案中立原则：在完成需求分析前，严禁讨论产品功能
- 区分事实与观点：用户说的≠用户要的
</hard_limits>

## 意图分类

| 场景 | 路由到 | 耗时 |
|:--|:--|:--|
| 快速拆解，3分钟出框架 | 引用 `tool-prompt-usp-quick-scan` | 3分钟 |
| 系统化深挖，引导用户自己思考 | `/demand-analysis-iceberg` | 20-40分钟 |
| AI主动给选项，用户只需选择 | 引用 `tool-prompt-jtbd-scenario-coach` | 30-60分钟 |
| 判断需求真伪/大小/紧迫 | `/demand-analysis-evaluate` | 15分钟 |
| 扫描遗漏维度 | `/demand-analysis-blindspot` | 10分钟 |
| Agent角色扮演+数据验证 | `/demand-analysis-synthetic` | 2-4小时 |

## 核心公式

```
Demand (需求) = User (用户) × Situation (场景) × Problem (问题)

演进链：场景 → 任务(JTBD) → 产生差距(Gap) → 阻碍/问题 → 真实需求
```

## 冰山模型速览

```
L1-L2 表层：用户是谁 + 什么场景 + 什么表面痛点
L3 核心任务：用户真正想完成什么（方案中立）
L4 任务地图：8步全流程 + 摩擦点识别
L5 隐藏洞察：四种力量 + 情感/社交驱动力
L6 需求假设：机会卡片 + 最危险假设(RAT)
```

## 参考卡片
- `framework-demand-usp-model` — USP模型
- `framework-demand-iceberg` — 冰山六层模型
- `tool-demand-assessment-triangle` — 需求评估三角形
- `tool-demand-four-forces` — 四种力量建模
- `tool-demand-blindspot-checklist` — 2B/2C盲区清单
