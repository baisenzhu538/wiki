---
id: task_20260629_vikki-five-tag-quality-labels
type: task
status: queued
assignee: 黄药师
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
related:
- 30_wiki/frameworks/framework-kdo-quality-gate
- 30_wiki/systems/system-kdo-frontmatter-schema
---

# 将 Vikki 五标签系统转化为 KDO 卡片质量标签

## 目标

把 Vikki 战队群聊运营中的五标签系统（💡洞察、🎯假设、✅实践、🔥金句、❤️为什么）迁移为 KDO 知识库的卡片质量/类型标签体系，提升 30_wiki 卡片的可检索性、可审核性和跨角色协作效率。

## Vikki 五标签原义

| 标签 | 含义 | KDO 映射方向 |
|:---:|:---|:---|
| 💡 洞察 | 有价值的发现 | `insight` — 卡片核心 claims 是否有新洞察 |
| 🎯 假设 | 待验证的判断 | `hypothesis` — 卡片中的判断是否需要后续验证 |
| ✅ 实践 | 可落地的方法 | `actionable` — 卡片是否包含可执行步骤 |
| 🔥 金句 | 值得记录的话 | `quotable` — 是否有高传播性表述 |
| ❤️ 为什么 | 底层逻辑 | `principle` — 是否解释了背后的因果机制 |

## 执行方案（二选一或组合）

### 方案 A：frontmatter tags 扩展

在现有 `tags:` 字段基础上，允许使用标准化质量标签：

```yaml
tags:
  - insight
  - actionable
  - principle
```

### 方案 B：新增 `quality_labels` 专用字段

```yaml
quality_labels:
  - insight
  - hypothesis
  - actionable
  - quotable
  - principle
```

### 方案 C：双轨制（推荐）

- `quality_labels` 用于结构化机器识别
- `tags` 保留自由标签供人阅读

## 执行要求

1. 黄药师评估三种方案对现有 `kdo lint` / `kdo query` / `kdo pre-submit` 的影响。
2. 若新增字段，同步更新 `90_control/schemas/` 或 kdo 源码中的 frontmatter schema。
3. 编写迁移脚本，对现有 30_wiki 卡片按内容自动/半自动打标签（首批可抽样 50 张）。
4. 更新 `.agent/laowantong-context.md`，让老顽童生产卡片时主动选择 quality_labels。
5. 在 `30_wiki/index.md` 或某个 system 卡中建立「KDO 卡片质量标签使用指南」。

## 验收标准

- 新增标签体系通过 `kdo pre-submit` 不报错
- 至少 50 张现有卡片完成标签迁移
- `kdo query --label actionable` 或等效命令可过滤出可执行卡片
- 欧阳锋抽查：标签与卡片内容真实匹配，无机器误标
