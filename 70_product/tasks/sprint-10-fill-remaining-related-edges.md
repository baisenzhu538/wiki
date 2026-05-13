---
id: sprint-10-fill-remaining-related-edges
title: "Sprint 10：填剩余 related 图边 + 收尾管理域"
status: pending
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

- [ ] `grep 'related: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits
- [ ] 所有 `related` 条目指向实际存在的卡片（抽查 5 张）
- [ ] 抽查 2 张管理域卡 query_triggers → 全部真实搜索词
- [ ] 抽查 1 张管理域卡 Constraints → 至少 1 条该工具特有边界（如该卡非纯索引）
- [ ] `kdo lint` → 0 errors
