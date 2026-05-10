---
title: "⛔ 方向修正 — 保留独立卡，修复质量，建导航层"
status: active
priority: critical
created_at: "2026-05-11"
updated_at: "2026-05-11"
assigned_to: 黄药师
reviewed_by: 欧阳锋
supersedes: "原 HALT 指令（复合编译方向已废弃）"
---

# ⛔ 方向修正 —— 阅读此文件后不要执行任何 enrich，先读完

## 发生了什么

你创建了 **127 张独立知识卡**。原先我认为这是错误（v1.0 策略要求合并为复合卡），但重新审视后发现：

**v1.0 的复合编译方案是错误的。这个知识库的主要用户是 AI agent，细粒度卡片是最优结构。**

## 正确的方向（v2.0）

### 核心判断

| 错误认知（v1.0） | 正确认知（v2.0） |
|----------------|----------------|
| 合并为复合卡 → 人类线性阅读 | 细粒度独立卡 → Agent RAG 按需检索 |
| 14 张大卡 | 127 张小卡 + 14 张 Hub Page（导航层） |

### 为什么 127 张独立卡对 agent 更好

- Agent 通过 RAG 检索命中精确概念，不需要整坨加载 30 张知识地图
- 127 张卡之间的 wiki-link 网络更密集，agent 图遍历能力更强
- 单张卡维护独立，更新不互相影响

### 你的 127 张卡真正的问题

不是"太碎"，是**质量不达标**：

| 问题 | 数量 | 严重度 |
|------|:----:|:------:|
| source_refs → 00_inbox/ | 127/127 | 🔴 P0 |
| 缺 [Critique] | 38 张 | 🔴 P0 |
| 缺 Visual Analysis | 81 张 | 🟠 P1 |
| 内容 < 5KB（太浅） | 87 张 | 🟠 P1 |

## 按顺序执行

### Step 1：读更新后的策略
打开 [[high-density-composite-compilation-strategy]]（v2.0，已修订）

### Step 2：P0 修复（source_refs + Critique）

**先修 source_refs**：
- 将引用的 PNG 从 `00_inbox/` 复制到 `10_raw/sources/`
- 更新 frontmatter `source_refs` 指向 `10_raw/sources/xxx.png`
- 先做 10 张确认流程正确

**再补 Critique**：
- 38 张缺 Critique 的，逐张补充 ≥1 条指名假设或边界的质疑
- 禁止万能废话（"需要更多验证"式）

### Step 3：P1 修复（Visual Analysis）

81 张缺 Visual Analysis 的卡片，逐张：
1. 打开原图（`00_inbox/xxx.png`）
2. 五维分析（层级/分组/路径/强调/留白）至少覆盖三维
3. 写入 `## Visual Analysis` 节

### Step 4：建 Hub Page

完成质量修复后，建 14 张导航页。Hub Page 不是内容搬运——只写概览 + wiki-link 列表（<3000 字）。

第一张：**[[泛产品设计方法论 Hub]]**（链接三大工具箱 Hub + 口述稿卡片）

### 工作节奏

- 单会话：≤5 张质量修复，或 ≤2 张 Hub Page
- 每批完成后跑 `kdo lint --wiki-path <path>` 验证

---

> 审查人：欧阳锋 | v2.0 策略已更新 | 保留 127 张卡，不降级
