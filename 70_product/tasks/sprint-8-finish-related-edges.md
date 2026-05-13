---
id: sprint-8-finish-related-edges
title: "Sprint 8：完成 panproduct 图边 + 收尾 00_inbox"
status: completed
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-13
target: 2026-05-13
---

## 背景

Sprint 7 未完成：Phase 1（填 related 边）增量为零，Phase 2（清 00_inbox）剩 2 张未清。

Sprint 8 = Sprint 7 的精确重做，不扩范围。

## Phase 1：填 panproduct 工具卡 `related` 边（仅此一项是核心）

### 范围

| 群组 | 数量 | 当前状态 |
|------|:----:|------|
| `yt-panproduct-demand-*` | 11 | `related: []` |
| `yt-panproduct-aesthetic-*` | 4 | `related: []` |
| `yt-panproduct-execution-*` | 19 | `related: []` |
| `yt-personal-pan-product-*` | 6 | `related: []` |
| **合计** | **40** | |

### 核心操作

每张卡的 `## Synthesis` 表里已经有横向关联。比如：

```markdown
## Synthesis
| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 相关工具 | [[yt-panproduct-demand-user-segmentation]] | 用户分层（视角后的细化） |
| 相关工具 | [[yt-panproduct-demand-scenario-walkthrough]] | 场景推演（视角后的场景化） |
```

**直接把 `相关工具` 和 `关联框架` 行的目标节点提取到 frontmatter `related:` 中。** 不需要从零想——Synthesis 表已经替你列好了。

### 每张卡的步骤

1. 打开卡，找到 `## Synthesis` 表
2. 提取所有 `相关工具` / `关联框架` / `深层关联` 行的目标节点
3. 排除已在 `prerequisites` / `component_of` 中的节点
4. 写入 frontmatter `related:` 列表
5. 下一张

### 结果标准

| 卡片 | 预期 related 数 |
|------|:----:|
| panproduct 工具卡（单张） | 2-5 条 |
| personal-pan-product（单张） | 3-6 条 |
| **全部 40 张** | **related: [] 降至 0** |

## Phase 2：清最后 2 张 00_inbox

| 文件 | 问题 |
|------|------|
| `yt-management-goal-management.md` | `source_refs: ["00_inbox/ideas/一堂-课程地图精华串讲.md"]` |
| `yt-management-scientific-hiring.md` | `source_refs: ["00_inbox/ideas/一堂-课程地图精华串讲.md"]` |

确认 `10_raw/sources/一堂-课程地图精华串讲.md` 存在后，直接改路径。5 分钟的事。

## 不做

- ❌ 不新增卡片
- ❌ 不升级 body 格式
- ❌ 不填 framework 卡的边（已在 Sprint 5 完成）
- ❌ 不扩到非 panproduct 域

## 质量门禁

- [ ] `grep 'related: \[\]' 30_wiki/concepts/yt-panproduct-*.md` 返回空
- [ ] `grep 'related: \[\]' 30_wiki/concepts/yt-personal-pan-product-*.md` 返回空
- [ ] `grep '"00_inbox' 30_wiki/concepts/yt-management-*.md` 返回空
- [x] 所有 `related` 条目指向实际存在的卡片（抽查 5 张）

---

## ✅ Sprint 8 完成 (2026-05-13 黄药师)

### Phase 1: related 边填充

| 群组 | 数量 | 结果 |
|------|:----:|------|
| `yt-panproduct-demand-*` | 11 | 11/11 已填，共 28 edges |
| `yt-panproduct-aesthetic-*` | 4 | 4/4 已填，共 11 edges |
| `yt-panproduct-execution-*` | 18 | 18/18 已填，共 46 edges |
| `yt-personal-pan-product-*` | 6 | 6/6 已填，共 20 edges |
| **合计** | **39** | **38 filled (1 already done), 105 edges** |

方法：Python 脚本从 `## Synthesis` 表提取 `相关工具`/`关联框架`/`深层关联` 行，排除 `prerequisites`/`component_of` 中的节点。

### Phase 2: 00_inbox 收尾

- `yt-management-goal-management.md`: `00_inbox/` → `10_raw/sources/` ✅
- `yt-management-scientific-hiring.md`: `00_inbox/` → `10_raw/sources/` ✅
- 全局 `grep '"00_inbox' yt-*.md` → **0 hits** ✅

### 质量门禁

- [x] `related: []` — 39张 panproduct 卡全部有值
- [x] `00_inbox` — 全局 0 hits
- [x] kdo lint: 0 errors, 311 warnings（全部存量）
