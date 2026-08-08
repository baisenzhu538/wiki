---
id: concept-truman-feature-six-stages
title: 「概念：Feature学习六阶段——从偶遇到肌肉记忆」
type: concept
status: draft
confidence: 0.90
trust_level: high
domain:
  - ai-basic
  - methodology
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
source_person: Truman
source_context: Truman口述下 L816-858（六阶段+Feature用会的）
reviewed_by: 待审
aliases:
  - 六阶段
  - 偶遇理解尝试内核边界肌肉记忆
discoverable_by:
  - 六阶段
  - Feature学习
  - 偶遇
  - 肌肉记忆
related:
  - framework-truman-feature-thinking-core
  - concept-truman-feature-four-scenarios
  - concept-一堂-基本功-刻意练习四要素
  - tool-Truman-Feature特性层训练法
tags:
  - method:learning
  - method:feature-thinking
  - scene:ai-learning
  - audience:general
  - content-format:concept
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - actionable
  - cited
diagnostic_signals:
  - signal: "学了一个Feature但下次还是不会用"
    lens: 卡在"理解→尝试"之间——理解了概念但没在真实项目里用过
    follow_up: 强制：本周内在真实任务中用一次这个Feature，记录效果
  - signal: "Feature用了很多次但遇到新场景还是不知道怎么调"
    lens: 可能没到"边界"阶段——只知道什么时候有效，不知道什么时候失效
    follow_up: 刻意制造一次失败——在极限场景下测试这个Feature的边界
---

> 本卡属于AI基本功域——Feature学习的六阶段路径。与 `[[concept-truman-feature-four-scenarios]]`（四场景）互补：四场景是"在哪用"，六阶段是"怎么学会"。

# Feature学习六阶段：从偶遇到肌肉记忆

> 一句话：不是听懂了就会了——从第一次听到一个Feature到它成为你的肌肉记忆，要经过六个阶段。大多数人停在"理解"——理解了但没用过，等于不会。

---

## 六阶段

```
偶遇(听) → 理解(想) → 尝试(做) → 内核(成) → 边界(败) → 肌肉记忆(练)
```

| 阶段 | 标志 | 验证方式 |
|:---|:---|:---|
| **1. 偶遇** | 第一次听到这个Feature | "哦，还有这种东西" |
| **2. 理解** | 能用自己的话说清楚这个Feature是干什么的 | 给别人讲一遍，对方能懂 |
| **3. 尝试** | 在真实项目中用过至少一次 | 有输出物——不是练习，是生产环境 |
| **4. 内核** | 用这个Feature稳定拿到好结果——成了 | 连续3次成功，不再翻车 |
| **5. 边界** | 知道这个Feature在什么情况下**失效** | 能说出至少2个不适合用的场景 |
| **6. 肌肉记忆** | 不需要想——遇到场景自动掏出来用 | 别人问你"为什么这么用"，你说"就是该这么用" |

---

## 关键洞察：Feature不是学会的，是用会的

> "你如果没有真正做出来过，你连实验都没做出来过——这个Feature对你来讲价值很低。"（口述下L834-836）

| 常见陷阱 | 说明 |
|:---|:---|
| 停在"理解" | 课听懂了、笔记记了——但从没用过。等于白学 |
| 跳过"边界" | 知道什么时候有效——不知道什么时候失效。换个场景就翻车 |
| 虚假的"肌肉记忆" | 用一个Feature做了10次同类任务——不是肌肉记忆，是路径依赖 |

**最小验证**：一个新Feature从偶遇到内核，至少需要在3个**不同的**项目和场景中使用过。

---

## 与KDO卡片生命周期的同构

| 六阶段 | KDO卡片生命周期 |
|:---|:---|
| 偶遇→理解 | 素材消化→诊断 |
| 尝试→内核 | draft→enriched→reviewed |
| 边界→肌肉记忆 | 反馈→迭代→stable |

"卡片不是入库就完了——入库只是'内核'阶段。真正到'肌肉记忆'，是这张卡被5个不同的人在5个不同场景中调用过。"

## When NOT to Use
- 一次性任务不需要建Feature练习计划
- "听完了"≠"可以练"——需要先有真实项目

## Critique
六阶段假设所有人都有"真实项目"可以练习。对于纯学习者（无项目），从"理解"到"尝试"之间有巨大鸿沟。这也是"Feature不是学会的是用会的"的最大挑战——不是不想用，是没地方用。
