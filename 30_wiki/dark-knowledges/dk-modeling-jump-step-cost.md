---
id: dk-modeling-jump-step-cost
title: "跳步代价：前置输入为空，后半段十倍百倍惩罚"
type: dk
status: draft
confidence: 0.88
trust_level: high
domain:
  - modeling
author: 老顽童
reviewed_by: 待审
review_date: "2026-07-19"
created_at: "2026-07-19"
updated_at: "2026-07-19"
quality_labels:
  - insight
  - principle
source_refs:
  - "00_inbox/Advanced modeling/ 口述 L2718-L2728"
  - "00_inbox/Advanced modeling/ 口述 L2378-L2384"
related:
  - dk-process-is-scar-tissue
  - concept-truman-18-component-cards
  - framework-modeling-relation-exploration
  - modeling-level-map
  - framework-kdo-modeling-methodology
---

# 跳步代价：前置输入为空，后半段十倍百倍惩罚

> 一句话："依赖关系是不可逆的。跳步的代价不是'多做一点'——而是前置输入为空，你后半段做的事全都是建立在空气上。埋的雷在后半段会有十倍百倍的惩罚。"

---

## 原始表述

> 口述 L2718-L2728, L2378-L2384

Truman 对跳步代价的警告：

"流程建模里最危险的不是拆错了——是跳过了一步。跳步意味着什么？意味着你要做的那一步的前置输入是空的。你所有的后续工作都是建立在一个空的、不存在的前提上的。这个雷不会在跳过的时候炸——它会在后半段炸，而且惩罚是十倍百倍的。"

---

## 使用场景

- 流程执行中反复出问题但找不到原因
- 建模时觉得"这步太简单，跳过吧"
- 团队说"我们都知道的，不用显式写出来"

---

## 操作方法

### 跳步检测清单

每当你觉得某个步骤可以跳过时，问三个问题：

1. **这步有输出吗？** → 如果有，它的输出是谁的输入？跳过它 = 那个后续步骤没有输入
2. **这步对应的组件牌是什么？** → 如果找不到对应的牌，可能确实不需要。找到了 → 不能跳
3. **上次跳过这步发生了什么？** → 如果这是第一次做，不要跳。如果有历史数据，看跳步后的失败率

---

## 适用边界

- ✅ 复杂流程、多步骤依赖的场景
- ✅ 团队协作流程（跳步最常发生在"我以为你知道"的场景）
- ❌ 个人习惯性操作（非团队依赖）——约束可以适当放松

---

## 为什么值钱

这是 Truman 方法论中最实用的"反模式"警告。大多数流程失败不是设计错误，是执行时跳了关键步骤——建模的价值就在于把那些"容易被跳但跳了就出事"的步骤显式化。

---

## 与其他知识的关联

- `dk-process-is-scar-tissue`：跳步 = 撕开旧疤痕 = 再流一次血
- `framework-modeling-relation-exploration`：依赖关系分析就是为了找到"跳了就出事"的关键步骤
