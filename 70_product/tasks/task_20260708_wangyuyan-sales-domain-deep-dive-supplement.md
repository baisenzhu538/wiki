---
id: task_20260708_wangyuyan-sales-domain-deep-dive-supplement
title: 销售域口述稿二次深挖补产：操作层工具卡 + Agent 规格
status: in_progress
priority: P1
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
expected_cards: 6
expected_agent_specs: 6
expected_upgrades: 4
source_refs:
  - 60_feedback/diagnosis/diag_20260708_yitang-sales-domain-oral-deep-dive-v2.md
  - 00_inbox/销售专题/李蕊-科学销售方法论-口述.txt L800-L814,L228-L230,L266,L372
  - 00_inbox/销售专题/李蕊-销售体系之一-客户分层和卖点提炼-口述.txt L280-L282,L392-L394,L432-L440,L470-L500,L508-L520
  - 00_inbox/销售专题/李蕊-销售体系之二-销售过程拆解-口述.txt L320-L354,L420-L458,L560-L588,L824-L832,L1386-L1394,L1466
  - 00_inbox/销售专题/李蕊-销售体系之三-销售过程管理-口述.txt L1426-L1462,L1488-L1490
  - 00_inbox/销售专题/李蕊-销售体系之四-激励体系搭建-口述.txt L398-L402,L1126-L1128,L1648-L1654
  - 00_inbox/销售专题/李蕊-销售系统之五-销售工具箱-口述.txt L34,L720,L1204,L1314,L1434-L1446,L1488-L1524,L2150-L2154,L2276-L2282
related:
  - "[[diag_20260708_yitang-sales-domain-oral-deep-dive-v2]]"
  - "[[diag_20260702_yitang-scientific-sales-methodology]]"
  - "[[task_20260702_laowantong-yitang-scientific-sales-methodology-production]]"
  - "[[framework-yitang-scientific-sales-five-step]]"
  - "[[tool-yitang-sales-performance-management]]"
  - "[[framework-yitang-sales-incentive-6d]]"
  - "[[tool-yitang-sales-toolkit-radar]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[case-yitang-yitu-lead-industrialization]]"
created_at: 2026-07-08
updated_at: 2026-07-08
---

# 销售域口述稿二次深挖补产：操作层工具卡 + Agent 规格

> 任务来源：`diag_20260708_yitang-sales-domain-oral-deep-dive-v2.md`
> 王语嫣判断：已有 12 张销售专题卡通过终审，但口述稿中仍存在大量**操作层暗知识**未被吸收；若直接用于销售 Agent，会在「话术生成、回款建议、激励设计、过程管理」等高频场景产生幻觉。本任务聚焦补齐 P0/P1 缺口，把销售域的 Agent 落地密度提上去。

---

## 一、目标产出

### P0 批次：直接影响 Agent 输出质量

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|--------|------|----------|----------|
| 1 | 前三秒话术优化卡 | tool | `30_wiki/tools/tool-yitang-three-second-opening-scripts.md` | 电话/AI 外呼「前三秒」决策点、降低挂断率话术模板、渠道差异、A/B 测试方法 |
| 2 | 阿里铁军聆听三七法则执行卡 | tool | `30_wiki/tools/tool-yitang-listening-37-rule.md` | 70/30 目标、50% 硬上限、六大技巧、不同阶段差异化比例、录音自检表 |
| 3 | 回款 / 催款 / 履约阶段 playbook | tool | `30_wiki/tools/tool-yitang-payment-collection-playbook.md` | 四类决策、付款顺序重构、催款话术、合规边界、关单标准 |
| 4 | 前三秒话术优化 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-three-second-opening-scripts.md` | 输入通话数据 → 输出开场白 3-5 版 + 风险标签 + A/B 测试建议 |
| 5 | 回款 / 履约风险预警 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-payment-collection-risk.md` | 输入合同/沟通记录 → 输出风险评分 + 下一步动作 + 合规提示 |

### P1 批次：完善系统能力

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|--------|------|----------|----------|
| 6 | 销售目标权衡框架 | framework | `30_wiki/frameworks/framework-yitang-sales-target-tradeoffs.md` | GMV/收入/毛利/利润/用户数/立标杆/高客单的冲突与阶段决策规则 |
| 7 | 日会 / 周会 SOP 与主持模板 | tool | `30_wiki/tools/tool-yitang-daily-weekly-meeting-hosting.md` | 日会 15 分钟议程、周会 60 分钟议程、Gap 分析模板、行动项追踪 |
| 8 | 销售工具武器库成熟度盘点 | tool | `30_wiki/tools/tool-yitang-sales-toolkit-maturity-60-75-85.md` | 60/75/85 分级清单、缺失诊断、建设路线图、与六维雷达映射 |
| 9 | 日会 / 周会智能主持 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-daily-weekly-meeting-host.md` | 输入日报/周报/Pipeline → 输出议程 + Gap + 待办 |
| 10 | 销售工具箱缺口盘点 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-sales-toolkit-gap.md` | 输入现有工具清单/业务参数 → 输出成熟度评分 + 缺失优先级 + 路线图 |
| 11 | 激励方案设计辅助 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-incentive-design.md` | 输入业务阶段/目标/客单价/现金流 → 输出激励组合草案 + 风险警示 |
| 12 | 线索漏斗健康度诊断 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-lead-funnel-health.md` | 输入漏斗数据 → 输出瓶颈级 + 责任归属 + 反向推算 |

### 升级现有卡

| # | 目标卡 | 升级点 | 来源行号 |
|---|--------|--------|----------|
| 13 | `framework-yitang-scientific-sales-five-step.md` | 增加「前三秒」作为电话触点独立决策点；增加电话/线上/面谈渠道差异说明 | `李蕊-科学销售方法论-口述.txt:800-814,228-230,266,372` |
| 14 | `tool-yitang-sales-performance-management.md` | 增加 6 类文件 + 5 种会议清单、日报语言标准、日会/周会差异化议程 | `李蕊-销售体系之三-销售过程管理-口述.txt:1426-1462,1488-1490`<br>`李蕊-销售系统之五-销售工具箱-口述.txt:2150-2154`<br>`_processed/业绩推进管理-一堂业绩管理拆解画布-课程匹配工具_vlm.md:21-24` |
| 15 | `framework-yitang-sales-incentive-6d.md` | 增加提成比例区间（低客单 8-10%、高客单 5%）、零底薪高提成适用边界、情感仪式案例与风险 | `李蕊-销售体系之四-激励体系搭建-口述.txt:398-402,1126-1128,1648-1654` |
| 16 | `case-yitang-yitu-lead-industrialization.md` | 增加五级漏斗量化数据、各级责任主体、转化率红线 | `李蕊-销售体系之一-客户分层和卖点提炼-口述.txt:432-440`<br>`_processed/销售体系之一-益涂工业化筛选线索模型_vlm.md:8-12` |

---

## 二、验收标准

- [ ] 6 张新卡 `kdo pre-submit` PASS，无新增 ERROR；每张卡 Critique ≥3 外部反对者 + ≥2 内部局限；related ≥5 且至少 2 条跨域。
- [ ] 4 张升级卡 `kdo pre-submit` PASS，新增 section 与 source_refs 对齐诊断报告。
- [ ] 6 个 agent-spec 文件包含：触发场景、输入、输出、工作流、调用卡、边界风险、System Prompt 模板；每个 spec 至少关联 1 张 tool/framework 卡。
- [ ] 所有新产出反向更新 `opc-ai-sales-agent-architecture.md` 的 related。
- [ ] 数字/比例全部降级为课程经验值，不当作普适真理。
- [ ] 涉及回款/合同/提成法律判断处必须标注「需财务/法务复核」。
- [ ] 欧阳锋终审通过。

---

## 三、生产顺序建议

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | 前三秒话术优化卡 + 聆听三七法则卡 | 直接解决话术类 Agent 幻觉 |
| 第二批 | 回款/履约 playbook + 两个对应 Agent | 直接解决现金流与合规风险 |
| 第三批 | 4 张现有卡升级 | 边产新卡边补链 |
| 第四批 | 销售目标权衡框架 + 日会/周会 SOP + 工具箱成熟度卡 | 完善系统层 |
| 第五批 | 剩余 4 个 Agent 规格 | 在卡片终审后再固化 agent-spec |

---

## 四、最终判断

**评级：A（高价值，直接支撑销售域 Agent 军团落地）**

- 来源可靠：全部引用原始口述稿行号，避免二次消化失真。
- 不重复建设：在已有 12 张卡基础上做操作层补产，而非推翻重来。
- Agent 落地密度高：6 个新 Agent 规格覆盖话术、回款、会议、工具箱、激励、漏斗六大高频场景。
- 风险提示：回款/合同/提成涉及合规，必须在 Agent 输出中内置「请财务/法务确认」提示。

**建议入队编号**：`#136`
**优先级**：P1（销售域 Agent 落地关键补产）
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 3-4 天 + 欧阳锋终审 1 天

---

*王语嫣 2026-07-08*
