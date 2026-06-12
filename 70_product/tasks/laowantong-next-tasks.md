# 老顽童后续任务

> **更新：2026-06-12** — 修正指令 + 下一轮任务。

---

## 🎯 当前执行顺序

| 顺序 | 任务 | 状态 | 参考 |
|:----:|:-----|:----:|:-----|
| **1** | **🔴 P1 旧卡补互链 — 核心工具卡 20 张** | **🔜** | 深黑节点互连已完成，扩大到 20 张核心工具卡 |
| **2** | **旧卡补互链 — P2 批次** | ⏳ | P1 完成后 |
| — | Pyramid Principle（已由洪七公完成） | ✅ | 不重复做 |
| — | P0 互链前 5 对 | ✅ | 已确认双向链接 |

---

## 🔴 任务 1：P1 旧卡补互链 — 核心工具卡 20 张

**为什么：** P0 修的是"深黑节点"（被大量引用的入口卡），P1 修的是"核心工具卡"（各步骤的实操工具，它们之间应该互连但尚未连接）。

### P1 批次清单

以下 10 对共 20 张卡，每对在 `related` 中互相添加上对方：

| 对 | 左 | 右 | 关联理由 |
|:--:|:---|:---|:---------|
| 1 | `yt-five-step-implementation` | `yt-tool-product-core-canvas` | 五步法落地实操需要产品内核画布 |
| 2 | `yt-unit-model-build` | `yt-unit-model-selection` | 单元模型搭建→选择的递进关系 |
| 3 | `yt-panproduct-execution-hypothesis-decomposition` | `yt-entrepreneur-key-hypotheses` | 泛产品假设拆解与一堂关键假设互参 |
| 4 | `yt-decision-width-method` | `yt-decision-depth-ladder` | 决策宽度→深度的递进关系 |
| 5 | `yt-model-five-step-canvas` | `yt-tool-product-core-canvas` | 五步法画布→产品内核画布的工具链 |
| 6 | `yt-research-osl-framework` | `yt-research-industry-canvas` | OSL调研框架→行业分析画布的搭配 |
| 7 | `yt-management-toolkit-overview` | `yt-tool-meeting-designer` | 管理工具箱→具体工具的引用 |
| 8 | `yt-personal-deep-review` | `yt-personal-knowledge-extraction` | 深度复盘→知识萃取的递进 |
| 9 | `yt-tool-foresight-canvas` | `yt-foresight-business-spectrum` | 预判画布→终局光谱图的配套使用 |
| 10 | `yt-model-cognitive-upgrade-framework` | `yt-model-entrepreneur-map` | 认知升级→创业地图的跨域对照 |

### 操作方法

跟 P0 一样：每张卡在 `related` 中加对方的 ID。双向。完成后 `updated_at` 更新。

---

## 任务 2：P2 旧卡补互链

P1 完成后通知欧阳锋。

### 问题

你之前补了机会预判域的互链，7 对深黑节点中完成了前 5 对。以下 2 对的 `related` 字段还是旧的 dict 格式（`{'series': False}`），需要先修复格式才能加链接。

#### 对 ⑥：`yt-five-step-method` ↔ `yt-entrepreneur-five-step-method`

**当前状态：**
```
yt-five-step-method 的 related: {'series': False}  ← 非法格式
```

**修正操作：**
1. 在 `yt-five-step-method.md` 的 frontmatter 中，把 `related: {'series': False}` 改为：
   ```yaml
   related:
     - "yt-entrepreneur-five-step-method"
   ```
2. 确认 `yt-entrepreneur-five-step-method` 的 `related` 已有 `yt-five-step-method`（如果没有就加上）

#### 对 ⑦：`yt-model-progress-map` ↔ `yt-model-entrepreneur-map`

**当前状态：**
```
yt-model-progress-map 的 related: {'level': 'foundational'}  ← 非法格式
```

**修正操作：**
1. 在 `yt-model-progress-map.md` 的 frontmatter 中，把 `related: {'level': 'foundational'}` 改为：
   ```yaml
   related:
     - "yt-model-entrepreneur-map"
     - "yt-model-management-map"
     - "yt-model-personal-map"
   ```
2. 确认 `yt-model-entrepreneur-map` 的 `related` 已有 `yt-model-progress-map`（如果没有就加上）

### 为什么要修

`related: {'series': False}` 和 `related: {'level': 'foundational'}` 是早期手写 YAML 解析器（P-18）产生的非法格式。`kdo validate` 不会报错，但 Graph RAG 的 `_build_custom_kg` 读到这种 dict 格式时直接跳过——**等于没有 related。** 这也是图谱放射状的原因之一——这些链接从未被图真正摄入过。

---

## 任务 2：旧卡补互链 — P1 批次

等 P0 修正完成并通知欧阳锋后，再给 P1 列表。
