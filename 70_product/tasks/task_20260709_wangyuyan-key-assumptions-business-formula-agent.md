---
id: task_20260709_wangyuyan-key-assumptions-business-formula-agent
title: 关键假设 + 业务公式拆解域 P0-P2 补产：主线总框架卡 + ABCD/三板斧/业务公式贯通卡 + orchestrator Agent Spec
status: reviewed
priority: P0
assignee: kimi-code
reviewer: 欧阳锋
reviewed_by: 欧阳锋
expected_cards: 12
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260709_yitang-key-assumptions-business-formula-deep-dive.md
- 00_inbox/一堂-关键假设课-truman-口述.txt L22-L80,L364-L402,L584,L818,L962-L982,L1064-L1074,L1560,L1644,L1810,L1982-L1998,L2460-L2482
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-口述.txt L10,L182-L194,L360,L510,L682-L694,L860,L1356-L1374,L1476-L1504,L1772,L1972,L2324,L2384,L2418,L2474-L2524
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-笔记.txt L15-L86
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式-逐字稿01.txt
- 00_inbox/一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt
- 00_inbox/一堂-关键假设-关键假设三板斧_paddle_ocr.txt
- 00_inbox/一堂-关键假设-商业画布259（9）_paddle_ocr.txt
- 00_inbox/一堂-关键假设-烤炉案例_paddle_ocr.txt
- 00_inbox/一堂-关键假设-奶茶案例_paddle_ocr.txt
- 00_inbox/一堂-关键假设-五步法259（5）_paddle_ocr.txt
- 00_inbox/一堂-关键假设-五步法259（2）_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-ABC模型图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-6层逻辑关系图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-冰山模型图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-十大业务公式范式_paddle_ocr.txt
related:
- '[[diag_20260709_yitang-key-assumptions-business-formula-deep-dive]]'
- '[[concept-一堂-key-assumptions]]'
- '[[concept-一堂-hypothesis-driven-business-methodology]]'
- '[[concept-一堂-business-prediction]]'
- '[[framework-一堂五步法]]'
- '[[yt-business-formula-abc-model]]'
- '[[yt-business-formula-parameter-iceberg]]'
- '[[yt-business-formula-six-level-logic]]'
- '[[yt-business-formula-ten-paradigms]]'
- '[[yt-business-formula-l6-essence-formulas]]'
- '[[yt-business-formula-business-pattern-selector]]'
- '[[yt-business-formula-qualitative-metrics-library]]'
- '[[tool-一堂-hypothesis-validation-three-axe]]'
- '[[tool-key-assumptions-check]]'
- '[[tool-first-principles-assumption-classify]]'
- '[[dk-mckinsey-hypothesis-driven-pitfalls]]'
- '[[dk-yitang-business-formula-plus-times-trap]]'
- '[[case-一堂-陈贤敏汉堡-hypothesis-validation]]'
- '[[case-一堂-无人餐厅-hypothesis-failure]]'
created_at: 2026-07-09
updated_at: '2026-07-10T15:18:15.753080+00:00'
review_date: '2026-07-10'
grade: A-
---

# 关键假设 + 业务公式拆解域 P0-P2 补产：主线总框架卡 + ABCD/三板斧/业务公式贯通卡 + orchestrator Agent Spec

> 来源：`diag_20260709_yitang-key-assumptions-business-formula-deep-dive.md`
> 王语嫣判断：关键假设课是 Truman 亲定的「第一节必修课 / 商业必修课」，业务公式拆解被孔源亲定为「关键假设 ABCD 体系的核心骨架与灵魂」（`孔源-业务公式拆解-口述.txt:2474-2500`）。素材完整、理论自洽，但 wiki 层面「有料无链」——缺一张统摄「假设驱动 + 三板斧 + ABCD + 风险管理 + 业务公式贯通」的主线总框架卡，缺关键假设 ABCD 模型卡，缺关键假设↔业务公式的贯通总纲，更缺本域 orchestrator Agent Spec。本任务把散落的 15+ 张卡串成「识别假设 → 三板斧收敛 → ABCD 定位 → 业务公式 L1-L6 定量化 → 最便宜验证」的可导航链路，并作为 #141 五步法 orchestrator 的前置入口。
>
> **领取安排**：#141/#143/#144 均已 reviewed，依赖已解锁；由 **Kimi 实例·老顽童** 领取执行；Agent 注册与共享能力调用按 #143/#144 协议接入。
>
> **口径约束**：所有源自口述稿/OCR/笔记的数字、比例、人数、转化率等一律降级为「课程经验值 / 课程案例口径」，不作为外部事实断言。

---

## 一、目标产出

### P0：主线总框架卡 + orchestrator Agent Spec

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 关键假设主线总框架卡 | framework | `30_wiki/frameworks/framework-一堂-关键假设.md` | 统摄「用假设驱动业务」命题（`truman:364-402`）、三板斧骨架（`:1064-1074`）、ABCD 四场景定位、风险管理本质（`:2474`）、与业务公式 ABC 的贯通（`孔源:2474-2500`）、与五步法「第一节必修课」关系（`:1560,1644`）；含 When NOT to Use / Failure Modes / Action Triggers |
| 2 | 关键假设教练 Agent Spec | agent-spec | `.agent/prompts/agent-一堂-关键假设教练.md` | orchestrator 角色：假设识别 → 三板斧编排 → ABCD 定位 → 业务公式定量化 → 子域调度；含完整 System Prompt、TCPR、工作流、调用卡、边界风险 |

### P1：ABCD / 三板斧 / 业务公式拆解贯通卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 3 | 关键假设 ABCD 模型卡 | framework | `30_wiki/frameworks/framework-一堂-关键假设-ABCD模型.md` | YitangABCDStrategyModel：A 商业场景 / B 决策场景（宏观—微观）/ C 增长场景 / D 转化场景；成败问题 + 效率问题（`关键假设ABCD模型_OCR`）；**显式区分** lean/decision/project 三张同名 ABCD 卡 |
| 4 | 关键假设三板斧方法骨架卡 | framework | `30_wiki/frameworks/framework-一堂-关键假设-三板斧.md` | 加法（解构要素）→ 减法（找风险最高假设）→ 验证（最便宜策略）→ 迭代（贝叶斯定理）（`truman:1064-1074`、`关键假设三板斧_OCR`）；与现有 `tool-一堂-hypothesis-validation-three-axe`（操作清单）分工、双向 related，不重复内容 |
| 5 | 业务公式拆解总纲（贯通关键假设）卡 | framework | `30_wiki/frameworks/framework-一堂-业务公式拆解-总纲.md` | 落实孔源「业务公式 = 关键假设 ABCD 体系核心骨架/灵魂」（`孔源:2474-2500`）；ABC 模型 × 参数冰山 L1-L6 × 六层逻辑关系 × 十大范式（4 张孔源 OCR）；三要素「看得清/讲得明/做得准」+ 三大认知突破（`笔记:15-71`）；**统摄导航 7 张 `yt-business-formula-*` 子卡，打通「定性假设 → L1-L6 定量参数」**；脚注说明「孔源/孔阳」署名差异 |

### P2：工具卡 + 现有卡 related/source_refs 升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 6 | 关键假设 ABCD 场景分类器 | tool | `30_wiki/tools/tool-一堂-关键假设-ABCD场景分类器.md` | 把业务问题分到商业/决策/增长/转化四场景，并标注成败 vs 效率；含「何时用/需要什么/操作步骤/常见坑」 |
| 7 | 业务公式 L1-L6 参数分层自检 | tool | `30_wiki/tools/tool-一堂-业务公式-L1L6参数分层自检.md` | L1-L6 参数分层 + 「看得清/讲得明/做得准」自检 + +×/因果校验（接 `dk-yitang-business-formula-plus-times-trap`） |
| 8 | `concept-一堂-key-assumptions` 升级 | concept | `30_wiki/concepts/concept-一堂-key-assumptions.md` | `source_refs` 由 `pending_archive` 补为精确口述行号；related 关联总框架/三板斧/ABCD |
| 9 | `tool-一堂-hypothesis-validation-three-axe` 升级 | tool | `30_wiki/tools/tool-一堂-hypothesis-validation-three-axe.md` | `source_refs` 补精确行号；related 关联 `framework-一堂-关键假设-三板斧` 与总框架 |
| 10 | `concept-一堂-hypothesis-driven-business-methodology` 升级 | concept | `30_wiki/concepts/concept-一堂-hypothesis-driven-business-methodology.md` | related 关联总框架卡 |
| 11 | `concept-一堂-business-prediction` 升级 | concept | `30_wiki/concepts/concept-一堂-business-prediction.md` | related 关联 `framework-一堂-业务公式拆解-总纲` |
| 12 | 两张 dk + 两张 tool 批量回链 | dk/tool | `dk-yitang-business-formula-plus-times-trap.md`、`dk-mckinsey-hypothesis-driven-pitfalls.md`、`tool-key-assumptions-check.md`、`tool-first-principles-assumption-classify.md` | related 回链总框架/总纲；不改正文逻辑 |

> **批量回链（不计入 expected_cards 12，作为收尾动作）**：7 张 `yt-business-formula-*`（abc-model / parameter-iceberg / six-level-logic / ten-paradigms / l6-essence-formulas / business-pattern-selector / qualitative-metrics-library）related 统一回链 `framework-一堂-业务公式拆解-总纲`；2 张 case（陈贤敏汉堡/无人餐厅）related 回链三板斧/总框架。

---

## 二、验收标准

- [x] `framework-一堂-关键假设.md` 通过 `kdo pre-submit`；引用至少 8 处口述稿/OCR 行号（含 `truman:364-402,1064-1074,2474` 与 `孔源:2474-2500`）；含 When NOT to Use / Failure Modes / Action Triggers；明确「定性假设 → 业务公式定量」贯通与「五步法第一节必修课」定位。
- [x] `agent-一堂-关键假设教练.md` 通过 `kdo pre-submit`；System Prompt 完整；默认 C 身份；含 TCPR 切换规则；明确声明「不替代商业/财务/法务决策」与「子域调度（#138/#140/#141）」边界；按 #143 协议注册、按 #144 协议调用共享能力。
- [ ] 3 张 P1 卡（ABCD / 三板斧 / 业务公式总纲）通过终审（内容已完成：ABCD 显式区分他域同名卡、三板斧与现有 tool 分工不重复、总纲统摄 7 张子卡且 source_refs 精确到 OCR/口述行号；待欧阳锋终审）。
- [x] 2 张 P2 工具卡每张都有「何时用 / 需要什么 / 操作步骤 / 常见坑」四 section。
- [x] 现有卡升级不产生重复内容；`concept-一堂-key-assumptions` 与 `tool-一堂-hypothesis-validation-three-axe` 的 `source_refs` 不再为 `pending_archive`。
- [x] 所有数字/比例/人数均标注为「课程经验值 / 课程案例口径」。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序建议

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `framework-一堂-关键假设.md` + `agent-一堂-关键假设教练.md` | 先定主线总纲与 orchestrator 入口 |
| 第二批 | 关键假设 ABCD / 三板斧 / 业务公式总纲 3 张 framework | 填四根柱子的其余三根，建立贯通 |
| 第三批 | ABCD 场景分类器、L1-L6 参数分层自检 2 张 tool | 操作化落地 |
| 第四批 | 现有卡 related/source_refs 升级 + 7 张子卡/2 张 case 批量回链 | 收口成网、避免重复 |

---

## 四、最终判断

**评级：A-（高价值，方法论入口层，具备冲到 A 的潜力）**

- 来源可靠：主课口述（3234 行）+ 孔源口述/笔记/逐字稿 + 11 张 OCR 模型图，自带 L1-L6 / 三板斧 / ABCD / ABC / 十大范式结构化框架。
- 入口地位突出：Truman 亲定「第一节必修课」，孔源亲定业务公式为「关键假设 ABCD 体系灵魂」——两侧亲口互证，贯通是课程本意而非外加。
- 与 #138/#140/#141 形成清晰上下游：本域是 #141 的「第一节必修课前置入口」、#140 的「假设层上游」、#138 的「验证方法上游」，不重复造轮子。
- 工程量可控：以「建总纲 + 补贯通 + 串链路」为主，7 张业务公式子卡与多张 concept/tool 复用率高。

**建议入队编号**：`#145`
**优先级**：P0
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 2-3 天 + 欧阳锋终审 1 天
**依赖**：依赖 `#141 一堂五步法 orchestrator`（前置入口衔接）、`#143 跨域双三角诊断 Agent`（域注册与入口协议）、`#144 P-23 能力中台 Phase 1`（OCR/VLM/检索共享底座）；建议这三项就绪后启动，避免返工

---

*王语嫣 2026-07-09*



---

## 五、老顽童产出记录（2026-07-09，提交 pending_review）

### 新建（6 卡 + 1 agent-spec）
- `30_wiki/frameworks/framework-一堂-关键假设.md`（P0 总框架，引用 11 处口述/OCR 行号）
- `.agent/prompts/agent-一堂-关键假设教练.md`（P0 orchestrator，默认 C，TCPR 完整）
- `30_wiki/frameworks/framework-一堂-关键假设-ABCD模型.md`（P1，显式区分 lean/decision/project 三张同名卡；**v2 增补**：案例演示节，含一个业务问题走四场景 + 顺序闸门 + 同名卡边界演示）
- `30_wiki/frameworks/framework-一堂-关键假设-三板斧.md`（P1 骨架/道，与 tool 操作分工；**v2 增补**：案例演示节，含外层循环 / 内层循环 / 贝叶斯迭代数值走查三案例，全标假设演示口径）
- `30_wiki/frameworks/framework-一堂-业务公式拆解-总纲.md`（P1，统摄 7 张子卡导航 + 定性→定量贯通 + 孔源/孔阳署名脚注）
- `30_wiki/tools/tool-一堂-关键假设-ABCD场景分类器.md`（P2，四 section）
- `30_wiki/tools/tool-一堂-业务公式-L1L6参数分层自检.md`（P2，四 section）

### 升级（计入 expected_cards 12 的 #8-11）
- `concept-一堂-key-assumptions`：补全 frontmatter + source_refs 精确行号（`truman:364-402,584,818,1064-1074,2460-2482`）+ related 关联总框架/三板斧/ABCD
- `tool-一堂-hypothesis-validation-three-axe`：清 `[[pending_unknown]]` 死链 + source_refs 精确行号 + related 关联三板斧 framework/总框架
- `concept-一堂-hypothesis-driven-business-methodology`：related 关联总框架
- `concept-一堂-business-prediction`：related 关联业务公式总纲；顺带修 2 处预存死链（`concept-一堂-五步法`→`framework-一堂五步法`、`concept-一堂-精益创业`→文本，因 vault 无对应卡）

### 批量回链（#12 四张 + 额外 9 张 = 13 张）
- #12：`dk-yitang-business-formula-plus-times-trap`、`dk-mckinsey-hypothesis-driven-pitfalls`、`tool-key-assumptions-check`、`tool-first-principles-assumption-classify`（related 回链总框架/总纲）
- 7 张 `yt-business-formula-*`（abc-model/parameter-iceberg/six-level-logic/ten-paradigms/l6-essence-formulas/business-pattern-selector/qualitative-metrics-library）related 回链业务公式总纲
- 2 张 case（陈贤敏汉堡/无人餐厅）related 回链三板斧/总框架
- 顺带修复：`ten-paradigms` / `l6-essence-formulas` 的 related 嵌套坏格式（`- - -`）重写为扁平 list；`qualitative-metrics-library` 补全 frontmatter 必填字段（id/title/status/reviewed_by/updated_at/source_refs）

### pre-submit 结果
- 核心 11 文件：11/11 PASS
- 回链 13 文件：13/13 PASS（仅 1 个预存 warning：无人餐厅 Synthesis 0 wikilink，非本次引入，不阻塞）

### 口径与差异处理
- 数字/人数（直播间 11 万、六轮升级）一律标「课程经验值」
- 孔源/孔阳署名：新卡统一「孔源（笔记正文作孔阳）」，总纲卡脚注说明
- 三板斧 framework（道/骨架）与 tool（术/操作）双向 related、不重复内容
- 总纲卡统摄 7 张子卡为导航，不搬动现有卡
