---
title: "Graph RAG 检索层技术说明"
author: "审查者欧阳锋"
role: "知识架构师 (Knowledge Architect)"
created_at: "2026-05-04"
status: proposed
target_implementer: "黄药师 (Builder)"
dependency: "30_wiki/.graph/index.json（由 build_graph_index.py 生成）"
---

# Graph RAG 检索层技术说明

> 写给黄药师：本文件定义检索层的输入输出格式、与现有组件的接线方式、以及在 KDO 流水线里的触发时机。实现细节由你决定。

---

## 零、整体架构

```
build_graph_index.py          ← 已有，遍历 30_wiki/ 建图
        │
        ▼
   index.json (30_wiki/.graph/)   ← 已有，静态节点+边
        │
        ▼
【待实现】 query_graph.py          ← 本文件定义
        │
        ├── Step 1: 关键词匹配节点
        ├── Step 2: 边遍历扩召回（1-2 hop）
        └── Step 3: 格式化为 LLM 可消费的上下文
        │
        ▼
     调用方（Agent / CLI / kdo 命令）
```

---

## 一、输入

### 1.1 调用方

任何需要查询知识库的 Agent 或脚本。

### 1.2 查询格式

```python
# 函数签名
def query_graph(
    query: str,       # 自然语言查询，如 "OSCAR 调研法"
    n_hops: int = 2,  # 扩展跳数，默认 2
    top_k: int = 5    # 返回节点数上限
) -> dict
```

```python
# CLI 调用
python query_graph.py "OSCAR 调研法怎么用" --hops 2 --top-k 5
python query_graph.py "YC 组织方法论" --format json
```

---

## 二、处理逻辑

### Step 1 — 关键词匹配

将 `query` 与 `index.json` 中每个节点的以下字段做子串匹配（大小写不敏感）：

| 匹配字段 | 来源 | 权重 |
|---------|------|:---:|
| `node.label` | 页面标题 | 最高 |
| `node.id` | 页面 ID，通常含中文关键词 | 中 |
| `node.frontmatter.tags` | #tag 标签 | 中 |
| `node.frontmatter.title` | frontmatter 标题 | 低（容易重复） |

匹配到 ≥1 个关键词的节点进入候选集。按命中次数排相关性。

### Step 2 — 边遍历扩召回

从 Step 1 的命中节点出发，沿 `index.json` 中的 edges 走 1-2 跳：

```
命中节点 A
  ├── edge → 节点 B（未在候选中）→ 加入结果，标记 "关联"
  └── edge → 节点 C
        └── edge → 节点 D → 加入结果，标记 "二阶关联"
```

返回结果按层级分组：`hits`（直接命中）、`neighbors`（1 跳）、`extended`（2 跳）。

### Step 3 — 格式化输出

```json
{
  "query": "OSCAR 调研法",
  "node_count_before": 28,
  "node_count_after": 0,
  "results": [
    {
      "node_id": "一堂调研行动营-ai辅助系统式调研方法论",
      "label": "一堂调研行动营-ai辅助系统式调研方法论",
      "path": "30_wiki/concepts/一堂调研行动营-ai辅助系统式调研方法论.md",
      "type": "concept",
      "domain": "master",
      "relevance": "hit",
      "hop": 0,
      "score": 3.0,
      "matched_on": ["label", "title", "tags"]
    },
    {
      "node_id": "kimi-深度调研集群方法论-deep-research-swarm",
      "label": "Kimi 深度调研集群方法论 (Deep-Research-Swarm)",
      "path": "30_wiki/concepts/kimi-深度调研集群方法论-deep-research-swarm.md",
      "type": "concept",
      "domain": "ai-saas",
      "relevance": "neighbor",
      "hop": 1,
      "score": 1.0,
      "matched_on": ["edge_from_hit"]
    }
  ]
}
```

附加一个纯文本格式供 Agent 直接消费：

```markdown
【核心命中】 一堂调研行动营-ai辅助系统式调研方法论
  路径: 30_wiki/concepts/一堂调研行动营-ai辅助系统式调研方法论.md
  类型: concept | 领域: master
  匹配原因: 标题命中关键词"调研"

【关联概念】 Kimi 深度调研集群方法论 (Deep-Research-Swarm)
  路径: 30_wiki/concepts/kimi-深度调研集群方法论-deep-research-swarm.md
  类型: concept | 领域: ai-saas
  关系: 一堂调研方法论 → Kimi 集群搜索（edge: related）

【二阶关联】 KDO Protocol
  路径: 30_wiki/systems/kdo-protocol.md
  类型: system
  关系: Kimi 集群搜索 → KDO Protocol（edge: links-to）
```

---

## 三、与现有组件接线

### 3.1 依赖 `build_graph_index.py` 产出

`query_graph.py` 只读 `index.json`，不重建索引。索引由 `build_graph_index.py` 生成和更新。

### 3.2 集成到 `kdo watch` 流水线

```
kdo watch 检测到新文件
  → ingest
  → enrich
  → build_graph_index.py   ← 重建索引
  → （未来：query_graph 可被 Agent 调用）
```

### 3.3 暴露为 CLI 命令（建议）

```
kdo graph --query "OSCAR 调研法"              → 纯文本输出
kdo graph --query "OSCAR 调研法" --json        → JSON 输出
kdo graph --rebuild                            → 手动重建索引
```

---

## 四、实现约束

| 约束 | 说明 |
|------|------|
| 零外部依赖 | 纯 Python 标准库（json, pathlib, re） |
| 不要向量化 | 当前阶段 keyword 匹配足够，不加 embedding |
| 文件路径用 vault 根路径 | `30_wiki/concepts/xxx.md`，不是绝对路径 |
| 不修改 `index.json` | 只读不改；重建由 `build_graph_index.py` 负责 |
| 错误静默降级 | `index.json` 不存在时返回空结果而非崩溃 |

---

## 五、验收标准

完成后验证以下场景：

1. **基础查询**: `"OSCAR 调研法"` → 返回一堂调研方法论
2. **扩展查询**: `"医疗 HIS"` → 返回鑫港湾、轻量级诊所HIS、开源HIS
3. **跨域关联**: `"AI 组织方法论"` → 返回 YC 方法论 + Kimi 集群
4. **无结果**: `"区块链"` → 返回空结果，不崩溃
5. **JSON 不存在**: 返回空结果，带错误说明

---

## 六、未来升级方向

以下**不做在 MVP**，仅供参考：

- 将 concept 正文内容（Condense 摘要）加入匹配
- 按 `domain` 字段过滤
- 返回结果附带简短的 edge 关系说明（如"因为 [[一堂]] 对标了 [[Kimi]]"）
- 向量化检索（含 embedding API）——当节点超过 200 时再考虑

---

*技术说明完成时间：2026-05-04*
*审查者欧阳锋*
