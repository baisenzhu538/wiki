---
id: task_20260709_wangyuyan-expression-pitch-agent
title: 个人修炼·表达力与讲香十指（增量）P0-P2：总框架卡 + 教练 Agent Spec + 火箭模型/执行武器库卡 + 现有卡升级
status: reviewed
priority: P1
assignee: hermes
reviewer: 欧阳锋
expected_cards: 5
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260709_yitang-expression-pitch-increment-deep-dive.md
- 00_inbox/一堂-个人修炼-讲香十指模型口述版.txt L36-L80,L46-L52,L56-L80
- 00_inbox/一堂-个人修炼-讲香基本功_paddle_ocr.txt
- 00_inbox/一堂-个人修炼-讲香十指模型-超级武器库_paddle_ocr.txt
- 00_inbox/一堂-个人修炼-讲香基本功-十指模型修炼地图_paddle_ocr.txt
- 00_inbox/一堂-个人修炼-表达力火箭模型_paddle_ocr.txt L1-L6
- 00_inbox/一堂-个人修炼-表达力火箭模型-执行武器库_paddle_ocr.txt
related:
- '[[diag_20260709_yitang-expression-pitch-increment-deep-dive]]'
- '[[yt-personal-scientific-expression]]'
- '[[yt-model-personal-pitch-toolkit]]'
- '[[yt-personal-verbatim-script]]'
- '[[tool-讲香基本功-十指模型]]'
- '[[tool-讲香十指模型-超级武器库]]'
- '[[yt-pitch-storytelling]]'
- '[[yt-pitch-quantification]]'
- '[[yt-pitch-metaphor]]'
- '[[ocr-一堂-个人修炼-表达力火箭模型]]'
- '[[ocr-一堂-个人修炼-表达力火箭模型-执行武器库]]'
created_at: 2026-07-09
updated_at: '2026-07-10T16:19:34.660001+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-10'
grade: A-
---

# 个人修炼·表达力与讲香十指（增量）P0-P2：总框架卡 + 教练 Agent Spec + 火箭模型/执行武器库卡 + 现有卡升级

> 来源：`diag_20260709_yitang-expression-pitch-increment-deep-dive.md`
> 王语嫣判断：表达力是个人修炼域的"输出层"——上游（产品内核、动力阻力、卖点）找准之后，靠它把卖点"讲得让人听得进去、完成兴趣-信任-转化"。5 月已就讲香本体早期挖过一轮，沉淀了 `yt-pitch-*` 10 张技巧卡，但经前置审计发现三处硬伤：① 讲香十指口述版（阿蕊 3504 行）只萃取了"术"、漏了"道"，且纲卡 `yt-model-personal-pitch-toolkit` 来源错位到 hackathon 摘要；② 表达力火箭模型有一张早期 tool 卡 `yt-personal-scientific-expression`，但火箭本体/执行武器库两份 OCR 未升级为正式卡；③ 表达力总框架卡 + coach Agent + 诊断报告三真空。本任务核心动作是"补 why、正纲源、升 OCR、串总纲、加 Agent"，不重写已有 `yt-pitch-*`。
>
> **领取安排**：#143/#144 均已 reviewed，依赖已解锁；由 **Hermes 实例·老顽童** 领取执行（agent 路由与 shared 工具调用按 #143/#144 协议接入）。

---

## 一、目标产出

### P0：表达力总框架卡 + 教练 Agent Spec + 讲香十指口述版补萃取

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 一堂个人表达力总框架卡 | framework | `30_wiki/frameworks/framework-一堂-个人表达力.md` | 统摄"火箭模型（纲）+ 十指讲香（术）+ 逐字稿（控制）+ 刻意练习/灵感闪念（训练）"；明确"找准卖点→讲好卖点"在方法论中的位置；与上游产品内核/销售的承接；含 When NOT to Use、Failure Modes、Action Triggers |
| 2 | 一堂个人表达力教练 Agent Spec | agent-spec | `.agent/prompts/agent-一堂-个人表达力教练.md` | coach 角色：诊断听众/目的/卖点 → 选十指组合 → 生成逐字稿 → 演练反馈；含完整 System Prompt、TCPR（默认 C）、工作流、调用卡、边界（不替代内容决策/不替用户上台） |
| 3 | 讲香·卖点直给到价值感（口述版 why 层补萃取） | concept | `30_wiki/concepts/concept-讲香-卖点直给到价值感.md` | 固化口述版 L62-L80：卖点找准却"直男式直给"→数据差；十指把"价值点"双向拉伸成"价值感"；承接 L56-L60 与科学销售/产品内核的关系 |

### P1：表达力火箭模型卡 + 执行武器库卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 4 | 表达力火箭模型（本体） | framework | `30_wiki/frameworks/framework-一堂-表达力火箭模型.md` | 由 `raw/ocr/ocr-一堂-个人修炼-表达力火箭模型`（draft）升级：四要素（有卖点/有专业度/打动人/逐字稿）、自下而上递进、与 `yt-personal-scientific-expression` 卡的分工说明、四要素权重随场景变化 |
| 5 | 表达力火箭模型·执行武器库 | tool | `30_wiki/tools/tool-一堂-表达力火箭模型-执行武器库.md` | 由执行武器库 OCR 升级为可执行 tool：何时用、需要什么、操作步骤、常见坑四 section；与火箭模型本体卡配套 |

### P2：现有 `yt-pitch-*` / 讲香卡 related 与 source 升级（不新增卡）

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 6 | `yt-model-personal-pitch-toolkit` 升级 | framework | `30_wiki/concepts/yt-model-personal-pitch-toolkit.md` | source_refs 补引口述版 L36-L80；related 关联总框架卡与 why 卡；注明原 hackathon 来源仅作佐证 |
| 7 | `yt-personal-scientific-expression` 升级 | tool | `30_wiki/concepts/yt-personal-scientific-expression.md` | 与火箭模型本体卡分工（本卡偏"科学表达/火箭应用"，本体卡偏模型结构）；related 关联总框架；清理 `src_unknown` |
| 8 | `tool-讲香十指模型-超级武器库` 升级 | tool | `30_wiki/tools/tool-讲香十指模型-超级武器库.md` | related 关联总框架；最低限度补全"目的/操作步骤/不要用的场景"三处"待补充" |
| 9 | `tool-讲香基本功-十指模型` 升级 | tool | `30_wiki/tools/tool-讲香基本功-十指模型.md` | related 关联总框架；清理 `pending_unknown` |
| 10 | `yt-pitch-*` 10 张 related 升级 | concept/tool | `30_wiki/concepts/yt-pitch-{aphorism,colloquialization,conflict,emotionalization,materialization,scenarization,sublimation}.md` + `30_wiki/tools/yt-pitch-{metaphor,quantification,storytelling}.md` | related 关联总框架卡，形成可导航链路；不重写正文 |

---

## 二、验收标准

- [ ] `framework-一堂-个人表达力.md` 通过 `kdo pre-submit`；引用口述版与 OCR 行号 ≥ 8 处；含 When NOT to Use / Failure Modes / Action Triggers；明确统摄火箭模型+十指讲香+逐字稿+刻意练习+灵感闪念，且不重写子卡内容。
- [ ] `agent-一堂-个人表达力教练.md` 通过 `kdo pre-submit`；System Prompt 完整；默认 C（Coach）身份；含 TCPR 切换规则；声明"不替代内容决策、不替用户上台"边界；明确调用总框架卡/十指/逐字稿/火箭模型卡。
- [ ] `concept-讲香-卖点直给到价值感.md` 准确引用口述版 L56-L80；包含高速吹风机案例与"卖点直给→数据差"动机链；通过终审。
- [ ] `framework-一堂-表达力火箭模型.md` 与 `tool-一堂-表达力火箭模型-执行武器库.md` 均由 OCR 升级、互为配套；source_refs 精确；与 `yt-personal-scientific-expression` 关系厘清，无内容重复。
- [ ] P2 升级卡不产生重复内容；`yt-model-personal-pitch-toolkit` source 错位得到校正；`yt-pitch-*` 10 张仅改 related，正文不动。
- [ ] 所有口述数字/比例（如"两年""数据差"）降级为课程经验值表述。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `framework-一堂-个人表达力.md` + `agent-一堂-个人表达力教练.md` | 先定总纲与 coach，作为后续所有卡的入口与导航 |
| 第二批 | `concept-讲香-卖点直给到价值感.md` | 补口述版 why 层，校正纲卡来源 |
| 第三批 | `framework-一堂-表达力火箭模型.md` + `tool-一堂-表达力火箭模型-执行武器库.md` | OCR 升级为正式卡，与 scientific-expression 分工 |
| 第四批 | P2 现有卡 related/source 升级（#6-#10） | 串链路、不返工正文 |

---

## 四、最终判断

**评级：B+/A-（中-高价值，增量补全 + 前置审计校正）**

- 来源可靠：1 份 3504 行口述版（阿蕊，why/how/案例齐全）+ 5 份模型图 OCR（火箭模型、执行武器库、讲香基本功、超级武器库、修炼地图）。
- 不重复造轮子：本任务"补 why、正纲源、升 OCR、串总纲、加 Agent"，明确不重写已有 `yt-pitch-*` 10 张。
- 闭环价值：打通"找准卖点（#136 销售 / 产品内核）→ 讲好卖点（本域）"的转化链路；表达力 coach 是个人修炼域天然入口，承接用户"深挖→生产 agent"诉求。

**建议入队编号**：`#148`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：5 张 wiki 卡 + 1 张 agent-spec + 约 12 张现有卡 related/source 升级
**预计工时**：老顽童 2-3 天 + 欧阳锋终审 0.5-1 天
**依赖**：依赖 `#136 销售`（卖点/产品内核输入）、`#143 跨域双三角诊断 Agent`（域注册与入口协议）、`#144 P-23 能力中台 Phase 1`（共享能力底座）；建议三者定稿后启动，避免 agent 路由与 shared 工具返工

---

*王语嫣 2026-07-09*
