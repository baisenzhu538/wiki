---
id: task_20260708_wangyuyan-five-step-method-orchestrator-supplement
title: 一堂五步法域 P0-P2 补产：总框架卡 + 子框架卡 + orchestrator Agent Spec
status: in_progress
priority: P0
assignee: hermes
reviewer: 欧阳锋
expected_cards: 10
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260708_yitang-five-step-method-deep-dive-v2.md
- 00_inbox/一堂五步法/一堂-一堂五步法-增长-口述.txt L39-L58,L331-L390,L372-L376,L582-L589,L866-L980,L1274,L1921-L1926
- 00_inbox/一堂五步法/一堂-一堂五步法-壁垒-口述.txt L425-L427,L1222-L1234
- 00_inbox/一堂五步法/一堂-一堂五步法-单元模型-口述.txt L6-L10
- 00_inbox/一堂五步法/一堂-一堂五步法-单元模型-AI落地行动-口述.txt L527-L528,L574-L589
- 00_inbox/一堂五步法/一堂-一堂五步法-单元模型-十大单元模型清单_paddle_ocr.txt
- 00_inbox/一堂五步法/一堂-一堂五步法-增长-增长周期模型_paddle_ocr.txt
- 00_inbox/一堂五步法/一堂-一堂五步法-壁垒-假的壁垒_paddle_ocr.txt
- 00_inbox/一堂五步法/一堂-toB五步法-必知必会十八式-图片_paddle_ocr.txt
- 00_inbox/一堂五步法/一堂-一堂五步法-单元模型-段位升级三部曲_paddle_ocr.txt
related:
- '[[diag_20260708_yitang-five-step-method-deep-dive-v2]]'
- '[[yt-five-step-method]]'
- '[[yt-entrepreneur-five-step-method]]'
- '[[yt-model-five-step-canvas]]'
- '[[framework-一堂五步法-泛产品设计]]'
- '[[yt-five-step-method-complete]]'
- '[[yt-five-step-cross-step-1]]'
- '[[yt-five-step-cross-step-2]]'
- '[[yt-five-step-cross-step-3]]'
- '[[tool-一堂-five-step-validation]]'
- '[[case-five-step-fake-vs-real-barriers]]'
created_at: 2026-07-08
updated_at: '2026-07-08T17:25:52.662266+00:00'
---

# 一堂五步法域 P0-P2 补产：总框架卡 + 子框架卡 + orchestrator Agent Spec

> 来源：`diag_20260708_yitang-five-step-method-deep-dive-v2.md`
> 王语嫣判断：一堂五步法是当前所有子域任务（#136 销售、#137 泛产品、#138 产品内核、#139 时间管理、#140 需求分析）的方法论中枢。素材完整、理论自洽，但 wiki 层面缺少统摄五步的总框架卡、增长周期框架卡、壁垒框架卡，以及最关键的“五步法 orchestrator Agent Spec”。本任务聚焦把单步卡片串成可导航的链路。
> 
> **领取安排**：等 #143 跨域双三角诊断 Agent 过审后，由 **Hermes 实例** 领取执行。

---

## 一、目标产出

### P0：总框架卡 + orchestrator Agent Spec

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 一堂五步法总框架卡 | framework | `30_wiki/frameworks/framework-一堂五步法.md` | 统摄五步、价值假设/增长假设分界、每步输出物、两次跃迁、换档检查清单、商业分析版 vs 泛产品设计版两种形态区分 |
| 2 | 一堂五步法教练 Agent Spec | agent-spec | `.agent/prompts/agent-一堂五步法教练.md` | orchestrator 角色：阶段诊断、换档判断、子域 Agent 调度；含完整 System Prompt、TCPR、工作流、调用卡 |

### P1：子框架卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 3 | 单元模型框架 | framework | `30_wiki/frameworks/framework-一堂五步法-单元模型.md` | 十大单元模型清单、斧子/尺子/梯子三角色、与机会预判/关键假设/增长阶段映射 |
| 4 | 增长周期框架 | framework | `30_wiki/frameworks/framework-一堂五步法-增长周期.md` | 获客驱动/系统驱动/对抗驱动三阶段、典型动作、卡点、最糟结果 |
| 5 | 壁垒框架 | framework | `30_wiki/frameworks/framework-一堂五步法-壁垒.md` | 六大护城河、真假壁垒判断、一堂自我诊断 |

### P1-P2：工具卡与现有卡升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 6 | 五步法换档检查清单 | tool | `30_wiki/tools/tool-一堂五步法-换档检查清单.md` | 每步进入下一步的验收条件与常见卡点 |
| 7 | ToB 五步法十八式检查清单 | tool | `30_wiki/tools/tool-一堂五步法-ToB-十八式-checklist.md` | ToB 十八式导航与优先级判断 |
| 8 | 段位升级三部曲自检 | tool | `30_wiki/tools/tool-一堂五步法-段位升级三部曲.md` | 从会用→用好→出神入化的自检清单 |
| 9 | `yt-five-step-method` 概念升级 | concept | `30_wiki/concepts/yt-five-step-method.md` | 替换为总框架卡的精简版，引用口述行号 |
| 10 | `framework-一堂五步法-泛产品设计` 升级 | framework | `30_wiki/frameworks/framework-一堂五步法-泛产品设计.md` | 在 related 中关联总框架卡；正文增加“两种形态”说明 |
| 11 | `yt-five-step-method-complete` 升级/合并 | framework | `30_wiki/frameworks/yt-five-step-method-complete.md` | 与总框架卡对齐，避免重复 |
| 12 | `case-five-step-fake-vs-real-barriers` 升级 | case | `30_wiki/cases/case-five-step-fake-vs-real-barriers.md` | 关联 `framework-一堂五步法-壁垒` |

---

## 二、验收标准

- [ ] `framework-一堂五步法.md` 通过 `kdo pre-submit`；引用至少 10 处口述稿/OCR 行号；包含 When NOT to Use、Failure Modes、Action Triggers；明确区分两种形态。
- [ ] `agent-一堂五步法教练.md` 通过 `kdo pre-submit`；System Prompt 完整；默认 C 身份；含 TCPR 切换规则；明确声明“不替代商业决策”和“子域调度”边界。
- [ ] 3 张子框架卡（单元模型、增长周期、壁垒）通过终审；source_refs 精确。
- [ ] 3 张工具卡每张都有“何时用、需要什么、操作步骤、常见坑”四 section。
- [ ] 现有卡升级后不产生重复内容；`yt-five-step-method-complete` 与总框架卡关系明确。
- [ ] 所有口述数字/比例降级为课程经验值。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序建议

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `framework-一堂五步法.md` + `agent-一堂五步法教练.md` | 先定总框架和 orchestrator |
| 第二批 | 单元模型/增长周期/壁垒 3 张子框架卡 | 填子域框架 |
| 第三批 | 换档检查清单、ToB 十八式、段位升级三部曲 | 操作工具 |
| 第四批 | 现有卡升级/合并 | 避免重复 |

---

## 四、最终判断

**评级：A-（高价值，方法论中枢必须补齐）**

- 来源可靠：9 份口述稿 + 大量 OCR 模型图。
- 与子域任务形成网络：本任务不做单步深挖，而是把 #136-#140 串成链路。
- Agent 投产优先级高：用户持续要求“深挖→生产 agent”，五步法作为 orchestrator 是天然入口。

**建议入队编号**：`#141`
**优先级**：P0
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 3-4 天 + 欧阳锋终审 1 天
**依赖**：依赖 `#144 P-23 能力中台 Phase 1`（共享能力底座）与 `#143 跨域双三角诊断 Agent`（域注册与入口协议）；建议这两个任务完成后再启动，避免返工

---

*王语嫣 2026-07-08*
