---
id: task_20260709_wangyuyan-opportunity-foresight-agent
title: 一堂机会预判 / 终局光谱域 P0-P2 补产：总框架卡 + 终局光谱图解读/案例预判方法卡 + 教练 Agent Spec
status: reviewed
priority: P1
assignee: kimi-code
reviewer: 欧阳锋
reviewed_by: 欧阳锋
expected_cards: 4
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260709_yitang-opportunity-foresight-deep-dive.md
- 00_inbox/一堂-机会预判课-Truman-口述.txt L38-L66,L40-L46,L50-L62,L62-L66,L68-L90
- 00_inbox/一堂-机会预判课-truman-笔记.txt L1-L40,L21-L37
- 00_inbox/一堂-机会预判-终局光谱图-truman-图01_paddle_ocr.txt L1-L9
- 00_inbox/一堂-机会预判-终局光谱图-truman-图02_paddle_ocr.txt L10-L20
- 00_inbox/一堂-机会预判-终局光谱图-truman-图03_paddle_ocr.txt L15-L24
- 00_inbox/一堂-机会预判-终局光谱图示例-truman-图01_paddle_ocr.txt L1-L14
- 00_inbox/一堂-机会预判-终局光谱图解读-truman-02_paddle_ocr.txt L1-L5
- 00_inbox/一堂-机会预判-案例预判01_paddle_ocr.txt L3-L14
- 00_inbox/一堂-机会预判-案例预判02_paddle_ocr.txt L1-L11
- 00_inbox/一堂-机会预判-案例预判03_paddle_ocr.txt L1-L10
- 00_inbox/一堂-机会预判-咖啡案例01_paddle_ocr.txt L1-L20
- 00_inbox/一堂-机会预判-咖啡店案例-五步法预判_paddle_ocr.txt L1-L5
- 00_inbox/一堂-机会预判-陪诊案例01_paddle_ocr.txt L1-L19
- 00_inbox/一堂-机会预判-三维排列组合01_paddle_ocr.txt L1-L14
- 00_inbox/一堂-机会预判-AI趋势12大变化模型_paddle_ocr.txt L1-L42
related:
- '[[diag_20260709_yitang-opportunity-foresight-deep-dive]]'
- '[[yt-foresight-business-spectrum]]'
- '[[yt-foresight-15-char-mantra]]'
- '[[yt-foresight-ab-steady-state]]'
- '[[yt-foresight-addition-subtraction]]'
- '[[yt-foresight-deliverables-four-levels]]'
- '[[yt-foresight-model-taxonomy]]'
- '[[yt-foresight-probability-engineering]]'
- '[[yt-foresight-ten-fatal-flaws]]'
- '[[yt-tool-foresight-canvas]]'
- '[[tool-一堂-spectrum-positioning]]'
- '[[tool-一堂-business-prediction-15-char]]'
- '[[yt-ai-trend-12-signals]]'
- '[[yt-ai-startup-20-risky-hypotheses]]'
- '[[yt-three-dimension-opportunity-matrix]]'
- '[[case-coffee-shop-foresight]]'
- '[[case-escort-service-tiered-growth]]'
- '[[case-ai-time-management-tiered-growth]]'
- '[[dk-foresight-tier-skip-illusion]]'
- '[[dk-foresight-source-material-blindness]]'
- '[[framework-一堂五步法]]'
- '[[framework-demand-opportunity-spectrum]]'
created_at: 2026-07-09
updated_at: '2026-07-10T16:26:57.322727+00:00'
review_date: '2026-07-10'
grade: A-
---

# 一堂机会预判 / 终局光谱域 P0-P2 补产：总框架卡 + 解读/方法卡 + 教练 Agent Spec

> 来源：`diag_20260709_yitang-opportunity-foresight-deep-dive.md`
> 王语嫣判断：机会预判是一堂课程体系**第一阶段「预判篇」第一节课**、CEO 最重要的工作之一，素材是一堂最丰富的一批（3466 行口述 + 笔记 + 实测 18 张 OCR）。但 wiki 只有单点珠子（8 张 `yt-foresight-*` + 3 张 AI/三维 + 几张 case），缺承重结构：**总框架卡（项链）、终局光谱图解读卡（读法）、案例预判方法卡（SOP）、教练 Agent**。本任务把口述主线「预判段位差→15字诀→终局光谱七段→保A争B→加法/减法→五步法预判」串成可导航链路，并明确「机会预判 = 五步法（#141）的前置滤镜」。
>
> **校准（不照搬用户口径）**：用户称「17 张 OCR 未充分萃取」。实测 18 张，其中 3 张已充分萃取（AI趋势12/20高风险/三维）、6 张部分萃取。**本任务不全量补图，只补承重层（解读/方法/总框架/Agent）**，避免重复造卡。
>
> **领取安排**：#141/#143/#144 均已 reviewed，依赖已解锁；由 **Kimi 实例·老顽童** 领取执行。

---

## 一、目标产出

> 新卡 4 张 + Agent Spec 1 个（计入 `expected_cards`/`expected_agent_specs`）；另有 6-8 张现有卡 related/内容升级（不计入新卡数）。

### P0：总框架卡 + 教练 Agent Spec

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 一堂机会预判总框架卡 | framework | `30_wiki/frameworks/framework-一堂-机会预判.md` | 串段位阶梯（L1-L6）/15字诀/终局光谱七段/保A争B/加法/减法/五步法预判；明确「预判 = 五步法前置滤镜」、与 `framework-demand-opportunity-spectrum` 区分；含必要预判工作流、三类硬伤映射、When NOT to Use |
| 2 | 一堂机会预判教练 Agent Spec | agent-spec | `.agent/prompts/agent-一堂-机会预判教练.md` | 预判篇总入口：段位定位→终局区间（保A争B）→加法拆选项→减法排硬伤→五步法逐格预判→转交 #141；含完整 System Prompt、TCPR（默认 C）、工作流、调用卡、边界 |

### P1：解读卡 / 方法卡 / 模型卡升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 3 | 终局光谱图解读卡 | concept | `30_wiki/concepts/concept-一堂-终局光谱图解读.md` | 5 条解读（就事论事/质变点/保A争B区间/谨慎务实/预判终局5-10年）+ 七段风险/收益量化表；与 `yt-foresight-business-spectrum` 互链（框架 vs 读法） |
| 4 | 案例预判方法卡 | tool | `30_wiki/tools/tool-一堂-机会预判-案例预判.md` | 任意 idea 跑七段光谱定保A争B 的 SOP：定位当前段→列七段形态→排「保1争7」幻觉→定保A争B 区间→三类硬伤校验；附陪诊保2争4/咖啡保3争5/AI时间保4争6 三例 |
| 5 | 五步法预判结构卡 | tool | `30_wiki/tools/tool-一堂-机会预判-五步法预判.md` | 快/好/办公店 × 需求-解决方案-商业模式-增长-壁垒矩阵；终局定了之后逐格预判，出口转交 #141 五步法教练 |
| 6 | 三维排列组合卡升级 | concept | `30_wiki/concepts/yt-three-dimension-opportunity-matrix.md` | 补「新行业×新模式×新能力」操作法 + 11 个机会例（老人陪护/虚拟女友/辅助编程…）的排列组合用法；回链总框架 |
| 7 | AI 趋势 12 变化卡升级 | concept | `30_wiki/concepts/yt-ai-trend-12-signals.md` | 补「12 变化按需求/解决方案/商业模式/增长/壁垒分组」映射，接入总框架「AI 机会扫描」环节 |

### P2：OCR 萃取校验 + 现有卡 related 升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 8 | OCR 萃取校验清单 | audit-note | `60_feedback/audit/ocr-foresight-18files-extraction-check.md` | 逐张核对 18 张 OCR → 卡映射（已充分/部分/未萃取），确认无遗漏承重层；**不产新卡** |
| 9 | 8 张 `yt-foresight-*` related 升级 | concept | `30_wiki/concepts/yt-foresight-*.md` | related 统一回链 `framework-一堂-机会预判`；正文各加一句「在总框架中的位置」 |
| 10 | 3 张 case 卡升级 | case | `30_wiki/cases/case-coffee-shop-foresight.md`、`case-escort-service-tiered-growth.md`、`case-ai-time-management-tiered-growth.md` | 回链案例预判方法卡；陪诊卡补「阶段/商业模式/团队规模/营收预估」四维量化（`陪诊案例01:1-19`） |
| 11 | `yt-foresight-business-spectrum` 升级 | concept | `30_wiki/concepts/yt-foresight-business-spectrum.md` | 回链解读卡（框架↔读法），指向总框架 |

---

## 二、验收标准

- [x] `framework-一堂-机会预判.md` 通过 `kdo pre-submit`；引用至少 12 处口述稿/OCR 行号；含段位阶梯、15字诀、七段光谱、保A争B、加法/减法、五步法预判、必要预判工作流、三类硬伤映射；含 When NOT to Use / Failure Modes / Action Triggers；显式区分 `framework-demand-opportunity-spectrum`，声明「预判 = 五步法前置滤镜」。
- [x] `agent-一堂-机会预判教练.md` 通过 `kdo pre-submit`；System Prompt 完整；默认 C 身份；含 TCPR 切换规则；明确「不替代商业/投资决策」「预判≠验证（须接 #140/#138）」「不替用户定人生目标」「转交 #141」边界。
- [ ] 解读卡（#3）、案例预判方法卡（#4）、五步法预判结构卡（#5）均通过终审；method/tool 卡各有「何时用、需要什么、操作步骤、常见坑」四 section；source_refs 精确到 OCR 行号。
- [x] 三维（#6）、AI趋势12（#7）升级后不重复造卡，新增内容均有 OCR 行号，回链总框架。
- [x] OCR 萃取校验清单（#8）逐张覆盖 18 张，结论与诊断一致（3 充分/6 部分/其余补承重层）。
- [x] 现有卡升级（#9-#11）related 全部回链总框架，不产生孤岛或重复内容。
- [x] 所有口述数字/比例（如「1%→30%→80%」「1000 个项目」）降级为课程经验值表述。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `framework-一堂-机会预判.md`（#1） + `agent-一堂-机会预判教练.md`（#2） | 先定总框架与入口 Agent，确立「预判→五步法」转交协议 |
| 第二批 | 终局光谱图解读卡（#3） + 案例预判方法卡（#4） + 五步法预判结构卡（#5） | 填读法与方法层，case/光谱卡有链可回 |
| 第三批 | 三维（#6）/AI趋势12（#7）升级 | 既有模型卡接入总框架 |
| 第四批 | OCR 萃取校验（#8） + 8 张 yt-foresight + 3 张 case + business-spectrum related 升级（#9-#11） | 收口防孤岛，确认 18 张无遗漏 |

---

## 四、最终判断

**评级：A-（高价值，预判篇承重结构必须补齐；克制萃取，只补承重层）**

- 来源可靠：1 份 3466 行口述 + 1 份笔记 + 实测 18 张 OCR，一堂体系最丰富。
- 与 #141/#143/#144 形成网络：机会预判是五步法（#141）的「第 0 步/前置滤镜」，经 #143 入口协议注册、用 #144 共享底座萃取图；本任务不做单点深挖，而是把 8 张 `yt-foresight-*` 串成链路并补读法/方法。
- Agent 投产优先级中高：CEO 最高频决策之一，天然需要「先定终局再转交」的入口 Agent。

**建议入队编号**：`#147`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 2-3 天 + 欧阳锋终审 1 天
**依赖**：`#141`（五步法总框架/orchestrator，预判出口转交）、`#143`（跨域双三角诊断 Agent，域注册与入口协议）、`#144`（能力中台 Phase 1，18 张图 VLM/OCR 共享底座）；三者均已 reviewed，可解锁启动，预计无返工

**建议卡数**：4 张新卡（1 总框架 framework + 1 终局光谱图解读 concept + 1 案例预判方法 tool + 1 五步法预判结构 tool）+ 1 个 Agent Spec + 6-8 张现有卡升级 + 1 份 OCR 萃取校验清单。

---

*王语嫣 2026-07-09*

---

## 五、老顽童产出记录（2026-07-09）

**自评：A（不替欧阳锋定级）**。4 新卡 + 1 agent-spec + 2 升级 + 12 回链 + 1 audit，全量 pre-submit PASS（0 errors）。

### 产出表

| 类别 | 文件 | 状态 |
|---|---|---|
| 新卡 P0 | `30_wiki/frameworks/framework-一堂-机会预判.md` | pending_review，≥12 行号，含 When NOT/Failure/Action，显式区分 demand-opportunity-spectrum，声明「预判=五步法前置滤镜」 |
| 新卡 P0 | `.agent/prompts/agent-一堂-机会预判教练.md` | pending_review，TCPR 默认 C，工作流：边界→段位→区间→加法→减法→五步法→转交 #141；三条边界（不替代决策/预判≠验证/不替定人生目标） |
| 新卡 P1 | `30_wiki/concepts/concept-一堂-终局光谱图解读.md` | pending_review，5 条解读逐字 + 七段风险/收益量化表；与 business-spectrum「框架 vs 读法」互链 |
| 新卡 P1 | `30_wiki/tools/tool-一堂-机会预判-案例预判.md` | pending_review，五步 SOP + 陪诊保2争4/咖啡保3争5/AI时间保4争6 三例 |
| 新卡 P1 | `30_wiki/tools/tool-一堂-机会预判-五步法预判.md` | pending_review，选项池→店型剧本（快/好/办公店）×五步矩阵，出口 #141 |
| 升级 #6 | `yt-three-dimension-opportunity-matrix.md` | 清 2 死链 + 补操作法 + 11 组合例 + 填末尾 stub + 回链总框架 |
| 升级 #7 | `yt-ai-trend-12-signals.md` | 补 related 数组 + 12 变化按五步法五步映射小节 + 回链总框架 |
| 回链 #9 | 8 张 `yt-foresight-*` | related 全部回链总框架；5 张 Synthesis 补「在总框架中的位置」句（顺带消 OUTLINK warning） |
| 回链 #10 | 3 张 case | related 回链总框架 + 案例预判方法卡（咖啡另回链五步法预判卡） |
| 回链 #11 | `yt-foresight-business-spectrum` | related 补 framework-一堂-机会预判 + concept-终局光谱图解读 + framework-一堂五步法（补缺口） |
| audit #8 | `60_feedback/audit/ocr-foresight-18files-extraction-check.md` | 逐张 18 OCR，结论对齐 3 充分/6 部分/9 承重未萃取（已处理），不产卡 |

### 门禁结果

- 核心新卡（5 张）：YAML 0 / WIKILINK 0 / DOMAIN 0 / DK 0 / OUTLINK 0 → PASS
- 回链+升级老卡（14 张）：修复 model-taxonomy/ai-trend-12 缺 status/updated_at（动 frontmatter 触发的全量校验暴露），5 张 Synthesis 补 wikilink 消 OUTLINK warning → PASS
- 全量合并（19 文件）：0 errors，2 warnings（ab-steady/probability 无跨域链接，域范围本身如此，不硬塞跨域卡）→ PASS

### 五个拍板项落地

1. **预判=五步法前置滤镜（第 0 步）**：总框架第七节显式声明，agent-spec 出口转交 #141，tool-五步法预判出口接 framework-一堂五步法。
2. **框架 vs 读法分卡**：business-spectrum（框架+数据）↔ concept-终局光谱图解读（读法），总框架导航表 + 解读卡第三节双向互链。
3. **case 结果 vs 方法分卡**：3 case 保「保2争4/保3争5/保4争6」结果，tool-案例预判保 SOP；case 回链方法卡，方法卡引用 case 作演示。
4. **需求域光谱显式区分**：总框架第四节 + 解读卡第三节均注明 `framework-demand-opportunity-spectrum` 属需求域（配评估三角形），与本机会预判域不重复。
5. **数字降级**：1%→30%→80% / 1000 项目 / 100 万 / 千万净利 / 七段营收数 全部标「课程经验值」；示例01 第 2 段「月入 10-100 万」与 business-spectrum「1-10 万」口径冲突，解读卡标注取校准值。

### 顺带修复

- `yt-foresight-addition-subtraction`（draft）：清 2 个 `[[pending_unknown]]` 死链，替换为总框架 + 解读卡回链（status 保持 draft，未越界升 enriched）。
- `yt-three-dimension-opportunity-matrix`：清 2 个 `[[pending_unknown]]` 死链 + 填实末尾「目的/操作步骤/不要用的场景」stub。
- `yt-foresight-model-taxonomy` / `yt-ai-trend-12-signals`：补 status: enriched + updated_at（动 related 时门禁全量校验暴露的缺失）。

### 遗留与诚实声明

- **陪诊四维量化（任务单 #10 后半）未重复补表**：经核查，case-escort-service-tiered-growth L64-L72「七级演进详解」表已覆盖 阶段/商业模式/组织规模/典型营收 四维，与 OCR 陪诊案例01 口径一致；为避冗余未再造表，已在 audit-note 第三节说明。
- **18 张 OCR 口径**：逐张核到 inbox 文件 16 张；另 2 张（解读01 / 终局光谱图·图04）按诊断口径计入、未单独核到文件名、判非承重未萃取，audit-note 以 * 标注。
- **老卡 frontmatter 历史遗留未改**：src_unknown（reviewed_by/source_refs 错配如 theme-finance-legal、酒店 AI 标签）等洪七公时期字段，不在本任务范围，未动。
- **2 个 OUTLINK warning 保留**：ab-steady/probability 的链接全在 yitang 域内，属卡片本身域范围，未为消 warning 硬塞跨域卡。
