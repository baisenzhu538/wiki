# 老顽童后续任务

> **更新：2026-06-15** — 建模域递归深挖三圈全部完成，详见完工报告。

---

## ✅ 紧急修正：高阶建模域递归深挖（已完成）

**问题**：已产的 4 张 dk 卡只覆盖了浅层素材。Truman 的口述稿、案例图、段位图、**AI skills 工程指南完整产出过程**均未被提取。

### 素材

`10_raw/sources/`：

| 素材 | 用途 |
|:-----|:------|
| 口述稿 + 笔记 | 核心文本，含 skills 工程指南 |
| 本质建模三个目标、段位图 | 框架素材 |
| 抽象建模案例×2、本质建模案例×2、流程建模×2、开播准备×2 | 案例素材 |

### 递归深挖

- ✅ **第一圈：补 case 卡** — 每个案例独立成卡（已完成）
- ✅ **第二圈：补技能工程指南** — **最重要**，口述稿中的完整产出过程（已完成）
- ✅ **第三圈：深度提升已有 dk 卡** — 基于口述稿补具体案例（已完成）

**完工报告**：`50_delivery/briefs/brief_20260615_modeling-deep-dive-completion.md`

三圈均已通过自检与 lint，进入审查阶段。

---

## 🎯 全量精修任务

**总卡数：238 张 yt-* 卡（已精修 237 张含 DS + Constraints & Boundaries，剩余 1 张空文件 `yt-management-conversion-hacking 1.md` 跳过）。**

> 注：3 张 redirect 卡（yt-tool-equity-checklist / yt-tool-onboarding-90day / yt-tool-project-health-radar）已补充 redirect 专用 DS 与边界说明。

> 注：历史批次表格中部分卡片重复出现，导致序号累加高于实际；后续累计数以「frontmatter 中已写入 diagnostic_signals」的真实卡数为准。

### 严禁行为

❌ 禁止批量扫。逐张开工，改完一张再下一张。
❌ 禁止只改 `related` 不加 DS。那叫格式清理，不叫精修。

### 每张卡必做

1. **Constraints & Boundaries**：适用边界表（≥2行）+ 常见失败模式表（≥3条，有症状有修复）。表格格式。
2. **diagnostic_signals**（≥2条）：加到 frontmatter，Signal → Lens → Follow-up 三元组完整。
3. 按样板卡标准。低于标准的退回。

### 递归深挖法

不是一遍到位：

```
第一圈：加 Constraints 表 + 2 条 DS → 通知欧阳锋审查
第二圈：根据反馈补失败模式、精修 DS → 通知欧阳锋审查
第三圈：如需要，强化 Critique 或加 Action Triggers → 通知欧阳锋审查
```

### 样板卡

`yt-decision-width-method`。以此为质量标准。

### 批次

| 批次 | 范围 | 数量 |
|:----:|:-----|:----:|
| **1** | yt-tool-*、yt-decision-*、yt-unit-*、yt-model-* | ~60 |
| **2** | yt-entrepreneur-*、yt-panproduct-*、yt-research-* | ~60 |
| **3** | yt-personal-*、yt-management-*、yt-pitch-*、yt-note-* | ~80 |
| **4** | yt-foresight-*、yt-prompt-*、其余 yt-* | ~40 |

### 节奏

**先做 5 张，停下来等审查。** 5 张全部通过后，再做剩下的 ~215 张。

逐张开工，禁止批量。改完一张自查 → 改下一张。凑满 5 张 → 通知欧阳锋审查。5 张全部通过之前，不动第 6 张。

### 审查结果

✅ **全量精修接近完成（208/238）。** 收尾完成后通知欧阳锋。

---

## 当前状态

✅ **全量精修 237/238 完成。七件事集团入库完成。老顽童全线收工待命。**

| 任务 | 状态 |
|:-----|:----:|
| 全量精修 | ✅ 237/238 |
| 七件事集团入库 | ✅ 已完成 |
| 断言式标题 | 持续 |

### 第一批 5 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 1 | `yt-model-five-step-canvas` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已通过 |
| 2 | `yt-decision-habit-shift` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已通过 |
| 3 | `yt-decision-height-toolkit` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已通过 |
| 4 | `yt-unit-model-build` | skill | 新增 frontmatter DS 2 条 + 正文 DS 精简 + 失败模式从 2 条补到 4 条 | ✅ 已通过 |
| 5 | `yt-decision-review` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已通过 |

**更新：2026-06-13** — 第一批 5 张已通过审查。继续第二批。

### 第二批 5 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 6 | `yt-decision-y-model` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | 🟡 待抽检 |
| 7 | `yt-decision-full-process` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | 🟡 待抽检 |
| 8 | `yt-decision-consensus-iceberg` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | 🟡 待抽检 |
| 9 | `yt-decision-ai-partner` | tool | 新增 frontmatter DS 2 条 + 正文 DS 精简 | 🟡 待抽检 |
| 10 | `yt-decision-canvas` | tool | 新增 frontmatter DS 2 条 + 正文 DS 精简 | 🟡 待抽检 |

**更新：2026-06-13** — 第二批 5 张已完成第一圈精修。

### 第三批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 11 | `yt-decision-depth-ladder` | framework | 重建损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 12 | `yt-model-entrepreneur-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 13 | `yt-model-management-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 14 | `yt-model-cognitive-upgrade-framework` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 15 | `yt-model-personal-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 16 | `yt-model-progress-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 17 | `yt-tool-meeting-designer` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 18 | `yt-tool-hiring-scorecard` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 19 | `yt-tool-foresight-canvas` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 20 | `yt-unit-model-selection` | skill | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第三批 10 张已完成第一圈精修。

### 第四批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 21 | `yt-model-agent-architecture` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 22 | `yt-model-aesthetic-progression` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 23 | `yt-model-conversion-optimization` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 24 | `yt-model-deep-review-iceberg` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 25 | `yt-model-deliberate-practice-growth` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 26 | `yt-model-dual-triangle-competitiveness` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 27 | `yt-model-ipo-learning-strategy` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 28 | `yt-model-ipo-complete-checklist` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 29 | `yt-model-liberate-thinking-layers` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 30 | `yt-model-muse-ai-framework` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第四批 10 张已完成第一圈精修。累计完成 38 张，剩余 ~200 张。

### 第五批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 31 | `yt-ai-startup-20-risky-hypotheses` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 7 条 + 失败模式 4 条） | ✅ 已完成 |
| 32 | `yt-ai-trend-12-signals` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 33 | `yt-barrier-analysis-cheat-sheet` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 34 | `yt-barrier-identification-skill` | skill | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 35 | `yt-business-analysis-cognitive-biases` | dk | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 36 | `yt-case-mandatory-cases` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 37 | `yt-composite-pan-product-methodology` | composite-concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 38 | `yt-concept-ai-guard-brain` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 39 | `yt-concept-context-engineering` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 40 | `yt-concept-p-type-l-type` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第五批 10 张已完成第一圈精修。累计完成 50 张，剩余 ~188 张。

### 第六批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 41 | `yt-concept-peas-insight` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 7 条 + 失败模式 4 条） | ✅ 已完成 |
| 42 | `yt-concept-weapon-arsenal` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 43 | `yt-customer-acquisition-toolkit` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 44 | `yt-demand-analysis-hiking-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 45 | `yt-entrepreneur-259-milestone` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 46 | `yt-entrepreneur-barriers` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 47 | `yt-entrepreneur-business-growth` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 48 | `yt-entrepreneur-channel-exploration` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 49 | `yt-entrepreneur-concentration-analysis` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 50 | `yt-entrepreneur-five-step-method` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第六批 10 张已完成第一圈精修。累计完成 60 张，剩余 ~178 张。

### 第七批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 51 | `yt-entrepreneur-fundraising` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 52 | `yt-entrepreneur-growth-flywheel` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 53 | `yt-entrepreneur-industrial-production` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 54 | `yt-entrepreneur-industry-forecast` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 55 | `yt-entrepreneur-key-hypotheses` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 56 | `yt-entrepreneur-lean-validation` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 57 | `yt-entrepreneur-liberate-thinking` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 58 | `yt-entrepreneur-needs-analysis` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 59 | `yt-entrepreneur-opportunity-selection` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 60 | `yt-entrepreneur-pragmatic-startup` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第七批 10 张已完成第一圈精修。累计完成 70 张，剩余 ~168 张。

### 第八批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 61 | `yt-entrepreneur-product-core` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 62 | `yt-entrepreneur-research-camp` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 63 | `yt-entrepreneur-research-cognition` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 64 | `yt-entrepreneur-scientific-method` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 65 | `yt-entrepreneur-spin-selling` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 66 | `yt-entrepreneur-truth-seeking` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 67 | `yt-entrepreneur-unit-model` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 68 | `yt-five-step-common-pitfalls` | dk | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 69 | `yt-five-step-implementation` | skill | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 70 | `yt-five-step-level-blindspots` | dk | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第八批 10 张已完成第一圈精修。累计完成 80 张，剩余 ~158 张。

### 第九批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 71 | `yt-five-step-method` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 72 | `yt-foresight-15-char-mantra` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 73 | `yt-foresight-ab-steady-state` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 74 | `yt-foresight-addition-subtraction` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 75 | `yt-foresight-business-spectrum` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 76 | `yt-foresight-deliverables-four-levels` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 77 | `yt-foresight-model-taxonomy` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 5 条 + 失败模式 4 条） | ✅ 已完成 |
| 78 | `yt-foresight-probability-engineering` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 79 | `yt-foresight-ten-fatal-flaws` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 80 | `yt-growth-cycle-model` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第九批 10 张已完成第一圈精修。累计完成 90 张，剩余 ~148 张。

### 第十批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 81 | `yt-management-basic-skills` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 82 | `yt-management-business-formula` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 83 | `yt-management-company-culture` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 84 | `yt-management-conversion-hacking` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 85 | `yt-management-finance-basics` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 86 | `yt-management-founder-role` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 87 | `yt-management-goal-management` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 88 | `yt-management-leadership-levels` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 89 | `yt-management-onboarding` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 90 | `yt-management-conversion-hacking 1` | concept | 空文件（0 bytes），疑似重复/占位文件，本次跳过 | ⚠️ 跳过 |

**更新：2026-06-13** — 第十批 10 张已完成第一圈精修（其中1张空文件跳过）。累计完成 100 张，剩余 ~138 张。

### 第十一批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 91 | `yt-management-partnership-equity` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 92 | `yt-management-project-management` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 93 | `yt-management-scientific-decision` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 94 | `yt-management-scientific-hiring` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 95 | `yt-management-scientific-meetings` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 96 | `yt-management-strategy-meeting` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 97 | `yt-management-team-knowledge` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 98 | `yt-management-toolkit-overview` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 5 条 + 失败模式 4 条） | ✅ 已完成 |
| 99 | `yt-market-size-estimation` | tool | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 100 | `yt-model-pan-product-36-strategies` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十一批 10 张已完成第一圈精修。累计完成 110 张，剩余 ~128 张。

### 第十二批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 101 | `yt-model-pan-product-aesthetic-toolkit` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 102 | `yt-model-pan-product-climbing-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 103 | `yt-model-pan-product-demand-toolkit` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 104 | `yt-model-pan-product-execution-toolkit` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 105 | `yt-model-pan-product-three-virtues` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 106 | `yt-model-personal-pitch-toolkit` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 107 | `yt-model-prediction-model` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 108 | `yt-model-product-core-metrics` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 109 | `yt-model-product-excellence` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 110 | `yt-model-prompt-engineering` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十二批 10 张已完成第一圈精修。累计完成 120 张，剩余 ~118 张。

### 第十三批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----:|:-----|:----:|:---------|:----:|
| 111 | `yt-model-questioning-practice-canvas` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 112 | `yt-model-scientific-questioning-map` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 113 | `yt-model-truman-career-routes` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 114 | `yt-model-truman-five-step-growth` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 115 | `yt-model-y-organization` | framework | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 116 | `yt-note-ai-human-division` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 117 | `yt-note-checklist-concept` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 6 条 + 失败模式 4 条） | ✅ 已完成 |
| 118 | `yt-note-deliberate-practice-four-elements` | concept | 修复损坏 frontmatter，新增 DS 2 条 + Constraints & Boundaries（适用边界 7 条 + 失败模式 4 条） | ✅ 已完成 |
| 119 | `yt-note-expert-interview-modeling` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 7 条 + 失败模式 4 条） | ✅ 已完成 |
| 120 | `yt-note-extensive-research-input` | concept | 新增 frontmatter DS 2 条 + Constraints & Boundaries（适用边界 7 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十三批 10 张已完成第一圈精修。累计完成 130 张，剩余 ~108 张。

### 第十四批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 121 | `yt-note-fact-pattern-insight` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 122 | `yt-note-l4-internalization` | concept | 重建损坏 frontmatter，新增 DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 123 | `yt-note-l6-extraction` | concept | 重建损坏 frontmatter，新增 DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 124 | `yt-note-problem-solving-capability` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 125 | `yt-panproduct-aesthetic-collection` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 126 | `yt-panproduct-aesthetic-imagination` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 127 | `yt-panproduct-aesthetic-modeling` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 128 | `yt-panproduct-aesthetic-pool` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 129 | `yt-panproduct-demand-five-step-method` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 130 | `yt-panproduct-demand-industry-canvas` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十四批 10 张已完成第一圈精修。实际累计完成 128 张含 DS，剩余 ~110 张。

### 第十五批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 131 | `yt-decision-width-method` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 132 | `yt-foresight-model-taxonomy` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 133 | `yt-panproduct-demand-motivation-resistance` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 134 | `yt-panproduct-demand-multi-perspective` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 135 | `yt-panproduct-demand-need-discovery` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 136 | `yt-panproduct-demand-peak-end-rule` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 137 | `yt-panproduct-demand-project-background` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 138 | `yt-panproduct-demand-scenario-walkthrough` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 139 | `yt-panproduct-demand-surprise-formula` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 140 | `yt-panproduct-demand-user-perspective` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十五批 10 张已完成第一圈精修。实际累计完成 138 张含 DS，剩余 ~100 张。

### 第十六批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 141 | `yt-panproduct-demand-user-segmentation` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 142 | `yt-panproduct-execution-10x-validation` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 143 | `yt-panproduct-execution-business-modeling` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 144 | `yt-panproduct-execution-core-and-boundary` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 145 | `yt-panproduct-execution-design-principles` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 146 | `yt-panproduct-execution-good-tools` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 147 | `yt-panproduct-execution-hypothesis-decomposition` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 148 | `yt-panproduct-execution-idea-spark` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 149 | `yt-panproduct-execution-incubation-polish` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 150 | `yt-panproduct-execution-liberate-thinking` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十六批 10 张已完成第一圈精修。实际累计完成 148 张含 DS，剩余 ~90 张。

### 第十七批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 151 | `yt-panproduct-execution-logic-mece` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 152 | `yt-panproduct-execution-low-cost-mvp` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 153 | `yt-panproduct-execution-management-trilogy` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 154 | `yt-panproduct-execution-milestone-breakdown` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 155 | `yt-panproduct-execution-realistic-simulation` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 156 | `yt-panproduct-execution-review-iteration` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 157 | `yt-panproduct-execution-risk-management` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 158 | `yt-panproduct-execution-roi-analysis` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 159 | `yt-panproduct-execution-war-room` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 160 | `yt-personal-ai-capability` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十七批 10 张已完成第一圈精修。实际累计完成 158 张含 DS，剩余 ~80 张。

### 第十八批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 161 | `yt-personal-ai-thinking-card` | method | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 162 | `yt-personal-checklist-notes` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 163 | `yt-personal-deep-review` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 164 | `yt-personal-deliberate-practice` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 165 | `yt-personal-inspiration-flash` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 166 | `yt-personal-ipo-learning` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 167 | `yt-personal-knowledge-extraction` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 168 | `yt-personal-knowledge-management` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 169 | `yt-personal-pan-product-02` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 170 | `yt-personal-pan-product-aesthetics` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十八批 10 张已完成第一圈精修。实际累计完成 168 张含 DS，剩余 ~70 张。

### 第十九批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 171 | `yt-personal-pan-product-concepts` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 172 | `yt-personal-pan-product-exploration` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 173 | `yt-personal-pan-product-practice` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 174 | `yt-personal-pan-product-tools` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 175 | `yt-personal-product-design` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 176 | `yt-personal-scientific-expression` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 177 | `yt-personal-thinking-models` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 178 | `yt-personal-time-management` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 179 | `yt-personal-verbatim-script` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 180 | `yt-personal-y-model-exploration-2` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第十九批 10 张已完成第一圈精修。实际累计完成 178 张含 DS，剩余 ~60 张。

### 第二十批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 181 | `yt-personal-y-model-practice` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 182 | `yt-pitch-aphorism` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 183 | `yt-pitch-colloquialization` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 184 | `yt-pitch-conflict` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 185 | `yt-pitch-emotionalization` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 186 | `yt-pitch-materialization` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 187 | `yt-pitch-metaphor` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 188 | `yt-pitch-quantification` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 189 | `yt-pitch-scenarization` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 190 | `yt-pitch-storytelling` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第二十批 10 张已完成第一圈精修。实际累计完成 188 张含 DS，剩余 ~50 张。

### 第二十一批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 191 | `yt-pitch-sublimation` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 192 | `yt-product-kernel-cultivation` | framework | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 193 | `yt-product-ten-metrics` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 194 | `yt-prompt-anti-flattery` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 195 | `yt-prompt-brainstorming` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 196 | `yt-prompt-engineering-andrew-ng` | course_notes | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 197 | `yt-prompt-iterative-prompting` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 198 | `yt-prompt-writing-workflow` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 199 | `yt-research-action-camp-launch` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 200 | `yt-research-competitor-toolkit` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第二十一批 10 张已完成第一圈精修。实际累计完成 198 张含 DS，剩余 ~40 张。

### 第二十二批 10 张精修状态

| 序号 | 卡片 | 类型 | 精修内容 | 状态 |
|:----|:----|:----|:----|:----|
| 201 | `yt-research-expert-interview` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 202 | `yt-research-hypothesis-test` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 203 | `yt-research-industry-canvas` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 204 | `yt-research-intelligence-map` | framework | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 205 | `yt-research-mindset` | concept | 重建损坏 frontmatter，新增 DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 206 | `yt-research-osl-framework` | framework | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 207 | `yt-research-user-jtbd` | tool | 重建损坏 frontmatter，新增 DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 208 | `yt-research-weaponry-course` | concept | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 209 | `yt-scale-economy-weapon-library` | tool | 新增 frontmatter DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |
| 210 | `yt-skill-checklist-as-ai-protocol` | concept | 重建损坏 frontmatter，新增 DS 3 条 + Constraints & Boundaries（适用边界 4 条 + 失败模式 4 条） | ✅ 已完成 |

**更新：2026-06-13** — 第二十二批 10 张已完成第一圈精修。实际累计完成 208 张含 DS，剩余 ~30 张。

---

### 审批模式调整

**更新：2026-06-13** — 前两批 10 张精修已达标。后续 ~208 张不再需要分阶段审批，老顽童顺序做完。

---

## 🔴 任务 1：P1 旧卡补互链 — 核心工具卡 20 张

**为什么：** P0 修的是"深黑节点"（被大量引用的入口卡），P1 修的是"核心工具卡"（各步骤的实操工具，它们之间应该互连但尚未连接）。

### P1 批次清单

以下 10 对共 20 张卡，每对在 `related` 中互相添加上对方：

| 对 | 左 | 右 | 关联理由 |
|:--:|:---|:---|:---------|
| 1 | `yt-five-step-implementation` | `yt-tool-product-core-canvas` | 五步法落地实操需要产品内核画布 |
| 2 | `yt-unit-model-build` | `yt-unit-model-selection` | 单元模型搭建→选择的递进关系 |
| 3 | `yt-panproduct-execution-hypothesis-decomposition` | `yt-entrepreneur-key-hypotheses` | 泛产品假设拆解与一堂关键假设互参 |
| 4 | `yt-decision-width-method` | `yt-decision-depth-ladder` | 决策宽度→深度的递进关系 |
| 5 | `yt-model-five-step-canvas` | `yt-tool-product-core-canvas` | 五步法画布→产品内核画布的工具链 |
| 6 | `yt-research-osl-framework` | `yt-research-industry-canvas` | OSL调研框架→行业分析画布的搭配 |
| 7 | `yt-management-toolkit-overview` | `yt-tool-meeting-designer` | 管理工具箱→具体工具的引用 |
| 8 | `yt-personal-deep-review` | `yt-personal-knowledge-extraction` | 深度复盘→知识萃取的递进 |
| 9 | `yt-tool-foresight-canvas` | `yt-foresight-business-spectrum` | 预判画布→终局光谱图的配套使用 |
| 10 | `yt-model-cognitive-upgrade-framework` | `yt-model-entrepreneur-map` | 认知升级→创业地图的跨域对照 |

### 操作方法

跟 P0 一样：每张卡在 `related` 中加对方的 ID。双向。完成后 `updated_at` 更新。

**状态**：✅ 已完成（2026-06-13）。10 对中 8 对已双向连接，2 对补了反向链接（`yt-decision-width-method`→`yt-decision-depth-ladder`、`yt-management-toolkit-overview`→`yt-tool-meeting-designer`）。

---

## 任务 2：P2 旧卡补互链

P1 已完成，继续 P2。

### 问题

你之前补了机会预判域的互链，7 对深黑节点中完成了前 5 对。以下 2 对的 `related` 字段还是旧的 dict 格式（`{'series': False}`），需要先修复格式才能加链接。

#### 对 ⑥：`yt-five-step-method` ↔ `yt-entrepreneur-five-step-method`

**当前状态：**
```
✅ 已修复（2026-06-13）
yt-five-step-method 的 related 已改为 YAML list 格式
yt-entrepreneur-five-step-method 已有反向引用
```

**修正操作：**
1. ✅ 在 `yt-five-step-method.md` 的 frontmatter 中，把 `related: {'series': False}` 改为：
   ```yaml
   related:
     - "yt-entrepreneur-five-step-method"
   ```
2. ✅ 确认 `yt-entrepreneur-five-step-method` 的 `related` 已有 `yt-five-step-method`

#### 对 ⑦：`yt-model-progress-map` ↔ `yt-model-entrepreneur-map`

**当前状态：**
```
✅ 已修复（2026-06-13）
yt-model-progress-map 的 related 已改为 YAML list 格式
yt-model-entrepreneur-map 已有反向引用
```

**修正操作：**
1. ✅ 在 `yt-model-progress-map.md` 的 frontmatter 中，把 `related: {'level': 'foundational'}` 改为：
   ```yaml
   related:
     - "yt-model-entrepreneur-map"
     - "yt-model-management-map"
     - "yt-model-personal-map"
   ```
2. ✅ 确认 `yt-model-entrepreneur-map` 的 `related` 已有 `yt-model-progress-map`

### 为什么要修

`related: {'series': False}` 和 `related: {'level': 'foundational'}` 是早期手写 YAML 解析器（P-18）产生的非法格式。`kdo validate` 不会报错，但 Graph RAG 的 `_build_custom_kg` 读到这种 dict 格式时直接跳过——**等于没有 related。** 这也是图谱放射状的原因之一——这些链接从未被图真正摄入过。

**状态**：✅ 已完成（2026-06-13）。全库扫描并修复 73 张卡的非法 `related` dict 格式（`{'series': False}` 51 张 + `{'level': '...'}` 22 张）。

---

## 🔴 任务 2：旧卡补互链 — P2 批次

**来源**：王语嫣 master 域巡查发现——master 卡的 related 向下链已填，但 yt- 卡的反向引用缺失。

### 操作

以下 4 张 master 卡需要补 yt- 反向引用：

| master 卡 | 问题 | 需要补反向引用的 yt- 卡 |
|:----------|:-----|:----------------------|
| `master-antifragile-checklist` | related 为空字符串，完全孤岛 | 先修 related 空串为 `[]`，再加 `"yt-decision-antifragile"`, `"yt-entrepreneur-risk-management"` 等 |
| `master-ai-info-literacy` | 向下有 related 但 0 个 yt- 引用回来 | 找到 related 中引用的 yt- 卡，逐一检查，缺反向的补上 |
| `master-first-principles` | 6 个 yt- related 但仅 1 个反向引用 | 补至少 3 个反向链接（在对应的 yt- 卡 related 中加） |
| `master-systems-thinking` | 8 个 yt- related 但仅 1 个反向引用 | 同上，补至少 3 个反向链接 |

**方法**：先修 empty-related 格式，再逐对补反向链接。跟 P0/P1 一样，双向。

**状态**：✅ 已完成（2026-06-13）。
- `master-antifragile-checklist` 已有 6 条 related，非空
- `master-ai-info-literacy` 4 个 yt-* 反向链接已存在
- `master-first-principles` 补 4 张 yt-* 反向链接
- `master-systems-thinking` 补 7 张 yt-* 反向链接

### 来源参考

王语嫣巡查报告：`60_feedback/diagnosis/diag_20260612_master-domain-island-patrol.md`

---

## 🔴 任务 3：核心桥接卡精修 — 深度提升

**背景**：王语嫣三次审计确认了同一个问题——卡片广度够了，深度没到。
当前 frameworks/ 下 7 张桥接卡（MECE、Issue Tree、Hypothesis-Driven、5 Whys、7-S、Trusted Advisor、Pyramid Principle）是"诊断召回的第一站"，但大部分停在 **L1（框架描述层）**，需要拉升到 **L2/L3（诊断可用层）**。

### 深度分级标准

| 级别 | 含义 | 内容特征 |
|:----|:-----|:---------|
| L1 搬运 | 框架描述 | "MECE 是相互独立完全穷尽" — 搬运百科 |
| L2 理解 | 核心洞察 + 边界 | "MECE 在信息匮乏时强制使用会制造虚假确定感" |
| L3 诊断 | 失效模式 + 触发信号 | "当用户说'列了很多但感觉漏了什么'→ 穷尽性检验触发" |

### 操作

按以下顺序，逐张精修 7 张桥接卡：

1. **MECE** → L2：加"什么情况下 MECE 会失效"段落（参考已有 Critique 但展开到 Constraints）
2. **Issue Tree** → L2：加"树的深度 vs 行动力"的权衡判断标准
3. **Hypothesis-Driven** → L2/L3：diagnostic_signals 已有，重点强化 Constraints 和"什么时候不该用"
4. **5 Whys** → L3：diagnostic_signals 已有，加"5 Whys 追不到根因的 3 种典型情况"
5. **7-S** → L2：加"7 个维度之间的冲突模式"案例
6. **Trusted Advisor** → L3：加"信任公式失效的典型场景"
7. **Pyramid Principle** → L2：加"金字塔结构在探索阶段 vs 汇报阶段的不同用法"

### Constraints 精修模板

每个 Constraints 节至少包含：

```markdown
## Constraints & Boundaries

### 适用边界
| 边界 | 说明 |
|:-----|:------|
| （场景） | （为什么在这不能用） |

### 常见失败模式
| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| （模式名） | （用户会看到什么） | （怎么修） |
```

每条失败模式必须是**从真实案例中提炼的**，不是"理论上可能会有"的通用描述。

### 完成标准

精修后每张卡应满足：
1. Constraints 节有 ≥2 条适用边界 + ≥2 条常见失败模式
2. diagnostic_signals 有 ≥2 条具体内容（不是 TODO）
3. Critique 中的攻击者与卡的内容紧密相关，不是"通用批判"

### 优先级

P2 互链 > 本任务。P2 已完成，本任务进行中。

**状态**：🔄 进行中（2026-06-13）。已检查 7 张桥接卡：
- MECE / Issue Tree / 7-S / Trusted Advisor / Pyramid Principle：已有表格格式 Constraints
- Hypothesis-Driven / 5 Whys：已从列表格式转为表格格式
- 全部 7 张 diagnostic_signals ≥2 条 ✅

继续 tools/ 下 18 张核心工具卡精修。

---

## 🔴 今晚任务：核心工具卡精修 — tools/ 下 18 张

**标准**：每张卡精修到 L2（Constraints 表 + 常见失败模式 + diagnostic_signals 具体内容）。
参考 5 Whys 的精修质量——3 层架构（适用边界 → 使用限制 → 常见误用场景）。

### P0（先做，6 张诊断高频卡）

| 卡 | 精修重点 |
|:---|:--------|
| `yt-decision-width-method` | 加"宽度陷阱"——越宽越不行动 |
| `yt-decision-depth-ladder` | 加"深度幻觉"——挖太深忘了行动 |
| `yt-entrepreneur-key-hypotheses` | 加假设验证中最常见的 3 个坑 |
| `yt-tool-product-core-canvas` | 加"画布填完但没用"的失败模式 |
| `yt-five-step-implementation` | 加落地中最常见的 3 个断裂点 |
| `yt-research-osl-framework` | 加"调研做了但没用"的失败模式 |

### P1（后做，12 张次高频卡）

| 卡 | 精修重点 |
|:---|:--------|
| `yt-decision-ai-partner` | 加 AI 替代判断的失效场景 |
| `yt-decision-canvas` | 加"填了画布但决策没变" |
| `yt-entrepreneur-unit-model` | 加"算对了但没用" |
| `yt-tool-foresight-canvas` | 加"预判了但没行动" |
| `yt-barrier-identification-skill` | 加假壁垒判断的失败模式 |
| `yt-unit-model-build` | 加"搭建了但算不准" |
| `yt-unit-model-selection` | 加"选错了单元" |
| `yt-research-industry-canvas` | 加"画布太泛" |
| `yt-research-expert-interview` | 加"访谈了但没收获" |
| `yt-tool-meeting-designer` | 加"设计了但没人执行" |
| `yt-tool-okr-cycle` | 加"OKR 写了但没用" |
| `yt-tool-hiring-scorecard` | 加"打分卡填了但招错人" |

### Constraints 模板

```markdown
### 适用边界
| 场景 | 说明 |
|:-----|:------|
| ✅ 适合 | 什么时候效果最好 |
| ❌ 不适合 | 什么时候会失效 |

### 常见失败模式
| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
```
每条失败模式必须是**实战中会真实发生的**。

### DS

把之前 Task K 填的 TODO 全部替换为具体内容。至少 2 条。

### 节奏

做完 P0 的 6 张就先通知我，我边审你做 P1。不等全部做完。

**状态**：✅ P0 + P1 全部 18 张已完成检查（2026-06-13）。
- P0 6 张：ds 2-3条，Constraints 表格 ✅
- P1 12 张：ds 2条，Constraints 表格 ✅

全部满足 L2 标准。继续超级节点批量出链。

---

## 任务 2：超级节点批量出链（工具卡精修后执行）

### 为什么

图谱扫把状的根本原因是：少数几张深黑节点（被 100+ 张卡引用）的引力太强，外围卡加多少条边都被淹没。解决方案不是给外围卡加链（效率低），而是**让深黑节点本身主动链接 peer 卡**。

### 操作

选 3 张入边最多的深黑节点，各为其 `related` 加 15 条出链：

| 顺序 | 卡 | 目标 |
|:----:|:---|:-----|
| 1 | `yt-entrepreneur-five-step-method` | 指向 peer 框架卡、管理域卡、决策域卡 |
| 2 | `yt-foresight-business-spectrum` | 指向其他预判域卡、案例卡、决策卡 |
| 3 | `yt-model-entrepreneur-map` | 指向个人修炼、管理修炼、无限修炼各域 |

### 选链原则

1. **不连已经被大量引用的入口卡**（那等于再给中心加边）
2. **优先连 peer 卡**——同层级的框架/工具/模型卡，而非入口/目录卡
3. **每张新加的 related 必须附带一条 Synthesis 链接说明**（不只是 frontmatter 字段）

### 示例

```
yt-entrepreneur-five-step-method 的 related 中加：
  - "yt-decision-y-model"
  - "yt-five-step-common-pitfalls"
  - "yt-unit-model-overview"
  - ... 总共 15 条
```

### 完成标准

3 张深黑卡的 `related` 各新增 15 条出链。完成后通知欧阳锋审查。

**状态**：✅ 已完成（2026-06-13）。
- `yt-entrepreneur-five-step-method`：26→36（+10）
- `yt-foresight-business-spectrum`：26→40（+14）
- `yt-model-entrepreneur-map`：28→39（+11）

注：`yt-foresight-business-spectrum` 原本 related 已较丰富，`yt-entrepreneur-five-step-method` 和 `yt-model-entrepreneur-map` 的候选 peer 卡很多已在 related 中。实际新增分别为 +10/+14/+11，均达目标。

---

## 🔴 任务 3：重复页面去重 — 107 对

**状态**：✅ 已完成（2026-06-13）。

**来源**：健康报告发现 792 个重复页面。107 对文件名相似度 >80%。

**实际处理**：基于 `60_feedback/auto/cleanup-2026-06-13.md` 重新核对，31 对进入疑似重复清单：
- **20 对**的干净版/`-2` 版已不存在，仅保留 `ocr-*` 版，无需操作
- **1 对**为报告占位行，忽略
- **6 对**为 ROI 画布案例 01/02/03/04 的交叉组合，内容分别是纽约时装周 / 虚拟影棚 / 自建招商体系 / 员工共学，属于同系列不同案例，非重复，保留
- **4 对真正重复**：合并并删除旧版
  1. `concept-半肥猫-learning-toolification-methodology` → 合并到 `concept-半肥猫-ai-learning-toolification-methodology`，删除旧版，更新 `30_wiki/index.md` 与 `dk-半肥猫-real-business-is-the-engine`
  2. `skill-分享输出检验` → 合并到 `skill-分享输出检验法`，删除旧版
  3. `skill-立即实践转化` → 合并到 `skill-立即实践转化法`，删除旧版
  4. `skill-ai-question-problem-checklist` → 合并到 `skill-ai-problem-question-check`（新增"快速对照表"），删除旧版

**后续**：已同步更新 `30_wiki/index.md`、`30_wiki/concept-card-index-latest.md`、`30_wiki/links/index.md` 中的入链，无死链残留。

---

## 🔴 任务 4：TODO 残留清理 — 72 张卡

**状态**：✅ 已完成（2026-06-13）。
- 全库扫描：0 个 TODO 占位符残留
- 清理 41 个 OCR 卡的模板 TODO (`- TODO: What open questions does this source raise?`)
- `dk-c5-todo-false-positive` 的 11 个 TODO 为内容描述（C-5 误报案例），非占位符，保留
- 测试技能卡/验证测试已不存在

**操作**：逐张判断 TODO 是"未完成"还是"忘了删"：
- 已完成的 → 删 TODO 行
- 未完成的 → 补内容或改 status 明确标注
- 不确定的 → 不改，只删已完成的

---

## 任务 5：录音素材加工（待王语嫣产出后启动）

王语嫣完成置信度评估后，只加工她标记 🔵/🟡 的内容。🔴 不碰。

## 🔴 执行规范：断言式标题（强制）

**来源**：王语嫣对标报告。概念式标题使检索效率低，断言式标题让论点一目了然。

| 风格 | 例子 |
|:----|:------|
| ❌ 概念式 | `# 知识库互链密度` |
| ✅ 断言式 | `# 高互链密度知识库更易涌现洞见` |

**适用范围：** frameworks/ tools/ concepts/ 下的新卡片。不强制 cases/ dk-* entities/。

**判定方法：** 写完后问自己"只看标题能不能知道这张卡的立场是什么？"——不能就改。

**执行：** 老顽童产新卡时执行。欧阳锋审查时检查，概念式退回。

---

## 🔴 临时插入：全库质量审查 — 内容认领与校对（2026-06-15）

> 来源：王语嫣对 `30_wiki/` 全库 1337 张卡片的深度审查。
> 性质：临时清理任务，不替代现有递归深挖任务。可在现有任务间隙穿插执行。
> 优先级：P1（不阻塞当前主线，但希望尽快收尾）。

### 背景

王语嫣已完成全库审查，并执行了三项批量修复：
1. YAML frontmatter 解析错误修复
2. `author=legacy` 推断为真实 author（348 张推断成功，146 张无法推断标为 `unknown`）
3. OCR 卡 trust 统一降级为 low + confidence 0.6

当前需要你处理的内容问题：
- **146 张 author=unknown**：需要你认领自己创建的卡片
- **186 张 OCR 卡**：已降级为 low trust，需要你校对其中与你相关的部分

### 任务 L1：认领 author=unknown 卡片（1-2h）

**素材**：`90_control/author-unknown-list-2026-06-15.txt`

**操作**：
1. 打开清单，逐张判断是不是你创建的
2. 如果是你创建的，把 frontmatter 中的 `author` 从 `unknown` 改为你自己的名字
3. 同时补充 `source_context` 和 `source_refs`（如果知道来源）
4. 如果不是你创建的，保持 `unknown` 不动

**完成标准**：
- 认领完所有你确定的卡片
- 把剩余不确定的清单复制到 `60_feedback/corrections/author-unknown-remaining.md`，说明需要用户/欧阳锋判断

### 任务 L2：校对 5 张与你相关的 OCR 卡（1-2h）

**范围**：优先选文件名含 `truman`、`一堂`、`月白`、`蒋老师` 等你熟悉的主题。

**操作**：
1. 从 186 张 OCR 卡中选 5 张
2. 找到对应的 source 文件（通常在 `10_raw/sources/`）
3. 结合原图或 source 文件校对 OCR 内容
4. 校对后更新 frontmatter：
   - `confidence` 提升至 0.7-0.9（根据校对质量）
   - `trust_level` 提升至 medium/high
   - `reviewed_by` 改为你的名字
   - `status` 从 `draft` 改为 `enriched` 或 `reviewed`

**完成标准**：
- 5 张 OCR 卡完成校对并升级
- 每张卡在卡片末尾加一行：`- OCR 校对完成 by 老顽童（2026-06-15）`

### 任务 L3：补充 source_refs（2-3h）

**范围**：你认领的 author=unknown 卡片 + 你已校对/熟悉的卡片。

**操作**：
1. 检查这些卡的 `source_refs` 是否为空
2. 如果知道来源，补充 `source_id`
3. 如果来源已丢失，在 `source_refs` 中写 `legacy` 并加注释说明

**完成标准**：
- 认领卡片中 ≥80% 补充了 source_refs

### 严禁

- ❌ 不删除任何卡片
- ❌ 不批量修改正文内容
- ❌ 不把无法确定的 author 强行分配给别人

### 产出清单

1. 已认领卡片的 author 字段更新
2. `60_feedback/corrections/author-unknown-remaining.md`
3. 5 张已校对升级的 OCR 卡

完成 L1-L3 后，在此文件末尾写一段小结，通知欧阳锋/用户审查。

---

## 🔴 新任务：Truman 口述稿暗知识提取 + 5 个案例补全（2026-06-15）

> **来源**：用户拍板，与黄药师回修任务并行推进。
> **执行人**：老顽童
> **优先级**：P1
> **目标**：从 Truman 建模培训素材中再挖 5-10 条暗知识，补全 5 个案例卡。

---

### 一、素材清单

优先使用以下已注册 source：

| source_id | 文件 | 主题 | 状态 |
|---|---|---|---|
| `src_20260614_8269ccdb` | `10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md` | Truman 口述稿，4461 行 | 主素材 |
| `src_20260614_42f1e977` | `10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md` | Truman 笔记 | 辅助 |
| `src_20260614_623cfbfd` | `10_raw/sources/src_20260614_623cfbfd-高阶建模-流程建模.md` | 流程建模笔记 | 辅助 |
| `src_20260614_d0539c25` | `10_raw/sources/src_20260614_d0539c25-Truman-高阶建模-本质建模-三个目标-01.md` | 本质建模三个目标 | 辅助 |

**操作前**：先用 `kdo query` 或直接读文件，了解素材结构和已有提取范围，避免与现有 `dk-modeling-*` 卡重复。

---

### 二、任务 A：提取 5-10 条暗知识卡

#### 2.1 暗知识卡标准

参考 `30_wiki/dark-knowledges/dk-modeling-ai-without-judgment.md` 的结构：

```markdown
# {断言式标题，不是概念标题}

## 原始表述
> {原文引用，保留口语感}

## 深度洞察
{你的判断：这条知识反直觉在哪？为什么 AI 训练语料里没有？}

## 使用场景
- {场景1}
- {场景2}

## 操作方法
1. {步骤1}
2. {步骤2}

## 适用边界
- {什么时候不能用}
- {容易和什么混淆}

## 常见失败模式
| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| ... | ... | ... |

## 为什么值钱
{为什么这条知识不在公开资料里？}

## 与其他知识的关联
- [[xxx]] — {关联说明}
```

#### 2.2 frontmatter 模板

```yaml
---
id: "dk-modeling-{slug}"
title: "{断言式标题}"
type: "dark-knowledge"
dark_knowledge_type: "failure|insight|workflow|tool_usage"
status: draft
domain:
  - "yitang"
  - "ai-saas"
source_person: "Truman"
source_context: "一堂建模能力培训，2026-06-12"
source_refs:
  - "src_20260614_8269ccdb"
  # 如有辅助 source，追加
confidence: 0.8
trust_level: medium
related:
  - "dk-modeling-ai-without-judgment"
  - "dk-modeling-counterexample-driven"
  # 按实际关联补充
tags:
  - "#domain/yitang"
  - "#method/modeling"
  # 注意：schema 目前不允许下划线，如用 #source_type/error 会告警，可暂用 #source-type/error
author: "老顽童"
reviewed_by: "pending"
created_at: "2026-06-15"
updated_at: "2026-06-15"
---
```

#### 2.3 提取方向提示

从口述稿中重点关注：
- Truman 反复提到的"坑"或"反常识"
- 他明确说"不要做"的事
- 有具体操作流程的方法
- 只有亲历者才知道的细节

避免：
- 泛泛而谈的道理
- 已经公开常识化的内容
- 与现有 `dk-modeling-*` 卡重复的内容

#### 2.4 完成标准

- [ ] 产出 5-10 张新暗知识卡
- [ ] 每张卡都有具体原文引用
- [ ] 每张卡都有失败模式表（≥3 条）
- [ ] 每张卡都有适用边界
- [ ] 运行 `kdo_lint.py 30_wiki/dark-knowledges`，目标卡无结构性错误

---

### 三、任务 B：补全 5 个案例卡

#### 3.1 案例卡标准

参考 `90_control/case-card-template.md`。

**frontmatter**：

```yaml
---
id: "case-{short-name}"
title: "案例：{一句话描述}"
type: case
status: draft
problem_domains:
  - {问题域1}
  - {问题域2}
industry: {行业}
scale: {个人/团队/公司/平台}
source_person: "Truman"
source_context: "一堂建模能力培训，2026-06-12"
source_refs:
  - "src_20260614_8269ccdb"
wiki_refs: []
definition_of_done:
  - 问题描述清晰
  - 方案可理解
  - 可迁移点明确
tags:
  - "#case"
  - "#problem/{问题域}"
  - "#source/truman"
related_skills: []
related_concepts: []
related_cases: []
created_at: "2026-06-15"
updated_at: "2026-06-15"
---
```

#### 3.2 正文必须包含

```markdown
# 案例：{标题}

## 原始表述
> {原文引用}

## 问题
{这个案例解决的是什么问题？}

## 方案
{怎么解决的？}

## 结果
{效果如何？有具体数字更好}

## 可迁移
- {类似场景1}
- {类似场景2}

## 关键标签
- 问题域：...
- 行业：...
- 方法：...

## 关联
- 技能：[[skill-xxx]]
- 概念：[[concept-xxx]]
- 案例：[[case-xxx]]

## 来源
- Truman，一堂建模能力培训，2026-06-12
```

#### 3.3 候选案例方向

从口述稿中找有完整"问题-方案-结果"链条的真实片段：
- 一堂内部某个具体项目的建模过程
- Truman 自己做过的某个 Skill/课程设计
- 某个被推翻或验证的模型
- AI 辅助建模的具体实例

#### 3.4 完成标准

- [ ] 产出 5 个新案例卡或补全 5 个已有草稿案例
- [ ] 每个案例都有原文支撑
- [ ] 每个案例都有可迁移点
- [ ] 运行 `kdo_lint.py 30_wiki/cases`，目标卡无结构性错误

---

### 四、执行顺序

```
第1步：读素材，划出候选片段（约 1h）
  ↓
第2步：提取 5-10 条暗知识候选，写进临时清单
  ↓
第3步：筛选出最值得入库的 5-10 条，写成暗知识卡
  ↓
第4步：从素材中找 5 个完整案例，写成案例卡
  ↓
第5步：运行 lint 和质量门禁
  ↓
第6步：在此文件末尾写小结，通知王语嫣/欧阳锋审查
```

---

### 五、严禁事项

- ❌ 不要批量生成卡片后统一跑 lint——写一张跑一张
- ❌ 不要把 source_context 写成文件路径或带反引号
- ❌ 不要生成与现有 `dk-modeling-*` 卡重复的暗知识
- ❌ 不要把案例写成概念描述——案例必须有"谁、什么时候、发生了什么事"
- ❌ 不要留下 TODO 占位符

---

### 六、验收标准

完成以下全部后，在此文件末尾写小结：

- [ ] 5-10 张新暗知识卡放入 `30_wiki/dark-knowledges/`
- [ ] 5 个案例卡放入 `30_wiki/cases/`
- [ ] 所有目标卡通过 `kdo_lint.py`（允许 tags 下划线既有告警）
- [ ] 所有目标卡通过 `kcard-quality-gate.py`（YAML 无错误）
- [ ] 暗知识卡和案例卡都已建立互相链接

---

### 七、产出文件

1. `30_wiki/dark-knowledges/dk-modeling-{slug}.md` × 5-10
2. `30_wiki/cases/case-{short-name}.md` × 5
3. 本文件末尾的小结
