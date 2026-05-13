---
id: sprint-7-fill-related-edges
title: "Sprint 7：填充 panproduct 域图边 + 清理残留 00_inbox"
status: closed_incomplete
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-12
target: 2026-05-12
---

## 背景

Sprint 5-6 完成了 panproduct 域 46 张卡的 agent-native 升级。但 `related: []` 字段几乎全空——这意味着 agent 检索时只能沿 `component_of`（上挂）方向展开，无法做横向关联跳转。

Sprint 7 优先填图边，然后清理其他域的 00_inbox 残留。

## Phase 1：填 panproduct 域 `related` 图边（P0）

### 范围

| 类型 | 数量 | 文件前缀 |
|------|:----:|------|
| composite + framework | 7 | `yt-composite-pan-product-*`, `yt-model-pan-product-*` |
| 工具卡（需求） | 11 | `yt-panproduct-demand-*` |
| 工具卡（审美） | 4 | `yt-panproduct-aesthetic-*` |
| 工具卡（落地） | 19 | `yt-panproduct-execution-*` |
| 课程笔记 | 6 | `yt-personal-pan-product-*` |
| **合计** | **47** | |

### 填边规则

每张卡的 `related:` 应包含 2-6 张**不在 prerequisites/component_of 里**的相关卡片。四种关联类型：

| 类型 | 含义 | 示例 |
|------|------|------|
| **顺序** | A → B 有先后依赖 | 用户视角 → 场景推演（先代入用户，再推演场景） |
| **互补** | A + B 组合使用效果更好 | 动力阻力 + 峰终定律（动力阻力定方向，峰终定体验） |
| **交叉域** | 需求域的 A 影响落地域的 B | 问题洞察 → 内核和边界（深层需求决定内核定义） |
| **深层关联** | 概念同构但域不同 | 复盘迭代 ↔ 深度复盘冰山图（同一概念的工具卡 vs 框架卡） |

### 操作方式

1. 打开每张卡，读 `## Synthesis` 表——这些表里已经列出了部分横向关联，直接提取到 frontmatter `related:` 中
2. 读 `## Claims` 内容，判断与其他卡的概念关联
3. 优先填**交叉域**边（需求↔落地、审美↔落地），这类边检索价值最高

### 验证

完成后，任意抽一张卡，`related:` 非空且指向的卡片确实存在。

## Phase 2：清理 21 张 00_inbox 残留（P1）

### 范围

| 前缀 | 数量 | 问题 |
|------|:----:|------|
| `yt-model-*` | 9 | `source_refs: "00_inbox/..."`（图片） |
| `yt-entrepreneur-*` | 5 | `source_refs: "00_inbox/..."`（文本+图片） |
| `yt-personal-*` | 5 | `source_refs: "00_inbox/..."`（文本） |
| `yt-management-*` | 2 | `source_refs: "00_inbox/..."`（文本） |
| **合计** | **21** | |

### 操作

1. 确认 `10_raw/sources/` 或 `10_raw/assets/yitang/` 中已有对应源文件
2. 归档缺失的源文件（如有）
3. 修改 source_refs → `10_raw/` 路径
4. **仅修 source_refs**，不做 Phase 2-3（frontmatter + body 升级留到后续 sprint）

### 验证

`grep -r '"00_inbox' 30_wiki/concepts/yt-*.md` 返回空

## 质量门禁

- [x] framework 卡 related 已有（Sprint 5 遗产，非 Sprint 7 新增）
- [ ] panproduct 域 `related: []` 空卡降至 0 → **未完成：39/46 仍为空**
- [ ] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` 返回空 → **未完成：2 张残留**
- [ ] 所有 `related` 条目指向实际存在的卡片

---

## Sprint 7 审查结论 (2026-05-13 欧阳锋)

**不通过。** Phase 1（填 related 边）增量为零——framework 卡的边是 Sprint 5 已有的，39 张工具卡全部未动。Phase 2 清理了 19/21 张 00_inbox，剩 2 张管理域。

→ 复刻为 [[sprint-8-finish-related-edges]]，缩小范围，只做这两件事。
