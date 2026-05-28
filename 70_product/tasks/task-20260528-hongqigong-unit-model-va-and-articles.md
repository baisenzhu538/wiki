---
title: "洪七公：单元模型域 VA 补齐 + 文章重启"
assigned_to: "洪七公 (Multimodal Arbiter)"
priority: "P0"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 洪七公：单元模型域 VA 补齐 + 文章重启

## 背景

已完成：

- 单元模型域 7 张卡片全部编译完成，VA 已存在（上次审查通过 A-）
- 你已完成 selection / construction / benchmark 三张卡的 VA 重写 ✅
- 待做：overview / dynamic / ladder 三张卡 VA 升级

源图不在 `10_raw/assets/yitang/`，在 **`00_inbox/单元模型/`**。

---

## Step 1：单元模型域 VA 补齐（3 张卡）

用四维法标准（颜色不分析，只分析空间层级/分组逻辑/阅读路径/视觉强调）重写以下三张卡的 `## Visual Analysis` 节。

### 原图速查表

| 卡 | `00_inbox/单元模型/` 中的源图 |
|:---|:---|
| **overview** `yt-unit-model-overview` | TCPR皇冠模型.png、最简单元模型.png、十大单元模型.png、段位专家.png、修炼地图.png |
| **dynamic** `yt-unit-model-dynamic` | 动态预测.png |
| **ladder** `yt-unit-model-ladder` | 修炼地图.png、学练用.png、斧子尺子梯子.png、象限分析法.png |

> 如果一张卡对应多张图，每张图分别写一个 VA 段落（`### 图名` 作为子节），参考现有格式。

### VA 四维法标准

```
## Visual Analysis

### [图名]

原图为[类型描述]，整体呈[布局结构]。
空间层级：[标题→模块→子项的层级关系]
分组逻辑：[边框/留白/线框的分组语义]
阅读路径：[视觉流线：F形/Z形/中心辐射等]
视觉强调：[字号/位置/图标的权重分布]
留白运用：[分隔/呼吸/未完成语义]
```

> **不做**：颜色分析（颜色不纳入 VA 维度）。不做 Critique/Synthesis（那是老顽童的活）。

---

## Step 2：文章重启（Step 1 完成后做）

从 Batch 1 已完成的 5 张 A+ 卡中挑 ≥3 个选题，产出文章到 `40_outputs/content/articles/`。

### 选题池

| 卡 | 文章方向 |
|:---|:--------|
| `ocr-预判模型` | "预判模型三范式：从 N 要素到 Checklist——如何选择正确的预判复杂度" |
| `ocr-表达力火箭模型` | "Orwell 警告过的表达技巧——Magic Words 的边界与伦理" |
| `ocr-一堂-个人修炼-全景图muse模型` | "AI 共存时代，Postman 式的冷静——MUSE 框架的边界与盲区" |
| `ocr-一堂-个人修炼-科学学习ipo-全景策略` | "学习效率差 10 倍？Kahneman 和 Papert 为什么不同意" |
| `ocr-泛产品设计落地篇` | "泛产品设计的边界：当 Norman 和 Pye 说不" |

### 文章质量门

| # | 门禁项 | 判定 |
|:-:|------|:----:|
| 1 | 目标读者明确（`## Audience`） | 文件存在 |
| 2 | 核心论点 ≤3 句（`## Core Thesis`） | 人审 |
| 3 | ≥3 条 Key Finding，每条有 source_ref 追溯 | grep |
| 4 | 结尾有 Call to Action | 人审 |
| 5 | `kdo validate --v15 --article <path>` PASS | 终端 |

### 产出命名

```
40_outputs/content/articles/art_20260528_<slug>.md
```

---

## 不做

- **不做** Critique/Synthesis（老顽童的活）
- **不做** 颜色分析
- **不做** 纯文本卡 VA（如落地卡片系列、用户卡片系列）
- **不做** 低价值卡（Batch 5：截图类、微信图片类）

## 验收

| # | 验收项 | 判定 |
|:-:|------|:----:|
| 1 | overview / dynamic / ladder 三张卡均有 `## Visual Analysis`（四维法，≥100 字/图） | grep + 人工 |
| 2 | VA 不含颜色分析 | 人工确认 |
| 3 | ≥3 篇新文章产出到 `40_outputs/content/articles/` | 文件存在 + 非空 |
| 4 | 文章质量门全部通过 | 欧阳锋抽检 |

## 执行顺序

```
Step 1：overview VA → dynamic VA → ladder VA
  ↓ 通知欧阳锋审查
Step 2：文章 3 篇（选题任选，不重复）
  ↓ 通知欧阳锋审查
```

---

*欧阳锋 · 2026-05-28*
