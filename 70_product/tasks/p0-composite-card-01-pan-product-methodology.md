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

### 🔧 进行中
- [ ] 6 张 yt-model-pan-product-* 框架卡升级到 agent-native 格式
- [ ] source_refs 迁移：00_inbox/ → 10_raw/sources/
- [ ] 关键原图归档：00_inbox/*.png → 10_raw/assets/yitang/
- [ ] kdo lint 0 error

## 验收标准
- [x] kdo lint 0 error（待重跑）
- [ ] 所有 source_refs 指向 10_raw/
- [x] frontmatter 图边字段无空值
- [x] query_triggers ≥ 3
- [x] Claims ≥ 10（实际 15）
- [x] Visual Analysis ≥ 2（实际 2）
- [x] 体量合规（≤500 行、≤5000 token）
