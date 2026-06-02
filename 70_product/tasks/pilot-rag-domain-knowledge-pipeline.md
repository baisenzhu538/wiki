---
title: "Pilot：用 KDO 管线精通 RAG 系统架构 — 验证 AI 快速掌握知识可行性"
assigned_to: "黄药师（Builder）"
priority: "P2"
created_at: "2026-06-02"
reviewer: "欧阳锋（Architect）"
status: "pending"
depends_on:
  - "Sprint 6 断裂点 1（enrich+label 串联）"
  - "Sprint 6 断裂点 2（ingest --assess）"
blocks: ["proposal-ai-domain-mastery-pipeline Phase 2 决策"]
risk_level: "中——验证管线为主，产出质量为辅"
origin: "proposal-ai-domain-mastery-pipeline — KDO 自反 Pilot"
---

# Pilot：用 KDO 管线精通 RAG 系统架构

> **目标**：验证 AI 自动精通领域知识管线的可行性。选 KDO 自身领域（RAG 系统架构）做 Pilot，因为验证成本最低、素材已在库中、且产出可被 KDO 自身检索验证。
>
> **不要求**：产出完美的 RAG 知识库。要求：管线能跑通、不产垃圾、收敛条件可验证。

---

## 素材

不需要外部搜索。KDO 工作空间已有：

| 来源 | 位置 | 说明 |
|:-----|:-----|:------|
| Graph RAG 实现 | `kdo/commands/graph.py` + `kdo/search_index.py` | 管线本身代码 |
| 架构决策 | `30_wiki/concepts/graph-rag.md` | 已有概念卡 |
| 标注方案 | `30_wiki/decisions/labeling-final-consolidation.md` | 标签体系设计 |
| 知识卡片 | `30_wiki/concepts/` 中与 RAG 相关的卡片 | 如 `yt-unit-model-ai-assisted` |
| KDO CLI 源码 | `kdo/` 全部 .py 文件 | 管线实现 |

---

## 步骤

### Phase 1：建骨架 — 三步编译

用已有素材自动产出 RAG 领域的概念卡骨架：

```bash
# 搜集 RAG 相关源文件
grep -ril "rag\|GraphRAG\|embedding\|检索\|向量" 10_raw/sources/ > rag-sources.txt

# 批量 ingest（如果尚未 ingest）
cat rag-sources.txt | while read f; do kdo ingest --path "$f"; done

# 批量三步编译（用 LLM，每篇产出概念卡）
# 注意：enrich 只做粗加工，精加工靠 label
kdo enrich --wiki-path 30_wiki/concepts/graph-rag.md --llm
```

**产出检查**：
- 概念卡覆盖的 RAG 子主题 ≥ 5 个（检索/索引/分块/排序/GraphRAG）
- 每张卡有 `source_refs` + `trust_level`
- `kdo lint` 无新增错误

### Phase 2：补缺口 — 图遍历识别盲区

```bash
# 分析当前 RAG 知识图谱覆盖
kdo graph query "RAG 系统的核心组件"

# 检查缺少哪些子主题
# 例如：分块策略、embedding 模型选型、混合检索、reranking
```

如果发现缺口（如"KDO 的卡片没有一张覆盖分块策略"），从现有素材中补上。

**收敛条件**：连续两轮新增卡片的 source_refs ≥ 80% 指向已有卡片已覆盖的源。

### Phase 3：注深度 — 四步编译

对 RAG 领域的核心争议/边界问题，产出深度文章（至少一篇）：

| 候选话题 | 为什么值得写 |
|:---------|:-------------|
| "Graph RAG 在什么场景下不如向量 RAG？" | 需要独立判断 + 边界分析 |
| "KDO 为什么选 LightRAG + HashingVectorizer？" | 需要 self-application |
| "全量检索 vs 分层检索的 trade-off" | 需要框架对照 |

用 Judge 三问：

```bash
kodo produce --deep --topic "Graph RAG vs 向量 RAG"
```

### Phase 4：验证 — Gold Standard 比对

欧阳锋手工标注 10 条 RAG 领域核心判断 → 对比管线产出：

```bash
python _verify_gold_standard.py
```

| 准确率 | 结论 |
|:------:|:------|
| ≥ 85% | 管线验证通过，可扩展到其他领域 |
| 70-85% | 排查哪步有问题，修复后重测 |
| < 70% | 管线设计有问题，复盘根因 |

---

## 验收清单

| # | 检查项 | 通过标准 |
|:-:|:-------|:---------|
| 1 | RAG 领域概念卡 ≥ 5 张 | 含检索/索引/分块/排序/GraphRAG |
| 2 | 每张卡有 source_refs + trust_level | 可追溯 |
| 3 | 图遍历识别出缺口并补充 | 收敛条件达成 |
| 4 | 至少一篇四步编译深度文章 | D1-D4 全部通过 |
| 5 | Gold Standard 准确率 ≥ 70% | 用欧阳锋标注的 10 条基准 |
| 6 | `kdo lint` 0新增错误 | 不破坏现有知识库 |

---

## 不做什么

- **不做** RAG 领域的 exhaustive 覆盖（这是 Pilot，不是百科全书）
- **不做** 外部搜索（已有素材足够验证管线）
- **不做** 修改 KDO 现有卡片（新产出放在新位置，不和已有卡片冲突）
- **不做** 全自动——每步之间需要人看一眼再继续

---

## 前置依赖

Pilot 依赖 Sprint 6 的断裂点 1（enrich+label 串联）和断裂点 2（ingest --assess）先就绪。如果 Sprint 6 还没跑完，可以先用手动模式验证：

```bash
# 手动模式（不需要 Sprint 6）：
kodo ingest --path "10_raw/sources/src_xxx.md"
kodo enrich --wiki-path "30_wiki/concepts/xxx.md" --llm
kodo label --card xxx --dry-run
```
