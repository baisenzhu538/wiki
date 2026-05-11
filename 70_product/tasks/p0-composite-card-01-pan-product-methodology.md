---
title: "P0 复合卡 #1——泛产品设计方法论（Agent 原生格式）"
status: "active"
priority: "P0"
assigned_to: "黄药师"
reviewer: "欧阳锋"
created_at: "2026-05-11"
updated_at: "2026-05-11"
---

# P0：泛产品设计方法论——首张 Agent 原生复合卡

## 设计决策（2026-05-11 黄药师/欧阳锋共识）

**三层图结构**（回应欧阳锋聚合粒度质疑）：

```
yt-composite-pan-product-methodology.md       ← composite-concept（15 claims，顶层方法论框架）
  ├── component_of → yt-model-pan-product-demand-toolkit.md    ← framework（需求维度，待升级）
  ├── component_of → yt-model-pan-product-aesthetic-toolkit.md ← framework（审美维度，待升级）
  └── component_of → yt-model-pan-product-execution-toolkit.md ← framework（落地维度，待升级）
```

- Hub Page 类型：放弃（图边 + query_triggers + Framework Gallery = 足够）
- 33 张 yt-panproduct-* 卡片：type tool, status enriched（保留为叶子节点）
- 6 张 yt-model-pan-product-* 框架卡：需升级到 agent-native 格式

## 素材清单

### 口述稿（5 份）
1. `00_inbox/一堂-个人修炼-泛产品设计概念口述版.md`
2. `00_inbox/一堂-个人修炼-泛产品设计探索营口述版.md`
3. `00_inbox/一堂-个人修炼-泛产品设计工具篇口述版.md`
4. `00_inbox/ideas/一堂-个人修身-泛产品设计审美口述.md`
5. `00_inbox/ideas/一堂-个人修身-泛产品设计实操口述版.md`

### 框架地图（6 张，均需 agent-native 升级）
- [[yt-model-pan-product-climbing-map]] — 十年修炼爬山地图
- [[yt-model-pan-product-36-strategies]] — 36计全套地图
- [[yt-model-pan-product-three-virtues]] — 三大自我修养
- [[yt-model-pan-product-demand-toolkit]] — 需求工具箱
- [[yt-model-pan-product-aesthetic-toolkit]] — 审美工具箱
- [[yt-model-pan-product-execution-toolkit]] — 落地工具箱

## 进度

### ✅ 已完成
- [x] `agent-native-card-design.md` v2 规范 + 欧阳锋/黄药师共识
- [x] `yt-composite-pan-product-methodology.md` v2 压缩版（15 claims, 2 Visual Analysis, ~2800 token）
- [x] 33 张 yt-panproduct-* 重新分类：type=tool, status=enriched
- [x] 6 张 yt-model-pan-product-* 框架卡升级到 agent-native 格式
- [x] kdo lint: 0 errors

### ⏳ 延后项（非阻塞，后续批量处理）
- [ ] source_refs 迁移：00_inbox/ → 10_raw/sources/（需先 kdo ingest 口述稿到 10_raw）
- [ ] 关键原图归档：00_inbox/*.png → 10_raw/assets/yitang/

## 验收标准
- [x] kdo lint 0 error（已重跑确认）
- [ ] 所有 source_refs 指向 10_raw/（延后，等待 kdo ingest 批处理）
- [x] frontmatter 图边字段无空值
- [x] query_triggers ≥ 3
- [x] Claims ≥ 10（实际 15）
- [x] Visual Analysis ≥ 2（实际 2）
- [x] 体量合规（≤500 行、≤5000 token）

---

## 最终交付报告（2026-05-11 黄药师）

### 产出清单

| 文件 | type | claims | token | 状态 |
|------|------|--------|-------|------|
| `30_wiki/concepts/yt-composite-pan-product-methodology.md` | composite-concept | 15 | ~2800 | enriched |
| `30_wiki/concepts/yt-model-pan-product-36-strategies.md` | framework | 11 | ~2200 | enriched |
| `30_wiki/concepts/yt-model-pan-product-three-virtues.md` | framework | 9 | ~1800 | enriched |
| `30_wiki/concepts/yt-model-pan-product-climbing-map.md` | framework | 13 | ~1800 | enriched |
| `30_wiki/concepts/yt-model-pan-product-demand-toolkit.md` | framework | 16 | ~1800 | enriched |
| `30_wiki/concepts/yt-model-pan-product-aesthetic-toolkit.md` | framework | 9 | ~1600 | enriched |
| `30_wiki/concepts/yt-model-pan-product-execution-toolkit.md` | framework | 18 | ~1800 | enriched |
| 33 × `yt-panproduct-*.md` | tool | 原有 | 原有 | enriched |

### 三层图结构已就绪

```
composite-concept (顶层)
  └── framework × 6 (中层)
        └── tool × 33 (叶子层)
```

### 质量检查

| 检查项 | 结果 |
|--------|------|
| kdo lint errors | 0 |
| 卡片体量合规 | 全部合规（均 ≤500 行、≤5000 token） |
| frontmatter 图边完整 | 7/7 卡 id/type/domain/confidence/query_triggers/prerequisites/component_of/related/contradicts 无空值 |
| Claims 格式 | 全部 `claim:NN [conf=X][src]` 格式 |
| Constraints 非空 | 7/7 卡至少 1 条 boundary claim |
| source_refs | 仍指向 00_inbox/（延后，等 kdo ingest 批处理） |

### 已知延后项
1. source_refs → 10_raw/：需先将 5 份口述稿 kdo ingest 到 10_raw/sources/，再批量更新所有卡的 source_refs
2. 原图归档：4 张 PNG 需从 00_inbox/ 复制到 10_raw/assets/yitang/
3. 实体页更新：`30_wiki/entities/一堂.md` 需补充 composite-concept 和 framework 卡的 wikilink
