---
id: diag_20260709_yitang-expression-pitch-increment-deep-dive
title: 个人修炼·表达力与讲香十指（增量）域诊断与入队建议
type: diagnosis
status: active
source: 讲香十指模型口述版（阿蕊 3504 行）+ 表达力火箭模型/执行武器库 OCR + 30_wiki 现有个人表达域散卡
source_refs:
  - 00_inbox/一堂-个人修炼-讲香十指模型口述版.txt L36-L80,L46-L52,L56-L80
  - 00_inbox/一堂-个人修炼-讲香基本功_paddle_ocr.txt
  - 00_inbox/一堂-个人修炼-讲香十指模型-超级武器库_paddle_ocr.txt
  - 00_inbox/一堂-个人修炼-讲香基本功-十指模型修炼地图_paddle_ocr.txt
  - 00_inbox/一堂-个人修炼-表达力火箭模型_paddle_ocr.txt L1-L6
  - 00_inbox/一堂-个人修炼-表达力火箭模型-执行武器库_paddle_ocr.txt
  - 30_wiki/concepts/yt-model-personal-pitch-toolkit.md
  - 30_wiki/concepts/yt-personal-scientific-expression.md
  - 30_wiki/concepts/yt-personal-verbatim-script.md
  - 30_wiki/tools/tool-讲香基本功-十指模型.md
  - 30_wiki/tools/tool-讲香十指模型-超级武器库.md
  - 30_wiki/raw/ocr/ocr-一堂-个人修炼-表达力火箭模型.md
  - 30_wiki/raw/ocr/ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md
reviewer: 欧阳锋
created_at: 2026-07-09
updated_at: 2026-07-09
related:
  - "[[yt-personal-scientific-expression]]"
  - "[[yt-model-personal-pitch-toolkit]]"
  - "[[yt-personal-verbatim-script]]"
  - "[[tool-讲香基本功-十指模型]]"
  - "[[tool-讲香十指模型-超级武器库]]"
  - "[[ocr-一堂-个人修炼-表达力火箭模型]]"
  - "[[ocr-一堂-个人修炼-表达力火箭模型-执行武器库]]"
  - "[[task_20260709_wangyuyan-expression-pitch-agent]]"
---

# 个人修炼·表达力与讲香十指（增量）域诊断与入队建议

## 执行摘要

本域是「个人修炼·练能力」模块的**输出层**：上游（产品内核、动力阻力、卖点）找准之后，如何把卖点"讲得让人听得进去、完成兴趣-信任-转化"。5 月已就"讲香本体"早期挖过一轮（`domain-xiang-jiang-deep-digestion`，2026-05-13），沉淀了 `yt-pitch-*` 10 张技巧卡 + 1 张 toolkit 框架卡 + 2 张讲香工具卡 + 1 张科学表达卡 + 1 张逐字稿卡。

经 Grep/Read 前置审计，结论如下：

1. **讲香十指口述版 = 部分萃取**：十指"术/how"层已萃取进 `yt-pitch-*`（source_refs 确为口述版迁移路径），但"道/why"层（两年团队基本功、卖点直给导致数据差、封装成必修课的来龙去脉）**无卡承接**，且 toolkit 框架卡/超级武器库卡的 source **错位**到 hackathon summary 与 VLM 图描述，而非口述版。
2. **表达力火箭模型并非"完全无卡"**：存在一张早期 tool 卡 `yt-personal-scientific-expression`（科学表达/火箭模型，2026-05-06，黄药师审、写审分离前），但来源单一（仅"执行武器库"OCR）、`domain: src_unknown`、related 大量 `src_unknown`，且"火箭模型"本体 OCR 与"执行武器库"OCR **未分别升级为正式知识卡**。
3. **三大真空**：表达力**总框架卡**（统摄火箭模型+十指讲香+逐字稿+刻意练习+灵感闪念）缺失；表达力 **agent-spec** 缺失；本域**诊断报告**缺失（本报告即补位）。

**深挖价值：中-高（B+/A-），但必须带前置审计**——动手前先校正现有散卡的来源错位、补萃取口述版 why 层、把 OCR 升级为正式卡，避免重复造卡。建议入队 `#148`，P1，依赖 `#136 销售`（卖点输入）、`#143 双三角诊断 Agent`（域入口协议）、`#144 P-23 能力中台 Phase 1`（共享底座）。

---

## 一、讲香十指口述版萃取核对结论（已萃取 / 未萃取 / 部分萃取）

**总体判定：部分萃取。** 口述版（阿蕊主讲，全篇 3504 行）的"术"被挖过，"道"被漏掉，且总纲卡来源错位。

| 层面 | 口述版内容（行号） | 萃取状态 | 承接卡 / 证据 |
|---|---|---|---|
| 术·十指技巧 | 故事化/数字化/隐喻/金句/口语化/冲突/情绪/具象/场景/升华 | ✅ **已萃取** | `yt-pitch-*` 10 张，source_refs = `10_raw/sources/一堂-个人修炼-讲香十指模型口述版.md`（即本口述版迁移路径，见 `yt-pitch-storytelling.md` L6-L7、`yt-pitch-quantification.md` L6-L7） |
| 术·武器库/修炼地图 | 十指分工、入门→进阶→精通路径 | ⚠️ **错位萃取** | `tool-讲香十指模型-超级武器库`（source=`_vlm_reprocess/...超级武器库_vlm_desc.md`）、`tool-讲香基本功-十指模型`（source=`...修炼地图_vlm_desc.md`）——来源是 VLM 图描述，**非口述版**，正文含大量"待补充"与 `pending_unknown` |
| 纲·十指框架总卡 | 十指作为整体框架 | ⚠️ **来源错位** | `yt-model-personal-pitch-toolkit` source_refs = `src_20260614_8bd357d3-theme-ai-hackathon-pitches-summary.md`（**hackathon 摘要，非口述版**），`domain: src_unknown` |
| 道·为什么要学 | L36-L52：两年带团队练的基本功、线下训练营局部封装、新学期正式封装为必修课 | ❌ **未萃取** | 无卡承接"讲香是怎么从内部基本功变成必修课"的来龙去脉 |
| 道·核心痛点 | L62-L80：卖点找准了，但"直男式/直给式"把产品内核那句话直接吐出去 → 数据很差 | ❌ **未萃取** | 无卡承接"卖点直给 → 数据差"这条最关键的动机链（这是十指模型存在的理由） |
| 道·上下游承接 | L56-L60：与科学销售、最佳转化率、产品内核、动力阻力的承接关系 | ❌ **未萃取** | 无卡明确"讲香是产品内核/卖点的下游输出层" |

**核对要点**：Grep `讲香十指模型口述版` 仅命中 `index.md` 与 `yt-pitch-storytelling/quantification/metaphor`（证实 `yt-pitch-*` 来自口述版）；而 toolkit/超级武器库/修炼地图三张"纲"卡均**不**引用口述版。这就是"术得道失、纲源错位"的根因。

---

## 二、表达力火箭模型缺口（核实后修正初步判断）

> 前置审计修正：初步判断"2 张 OCR 完全无卡"**不精确**。Grep `表达力火箭` 命中 `30_wiki/concepts/yt-personal-scientific-expression.md`——即"科学表达（火箭模型）"卡已存在，但有如下缺陷，故实质缺口仍成立。

| 素材 | 现有承接 | 缺陷 | 缺口性质 |
|---|---|---|---|
| 火箭模型本体 OCR（`...表达力火箭模型_paddle_ocr.txt` L1-L6：有卖点/有专业度/打动人/逐字稿 四要素） | `raw/ocr/ocr-一堂-个人修炼-表达力火箭模型.md`（draft，conf 0.6，low trust，正文大量 `src_unknown`/待补充，仅为 OCR 卡非知识卡） | 未升级为正式 framework；与 scientific-expression 卡关系未厘清 | **本体无正式卡** |
| 执行武器库 OCR（`...执行武器库_paddle_ocr.txt`） | `yt-personal-scientific-expression` 的 source_refs 仅引用此一份 OCR（`10_raw/...ocr-...执行武器库.md` 旧路径） | 来源单一；卡为 2026-05-06 早期 enriched、黄药师审（写审分离前）、`domain: src_unknown`、related 含 `src_unknown` | **武器库未独立成 tool 卡** |
| 表达力总纲（火箭模型+十指讲香+逐字稿+刻意练习+灵感闪念的统摄） | 无 | `scientific-expression` related 已挂 `yt-model-personal-pitch-toolkit`/`yt-personal-verbatim-script`/`yt-personal-deliberate-practice`/`yt-personal-inspiration-flash`，说明散卡已具备但**无人串成总框架** | **总框架真空** |
| 表达力 Agent | 无 | `.agent/prompts/` 下无表达力 coach/orchestrator | **agent-spec 真空** |

---

## 三、素材证据

### 3.1 口述稿（主证据）

- `00_inbox/一堂-个人修炼-讲香十指模型口述版.txt`（阿蕊主讲，全篇 3504 行）
  - L36-L52：两年带团队练的基本功；线下训练营曾局部封装；新学期第一节正式把"讲项基本库里一个很核心的模块封装成一节必修课"。
  - L56-L60：承接科学销售、最佳转化率、产品内核——强调"把点找准"（卖点/产品内核/动力阻力）。
  - L62-L80：高速吹风机案例（高速吹干/非常安静/颜值好看）→ 找准卖点后"直男式、直给式"直接讲出去 → 销售文案/落地页/直播话术/短视频"干啦啦把产品内核那句话吐出去" → **数据很差**。这是十指模型存在的根本动机。

### 3.2 OCR / 模型图（结构证据）

| 文件 | 关键信息 | 当前 wiki 承接 |
|---|---|---|
| `00_inbox/一堂-个人修炼-表达力火箭模型_paddle_ocr.txt` L1-L6 | 四要素：有卖点 / 有专业度 / 打动人 / 逐字稿（YITANG EXPRESSIVE ROCKET MODEL） | 仅 OCR 卡，无正式 framework |
| `00_inbox/一堂-个人修炼-表达力火箭模型-执行武器库_paddle_ocr.txt` | 火箭模型可执行武器库（内容主体） | 被 `scientific-expression` 单一引用，未独立成卡 |
| `00_inbox/一堂-个人修炼-讲香基本功_paddle_ocr.txt` | 讲香基本功总图 | `raw/ocr/ocr-一堂-个人修炼-讲香基本功.md` |
| `00_inbox/一堂-个人修炼-讲香十指模型-超级武器库_paddle_ocr.txt` | 十指武器库 | `tool-讲香十指模型-超级武器库`（经 VLM，待补充多） |
| `00_inbox/一堂-个人修炼-讲香基本功-十指模型修炼地图_paddle_ocr.txt` | 入门→进阶→精通路径 | `tool-讲香基本功-十指模型`（经 VLM） |

---

## 四、wiki 现状（已核实）

| 卡 | 类型 | 状态 | 来源 | 主要问题 |
|---|---|---|---|---|
| `yt-pitch-aphorism/colloquialization/conflict/emotionalization/materialization/scenarization/sublimation`（concepts）+ `yt-pitch-metaphor/quantification/storytelling`（tools） | concept/tool | enriched | 口述版 ✅ | 来源正确，但 `prerequisites/component_of/query_triggers` 多 `src_unknown`，related 含 `pending_unknown` |
| `yt-model-personal-pitch-toolkit` | framework(concepts/) | enriched | hackathon 摘要 ❌ | 纲卡来源错位，非口述版 |
| `tool-讲香十指模型-超级武器库` | tool | reviewed | VLM 图描述 | 待补充多、related=pending_unknown |
| `tool-讲香基本功-十指模型` | tool | reviewed | VLM 图描述 | 来源非口述版 |
| `yt-personal-scientific-expression`（科学表达/火箭模型） | tool(concepts/) | enriched | 仅执行武器库 OCR | 早期卡、来源单一、domain=src_unknown |
| `yt-personal-verbatim-script`（逐字稿） | concept | enriched | personal-growth summary | 早期卡、与火箭模型"逐字稿"要素未对齐 |
| `ocr-一堂-个人修炼-表达力火箭模型` / `...执行武器库` | raw OCR | draft | OCR | 非正式知识卡 |

**已有散卡族**（科学表达、十指讲香、逐字稿、刻意练习 `yt-personal-deliberate-practice`、灵感闪念 `yt-personal-inspiration-flash`）已具备"个人表达域"雏形，**缺一张总框架卡把它们串成可导航链路**，并缺一个 coach Agent 做表达诊断。

---

## 五、深挖价值与前置审计

**价值评级：中-高（B+/A-）。**

- **素材扎实**：1 份 3504 行口述版（含完整 why/how/案例）+ 5 份 OCR/模型图（火箭模型、执行武器库、讲香基本功、超级武器库、修炼地图），理论自洽。
- **承上启下**：本域是 `#136 销售`、`产品内核/卖点` 的**下游输出层**——卖点找准之后，靠表达力完成"兴趣-信任-转化"。补它能把"找准卖点 → 讲好卖点"闭环打通。
- **Agent 需求真实**：用户持续要求"深挖→生产 agent"；表达力 coach（诊断听众-目的-卖点-十指组合-逐字稿）是个人修炼域天然入口。

**前置审计（动手前必做，避免返工/重复造卡）**：

1. 校正 `yt-model-personal-pitch-toolkit` 的 source 错位——补引口述版 L36-L80，纳入 why 层。
2. 口述版补萃取：新增"卖点直给 → 价值感"动机卡，把 L62-L80 数据差案例固化，避免再造一张重复纲卡。
3. 火箭模型本体 OCR（draft）升级为正式 framework；执行武器库 OCR 升级为 tool；与 `scientific-expression` 卡关系明确（合并/分工），避免三张卡讲同一件事。
4. 明确总框架卡与既有散卡（逐字稿/刻意练习/灵感闪念/十指）的边界——总框架只做导航与统摄，不重写子卡内容。

---

## 六、建议新建 / 升级清单（移交任务 spec）

| # | id | 类型 | 优先级 | 说明 |
|---|---|---|---|---|
| 1 | `framework-一堂-个人表达力` | framework | P0 | 表达力总框架：火箭模型（纲）+ 十指讲香（术）+ 逐字稿（控制）+ 刻意练习/灵感闪念（训练）的统摄导航 |
| 2 | `agent-一堂-个人表达力教练` | agent-spec | P0 | 表达力 coach：诊断听众/目的/卖点 → 选十指组合 → 逐字稿 → 演练；含 System Prompt、TCPR、工作流 |
| 3 | `concept-讲香-卖点直给到价值感` | concept | P0 | 口述版 why 层补萃取：L62-L80 卖点直给导致数据差 → 十指把价值点拉成价值感 |
| 4 | `framework-一堂-表达力火箭模型` | framework | P1 | 火箭模型本体正式卡：四要素 + 与 scientific-expression 卡关系厘清 |
| 5 | `tool-一堂-表达力火箭模型-执行武器库` | tool | P1 | 执行武器库 OCR 升级为可执行 tool |
| 6 | `yt-model-personal-pitch-toolkit` 升级 | framework | P2 | source_refs 补引口述版 L36-L80；related 关联总框架与 why 卡 |
| 7 | `yt-personal-scientific-expression` 升级 | tool | P2 | 与火箭模型本体卡分工；related 关联总框架；清理 src_unknown |
| 8 | `tool-讲香十指模型-超级武器库` / `tool-讲香基本功-十指模型` 升级 | tool | P2 | related 关联总框架；补"待补充"段落（最低限度） |
| 9 | `yt-pitch-*` 10 张 related 升级 | concept/tool | P2 | related 关联总框架卡，形成可导航链路 |

**预计新增卡：5 张 wiki 卡 + 1 张 agent-spec**；P2 升级约 12 张现有卡（仅 related/source_refs/最低限度补全，不重写正文）。

---

## 七、最终判断

**评级：B+/A-（中-高价值，增量补全 + 前置审计校正）**

- 来源可靠：口述版（阿蕊 3504 行）+ 5 份模型图 OCR，why/how/案例齐全。
- 不重复造轮子：本任务核心是"补 why、正纲源、升 OCR、串总纲、加 Agent"，而非重写已有 `yt-pitch-*`。
- 闭环价值：打通"找准卖点（#136/产品内核）→ 讲好卖点（本域）"的转化链路。

**建议入队编号**：`#148`
**任务名称**：`task_20260709_wangyuyan-expression-pitch-agent`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：5 张 wiki 卡 + 1 张 agent-spec + 约 12 张现有卡 related/source 升级
**依赖**：依赖 `#136 销售`（卖点/产品内核输入）、`#143 跨域双三角诊断 Agent`（域注册与入口协议）、`#144 P-23 能力中台 Phase 1`（共享能力底座）；建议三者定稿后启动，避免 agent 路由与 shared 工具返工

---

*王语嫣 2026-07-09*
