---
title: "洪七公任务：OCR 卡 VA 前置 + 文章管线预热"
assigned_to: "洪七公 (Multimodal Arbiter)"
priority: "P1"
created_at: "2026-05-23"
reviewer: "欧阳锋"
status: "pending"
depends_on: []
blocks: ["70_product/tasks/task-20260523-laowantong-ocr-critique-synthesis"]
---

# 洪七公任务：OCR 卡 VA 前置 + 文章管线重启

## 背景

老顽童正在逐张补 136 张 OCR 卡的 Critique + Synthesis。36 张已完成（5 张 A+ 水准，31 张科学决策域达标）。剩余 100 张中，大量是**复杂视觉知识**（知识地图、矩阵图、全景图、工具箱示意图）——老顽童做 VA 不够专业，导致 Critique/Synthesis 缺少视觉上下文，质量从 Batch 1 的 A+ 退化。

同时，文章管线自 5/17 起完全停摆（6 天零产出）。已完成卡片的 Output Opportunities 中积累了大量 article 选题，无人启动。

## 做什么（两项，互不依赖，可并行）

### 任务 A：复杂视觉卡 VA 前置

从剩余 100 张 OCR 卡中，挑出**视觉结构复杂**的卡（知识地图、全景图、矩阵图、流程图、工具箱示意图），对原图做 Visual Analysis 五维法，产出 VA 段落写入卡片的 `## Visual Analysis` 节。

**五维法标准**（参照 `90_control/kdo-industrialization-manual.md` 中 VA 规范）：
- 空间层级：标题→模块→子项的层级关系
- 分组逻辑：色块/边框/留白的分组语义
- 阅读路径：视觉流线（F形/Z形/中心辐射等）
- 视觉强调：字号/颜色/位置/图标的权重分布
- 留白含义：空白区的功能（分隔/呼吸/未完成暗示）

**目标卡**（优先级从高到低）：

| 优先级 | 卡 | 视觉特征 |
|:--:|:---|:---|
| 🔴 | `ocr-一堂进步大地图` | 系统全景图 |
| 🔴 | `ocr-一堂-地图-创业地图` | 课程地图 |
| 🔴 | `ocr-一堂-地图-个人地图` | 课程地图 |
| 🔴 | `ocr-一堂-地图-管理地图` | 课程地图 |
| 🔴 | `ocr-一堂泛产品设计36计-全套地图` | 工具箱全景 |
| 🔴 | `ocr-一堂泛产品设计-十年修炼爬山地图` | 成长路径图 |
| 🔴 | `ocr-一堂个人地图高潜力成长者修炼全景图` | 成长全景 |
| 🔴 | `ocr-萃取总结` | 流程+层级（洪七公 cross-review 中标记过） |
| 🔴 | `ocr-一堂y模型实操工作流` | 工作流图 |
| 🔴 | `ocr-一堂y模型-科学成事道理` | 方法论图 |
| 🟡 | `ocr-泛产品设计审美工具箱指南` | 工具箱索引 |
| 🟡 | `ocr-泛产品设计需求工具箱指南` | 工具箱索引 |
| 🟡 | `ocr-泛产品设计落地工具篇指南` | 工具指南 |
| 🟡 | `ocr-泛产品设计者的三大自我修养` | 能力框架 |
| 🟡 | `ocr-婚礼规划` | 视觉规划图 |
| 🟡 | `ocr-一堂-个人修炼-双三角模型` | 双三角可视化 |
| 🟡 | `ocr-泛产品设计的应用场景示意图` | 应用场景矩阵 |
| 🟡 | `ocr-项目背景问题思考的8个维度` | 8维度框架图 |
| 🟢 | `ocr-一堂-个人修炼-讲香十指模型-超级武器库` | 十指模型可视化 |
| 🟢 | `ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图` | 修炼地图 |
| 🟢 | `ocr-一堂-个人修炼-表达力火箭模型` | 火箭模型 |
| 🟢 | `ocr-一堂-个人修炼-科学学习ipo模型` | IPO模型图 |
| 🟢 | `ocr-一堂深度复盘冰山图` | 冰山图 |
| 🟢 | `ocr-一堂五步法画布` | 画布图 |
| 🟢 | `ocr-一堂最佳转化率动力曲线图` | 曲线图 |

**产出格式**（写入卡片的 `## Visual Analysis` 节，位置在 `## Source Refs` 后、`## Reusable Knowledge` 前）：

```markdown
## Visual Analysis

原图为[类型描述]，整体呈[布局结构]。标题[描述]位于[位置]。主体分为[N]个区域：[区域1描述]→[区域2描述]→[区域3描述]。色彩编码：[颜色=含义映射]。阅读路径：[描述]。关键视觉元素：[描述]。留白运用：[描述]。
```

**不需要**做：VA 写入后不继续做 Critique/Synthesis——那是老顽童的活。

### 任务 B：文章管线重启

从**已完成的 36 张 OCR 卡**中，挑 3-5 个 Output Opportunities 里标注了 `article` 的选题，产出文章初稿到 `40_outputs/content/articles/`。

**选题标准**：
- 该卡已完成 Critique + Synthesis（老顽童已过）
- Output Opportunities 中 Content 字段非空
- 主题跨域或具有实战指导价值（而非纯 OCR 文本复原）

**建议首发**（从已完成卡中提取）：

| 卡 | 文章方向 | 理由 |
|:---|:---|:---|
| `ocr-预判模型` | "预判模型三范式：从 N 要素到 Checklist——如何选择正确的预判复杂度" | Kahneman+Taleb 攻击者论证已完成，文章可整合批判视角 |
| `ocr-表达力火箭模型` | "Orwell 警告过的表达技巧——Magic Words 的边界与伦理" | Orwell+Simon 攻击者选择精妙，文章可独立成篇 |
| `ocr-MUSE模型` | "AI 共存时代，Postman 式的冷静——MUSE 框架的边界与盲区" | Postman+Morozov 攻击有力，适合长文 |
| `ocr-科学学习IPO` | "学习效率差 10 倍？Kahneman 和 Papert 为什么不同意" | Papert 建构主义视角稀缺 |
| `ocr-泛产品设计落地篇` | "泛产品设计的边界：当 Norman 和 Pye 说不" | Norman+Pye 组合独特，设计域稀缺内容 |

**产出路径**：
```
已完成卡 → Read 原卡（Summary + Reusable Knowledge + Critique + Synthesis）
         → 整合为文章骨架（Audience + Core Thesis + Key Findings）
         → 产出到 40_outputs/content/articles/art_<date>_<slug>.md
```

**文章质量门**（参照 `90_control/kdo-industrialization-manual.md`）：
- 目标读者明确（`## Audience`）
- 核心论点 ≤3 句（`## Core Thesis`）
- ≥3 条 Key Finding，每条有 source_ref 追溯
- 结尾有 Call to Action

## 不做什么

- **不做** Critique/Synthesis（老顽童）
- **不做** 纯文本卡 VA（如落地卡片系列、用户卡片系列）——这些留给老顽童自己处理
- **不做** 低价值卡（Batch 5：screenshot1/2、微信图片、_conv、_compressed）——这些等评估后再决定
- **不做** dont-use/AT 段落——那是老顽童的 Critque 一部分

## 验收

| # | 验收项 | 判定方式 |
|:--:|------|------|
| 1 | ≥10 张视觉框架卡有 `## Visual Analysis` 节（五维法完整，≥200 字） | grep + 人工抽检 3 张 |
| 2 | ≥3 篇新文章产出到 `40_outputs/content/articles/` | 文件存在 + 非空 |
| 3 | 文章质量门通过（Audience/Thesis/Findings/CTA 齐全） | 欧阳锋抽检 |
| 4 | VA 段落未覆盖 Critique/Synthesis 内容（不踩老顽童的活） | 人工确认 |

## 进度表

| Task | 目标 | 已完成 | 备注 |
|:---|:--:|:--:|:---|
| A：VA 前置 | ≥10 张 | 0 | 优先级 🔴→🟡→🟢 顺序 |
| B：文章 | ≥3 篇 | 0 | 可选上述 5 个选题，也可自选 |

---

*欧阳锋 · 2026-05-23*
