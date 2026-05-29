---
title: "段王爷：花总AMA卡片修补 — source_refs格式+交叉链接+格式清理"
assigned_to: "段王爷 (Publisher)"
priority: "P2"
created_at: "2026-05-29"
reviewer: "欧阳锋"
status: "pending"
depends_on: []
blocks: []
---

# 段王爷：花总AMA卡片修补

## 背景

你已完成 [[yitang-huazong-ama-summary]] 和 [[yitang-huazong-ama-by-industry]] 两张概念卡的制作，内容质量 B+/A-，框架提炼和行业分类到位。欧阳锋审查发现 3 处需要修补后才能达标。

---

## 修补项

### Fix 1：source_refs 格式违规（P0）

**现状**：两张卡 frontmatter 中 `source_refs: [[yitang-huazong-ama-20250526]]` 使用了 wikilink 格式。

**标准**：全库约定 `source_refs` 为 `list[str]`，取值是 `10_raw/sources/` 下带 `src_` 前缀的 source_id：
```yaml
source_refs: ["src_20260529_xxxxxx"]
```

**做法**：
1. 将 `10_raw/web/yitang-huazong-ama-20250526.md` 复制到 `00_inbox/`（加 frontmatter），运行 `kdo ingest` 注册为正式 source 文件
2. 或者直接复制到 `10_raw/sources/` 手动创建 source 文件（参考其他 `src_` 文件格式）
3. 获取生成的 source_id，更新两张卡 frontmatter 中的 `source_refs`

### Fix 2：补充与既有卡片的交叉链接（P1）

**现状**：两张卡均未链接库中已有的一堂框架卡片。

**需要补充的链接**：

在 **summary 卡**的 Core Methodology 章节：

| 位置 | 应链接 |
|:-----|:-------|
| 双三角模型 | [[ocr-一堂-个人修炼-双三角模型]]、[[yt-model-dual-triangle-competitiveness]] |
| 五步法 | [[yt-entrepreneur-five-step-method]]、[[yt-model-five-step-canvas]] |

在 **by-industry 卡**同理，在相关行业 Q&A 处补充链接。

### Fix 3：格式清理（P2）

**by-industry 卡**：
- L24-26 删除多余的孤立 `---`
- 删除 2 处"未回答"的条目（"不同行业AI落地差异工具团队"、""制造业AI结合案例餐饮业借鉴"），无信息量

---

## 验收

| # | 验收项 | 判定 |
|:-:|:------|:----:|
| 1 | source_refs 改为 `["src_xxx"]` 格式 | grep 无 `source_refs: [[` |
| 2 | 两张卡补充了双三角模型/五步法的 wikilink | 文件存在 |
| 3 | by-industry 卡无多余 `---` 横线和"未回答"条目 | 文件存在 |
| 4 | `kdo validate --v15` 不降级 | 0 Failed |

## 不做

- **不做** 重写内容或新增 Q&A
- **不做** 给 summary 卡加 Question/Synthesis 节（AMA 摘要不需要三步编译法）
- **不做** 处理 `00_inbox/AI-study/` 下的另一份 AMA（那是不同材料）

---

*欧阳锋 · 2026-05-29*
