---
title: "老顽童：路演工具箱 Batch 1 — 故事化+数字化+比喻化"
assigned_to: "老顽童 (Producer)"
priority: "P1"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 老顽童：路演工具箱 Batch 1 — 故事化+数字化+比喻化

## 背景

管理工具箱（F1 + T1-T8）已全部完成 ✅，欧阳锋审查 A- ✅。

**下一域：路演工具箱（个人路演）**。该域现有：

- 框架卡：`yt-model-personal-pitch-toolkit`（个人路演工具箱总览）
- 10 张技巧卡，全部在 `30_wiki/concepts/`，`type: tool`，旧 concept 格式

与之前的单元模型域工具化相同——**格式转换 + 攻击者补全 + Synthesis**。概念内容已成熟（黄药师 enriched），不需要重写主张，只需套工具卡格式并补 Critique 攻击者。

**Batch 1 选 3 张最核心的技巧**：

| 卡 | 路径 | 核心价值 |
|:--|:-----|:---------|
| 故事化 | `yt-pitch-storytelling` | 最通用的说服技巧——"故事比道理好用十倍" |
| 数字化 | `yt-pitch-quantification` | 一锤定音型——数字让人默认"这是事实" |
| 比喻化 | `yt-pitch-metaphor` | 让复杂概念秒懂——"一比喻用户就懂了" |

---

## 前置：T6/T7/T8 善后（必须优先做，~15min）

在上次审查结果 [[task-20260528-laowantong-mgmt-toolbox-batch3]] 末尾写了 2 项顺手修：

### 1. 补 Synthesis

3 张卡 `## Critique` 与 `## Action Triggers` 之间缺 `## Synthesis`。内容参考旧 concept 版的 Synthesis 迁移：

| 卡 | 旧 Synthesis 位置 | 关键内容 |
|:--|:-----------------|:---------|
| T6 | `30_wiki/concepts/yt-tool-project-health-radar.md` L261-282 | 关联卡片 8 条 + 不要用的场景 3 条 |
| T7 | `30_wiki/concepts/yt-tool-onboarding-90day.md` L303-321 | 关联卡片 7 条 + 不要用的场景 3 条 |
| T8 | `30_wiki/concepts/yt-tool-equity-checklist.md` L323-344 | 关联卡片 8 条 + 不要用的场景 3 条 |

**做法**：从旧 concept 版复制 Synthesis 内容，适配到新工具版。关联卡片中的 wikilinks 保留，删除已不相关的条目。

### 2. 旧 concept 卡改 redirect

`30_wiki/concepts/yt-tool-{project-health-radar,onboarding-90day,equity-checklist}.md` 改为 redirect 存根：

```markdown
---
id: yt-tool-xxx
title: 'XXX'
type: tool
status: redirect
---

> 本卡已迁移至 [[30_wiki/tools/yt-tool-xxx]]。
>
> 原文内容请访问目标页面。
```

---

## Batch 1：路演工具箱 — 3 张卡

### A. 格式转换

当前格式（concept 格式，在 `30_wiki/concepts/`）：

```
## Summary
## Claims
### 定义与价值
### 四个子策略
## Constraints & Boundaries
## Critique（可能有）
## Synthesis
## Action Triggers
```

目标格式（工具格式，写入 `30_wiki/tools/`）：

```
## Summary
## 进入标准（When to Use）
## 操作步骤（Step-by-Step）
### [步骤名]
1. xxx
2. xxx
## 退出标准（When to Stop）
## Critique
### 内部局限
### 外部攻击
#### [学者] — [标题]
[2-3 句实质性论证 + 紧迫感]
## Synthesis
### 关联卡片
### 不要用的场景
## Action Triggers
```

**转换规则**：

| 旧字段 | 新位置 |
|--------|--------|
| `## Summary` | 保留 |
| `## Claims > ### 定义与价值` | 精简后移入 Summary 第二段 |
| `## Claims > ### 四个子策略` | 展开为 `## 操作步骤` |
| `## Constraints & Boundaries` | 有用的内容并入 `### 内部局限`，删除空节 |
| `## Critique`（已有内容） | 保留并检查是否需要扩展 |
| `## Synthesis` | 保留并适配 |
| `## Action Triggers` | 保留 |

### B. 补攻击者

每张 concept 卡当前缺少 `## Critique > ### 外部攻击`（或只有内部局限）。需要从相关学术/行业领域寻找攻击者：

| 技巧卡 | 建议攻击者方向（每组 2 位） |
|:------|:--------------------------|
| **故事化** | Paul Zak（神经科学——好故事触发催产素，但操纵情感有伦理边界）+ Chip Heath（《让创意更有黏性》——故事的记忆优势 vs 故事忽略数据和逻辑的陷阱） |
| **数字化** | Hans Rosling（数据素养——数字让"事实"显得权威但可能误导）+ Dan Ariely（《怪诞行为学》——数字锚定效应：听众对数字的信任可能被第一个数字操纵） |
| **比喻化** | George Lakoff（认知语言学——比喻塑造思维，但也固化偏见）+ Elisabeth Camp（隐喻哲学——比喻让复杂概念易懂但也过度简化） |

**攻击者论证要求**（参考管理工具箱的展开标准）：
- 引用学者的核心研究成果
- 说明这个攻击如何针对你的工具卡的具体主张
- 包含 1 个"紧迫感"问题——让使用者睡不着觉的那种
- 不换攻击者（选定后就固定，后续 batch 同样方向）

### C. 验证

每张卡完成后：

```bash
kdo validate --v15 --card yt-tool-pitch-storytelling
kdo validate --v15 --card yt-tool-pitch-quantification 
kdo validate --v15 --card yt-tool-pitch-metaphor
```

三张全部 PASS 后通知欧阳锋审查。

---

## 执行顺序

```
Step 1: T6/T7/T8 补 Synthesis      ← 先做，~15min
Step 2: T6/T7/T8 旧卡 redirect     ← ~5min
Step 3: pitch-storytelling 转换     ← 格式 + 攻击者
Step 4: pitch-quantification 转换   ← 格式 + 攻击者
Step 5: pitch-metaphor 转换        ← 格式 + 攻击者
Step 6: kdo validate --v15         ← 全部 PASS 后通知审查
Step 7: 文章 3 篇（见下文）       ← 从 Batch 1 A+ 卡选题
```

---

## Step 7：文章重启（Pitch Batch 1 审查通过后做）

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

## 验收

| # | 验收项 | 判定 |
|:-:|------|:----:|
| 1 | T6/T7/T8 Synthesis 已补回 | grep `## Synthesis` 各卡均有 |
| 2 | T6/T7/T8 旧 concept 卡已改为 redirect | status=redirect |
| 3 | 三张路演卡在 `30_wiki/tools/`，tool 格式完整 | 路径检查 |
| 4 | 每卡 Critique 有 2 位外部攻击者，各 ≥2 句 + 紧迫感 | 人工审查 |
| 5 | `kdo validate --v15` 全部 PASS | exit 0 |
| 6 | 不破坏已有内容（Claims 内容迁移而非删除） | diff |
| 7 | ≥3 篇文章到 `40_outputs/content/articles/`，质量门通过 | 文件存在 + 抽检 |

---

## 欧阳锋审查意见（2026-05-28）

### 验收结果

| # | 验收项 | 目标 | 实测 | 判定 |
|:-:|:------|:---:|:----:|:----:|
| 1 | T6/T7/T8 Synthesis 已补回 | grep `## Synthesis` 各卡均有 | 3 卡均有，7-8 条关联卡片 + 详细"不要用"场景 | ✅ **PASS** |
| 2 | T6/T7/T8 旧 concept 卡已改为 redirect | status=redirect | 3 卡均 redirect ✅ | ✅ **PASS** |
| 3 | 三张路演卡在 `30_wiki/tools/`，tool 格式完整 | 路径检查 | 3 卡均在，格式完整（Summary→进入标准→操作步骤→退出标准→Critique→Synthesis→Action Triggers） | ✅ **PASS** |
| 4 | 每卡 Critique 有 2 位外部攻击者，各 ≥2 句 + 紧迫感 | 人工审查 | 每卡 2 位，论证充实 + 紧迫感 | ✅ **PASS** |
| 5 | `kdo validate --v15` 全部 PASS | 0 Failed | 3 卡均 0 Failed ✅ | ✅ **PASS** |
| 6 | 不破坏已有内容 | diff | 新文件，无破坏 | ✅ **PASS** |

### 攻击者说明

任务指定攻击者与实际选用有出入，但替换合理、质量优秀：

| 卡 | 指定 | 实际 | 评语 |
|:--|:-----|:-----|:-----|
| 故事化 | Zak + Heath | **Gottschall + Oatley** | Gottschall 的"故事是信念修改器"比 Zak 的催产素研究更具批判锋芒；Oatley 的叙事传输理论比 Heath 的"黏性"框架更直接攻击故事化的认知漏洞。**升级而非降级。** |
| 数字化 | Rosling + Ariely | **Huff + Harford** | Huff 是统计素养领域的经典奠基人，比 Rosling 更直接；Harford 的"真但误导"比 Ariely 的锚定效应更精准对应数字化的核心主张。**对等替换，质量相当。** |
| 比喻化 | Lakoff + Camp | **Lakoff + Richards** | Lakoff 保留（正确）；Richards 的"意义互动理论"比 Camp 的"过度简化"更具理论深度，精准打击比喻化的核心风险——喻体的不可控联想。**替换合理。** |

### 签发

> **老顽童：路演工具箱 Batch 1 — PASS ✅**
>
> Phase A（T6/T7/T8 善后）✅ — Synthesis 补回、旧卡 redirect
> Phase B（故事化/数字化/比喻化格式转换 + 攻击者补全）✅ — 3 卡格式完整、攻击者论证充实、v1.5 0 Failed
>
> **Phase C（文章 3 篇）可启动。** 从选题池挑选 ≥3 篇，写入 `40_outputs/content/articles/art_20260528_<slug>.md`，质量门通过后通知欧阳锋审查。
>
> *欧阳锋 · 2026-05-28*

---

## 欧阳锋审查意见 — Phase C 文章（2026-05-28）

### 文章清单

| 文章 | 选题方向 | 状态 |
|:----|:--------|:----:|
| `art_20260528_storytelling_vs_truth.md` | 故事化的认知风险——来自 Pitch Batch 1 故事化卡 | 待修 |
| `art_20260528_quantification_traps.md` | 数字化的统计操纵陷阱——来自 Pitch Batch 1 数字化卡 | 待修 |
| `art_20260528_metaphor_cognitive_implant.md` | 比喻作为认知框架植入器——来自 Pitch Batch 1 比喻化卡 | 待修 |

> 选题方向与任务建议的选题池（预判模型/火箭模型/MUSE/IPO/泛产品设计）不同，而是直接取材自 Pitch Batch 1 三张工具卡。**方向合理**——刚产出的卡直接转化为文章是高效的。不必改。

### 质量门逐项审查

| # | 门禁项 | 故事化 | 数字化 | 比喻化 | 判定 |
|:-:|:-------|:------:|:------:|:------:|:----:|
| 1 | `## Audience` 存在 | ❌ | ❌ | ❌ | **FAIL** |
| 2 | `## Core Thesis` 存在 | ❌ | ❌ | ❌ | **FAIL** |
| 3 | ≥3 条 Key Finding + source_ref | ⚠️ 有内容但无结构化 Key Finding 节，frontmatter 有 source_refs 但 validator 未识别 | 同 | 同 | **WARN** |
| 4 | 结尾 CTA | ✅ 结语明确 | ✅ 结语明确 | ✅ 结语明确 | **PASS** |
| 5 | `kdo validate --v15 --article` | ❌ exit 1 | ❌ exit 1 | ❌ exit 1 | **FAIL** |

### 内容质量评估

**故事化文章**：A-。Gottschall + Oatley 两个攻击者引入流畅，三段式（故事的力量→叙事传输→安全边界）结构清晰。与前两篇的 System 1/System 2 呼应略有重复（数字化的也用了 Kahneman），但每个角度不同，不是硬伤。四条安全边界具体可操作。**亮点：** 4D 故事类型的"反伤状态"讨论——每一类故事都有黑暗面，有原创深度。

**数字化文章**：A-。Huff + Harford 引用恰当。4C 策略逐个展开，"选对数字"和"巧用数字"的道德边界讨论到位。三条安全边界具体可执行。**亮点：** "弱数字+合理解释的诚信溢价高于回避"——该结论在 Huff 和 Harford 的批判中给出了出路，不是纯批判。**扣分点：** 标题"用真数字说出真谎言？你以为的确冴"——"确冴"是错别字（应为"确凿"）。

**比喻化文章**：A。Lakoff + Richards 引用精准。三篇中结构最紧凑——从比喻的魔力到双刃剑一气呵成。喻体联想审计、比喻回译测试等实操工具嵌入自然。**亮点：** "比喻是渡河的船，过了河要学会下船"与故事化结尾呼应，三篇之间有整体感。

### 文章间的交叉引用设计

三篇文章在开头段互相引用，均指向各自的工具卡和 `[[yt-model-personal-pitch-toolkit]]` 框架卡。从 Phase B 到 Phase C 的知识传递闭环完整。**设计是刻意的且有意的。** ✅

### 需要修复

**3 处必须修（修复后 PASS）**：

1. **三篇文章各加 `## Audience`** — 目标读者明确：讲香者（一线销售/B2B 创始人/咨询顾问）和听众（高客单价决策者）
2. **三篇文章各加 `## Core Thesis`** — 每篇文章的 thesis 已经在摘要和正文中存在，只需提取。例如故事化文章："故事是比道理更好用的说服工具，但它的说服力与真实性之间没有必然关联——讲香者必须用三源验证和安全边界来防止故事从'说服工具'变成'操纵工具'。"
3. **修复数字化文章标题错别字**："确冴"→"确凿"

**1 处建议修**：

4. **机内 footnote 增强**：validator 报告"No source_refs or footnotes found"——建议在正文中合适位置加 `[^1]` 标注，文末加 `## References` 或 `[^1]: ...` 脚注块，让 validator 认可来源追溯

### 签发

> **老顽童：Phase C 文章 3 篇 — 有条件 PASS 🟡**
>
> 内容质量 A-/A，三篇之间有整体感，知识传递闭环完整。但未通过正式质量门（缺 `## Audience` 和 `## Core Thesis`）。
>
> **需修复 3 处 FAIL + 1 处建议修复**，修复后即可通过。修复后 `kdo validate --v15 --article` 三篇全部 PASS 即验收完成，无需再次审查。
>
> *欧阳锋 · 2026-05-28*

## 不做

- **不做** 非 Batch 1 的路演卡（故事化/数字化/比喻化之外的 7 张等下一批）
- **不做** 框架卡 `yt-model-personal-pitch-toolkit` 的修改（在后续批次一起做）
- **不做** VA 视觉分析（那是洪七公的活）
- **不做** `yt-decision-*` 域的路演关联（专注路演域自身）

---

*欧阳锋 · 2026-05-28*
