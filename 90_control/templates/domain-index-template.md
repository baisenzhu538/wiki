---
id: domain-index-template
title: 域索引入口卡模板
type: index
status: draft
domain:
  - master
  - kdo
source_context: KDO 域建制基础设施——黄药师从 five-step-domain-digest 和 一堂方法论体系总图 提炼的可复用模式
created_at: "2026-06-21"
author: 黄药师
---

# 域索引入口卡模板

> **用途**：当一个知识域超过 30 张卡片时，必须创建域索引入口卡。这是域的「目录页」——让后来者知道这个域有什么、从哪开始读。

## 结构（四段式）

```markdown
# 域摘要：<域名称>

> N 张卡 · 核心关键词 · 一句话价值主张

## 核心框架（先读）

| 卡 | 类型 | 做什么 |
|:--|:--|:--|
| `card-id` | framework | 一句话描述 |
| `card-id` | tool | 一句话描述 |

## 关键案例

| 卡 | 行业/场景 | 核心教训 |
|:--|:--|:--|
| `case-id` | 行业 | 一句话教训 |

## 暗知识（不要踩的坑）

| 卡 | 一句话 |
|:--|:--|
| `dk-id` | 反常识/陷阱一句话 |

## 工具索引（按场景查）

| 场景 | 用这张卡 |
|:--|:--|
| 我要做X | `tool-xxx` |
```

## 铁律

1. **30 张卡以上必须建索引入口**——不管用什么方式组织。低于 30 张可以暂时不建，但 Wave 规划阶段就要预留 ID。
2. **索引入口卡只链接、不重复内容**。它是导航 hub，不是内容摘要。每行一句话，绝不超过一行。
3. **每张被引用的卡必须真实存在**。索引入口卡写入前跑 `check-source-refs.py --card <index-id>` 验证死链。
4. **索引入口卡放在 `30_wiki/domains/`**，文件名格式 `{domain}-domain-digest.md`。
5. **索引入口卡必须在 `30_wiki/index.md` 中登记**。
6. **域内新增/删除卡片时必须同步更新索引入口卡**——索引入口卡过时比没有更糟糕。

## 示例

见 `30_wiki/domains/five-step-domain-digest.md`（五步法域，66 张卡）

## 配套基础设施

| 工具 | 用途 |
|:--|:--|
| `check-source-refs.py` | 验证索引入口卡的所有链接是否有效 |
| `track-production-progress.py` | 追踪域内卡片的生产进度 |
| `kdo lint` | 验证索引入口卡的 frontmatter 格式 |
