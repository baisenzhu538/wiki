---
title: "老顽童：三项任务 — 文章修复 + 工具箱升级 + AI数据第一课"
assigned_to: "老顽童（Producer）"
priority: "P1"
created_at: "2026-06-01"
reviewer: "欧阳锋"
status: "pending"
depends_on: []
blocks: ["Phase C 文章入库", "管理工具箱 A 级", "AI数据第一课产出"]
---

# 老顽童：三项任务

---

## 任务 1：Phase C 文章修复 🟡（15min）

上次审查有条件 PASS，3 处 FAIL 待修：

| # | 问题 | 修复方式 |
|:-:|:-----|:---------|
| 1 | 缺 `## Audience` 节 | 补一段目标读者描述 |
| 2 | 缺 `## Core Thesis` 节 | 补一段核心论点 |
| 3 | 错别字若干 | 通读一遍修掉 |

**修复后无需再审**，直接入库。

---

## 任务 2：管理工具箱 T6/T7/T8 升级 A- → A（~1h）

仪表盘记录的提升路径：

| 卡 | 当前问题 | 修复方式 |
|:---|:---------|:---------|
| T6 project-health-radar | 缺 Synthesis 节 | 补跨域综合结论 |
| T7 onboarding-90day | 缺 Synthesis 节 | 补跨域综合结论 |
| T8 equity-checklist | 缺 Synthesis 节 | 补跨域综合结论 |

每张卡补 `## Synthesis` 节后，检查旧版管理卡是否有指向新版的重定向需求。

---

## 任务 3（新）：AI数据第一课 → 内容产出（~4h）

### 素材

`00_inbox/AI-study/AI数据/` 下有 4 份口述稿（一堂课程体系，~240KB 总文本）：

| 文件 | 大小 | 类型 |
|:-----|:----:|:-----|
| 一堂-AI数据第一课口述01.txt | 78KB | 正式口述 |
| 一堂-AI数据第一课口述02.txt | 85KB | 正式口述 |
| 一堂-AI数据第一课口述03.txt | 38KB | 正式口述 |
| 一堂-AI数据第一课闲聊篇口述.txt | 38KB | 闲聊/补充 |
| AI数据理解第一课表格.md | 112B | **空模板**（待填充） |

### 做法

**Step 1：ingest + enrich**
```powershell
kdo ingest --limit 10
kdo enrich --all
```
确认 4 份口述稿生成 wiki 骨架（`30_wiki/concepts/` 下应有新文件）。

**Step 2：三步编译法**
对每张骨架卡执行三步编译：
1. **浓缩** — 提取 3-5 条核心论点
2. **质疑** — 评估前提假设、边界、可靠性
3. **对标** — 与现有概念卡建立双向链接

**Step 3：产出文章**
基于编译后的知识卡，产出文章到 `40_outputs/content/articles/`。

**Step 4：填充表格**
将 `AI数据理解第一课表格.md` 中的两个空表填满：
- AI 数据使用的 5 个层次
- AI 相关数据类型

### 产出格式

产出文件使用标准的 artifact frontmatter：

```yaml
---
artifact_id: "art_20260601_auto"
type: "content"
subtype: "article"
title: "AI数据理解第一课：..."
target_user: "正在建立AI数据认知的学习者"
status: "draft"
delivery_channel: "local"
source_refs: ["src_...", "src_..."]
wiki_refs: ["ai-data-lesson-1"]
---
```

### 自检清单

| # | 检查项 |
|:-:|:-------|
| 1 | 4 份口述稿全部 ingest + enrich？ |
| 2 | 每张卡完成三步编译？ |
| 3 | 文章有 Audience + Core Thesis + Draft 三节？ |
| 4 | 两个表格已填充？ |
| 5 | 文章内的 wiki_refs 链到对应概念卡？ |

### 顺序建议

先做任务 1（快修），再做任务 3（AI数据第一课），任务 2（工具箱升级）穿插作为换脑用途。
