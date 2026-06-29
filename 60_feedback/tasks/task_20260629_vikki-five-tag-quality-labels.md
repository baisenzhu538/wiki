---
id: task_20260629_vikki-five-tag-quality-labels
type: task
status: queued
assignee: 黄药师
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-30
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- 30_wiki/frameworks/framework-kdo-quality-gate
- 30_wiki/systems/system-kdo-frontmatter-schema
- framework-brand-three-degree
---

# Vikki 五标签 + 大馨品牌三度 → KDO 卡片质量标签体系

## 目标

把 Vikki 战队的群聊运营标签系统与大馨战队的品牌三度体系融合，建立一套**既描述卡片内容类型、又评估卡片质量层级**的 KDO 卡片质量标签体系，提升 30_wiki 卡片的可检索性、可审核性和跨角色协作效率。

## 输入模型

### Vikki 五标签（内容类型维度）

| 标签 | 含义 | KDO 映射 |
|:---:|:---|:---|
| 💡 洞察 | 有价值的发现 | `insight` |
| 🎯 假设 | 待验证的判断 | `hypothesis` |
| ✅ 实践 | 可落地的方法 | `actionable` |
| 🔥 金句 | 值得记录的话 | `quotable` |
| ❤️ 为什么 | 底层逻辑 | `principle` |

### 大馨品牌三度（质量层级维度）

| 维度 | 品牌含义 | KDO 卡片映射 |
|:---:|:---|:---|
| 知名度 | 让人知道你是谁 | `cited` — 被引用次数 / 入度 |
| 美誉度 | 让人喜欢你、信任你 | `quality` — lint/审查质量评分 |
| 信任度 | 让人愿意为你付费 | `validated` — 实战验证 / source_refs 可信度 |

## 融合后的 KDO 质量标签体系

```yaml
quality_labels:
  # 内容类型（Vikki）
  - insight        # 有新洞察
  - hypothesis     # 待验证判断
  - actionable     # 可执行步骤
  - quotable       # 高传播性表述
  - principle      # 解释因果机制
  # 质量层级（大馨）
  - cited          # 被多次引用
  - quality        # 审查质量高
  - validated      # 有实战验证
```

## 执行方案

### 方案 A：扩展 `tags:` 字段（推荐）

在现有 `tags:` 中允许标准化质量标签，与自由标签共存：

```yaml
tags:
  - insight
  - actionable
  - validated
  - 渠道增长
```

### 方案 B：新增 `quality_labels:` 字段

机器可读的结构化字段：

```yaml
quality_labels:
  - insight
  - actionable
  - validated
```

### 方案 C：双轨制

- `quality_labels` 用于机器识别和过滤
- `tags` 保留自由标签供人阅读

## 执行要求

1. 黄药师评估三种方案对 `kdo lint` / `kdo query` / `kdo pre-submit` 的影响。
2. 若新增字段，同步更新 kdo 源码中的 frontmatter schema。
3. 编写迁移脚本，对现有 30_wiki 卡片按内容自动/半自动打标签（首批 50 张）。
4. 更新 `.agent/laowantong-context.md`，让老顽童生产卡片时主动选择 quality_labels。
5. 在 `30_wiki/index.md` 或 `30_wiki/systems/` 中建立「KDO 卡片质量标签使用指南」。
6. 同步生产一张 `framework-brand-three-degree` 概念卡，作为品牌三度体系在 KDO 中的沉淀。

## 验收标准

- 新增标签体系通过 `kdo pre-submit` 不报错
- 至少 50 张现有卡片完成标签迁移
- `kdo query --label actionable` 或等效命令可过滤出可执行卡片
- 欧阳锋抽查：标签与卡片内容真实匹配，无机器误标
