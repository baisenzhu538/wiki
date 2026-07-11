---
id: diag_20260709_yitang-personal-learning-method-deep-dive
title: 个人修炼·学习方法域（IPO + 科学提问 + 思维模型 + 知识萃取）深挖诊断报告
type: diagnosis
status: active
source: 00_inbox/ideas, 00_inbox/AI-study, 00_inbox（个人修炼口述 + 科学学习IPO/科学提问 OCR）
source_refs:
  - 00_inbox/ideas/一堂-个人修炼-IPO模型实操课口述.md L18-L58（IPO 是一堂第一课、学习能力=IPO 速度和质量、三价值；全篇 3378 行）
  - 00_inbox/AI-study/一堂-AI学习-科学提问口述.txt L96,L396,L432-L436,L1070（3010 行）+ 00_inbox/AI-study/cleaned/一堂-AI学习-科学提问口述_cleaned.md（2957 行）
  - 00_inbox/一堂-个人修身-思维模型口述版.md L8,L18,L1072-L1086,L2756（3022 行）+ 00_inbox/ideas/一堂-个人修身-思维模型口述版.md（3035 行，同名副本）
  - 00_inbox/一堂-个人修炼-知识萃取探索营口述版.md L22-L36,L48,L80,L96（3094 行）+ 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md（3107 行，同名副本）
  - 00_inbox/一堂-个人修炼-科学学习IPO-全景策略_paddle_ocr.txt（60 行，全景策略图 V2.0：Goal/Input/Process/Output/Feedback）
  - 00_inbox/一堂-个人修炼-科学学习IPO完整清单_paddle_ocr.txt（51 行，IPO 各模块对应课程/服务清单）
  - 00_inbox/一堂-个人修炼-科学学习IPO模型_paddle_ocr.txt（0 行，空文件，需走 _vlm_reprocess 补 OCR）
  - 00_inbox/一堂-个人修炼-提问刻意练习画布_paddle_ocr.txt（13 行，4 段位 × 向谁提问/目标/难度/场景/套路/工具箱）
  - 00_inbox/一堂-个人修炼-科学提问刻意练习_paddle_ocr.txt（8 行，科学提问刻意练习成长地图）
reviewer: 欧阳锋
reviewed_by: 欧阳锋
created_at: 2026-07-09
updated_at: 2026-07-09
related:
  - "[[yt-personal-ipo-learning]]"
  - "[[yt-model-ipo-learning-strategy]]"
  - "[[yt-model-ipo-complete-checklist]]"
  - "[[tool-科学学习IPO完整清单]]"
  - "[[tool-Truman-AI时代IPO模型重构]]"
  - "[[yt-model-questioning-practice-canvas]]"
  - "[[yt-model-scientific-questioning-map]]"
  - "[[tool-提问刻意练习画布]]"
  - "[[tool-科学提问刻意练习]]"
  - "[[yt-personal-thinking-models]]"
  - "[[yt-personal-knowledge-extraction]]"
  - "[[yt-tool-knowledge-extraction]]"
  - "[[yt-decision-y-model]]"
  - "[[framework-yitang-y-model-cross-domain-fusion]]"
  - "[[modeling-personal-practice-loop]]"
---

# 个人修炼·学习方法域深挖诊断报告（IPO + 科学提问 + 思维模型 + 知识萃取）

## 执行摘要

本域是「个人修炼」系列里**最契合"有口述稿但 wiki 缺失"特征**的一块：IPO、科学提问、思维模型、知识萃取四个子域**各自都有 3000+ 行完整口述稿 + OCR 模型图**，素材完整、理论自洽；但 wiki 层面四个子域**各自只有零散的概念卡/工具卡（IPO 5 张、提问 4 张、思维模型 1 张、知识萃取 2 张），且彼此孤立**——缺少一张把四者串成"会学习 → 会提问 → 会想 → 会沉淀"闭环的**个人学习方法总框架卡**，缺少各子域的**子框架卡与 agent-spec**，也从未澄清 **IPO（学习能力引擎）与 Y 模型（科学成事/问题解决引擎）的关系**。

**评级：A-（高价值，建议尽快入队 #146）**。本域是 #136-#144 之后个人修炼线的自然收口，深挖价值高。

---

## 一、域结构总览

```
个人修炼·学习方法（待建总框架）
├── IPO 学习闭环（学习能力引擎）        —— 信息输入 Input → 处理 Process → 输出 Output + 反馈 Feedback
│       └── 一句话：学习能力 = IPO 的速度和质量（口述 L48）
├── 科学提问（IPO 中 Input/Process 的关键放大器）
│       └── AI 时代提问能力 = 生产力入口（口述 L432-L436）
├── 思维模型（IPO 中 Process 的处理内核）
│       └── 项目随时换，思维模型永生（口述 L1072）
└── 知识萃取（IPO 中 Output 的高阶形态）
        └── 把碎片化案例/经验沉淀成可复用模型与资产（口述 L36）

关系主轴：
  IPO 回答"学习能力的底层机制是什么"；
  提问 决定 IPO 输入与处理的质量上限；
  思维模型 是 IPO 处理环节的可迁移内核；
  知识萃取 是 IPO 输出环节的固化与资产化；
  Y 模型（#142）回答"如何科学成事/解决问题"，与 IPO 是"成事引擎 × 学习引擎"的并列互补关系，而非包含。
```

**核心判断**：四个子域不是四个并列主题，而是**同一条"学习能力 → 问题解决"链路上的四个齿轮**。总框架卡必须显式画出这条链路，并澄清 IPO 与 Y 模型的边界，否则会与 #142 Y 模型域、#141 五步法域概念打架。

---

## 二、现有覆盖度评估（Grep 核实）

| 子域 | 现有卡（Grep 命中） | 数量 | 评价 |
|---|---|---|---|
| IPO | `yt-personal-ipo-learning`(concept)、`yt-model-ipo-learning-strategy`(concept)、`yt-model-ipo-complete-checklist`(concept)、`tool-科学学习IPO完整清单`(tool)、`tool-Truman-AI时代IPO模型重构`(tool) | 5（含 1 张 Truman 重构；核心 4 张与上游清单一致） | 概念卡/工具卡齐全，但**无统摄框架卡**，且 IPO 与提问/思维模型/萃取的关系未建 |
| 科学提问 | `yt-model-questioning-practice-canvas`(concept)、`yt-model-scientific-questioning-map`(concept)、`tool-提问刻意练习画布`(tool)、`tool-科学提问刻意练习`(tool)（另有 Truman 系列工具卡） | 4 核心 | OCR 画布/成长地图已工具化，但**与 IPO 闭环、与 Y 模型提问环节未挂钩** |
| 思维模型 | `yt-personal-thinking-models`(concept)（另 `yt-tool-mental-model-refinement`） | 1 核心 | **最薄**：3022 行口述只沉淀出 1 张概念卡，无框架、无与 IPO Process 的映射 |
| 知识萃取 | `yt-personal-knowledge-extraction`(concept)、`yt-tool-knowledge-extraction`(concept)（另 `dk-truman-knowledge-extraction-three-schools`） | 2 + 1 DK | 有概念有 DK，但**无"萃取作为 IPO 输出高阶形态"的定位** |

**核心缺口**：
1. **无个人学习方法总框架卡**：四子域孤岛化，没有"会学习→会提问→会想→会沉淀"的闭环导航。
2. **无各子域子框架卡**：IPO 全景策略（Goal/I/P/O/F + L1-L6 工具）、提问四段位画布、思维模型体系、萃取方法论都只停在 concept/tool 粒度。
3. **无 orchestrator / 子域 agent-spec**：用户无法从一个入口诊断"我的学习能力卡在哪一环"。
4. **无 IPO × Y 模型关系说明**：与 #142 边界不清，存在概念重叠风险。
5. **诊断报告缺位**：本报告即补此缺口。
6. **OCR 空文件**：`一堂-个人修炼-科学学习IPO模型_paddle_ocr.txt` 为 0 行，需走 `_vlm_reprocess/个人修炼/` 补 OCR 后方可引用。

---

## 三、未被吸收的暗知识 / 操作细节

| # | 暗知识/操作细节 | 精确来源 | 现有卡覆盖 | 建议动作 |
|---|---|---|---|---|
| 1 | **IPO 是"一堂第一课"**：所有课最入门最基础、解释教育公司最顶层机制、面对同行的底牌 | `IPO模型实操课口述.md:18-26` | 概念卡有提及但缺口述行号 | 写入总框架卡定位章节 |
| 2 | **学习能力 = IPO 的速度和质量**；输入（质量+数量）/处理/输出 + 长周期目标/模型/反馈机制 | `IPO模型实操课口述.md:42-48` | `yt-model-ipo-*` 有提及 | 总框架卡核心公式 |
| 3 | **IPO 三价值**：快速上手（IPU 强则学新东西快）/科学体系（完备框架、确定性优化）/无限进步（挑战天花板） | `IPO模型实操课口述.md:50-58` | 未系统整合 | 总框架卡 + IPO 子框架卡 |
| 4 | **IPO 全景策略 V2.0**：Goal（人生红点/长期渴望）→ Input（L1 案例/L2 资料/L2 高手/L3 实践）→ Process（L1 存储/L2 联系/L3 建模/L1 提炼/L2 专题/L3 复盘）→ Output（L4 分享/L5 辩证/L6 实践）→ Feedback（理性/感性） | `科学学习IPO-全景策略_paddle_ocr.txt:3-58` | `tool-科学学习IPO完整清单` 部分覆盖 | IPO 子框架卡主图 |
| 5 | **IPO 完整清单**：把每个 I/P/O 模块映射到具体课程/服务/入口（"我选/加入/会员日"） | `科学学习IPO完整清单_paddle_ocr.txt:3-51` | `tool-科学学习IPO完整清单` 覆盖 | 升级该 tool 并挂到 IPO 子框架 |
| 6 | **提问能力 = AI 时代生产力入口**：好问题是激励/厚礼，提问能力前所未有地关键 | `科学提问口述.txt:96,396,432-436` | `tool-ai-problem-question-check` 等散落 | 提问子框架卡定位 |
| 7 | **提问刻意练习四段位**：业务分析（★) → 辅导团队（★★) → 咨询教练（★★★★) → 萃取经验（★★★★★)，各段位对应"向谁提问/目标/场景/套路/工具箱"（STAR/GROW/关键假设/苏格拉底式） | `提问刻意练习画布_paddle_ocr.txt:1-14` | `tool-提问刻意练习画布` 覆盖 | 升级为子框架卡并把 L4"萃取经验"接到知识萃取域 |
| 8 | **科学提问成长地图**：Analysis / Teaching(Socrates) / Coaching 三阶 | `科学提问刻意练习_paddle_ocr.txt:1-9` | `tool-科学提问刻意练习` 覆盖 | 纳入提问子框架卡 |
| 9 | **思维模型永生**：项目随时换，思维模型伴随走很远、跨越时间周期、累加式拿结果 | `思维模型口述版.md:1072-1086` | `yt-personal-thinking-models` 有提及但缺口述行号 | 思维模型子框架卡核心命题 |
| 10 | **经验判断 vs 逻辑思维模型判断**：两种状态、不同场景各取所需 | `思维模型口述版.md:2756` | 未覆盖 | 思维模型子框架卡"When NOT to Use" |
| 11 | **知识萃取的本质**：把碎片化案例/经验做成可落地、知行合一、有指导意义的模型；市场普遍意识和能力太弱、大量经验被浪费 | `知识萃取探索营口述版.md:28-36,80` | `yt-tool-knowledge-extraction` + DK 部分覆盖 | 知识萃取子框架卡定位 |
| 12 | **萃取作为 IPO 输出的高阶形态**：IPO Output 的 L4-L6（分享/辩证/实践）走到极致就是萃取建模能力外放 | `知识萃取探索营口述版.md:96` + `全景策略 OCR:36-50` | 未建立映射 | 总框架卡"四环链路"章节 |
| 13 | **IPO × Y 模型关系**：IPO = 学习能力引擎（输入-处理-输出），Y 模型 = 科学成事/问题解决引擎（因果/道理）；两者并列互补，提问与思维模型同时服务两者 | 综合 IPO 口述 + Y 模型域（#142） | 未澄清 | 总框架卡"边界与关系"章节（防概念打架） |

---

## 四、矛盾 / 差异点

| # | 差异点 | 来源 A | 来源 B | 建议处理 |
|---|--------|--------|--------|---------|
| 1 | **IPO vs IPU 命名** | 口述稿多处转写为"IPU"（语音识别） | OCR/课程正式名称为"IPO"（Input-Process-Output） | 统一采用 IPO，口述引用处标注"原文转写为 IPU" |
| 2 | **IPO 与 Y 模型是否包含** | IPO 讲"学习机制"，可能被理解为包含一切 | Y 模型讲"科学成事道理/因果"，独立成域（#142) | 总框架卡显式声明"并列互补、不互相包含"，给出分工表 |
| 3 | **提问归属**：提问属 IPO 的 Input/Process，还是属 Y 模型的问题定义 | IPO 域把提问当学习能力放大器 | Y 模型/科学成事把提问当问题定义环节 | 提问子框架卡声明"横跨 IPO 与 Y 模型"，两侧 related 互链 |
| 4 | **思维模型定位**：是 IPO Process 内核，还是独立"个人修身"域 | 本诊断归入学习方法 Process 内核 | 现有卡 `yt-personal-thinking-models` 归 personal | 子框架卡说明"思维模型是 Process 的可迁移内核"，保留 personal 标签 |
| 5 | **知识萃取 vs 知识管理** | 萃取 = 把经验建模成资产 | 知识管理（`yt-personal-knowledge-management`）= 存储/整理 | 知识萃取子框架卡区分"管理（存）vs 萃取（炼）" |
| 6 | **IPO OCR 模型图空文件** | `科学学习IPO模型_paddle_ocr.txt` 0 行 | `_vlm_reprocess/个人修炼/一堂-个人修炼-科学学习IPO模型_vlm_desc.md` 可能有 VLM 描述 | 生产前先补 OCR/VLM，引用以非空源为准 |

---

## 五、可直接 Agent 化的环节

| # | Agent 环节 | 解决的问题 | 输入 | 输出 | 调用/转交 | 边界风险 |
|---|---|---|---|---|---|---|
| 1 | **学习能力卡点诊断** | 用户不知自己 IPO 哪一环弱 | 学习场景描述 + 近期输入/输出 | 定位 I/P/O/F 薄弱环节 + 优先动作 | 总框架卡、IPO 子框架卡 | 不替代学科专业判断 |
| 2 | **提问段位判断** | 用户提问停在低段位 | 提问场景 + 对象 | 四段位定位 + 对应套路/工具箱 | 提问子框架卡、`tool-提问刻意练习画布` | 不替代咨询/教练实战 |
| 3 | **思维模型匹配** | 遇到问题不知调用哪个模型 | 问题类型 + 场景 | 推荐 1-3 个思维模型 + 使用边界 | 思维模型子框架卡 | 不堆模型、不替决策 |
| 4 | **经验萃取引导** | 经验停在碎片、无法复用 | 案例/项目复盘 | 提炼模型草案 + 沉淀路径 | 知识萃取子框架卡 | 不伪造普适结论 |
| 5 | **IPO × Y 模型分流** | 用户混淆"学"与"做" | 用户目标（学会 vs 做成） | 分流到 IPO 闭环 或 Y 模型（#142) | Y 模型 orchestrator | 分流前先确认目标类型 |
| 6 | **子域调度** | 需深入单环 | 卡点环节 + 用户问题 | 调用对应子框架/工具 | #142 Y 模型、现有 Truman 工具 | 调度前先做卡点诊断 |

---

## 六、个人学习方法专属 Agent 设计：`agent-个人学习方法教练`

### 6.1 定位

- **名称**：`agent-个人学习方法教练`
- **一句话**：个人学习方法域的总入口与四环调度器，帮用户诊断 IPO 卡点、判断提问段位、匹配思维模型、引导经验萃取，并在"学"与"做"之间分流到 Y 模型。
- **边界**：不替代学科/专业判断，不替用户做决策，不伪造普适模型，只提供结构化诊断与下一步建议。

### 6.2 TCPR 身份

- **默认身份**：C（Coach/教练）——先诊断 IPO 卡点。
- **切换规则**：
  - 用户问"某个环节怎么做" → T（Teacher）
  - 用户要一起梳理学习系统 → P（Partner）
  - 用户要复盘/萃取经验 → R（Researcher）
  - 用户想跳过输入直接要答案 → C→T，先用"输入质量决定上限"纠偏

### 6.3 触发场景

1. "我为什么学了很多但用不上？"（IPO 断在 Process/Output）
2. "我提问总是得不到好答案。"（提问段位）
3. "这个问题该用哪个思维模型？"（模型匹配）
4. "我做了这么多项目，怎么沉淀成自己的能力？"（萃取）
5. "我是该先学还是该先做？"（IPO × Y 模型分流）

### 6.4 工作流

```
Step 0: 边界确认 → 声明只提供结构化诊断
Step 1: 目标分流 → 学会（IPO 闭环）/做成（转交 #142 Y 模型）
Step 2: IPO 卡点诊断 → 定位 I/P/O/F 薄弱环节
Step 3: 提问段位判断 → 四段位 + 对应套路/工具箱
Step 4: 思维模型匹配 → 按问题类型推荐 1-3 个模型 + 边界
Step 5: 输出/萃取引导 → 把经验推到 L4-L6，必要时进入萃取
Step 6: 输出个人修炼闭环清单 + 风险警示
```

### 6.5 调用卡 / 转交 Agent

- `framework-个人学习方法总框架.md`（待建）
- `framework-个人学习方法-IPO学习闭环.md`（待建）
- `framework-个人学习方法-科学提问.md`（待建）
- `framework-个人学习方法-思维模型.md`（待建）
- `framework-个人学习方法-知识萃取.md`（待建）
- `tool-科学学习IPO完整清单`、`tool-提问刻意练习画布`、`tool-科学提问刻意练习`
- 跨域转交：`agent-spec-yitang-Y-model-cross-domain-coach`（#142）

### 6.6 边界风险

1. 用户想要"标准答案模型库" → 强调模型是工具不是答案，匹配需看场景。
2. 把 IPO 与 Y 模型混用 → Step 1 先做"学/做"分流。
3. 跳过输入直接要输出 → 用"输入质量决定上限"纠偏。
4. 萃取时伪造普适结论 → 要求标注样本边界与失效条件。
5. 替代 #142 Y 模型 orchestrator → 只做分流，不深入成事环节。

---

## 七、建议新建 / 升级清单

### P0：总框架卡 + orchestrator Agent Spec

| # | id | 类型 | 核心内容 | source_refs |
|---|---|---|---|---|
| 1 | `framework-个人学习方法总框架` | framework | 四环闭环（IPO/提问/思维模型/萃取）、每环输入输出、IPO 三价值、IPO×Y 模型关系与边界、个人修炼闭环自检 | `IPO口述:18-58`；`全景策略OCR:3-58` |
| 2 | `agent-个人学习方法教练` | agent-spec | orchestrator：卡点诊断、提问段位、模型匹配、萃取引导、IPO×Y 分流；含完整 System Prompt、TCPR、工作流 | 综合 |

### P1：四张子框架卡

| # | id | 类型 | 核心内容 | source_refs |
|---|---|---|---|---|
| 3 | `framework-个人学习方法-IPO学习闭环` | framework | Goal/I/P/O/F 全景、L1-L6 工具、三价值、与课程服务清单映射 | `IPO口述:42-58`；`全景策略OCR`；`完整清单OCR` |
| 4 | `framework-个人学习方法-科学提问` | framework | AI 时代提问=生产力、四段位画布、成长地图、横跨 IPO/Y 模型声明 | `科学提问口述:96,396,432-436,1070`；`提问画布OCR`；`科学提问OCR` |
| 5 | `framework-个人学习方法-思维模型` | framework | 模型永生、经验判断 vs 逻辑模型、作为 IPO Process 内核、When NOT to Use | `思维模型口述:1072-1086,2756` |
| 6 | `framework-个人学习方法-知识萃取` | framework | 碎片经验→可落地模型、管理（存）vs 萃取（炼）、作为 IPO Output 高阶形态、样本边界 | `知识萃取口述:28-36,80,96` |

### P2：工具卡 + 现有卡升级

| # | id | 类型 | 核心内容/升级点 |
|---|---|---|---|
| 7 | `tool-个人学习方法-修炼闭环自检清单` | tool | 四环"会学习→会提问→会想→会沉淀"自检项与卡点定位 |
| 8 | `tool-IPO学习-输入处理输出工具箱导航` | tool | 整合 IPO 全景策略 L1-L6 工具到 I/P/O 三段索引 |
| 9 | `yt-personal-ipo-learning` 升级 | concept | related 关联总框架卡；正文加"闭环位置（总引擎）"说明 |
| 10 | `yt-model-questioning-practice-canvas` 升级 | concept | related 关联 `framework-个人学习方法-科学提问`；补 IPO/Y 模型双挂 |
| 11 | `yt-personal-thinking-models` 升级 | concept | related 关联思维模型子框架；补口述行号 L1072-1086 |
| 12 | `yt-personal-knowledge-extraction` 升级 | concept | related 关联知识萃取子框架；补"IPO Output 高阶形态"定位 |

> 注：IPO 另 3 张（`yt-model-ipo-learning-strategy`、`yt-model-ipo-complete-checklist`、`tool-Truman-AI时代IPO模型重构`)、提问 Truman 系列、`yt-tool-mental-model-refinement`、`yt-tool-knowledge-extraction`、`dk-truman-knowledge-extraction-three-schools` 仅做 related 回填，不改正文，避免重复生产。

---

## 八、最终判断与入队建议

**评级：A-**

- 素材完整度 A：4 份 3000+ 行口述稿 + 5 份 OCR 模型图齐全（仅 1 份 IPO 模型 OCR 为空，可补）。
- 理论自洽性 A：IPO 闭环 + 提问四段位 + 思维模型内核 + 萃取输出，四环天然成链。
- wiki 现状 C：四子域孤岛、无总框架、无子框架、无 agent-spec、IPO×Y 模型关系未澄清。
- Agent 必要性 A：个人修炼线收口，需要一个"学习能力卡点诊断 + 学做分流"的入口 Agent。
- 深挖价值：**高（最契合"有口述稿但 wiki 缺失"）**。

**建议入队编号**：`#146`
**任务名称**：`task_20260709_wangyuyan-personal-learning-method-agent`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：7 张新建卡（1 总框架 + 4 子框架 + 2 工具）+ 1 张 Agent Spec + 4 张现有卡轻升级 = 触达 12 张卡 + 1 个 Agent
**依赖**：依赖 `#142 Y 模型`（IPO×Y 分流边界）、`#143`、`#144`（域注册与入口协议、共享能力底座）；建议这三个任务到位后再启动，避免返工

---

## 跨域联动边界

> 本诊断与 [[framework-yitang-y-model-cross-domain-fusion]]、[[agent-spec-yitang-Y-model-cross-domain-coach]]（#142)、[[agent-一堂五步法教练]]（#141）联动：IPO/提问/思维模型同时服务"学习"与"成事"，分流边界由本域总框架卡显式声明，避免与 #141/#142 概念打架。

*王语嫣 2026-07-09*
