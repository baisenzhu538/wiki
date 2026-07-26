---
id: diag-20260726-huangyaoshi-index-pipeline-upgrade
title: "索引管道升级：让 aliases/tags/discoverable_by 进入检索层"
type: diagnosis
status: draft
author: 黄药师
reviewed_by: 待王语嫣审
created_at: "2026-07-26"
updated_at: "2026-07-26"
source_refs:
  - 90_control/tag-registry.yaml
  - kdo-tools/mcp/tools.py
  - KDO/search_index.py
  - KDO/commands/delivery.py
related:
  - framework-kdo-retrieval-architecture-v2
  - framework-kdo-mcp-server
  - kdo-infra-health-dashboard
---

# 索引管道升级：让 aliases/tags/discoverable_by 进入检索层

> 审阅对象：王语嫣  
> 日期：2026-07-26  
> 触发：小昭 MCP 搜"坏世界的研究"返回空——aliases 已标但索引层未感知。王语嫣诊断：索引管道落后元数据层三周。

---

## 1. 现状诊断

### 1.1 三周时间线

```
7月初:   tag-registry.yaml 设计完成（27维）
7月初:   discoverable_by 字段加入卡片模板
7月中:   aliases 字段在 agent-native-card-design 中定义
7月19:   Phase 1 自动标签——2,337 张卡有 audience/scene/skill-level
7月26:   自动 aliases——1,616 张卡补了可发现名称
```

### 1.2 索引层盲区

`kdo query` 的检索管道由两层组成：

| 层 | 引擎 | 索引内容 | 最后更新 |
|:--|:--|:--|:--|
| Graph RAG | LightRAG (vector + graph) | chunk 切分后的 body 文本 | 7月4日 |
| BM25 | SearchIndex (TF-IDF) | title + body 全文的 bigram 索引 | 7月26日（tokenizer 修 bug） |

**两层都只索引 title + body，不索引 frontmatter 中的结构化字段。**

| 字段 | 当前覆盖 | 索引层行为 | 差距 |
|:--|:--|:--|:--|
| `aliases` | 1,616 张卡 | BM25 碰巧扫到（读全文件时顺带） | 不是设计行为。aliases 应和 title 同权重，但当前无加权 |
| `tags` | 2,337 张卡 | BM25 扫到了 value 部分（如 "audience:executor"） | 不支持按维度过滤。搜 "audience:ceo" 有结果但无法区分"搜标签"和"搜正文" |
| `discoverable_by` | 26 张卡 | **不索引** | 用户场景关键词——应该是搜索第一入口，但从未进入索引 |

### 1.3 狗粮验证（坏世界研究）

```
kdo query "坏世界 研究"  
  → 修复前: TCPR框架 + 半肥猫工具（三张坏世界卡全丢）
  → 加别名后: 地位互换测试 + 博弈环境清单（搜到了）
  → 但仍缺: concept-collaboration-philosophy-foundation（概念卡未被召回）
  
根因: "坏世界"现在在 aliases 中，BM25 碰巧扫到了。
     但 concept 卡索引权重低（正文是理论性内容，BM25 分数低）。
     aliases 没有被显式加权——BM25 把它当普通正文处理。
```

---

## 2. 改造方案

### 2.1 核心原则

不重写检索架构——在现有 Graph RAG + BM25 + RRF 融合管道中，给结构化元数据**加权注入**。

### 2.2 三层改动

#### 第一层：BM25 索引感知 aliases + tags + discoverable_by

**改动文件**：`KDO/search_index.py` → `SearchIndex.build()` 方法

**当前行为**：读整个 .md 文件 → tokenize → 建倒排索引

**新行为**：
```
读文件 → parse frontmatter → 
  index_text = (
    title × 3 +           # 标题 3x 权重
    aliases × 3 +         # 别名 3x 权重（和 title 同级）
    discoverable_by × 2 + # 可发现场景 2x 权重
    tags × 2 +            # 标签值 2x 权重
    body × 1              # 正文 1x 权重
  )
```

**效果**：搜"坏世界"→ aliases 中有 → 3x 权重 → 排在正文匹配前面。搜"audience:ceo"→ tags 中有 → 2x 权重 → 可作为检索维度。

**工作量**：~30 行代码改动 + 重建索引

#### 第二层：RRF 融合感知 MOC 域的 tags

**改动文件**：`KDO/commands/delivery.py` → `_rrf_fuse()` 函数

**当前行为**：RRF 融合时，MOC boost 只看 `domain-routes.yaml` 的 keyword 匹配

**新行为**：增加 tag 维度匹配
```
if card.tags 包含 "audience:ceo" and query 含 "CEO/战略/决策":
  score += 额外 boost

if card.tags 包含 "scene:execution" and query 含 "怎么做/步骤/操作":
  score += 额外 boost
```

**效果**：小昭搜"坏世界"→ aliases 命中。小昭搜"CEO 该怎么设计分钱规则"→ tags `audience:ceo` + `scene:diagnosis` 双命中 → 地位互换测试卡排第一。

**工作量**：~40 行代码 + domain-routes.yaml 增加 tag_routing 配置段

#### 第三层：MCP Tool 支持标签过滤

**改动文件**：`kdo-tools/mcp/tools.py` → `search()` 函数 + `onboard()` 函数

**当前行为**：`kdo_search` 返回 `{id, title, type, snippet, score, updated_at}`

**新行为**：返回结果加 `tags` 和 `aliases` 字段
```
{
  "id": "tool-position-switching-test",
  "title": "地位互换测试",
  "tags": ["audience:executor", "scene:execution", "skill-level:intermediate"],
  "aliases": ["坏世界研究", "坏世界", "椅子测试"],
  ...
}
```

**效果**：小昭收到结果后不需要逐张 `kdo_read` 就能判断"这张卡能不能用"。

**工作量**：~15 行代码

---

## 3. 编排建议

三个改动是递进关系——第一层是基础（索引感知元数据），第二层是智能（RRF 利用标签），第三层是出口（MCP 暴露标签）。

```
执行顺序: 第一层 → 索引重建 → 验证 → 第二层 → 第三层
```

| # | 内容 | 执行者 | 文件 | 预计工作量 |
|:--|:--|:--|:--|:--|
| 1 | BM25 索引感知 aliases/tags/discoverable_by + 加权 | 黄药师 | `search_index.py` | 0.5d |
| 2 | 重建 BM25 索引 + 验证 | 黄药师 | `kdo index` | 10min |
| 3 | RRF 融合增加 tag 维度匹配 | 黄药师 | `delivery.py` + `domain-routes.yaml` | 0.5d |
| 4 | MCP Tool 返回 tags + aliases | 黄药师 | `kdo-tools/mcp/tools.py` | 0.5d |

**全部由黄药师执行。不需要老顽童、不需要欧阳锋终审——这是基建层的索引管道升级。**

### 验证方式

```
第一层完成 → kdo query "坏世界" → 三张坏世界卡全部出现且 concept 卡不丢
第二层完成 → kdo query "CEO 分钱规则" → framework 卡排第一（tag匹配boost）
第三层完成 → 小昭 kdo_search → 返回结果带 tags + aliases → 无需逐张 kdo_read
```

---

## 4. 为什么现在必须做

不是在修一个 aliases 的 bug——是在修索引管道落后元数据层三周的结构性债务。如果只补 aliases 不修管道，下周 `discoverable_by` 铺开后又会出现"小昭搜不到"。下周 `tags` 的精标维度（method/industry/value-tier）铺开后，索引层还是只扫 title + body——那些标签打了等于没打。

---

*黄药师 · 2026-07-26*
