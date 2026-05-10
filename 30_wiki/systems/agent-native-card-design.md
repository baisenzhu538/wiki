---
title: "Agent 原生知识卡设计规范"
type: "system"
status: "active"
domain: "kdo"
created_at: "2026-05-11"
---

# Agent 原生知识卡设计规范

## 定位

`30_wiki/` 中的卡片是 **agent 的知识基座**。Agent 消费卡片后，产出 `40_outputs/` 中的人类可读文章。

```
30_wiki（Agent 消费）──查询/遍历──▶ Agent ──生成──▶ 40_outputs（人类阅读）
```

## 卡片类型

| type | 用途 |
|------|------|
| `composite-concept` | 复合概念卡——聚合多份素材的完整概念 |
| `framework` | 框架卡——知识地图/模型图的结构化描述 |
| `case` | 案例卡——具体案例 |
| `tool` | 工具卡——可操作的检查清单、画布、模板 |

## 核心设计原则

- **结构化优于叙事**：claims 列表、键值对、表格，而不是连续段落
- **frontmatter 是一等查询入口**：agent 通过 Dataview / API 按 frontmatter 过滤
- **图边显式声明**：prerequisites、component_of、related、contradicts 全部在 frontmatter
- **每条 claim 有 id**：可独立引用、独立验证

## Agent 原生 Frontmatter

```yaml
---
title: ""
type: "composite-concept"
status: "enriched"
domain: "yitang"
confidence: 0.8

# 图遍历边
prerequisites: []          # 理解本卡前需先掌握的卡片
component_of: []           # 本卡是哪个更大概念的子集
related: []                # 相关卡片
contradicts: []            # 与其他卡片有矛盾的主张

# 检索触发
query_triggers: []         # agent 按此匹配用户意图

# 溯源（必须指向 10_raw/）
source_refs:
  - "10_raw/sources/xxx.md"
---
```

## Agent 原生 Body 结构

```markdown
## Claims
<!-- 核心断言，每条可独立引用 -->
- [claim:01] 断言内容...

## Framework Gallery
<!-- 知识地图/原图作为视觉附件 -->
- [[framework-card-1]]
- ![[image.png]]

## Visual Analysis
<!-- 仅对知识地图/模型图：五维分析 -->
- 布局结构：
- 核心隐喻：
- 信息层级：
- 视觉锚点：
- 隐含假设：

## Constraints & Boundaries
<!-- 什么时候不适用 -->
- 不适用场景：
- 边界条件：

## Synthesis
<!-- 与其他节点关系的可机器解析图 -->
| 关系 | 目标节点 |
|------|---------|
| 前置 | [[]] |
| 组件 | [[]] |
```

## 三步编译的 Agent 化映射

| 旧（人类叙事） | 新（Agent 结构） |
|:--|:--|
| Condense 叙事段落 | Claims 列表（每条可独立引用） |
| Critique 推理过程 | Constraints & Boundaries + contradicts 字段 |
| Synthesis 叙事整合 | Synthesis 关系表 + related frontmatter |
| 文章内 wikilink | frontmatter 图边 + Framework Gallery |

## 卡片质量门禁

| 门禁 | 要求 |
|:--|:--|
| frontmatter 完整 | 所有图边字段 + query_triggers 非空 |
| Claims ≥ 5 | 每条带 [claim:NN] id |
| source_refs → 10_raw/ | 不得指向 00_inbox/ |
| Visual Analysis | 每个嵌入原图都有五维分析 |
| Constraints 非空 | 明确写出不适用场景 |
| kdo lint 0 error | |
