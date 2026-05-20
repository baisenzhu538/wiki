---
title: 任务仪表盘
updated: 2026-05-20 (Gate 0+1+2+3+4 条件通过 · 7a-7g ✅ · 待洪七公补 timing.md → ship)
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
| ⑥ | v1.5 全库修复（20 FAILED→0） | 质量 | ✅ | `kdo validate --v15` 结果 215 cards: 211 pass / 0 fail / 4 warn（4 warn 均为 research 卡缺 dont-use/external-attacks，非 tool/concept）。scaffold 自动修复 + 手动补充完成 |
|| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ✅ | T6 项目雷达 Flyvbjerg+Goldratt / T7 新人融入 Van Maanen&Schein+Edmondson / T8 股权清单 Coase+Williamson。3/3 kdo validate PASS |
| 🎬 | KDO 视频脚本精炼（Stage 1） | 视频 | ✅ | Gate 0 v2 通过 · A+。十指讲香 10/10 全命中，2219 字。kdo validate PASS |

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
|| **7** | ~~⑥ v1.5 全库修复（20 FAILED→0）~~ | ✅ 完成 | 分批 | `kdo validate --v15` 215 cards: 211 pass / 0 fail / 4 warn。scaffold 自动修复完成。残 4 warn 均为 research 卡 |
|| **8** | ~~⑦ 管理工具箱 Batch 3（T6+T7+T8）~~ | ✅ 完成 | 6h | 3/3 PASS。T6 Flyvbjerg+Goldratt / T7 Van Maanen&Schein+Edmondson / T8 Coase+Williamson |
|| **9** | 下一个任务等老朱指派 | ⏳ | — | 老顽童待命 |

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
| 16 | 🔥 `kdo video render` 修两个缺口（散文体+TTS） | **P0** | ✅ | `fa66855`。散文体提取 + edge-tts 集成。32 video tests，317 total |
| 17 | `kdo video render` 遗留缺陷（Seg5 TTS + compose 动态帧时长） | **P1** | ⏳ | 不阻塞当前试点 ship。Backlog。门禁见 [[huangyaoshi-next-tasks#Task 17：kdo video render 两个遗留缺陷（~1h P1）]] |

### 黄药师 — 当前任务

**Task 17 排队中** ⏳。Task 1-16 全部交付 ✅。Task 17（Seg 5 TTS 异常 + compose 动态时长）P1 backlog，不阻塞当前试点 ship。修完后用于后续视频项目。

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
| 7 | KDO 快速上手指南 → 中视频 | 🔨 | 7a-7g ✅。Gate 0-4 通过（Gate 4 条件通过 B+）。待洪七公补 timing.md → ship |

### 洪七公 — 视频流水线任务（Task 7 v2）

> **工作流**：[[40_outputs/capabilities/workflows/video-production-flow.md]]
> **原则**：每阶段独立 `/new` session，读入参文件→写出参文件，不靠记忆。
> **🛑 审批铁律**：**每一个节点都必须提报审查，无一例外。** 审查通过前**不得**进入下一阶段。不通过则标注修改点→修改→重新提报。

| 子任务 | 阶段 | 入参 | 出参 | 前置依赖 | 估时 | 🛑 审查节点 |
|:--:|------|------|------|------|:--:|------|
| **7a v2** | 分镜修订 | 新版 `01-script.md`（十指讲香版） | `02-storyboard.md` v2 | 老顽童 Gate 0 通过 | 45min | ✅ **Gate 1 通过 · A+**。40 帧，6/6 门禁全过。烹饪比喻 3 帧+墓碑独立设计+情绪弧线全覆盖 |
| 7b | 画面 Seg 1 | `02-storyboard.md` v2 | `frames/segment_1_*.png` | Gate 1 通过 | 30min | ✅ 完成（10 帧，17:54）。⚠️ 未提报即进入 7c——违规 |
| 7c | 画面 Seg 2 | `02-storyboard.md` v2 | `frames/segment_2_*.png` | 7b 提报完成 | 30min | ✅ 完成（7 帧，18:07）。⚠️ 未提报即进入 7d——违规 |
| 7d | 画面 Seg 3 | `02-storyboard.md` v2 | `frames/segment_3_*.png` | 7c 提报完成 | 30min | ✅ 完成（14 帧，18:39）。🛑 **Gate 2 通过**：用户初步看过，先跑通再迭代 |
| 7e | 画面 Seg 4 | `02-storyboard.md` v2 | `frames/segment_4_*.png` | Gate 2 通过 | 30min | 🛑 7e 完成后提报 |
| 7f | 画面 Seg 5 | `02-storyboard.md` v2 | `frames/segment_5_*.png` | Gate 2 通过 | 30min | ✅ 完成（6 帧，19:36）。7e→7f 间隔 8min，洪七公遵守停等信号（C-11 纪律已生效） |
| **7h** | 渲染合成 | `frames/` 全部 40 帧 | `draft/draft.mp4` | ✅ 黄药师 Task 16 完成 | 15min | ✅ 完成。draft.mp4: 11810 KB, 500.1s, H.264/AAC |
| 7g | 配音节奏审查 | `draft/draft.mp4` | `timing.md` → 实际产出 `03-qa-report.md` | 7h 完成 | 20min | ⚠️ **Gate 4 条件通过 · B+**。待修：拆出 `timing.md` + 补逐段时长表（15min）。[[#🛑 Gate 4 审查：洪七公 7g 音画对位]] |

**洪七公总估时**：~4.5h（含 7a v2 分镜修订 45min + 7h 渲染合成 15min）。`kdo video render` 是 CLI 命令，洪七公自行执行，不需要黄药师介入。`kdo video ship` 最后一步由段王爷执行。

### 🛑 审批节点总览（视频试点 v2）

```
老顽童 01-script.md（十指讲香版）
    │
    ▼
🛑 GATE 0 ✅ 通过 — 欧阳锋审查脚本（十指 10/10，A+）
    │
    ▼
洪七公 7a v2 修订分镜 ✅ Gate 1 通过 · A+
    │
    ▼
🛑 GATE 1 ✅ 通过（40 帧，烹饪比喻 3 帧+墓碑独立设计+情绪弧线全覆盖）
    │
    ▼
洪七公 7b Seg 1 ✅ → 7c Seg 2 ✅ → 7d Seg 3 ✅
    │  ⚠️ 7b/7c/7d 提报缺失（C-11 违规。纪律已写入 F-KDO-017 + beikai-role-positioning.md）
    │
    ▼
🛑 GATE 2 ✅ 通过 — 用户初步看过，31 帧先跑通再迭代
    │
    ▼
洪七公 7e Seg 4 ✅ → 7f Seg 5 ✅（7e→7f 间隔 8min，停等信号生效）
    │
    ▼
🛑 GATE 3 ✅ 通过 — 用户终检全部 5 段 40 帧画面（效果一般，先跑通流程）
    │
    ▼
黄药师 Task 16 ✅ — kdo video render 修复（fa66855）
    │
    ▼
洪七公 7h ✅ 渲染合成（draft.mp4: 11810 KB, 500.1s, H.264/AAC）
    │
    ▼
洪七公 7g ⚠️ 条件通过 · B+
    │
    ▼
🛑 GATE 4 ⚠️ 条件通过 — timing.md 命名不符 + 缺逐段时长表（15min 修正）
    │
    ▼
洪七公 补 timing.md → 欧阳锋复审 → 段王爷 kdo video ship → final.mp4
```

### 🛑 GATE 1 审查标准（分镜 v2）

新版脚本核心变化（旧分镜未覆盖的部分）：

| 新增元素 | 脚本中的位置 | 分镜必须回答的问题 |
|---------|------------|-----------------|
| 烹饪比喻系统 | Seg 2-3："炖成自己的汤""生肉→粥→上桌的菜" | 用什么视觉序列表达"烹饪"这个贯穿隐喻？不能只靠文字，要有画面 |
| 墓碑意象 | Seg 4："传统做法，文档写完就是墓碑" | 墓碑的视觉实现方式（墓碑上长草？文件图标裂成墓碑形状？） |
| 产品经理故事线 | Seg 4：完整人物+时间线+反转 | 是继续用左右分屏对比，还是改成单人叙事镜头？ |
| 4 层情绪弧线 | Seg 1："假象"→"焦虑"→"共情"→"狼狈" | 画面的色调/构图/节奏如何配合情绪递进？不能从头到尾一种调子 |
| 6 条金句 | 贯穿全文 | 每条金句出现时，画面如何处理？是黑底白字大字，还是配合意象？ |
| 5 处冲突反差 | "消费 vs 生产""墓碑 vs 开始"等 | 每次冲突出现时，画面是否有对比结构来呼应？ |

**门禁（通过标准，缺一不可）**：

| # | 门禁项 | 判定方式 |
|:--:|------|------|
| 1 | 新版脚本 5 段全部 speaking point 在分镜表中有对应帧 | 逐段对照，无遗漏 |
| 2 | 烹饪比喻有至少 3 帧的视觉序列支撑（生肉→粥→菜） | 分镜表中的 Visual Type 和 Description 具体到画面元素 |
| 3 | 墓碑意象有至少 1 帧的独立设计（不是通用文件图标） | 描述具体到墓碑的视觉形态和动画 |
| 4 | 5 段画面色调/节奏有区分，配合情绪弧线 | 分镜表中每段标注情绪关键词和色调方案 |
| 5 | Style Guide 保留（amber/black Bauhaus，非蓝紫科技风） | 不因内容变化而滑回通用科技风 |
| 6 | `kdo video validate --stage storyboard` 返回 PASS | 终端 exit 0 |

**🛑 审批**：

提报格式：
```
洪七公 [Storyboard v2] 已完成
路径：40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/02-storyboard.md
```

审批结果：
- **通过** → 欧阳锋通知洪七公进入 7b（Seg 1 画面）
- **修改** → 欧阳锋标注具体修改点（帧号+问题+期望），洪七公修改后重新提报

**🛑 节点**：你在 Gate 0（脚本已通过）和 7b（首次画面制作）之间。上游 = 老顽童（脚本已完成✅），下游 = 你自己的 7b-7g 在等你。

---

### 🛑 每个子任务的审批节点（7b∼7g）

**⚠️ 以下每个节点都必须提报，无一例外。跳过一个节点 = 违规。**

#### 7b — Seg 1 画面

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `frames/segment_1_*.png`，帧数与分镜表 Frame Map 一致 | 文件数量 + 命名匹配 |
| 画面风格符合 Style Guide（amber/black/Bauhaus） | 抽查 2 帧 |
| 关键帧到位：数字跳出动画（200+/50+/10+/713/1200）、"然后呢？"闪烁、"老板周一早"场景 | 逐帧对照分镜表 |

**审批**：7b 完成后立即提报——"洪七公 [7b Seg 1] 已完成，路径：frames/segment_1_*.png，请欧阳锋审查"。快速扫一眼不阻塞，但**必须报**。

#### 7c — Seg 2 画面

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `frames/segment_2_*.png` | 文件数量匹配 |
| 关键帧到位：三 App 图标+消费行为红叉、闭环循环动画、9 工序流水线 | 逐帧对照 |
| "消费行为 vs 生产行为"的对比结构在画面中可见 | 人审 |

**审批**：同 7b，完成后立即提报。

#### 7d — Seg 3 画面 + Gate 2

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `frames/segment_3_*.png` | 文件数量匹配 |
| 漏斗动画（9 节点依次闪烁）完整 | 人审 |
| 烹饪比喻视觉序列（≥3 帧）到位 | 逐帧对照门禁项 #2 |
| 溯源链时间轴（source→wiki→artifact）清晰 | 人审 |

**审批**：7d 完成后，连同 7b+7c 打包提报 Gate 2——"洪七公 [7b+7c+7d Seg 1-3] 已完成，请欧阳锋正式抽检"。**这是正式审查节点，不是快速扫一眼。** 欧阳锋抽查 2/3 段画面。

#### 7e — Seg 4 画面

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `frames/segment_4_*.png` | 文件数量匹配 |
| 墓碑意象到位（至少 1 帧独立设计） | 人审 |
| 产品经理故事线：左右对比 or 单人叙事，风格明确 | 人审 |

**审批**：完成后立即提报。

#### 7f — Seg 5 画面 + Gate 3

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `frames/segment_5_*.png` | 文件数量匹配 |
| 花园 vs 厨房的视觉对比清晰 | 人审 |
| 结尾"让你的知识值得被交付"的 CTA 画面有力 | 人审 |

**审批**：7f 完成后，连同全部 5 段画面打包提报 Gate 3——"洪七公 [7b-7f Seg 1-5 全部画面] 已完成，请欧阳锋终检"。**这是画面阶段的最终审查，逐段审查，不放水。**

#### 7h — 渲染合成（洪七公执行，非黄药师）

> ⚠️ `kdo video render` 是 CLI 命令，不是开发任务。**洪七公自行执行**，黄药师不介入。黄药师只负责建造工具（Task 15），不负责每次运行。

**执行步骤**：

```bash
# Step 1: 生成 TTS 配音
cd "C:\Users\Administrator\Desktop\wiki"
kdo video render --audio "40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产"

# Step 2: 合成视频（40 帧 + 配音 → draft.mp4）
kdo video render --compose "40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产"
```

| 🛑 门禁 | 判定方式 |
|------|------|
| `audio/` 目录下有 TTS 音频文件 | 文件存在 |
| `draft/draft.mp4` 存在且可播放 | 文件 > 1MB，ffprobe 可读 |
| 视频时长 8-10 分钟（对应 2219 字脚本） | ffprobe duration |

**审批**：7h 完成后提报——"洪七公 [7h 渲染合成] 已完成，路径：draft/draft.mp4，请欧阳锋审查"。欧阳锋快速确认 draft.mp4 可播放后，洪七公进入 7g。

#### 7g — 配音节奏审查 + Gate 4

| 🛑 门禁 | 判定方式 |
|------|------|
| 产出 `timing.md`，标注每段实际时长和需要调整的时间点 | 文件存在 + 结构化 |
| 对音画不同步的位置有具体修正标注 | 至少 3 处具体标注 |

**审批**：7g 完成后提报 Gate 4——"洪七公 [7g 配音节奏审查] 已完成，路径：timing.md，请欧阳锋审查"。欧阳锋审时间轴→黄药师合成→欧阳锋终审 draft.mp4。

---

### ⚠️ 禁止事项

- **禁止**：审查通过前自行进入下一阶段
- **禁止**：跳过任何一个审批节点（包括 7b/7c/7e 的"快速提报"——快速 ≠ 跳过）
- **禁止**：在一个 session 里连续做多个阶段不报批
- **禁止**：换 session 后不重新读入参文件，凭记忆续做

跳步后果：产出质量不可控（参 C-8：格式完整但思维空洞）。

## 段王爷（Publisher · 飞书 Hermes）

> **定位**：发布管线。`kdo ship`→渠道分发、反馈收集、版本发布记录。
> **输入**：`dashboard` 任务 + `40_outputs/` 待发布 artifact
> **输出**：`50_delivery/` 发布记录 · `50_delivery/channels/` 渠道配置 · `60_feedback/comments/` + `issues/`

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 1 | 🎬 KDO 视频试点 ship | ⏳ | 前置：洪七公补 timing.md → Gate 4 正式放行。`kdo video ship` → 记录交付事件 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 洪七公 | 7g timing.md 修正 | ⚠️ 拆出 `timing.md` + 补逐段时长表，15min。完成后 → ship |
| 黄药师 | Task 17 Seg5 TTS + compose 动态时长 | ⏳ P1 backlog。不阻塞当前试点，修完后用于后续视频项目 |
| 老顽童 | v1.5 全库修复（20 FAILED） | 🔨 可随时启动 |
| 老顽童 | 🔧 4 项顺手修（Anthropic typo + 双三角文章归属+引用） | 积压，可随时清 |
| 老顽童 | v1.5 全库修复（20 FAILED） | scaffold 已修好，可随时启动 |
| 洪七公 | `art_双三角纠错_v2` 修复后→多模态转换 | 等老顽童修完归属错位 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-20 | 欧阳锋 | 🛑 Gate 4 审查：洪七公 7g 音画对位 | ⚠️ 条件通过 · B+。待补 timing.md 逐段时长表（15min） |
| 05-20 | 洪七公 | 7g 音画对位审查 | ⚠️ 完成。产出 `03-qa-report.md`（非 `timing.md`）。draft.mp4: 500.1s, H.264/AAC。发现 Seg 5 TTS 异常 + compose 均匀分配问题 |
| 05-20 | 洪七公 | 7h 渲染合成 | ✅ 完成。draft.mp4 生成：11810 KB, 500.1s, H.264/AAC |
| 05-20 | 黄药师 | Task 16 kdo video render 修复 | ✅ `fa66855`。散文体提取 + edge-tts 集成。32 tests, 317 total |
| 05-20 | 洪七公 | 7f Seg 5 画面（6 帧） | ✅ 完成。7e→7f 间隔 8min，遵守停等信号（C-11 纪律生效） |
| 05-20 | 洪七公 | 7e Seg 4 画面（3 帧） | ✅ 完成。Gate 2 通过后执行，7d→7e 间隔 49min |
| 05-20 | 欧阳锋 | 🛑 Gate 2 审查：7b+7c+7d 三段画面 | ✅ 通过。用户初步看过，31 帧可接受，先跑通再迭代 |
| 05-20 | 欧阳锋 | 🛑 C-11 违规处理：洪七公跳步 | ✅ F-KDO-017 写入 AGENTS.md，C-11 写入 corrections.md，审批纪律写入 beikai-role-positioning.md |
| 05-20 | 洪七公 | 7d Seg 3 画面（14 帧） | ✅ 完成但未提报（18:39）。⚠️ 7b→7c→7d 连续产出无审批——C-11 违规 |
| 05-20 | 洪七公 | 7c Seg 2 画面（7 帧） | ✅ 完成但未提报（18:07）。⚠️ 跳步 |
| 05-20 | 洪七公 | 7b Seg 1 画面（10 帧） | ✅ 完成但未提报（17:54）。⚠️ 触发 C-11 调查 |
| 05-20 | 欧阳锋 | 🛑 Gate 1 审查：洪七公分镜 v2 | ✅ 通过 · A+。40 帧，6/6 门禁全过。烹饪比喻 3 帧+墓碑独立设计+Emotional Arc Guide |
| 05-20 | 洪七公 | 7a v2 分镜修订（对齐十指讲香脚本） | ✅ 完成。02-storyboard.md v2，34→40 帧，新增情绪弧线章节 |
| 05-20 | 欧阳锋 | 🛑 Gate 0 复审：老顽童脚本（十指讲香版） | ✅ 通过 · A+。十指 10/10 全命中，烹饪比喻贯穿+墓碑意象+4层情绪弧。2219 字，kdo validate PASS |
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

## 🛑 欧阳锋审查：视频试点（2026-05-20）

### Gate 0 v1 — 老顽童脚本（初版）❌ 驳回

初版脚本格式门禁全过，但用户（欧阳锋）指出：**内容停在"清单式讲香"，未使用十指讲香方法论**。驳回，要求按十指双向拉伸重写。

驳回理由：
- 把 9 步 CLI 命令平铺罗列 → 清单式讲香（十指模型 claim:03 典型翻车）
- 缺比喻系统、缺情绪弧线、缺冲突结构、缺故事化

### Gate 0 v2 — 老顽童脚本（十指讲香版）✅ 通过 · A+

| # | 门禁项 | 结果 | 证据 |
|:--:|------|:--:|------|
| 1 | 总字数 2000-2500 | ✅ 2219 | 在目标范围内 |
| 2 | 无占位残留 | ✅ | 0 `[Speaking point` 匹配 |
| 3 | 每段 Visual hint 增强 | ✅ | 5/5，墓碑动画/钟表倒计时/消费行为红叉 |
| 4 | `kdo video validate --stage script` | ✅ | PASS |
| 5 | 欧阳锋抽查朗读 | ✅ | Seg 1 + Seg 4，节奏感+情绪张力显著优于初版 |

**十指讲香逐指审查**：十指 10/10 全命中。烹饪比喻（生肉→粥→菜）作为贯穿隐喻，墓碑 vs 开始的冲突结构作为全文最强记忆钩子，4 层情绪递进（假象→焦虑→共情→狼狈）有弧线。

### Gate 1 v1 — 洪七公分镜（旧脚本版）⚠️ 废止

旧分镜（34 帧，Bauhaus Style Guide）质量 A，但基于旧脚本制作。新版脚本新增的烹饪比喻系统、墓碑意象、产品经理故事线、4 层情绪弧线在旧分镜中无对应。**要求洪七公执行 7a v2（分镜修订）对齐新版脚本。**

### Gate 1 v2 — 洪七公分镜修订 ✅ 通过 · A+

**审查结果**：6/6 门禁全过。40 帧（v1 34→v2 40），新增 Emotional Arc Guide 章节+每帧情绪列+烹饪比喻 3 帧视觉序列+墓碑独立设计+金句特殊处理。`kdo video validate` PASS。

### 审批节点状态

```
🛑 GATE 0 ✅ A+
🛑 GATE 1 ✅ A+
🛑 GATE 2 ✅ 用户初步通过
🛑 GATE 3 ✅ 用户终检通过
🛑 GATE 4 ⚠️ 条件通过 · B+（洪七公补 timing.md 后放行 ship）
```

---

### 🛑 Gate 4 审查：洪七公 7g 音画对位（2026-05-20）

**结论：有条件通过。B+。不阻塞 ship。**

| # | 门禁 | 结果 |
|:--:|------|:--:|
| 1 | draft.mp4 存在 + 可播放 | ✅ 11810 KB, H.264/AAC, 1920×1080 |
| 2 | 视频时长 8-10 分钟 | ✅ 500.1s (8.3min) |
| 3 | `kdo video validate` PASS | ✅ |
| 4 | 至少 3 处音画同步修正标注 | ✅ 4 处 |
| 5 | 产出 `timing.md` | ⚠️ 产出 `03-qa-report.md`（内容等效，命名不符规范） |

**待修（洪七公 15min）**：
1. 从 `03-qa-report.md` 拆出独立 `timing.md`
2. 补逐段时长表（Seg 1-5 × 帧范围 × 脚本标注 × 音频实测 × 建议帧时长）
3. Seg 5 TTS 异常（558.5s→预期 ~60s）记录供黄药师排查

**审查记录已写入** `03-qa-report.md` 底部。

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
