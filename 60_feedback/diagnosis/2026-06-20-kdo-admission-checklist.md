---
id: "admission_20260620_yitang_research"
title: "准入清单：一堂调研方法论课程体系"
type: "admission_checklist"
created_at: "2026-06-20"
diagnostician: "wangyuyan"
reviewer: "ouyangfeng (pending)"
---

# KDO 准入清单：一堂调研方法论

**诊断编号**：diag_20260620_yitang_research_methodology
**素材**：`00_inbox/调研专题/`
**诊断日期**：2026-06-20

---

## 🟢 建议放行（6项）— 高置信度，直接入库

| # | 卡片名称 | 类型 | 置信度 | 入库路径 | 理由 |
|:--|:---------|:----|:------:|:---------|:-----|
| A1 | `framework-yitang-oscar-research-5step` | framework | 0.80 | `30_wiki/frameworks/` | OSCAR五步法：4源交叉验证，8年持续迭代，方法论核心 |
| A2 | `framework-yitang-three-layer-intelligence` | framework | 0.80 | `30_wiki/frameworks/` | 三层信息挖掘：2源+具备结构可验证性 |
| A3 | `framework-yitang-nine-intelligence-sources` | framework | 0.80 | `30_wiki/frameworks/` | 九大信息源模块：2源交叉验证，框架清晰可操作 |
| A4 | `concept-ai-assisted-research-workflow` | concept | 0.80 | `30_wiki/concepts/` | AI辅助调研全流程：口述+图中均有体现 |
| A5 | `concept-research-fact-over-opinion` | concept | 0.80 | `30_wiki/concepts/` | 多问事实少问观点：用户调研+行业报告双源验证 |
| A6 | `framework-doris-industry-report-4step` | framework | 0.80 | `30_wiki/frameworks/` | 行业报告四步法：Doris口述+笔记双源验证 |

## 🟡 待审核（4项）— 需补充验证后放行

| # | 卡片名称 | 类型 | 置信度 | 入库路径 | 需补充 |
|:--|:---------|:----|:------:|:---------|:-------|
| B1 | `framework-yitang-four-research-directions` | framework | 0.70 | `30_wiki/frameworks/` | 四种调研方向分类完备性需要更多独立案例验证 |
| B2 | `framework-yitang-research-weapon-system` | framework | 0.70 | `30_wiki/frameworks/` | 14节点武器谱系——建议简化为8大模块，去"99.9%"修辞 |
| B3 | `framework-yitang-user-interview-5step` | framework | 0.60 | `30_wiki/frameworks/` | 用户访谈五步：需Doris口述交叉验证 |
| B4 | `framework-yitang-expert-interview-5step` | framework | 0.60 | `30_wiki/frameworks/` | 专家访谈五步：需结合Truman PDF对话补充 |

## 🔴 禁止入库（6项）— 仅归档，不入库

| # | 内容 | 置信度 | 禁止理由 |
|:--|:-----|:------:|:---------|
| C1 | OSCAR七步推理引擎(AI教练版) | 0.45 | 仅在产品设计图中出现一次，非方法论核心 |
| C2 | 双三角模型(人类×AI) | 0.45 | 仅课程图一张，缺乏多源验证 |
| C3 | AI调研报告价值层级L1-L6 | 0.45 | 仅一张图，缺乏独立验证 |
| C4 | "调研能力决定创业成败" | 0.25 | 教学营销修辞，不可证伪 |
| C5 | "十倍速公式" | 0.25 | 缺乏精确量化，为教学简化模型 |
| C6 | "行业报告解决80%创业难题" | 0.20 | 无法证伪，Doris个体经验不可推广 |

## ⚫ 绝对禁止（0项）

---

## ⚡ 矛盾追踪

| 编号 | 矛盾 | 陈述A(课程) | 陈述B(行为) | 建议处理 |
|:----|:-----|:----------|:----------|:---------|
| ⚡1 | CEO调研职责矛盾 | "CEO必须亲自做用户调研" | Truman大量委托下属/产品经理 | **不掩盖。两张独立卡片共存，标注 contradiction。** 出"方法论原教旨 vs 组织规模化现实"概念卡。欧阳锋裁决。 |

---

## 📋 操作清单（给老顽童）

### 第一批：🟢 直接写卡（6张）

```
写卡顺序：
1. framework-yitang-oscar-research-5step   → 对应素材：系统式调研口述 + OSCAR模型图
2. framework-yitang-three-layer-intelligence → 对应素材：武器库培训口述 86-130行 + 超级武器库图
3. framework-yitang-nine-intelligence-sources → 对应素材：武器库培训口述 + 超级武器库图
4. framework-doris-industry-report-4step     → 对应素材：Doris笔记 35-64行
5. concept-ai-assisted-research-workflow     → 对应素材：武器库培训口述 + AI教练图
6. concept-research-fact-over-opinion        → 对应素材：用户调研笔记 第53行 + Doris笔记 第49行
```

### 第二批：🟡 补充验证后写卡（4张）

```
等欧阳锋审批后：
7. framework-yitang-four-research-directions  → 对应素材：高阶情报口述 152-200行 + 全景策略图
8. framework-yitang-research-weapon-system    → 对应素材：武器库培训口述 174-200行
9. framework-yitang-user-interview-5step      → 对应素材：用户调研笔记 39-57行
10. framework-yitang-expert-interview-5step   → 对应素材：专家访谈口述
```

### 每张卡的必须要素

- `source_refs`：标注源文件路径（从 `00_inbox/调研专题/` ）
- `confidence`：继承本清单中的评分
- `diagnostic_signals`：统一标注 `["假设驱动", "多源信息", "结构化框架"]`
- `domain`：标为 `research-methodology`（新域）
- `related`：链接到 `yt-five-step-method-complete` 和 `concept-mckinsey-hypothesis-driven`
- 所有口述中的营销修辞需转换为客观陈述

---

## ⚠️ 特别提醒

1. **AI工具清单不要照抄**——超级武器库图中的具体工具(秘塔/ChatGPT等)60天后可能过时，应标注"截至2026年初"
2. **Truman教学风格过滤**——口述中"特别有趣""特别有成就感""终于"等情绪化表达需转为结构化陈述
3. **跨卡一致性**——OSCAR五步法在Truman口述、二舅口述、外部skill中表述略有不同，写卡时应以Truman最新版为准，差异记入脚注

---

*生成：王语嫣 · 入口质量门 · 2026-06-20*
*审核：欧阳锋 (等待中)*
