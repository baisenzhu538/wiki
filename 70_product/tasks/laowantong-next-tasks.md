# 老顽童后续任务

> **更新：2026-06-12** — 修正指令 + 下一轮任务。

---

## 🎯 当前执行顺序

| 顺序 | 任务 | 状态 | 参考 |
|:----:|:-----|:----:|:-----|
| **1** | **🔴 修正：P0 旧卡补互链 — 未完成对** | **✅ 已完成** | 2对全部修复+双向链已补 |
| **2** | **旧卡补互链 — P1 批次** | ⏳ | P0 完成后 |
| — | Pyramid Principle（已由洪七公完成） | ✅ | 不重复做 |
| — | P0 互链前 5 对 | ✅ | 已确认双向链接 |

---

## 🔴 任务 1：修正 — P0 旧卡补互链未完成对

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
