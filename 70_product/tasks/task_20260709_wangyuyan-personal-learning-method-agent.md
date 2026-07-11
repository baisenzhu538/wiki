---
id: task_20260709_wangyuyan-personal-learning-method-agent
title: 个人修炼·学习方法域（IPO + 科学提问 + 思维模型 + 知识萃取）：总框架卡 + 4 子框架卡 + orchestrator Agent Spec
status: reviewed
priority: P1
assignee: hermes
reviewer: 欧阳锋
expected_cards: 7
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260709_yitang-personal-learning-method-deep-dive.md
- 00_inbox/ideas/一堂-个人修炼-IPO模型实操课口述.md L18-L58（3378 行）
- 00_inbox/AI-study/一堂-AI学习-科学提问口述.txt L96,L396,L432-L436,L1070（3010 行）
- 00_inbox/AI-study/cleaned/一堂-AI学习-科学提问口述_cleaned.md（2957 行）
- 00_inbox/一堂-个人修身-思维模型口述版.md L8,L18,L1072-L1086,L2756（3022 行）
- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md（3035 行，同名副本）
- 00_inbox/一堂-个人修炼-知识萃取探索营口述版.md L22-L36,L48,L80,L96（3094 行）
- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md（3107 行，同名副本）
- 00_inbox/一堂-个人修炼-科学学习IPO-全景策略_paddle_ocr.txt（60 行）
- 00_inbox/一堂-个人修炼-科学学习IPO完整清单_paddle_ocr.txt（51 行）
- 00_inbox/一堂-个人修炼-提问刻意练习画布_paddle_ocr.txt（13 行）
- 00_inbox/一堂-个人修炼-科学提问刻意练习_paddle_ocr.txt（8 行）
related:
- '[[diag_20260709_yitang-personal-learning-method-deep-dive]]'
- '[[yt-personal-ipo-learning]]'
- '[[yt-model-ipo-learning-strategy]]'
- '[[yt-model-ipo-complete-checklist]]'
- '[[tool-科学学习IPO完整清单]]'
- '[[tool-Truman-AI时代IPO模型重构]]'
- '[[yt-model-questioning-practice-canvas]]'
- '[[yt-model-scientific-questioning-map]]'
- '[[tool-提问刻意练习画布]]'
- '[[tool-科学提问刻意练习]]'
- '[[yt-personal-thinking-models]]'
- '[[yt-personal-knowledge-extraction]]'
- '[[yt-tool-knowledge-extraction]]'
- '[[yt-decision-y-model]]'
- '[[framework-yitang-y-model-cross-domain-fusion]]'
created_at: 2026-07-09
updated_at: '2026-07-10T15:44:02.753013+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-10'
grade: A-
---

# 个人修炼·学习方法域：总框架卡 + 4 子框架卡 + orchestrator Agent Spec

> 来源：`diag_20260709_yitang-personal-learning-method-deep-dive.md`
> 王语嫣判断：本域是个人修炼线最契合"有口述稿但 wiki 缺失"的一块。IPO（学习能力引擎）、科学提问（输入/处理放大器）、思维模型（处理内核）、知识萃取（输出高阶形态）四者各有一整份 3000+ 行口述稿 + OCR 模型图，素材完整、理论自洽；但 wiki 上四子域零散孤立、无总框架、无子框架、无 agent-spec，且 IPO 与 Y 模型（#142）的关系从未澄清。本任务不做单点深挖，而是把四环串成"会学习→会提问→会想→会沉淀"的可导航闭环，并显式声明 IPO × Y 模型的分工边界，避免与 #141 五步法、#142 Y 模型概念打架。
>
> **领取安排**：#142/#143/#144 均已 reviewed，依赖已解锁；由 **Hermes 实例·老顽童** 领取执行，欧阳锋终审。

---

## 一、目标产出

### P0：个人学习方法总框架卡 + orchestrator Agent Spec

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 个人学习方法总框架卡 | framework | `30_wiki/frameworks/framework-个人学习方法总框架.md` | 四环闭环（IPO/提问/思维模型/萃取）、每环输入输出、IPO 三价值（快速上手/科学体系/无限进步）、**IPO × Y 模型关系与边界表**、个人修炼闭环自检 |
| 2 | 个人学习方法教练 Agent Spec | agent-spec | `.agent/prompts/agent-个人学习方法教练.md` | orchestrator：IPO 卡点诊断、提问段位判断、思维模型匹配、萃取引导、IPO×Y 学做分流；含完整 System Prompt、TCPR、工作流、调用卡 |

### P1：四张子框架卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 3 | IPO 学习闭环子框架 | framework | `30_wiki/frameworks/framework-个人学习方法-IPO学习闭环.md` | Goal/Input/Process/Output/Feedback 全景、L1-L6 工具、三价值、与课程服务清单（完整清单 OCR）映射 |
| 4 | 科学提问子框架 | framework | `30_wiki/frameworks/framework-个人学习方法-科学提问.md` | AI 时代提问=生产力入口、四段位画布（业务/辅导/咨询/萃取）、成长地图、横跨 IPO 与 Y 模型声明 |
| 5 | 思维模型子框架 | framework | `30_wiki/frameworks/framework-个人学习方法-思维模型.md` | "项目随时换、思维模型永生"、经验判断 vs 逻辑模型、作为 IPO Process 可迁移内核、When NOT to Use |
| 6 | 知识萃取子框架 | framework | `30_wiki/frameworks/framework-个人学习方法-知识萃取.md` | 碎片经验→可落地模型、管理（存）vs 萃取（炼）、作为 IPO Output 高阶形态、样本边界与失效条件 |

### P2：工具卡 + 现有卡升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 7 | 修炼闭环自检清单 | tool | `30_wiki/tools/tool-个人学习方法-修炼闭环自检清单.md` | 四环"会学习→会提问→会想→会沉淀"自检项与卡点定位 |
| 8 | IPO 工具箱导航 | tool | `30_wiki/tools/tool-IPO学习-输入处理输出工具箱导航.md` | 整合 IPO 全景策略 L1-L6 工具到 I/P/O 三段索引 |
| 9 | `yt-personal-ipo-learning` 升级 | concept | `30_wiki/concepts/yt-personal-ipo-learning.md` | related 关联总框架卡；正文加"闭环位置（总引擎）"说明，引用口述 L42-58 |
| 10 | `yt-model-questioning-practice-canvas` 升级 | concept | `30_wiki/concepts/yt-model-questioning-practice-canvas.md` | related 关联科学提问子框架；补 IPO/Y 模型双挂说明 |
| 11 | `yt-personal-thinking-models` 升级 | concept | `30_wiki/concepts/yt-personal-thinking-models.md` | related 关联思维模型子框架；补口述行号 L1072-1086 |
| 12 | `yt-personal-knowledge-extraction` 升级 | concept | `30_wiki/concepts/yt-personal-knowledge-extraction.md` | related 关联知识萃取子框架；补"IPO Output 高阶形态"定位 |

> 其余现有卡（`yt-model-ipo-learning-strategy`、`yt-model-ipo-complete-checklist`、`tool-Truman-AI时代IPO模型重构`、`yt-tool-mental-model-refinement`、`yt-tool-knowledge-extraction`、`dk-truman-knowledge-extraction-three-schools`、提问 Truman 系列）仅做 related 回填，**不改正文**，避免重复生产。
> 生产前须先处理空 OCR：`00_inbox/一堂-个人修炼-科学学习IPO模型_paddle_ocr.txt` 为 0 行，引用以 `_vlm_reprocess/个人修炼/` 下 VLM 描述或非空源为准。

---

## 二、验收标准

- [ ] `framework-个人学习方法总框架.md` 通过 `kdo pre-submit`；引用至少 8 处口述稿/OCR 行号；包含 When NOT to Use、Failure Modes、Action Triggers；**显式画出四环闭环链路**；**含 IPO × Y 模型关系与边界表**（并列互补、不互相包含）。
- [ ] `agent-个人学习方法教练.md` 通过 `kdo pre-submit`；System Prompt 完整；默认 C 身份；含 TCPR 切换规则；明确声明"不替代学科/专业判断、不替决策、不伪造普适模型"；含 IPO×Y 学做分流规则。
- [ ] 4 张子框架卡（IPO 闭环/科学提问/思维模型/知识萃取）通过终审；source_refs 精确到行；每张子框架卡都声明自己在四环闭环中的位置。
- [ ] 2 张工具卡每张都有"何时用、需要什么、操作步骤、常见坑"四 section。
- [ ] 现有 4 张概念卡升级后不产生重复内容；related 正确回填到总框架卡/对应子框架卡。
- [ ] 所有口述数字/比例（如"效率差 10 倍、100 倍""一年读 30-50 本书"）降级为课程经验值，不作为普适结论。
- [ ] IPO/IPU 命名统一为 IPO，口述引用处标注"原文转写为 IPU"。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `framework-个人学习方法总框架.md` + `agent-个人学习方法教练.md` | 先定总框架、四环链路与 orchestrator；锁定 IPO×Y 边界 |
| 第二批 | IPO 闭环 / 科学提问 / 思维模型 / 知识萃取 4 张子框架卡 | 填四环子域框架 |
| 第三批 | 修炼闭环自检清单、IPO 工具箱导航 | 操作工具 |
| 第四批 | 4 张现有概念卡轻升级 + 其余卡 related 回填 | 避免重复，串成网络 |

---

## 四、最终判断

**评级：A-（高价值，个人修炼线收口必须补齐）**

- 来源可靠：4 份 3000+ 行口述稿 + 5 份 OCR 模型图（仅 IPO 模型 OCR 为空，可补）。
- 与子域任务形成网络：本任务不做单点深挖，而是把 IPO/提问/思维模型/萃取四环串成闭环，并与 #142 Y 模型做"学/做"分流。
- Agent 投产优先级高：用户持续要求"深挖→生产 agent"，个人学习方法教练是"学习能力卡点诊断 + 学做分流"的天然入口。

**建议入队编号**：`#146`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：7 张新建卡（1 总框架 + 4 子框架 + 2 工具）+ 1 张 Agent Spec + 4 张现有卡轻升级（触达 12 张卡 + 1 个 Agent）
**预计工时**：老顽童 3-4 天 + 欧阳锋终审 1 天
**依赖**：依赖 `#142 Y 模型`（IPO×Y 分流边界）、`#143`、`#144`（域注册与入口协议、共享能力底座）；建议这三个任务到位后再启动，避免返工

---

*王语嫣 2026-07-09*
