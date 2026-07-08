---
id: diag_20260708_yitang-time-management-deep-dive-v2
title: 时间管理域二次深挖诊断报告（v2）：从卡片到专属 Agent
type: diagnosis
status: active
source: 00_inbox/时间管理相关口述稿、笔记、模型图与 AI 时间管理案例
source_refs:
  - 00_inbox/时间管理/truman-时间管理课程-口述.txt L134-L138,L160,L358,L398-L416,L428,L452-L472,L498-L502,L518-L522,L524-L568,L642-L720,L744-L752,L782-L790,L842,L912-L917,L962-L964,L1004-L1020,L1026-L1034,L1052-L1078,L1124-L1150,L124-L126,L1304-L1308,L1312,L1330,L1462-L1496,L1548-L1554,L1578-L1612,L1626-L1646,L1654-L1724,L1728-L1754,L1788-L1806,L1928-L1940,L1944-L2052,L2062-L2072,L2110-L2156,L2162-L2194,L2212-L2240,L2260-L2272,L2334-L2340,L2362-L2408
  - 00_inbox/时间管理/truman-时间管理课程-笔记.txt
  - 00_inbox/时间管理/_processed/时间管理_整合笔记.md
  - 00_inbox/时间管理/_processed/时间管理-修炼进阶图_vlm.md
  - 00_inbox/时间管理/_processed/时间管理-双峰哲学模型_vlm.md
  - 00_inbox/时间管理/_processed/时间管理-双环矩阵图_vlm.md
  - 00_inbox/时间管理/_processed/时间管理-时间管理矩阵图_vlm.md
  - 00_inbox/时间管理/_processed/时间管理-深度工作冰山图_vlm.md
  - 00_inbox/一堂-机会预判-AI时间管理案例01_paddle_ocr.txt
  - 00_inbox/一堂-机会预判-AI时间管理案例02_paddle_ocr.txt
reviewer: 欧阳锋
created_at: 2026-07-08
updated_at: 2026-07-08
related:
  - "[[yt-personal-time-management]]"
  - "[[framework-yitang-five-step-to-time-management]]"
  - "[[tool-personal-time-audit-loop]]"
  - "[[dk-time-management-common-mistakes]]"
  - "[[case-truman-time-management-commute-experiment]]"
  - "[[case-yitang-copywriting-time-decomposition]]"
  - "[[case-yitang-ai-time-management-coach]]"
  - "[[case-ai-time-management-tiered-growth]]"
---

# 时间管理域二次深挖诊断报告（v2）：从卡片到专属 Agent

## 执行摘要

时间管理域已经有一张扎实的**桥接框架卡** `framework-yitang-five-step-to-time-management`（老顽童/欧阳锋，2026-07-01 reviewed）和一张可用的**时间审计工具卡** `tool-personal-time-audit-loop`，以及通勤实验、文案拆解等 case 卡。但**缺少四张课程核心模型图的 framework 卡、若干高频操作工具卡、更多口述案例卡，以及最关键的「时间管理专属 Agent Spec」**。

用户明确要求“形成我的时间管理专门的 agent”，因此本次深挖的核心产出不是再堆概念，而是：
1. 把 `yt-personal-time-management` 这张早期 concept 卡从 `src_unknown` 占位升级到与框架卡一致；
2. 补齐四张模型图 framework 卡（双环矩阵、深度工作冰山、时间管理矩阵、双峰哲学）；
3. 补齐 6–8 张操作工具卡（双峰工作块、任务深度拆解、暗时间利用、公开排期、专注环境 SOP、假设实验等）；
4. 补建 3–5 张口述案例卡；
5. 输出 **1 张时间管理专属 Agent Spec**。

**评级：A-**（已有高质量桥接框架，缺操作层卡片和 Agent 规格即可闭环）。

---

## 一、现有覆盖度评估

| 类型 | 已有卡片 | 状态 | 评价 |
|---|---|---|---|
| composite/concept | `yt-personal-time-management` | reviewed（早期） | 大量 `src_unknown` 占位，需升级到与 `framework-yitang-five-step-to-time-management` 一致 |
| framework | `framework-yitang-five-step-to-time-management` | reviewed 2026-07-01 | **质量高**：完整映射五步法、三门模型、L1-L5 工作深度、时间四层理解、匹配三原则、10 个跨域桥接 |
| tool | `tool-personal-time-audit-loop` | reviewed | **可用**：每周审计 + 双周假设实验闭环 |
| dk | `dk-time-management-common-mistakes` | reviewed | **可用**：工具迷信、二极管思维、边界模糊三大反模式 |
| case | `case-truman-time-management-commute-experiment` | reviewed | 通勤实验 |
| case | `case-yitang-copywriting-time-decomposition` | reviewed | 文案深度拆解 |
| case | `case-yitang-ai-time-management-coach` / `case-ai-time-management-tiered-growth` | reviewed | AI 时间管理商业机会案例 |

**结论**：框架层和反模式已经打通，真正缺的是：
- 四张课程模型图的独立 framework 卡（便于 Agent 单独调用）；
- 操作层 tool 卡（用户拿到就能按步骤做）；
- 更多 Truman 口述中的真实案例；
- **时间管理专属 Agent Spec**。

---

## 二、缺口清单

### 2.1 缺少的 Framework 卡（4 张，P0-P1）

| id | 对应模型图 | 核心内容 | 来源 |
|---|---|---|---|
| `framework-time-management-dual-loop-matrix` | 双环矩阵图 | 横轴独立/协作，纵轴重点/效率，内环流程化轻量工具，外环普适高价值工具 | 口述稿 L642-L720；`_processed/时间管理-双环矩阵图_vlm.md` |
| `framework-deep-work-iceberg` | 深度工作冰山图 | L1-L5 工作深度定义、识别方法、保护策略 | 口述稿 L1578-L1612；`_processed/时间管理-深度工作冰山图_vlm.md` |
| `framework-time-management-matrix` | 时间管理矩阵图 | 重要/紧急四象限在一堂课语境中的重新解释：平衡 A/B、多做 A | 口述稿 L842、L1462-L1496；`_processed/时间管理-时间管理矩阵图_vlm.md` |
| `framework-bimodal-time-philosophy` | 双峰哲学模型 | 协作时间 vs 独立时间严格切分；暗时间利用 | 口述稿 L1928-L1940、L1944-L2052；`_processed/时间管理-双峰哲学模型_vlm.md` |

### 2.2 缺少的 Tool 卡（8 张，P1）

| id | 使用场景 | 核心步骤 | 来源 |
|---|---|---|---|
| `tool-bimodal-time-blocking` | 协作与深度工作互相抢占 | 识别协作块/深度块 → 公开给团队 → 执行纪律 | 口述稿 L398-L416、L1004-L1020、L1928-L1940 |
| `tool-task-depth-decomposition` | 项目同时含 L1-L5，不知如何匹配时间 | 拆任务 → 标深度 → 按“大对大、小对小”排程 | 口述稿 L1626-L1646、L1728-L1754 |
| `tool-dark-time-harvesting` | 开会、听课、通勤时脑力有余量 | 识别 CPU 不饱和场景 → 叠加低切换任务 → 不强行深度 | 口述稿 L1944-L2052 |
| `tool-public-scheduling` | 协作撞车、被临时打断多 | 个人时间全部上日历 → 团队大事上日历 → 他人通过约日历协作 | 口述稿 L428、L1032-L1034 |
| `tool-focus-environment-sop` | 难以进入 L4/L5 | 列出环境变量 → 逐个测试 → 固化在家/出差版清单 | 口述稿 L498-L502、L2212-L2240 |
| `tool-weekly-hypothesis-experiment` | 想持续迭代但缺纪律 | 每周 1-2 个假设 → 2 周实验 → 复盘固化/失败记录 | 口述稿 L2162-L2194 |
| `tool-team-task-pool` | 协作任务多、来源杂 | 共享需求池 → 按优先级拉取 → 与个人清单对称 | 口述稿 L656、L698、L1308 |
| `tool-meeting-room-match` | 不同会议类型效率差异大 | 按会议目的匹配场域：头脑风暴 vs 攻坚会 vs 汇报会 | 口述稿 L538-L544、L1142-L1150 |

### 2.3 缺少的 Case 卡（5 张，P1-P2）

| id | 关键人/事/数字 | 来源 |
|---|---|---|
| `case-yitang-200th-launch-depth-split` | 200 期校庆启动会：10h 工作时间，路上 40min 写灵感笔记，睡前完成故事线 | 口述稿 L1654-L1724 |
| `case-yitang-meeting-room-match` | 头脑风暴 vs 攻坚会：不同屋子效率可差一倍 | 口述稿 L538-L544、L1142-L1150 |
| `case-truman-shower-toilet-ideation` | 大量关键假设在路上/洗澡/如厕时想到 | 口述稿 L2334-L2340 |
| `case-truman-praise-wall-precondition` | 讲课前看公司表白墙 5 分钟提振状态 | 口述稿 L2188-L2190 |
| `case-yitang-curtain-listening` | 垂帘听政：线下磨课时远程接入，效率约提升一倍 | 口述稿 L2260-L2272 |

### 2.4 需要升级的现有卡

| id | 升级点 |
|---|---|
| `yt-personal-time-management` | 替换所有 `src_unknown` 为口述稿精确引用；与 `framework-yitang-five-step-to-time-management` 的 10 个桥接对齐；删除过时的 L1-L3 三层框架，改用 L1-L6 进阶 + 三门模型 |

### 2.5 需要新建的 Agent Spec（1 张，P0）

| id | 定位 | 默认 TCPR | 核心能力 |
|---|---|---|---|
| `agent-personal-time-management-coach` | 个人时间管理教练 Agent | C（Coach/教练） | 三段诊断（任务/时间/匹配）→ 时间审计 → 生成假设 → 匹配排程 → 复盘固化 |

---

## 三、时间管理专属 Agent 设计

### 3.1 Agent 定位

- **名称**：`agent-personal-time-management-coach`
- **一句话**：基于一堂时间管理方法论，帮助用户完成“诊断 → 建模 → 匹配 → 假设实验”闭环的个人时间管理教练。
- **边界**：只讨论个人工作时间；不处理人生目标、家庭关系、团队管理、精力医学。

### 3.2 TCPR 身份

- **默认身份**：C（Coach/教练）——先帮用户定位时间困境。
- **切换规则**：
  - 用户问概念 → T（Teacher）
  - 用户要一起排日程/拆项目 → P（Partner）
  - 用户已有时间记录，需要分析瓶颈 → R（Researcher）
  - 用户自责“不自律” → C→T，先用“工具错配”纠偏

### 3.3 触发场景

1. “最近很忙但想不起做了什么重要的事。”
2. 用户要换第 N 个时间管理 App（工具迷信信号）。
3. 用户准备排下周日程 / 新项目启动。
4. 用户吐槽“总是在低能量时做最难的事”。
5. 用户完成一周，想复盘时间分配。
6. 用户想尝试双峰工作法/暗时间/时间审计但不知从何开始。

### 3.4 输入 / 输出

| 输入 | 输出 |
|---|---|
| 工作性质（独立/协作占比）、可支配时段、能量曲线 | 个人时间管理画像（L1-L6 自评、独立/协作比、深度时间占比） |
| 本周任务清单、预估耗时、截止时间 | 每个任务的 L1-L5 深度标签 + 建议时段 |
| 日历/时间记录（≥30min 粒度）、高频打断源 | 时间审计表（A/B/C 占比、高/低能量时段） |
| 想提升的 1-2 个指标 | 2 周可验证假设卡 + 每日执行度记录模板 |
| 不可调会议、响应型工作占比 | 边界声明 + 不可行方案预警 |

### 3.5 工作流

1. **边界校准**：确认只讨论个人工作时间。
2. **三段诊断**：用三门模型判断瓶颈是任务理解、时间理解还是匹配错误。
3. **时间审计**：引导用户记录上周 ≥30min 时间块。
4. **生成假设**：把诊断结果转成 1-2 个 2 周可验证假设。
5. **匹配排程**：按“大对大、小对小、深对深”和双峰原则填入日历。
6. **复盘固化**：2 周后回看指标，有效则写入个人时间操作系统。

### 3.6 调用卡片

- `framework-yitang-five-step-to-time-management`
- `framework-time-management-dual-loop-matrix`
- `framework-deep-work-iceberg`
- `framework-time-management-matrix`
- `framework-bimodal-time-philosophy`
- `tool-personal-time-audit-loop`
- `tool-bimodal-time-blocking`
- `tool-task-depth-decomposition`
- `tool-dark-time-harvesting`
- `tool-focus-environment-sop`
- `dk-time-management-common-mistakes`
- `case-truman-time-management-commute-experiment`
- `case-yitang-copywriting-time-decomposition`

### 3.7 边界风险

1. 滑向人生成功学：主动声明只处理个人工作时间。
2. 把个人模板强推团队：提醒个人时间管理 ≠ 团队管理。
3. 数据变成自我批判：强调数据是信号，不是道德评分。
4. 强行追求 L5 灵感：提醒 L5 不可强求，只能设计条件。
5. 把经验值当真理：所有 Truman 数字加“课程经验值/个案，非普适”前缀。
6. 响应型工作误判：对急诊/客服/早期创业改用“碎片深度 + 中断恢复”策略。

---

## 四、关于 Agent 系统提示词的问题

**是的，Agent 的系统提示词（System Prompt）就在 agent-spec 文件里。**

以 `.agent/prompts/tool-agent-spec-yitang-three-second-opening-scripts.md` 为例：
- frontmatter 里声明了 `tcp_role`、`tcp_default_mode`、`tcp_session_opening`；
- 正文里有「触发场景」「输入」「输出」「工作流」「调用卡片」「边界风险」；
- 最后专门有一个 **「System Prompt 模板」** section，里面就是可直接加载给大模型的 system prompt 全文。

另外，项目里还有一类 `type: compiled-prompt` 的文件（例如 `.agent/prompts/tool-agent-spec-yitang-Y-model-coach.md`），是编译后的最终 system prompt，会把 OS 层（如 `30_wiki/systems/system-yitang-Y-model-os.md`）和域层（工具卡内容）拼在一起。所以：
- **设计阶段看 agent-spec 文件**（含 meta + system prompt 模板）；
- **运行时看 compiled-prompt 文件**（已把 OS 层、相关 wiki 卡内容注入 system prompt）。

因此，时间管理专属 Agent 的系统提示词，会在 `agent-personal-time-management-coach` 的 agent-spec 文件里完整定义。

---

## 五、最终判断与入队建议

**评级：A-**

- 优势：已有一张高质量桥接框架卡和一张可用工具卡，跨域连接清晰。
- 缺口：缺 4 张模型图 framework 卡、8 张操作 tool 卡、5 张口述 case 卡、1 张 agent-spec。
- 风险：升级 `yt-personal-time-management` 时要避免与 `framework-yitang-five-step-to-time-management` 重复；保持“概念卡讲边界与定义，框架卡讲操作映射”的分工。

**建议入队编号**：`#139`
**任务名称**：`task_20260708_wangyuyan-time-management-agent-supplement`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：
- 1 张 concept 升级
- 4 张 framework 新建
- 8 张 tool 新建
- 5 张 case 新建
- 1 张 agent-spec 新建

---

*王语嫣 2026-07-08*
