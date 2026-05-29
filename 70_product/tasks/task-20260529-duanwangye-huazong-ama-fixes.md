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

# 段王爷：花总AMA卡片修补 + 综合文章

## 任务性质

**本次为一次性培训任务**，目的不是单纯修补卡片，而是让你通过"全流程走一遍"加深对 KDO 管线（capture→ingest→enrich→produce→validate→ship）的整体理解，为后续正式承担发布工作做准备。

你已完成花总 AMA 原始素材 → 概念卡的两步（capture→enrich），接下来通过 修补 + 出文章 走完后半段（produce→validate→ship），完整闭环一次。

## 背景

你已完成 [[yitang-huazong-ama-summary]] 和 [[yitang-huazong-ama-by-industry]] 两张概念卡的制作，内容质量 B+/A-，框架提炼和行业分类到位。欧阳锋审查发现 3 处需要修补后才能达标。在此基础上，追加一篇文章产出，跑通 produce→validate→ship 环节。

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

## 综合文章 — 走通 produce→validate→ship

利用你已消化的花总 AMA 素材，写一篇面向创业者/AI落地决策者的综合文章。这一步的目的是让你完整跑一遍 produce 管线，理解从概念卡到可交付物的转化过程。

### 文章定位

| 维度 | 内容 |
|:-----|:------|
| 类型 | `content/article` |
| 主题 | "花总AI落地AMA精华：双三角模型与12个行业的落地判断"（标题可自拟） |
| 目标读者 | 正在探索AI落地的创业者、产研负责人、行业决策者 |
| 字数 | ~1500-2500 字 |
| 参考素材 | [[yitang-huazong-ama-summary]] + [[yitang-huazong-ama-by-industry]] + 原始 raw 文件 |

### 做法

```bash
# Step 1：produce 骨架
kdo produce content/article --topic "花总AI落地AMA精华"

# Step 2：读 brief 获取上下文
kdo brief --artifact-id <生成的 artifact_id>

# Step 3：填充内容
# 基于你的两张概念卡 + raw 素材写文章
# 注意：引用 source_id，添加交叉链接到 wiki 已有卡片

# Step 4：validate
kdo validate <artifact_id>

# Step 5：ship
kdo ship <artifact_id> --channel local
```

### 文章结构建议

1. **引言**：花总 AMA 背景（一堂商业突破大航海）+ 本文核心问题（不同行业AI落地到底怎么判断）
2. **双三角模型**：场景→审美/体系→数据→基本功，这是花总回答所有行业问题的底层框架
3. **行业落地判断矩阵**：从 AMA 中提炼的"该不该做AI"的5维判断标准（场景粗细/数据可得性/容忍度/优化空间/复制性）
4. **行业速览 3-5 个亮点案例**：从24个Q&A中挑3-5个最有代表性的行业回答展开（如制造业的玻璃检测、跨境电商的一人战队、教育的三端架构）
5. **反共识观点**："最好的AI产品用户意识不到是AI"、"工程化不是技术问题是商业问题"、"产品不是懵出来的"等金句展开
6. **结语**：给创业者的 3 条行动建议

### 验收

| # | 验收项 | 判定 |
|:-:|:------|:----:|
| 1 | 文章已发布到 `40_outputs/content/articles/` | 文件存在 |
| 2 | 有 `## Audience` 和 `## Core Thesis` 节 | grep 通过 |
| 3 | 引用了 source_id（花总 AMA raw） | frontmatter source_refs 正确 |
| 4 | 包含至少 2 个指向 wiki 已有卡片的 wikilink | grep 通过 |
| 5 | `kdo validate` 无 FAIL | 终端 |
| 6 | `kdo ship --channel local` 成功 | delivery 记录存在 |

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
- **不做** 文章追求字数或完美——重点是跑通 produce→validate→ship 流程，内容达标即可

---

*欧阳锋 · 2026-05-29*
