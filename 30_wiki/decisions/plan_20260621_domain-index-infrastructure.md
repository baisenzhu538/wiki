---
id: plan_20260621_domain-index-infrastructure
title: 域索引入口卡 —— 大规模域建制的基础设施方案
type: improvement-plan
status: reviewed
domain:
- master
- kdo
source_refs:
- 90_control/templates/domain-index-template.md
- 30_wiki/domains/five-step-domain-digest.md
- 60_feedback/diagnosis/diag_20260620_调研专题素材验收.md
created_at: '2026-06-21'
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
related:
- '[[five-step-domain-digest]]'
- <code>check-source-refs.py</code>
- <code>track-production-progress.py</code>
- huangyaoshi-tagging-and-scope-proposal
updated_at: '2026-06-29'
---
# 域索引入口卡 —— 大规模域建制的基础设施方案

> 提交：黄药师 → 审查：欧阳锋 · 2026-06-21

## 问题

调研专题域经王语嫣诊断，预估 140+ 张卡片机会。分散在 `concepts/`、`frameworks/`、`tools/`、`cases/`、`dark-knowledges/` 五个目录。全库当前 1,389 张卡，调研域新增后增长约 10%。

**风险不在卡片数量，在于缺少导航结构。** 用户和老顽童都面临同一个问题：140 张卡散落在不同目录里，从哪开始看？哪些是核心框架、哪些是辅助案例？

## 方案：域索引入口卡（Domain Index Card）

### 核心思路

任何知识域超过 30 张卡片时，**必须**创建一张索引入口卡作为该域的「目录页」。入口卡不重复内容，只做导航——每行一句话，链接到具体卡片。

### 结构（四段式，已验证有效）

```
域摘要：<域名称>
├── 核心框架（先读）    → 框架卡 + 核心工具卡
├── 关键案例             → 按行业/场景索引
├── 暗知识（不要踩的坑） → 反常识/陷阱速查
└── 工具索引（按场景查） → 场景 → 卡片的映射表
```

### 已有验证案例

`30_wiki/domains/five-step-domain-digest.md`（五步法域，66 张卡）——已运行数周，证明四段式结构在 50-70 卡规模下导航清晰、维护成本低。

### 模板

已固化为 `90_control/templates/domain-index-template.md`，老顽童可按模板直接填表。

## 对调研域的具体建议

**在 Wave 1（核心框架卡）完成后，立即创建 `yitang-research-domain-digest.md`。**

时间点选择理由：
- src_unknown
- src_unknown
- src_unknown

## 基础设施配套

| 能力 | 状态 | 用途 |
|:--|:--|:--|
| `domain-index-template.md` | ✅ 已创建 | 可复用模板 |
| `check-source-refs.py` | ✅ 已交付 | 验证入口卡链接有效性 |
| `track-production-progress.py` | ✅ 已交付 | 追踪域内卡片生产进度 |
| `kdo scaffold --domain-index` | 🔵 建议后续 | 自动从域内卡片生成入口卡骨架 |

## 铁律（建议写入工厂规则）

1. **30 张以上必建入口**——不管用什么方式组织，低于 30 张可暂缓
2. **入口卡只链接不重复**——它是 GPS，不是百科全书
3. **入口卡过时比没有更糟**——域内增删卡片必须同步更新入口
4. **入口卡放 `30_wiki/domains/`**，命名 `{domain}-domain-digest.md`

## 决策请求

请欧阳锋裁定：
1. 是否批准域索引入口卡作为工厂标准基础设施
2. 调研域入口卡是否在 Wave 1 完成后立即创建
3. `kdo scaffold --domain-index` 是否纳入后续 Sprint
