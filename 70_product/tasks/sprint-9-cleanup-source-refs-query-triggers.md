---
id: sprint-9-cleanup-source-refs-query-triggers
title: "Sprint 9：修复 source_refs 空值 + query_triggers 污染"
status: pending
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-13
target: 2026-05-14
---

## 背景

Sprint 6 终审发现三个遗留问题：
1. **source_refs 空值**：57 张卡 `source_refs: []`，KF-020 违规
2. **query_triggers 污染**：Batches 3-4 的 query_triggers 被自动从 section headers 提取（如 "与一堂方法论的关系"、"从知道到做到的鸿沟"），非真实搜索词
3. **Constraints 模板化**：~20 张 entrepreneur 卡共用 boilerplate 三条（"信息损失"+"前提假设"+"知行鸿沟"），非该工具特有边界

## Phase 1：source_refs 空值修复（P0，先做）

### 范围

```
grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md
```

| 前缀 | 数量 |
|------|:----:|
| `yt-entrepreneur-*` | 20 |
| `yt-management-*` | 15 |
| `yt-model-*` | 7 |
| `yt-personal-*` | 7 |
| **其他 yt- 卡** | ~8 |
| **合计** | **~57** |

### 操作

每张卡的 source_refs 需指向实际存在的 `10_raw/sources/` 或 `10_raw/assets/yitang/` 文件：

1. 检查该卡对应的一堂课程——多数 entrepreneur/management/personal 卡源自 `10_raw/sources/一堂-课程地图精华串讲.md`
2. 如该卡有独立源文件（如 `一堂-个人修炼-时间管理必修课.md`），指向独立文件
3. 如无独立源文件，指向课程地图串讲
4. **绝不**指向 `00_inbox/`

### 验证

`grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits

## Phase 2：query_triggers 重写（P1）

### 范围

Batches 3-4 共 ~40 张卡（entrepreneur + personal 非 panproduct）。

### 问题症状

以下类型的 "triggers" 无效：
- 从 `## Critique` / `## Constraints` headers 提取的句子
- "与一堂方法论的关系" / "关联卡片" / "关键概念" 等通用 section 名
- "从知道到做到的鸿沟" / "方法论的前提假设需要检验" 等 critique 文本

### 重写标准

每条 query_triggers 应满足：
- 用户可能实际输入的中文搜索词
- 5-10 条
- 包含：工具名/方法名 + 核心概念 + 同义词/别名 + 问题场景描述

**正确示例**（来自 `yt-personal-time-management`）：
```yaml
query_triggers:
  - 时间管理
  - 优先级管理
  - 高能量窗口
  - 深度工作
  - 保护时间块
  - 日历管理
  - 时间分配
  - L3战略层
```

**错误示例**（来自抽检发现的污染）：
```yaml
query_triggers:
  - 与一堂方法论的关系
  - 从知道到做到的鸿沟
  - 关联卡片
  - 关键概念
```

### 验证

欧阳锋随机抽 3 张卡，query_triggers 全部为真实搜索词。

## Phase 3：Constraints 去模板化（P1）

### 范围

~20 张 entrepreneur 卡 Constraints 节疑似使用相同模板。

### 筛选标准

优先修复满足以下条件之一的卡：
- 当前 Constraints 仅含 boilerplate 三条（"信息损失"+"前提假设"+"知行鸿沟"）
- 该工具在 domain 中有独特边界（与其他工具存在交叉/冲突/互补的边界）

### 操作

每张卡至少 1 条 **该工具特有的** boundary claim：
- 具体场景（什么时候这个工具不好用？）
- 失败模式（用了但失败了，典型症状是什么？）
- 条件依赖（需要什么前置条件？缺了什么会失效？）

### 不修的情况

如果该卡确实只是课程目录索引（无独立方法论），Constraints 可为空——但应在 body 中明确标注卡片性质。

## 不做

- ❌ 不升级 body 格式（已在 Sprint 6 完成）
- ❌ 不填 related 边（panproduct 域已在 Sprint 7-8 完成，非 panproduct 域留 Sprint 10）
- ❌ 不新增卡片

## 质量门禁

- [ ] `grep 'source_refs: \[\]' 30_wiki/concepts/yt-*.md` → 0 hits
- [ ] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` → 0 hits（全局仅剩 paddleocr-skill.md）
- [ ] 抽查 3 张 entrepreneur 卡 query_triggers → 全部真实搜索词
- [ ] 抽查 3 张 personal 卡 query_triggers → 全部真实搜索词
- [ ] 抽查 2 张 entrepreneur 卡 Constraints → 至少 1 条该工具特有边界
