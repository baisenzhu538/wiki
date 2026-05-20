---
title: 任务仪表盘
updated: 2026-05-20 (Gate 0+1 审查通过)
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 批次 | 状态 | 备注 |
|---|------|------|------|------|
| ① | 补 related 边 | — | ✅ | 3 条 wikilink + frontmatter relation |
| ② | 双三角文章 v2 | — | ✅ | 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1（F1+T1+T2） | 工具箱 | ✅ | 全 A。T1 typo 已修 ✅ |
| ④ | 管理工具箱 Batch 2（T3+T4+T5） | 工具箱 | ✅ | T3 A / T4 A+ / T5 A。T3 typo 已修 ✅ |
| 🔍 | 双三角卡结构修复 | — | ✅ | H3→H4 ✅ + 删重复 related ✅。⚠️ 攻击者在 Framework Gallery 下，建议移入 Constraints & Boundaries |
| 🆕 | Anthropic AI 原生初创手册 | 素材编译 | ✅ | A-。Christensen+Pfeffer 攻击精准，5 ATs。⚠️ `创新者斗姄`→`创新者窘境`，补 `reviewed_by` |
| ⑤ | 设计域 S1+S2+S3 skill | 洪七公+段王爷 | ✅ | 命名+格式+五段式全修。3/3 通过 |
| 🆕 | 科学决策域 35 PNG 增强消化 | 增强 | ✅ | 审计报告 A，91%覆盖，2 遗漏→现有卡 amendment，无需新卡 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 v1.5 修复间隙 |
| 🎬 | KDO 视频脚本精炼（Stage 1） | 视频 | ✅ | 脚本 A，Gate 0 通过。欧阳锋审查：1825 字（略低于 2000 下限，内容覆盖完整不阻塞） |

### 老顽童 — 执行顺序（从上到下，做完一个再看下一个）

| 顺序 | 任务 | 内容 | 估时 | 备注 |
|:----:|------|------|:--:|------|
| **1** | ~~🔍 双三角卡结构修复~~ | ✅ 完成 | 5min | 欧阳锋复审：通过。⚠️ 攻击者在 Framework Gallery 下，建议移入 Constraints & Boundaries |
| **2** | ~~🔧 设计域 Skill 命名+格式修复~~ | ✅ 完成 | 15min | 欧阳锋复审：通过。3/3 全修 |
| **3** | ~~🆕 Anthropic 创始人手册~~ | ✅ 完成 | 2h | 欧阳锋复审：A-。⚠️ 修 typo `斗姄`→`窘境`，补 `reviewed_by` |
| **4** | ~~⑤ 设计域 S1+S2+S3 复审~~ | ✅ 欧阳锋已复审 | — | 三 skill 内容 A，格式完备，闭环 |
| **5** | ~~① 补 related 边~~ | ✅ 完成 | 30min | 3 条 wikilink + frontmatter relation |
| **6** | ~~🆕 科学决策域 35 PNG 增强消化~~ | ✅ 完成 | 3h | 审计报告：91%覆盖，2 遗漏→amendment，无需新卡 |
| **🔧** | 🆕 洪七公审计修复 — 双三角文章归属错位 + 引用补齐 | 15min | 方案A：严格按原图修正。`art_双三角纠错_v2` L51 + `art_20260517_9c7a63cb` source_refs/wiki_refs。见 [[#🔍 洪七公文章审计（2026-05-19）]] |
| **7** | ⑥ v1.5 全库修复（20 FAILED） | Batch B（~69张缺Critique）先做，再 Batch A（13张全缺）| 分批 | 穿插 ⑦ Batch 3。策略见 [[#🔍 v1.5 修复策略（欧阳锋拍板 2026-05-20）]] |
| **8** | ⑦ 管理工具箱 Batch 3（T6+T7+T8） | 穿插在 ⑥ 间隙 | 6h | T6 项目雷达 / T7 新人融入 / T8 股权清单 |
| **🎬** | KDO 视频脚本精炼 | ✅ 完成。Gate 0 通过 | 30min | 欧阳锋审查：A。5 段，1825 字，5/5 Visual hints，`kdo video validate` PASS |

> **规则**：顺序执行，不跳。每完成一个 → 跑验证 → 通知欧阳锋审查。不要等批次全部完成。
> 🎬 视频脚本试点的前置依赖（黄药师 `kdo video init`）已就绪。优先执行。

### 🎬 老顽童 — 视频脚本任务（试点，30min）

- **入参**：`40_outputs/content/articles/art_20260504_02b8c4d6-kdo-quickstart-guide.md`
- **出参**：`40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/01-script.md`
- **规范**：[[40_outputs/capabilities/workflows/video-production-flow#Stage 1]] + [[laowantong-next-tasks#🎬 KDO 视频脚本精炼]]
- **验收**：欧阳锋抽查朗读 2 段；`kdo video validate --stage script` 无 TODO 警告
- **完成后通知**：欧阳锋审查脚本→洪七公启动分镜

---

---

## 黄药师（Builder · WSL tmux claude）

| # | 任务 | 优先级 | 状态 | 备注 |
|---|------|--------|------|------|
| 1 | `kdo scaffold` | P0 | ✅ | A，17 tests |
| 2 | `kdo clean-transcript` | P1 | ✅ | A，7 tests |
| 3 | `kdo validate --v15 --watch` | P2 | ✅ | A，纯标准库 |
| 4 | `kdo watch` 依赖解耦 | P1 | ✅ | 4 tests |
| 5 | scaffold 插入位置修正 | P2 | ✅ | Critique→CB/Synthesis 间 |
| 6 | `kdo task` 自动化 + dashboard | **P0** | ✅ | 6 tests, 5 子命令, 向后兼容 |
| 7 | graph rebuild --incremental | P2 | ✅ | 5 tests, --full + incremental |
| 8 | `kdo graph stats` | P3 | ✅ | 4 tests, --json, NOT BUILT |
| 9 | Graph RAG 深化 | P1 | ✅ | graph path + 跨域标注 + --health, 9 tests |
| 10 | Quality Gate v2（article+skill） | P1 | ✅ | --article + --skill + --all, 9 tests |
| 11 | `kdo validate --skill-dir` 审查流水线 | P1 | ✅ | batch 扫描 + L1 5节检查, 5 tests |
| 12 | KDO Build 系统 | P2 | ✅ | `kdo build` + CHANGELOG + build_state, 11 tests |
| 13 | 🔥 scaffold 四缺陷（盲区+重复插入+内容丢弃+空H4） | **P0** | ✅ | `877c41a`。286 tests PASS (+4)。欧阳锋审查：A，通过 |
| 14 | validator 空 H4 校验 | P1 | ✅ | 并入 Task 13。H4 <100 字不计入。验收测试全部通过 |
| 15 | `kdo video` CLI（init/validate/render/ship） | **P1** | ✅ | `e8b9265`。5 子命令，24 tests，310 total 0 regressions |

### 黄药师 — 当前任务

**全部完成** ✅。Task 1-15 全部交付。等欧阳锋审查后派新任务。

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

> **定位**：多模态知识仲裁者。主业=知识→视觉资产。副业=VA 过程中发现归属错位。
> **输入**：`dashboard` 任务 + `30_wiki/concepts/` 卡片 + `10_raw/assets/` 原图
> **输出**：静态视觉 → `40_outputs/content/images/` · 动态视觉 → `videos/` · 音频 → `audio/` · 演示 → `presentations/` · 网页 → `code/templates/` · 勘误 → `60_feedback/corrections/`
> **规则**：不自行修改卡片主体结构。原图优先于卡片文字。详细 → [[20_memory/beikai-role-positioning.md]]

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 1 | 角色自我定义 | ✅ | 已获欧阳锋确认为"多模态仲裁者" |
| 2 | 双三角 Visual Analysis | ✅ | `40_outputs/content/images/infographics/dual-triangle-visual-analysis.md` |
| 3 | 双三角 Excalidraw 重绘 | ✅ | `40_outputs/content/images/infographics/dual-triangle-competitiveness.excalidraw` |
| 4 | wiki 勘误（归属错位） | ✅ | 已反馈 → `60_feedback/corrections/`，卡片修正由老顽童执行 |
| 5 | 通道就绪确认 | ✅ | 13 路径全部就绪，5 核心输出路径写入测试通过 |
| 6 | 双三角文章审计 | ✅ | 审计 2 篇，发现 🔴归属错位 1 处 + 🟡引用/渠道 3 处，报告已交付 |
| 7 | KDO 快速上手指南 → 中视频（分镜+画面） | 🔨 | 7a ✅ Gate 1 通过。7b-7g 排队。详见下方 |

### 洪七公 — 视频流水线任务（Task 7 重构）

> **工作流**：[[40_outputs/capabilities/workflows/video-production-flow.md]]
> **原则**：每阶段独立 `/new` session，读入参文件→写出参文件，不靠记忆。
> **🛑 审批铁律**：每个阶段完成后**必须提报欧阳锋审查**，审查通过前**不得**进入下一阶段。不通过则标注修改点→修改→重新提报。

| 子任务 | 阶段 | 入参 | 出参 | 前置依赖 | 估时 | 审查节点 |
|:--:|------|------|------|------|:--:|:--:|
| 7a | 分镜设计 | `01-script.md` | `02-storyboard.md`（Style Guide + 分镜表） | 老顽童脚本完成 | 45min | ✅ **Gate 1 通过**：欧阳锋审查 A，34 帧，Style Guide 完整，非通用科技风 |
| 7b | 画面 Seg 1 | `02-storyboard.md` | `frames/segment_1_*.png` | Gate 1 通过 | 30min | — |
| 7c | 画面 Seg 2 | `02-storyboard.md` | `frames/segment_2_*.png` | Gate 1 通过 | 30min | — |
| 7d | 画面 Seg 3 | `02-storyboard.md` | `frames/segment_3_*.png` | Gate 1 通过 | 30min | 🛑 **Gate 2**：7b-7d 完成 3/5 段时提报欧阳锋抽检 |
| 7e | 画面 Seg 4 | `02-storyboard.md` | `frames/segment_4_*.png` | Gate 2 通过 | 30min | — |
| 7f | 画面 Seg 5 | `02-storyboard.md` | `frames/segment_5_*.png` | Gate 2 通过 | 30min | 🛑 **Gate 3**：全部 5 段画面完成后提报欧阳锋终检 |
| 7g | 配音节奏审查 | `draft/draft.mp4` | `timing.md`（时间轴修正标注） | 黄药师 render + Gate 3 通过 | 20min | 🛑 **Gate 4**：timing.md 提报欧阳锋→黄药师最终合成→**欧阳锋终审 draft.mp4** |

**洪七公总估时**：~3.5h。音频和组装由 `kdo video render` 工具链完成，不占用洪七公 session。

### 🛑 审批节点总览（视频试点）

```
老顽童 01-script.md 完成
    │
    ▼
🛑 GATE 0 — 欧阳锋审查脚本（抽查朗读 2 段）
    │
    ▼
洪七公 7a 02-storyboard.md
    │
    ▼
🛑 GATE 1 — 欧阳锋审查分镜（Style Guide 完整？每句有画面？不是通用科技风？）
    │
    ▼
洪七公 7b-7d（Segment 1-3）
    │
    ▼
🛑 GATE 2 — 欧阳锋抽检画面（抽查 2/5，风格一致？匹配分镜表？）
    │
    ▼
洪七公 7e-7f（Segment 4-5）
    │
    ▼
🛑 GATE 3 — 欧阳锋终检全部画面
    │
    ▼
黄药师 kdo video render --audio → --compose
    │
    ▼
洪七公 7g timing.md
    │
    ▼
🛑 GATE 4 — 欧阳锋终审 draft.mp4（节奏+音画同步+整体观感）
    │
    ▼
黄药师 kdo video ship → final.mp4
```

### 提报规范

每阶段完成后，洪七公/老顽童必须通知欧阳锋：

```
"[角色名] [阶段名] 已完成，路径：[产出文件路径]，请欧阳锋审查"
```

欧阳锋审查后在同一文件末尾或任务文件追加审查结论。结论为"通过"方可进入下一阶段。结论为"修改"则标注具体修改点，修改完成后重新提报。

**禁止**：审查通过前自行进入下一阶段。跳步后果：产出质量不可控（参 C-8：格式完整但思维空洞）。

## 段王爷（Publisher）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 黄药师 | `kdo video` CLI（Task 15） | ✅ 已交付。阻塞解除 |
| 洪七公 | 视频分镜+画面（Task 7b-7g） | 🔨 可立即开工。7a 分镜已通过 Gate 1，7b-7d 无阻塞 |
| 老顽童 | v1.5 全库修复（20 FAILED） | 🔨 可随时启动 |
| 老顽童 | 🔧 4 项顺手修（Anthropic typo + 双三角文章归属+引用） | 积压，可随时清 |
| 老顽童 | v1.5 全库修复（20 FAILED） | scaffold 已修好，可随时启动 |
| 洪七公 | `art_双三角纠错_v2` 修复后→多模态转换 | 等老顽童修完归属错位 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-20 | 欧阳锋 | 🛑 Gate 0 审查：老顽童视频脚本 | ✅ 通过。5 段/1825 字/5 Visual hints/抽查朗读 2 段不拗口。字数略低于 2000 下限，内容覆盖完整不阻塞 |
| 05-20 | 欧阳锋 | 🛑 Gate 1 审查：洪七公视频分镜 | ✅ 通过。34 帧/Bauhaus amber 非通用科技风/每句有画面/Style Guide 完整可执行 |
| 05-20 | 老顽童 | 🎬 KDO 视频脚本精炼 | ✅ 完成。01-script.md，5 段 full text + TTS 稿 |
| 05-20 | 洪七公 | 7a 视频分镜设计 | ✅ 完成。02-storyboard.md，34 帧 + Style Guide + Production Notes + Asset Checklist |
| 05-20 | 黄药师 | Task 13-14 scaffold 四缺陷修复 | ✅ `877c41a`，286 tests (+4)，0 回归。欧阳锋审查：A |
| 05-20 | 欧阳锋 | Task 13-14 审查 + AGENTS.md 新增强 9/10/11 三条铁律 | ✅ F-KDO-014/015/016 已写入禁止清单 |
| 05-20 | 老顽童 | scaffold 恢复 70/71 张卡 + lean-validation 二轮修复 | ✅ Savoia/Beck 各自独立 H4，内容正确 |
| 05-20 | 老顽童 | ⑨ 科学决策 35 PNG 审计 + ① 补 related | ✅ 审计报告 A，91%覆盖；① 3 wikilink 已补 |
| 05-20 | 老顽童 | v1.5 全库扫描 + scaffold 恢复后重扫 | 恢复前 54/89/72 → 恢复后 125/20/70 |
| 05-19 | 黄药师 | Task 11+12 完成 | ✅ skill-dir validation + KDO Build，282 tests PASS |
| 05-19 | 欧阳锋 | 黄药师 Task 11+12 审查 | A/代码良，A/实测通，⚠️ 全部未 commit |
| 05-19 | 老顽童 | ①+②+③ 三项完成 | ✅ 双三角修复 + Skill 修复 + Anthropic 编译 |
| 05-19 | 欧阳锋 | 老顽童①+②+③ 审查 | ✅ 双三角通过/设计域通过/Anthropic A-，2 小修 |
| 05-19 | 黄药师 | Task 10 Quality Gate v2 | ✅ --article + --skill + --all, 9 tests |
| 05-19 | 黄药师 | Task 9 Graph RAG 深化 | ✅ graph path + 跨域标注 + --health, 9 tests |
| 05-19 | 洪七公 | 双三角 VA + Excalidraw 重绘 | ✅ VA 158行 + `.excalidraw` 源文件 |
| 05-19 | 洪七公 | 角色自我定义 | ✅ `beikai-role-positioning.md`（296行，85技能×18领域） |
| 05-19 | 洪七公 | wiki 勘误 | ✅ 发现双三角归属错位，已记录 |
| 05-19 | 老顽童 | 双三角卡 Visual Analysis 节引用 | ✅ 引用洪七公 VA 产出 + 归属错位注释 |
| 05-19 | 欧阳锋 | 老顽童工作审查 | T1/T3 typo ✅，双三角卡 A-（2 结构问题），Anthropic 未开工 |
| 05-19 | 黄药师 | Task 8 graph stats | ✅ 4 tests, --json |
| 05-19 | 黄药师 | Task 7 graph rebuild --incremental | ✅ 5 tests, --full + incremental |
| 05-19 | 黄药师 | Task 6 kdo task 自动化 | ✅ 5 子命令 + 6 tests |

---

## 🔍 欧阳锋审查（老顽童 ①+②+③，2026-05-19）

### 待修（2 项，老顽童下次会话顺手修）

**1. Anthropic 卡 typo**：[[anthropic-官方发布创始人手册打造-ai-原生初创公司]] Line 105
- `创新者斗姄` → `创新者窘境`（Christensen 书名标准译名）
- 补 frontmatter `reviewed_by: 欧阳锋`

**2. 双三角卡结构微调**（建议，非阻塞）：[[yt-model-dual-triangle-competitiveness]]
- 两个 H4 攻击者当前在 `## Framework Gallery` 下，惯例应放在 `## Constraints & Boundaries`
- 不影响 v1.5 解析，不改也行

---

## 🔍 欧阳锋审查（黄药师 Task 11+12，2026-05-19）

**Task 11** `kdo validate --skill-dir`：A
- 递归扫描 SKILL.md → L1 五段检查 → PASS/FAIL/WARN 汇总 + JSON 输出
- 11 tests（TestSkillQualityGate×4 + TestValidateSkillDir×4 + TestSkillL1Structure + TestValidateAllAutoDetect×2）
- 实测 `ai-design-fundamentals` → PASS

**Task 12** KDO Build：A
- `--check` 工作空间完整性 · `--version` CHANGELOG + build_state · `--release` 全流程
- 11 tests（check/changelog/module guess/version state 全覆盖）
- 实测 `build --check` → PASS

**⚠️ 全部未 commit**：20 个文件（12 modified + 8 untracked），在 KDO repo 目录执行：
```bash
cd "C:\Users\Administrator\Knowledge Delivery OS 0.0.1"
git add -A
git commit -m "feat: Task 11+12 — skill-dir validation + KDO build system"
```

---

## 🔍 v1.5 修复策略（欧阳锋拍板 2026-05-20）

> 老顽童扫描结果：215 卡，125 pass / 20 fail / 70 warn。scaffold 恢复后 FAILED 从 89→20（所有 FAILED 均为 AT 缺失，非 scaffold 损害）。**scaffold 已修复（Task 13-14 ✅），阻塞解除。**

### 执行顺序

| 顺序 | Batch | 内容 | 卡数 | 每卡工作量 | 总估时 |
|:--:|-------|------|:--:|:--:|:--:|
| **1** | B | 缺外部攻击者（有 DU+AT，只缺 Critique） | ~69 | 30min | ~35h |
| **2** | A | 全信号缺失（ATK=0/DU=0/AT=0） | ~13 | 90min | ~20h |
| **3** | Warnings | 格式微调 + 手动审查（other 类） | ~72 | — | 穿插 |

### 为什么 B 先做

- B 卡已有 DU table 和 AT table，结构半成型，只差 `## Critique` + 2 个 H4 攻击者
- 每张 30min（查 2 个学者 → 写攻击段落 → scaffold 验证），做完 69 张后 FAILED 从 89 降到 ~20
- A 卡每张 90min（从零搭 Critique+DU+AT），但只有 13 张，放后面集中突破

### B 执行规范

每张 B 卡补：
```markdown
## Constraints & Boundaries

#### [学者名] — [攻击标题]
[2-3 句攻击论证，含具体引用来源]

#### [学者名] — [攻击标题]
[2-3 句攻击论证，含具体引用来源]
```

攻击者选择原则：
- pan-product 卡 → JTBD、精益创业、设计思维、系统动力学范式
- 两张卡不同攻击者（不重复用同一学者）
- 有紧迫感（"这个框架的边界在哪？什么时候失效？"）

### CLI 问题

`kdo validate --v15` 文本输出正常，`--json` 有编码问题但不影响使用。老顽童用文本输出即可。

### 穿插规则

每做完 5 张 B 卡 → 跑 `kdo validate --v15 --card <id>` 验证 → 穿插 1 张 Batch 3（T6/T7/T8）换脑。

---

## 🛑 欧阳锋审查：视频试点 Gate 0 + Gate 1（2026-05-20）

### Gate 0 — 老顽童脚本 `01-script.md`

| # | 门禁项 | 结果 | 证据 |
|:--:|------|:--:|------|
| 1 | 总字数 2000-2500 | ⚠️ 1825 | 比下限少 175 字，~7.3 分钟。内容覆盖完整，不阻塞 |
| 2 | 无占位残留 | ✅ | 0 `[Speaking point` 匹配 |
| 3 | 每段 Visual hint | ✅ | 5/5，具体可执行 |
| 4 | `kdo video validate --stage script` | ✅ | PASS |
| 5 | 欧阳锋抽查朗读 2 段 | ✅ | Seg 1 + Seg 3，短句无嵌套，一口气说完 |

**质量评定：A**。五段递进清晰，`--` 停顿可朗读，Visual hints 给出具体意象。字数偏少不阻塞——"快速上手指南"7.3 分钟长度合理。

### Gate 1 — 洪七公分镜 `02-storyboard.md`

| # | 审批项 | 结果 | 证据 |
|:--:|------|:--:|------|
| 1 | Style Guide 完整 | ✅ | 色彩/字体/动效/品牌/AVOID 全 |
| 2 | 每句有画面 | ✅ | 34 帧覆盖 5 段全部 speaking point |
| 3 | 非通用科技风 | ✅ | amber+黑底 Bauhaus，非蓝紫渐变 |
| 4 | `kdo video validate --stage storyboard` | ✅ | PASS |
| 5 | Production Notes 可执行 | ✅ | 5 个关键帧有具体实现说明 |

**质量评定：A**。分镜覆盖无遗漏，9 种视觉类型有区分度，Style Guide 有记忆点（Bauhaus + amber terminal），Asset Checklist 提前列出了依赖资产。

### 审批结论

- ✅ **Gate 0 通过** → 老顽童脚本任务关闭，回归 v1.5 修复主线
- ✅ **Gate 1 通过** → 洪七公可立即启动 7b-7d（Segment 1-3 画面制作）

### 提报记录

```
老顽童 [Script Stage 1] 已完成
路径：40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/01-script.md
欧阳锋审查：✅ Gate 0 通过

洪七公 [Storyboard Stage 7a] 已完成
路径：40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/02-storyboard.md
欧阳锋审查：✅ Gate 1 通过
```

---

## 🔍 洪七公文章审计（2026-05-19）

> 审计报告：[[60_feedback/corrections/art-audit-20260519-dual-triangle-batch]]

### 审计发现

| # | 严重级别 | 文件 | 问题 |
|---|:--:|------|------|
| 1 | 🔴 高 | `art_双三角纠错_v2.md` L51 | 归属错位："业务拆解"被归入创造力，原图属于场景；漏"善于解放思想" |
| 2 | 🟡 中 | `art_20260517_9c7a63cb` | source_refs 不完整（1 个→需 7+ 学术来源） |
| 3 | 🟡 中 | 两篇文章 | delivery_channel 不一致（wiki vs homework） |
| 4 | 🟡 中 | `art_20260517_9c7a63cb` | wiki_refs 不完整（1 个→需 3+） |

### 欧阳锋决策

1. **方案A**（推荐）：严格按原图修正——创造力子项改为"理解底层规律、善于解放思想、提出创造假设"，场景子项改为"业务拆解、ROI预判、AI打磨、组织部署"
2. **保留双版本**：`art_双三角纠错_v2`（wiki 渠道）+ `art_20260517_9c7a63cb`（统一为 wiki 渠道），标题区分受众
3. **执行人**：老顽童（15min）。修复完成后通知洪七公做多模态转换
4. **洪七公后续**：修复完成后，将 `art_双三角纠错_v2` 转为中视频 + TTS 播客 + 信息图

---

## 🔧 黄药师 Task 13-14：scaffold 紧急修复（P0）

> **触发**：老顽童 2026-05-20 跑 `kdo scaffold --batch B --write`，71 张卡的攻击者内容被清空。
> **根因**：scaffold 三个缺陷叠加（老顽童自检确认）。

### Bug 1：攻击者检测盲区（`_count_external_attacks`）

**位置**：`quality.py` L152-188

**问题**：只查 `## Critique` H2 节。旧格式卡攻击者内容放在 `## Framework Gallery` 下面，`_find_section(sections, "critique")` 返回 None → `atk_count = 0`。

### Bug 2：重复插入（`_insert_critique` 幂等缺失）

**问题**：卡片已有 `## Critique` 但 scaffold 判定缺攻击者时，`_insert_critique` 会在 `## Synthesis` 前插入**第二个** `## Critique` 块。老顽童发现 6 张卡出现双 Critique 节。

### Bug 3：内容丢弃（`_insert_critique` 覆盖替换）

**问题**：`_insert_critique` 插入新块时，旧攻击者正文未被保留——插入操作覆盖/替换了相邻旧内容。这是 71 张卡内容丢失的直接根因。

### Bug 4：validator 空 H4 不计内容

**位置**：`quality.py` L164-175

**问题**：H4 标题存在即计为攻击者，不检查标题下面是否有实质内容（≥100 字符）。

### 修复清单

| # | 改什么 | 位置 | 估时 |
|:--:|------|------|:--:|
| 1 | `_count_external_attacks` 增加 fallback——也检查 `## Framework Gallery` 下的 `### 外部攻击*` | quality.py L152 | 15min |
| 2 | `_insert_critique` 增加幂等检查——已有 `## Critique` 时只追加缺失 H4，不重建整个块 | quality.py L787 | 15min |
| 3 | `_insert_critique` 改为纯追加模式——绝不对已有内容做替换/覆盖 | quality.py L787 | 15min |
| 4 | H4 计数增加内容检查——下一个 H4/H3/H2 前纯文本 <100 字不计入 | validator 路径 | 15min |

### 验收

- `_count_external_attacks` 能识别 `## Framework Gallery` 下 `### 外部攻击*` 中的 `**学者名**` 格式
- 已有 `## Critique` 时不重复创建第二个
- `_insert_critique` 纯追加，不覆盖已有内容
- 空 H4（下面 <100 字正文）不计入攻击者计数
- 在 `yt-entrepreneur-key-hypotheses` 原始版本上 dry-run scaffold 返回 `None`（无需 scaffold）
- pytest ≥5 new tests：旧格式识别 / 双 Critique 幂等 / 内容保留 / 空 H4 拒绝 / dry-run 不误伤
- 不破坏现有 282 tests
