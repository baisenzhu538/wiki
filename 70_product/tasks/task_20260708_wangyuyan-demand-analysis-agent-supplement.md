---
id: task_20260708_wangyuyan-demand-analysis-agent-supplement
title: 需求分析域 P0-P2 补产：冰山工具卡补全 + 天花板框架 + 专属 Agent Spec
status: reviewed
priority: P0
assignee: hermes
reviewer: 欧阳锋
expected_cards: 17
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260708_yitang-demand-analysis-deep-dive-v2.md
- 00_inbox/五步法之需求分析/一堂-需求分析-方法论-口述.txt L80-L122,L224-L276,L332-L460,L1074-L1126,L1262-L1272,L1308-L1318,L2176-L2206
- 00_inbox/五步法之需求分析/一堂-需求分析-剥离需求-口述.txt L110,L1228-L1232,L1336-L1342
- 00_inbox/五步法之需求分析/一堂-需求分析-需求评估-口述.txt L476-L536,L1104-L1186,L1720-L1796,L1962-L1976
- 00_inbox/五步法之需求分析/一堂-需求分析-空间测算-口述.txt L322-L344,L1308-L1320,L1308-L1870,L2252-L2278,L2348
- 00_inbox/五步法之需求分析/一堂-需求分析-JTBD理论-口述.txt L1034-L1044
- 00_inbox/五步法之需求分析/AI场景推演教练提示词.txt
- 00_inbox/五步法之需求分析/AI辅助探讨需求选项的提示词.md
- 00_inbox/五步法之需求分析/需求分析提示词.txt
related:
- '[[diag_20260708_yitang-demand-analysis-deep-dive-v2]]'
- '[[domain-demand-analysis-index]]'
- '[[framework-demand-iceberg]]'
- '[[framework-demand-usp-model]]'
- '[[framework-demand-validation-pipeline]]'
- '[[framework-demand-opportunity-spectrum]]'
- '[[tool-demand-assessment-triangle]]'
- '[[tool-demand-four-forces]]'
- '[[tool-demand-blindspot-checklist]]'
- '[[tool-demand-report-template]]'
- '[[prompt-demand-ai-coach]]'
- '[[yt-demand-insight-extraction]]'
created_at: 2026-07-08
updated_at: '2026-07-08T17:11:41.794352+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-08'
grade: A-
---

# 需求分析域 P0-P2 补产：冰山工具卡补全 + 天花板框架 + 专属 Agent Spec

> 来源：`diag_20260708_yitang-demand-analysis-deep-dive-v2.md`
> 王语嫣判断：需求分析域知识密度高、官方已验证、Agent 适配度极高。当前 wiki 骨架完整，但 6 张 L1-L6 工具卡大量 `src_unknown`、官方 `AI场景推演教练提示词.txt` 未迁移为 Agent Spec、缺少评估三角形打分器/天花板测算教练/RAT 生成器等关键工具。本任务聚焦把“已验证知识”封装成“可调用 Agent”。

---

## 一、目标产出

### P0：Agent Spec + 冰山工具卡补全

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 需求分析冰山教练 Agent Spec | agent-spec | `.agent/prompts/agent-spec-demand-iceberg-coach.md` | 迁移 `AI场景推演教练提示词.txt` 为 TCPR 格式；含完整 System Prompt 模板、6 步工作流、调用卡、边界风险 |
| 2 | L1 用户层工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l1-user.md` | 补全 `src_unknown`、执行占位符、口述案例、精确行号 |
| 3 | L2 场景层工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l2-scenario.md` | 同上 |
| 4 | L3 核心任务工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l3-core-job.md` | 同上；强化 JTBD 公式 |
| 5 | L4 任务地图工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l4-job-map.md` | 同上 |
| 6 | L5 隐藏洞察工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l5-forces.md` | 同上；强化四种力量、三种任务、微观体感 |
| 7 | L6 机会假设工具卡升级 | tool | `30_wiki/tools/tool-demand-iceberg-l6-hypothesis.md` | 同上；强化 RAT |
| 8 | 拆推评算使用指南 | tool | `30_wiki/tools/tool-demand-chai-tui-ping-suan-guide.md` | 拆推评算是“工具箱而非工作流”，含跳步/滑步规则 |
| 9 | 需求评估三角形打分器 | tool | `30_wiki/tools/tool-demand-assessment-triangle.md` | 升级：普遍性×频次×刚性打分流程，含频次四层对齐 |

### P1：新增框架/工具

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 10 | 天花板四层线框架 | framework | `30_wiki/frameworks/framework-demand-ceiling-four-lines.md` | TAM/SAM/SOM/CR1/BEL，融资版 vs 经营版 |
| 11 | 天花板测算教练工具 | tool | `30_wiki/tools/tool-demand-ceiling-coach.md` | 10-15 分钟对话输出天花板报告 |
| 12 | RAT 生成器 | tool | `30_wiki/tools/tool-demand-rat-generator.md` | 从 L5 洞察自动生成最危险假设清单 |
| 13 | 微观体感访谈脚本生成器 | tool | `30_wiki/tools/tool-demand-micro-experience-script.md` | 基于 L4 崩溃点生成 5 感访谈问题 |
| 14 | 需求选项探讨工具 | tool | `30_wiki/tools/tool-demand-option-explorer.md` | 用户初步想法后的 USP 追问、控变量、找盲区 |
| 15 | 需求报告模板升级 | tool | `30_wiki/tools/tool-demand-report-template.md` | 区分融资版与经营版输出 |

### P2：案例库、知识库、Skill

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 16 | 冰山 few-shot 案例库 | case | `30_wiki/cases/case-demand-iceberg-few-shot.md` | 奶昔 / 银发育儿 / 挂脖空调 / 马术课 结构化 few-shot |
| 17 | 2B 需求字典 | knowledge | `30_wiki/knowledges/knowledge-demand-2b-dictionary.md` | 角色/决策链/采购周期/隐性需求 |
| 18 | 2C 需求字典 | knowledge | `30_wiki/knowledges/knowledge-demand-2c-dictionary.md` | 场景/频次/情感任务/替代方案 |
| 19 | 需求分析 Skill | skill | `30_wiki/skills/skill-demand-analysis.md` | 打包 Agent + 卡片 + 案例 + 字典 |

---

## 二、验收标准

- [ ] `agent-spec-demand-iceberg-coach.md` 通过 `kdo pre-submit`；System Prompt 完整；`tcp_role` 为 C；含 TCPR 切换规则；L4/L5 前禁止产品方案的纪律写入 prompt。
- [ ] 6 张 L1-L6 工具卡补全后 0 个 `src_unknown`；每个层级至少 1 个口述案例 + 精确行号。
- [ ] `tool-demand-assessment-triangle` 升级后包含频次四层对齐和打分流程。
- [ ] `framework-demand-ceiling-four-lines` 明确区分融资版/经营版，含 CR1/BEL 定义。
- [ ] `tool-demand-rat-generator` 能从 L5 洞察输出 3-5 个关键假设 + 验证方法 + 优先级。
- [ ] 所有口述数字/比例降级为课程经验值，标注置信度（✅/⚠️/🔮）。
- [ ] 不迁移 `优秀提示词合集.md` 为官方 Agent Spec；仅作为 few-shot/反例素材。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序建议

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | Agent Spec + 6 张 L1-L6 工具卡补全 | 先让 Agent 能跑通冰山推演 |
| 第二批 | `tool-demand-assessment-triangle` + `tool-demand-chai-tui-ping-suan-guide` | 补核心工具 |
| 第三批 | 天花板框架 + 天花板教练 + RAT 生成器 | 扩展评估能力 |
| 第四批 | 微观体感脚本 + 需求选项探讨 + 报告模板升级 | 完善操作层 |
| 第五批 | 案例库 + 2B/2C 字典 + Skill | 打包复用 |

---

## 四、最终判断

**评级：A（高价值、已验证、可快速封装）**

- 来源可靠：官方口述稿 + 官方提示词 + 图像 VLM 解析。
- 不重复建设：在已有 domain-index 和 framework 基础上补全工具卡和 Agent Spec。
- Agent 投产优先级高：用户明确“需求是极其重要的域，最终也是要生产 agent”。

**建议入队编号**：`#140`
**优先级**：P0
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 4-5 天 + 欧阳锋终审 1 天
**依赖**：依赖 `#144 P-23 能力中台 Phase 1`（共享能力底座）与 `#143 跨域双三角诊断 Agent`（域注册与入口协议）；建议这两个任务完成后再启动，避免返工

---

*王语嫣 2026-07-08*
