---
id: task_20260704_laowantong-human-in-loop-dual-triangle-principle
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: null
related:
- "[[annotation-yihang-dual-triangle-master]]"
- "[[tool-Truman-人在环渐进自动化策略]]"
- "[[concept-yihang-dual-triangle-core]]"
- "[[framework-yitang-shishi-qiushi]]"
---

# 任务 #67：人在环与双三角关系说明卡

## 任务目标

产出一张 concept/framework 卡（建议 id：`concept-yihang-human-in-loop-dual-triangle-relation` 或 `framework-yihang-human-in-loop-dual-triangle-principle`），澄清「人在环」与「双三角」的关系，形成「原则 ↔ 能力」互补的清晰认知。

## 核心命题

1. 人在环（human-in-the-loop）是人机协作的早期主流概念，解决的是「AI 执行时关键节点需要人确认」的运行时安全问题。
2. 双三角是人在环的能力层深化：不仅要知道「人在哪里」，还要知道「人要练什么」。
3. 两者不是替代关系，而是互补关系：人在环定治理规则，双三角定能力建设。

## 原始素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt` 第 4556 行：「人机协作之前好像只有一个主流，就是人在环」
- `30_wiki/tools/tool-Truman-人在环渐进自动化策略.md`：已有基础草稿，但质量低、src_unknown
- `30_wiki/tools/tool-Truman-双三角模型应用.md`：已有基础草稿，但质量低、src_unknown
- 王语嫣入口标注：`60_feedback/annotations/annotation-yihang-dual-triangle-master.md` 第 1.1 节

## 卡片必须包含的内容

### 1. 三层次关系图

```
Y模型（底层引擎）
    ↓ 驱动
人在环（治理原则）—— 人在哪些节点把关、如何渐进自动化
    ↓ 需要能力支撑
双三角（能力地图）—— 审美/体系/创造力 + 场景/数据/基本功
    ↓ 落地为
Skills / Workflows / Agents / DataPacks
```

### 2. 对比表

| 维度 | 人在环 | 双三角 |
|:---|:---|:---|
| 回答的问题 | 人在哪里确认/干预？ | 人要练什么能力？ |
| 核心动作 | 把关、校准、渐进自动化 | 补短板、建系统、设计飞轮 |
| 产出形态 | 决策节点图、自动化路线图 | 六要素画布、武器库、飞轮 |
| 适用阶段 | 运行时 | 能力建设时 |
| 风险 | 过度干预或过度放任 | 能力短板导致无法有效把关 |

### 3. 组合使用原则

- 先用双三角诊断六要素短板
- 再设计人在环的介入节点
- 随着 AI 能力稳定和场景成熟，逐步后移人在环节点
- 但审美和创造力的最终判断权始终在人

## 验收标准

- `kdo pre-submit` 通过
- 清晰区分「原则」和「能力」
- 有图示或表格说明关系
- 指出与已有 `tool-Truman-人在环渐进自动化策略.md` 的关系（建议合并或重定向）
- 欧阳锋终审通过

## 备注

本任务也可考虑与 `tool-Truman-人在环渐进自动化策略.md` 合并升级，而不是新建卡。具体方案由老顽童根据素材情况判断，但必须在任务产出中说明处理理由。
