---
title: "老顽童：y-model validator 修复 + 单元模型域 2 处小修"
assigned_to: "老顽童 (Producer)"
priority: "P0"
created_at: "2026-05-26"
reviewer: "欧阳锋"
status: "completed"
depends_on: []
blocks: []
---

# 老顽童：y-model validator 修复 + 单元模型域 2 处小修

## 背景

上一轮已完成：

- OCR Batch 4 15 张卡 ✅ 全部审查通过（手写 7 张 ✅、批量模板 8 张 A- ✅）
- Batch 5 评估已完成（117 张候选卡分析）：**不需要老顽童做**
  - 科学决策 31 张已精修通过（Batch 2+3 终验）
  - 其余 77 张内容太薄（condense 平均 10-15 words），ROI 低不投入
  - 9 张 Kahneman 残留的极低价值卡由欧阳锋直接改

**待修两件事**：y-model（P0 阻塞）+ 单元模型域 2 处小修（P2 顺手修）

---

## Step 1：y-model validator 修复（P0，~10min）

**目标**：`kdo validate --v15 --card yt-decision-y-model` 跑通 exit 0

**根因**：`yt-decision-y-model.md` 当前仍是 `## Constraints & Boundaries` 旧格式，`#### Gary Klein` 和 `#### Daniel Kahneman` 直接挂在 `Constraints & Boundaries` 下，没有 `### 外部攻击` 容器。

**修复方法**（同前）：
1. 将 `## Constraints & Boundaries` 改为 `## Critique`
2. 在 `####` 攻击者前插入 `### 外部攻击`，把当前所有 `####` 攻击者包进去
3. 确认格式与已 PASS 卡片（如 `yt-decision-canvas`）一致——详见 v1.5 格式要求：
   ```
   ## Critique

   ### 内部局限
   [内容]

   ### 外部攻击
   #### [学者名] — [标题]
   [攻击内容]
   ```
4. `kdo validate --v15 --card yt-decision-y-model` 直至 exit 0

> ⚠️ y-model 被引用 31 次，是跨域元框架。留一个已知 FAIL 会在后续批量验证时持续报警。

**参考卡片**：`yt-decision-canvas.md`、`yt-decision-depth-ladder.md`（已 PASS v1.5 验证）

---

## Step 2：单元模型域 2 处小修（P1，~5min，做完 Step 1 后顺手做）

上一轮审查发现 2 处小问题，当时约定"下一轮统一修"：

| # | 文件 | 问题 | 修复 |
|:-:|:----|:----|:-----|
| 1 | `yt-unit-model-overview.md` | frontmatter 缺 `id:` 字段；`author:` 写的是 `"老顿童"`（应为 `"老顽童"`） | 补上 `id:`，改 `author:` |
| 2 | `yt-unit-model-benchmark.md` | Thaler 攻击者段有乱码：`"不知豁的伙侑效应"` | 改为正确的 `"蔡加尼克效应"` 或其他 Thaler 术语 |

---

## 不做

- **不做** Batch 5 100+ 张卡——评估完成，ROI 低不投入
- **不做** VA 相关修改——洪七公已完成，无需回炉
- **不做** 9 张 Kahneman 残留低价值卡——欧阳锋已处理

---

## 验收

| # | 验收项 | 判定 |
|:-:|-------|:----:|
| 1 | `kdo validate --v15 --card yt-decision-y-model` exit 0 | 终端 |
| 2 | `yt-unit-model-overview.md` 有 `id:` 字段 + `author: "老顽童"` | grep |
| 3 | `yt-unit-model-benchmark.md` 无"不知豁的伙侑效应"乱码 | grep |

---

*欧阳锋 · 2026-05-26*
