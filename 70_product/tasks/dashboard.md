---
title: 任务仪表盘
updated: 2026-05-19
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 批次 | 状态 | 备注 |
|---|------|------|------|------|
| ① | 补 related 边 | — | ⏳ | 3 条 wikilink + frontmatter relation |
| ② | 双三角文章 v2 | — | ✅ | 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1（F1+T1+T2） | 工具箱 | ✅ | 全 A。T1 typo 已修 ✅ |
| ④ | 管理工具箱 Batch 2（T3+T4+T5） | 工具箱 | ✅ | T3 A / T4 A+ / T5 A。T3 typo 已修 ✅ |
| 🔍 | 双三角卡结构修复 | — | ✅ | H3→H4 ✅ + 删重复 related ✅。⚠️ 攻击者在 Framework Gallery 下，建议移入 Constraints & Boundaries |
| 🆕 | Anthropic AI 原生初创手册 | 素材编译 | ✅ | A-。Christensen+Pfeffer 攻击精准，5 ATs。⚠️ `创新者斗姄`→`创新者窘境`，补 `reviewed_by` |
| ⑤ | 设计域 S1+S2+S3 skill | 洪七公+段王爷 | ✅ | 命名+格式+五段式全修。3/3 通过 |
| 🆕 | 科学决策域 35 PNG 增强消化 | 增强 | ⏳ | OCR+交叉比对，老顽童自闭环 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 89 卡修复间隙 |

### 老顽童 — 执行顺序（从上到下，做完一个再看下一个）

| 顺序 | 任务 | 内容 | 估时 | 备注 |
|:----:|------|------|:--:|------|
| **1** | ~~🔍 双三角卡结构修复~~ | ✅ 完成 | 5min | 欧阳锋复审：通过。⚠️ 攻击者在 Framework Gallery 下，建议移入 Constraints & Boundaries |
| **2** | ~~🔧 设计域 Skill 命名+格式修复~~ | ✅ 完成 | 15min | 欧阳锋复审：通过。3/3 全修 |
| **3** | ~~🆕 Anthropic 创始人手册~~ | ✅ 完成 | 2h | 欧阳锋复审：A-。⚠️ 修 typo `斗姄`→`窘境`，补 `reviewed_by` |
| **4** | ~~⑤ 设计域 S1+S2+S3 复审~~ | ✅ 欧阳锋已复审 | — | 三 skill 内容 A，格式完备，闭环 |
| **5** | ① 补 related 边 ← **下一个** | 3 张卡的 wikilink + frontmatter relation | 30min | 详见 [[70_product/tasks/laowantong-next-tasks#① 补 related 边（立即，30min）]] |
| **6** | 🆕 科学决策域 35 PNG 增强消化 | OCR+交叉比对→查漏补缺 | 3h | 老顽童自闭环（含 OCR）。详见 [[70_product/tasks/laowantong-next-tasks#⑨ 科学决策域 35 PNG 增强消化]] |
| **7** | ⑥ v1.5 全库修复（89 FAILED） | scaffold 分批修 | 分批 | 穿插 ⑦ Batch 3（T6+T7+T8，换脑休息） |
| **8** | ⑦ 管理工具箱 Batch 3（T6+T7+T8） | 穿插在 ⑥ 间隙 | 6h | T6 项目雷达 / T7 新人融入 / T8 股权清单 |

> **规则**：顺序执行，不跳。每完成一个 → 跑验证 → 通知欧阳锋审查。不要等批次全部完成。

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

### 黄药师 — 当前任务

**Task 1-12 全部完成** ✅。282 tests pass。**⚠️ 20 个文件未 commit**，详见 [[70_product/tasks/huangyaoshi-next-tasks#🔍 欧阳锋审查（2026-05-19）]]。

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
| 5 | 通道就绪确认 | ⏳ | 确认能读写上述输入/输出路径 |

## 段王爷（Publisher）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 黄药师 | Task 11+12 全部未 commit | 20 个文件（12 modified + 8 untracked），需 commit |
| 老顽童 | Anthropic 卡 typo `斗姄`→`窘境` + 补 `reviewed_by` | 审查发现，修完即关 |
| 老顽童 | 双三角攻击者位置（Framework Gallery → Constraints & Boundaries） | 建议移，非阻塞 |
| 洪七公 | 通道就绪确认 | 确认能读写输入/输出路径 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
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
