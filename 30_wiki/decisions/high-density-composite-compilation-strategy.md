---
title: "高密度素材编译策略（修订）"
type: decision
status: revised
version: "2.0"
supersedes: "v1.0（复合编译方案，已废弃）"
domain:
  - kdo
source_refs:
  - "30_wiki/decisions/kdo-ec-industrialization-migration-proposal.md"
created_at: "2026-05-10"
updated_at: "2026-05-11"
tags:
  - "#kdo"
  - "#enrichment"
  - "#methodology"
  - "#agent-native-design"
---

# 高密度素材编译策略 v2.0

> 欧阳锋制定。v1.0 提出的"复合编译"方案已被废弃——该方案按人类线性阅读优化，不适用于 agent 的 RAG 检索模式。v2.0 改用细粒度知识卡 + 导航层架构。

## 关键设计判断

**这个知识库的主要用户是 AI agent，不是人类。**

这意味着设计原则与人类导向的 wiki 完全不同：

| 维度 | 人类读者 | AI Agent |
|------|---------|----------|
| 信息消费 | 线性阅读，需要上下文连贯 | RAG 检索，按需拉取相关片段 |
| 最佳粒度 | 中长篇文章（5000-10000 字） | 单概念卡片（500-2000 字），精确命中 |
| 关联方式 | 目录 + 章节导航 | wiki-link 图遍历 + 向量检索 |
| 风险 | 碎片化导致"看不到全貌" | 大卡导致检索上下文爆炸 |

**结论：细粒度卡片对 agent 是正确的结构选择。黄药师的 127 张独立知识卡在结构上没有错——错的是质量问题。**

## v1.0 的错误

v1.0 方案要求将 ~60 份素材（85 张知识地图 + 12 份口述稿）按 14 个主题聚类合并为 ~14 张复合概念卡。这个方案：

1. **对 agent 有害**：一张卡塞 30 张知识地图 → RAG 检索时整坨拉入，agent 只需要一个概念却被灌进整张卡
2. **wiki-link 网络稀疏**：14 张复合卡之间的链接比 127 张独立卡少一个数量级——agent 靠图遍历发现关联的能力被削弱
3. **维护成本高**：更新一张知识地图需要重新编译整张复合卡

## v2.0 方案：细粒度知识卡 + 导航层

```
知识层（细粒度）          导航层（Hub Pages）
                      
 [[用户视角]] ←────────── [[需求工具箱 Hub]]
 [[用户分层]] ←──────────       │
 [[场景推演]] ←──────────       │ links to all demand cards
 [[动机阻力]] ←──────────       │ + overview summary
                      
 [[内核边界]] ←────────── [[落地工具箱 Hub]]
 [[逻辑MECE]] ←──────────       │
 [[管理三段论]] ←─────────      │ links to all execution cards
```

### 原则

1. **每张知识地图 → 一张独立概念卡**（黄药师已做，结构正确）
2. **每张口述稿 → 一张独立概念卡**（黄药师已做，结构正确）
3. **每张卡必须通过质量门禁**：三步编译 + Visual Analysis + source_refs → 10_raw/
4. **建少量 Hub Page**（导航页）：按工具箱/主题聚类，提供概览和 wiki-link 导航
5. **Agent 的工作流**：RAG 检索命中具体卡片 → 通过 wiki-link 图走到相关卡片 → Hub Page 提供宏观定位

### Hub Page 与复合卡的区别

| 维度 | 复合卡（v1.0，已废弃） | Hub Page（v2.0） |
|------|----------------------|-----------------|
| 内容 | 复制/合并所有子卡内容 | 只含概览 + wiki-link 列表 |
| 大小 | 可能 10K-50K 字 | 控制在 3K 字以内 |
| 用途 | 人类从头读到尾 | Agent 快速定位 + 图遍历入口 |
| 维护 | 子卡更新须同步更新复合卡 | 子卡独立更新，Hub 只更新索引 |

## 执行方案

### 阶段一：质量修复（针对黄药师已产出的 127 张卡）

黄药师的 127 张独立卡片**不删除**。按以下优先级修复：

| 优先级 | 动作 | 涉及卡片 |
|:------:|------|:----:|
| **P0** | `source_refs` 从 `00_inbox/` → `10_raw/sources/`（图片归档 + 路径修正） | 127 张 |
| **P0** | 补 38 张缺 [Critique] 的卡片 | 38 张 |
| **P1** | 补 81 张缺 Visual Analysis 的卡片（五维分析） | 81 张 |
| **P1** | 已有 Critique 但质量低的（万能废话式）重写 | 抽查确定 |

### 阶段二：建导航层

当前 127 张卡分散在命名空间下，需要有 Hub Page 串联：

| # | Hub Page | 链接的卡片群 | 现有材料 |
|---|---------|------------|---------|
| 1 | [[泛产品设计方法论 Hub]] | 三大工具箱 + 36计 + 三大修养 + 爬山地图 | 口述稿 5 份 |
| 2 | [[需求工具箱 Hub]] | 13 张需求卡片 | 已有 [[yt-model-pan-product-demand-toolkit]] |
| 3 | [[审美工具箱 Hub]] | 4 张审美卡片 | 已有 [[yt-model-pan-product-aesthetic-toolkit]] |
| 4 | [[落地工具箱 Hub]] | 19 张落地卡片 | 已有 [[yt-model-pan-product-execution-toolkit]] |
| 5 | [[一堂五步法 Hub]] | 画布卡 + 产品内核卡 + 指标卡 | 口述稿 |
| 6 | [[SPIN销售法 Hub]] | SPIN 口述稿 | 已有 [[yt-entrepreneur-spin-selling]] |
| 7 | [[Y模型实操 Hub]] | Y模型卡片 + 2 份口述 | 已有 |
| 8 | [[科学学习IPO Hub]] | IPO模型卡 + 口述 | 已有 |
| 9 | [[调研方法论 Hub]] | 调研口述 + 课程清单 | 已有 |
| 10 | [[知识萃取方法论 Hub]] | 口述稿 | 已有 |
| 11 | [[思维模型提炼 Hub]] | 口述稿 | 已有 |
| 12 | [[个人成长地图 Hub]] | 个人地图 + 五步法 + 进步大地图 | 已有 |
| 13 | [[转化率优化 Hub]] | 转化率触点 + 动力曲线 | 已有 |
| 14 | [[婚礼项目管理 Hub]] | 婚礼规划卡 | 已有 |

### Hub Page 模板

```markdown
---
title: "XXX Hub"
type: hub
status: enriched
domain: ["yitang"]
source_refs: ["10_raw/sources/xxx.md", ...]
---

# XXX Hub

## 概览
3-5 句话说明这个工具箱/方法论是什么，解决什么问题。

## 核心概念
- [[概念卡 A]] — 一句话定位
- [[概念卡 B]] — 一句话定位
- ...

## 与一堂知识体系的关联
- 属于 [[yt-model-pan-product-36-strategies|36计]] 的 X 场景层
- 对练的是 [[yt-model-pan-product-three-virtues|三大修养]] 中的 Y

## Critique
至少 1 条针对该工具箱整体的质疑。

## Synthesis
与本工具箱以外的概念关联。
```

### 阶段三：验证

每张 Hub Page 产出后：
- `kdo lint --wiki-path <path>` 0 warning
- 所有子卡 quality gate 通过后再标记 Hub 为 enriched

## 执行规范（更新）

1. **细粒度优先**：每张知识地图一张卡，不合并。Hub Page 只做导航不做内容搬运
2. **质量必须过门禁**：三步编译（Condense + Critique + Synthesis）+ Visual Analysis + source_refs 归档
3. **Visual Analysis 必须**：每张知识地图原图打开分析，五维（层级/分组/路径/强调/留白）至少覆盖三维
4. **源文件归档**：引用图片从 `00_inbox/` → `10_raw/sources/`，source_refs 指向源文件
5. **Hub Page 轻量化**：< 3000 字，只含概览 + 导航，不复制子卡内容
6. **单会话 ≤5 张质量修复**，或 ≤2 张 Hub Page（防 context overload）

### 禁止事项

- ❌ 不要将多张知识地图合并为一张复合大卡
- ❌ 不要只依赖 OCR 文字——必须打开原图分析视觉结构
- ❌ source_refs 不要指向 `00_inbox/`
- ❌ 不要跳过 Critique 或 Visual Analysis
- ❌ Hub Page 不要复制子卡完整内容——只写概览 + 链接

## 验收标准

| 标准 | 阈值 |
|------|:--:|
| 每张知识卡 | Condense ≥3 条 / Critique ≥1 条（指名假设或边界） / Synthesis ≥2 个 wikilink / Visual Analysis 覆盖 ≥3 个维度 |
| source_refs | 全部指向 `10_raw/sources/` |
| 全文字数 | >500 字 |
| Hub Page | <3000 字，wili-link 密度 ≥5 个 |
| `kdo lint` | 0 warning |

---

> v1.0 审批人：欧阳锋 | v2.0 修订：欧阳锋 | 执行人：黄药师 | 状态：待执行
