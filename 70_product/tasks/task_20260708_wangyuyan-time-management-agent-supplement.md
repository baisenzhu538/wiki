---
id: task_20260708_wangyuyan-time-management-agent-supplement
title: 时间管理域 P1 补产：四张模型图 + 操作工具 + 案例 + 专属 Agent Spec
status: in_progress
priority: P1
assignee: hermes
reviewer: 欧阳锋
expected_cards: 18
expected_agent_specs: 1
source_refs:
- 60_feedback/diagnosis/diag_20260708_yitang-time-management-deep-dive-v2.md
- 00_inbox/时间管理/truman-时间管理课程-口述.txt L134-L138,L160,L358,L398-L416,L428,L452-L472,L498-L502,L518-L522,L642-L720,L744-L752,L842,L912-L917,L962-L964,L1004-L1020,L1026-L1034,L1052-L1078,L1462-L1496,L1548-L1554,L1578-L1612,L1626-L1646,L1654-L1724,L1728-L1754,L1788-L1806,L1928-L1940,L1944-L2052,L2162-L2194,L2212-L2240,L2260-L2272,L2334-L2340
- 00_inbox/时间管理/_processed/时间管理_整合笔记.md
- 00_inbox/时间管理/_processed/时间管理-双环矩阵图_vlm.md
- 00_inbox/时间管理/_processed/时间管理-深度工作冰山图_vlm.md
- 00_inbox/时间管理/_processed/时间管理-时间管理矩阵图_vlm.md
- 00_inbox/时间管理/_processed/时间管理-双峰哲学模型_vlm.md
related:
- '[[diag_20260708_yitang-time-management-deep-dive-v2]]'
- '[[yt-personal-time-management]]'
- '[[framework-yitang-five-step-to-time-management]]'
- '[[tool-personal-time-audit-loop]]'
- '[[dk-time-management-common-mistakes]]'
- '[[case-truman-time-management-commute-experiment]]'
- '[[case-yitang-copywriting-time-decomposition]]'
created_at: 2026-07-08
updated_at: '2026-07-08T14:32:46.113177+00:00'
---

# 时间管理域 P1 补产：四张模型图 + 操作工具 + 案例 + 专属 Agent Spec

> 来源：`diag_20260708_yitang-time-management-deep-dive-v2.md`
> 王语嫣判断：时间管理域已有高质量桥接框架卡 `framework-yitang-five-step-to-time-management` 和时间审计工具卡，但缺少四张课程模型图 framework 卡、若干高频操作工具卡、更多口述案例卡，以及用户明确要求的「时间管理专属 Agent Spec」。本任务聚焦补齐这些缺口，让时间管理 Agent 可直接落地。

---

## 一、目标产出

### P0：专属 Agent Spec

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 个人时间管理教练 Agent Spec | agent-spec | `.agent/prompts/agent-personal-time-management-coach.md` | 默认 C 身份、TCPR 切换规则、触发场景、输入输出、6 步工作流、调用卡清单、边界风险、完整 System Prompt 模板 |

### P1：模型图 Framework 卡 + 概念升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 2 | 双环矩阵框架 | framework | `30_wiki/frameworks/framework-time-management-dual-loop-matrix.md` | 独立/协作 × 重点/效率 × 内环/外环工具选择地图 |
| 3 | 深度工作冰山框架 | framework | `30_wiki/frameworks/framework-deep-work-iceberg.md` | L1-L5 工作深度定义、识别、保护策略 |
| 4 | 时间管理矩阵框架 | framework | `30_wiki/frameworks/framework-time-management-matrix.md` | 重要/紧急四象限在一堂课语境中的解释：平衡 A/B、多做 A |
| 5 | 双峰哲学框架 | framework | `30_wiki/frameworks/framework-bimodal-time-philosophy.md` | 协作时间 vs 独立时间切分；暗时间利用 |
| 6 | 个人时间管理概念升级 | concept | `30_wiki/concepts/yt-personal-time-management.md` | 替换所有 `src_unknown`；与框架卡对齐；删除过时 L1-L3 三层，改用 L1-L6 进阶 + 三门模型 |

### P1：操作工具卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 7 | 双峰工作块 | tool | `30_wiki/tools/tool-bimodal-time-blocking.md` | 识别协作块/深度块 → 公开 → 执行纪律 |
| 8 | 任务深度拆解 | tool | `30_wiki/tools/tool-task-depth-decomposition.md` | 拆任务 → 标 L1-L5 → 按“大对大、小对小”排程 |
| 9 | 暗时间利用 | tool | `30_wiki/tools/tool-dark-time-harvesting.md` | 识别 CPU 不饱和场景 → 叠加低切换任务 |
| 10 | 公开排期 | tool | `30_wiki/tools/tool-public-scheduling.md` | 个人时间上日历、团队大事上日历、约日历协作 |
| 11 | 专注环境 SOP | tool | `30_wiki/tools/tool-focus-environment-sop.md` | 环境变量清单 → 测试 → 固化在家/出差版 |
| 12 | 每周假设实验 | tool | `30_wiki/tools/tool-weekly-hypothesis-experiment.md` | 每周 1-2 个假设 → 2 周实验 → 复盘固化 |
| 13 | 团队任务池 | tool | `30_wiki/tools/tool-team-task-pool.md` | 共享需求池 → 按优先级拉取 → 与个人清单对称 |
| 14 | 会议场域匹配 | tool | `30_wiki/tools/tool-meeting-room-match.md` | 头脑风暴/攻坚会/汇报会的场域选择 |

### P2：口述案例卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 15 | 200 期校庆启动会深度拆分 | case | `30_wiki/cases/case-yitang-200th-launch-depth-split.md` | 10h 工作时间，路上 40min 写灵感，睡前故事线 |
| 16 | 会议室场域匹配 | case | `30_wiki/cases/case-yitang-meeting-room-match.md` | 不同会议类型与场域的效率差异 |
| 17 | 洗澡/如厕/睡前想出关键假设 | case | `30_wiki/cases/case-truman-shower-toilet-ideation.md` | 高价值思考不只发生在办公室 |
| 18 | 表白墙 5 分钟提振状态 | case | `30_wiki/cases/case-truman-praise-wall-precondition.md` | 讲课前看公司表白墙进入状态 |
| 19 | 垂帘听政 | case | `30_wiki/cases/case-yitang-curtain-listening.md` | 线下磨课时远程接入，效率提升 |

---

## 二、验收标准

- [ ] `agent-personal-time-management-coach.md` 包含完整 System Prompt 模板，`tcp_role` 为 C，切换规则清晰。
- [ ] 4 张 framework 卡 `kdo pre-submit` PASS，source_refs 精确到口述稿行号或 VLM 文件。
- [ ] `yt-personal-time-management` 升级后 0 个 `src_unknown`，并与 `framework-yitang-five-step-to-time-management` 保持一致。
- [ ] 8 张 tool 卡每张都有“何时用、需要什么、操作步骤、常见坑、案例”五个 section。
- [ ] 5 张 case 卡通过欧阳锋终审。
- [ ] 所有 Truman 课程经验值数字（如“50min≈5h”“效率差一倍”）降级标注。
- [ ] Agent Spec 中显式声明边界：不负责人生目标、家庭关系、团队管理、精力医学。

---

## 三、生产顺序建议

| 批次 | 产出物 | 说明 |
|---|---|---|
| 第一批 | `agent-personal-time-management-coach.md` + 4 张 framework 卡 | 先定 Agent 骨架和模型图 |
| 第二批 | 8 张 tool 卡 | 填充操作层 |
| 第三批 | `yt-personal-time-management` 升级 | 在框架卡定稿后统一口径 |
| 第四批 | 5 张 case 卡 | 用口述细节支撑工具卡 |

---

## 四、最终判断

**评级：A-（高价值，可直接落地专属 Agent）**

- 已有 `framework-yitang-five-step-to-time-management` 高质量桥接，不需要从零造概念。
- 用户明确要“时间管理专门的 agent”，本任务把 Agent Spec 作为 P0 产出。
- 19 张卡片工作量适中，老顽童可独立完成。

**建议入队编号**：`#139`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 3-4 天 + 欧阳锋终审 1 天
**依赖**：无

---

*王语嫣 2026-07-08*
