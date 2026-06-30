---
id: kdo-scalability-roadmap-10k-cards
title: "KDO 10,000 张卡扩展性路线图"
type: roadmap
status: draft
author: 王语嫣
created_at: 2026-06-29
updated_at: 2026-06-29
domain:
  - kdo
  - infrastructure
  - scalability
source_refs:
  - kdo-source-code-local-audit-2026-06-29
  - web-research-obsidian-10k-notes
  - web-research-lightrag-production-backends
  - web-research-pkm-at-scale-dsebastien
  - web-research-moc-map-of-content-practice
related:
  - [[kdo-system-manual]]
  - [[kdo-industrialization-manual]]
  - [[incident-impact-assessment-hermes-wiki-2026-06-29]]
  - [[plan-kdo-infrastructure-disaster-prevention]]
---

# KDO 10,000 张卡扩展性路线图

> **研究范围**：先对 KDO 源码与本地 wiki 做了实测，再针对 Obsidian 大库、PKM 规模化、LightRAG 生产部署、MOC 组织法做了全网交叉验证。
>
> **核心结论**：KDO 能“装下”10,000 张卡，但按当前架构会慢到影响日常使用；必须在 5,000 张卡之前完成三项改造——**MOC 分层组织**、**工具链缓存/增量化**、**Graph RAG 后端生产化**。

---

## 一、本地实测基线（当前 2,189 张卡）

| 指标 | 当前值 | 类型 | 10k 外推 | 外推假设 |
|:---|---:|:---|---:|:---|
| `30_wiki/*.md` 数量 | 2,189 | 实测 | 10,000 | 线性 |
| `kdo lint --summary` | **1m17s** | **实测** | ~6–10 min | 线性；若 O(n²) 相似度未关，可能 20min+ |
| `.kdo/search_index.json` | 2.8 MB | 实测 | ~13 MB | 线性 |
| `.kdo/graph_index/` | 72 MB | 实测 | ~330 MB | 线性 |
| `.kdo/state.json` | 1.8 MB | 实测 | ~8 MB | 线性 |
| `.kdo/baseline.json` | 12.5 MB | 实测 | ~57 MB | 线性 |
| 全库 `.md` 文件 | 8,551 | 实测 | ~40,000 | 线性 |

> **重要区分**：`1m17s` 是当前实测；`6–10min` 是线性外推估算，不是承诺。实际 10k 卡 lint 时间强烈取决于 Phase 1 改造是否完成（单次扫描、关闭相似度、baseline）。
>
> 实测环境：Windows + Git Bash，`kdo` 安装在系统 Python，wiki 在 `C:/Users/Administrator/Desktop/wiki`。

---

## 二、全网调研的关键发现

### 2.1 Obsidian / PKM 大库共识

- **10k 笔记对 Obsidian 本身可行**，但需要优化：关闭冗余插件、预建 search index、用 tag/文件夹限缩搜索范围。
- **大库三大性能杀手**：全量扫描型插件、过度链接导致图视图卡顿、未归档冷数据拖慢索引。
- **规模化组织公式**（多源交叉验证）：
  ```
  Tags > Links > Hierarchy
  原子笔记 + MOC 导航 + 自动化归档
  ```

### 2.2 MOC（Map of Content）不是“目录页”，是缩放阀

MOC 在 PKM 社区被反复验证为**唯一能在 1k→10k 阶段不崩盘**的组织层：

- **功能**：每个 MOC 是一个主题的入口页，手工列出相关笔记的 wikilink。
- **价值**：把“全图遍历”变成“MOC → 子主题 → 卡片”的局部遍历，降低 Graph RAG 的检索半径。
- **关键阈值**：1,000 张卡左右就要开始建 MOC；到 5,000 张卡时，没有 MOC 的纯标签/纯 backlinks 系统会显著失效。
- **最佳实践**：MOC 本身也是卡片，有 frontmatter，可以被检索、被链接、被审核。

> KDO 已有 `30_wiki/index.md` 和 `30_wiki/links/index.md`，但它们是**自动生成的全库索引**，不是主题级 MOC。需要为每个核心 domain 建立人工/半自动 MOC。

### 2.3 LightRAG 文件后端 ≠ 生产环境

- LightRAG 官方文档明确：默认的 `JsonKVStorage` + `NanoVectorDBStorage` + `NetworkXStorage` **仅用于开发调试**，不适合生产。
- 生产级后端选项：
  - 一站式：`PostgreSQL`、`MongoDB`、`OpenSearch`
  - 专业向量库：`Milvus`、`Qdrant`、`Faiss`
  - 专业图库：`Neo4j`、`Memgraph`
- LightRAG 2025.10 已声明“Eliminated processing bottlenecks to support Large-Scale Datasets Efficiently”，但前提是使用生产后端并配置并发参数。

### 2.4 归档冷数据是被低估的杠杆

- PKM 规模化案例（8,000 笔记 / 64,000 链接）的核心经验：**Manual organization breaks down past 1,000 notes**；必须引入自动化归档。
- 冷热分离能把活跃工作集控制在 2,000–3,000 张卡，让 10k 总库在体验上仍然“像 3k 库”。

---

## 三、KDO 当前架构的瓶颈定位

### 3.1  confirmed 瓶颈（本地代码 + 实测）

| 组件 | 瓶颈 | 复杂度 | 10k 影响 |
|:---|:---|:---|:---|
| `kdo lint` | ~20 轮独立 `rglob`；O(n²) 跨卡相似度 | 最致命 | 单次 6–10 min+ |
| `kdo index` | 全量重建 search_index.json，无增量 | 高 | 每次 5–15 min |
| `kdo graph rebuild` | LightRAG 默认文件后端 | 高 | 30–60 min，300MB+ index |
| `kdo enrich --all` | O(wiki × sources) 线性查找 | 中高 | 小时级 |
| pre-submit / freeze | 对每个 link 重新 `rglob` | 中 | 单卡提交变慢 |
| Obsidian Graph | 全节点渲染 + 密集连接 | 中 | 图视图卡顿 |

### 3.2 当前不是瓶颈、但会被误伤的

- **Git**：10k 文件对 Git 完全不是问题。
- **NTFS / 文件系统**：10k markdown 文件很小。
- **Obsidian 打开/搜索**：只要插件克制、索引预建， Obsidian 本身能撑住 10k。

---

## 四、10k 卡能不能撑？分场景回答

| 场景 | 当前架构下 | 完成本路线图后 | 关键假设 |
|:---|:---|:---|:---|
| 单纯存储 10k 卡 | ✅ 可以 | ✅ 可以 | Git + 文件系统无压力 |
| 日常 `kdo lint` | ⚠️ 6–10 min（线性外推） | ✅ <30s（baseline + 增量） | 完成 Phase 1 改造 |
| `kdo index` | ⚠️ 5–15 min（估算） | ✅ 增量 <1 min | 实现增量 index |
| `kdo graph query` | ⚠️ 延迟上升 | ✅ <1s | 完成增量 rebuild；换后端是后半段选项 |
| `kdo graph rebuild` | ❌ 30–60 min（全量估算） | ✅ 增量 <5 min | 只重新嵌入新增/修改/删除卡 |
| `kdo enrich --all` | ❌ 小时级（估算） | ✅ SQLite 状态 + 增量 | state.json → SQLite |
| 多 Agent 并发调用 kdo | ❌ 文件写入冲突风险 | ✅ 状态库 + 锁机制 | SQLite WAL + busy timeout + 文件锁 |

---

## 五、改造路线图

### Phase 0：组织层——MOC + 冷热分离（现在就能做，零代码）

**目标**：把“全图遍历”降级为“MOC 局部遍历”，把活跃卡数控制在 3k 以内。

1. **为核心 domain 建立 MOC 卡片**
   - 每个 MOC 放在 `30_wiki/moc/` 或对应 domain 根目录。
   - MOC 内容：domain 定义 + 子主题列表 + 精选卡片 wikilink + 边界说明。
   - 示例：`moc-strategy.md`、`moc-yitang.md`、`moc-ai-collaboration.md`。

2. **把自动生成索引降级为“导航辅助”**
   - `30_wiki/index.md` 不再承担核心检索职责，只作为目录页。
   - 检索入口交给 MOC + Graph RAG + search index。

3. **建立 Archive 机制（先软归档，后硬归档）**
   - **Phase 0 采用软归档**：把卡片 `status` 改为 `archived` 或 `superseded`，**留在原目录不动**。
   - 软归档触发条件：
     - 卡片 status 明确为 `archived` 或 `superseded`
     - 超过 12 个月未被任何 link 引用
     - 内容被新卡完全覆盖
   - 软归档后从 `kdo lint` 默认范围排除，但保留在 Graph RAG 历史查询中。
   - **暂不物理移动到 `30_wiki/_archive/`**：避免破坏现有 wikilink，降低 link 维护成本。等软归档规则跑稳定后，再评估是否需要物理移动。
   - 当前 `30_wiki/_archive/` 里已有的 26 张卡保持现状，新归档卡先不改物理位置。

4. **标签瘦身**
   - 从“描述内容”转向“标记状态”：`#review-needed`、`#archived`、`#high-priority`。
   - 内容分类交给 frontmatter `domain` 和 MOC。

### Phase 1：工具链快赢（1–2 周，5k 卡前必须完成）

**目标**：把日常 lint/index 从分钟级降到秒级/十秒级。

1. **lint 单次扫描 + 内容 hash 缓存**
   - 合并 20 轮 `rglob` 为一次统一 walker。
   - 缓存解析后的 frontmatter 和 body hash，只重新处理修改过的文件。

2. **跨卡相似度检查改为“夜间任务”**
   - 默认 lint 关闭 O(n²) `SequenceMatcher`。
   - 改为 `kdo lint --deep` 或 nightly CI 任务。

3. **pre-submit / freeze verify 用内存索引**
   - 启动时加载 `id → path` 映射，不要对每个 link `rglob`。

4. **`kdo lint --domain` 真正限定扫描范围**
   - 现在 `--domain` 是后过滤；改为只扫描对应目录。

5. **lint baseline 分层**
   - 历史 WARNING 接受为 baseline，lint 只检查新增问题。
   - 目标：`kdo lint --summary` 在 baseline 模式下 <10s。

### Phase 2：状态与索引数据库化（1–2 个月）

**目标**：解决 O(n²) 查找和 JSON 全量读写。

1. **`state.json` → SQLite**
   - sources、tasks、projects、artifacts 等表迁移到 SQLite。
   - enrich 时的 source 查找从线性扫描变成 `SELECT`。

2. **Search Index 增量更新**
   - 根据 `mtime` 只更新变化文档，避免每次全量重建。
   - 可考虑 `whoosh`、`sqlite-fts5` 或本地向量库。

3. **增量 Graph RAG（优先）**
   - 默认增量 rebuild；只有新增/修改/删除的卡片触发 chunk 重新嵌入。
   - 当前 2,189 卡、72MB index，文件后端的最大痛点是**全量 rebuild 时间**，不是查询延迟。
   - 先实现增量 rebuild，如果查询延迟仍高，再考虑后端替换。

4. **Graph RAG 生产后端（延后评估）**
   - 当前不急着换；等增量 rebuild 完成后，根据 benchmark 决定。
   - 候选方案：
     - 最小可行方案：SQLite + Qdrant（Docker）+ Neo4j（Docker）
     - 更轻量方案：PostgreSQL + pgvector + AGE（图扩展）
   - 引入 Docker 依赖会显著增加部署复杂度，单机本地优先场景下 ROI 需重新计算。

### Phase 3：并行化与生产级（3–6 个月）

**目标**：支撑 10k+ 卡和并发 Agent。

1. **并行 lint / index / graph build**
   - 多进程处理不同 domain；IO 与 CPU 任务分离。

2. **引入专用向量数据库**
   - 10k+ 卡长期建议 `Qdrant` 或 `Weaviate`。

3. **状态变更队列 + 锁机制**
   - 多 Agent 同时写 `state.json` 时容易 corrupt；需要 SQLite WAL 或变更队列。

4. **性能回归测试**
   - 增加 benchmark：`time kdo lint/index/graph-rebuild` 在模拟 5k/10k 卡数据集上。

---

## 六、MOC 与现有 KDO 体系的融合

KDO 已有“四卡体系”（concept / skill / case / dk）。MOC 可以作为第五种卡片类型或索引卡变体：

| 层级 | 角色 | 示例 |
|:---|:---|:---|
| Domain MOC | 一个知识域的入口 | `moc-strategy.md` |
| Method MOC | 一套方法的索引 | `moc-yitang-methodology.md` |
| Project MOC | 一个交付项目的知识枢纽 | `moc-goat-milk-channel.md` |
| Anti-MOC | “不要从这里进入”的边界说明 | `moc-deprecated-concepts.md` |

**MOC 验收标准**：
- 包含本主题 30–50 张核心卡片的 wikilink
- 说明本 MOC 的边界（包含什么、不包含什么、相邻 MOC 是什么）
- 自身也是一张可检索的 concept/framework 卡

---

## 七、监控指标

| 指标 | 当前 | 5k 卡目标 | 10k 卡目标 |
|:---|---:|---:|---:|
| `kdo lint --summary` | 77s | <30s | <60s |
| `kdo index` | 全量重建 | <1min 增量 | <2min 增量 |
| `kdo graph query` | 未测 | <2s | <2s |
| Obsidian graph 打开 | 可接受 | <3s | <5s |
| 活跃卡占比 | 100% | <70% | <50% |
| frontmatter 错误率 | 4.2% | <1% | <0.5% |

---

## 八、最小可行启动（本周可做）

如果只做 3 件事：

1. **选一个核心 domain 做 MOC 试点**（如 `strategy` 或 `yitang`），验证 MOC 是否能减少 Graph RAG 查询半径。
2. **把 `kdo lint` 的跨卡相似度检查改为默认关闭**，作为 `--deep` 选项。
3. **在 `.kdo/` 下加一个 `archive/` 目录规划**，先把 20–30 张长期未引用的卡标记为 `status: archived`。

---

## 九、风险与反例

- **风险 1：过早数据库化**。如果卡片还没过 3k 就引入复杂数据库，运维成本会超过收益。Phase 0 和 Phase 1 的零代码/小代码改造足以撑到 5k。
- **风险 2：MOC 成为新瓶颈**。如果 MOC 本身太大（>3000 字）或链接过多，会变成“大卡”，反而拖慢检索。MOC 也要遵守 500–2000 字原则。
- **风险 3：归档后查不到**。归档卡片必须从 Graph RAG 历史索引中保留，只是从日常 lint/index 默认范围排除。

---

## 十、决策框架

| 问题 | 判断 |
|:---|:---|
| 现在就要上数据库吗？ | 不需要。Phase 0 + Phase 1 先做完，到 5k 卡再评估。 |
| 现在就要换 LightRAG 后端吗？ | 不需要。先做增量 rebuild；查询延迟仍高再评估后端替换。 |
| MOC 是必选项吗？ | 是。没有 MOC，10k 卡的图网络会不可导航。 |
| 需要分布式/多机吗？ | 10k 卡不需要；单机 + SSD + 16GB 内存足够。 |

---

## 十一、欧阳锋评审意见（2026-06-29）

**总体评定**：
- `plan-state-json-to-sqlite-migration.md`：**A-，采纳，从 MVP 开始**
- `kdo-scalability-roadmap-10k-cards.md`：**B+，方向正确，但需补充细节**

### 完全同意的点

1. 不改 272 处调用，只改 `load_state()` / `save_state()` 抽象层。
2. 统一表 + JSON 列，而不是 15 张独立表。
3. MVP 只做 `sources` 集合。
4. 不做双写过渡期。
5. Phase 0（MOC + 归档）先于 Phase 2（数据库化）。

### 补充与纠正

1. **文档内部矛盾**：migration plan 的 MVP 小节原写“双写一周”，与 5.3 节冲突，已修正为“单写 + 备份 + 回退”。
2. **多进程并发**：KDO 真实场景是多进程（老顽童 CLI / 黄药师 lint / 王语嫣 dashboard），需 `busy_timeout=5000` + 进程级文件锁。
3. **`save_state` 语义改变**：批量 append 模式在 SQLite 下会立即落库，需提供显式 `state.transaction()` 上下文。
4. **归档机制**：先采用“`status: archived` + 留在原目录 + lint 排除 archived”，避免破坏 wikilink。
5. **性能数字**：实测与外推需明确区分，`1m17s` 是实测，`6–10min` 是假设线性外推。
6. **Graph RAG 后端**：当前 72MB index、2,189 卡，文件后端查询延迟不是瓶颈；**增量 rebuild 优先级高于换后端**。

### 明确不做

- ❌ 双写过渡期
- ❌ `check_same_thread=False` 无保护方案
- ❌ 现在就换 Graph RAG 后端

---

**关联文档**：
- [[kdo-system-manual]]
- [[kdo-industrialization-manual]]
- [[plan-kdo-infrastructure-disaster-prevention]]
- [[incident-impact-assessment-hermes-wiki-2026-06-29]]
