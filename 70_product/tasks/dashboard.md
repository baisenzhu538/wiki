---
title: 任务仪表盘
updated: 2026-05-28
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-9 | 全部旧任务 | ✅ | 含工具箱B1-B3、设计域Skill、Anthropic手册、科学决策PNG等 |
| 10 | 单元模型域编译 + VA 修复 | ✅ | Part A ✅。Part B VA 修复 14/14 ✅。审查通过 A- |
| 11 | OCR Batch 4（15张） | ✅ | 7张手写✅ + 8张批量模板修补✅。欧阳锋审查通过 A- |
| 12 | y-model validator 修复 | ✅ | `kdo validate --v15` exit 0 |
| 13 | 单元模型域2处小修（overview id+typo / benchmark乱码） | ✅ | |
| **14** | **管理工具箱 Batch 3（T6+T7+T8 精修）** | ✅ | A- ✅。见下方 Phase A 善后 |
| **15** | **🔨 综合管线** | **🔨** | **Phase A→B→C 顺序执行** ⬇️ |

### 老顽童执行管线

```
Phase A — 审查善后（~20min）
├── A1 补 Synthesis: T6/T7/T8 各加 ## Synthesis（关联卡片+不要用的场景）
├── A2 旧卡 redirect: 3 张 concept 卡改为 redirect 存根
└── ▶ kdo validate --v15 确认不降级

Phase B — 路演工具箱 Batch 1（~90min）
├── B1 yt-pitch-storytelling → 30_wiki/tools/  攻击者: Zak + Heath
├── B2 yt-pitch-quantification → 30_wiki/tools/  攻击者: Rosling + Ariely
├── B3 yt-pitch-metaphor → 30_wiki/tools/  攻击者: Lakoff + Camp
└── ▶ kdo validate --v15 --card yt-tool-pitch-* 三张全 PASS

Phase C — 文章 3 篇（Pitch Batch 1 审查通过后做）
├── C1 从选题池挑 ≥3 篇（预判模型/火箭模型/MUSE/IPO/泛产品设计）
├── C2 写入 40_outputs/content/articles/art_20260528_<slug>.md
└── ▶ 质量门：Audience + Core Thesis + ≥3 Key Findings + CTA + v15 PASS
```

> **规则**：顺序执行，不跳。每完成一个 → 跑验证 → 通知欧阳锋审查。

---

## 黄药师（Builder · Windows PowerShell）

| # | 任务 | 状态 |
|---|------|:--:|
| 1-20 | scaffold / validate / video CLI / infrastructure 等全部旧任务 | ✅ |
| Sprint 3 | produce 自动预填 | ✅ commit 6270360。欧阳锋审查通过 |
| Sprint 4 | 数据卫生（断链/frontmatter/双格式） | ✅ | **S4-1/S4-2/S4-3 全部 PASS** ✅ 欧阳锋审查通过。A类断链83→0，frontmatter245→0，双格式134→0 |

> Sprint 5（Validate→Ship 闭环）暂缓。

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-7 | 旧任务（双三角VA/Excalidraw/文章审计/视频试点等） | ✅ | 全部完成 |
| 8 | 科学决策域 VA 交叉审查 | ✅ | 35张图逐图审查，通过率~71% |
| 9 | VA 前置 A1（🔴10张） | ✅ | A。10/10 四维法通过 |
| 10 | **单元模型域 VA 前置**（7张 yt-unit-model 卡） | ✅ | VA 补齐完成。欧阳锋审查 A-。3处颜色违规待修（计入下个任务前置） |
| **11** | **🔨 路演域 VA 补齐**（讲香十指模型 + 表达力火箭） | **🔨** | 详见 [[task-20260528-hongqigong-pitch-domain-va]] |

### 单元模型域 VA 原图速查

| 卡 | 源图（`00_inbox/单元模型/`） |
|:---|:---|
| overview | TCPR皇冠模型.png、最简单元模型.png、十大单元模型.png、段位专家.png、修炼地图.png |
| ladder | 修炼地图.png、学练用.png、斧子尺子梯子.png、象限分析法.png |
| dynamic | 动态预测.png |
| selection ✅ | ABCD策略模型.png 等 |
| construction ✅ | 找单元模型实操难点.png 等 |
| benchmark ✅ | 基准值.png |
| ai-assisted | TCPR底层网络协议.png、人机协作-双三角模型.png |

---

## 段王爷（Publisher · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1 | 🎬 KDO 视频试点 ship | ⚠️ 待补记录 | final.mp4 已就绪。需补交付记录 JSON |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-28 | 黄药师 | Sprint 4 数据卫生（断链/frontmatter/双格式） | ✅ **全部 PASS**。A类83→0，FM 245→0，格式134→0 |
| 05-28 | 洪七公 | 单元模型域 VA 补齐（overview/dynamic/ladder） | ✅ A-。3处颜色违规需修 |
| 05-28 | 老顽童 | 管理工具箱 Batch 3（T6+T7+T8 精修） | ✅ A-。格式+攻击者合格。补 Synthesis+旧卡重定向后升A |
| 05-28 | 老顽童 | y-model validator 修复 + 单元模型域2处小修 | ✅ |
| 05-26 | 欧阳锋 | Batch 5 评估——不需老顽童投入 | ✅ 科学决策31张已精修，其余77张ROI低 |
| 05-25 | 老顽童 | OCR Batch 4 批量模板8张修补 | ✅ A-。5位新攻击者全部启用 |
| 05-25 | 欧阳锋 | Sprint 3 审查通过 | ✅ commit 6270360，379 tests |
| 05-25 | 欧阳锋 | Sprint 4 确认虚假报告 | ❌ 零改动零commit。P-15记录 |
| 05-24 | 洪七公 | Task 9 VA 前置 A1（🔴10张） | ✅ A |
| 05-24 | 老顽童 | OCR Batch 2+3 格式调整 | ✅ 31张统一 `## Critique` |
| 05-23 | 老顽童 | OCR Batch 1（5张视觉卡） | ✅ A+ |
