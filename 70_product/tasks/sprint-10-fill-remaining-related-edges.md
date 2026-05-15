---
id: sprint-10-fill-remaining-related-edges
title: "Sprint 10：填剩余 related 图边 + 收尾管理域"
status: completed
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-14
target: 2026-05-14
---

## 背景

Sprint 7-8 完成了 panproduct 域 39 张卡的图边填充。剩余 57 张非 panproduct 卡 `related: []` 仍为空——agent 无法沿图边横向跳转。同时管理域 15 张卡从未被任何 sprint 触碰。

## Phase 1：填图边（P0）

### 范围

| 群组 | 数量 | 当前状态 |
|------|:----:|------|
| `yt-entrepreneur-*` | 23 | `related: []` |
| `yt-model-*`（非 panproduct） | 22 | `related: []` |
| `yt-personal-*`（非 panproduct） | 16 | `related: []` |
| `yt-management-*` | 15 | `related: []` |
| **合计** | **76** | |

### 操作

和 Sprint 8 完全一样——每张卡的 `## Synthesis` 表里已经列出了横向关联：

```markdown
## Synthesis
| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 关联工具 | [[yt-entrepreneur-five-step-method]] | 五步法总纲 |
| 关联工具 | [[yt-entrepreneur-scientific-method]] | 科学理念 |
```

**提取 `关联工具` / `关联框架` / `深层关联` 行的目标节点 → 排除已在 `prerequisites` / `component_of` 中的 → 写入 frontmatter `related:`。**

### 结果标准

`grep 'related: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits

## Phase 2：管理域 query_triggers 重写（P1）

### 范围

15 张 `yt-management-*` 卡。Sprint 9 未覆盖（范围限定 entrepreneur + personal）。

### 操作

每张卡手写 5-10 条真实中文搜索词。标准同 Sprint 9 Phase 2。

### 验证

欧阳锋随机抽 2 张管理域卡，query_triggers 全部真实搜索词。

## Phase 3：管理域 Constraints 检查（P1）

### 范围

15 张 `yt-management-*` 卡。

### 操作

- 如 Constraints 含 boilerplate 三条（"信息损失"+"前提假设"+"知行鸿沟"），新增 1 条该工具特有边界
- 如该卡无独立方法论（纯课程索引），跳过并标注

## 不做

- ❌ 不新增卡片
- ❌ 不升级 body 格式
- ❌ 不碰非 yt 前缀的卡

## 质量门禁

- [x] `grep 'related: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits
- [x] 所有 `related` 条目指向实际存在的卡片（抽查 5 张）
- [x] 抽查 2 张管理域卡 query_triggers → 全部真实搜索词
- [x] 抽查 1 张管理域卡 Constraints → 至少 1 条该工具特有边界（如该卡非纯索引）
- [x] `kdo lint` → 0 errors

---

## 最终交付报告（2026-05-15 黄药师）

### Phase 1：related 图边填充

| 指标 | 结果 |
|------|------|
| 修复前 `related: []` 卡数 | 57（23 entrepreneur + 20 model + 14 personal） |
| 修复后 `related: []` 卡数 | 0 |
| 管理域新增 `related:` | 16 张（原本无此字段） |
| 提取方式 | entrepreneur/model/personal: 从 `## Synthesis` 表机械提取；management: 从 body wikilinks 提取 |
| 去重策略 | 排除 `prerequisites` / `component_of` / `source_of` 中已有条目；排除非知识卡引用页 |

### Phase 2：管理域 query_triggers 重写

| 指标 | 结果 |
|------|------|
| 处理卡数 | 16 张 yt-management-* |
| 原状态 | 全部无 `query_triggers` 字段 |
| 新增 | 每卡 8-10 条真实中文搜索词（方法名+核心概念+同义词+问题场景） |
| 实施方式 | 2 并行 agent，各处理 8 张卡，Read → 理解内容 → Edit 插入 |

### Phase 3：管理域 Constraints 检查

| 指标 | 结果 |
|------|------|
| 处理卡数 | 0（跳过） |
| 原因 | 管理卡使用 `## [Critique]` 节而非 `## Constraints & Boundaries`，所有 critique 条目均为工具特有、非三模板 boilerplate（"信息损失"+"前提假设"+"知行鸿沟"未同时出现于任何单卡） |
| 判定 | 无 boilerplate 需修复，按 sprint 规定跳过 |

### 质量门禁

- [x] `grep 'related: []' 30_wiki/concepts/yt-*.md` → 0 hits ✅
- [x] 抽查 3 entrepreneur: barriers/five-step-method/scientific-method → related 全部指向实际存在的 yt-* 卡 ✅
- [x] 抽查 2 management: goal-management/scientific-decision → query_triggers 全部为真实中文搜索词 ✅
- [x] 管理域 Constraints: 0 张卡含完整三模板，现有 `[Critique]` 均为工具特有 ✅
- [x] `kdo lint` → 0 errors, 350 warnings（全部来自非 yt 卡/调研报告） ✅

### 已更新文件

| 类别 | 数量 | 操作 |
|------|:----:|------|
| yt-entrepreneur-*.md | 23 | related 从 Synthesis 表提取 |
| yt-model-*.md | 20 | related 从 Synthesis 表提取 |
| yt-personal-*.md | 14 | related 从 Synthesis 表提取 |
| yt-management-*.md | 16 | related 从 body wikilinks 提取 + query_triggers 新增 |
| **合计** | **73** | |

### 已知残留（非阻塞）

- `yt-model-prompt-engineering.md` 无 `related:` 字段——属 prompt-engineering 域，不在 Sprint 10 范围内
- 其他非 scope 卡（yt-prompt-*, yt-concept-*, yt-case-*, yt-research-*, yt-system-*）无 `related:` 字段——均不在本次 sprint 范围
- kdo lint 的 350 warnings 全部来自非 yt 卡的历史问题
