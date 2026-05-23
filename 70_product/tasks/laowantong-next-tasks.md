# 老顽童后续任务

## 任务方：老顽童（飞书 Hermes）

## 🎯 当前执行顺序（从上到下，不做完不开下一个）

| 顺序 | 任务 | 估时 | 验证方式 |
|:----:|------|:--:|------|
| **1-4** | ✅ 双三角修复 + Skill 修复 + Anthropic + 设计域复审 | — | 全 A/A-，审查通过 |
| **5** | ✅ ① 补 related 边 | 30min | 3 wikilink + frontmatter relation ✅ |
| **6** | ✅ ⑨ 科学决策域 35 PNG 增强消化 | 3h | 审计报告：91%覆盖，2 遗漏→amendment ✅ |
| **🔧** | ⚠️ 顺手修（开工前 2min） | 2min | ① Anthropic `斗姄`→`窘境` + `reviewed_by` ✅ ② 双三角攻击者移入 Constraints & Boundaries ✅ |
| **🔧** | 🆕 洪七公审计修复 — 双三角文章归属错位 + 引用补齐 | 15min | 方案A：严格按原图修正。`art_双三角纠错_v2` L51 + `art_20260517_9c7a63cb` source_refs/wiki_refs。详见 [[60_feedback/corrections/art-audit-20260519-dual-triangle-batch]] ✅ |
| **🎬** | 🆕 KDO 视频脚本精炼 | 30min | 试点任务。读源文章 → 填 `01-script.md`。详见表下方 |
| **7** | ⑥ v1.5 全库修复 | 分批 | Batch B（~69张缺Critique）→ Batch A（13张全缺）。详见表下方策略 |
| **8** | ⑦ 管理工具箱 Batch 3（T6+T7+T8） | 6h | 每 5 张 B 卡后穿插 1 张 T 卡换脑 |
| **🆕** | 🆕 **OCR 卡 Critique + Synthesis 补全** ← **插队** | 分批 | **136 张 OCR 卡补 Critique + Synthesis + wikilinks**。5 个 Batch，详见 [[70_product/tasks/task-20260523-laowantong-ocr-critique-synthesis]] |
| **🆕** | 🆕 **单元模型域编译 + VA 修复** ← **当前** | 3-4h | **新域编译 + 14条VA修复穿插**。详见 [[70_product/tasks/task-20260524-laowantong-unit-model-plus-va-repair]] |

> **规则**：顺序执行。每 5 张 B 卡 → `kdo validate --v15 --card <id>` 验证 → 通知欧阳锋抽检。穿插 1 张 T 卡换脑。

---

## 状态

- 科学决策域 10 张卡 ✅ | 调研方法论域 8 张卡 ✅ | 全库消化 ✅
- 管理工具箱 Batch 1 ✅（F1+T1+T2 全 A）| Batch 2 ✅（T3 A / T4 A+ / T5 A）
- T1/T3 typo 已修 ✅（欧阳锋 05-19 确认）
- ② 双三角文章 v2 ✅（用户已通过，关闭）
- Anthropic 创始人手册 ✅（A-，Christensen+Pfeffer，5 ATs）
- ⑤ 设计域 S1+S2+S3 ✅（命名+格式+五段式全修）
- ① 补 related 边 ✅ | ⑨ 科学决策 35 PNG ✅（审计报告 A，91%覆盖）
- ⑥ v1.5 修复进行中 ← **当前**
- 🆕 **OCR Critique+Synthesis 补全** ← **新任务，插队执行**（详见 [[70_product/tasks/task-20260523-laowantong-ocr-critique-synthesis]]）

**🆕 最新审查**（欧阳锋 05-20）：[[#🔍 欧阳锋审查（2026-05-19）]] · [[70_product/tasks/dashboard#🔍 v1.5 修复策略（欧阳锋拍板 2026-05-20）|v1.5 修复策略]]

---
## ① 补 related 边（立即，30min）

判卷 Q1 发现：三道跨域连接只在嘴上说了，卡里的 `related:` 字段还没加。

需补的 wikilink + frontmatter relation：

### 卡 yt-decision-y-model 补

```yaml
related:
  - yt-entrepreneur-key-hypotheses  # "拆假设"工具
```

body 关键假设相关段添加：`[[yt-entrepreneur-key-hypotheses]]`

### 卡 yt-decision-review 补

```yaml
related:
  - yt-personal-deep-review  # 冰山图五层→决策复盘上限
```

body 深度复盘段添加：`[[yt-personal-deep-review]]`

### 卡 yt-decision-height-toolkit 补

```yaml
related:
  - yt-model-liberate-thinking-layers  # 高度瓶颈诊断
```

body 高度提升段添加：`[[yt-model-liberate-thinking-layers]]`

### 完成后

跑 `kdo lint` 确认新增 wikilink 的目标页都存在。

---

## ② 双三角文章 v2 — ✅ 已关闭

用户已通过文章，任务关闭。

---

## ③ 管理工具箱 Batch 1 — ✅ 已完成（F1+T1+T2）

欧阳锋审查通过，全 A：

| 卡 | 评级 | 攻击者 |
|----|------|--------|
| F1 [[yt-management-toolkit-overview]] | A | Mintzberg+Pfeffer |
| T1 [[yt-tool-meeting-designer]] | A | Kahneman+Perrow |
| T2 [[yt-tool-hiring-scorecard]] | A | Kahneman+Tetlock |

**⚠️ T1 typo 仍未修复**（Line 90 "只需要知会议会把议程定好"语义不通）。

---

## ④ 管理工具箱 Batch 2 — T3+T4+T5 全部完成 ✅

| 卡 | 评级 | 攻击者 | 状态 |
|----|------|--------|------|
| T3 [[yt-tool-okr-cycle]] | **A** | Mintzberg（涌现战略）+ Ordonez（目标副作用） | ✅ 审查通过。⚠️ typo 仍未修复：Line 105 `团队脚脑暴`→`团队头脑风暴` |
| T4 [[yt-tool-strategy-workshop]] | **A+** | Christensen（创新者窘境）+ Taleb（黑天鹅/规划伪科学） | ✅ 审查通过。全库迄今最佳 tool 卡，建议作为后续标准 |
| T5 [[yt-tool-knowledge-extraction]] | **A** | Nonaka&Takeuchi（SECI 模型）+ Snowden（Cynefin——复杂域知识不可萃取） | ✅ 审查通过。typo 已修复 ✅ |

**审查备注**：
- T4 是全工具箱 5 张 tool 卡的结构标杆：会前四件套+会中五段式+会后三检查，11 步各有时间分配+关键约束+退出标准
- T3 的 Ordonez 是非显而易见但高度相关的选择（"Goals Gone Wild"研究），体现了独立学术判断
- Mintzberg 已在 F1/T3/T4 三次出场，攻击角度有区分（管理手艺 vs 涌现战略 vs 战略涌现）但目前频次触顶，T5-T8 应避开
- Taleb 已出场 ~3 次，同样建议 T5-T8 避开

---

## ⑤ 设计域 → 洪七公/段王爷 Skills（方向调整）

> **2026-05-19 欧阳锋拍板**：废弃 D1-D7 卡片地图 + 两篇文章方案。这不是知识卡片（不需要 Critique/攻击者），是操作手册。产出改为 3 个 skill 文件，供洪七公和段王爷直接调用。格式参照 `[[40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md]]`。

### 素材

已就位 `00_inbox/design/`（2026-05-19 欧阳锋核实）：

| 文件 | 内容 | 大小 | 状态 |
|------|------|------|------|
| `AI设计-AI设计基础01.txt` | 月白老师第一期分享 | 72KB | ✅ 已清理 → `cleaned/` |
| `AI设计-AI设计师实操培训01.txt` | 月白老师第二期分享 | 122KB | ✅ 已清理 → `cleaned/` |
| `prompts/ai-image-generation.md` | NANO BANANA PRO 提示词集合链接 | 230B | ✅ 骨架 |

### 产出：3 个 Skill

| # | Skill 名称 | 给谁用 | 素材来源 | 核心内容 |
|---|-----------|--------|---------|---------|
| **S1** | AI 生图模型选型指南 | 洪七公 | 素材1 前半 | GPT-2o / 巨米4.0 / Nano Banana 场景匹配矩阵、"去油腻"概念、何时用/不用 |
| **S2** | AI 设计 Prompt 工程 | 洪七公 | 素材2 | "拜拜"工作流（说出来→写下来→喂给AI）、设计MVP、灵感画布五维检索 |
| **S3** | 设计资产管理规范 | 段王爷 | 素材1 后半 | 8要素命名法、四类资产沉淀、输出格式规范 |

### Skill 格式规范

参照 `[[40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md]]`，每个 skill 必须包含：

```markdown
# Skill Name

## Purpose（一句话说清干什么）

## When to Use（触发条件）

## When NOT to Use（边界——这很重要）

## Protocol / Guide（操作步骤，能照着做）

## Examples（至少一个真实案例）
```

**不需要**：Critique、攻击者、不要用场景、Action Triggers、wikilink 引用。这是操作手册，不是知识卡片。

### 执行顺序

S1 → S2 → S3，分段输出。每完成一个发欧阳锋审查。

---

## ⑤-B 设计域 Skill 命名与格式修复（欧阳锋审查反馈）

> **审查结论**：三份 SKILL.md 内容评级均为 A（S1 模型选型准确、S2 提示词模板实用、S3 资产管理体系完整），但存在 3 个命名/格式 Bug，需修复后复议。

### Bug 1：目录名与内容错位

| 现状 | 问题 | 应改为 |
|------|------|--------|
| `ai-design-workflow/` | 内容=Prompt 工程，目录名叫 workflow | `ai-design-prompts/` |
| `ai-design-prompts/` | 内容=资产管理规范，目录名叫 prompts | `ai-design-assets/` |
| `ai-design-fundamentals/` | ✅ 正确（内容=模型选型） | 不改 |

### Bug 2：Frontmatter `name:` 重复

两个文件共用 `name: ai-design-prompts`，`skill_view()` 会加载到错的文件：

| 文件 | 当前 name | 应为 |
|------|-----------|------|
| `ai-design-fundamentals/SKILL.md` | 无 (缺失) | `ai-design-fundamentals` |
| `ai-design-workflow/SKILL.md` | `ai-design-prompts` | `ai-design-prompts` |
| `ai-design-prompts/SKILL.md` | `ai-design-prompts` | `ai-design-assets` |

### Bug 3：缺失标准五段式结构

三个文件均无 `## Purpose` / `## When to Use` / `## When NOT to Use` / `## Protocol` / `## Examples` 标准段。当前是讲义体（## 1. / ## 2. / ...），需在现有内容基础上**添加**标准头部段：

1. 在每个文件开头（`# 标题` 之后、正文之前）添加：
   ```markdown
   ## Purpose
   （一句话说清这个 skill 干什么）

   ## When to Use
   - 场景1
   - 场景2

   ## When NOT to Use
   - 边界1
   - 边界2
   ```
2. 现有正文整体归入 `## Protocol` 段
3. 末尾添加 `## Examples`（至少 1 个真实案例，可简化）

### 修复清单

| 步骤 | 操作 | 文件 |
|:----:|------|------|
| 1 | 重命名目录 | `ai-design-workflow/` → `ai-design-prompts/` |
| 2 | 重命名目录 | `ai-design-prompts/` → `ai-design-assets/` |
| 3 | 改 frontmatter `name:` | `ai-design-fundamentals` → `name: ai-design-fundamentals` |
| 4 | 改 frontmatter `name:` | `ai-design-prompts` → `name: ai-design-prompts` |
| 5 | 改 frontmatter `name:` | `ai-design-assets` → `name: ai-design-assets` |
| 6 | 修 prerequisites 交叉引用 | 三个文件的 `prerequisites:` 字段改为新 name |
| 7 | 加标准五段式 | 三个文件各加 Purpose/When to Use/When NOT to Use/Protocol/Examples |

### 验收

- 三个目录名与内容一致
- 三个 frontmatter `name:` 互不相同
- 三个文件均有 `## Purpose` `## When to Use` `## When NOT to Use` `## Protocol` `## Examples` 五段
- `kdo validate --skill-dir 40_outputs/capabilities/skills/ai-design-fundamentals --skill-dir 40_outputs/capabilities/skills/ai-design-prompts --skill-dir 40_outputs/capabilities/skills/ai-design-assets` 通过（黄药师 Task 11 完成后可用）

---

## ⑥ v1.5 全库修复流水线（设计域完成后）

### 背景

`kdo validate --v15` 诊断结果：205 张卡，45 pass / 89 fail / 71 warn。`kdo scaffold`（黄药师 Task 1）已经搭好了工具。

### 执行方式

```bash
# 1. 先看全局
kdo validate --v15 --upgrade-plan

# 2. 按优先级分批（黄药师的 scaffold 已可用）
kdo scaffold --batch A --write    # 全信号缺失高引卡（~3 张）
kdo scaffold --batch C --write    # 缺 Action Triggers（~6 张）
kdo scaffold --batch B --write    # 缺外部攻击（~80 张，大头）
kdo scaffold --batch D --write    # 研究降级（~26 张）

# 3. 逐张填内容（scaffold 给了 TODO + 学者建议）
# 4. 填完验证
kdo validate --v15 --card <id>
```

### 优先级

| 顺序 | Batch | 内容 | 卡数 | 策略 |
|------|-------|------|------|------|
| 1 | C | 缺 Action Triggers | ~6 | **先做**。每张只需补一个 3 行表，15min/张，最快看到 PASS 增长 |
| 2 | A | 全信号缺失高引 | ~3 | 工作量大（90min/张）但价值最大——修一张 = 0→3 信号 |
| 3 | B | 缺外部攻击 | ~80 | **大头**。每张需研究 2 位学者 + 写攻击段落，60min/张 |
| 4 | D | 研究降级 | ~26 | 标准降低但仍需 ≥1 攻击 |
| 5 | E | Warnings | ~71 | 不算 fail，精修 |

> 注意：不是一次做完 89 张。按批推进，每做完一批通知欧阳锋抽检。

---

## ⑦ 管理工具箱 Batch 3（89 卡修复喘口气时穿插）

工具箱还剩最后 3 张，可以在 89 卡修复的间隙穿插（换脑休息）：

**T6 [[yt-tool-project-health-radar]]** — 项目健康度雷达（L2-L4 交叉）
**T7 [[yt-tool-onboarding-90day]]** — 新人 90 天融入加速器（L3 管团队）
**T8 [[yt-tool-equity-checklist]]** — 股权设计检查清单（L5 管公司）

攻击者方向：
- T6 项目雷达：Flyvbjerg（巨型项目铁律）+ Goldratt（约束理论——局部最优≠全局最优）
- T7 新人融入：Van Maanen&Schein（组织社会化策略）+ Edmondson（心理安全——融入≠同化）
- T8 股权清单：Coase（交易成本/企业边界）+ Williamson（资产专用性——股权是一种治理结构选择）

---

## ⑧ Anthropic AI 原生初创公司手册（🆕 优先）

### 素材

| 文件 | 来源 | 大小 |
|------|------|------|
| `00_inbox/Anthropic 官方发布：《创始人手册：打造 AI 原生初创公司》.md` | Anthropic 2026.5.17 | 82KB |

已 ingest → source `src_20260519_f6ec0400`，wiki 骨架已生成：[[anthropic-官方发布创始人手册打造-ai-原生初创公司]]

### 执行步骤

标准三步编译法：

1. **读素材**：`10_raw/sources/src_20260519_f6ec0400-*.md`
2. **Condense**：提取 3-5 条核心观点（AI 四阶段创业法、创始人角色演变、精益独角兽模式、三类 AI 能力）
3. **Question**：写 `## Constraints & Boundaries` + `### [Critique]` 节
   - 至少 2 位外部攻击者（建议方向：Christensen 创新者窘境——AI 原生是否是新颠覆？Pfeffer 领导力 BS——AI 指挥家是否是新包装？）
   - 至少 2 个不要用场景
4. **Synthesize**：对标已有卡片（管理工具箱 F1/T4、决策域 Y 模型等），创建 wikilink
5. **Action Triggers**：≥3 条可执行触发器

### 卡片类型

`concept`（方法论概念卡），domain 建议 `entrepreneur`

### 验收

- v1.5 三信号齐全（≥2 attackers, ≥2 don't-use, ≥3 AT）
- 引用 Anthropic 原文关键数据
- 跨域引用 ≥3 张已有卡片
- `kdo validate --v15 --card anthropic-官方发布创始人手册打造-ai-原生初创公司` 返回 PASS

---

## ⑨ 科学决策域 35 PNG 增强消化

### 素材

```
00_inbox/科学决策/
├── 35 张 PNG 图片（白板/手绘/框架图/PPT 截图等）
└── 口述稿转录文本（如有，待确认）
```

### 定位

不是缺素材——科学决策域 **10 张卡已完成且审查通过**。这批 PNG 是**增强素材**，目的是查漏补缺：现有卡是否遗漏了口述稿/图片中的关键概念或框架。

### 执行步骤

1. **OCR 提取**：35 张 PNG 逐张 OCR → 每张输出 `*_paddle_ocr.txt`
   - 工具：`node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image>`
   - 或 `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1`
2. **口述稿交叉**（如有）：OCR 文本与口述稿转录对照，标记口述稿提到但 10 张卡未覆盖的概念
3. **逐卡比对**：以现有 10 张卡为基准，检查每张：
   - 核心观点是否有遗漏？（对照 OCR + 口述稿）
   - 攻击者覆盖是否充分？
   - 视觉框架是否有可补充的图例？
4. **产出**：
   - 无遗漏 → 记录结论，归档关闭
   - 有遗漏 → 在对应卡片中补充（amendment），不改卡片主体结构
   - 发现新概念 → 评估是否需要新卡（需先向欧阳锋提议，获批后再开卡）

### 约束

- **不改卡片主体结构**——只补遗漏，不重构已有内容
- **新卡须先提议**——发现新概念不能自己直接开卡，先汇报欧阳锋评估
- **OCR 在 vault 外运行**——ocr-pipeline 路径 `C:\Users\Administrator\ocr-pipeline\`，不进 git

### 验出

- 35 张 PNG 全部 OCR 完成
- 与 10 张科学决策卡交叉比对报告（遗漏清单 or "无遗漏"确认）
- 如有遗漏 → 对应卡片 amendment + `kdo validate --v15 --card <id>` PASS

---

## 🔍 欧阳锋审查（2026-05-19）

### T1/T3 Typo 修复 → ✅ 已确认

| 卡 | 原文 | 修复后 | 验证 |
|----|------|--------|------|
| T1 `yt-tool-meeting-designer` Line 90 | `只需要知会议会把议程定好` | `只需要知道会议会把议程定好` | ✅ |
| T3 `yt-tool-okr-cycle` Line 105 | `团队脚脑暴` | `团队头脑风暴` | ✅ |

### 双三角竞争力模型卡 → A-（内容 A，结构需修，设计域产出完整 ✅）

**卡片**：[[yt-model-dual-triangle-competitiveness]]

**内容评价（A）**：
- Mintzberg（实践手艺不可编码）+ Taleb（幸存者偏差/赢家归纳错误）——两个攻击角度精准、独立、有具体引用来源
- Visual Analysis 五维分析（空间层级/分组逻辑/阅读路径/视觉强调/留白含义）是 KDO 迄今最详尽的信息图分析，方法论自觉
- 3 个不要用场景 + 4 个 Action Triggers 均合格，替代方案具体可操作

**关联设计域产出**（洪七公+老顽童联合产出，均已完成 ✅）：
- `40_outputs/content/images/infographics/dual-triangle-visual-analysis.md` — 158 行完整视觉分析报告（洪七公）
- `40_outputs/content/images/infographics/dual-triangle-competitiveness.excalidraw` — Excalidraw 重绘信息图（洪七公）
- 归属错位发现：原图 vs wiki 卡片子项归属不一致（洪七公发现，老顽童在卡片中添加注释）

**结构问题（需修复，5min）**：

1. **H3→H4 攻击者标题**：两个攻击者（Mintzberg、Taleb）写在同一个 H3 标题下：
   ```
   ### 外部攻击：Henry Mintzberg的实践手艺论 + Nassim Taleb的幸存者偏差
   ```
   `kdo validate --v15` 解析器只识别 H4 标题统计攻击者，当前报告 0/2。需拆为：
   ```markdown
   #### Henry Mintzberg — 实践手艺论
   （Mintzberg 攻击段落）

   #### Nassim Taleb — 幸存者偏差
   （Taleb 攻击段落）
   ```

2. **重复 `related:` 字段**：frontmatter 中 `related:` 出现两次（Line 14-17 和 Line 34-37），YAML 解析时后者覆盖前者。删掉其中一组（保留较完整的 Line 14-17，删 Line 34-37 的简版）。

### 老顽童本次完成总结

| 产出 | 状态 | 评级 |
|------|:--:|:--:|
| T1/T3 typo 修复 | ✅ | — |
| 双三角卡内容（Mintzberg+Taleb, VA, 3 不要用, 4 AT） | ✅ | A |
| 双三角卡结构（H3→H4, 重复 related） | ✅ | 已修，欧阳锋确认 |
| 双三角配套 Visual Analysis + Excalidraw | ✅ | 洪七公联合作业 |
| Anthropic 创始人手册 | ✅ | A-，已编译 |
| 设计域 S1/S2/S3 | ✅ | 命名+格式+五段式已修 |

**审查结论（2026-05-19 更新）**：三项全部完成。遗留 2 个顺手修（见下方 [[#🔍 本次审查遗留（2026-05-19）]]）。

---

## 完成标志

| 序号 | 任务 | 验证 |
|------|------|------|
| ① | 补 related 边 | `kdo lint` 通过 + 欧阳锋确认 |
| ② | 双三角文章 v2 | ✅ 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1 | ✅ 全 A，T1 typo 已修 ✅ |
| ④ | 管理工具箱 Batch 2 | ✅ T3 (A) + T4 (A+) + T5 (A)，T3 typo 已修 ✅ |
| 🔍 | 双三角卡结构修复 | ✅ H3→H4 ✅ + 删重复 related ✅ |
| ⑤ | 设计域 3 个 Skill | ✅ 命名+格式+五段式全修 |
| ⑥ | v1.5 全库修复（89 FAILED） | `kdo validate --v15` FAILED → 0 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 欧阳锋审查通过 |
| ⑧ | Anthropic 创始人手册 | ✅ A-。v1.5 三信号齐全 |
| ⑨ | 科学决策域 35 PNG 增强消化 | 35 张 OCR + 10 卡交叉比对完成 |

---

## 🔍 本次审查遗留（欧阳锋 2026-05-19，老顽童下次会话顺手修）

两项都是 1 分钟修完的小事：

**1. [[anthropic-官方发布创始人手册打造-ai-原生初创公司]] — typo**
- Line 105 `创新者斗姄` → `创新者窘境`
- 补 frontmatter `reviewed_by: 欧阳锋`

**2. [[yt-model-dual-triangle-competitiveness]] — 结构微调（建议）**
- 两个 H4 攻击者目前在 `## Framework Gallery` 下，惯例放 `## Constraints & Boundaries`
- 不影响 `kdo validate --v15`，不改也行

---

## 🆕 洪七公审计修复 — 双三角文章（插队执行，15min）

> 审计来源：[[60_feedback/corrections/art-audit-20260519-dual-triangle-batch]]（洪七公 2026-05-19）
> 欧阳锋决策：方案A——严格按原图 `00_inbox/一堂-个人修炼-双三角模型.jpg` 修正

### 文件 1：`40_outputs/content/articles/art_双三角纠错_v2.md`

**L51 归属错位修复**：

当前（错误）：
```
创造力…包含三个动作：业务拆解、理解底层规律、提出创造假设
```

改为：
```
创造力…包含三个动作：理解底层规律、善于解放思想、提出创造假设
```

同时检查场景段是否完整列出四个子项：**业务拆解、ROI预判、AI打磨、组织部署**。如有缺失补全。

### 文件 2：`40_outputs/content/articles/art_20260517_9c7a63cb-人机协作决策双三角模型读后感.md`

**① 补全 source_refs**：
当前只有 1 个：
```yaml
source_refs: ["src_20260510_7c58991a"]
```
补充正文引用的外部学术来源（至少 5 个 src_ id），包括 Mintzberg、Taleb、Klein、Kahneman 等。

**② 补全 wiki_refs**：
当前只有 1 个：
```yaml
wiki_refs: ["30_wiki/concepts/yt-decision-ai-partner.md"]
```
补全正文引用的所有 wiki 概念（至少 3 个），包括：
- `30_wiki/concepts/yt-model-dual-triangle-competitiveness.md`
- `30_wiki/concepts/yt-decision-y-model.md`

**③ 统一 delivery_channel**：
```yaml
delivery_channel: homework  →  delivery_channel: wiki
```
与 `art_双三角纠错_v2` 统一为 wiki 渠道。如需区分受众，在标题中标注（如"深度篇"）。

### 验收

- `art_双三角纠错_v2` L51 归属与原图一致
- `art_20260517_9c7a63cb` 的 source_refs ≥ 5, wiki_refs ≥ 3, delivery_channel = wiki
- 完成后通知洪七公做多模态转换

---

## 🔍 v1.5 修复策略（欧阳锋拍板 2026-05-20）

> 扫描结果：215 卡，54 pass / 89 fail / 72 warn。89 张 FAILED 分两批。

### 执行顺序：B → A

| 顺序 | Batch | 问题 | 卡数 | 每卡 | 总估时 |
|:--:|-------|------|:--:|:--:|:--:|
| **1** | B | 缺 Critique（有 DU table + AT table） | ~69 | 30min | ~35h |
| **2** | A | 全信号缺失（ATK=0/DU=0/AT=0） | ~13 | 90min | ~20h |

### 为什么 B 先做

B 卡结构半成型，DU table 和 AT table 已存在，只差 `## Constraints & Boundaries` + 2 个 H4 攻击者。做完 69 张后 FAILED 从 89 降到 ~20，再集中突破 13 张 A 卡。

### B 卡执行模板

每张 B 卡在 `## Synthesis` 前插入：

```markdown
## Constraints & Boundaries

#### [学者名] — [攻击标题]
[2-3 句攻击论证，含具体引用来源]

#### [学者名] — [攻击标题]
[2-3 句攻击论证，含具体引用来源]
```

攻击者选择原则：
- pan-product 卡 → JTBD、精益创业、设计思维、系统动力学范式
- 同一域内不同卡使用不同攻击者（不重复）
- 攻击要有紧迫感："这个框架的边界在哪？什么时候会失效？"

### CLI

`kdo validate --v15` 文本输出正常，**不用 `--json`**（有编码问题）。

### 穿插规则

- 每 5 张 B 卡 → `kdo validate --v15 --card <id>` 验证 PASS → 通知欧阳锋抽检
- 每 5 张 B 卡后穿插 1 张 T 卡（T6/T7/T8）换脑
- Batch B 做到 30 张时暂停，让欧阳锋审查节奏和攻击者质量

### 验收

- `kdo validate --v15` FAILED 从 89 降到 0
- 不得新增 WARN

---

## 🎬 KDO 视频脚本精炼（试点任务，~30min）

> **背景**：KDO 视频流水线试点。黄药师 `kdo video` CLI 已就绪（`e8b9265`），项目已 init。
> **工作流**：[[40_outputs/capabilities/workflows/video-production-flow.md]]

### 做什么

```
/new session
入参：源文章 + 01-script.md 模板
出参：填好的 01-script.md
```

**源文章**：`40_outputs/content/articles/art_20260504_02b8c4d6-kdo-quickstart-guide.md`

**输出路径**：`40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/01-script.md`

### 怎么做

1. **Read** 源文章（74 行，5 Key Takeaways + 6 节 Draft）
2. **Read** `01-script.md` 模板——已有 5 段框架（Segment 1-5 + 时长标注 + 空 speaking points）
3. 逐段填充 speaking points：
   - **每段 3-5 个 bullet points**，不是段落——给口语表达留弹性
   - 每句话写完默念一遍——**说出来顺不顺**
   - 标注 `[Visual hint: ...]` 告诉洪七公这 30 秒画面上该出现什么
4. 替换所有 `[Speaking point N]` 占位符

### 脚本规范

| 要求 | 标准 |
|------|------|
| 时长 | 总 2000-2500 字（中文口播 ~250 字/min，8-10 分钟） |
| 结构 | 5 段：Hook(45s) → 什么是KDO(2min) → 怎么做(3-4min) → 谁适合(1.5min) → 结尾(1min) |
| 语言 | 短句为主（≤25 字/句），嵌套从句砍掉。停顿时用 `--` 标注 |
| 术语 | 首次出现时一句话解释（"KDO 是一个本地知识流水线——把飞书文档变成可交付资产"） |
| 禁止 | 不说"众所周知""显而易见"；不堆砌排比句；每段不超过 5 个 speaking point |
| Visual hint | 每段至少 1 个，用 `[Visual hint: 画面描述]` 格式 |

### 🛑 门禁（通过标准，缺一不可）

| # | 门禁项 | 判定方式 |
|:--:|------|------|
| 1 | 总字数 2000-2500 | 编辑器字数统计 |
| 2 | 5 个 Segment 无 `[Speaking point` 占位残留 | `grep "\[Speaking point" 01-script.md` 返回空 |
| 3 | 每段 ≥1 个 `[Visual hint: ...]` | `grep "\[Visual hint" 01-script.md` 返回 ≥5 |
| 4 | `kdo video validate --stage script` 返回 PASS（无 TODO 警告） | 终端 exit 0 |
| 5 | 欧阳锋抽查朗读 2 段——不拗口、可一口气说完 | 人审 |

### 🛑 审批（提报规范）

**完成后必须立即提报，不得自行进入后续阶段。**

提报人：老顽童 → 审批人：欧阳锋

提报格式：
```
KDO 视频脚本已完成，请欧阳锋审查。
路径：40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/01-script.md
```

审批结果：
- **通过** → 欧阳锋通知洪七公启动分镜（7a）
- **修改** → 欧阳锋标注具体修改点（行号+问题+期望），老顽童修改后重新提报

> ⚠️ 审批通过前自行进入下一阶段 = 违规。跳步后果参 C-8。

### 🛑 节点（你在流水线中的位置）

```
GATE 0 ← 你在这里，产出 01-script.md
  ↓ 欧阳锋审批通过
GATE 1 ← 洪七公分镜（你不出力，但要知道下游在等你）
  ↓
GATE 2-4 ← 洪七公 + 黄药师 + 欧阳锋
  ↓
final.mp4
```
