---
title: "Graph RAG 检索层技术说明"
author: "审查者欧阳锋"
role: "知识架构师 (Knowledge Architect)"
created_at: "2026-05-04"
updated_at: "2026-05-04"
status: stable
implementor: "黄药师 (Builder)"
dependencies:
  - "LightRAG 库（pip install lightrag）"
  - ".kdo/graph_index/（LightRAG 产出物）"
superseded_design: "v0.1 keyword-based — 原计划基于 index.json 的纯标准库方案，因黄药师已完成 LightRAG MVP 且检索质量更优，该方案已废弃"
---

# Graph RAG 检索层技术说明

> **实际实现：LightRAG（图 + 向量混合检索）**
> 黄药师于 2026-05-04 完成 MVP，全链路跑通，零 LLM 调用。
> 本文件为后续 Agent 调用的接口规范。

---

## 零、整体架构（实际）

```
30_wiki/concepts/（全部概念卡）
        │
        ▼
   LightRAG（分块 + 实体提取 + 向量建库 + 图关系）
        │
        ▼
   .kdo/graph_index/   ← 检索层的持久化数据库
   ├── kv_store_text_chunks.json （199KB）
   ├── vdb_chunks.json            （364KB，向量检索）
   ├── vdb_entities.json          （81KB，实体检索）
   ├── vdb_relationships.json     （48B，图关系）
   └── graph_chunk_entity_relation.graphml （11KB）
        │
        ▼
   LightRAG 查询接口  ← 混合检索（图遍历 + 向量匹配）
        │
        ▼
【待实现】 CLI 统一入口 → kdo graph --query "xxx"
        │
        ▼
     调用方（Agent / Bot / 脚本）
```

---

## 一、已完成 vs 待完成

| 状态 | 事项 |
|:----:|------|
| ✅ | LightRAG 分块：所有 wiki 概念卡已完成 chunk |
| ✅ | 向量建库：chunks + entities 向量已就绪 |
| ✅ | 图关系建库：实体间关系已自动提取 |
| ✅ | 混合检索：graph + vector 协同查询 |
| ✅ | 零 LLM 调用：预填 keywords 绕过 LLM 关键词提取 |
| ⏳ | CLI 统一入口：`kdo graph --query "xxx"` 未实现 |
| ⏳ | Agent 调用格式：输出需标准化为 Agent 可直接消费的格式 |

---

## 二、CLI 接口规范（黄药师下一步实现）

### 命令形式

```
kdo graph --query "<自然语言查询>"        → 纯文本输出（Agent 消费）
kdo graph --query "<查询>" --json          → JSON 输出（脚本消费）
kdo graph --rebuild                        → 手动重建 LightRAG 索引
```

### 输出格式

#### 纯文本（Agent 直接读）

```markdown
【Graph RAG 检索结果】查询: "OSCAR 调研法"

┌─ 核心命中（3 chunks）
├─ 一堂调研行动营-ai辅助系统式调研方法论
│   片段: "OSCAR五步法：O（目标界定）→ S（扫描）→ C（比较）→ A（行动）→ R（复盘）..."
│   路径: 30_wiki/concepts/一堂调研行动营-ai辅助系统式调研方法论.md
│   领域: master | 状态: enriched
│
├─ 一堂-调研行动营启动_原文润色
│   片段: "..."
│   路径: 30_wiki/concepts/一堂-调研行动营启动_原文润色.md
│
└─ 一堂调研武器库13招
   片段: "..."
   路径: 30_wiki/concepts/一堂调研武器库13招.md

┌─ 相关实体（10）
├─ KDO Protocol | 30_wiki/systems/kdo-protocol.md
├─ Wiki Index | 30_wiki/index.md
├─ Kimi 深度调研集群方法论 | 30_wiki/concepts/kimi-深度调研集群方法论-deep-research-swarm.md
└─ ...（共 10 个）
```

#### JSON（脚本消费）

```json
{
  "query": "OSCAR 调研法",
  "chunks": [
    {
      "content": "...",
      "file_path": "30_wiki/concepts/一堂调研行动营-ai辅助系统式调研方法论.md",
      "concept_title": "一堂调研行动营-ai辅助系统式调研方法论",
      "domain": "master",
      "relevance_score": 0.95
    }
  ],
  "entities": [
    {
      "name": "KDO Protocol",
      "file_path": "30_wiki/systems/kdo-protocol.md",
      "entity_type": "concept"
    }
  ],
  "relationships": [
    {
      "from": "一堂调研行动营",
      "to": "Kimi 深度调研集群",
      "relation_type": "related"
    }
  ]
}
```

---

## 三、与 KDO 流水线的集成

```
kdo watch 检测到新文件
  → ingest
  → enrich（Agent 三步编译）
  → kdo graph --rebuild   ← 重建 LightRAG 索引（新增这一环）
  → Agent 可通过 kdo graph --query 检索
```

**触发时机：** 每次 enrich 完成后自动 rebuild。或者由 `kdo watch` 定期巡检触发。

---

## 四、Agent 调用约定

任何 Agent 需要查询知识库时，调用方式：

```
kdo graph --query "<问题>" 
```

输出即为纯文本上下文，Agent 可直接嵌入对话引用。

**Agent 不需要知道下面用了 LightRAG 还是 keyword。** 接口是 `kdo graph --query`，底层替换不影响调用。

---

## 五、已知限制

| 限制 | 原因 | 影响 |
|------|------|------|
| relations=0（部分查询） | wiki 中部分 wikilink 指向的页面不存在 | 图遍历跳数不足，召回偏低 |
| 索引需手动重建 | 未接入 kdo watch 自动触发 | 新 enrich 的页面不会被自动检索 |
| LightRAG 外部依赖 | 非标准库 | 需 pip install，环境迁移多一步 |

---

## 六、与原 keyword 方案的取舍

| 维度 | 原 keyword 方案 | 实际 LightRAG 方案 | 取舍理由 |
|------|:---:|:---:|------|
| 依赖 | 纯标准库 | LightRAG 库 | 检索质量 > 零依赖原则 |
| 匹配方式 | 子串匹配 | 向量语义匹配 | "调研方法" 能命中 "OSCAR 五步法" |
| 图关系 | 人工维护 wikilink | 自动提取实体关系 | 覆盖率更高，但准确性需校验 |
| LLM 调用 | 无 | 无 | 一致 |
| 维护成本 | 低（无外部依赖） | 中（LightRAG 版本升级） | 可接受 |

**结论：** 黄药师的 LightRAG 实现优于原 keyword 方案。原方案及 `build_graph_index.py` → `index.json` 链路标记为废弃。新检索层以 LightRAG 为唯一引擎。

---

*技术说明完成时间：2026-05-04（v1.0），更新于 2026-05-04（v1.1 对齐实际实现）*
*审查者欧阳锋*
