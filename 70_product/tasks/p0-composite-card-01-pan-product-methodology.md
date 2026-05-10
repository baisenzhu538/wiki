---
title: "P0 复合卡 #1——泛产品设计方法论（Agent 原生格式）"
status: "active"
priority: "P0"
assigned_to: "黄药师"
reviewer: "欧阳锋"
created_at: "2026-05-11"
---

# P0：泛产品设计方法论——首张 Agent 原生复合卡

## 背景

- 33 张 yt-panproduct-* 碎片卡已降级为 draft
- 新设计规范：[[agent-native-card-design]]
- 目标：按 Agent 原生格式产出第一张 composite-concept 卡

## 素材清单

### 口述稿（5 份）
1. `00_inbox/一堂-个人修炼-泛产品设计概念口述版.md`
2. `00_inbox/一堂-个人修炼-泛产品设计探索营口述版.md`
3. `00_inbox/一堂-个人修炼-泛产品设计工具篇口述版.md`
4. `00_inbox/ideas/一堂-个人修身-泛产品设计审美口述.md`
5. `00_inbox/ideas/一堂-个人修身-泛产品设计实操口述版.md`

### 框架地图（6 张）
- [[yt-model-pan-product-climbing-map]] — 十年修炼爬山地图
- [[yt-model-pan-product-36-strategies]] — 36计全套地图
- [[yt-model-pan-product-three-virtues]] — 三大自我修养
- [[yt-model-pan-product-demand-toolkit]] — 需求工具箱
- [[yt-model-pan-product-aesthetic-toolkit]] — 审美工具箱
- [[yt-model-pan-product-execution-toolkit]] — 落地工具箱

### 知识地图原图（关键几张）
- `00_inbox/一堂泛产品设计36计-全套地图.png`
- `00_inbox/一堂泛产品设计-十年修炼爬山地图.png`
- `00_inbox/优秀泛产品设计者的自我修养.png`
- `00_inbox/泛产品设计者的三大自我修养.png`

## 产出要求

### 文件
- `30_wiki/concepts/yt-composite-pan-product-methodology.md`

### Frontmatter
- type: composite-concept
- domain: yitang
- query_triggers 非空
- source_refs → 10_raw/sources/
- prerequisites、component_of、related 完整

### Body
- Claims ≥ 10（30 张知识地图压缩后的核心断言）
- Framework Gallery：嵌入 6 张框架卡 wikilink + 关键原图
- Visual Analysis：爬山地图、36计地图、三大修养（共 3 份五维分析）
- Constraints & Boundaries：明确不适用场景
- Synthesis：图边关系表

## 验收标准
- [ ] kdo lint 0 error
- [ ] 所有 source_refs 指向 10_raw/
- [ ] frontmatter 图边字段无空值
- [ ] query_triggers ≥ 3
- [ ] Claims ≥ 10
- [ ] Visual Analysis ≥ 3
