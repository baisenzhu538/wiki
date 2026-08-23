---
id: file-flow-protocol
title: 《KDO 文件流转规范》v1.0
type: protocol
version: v1.0
author: 老顽童
created_at: '2026-08-23T16:30:00+08:00'
updated_at: '2026-08-23T16:30:00+08:00'
status: effective
effective_from: '2026-08-23'
approved_by: 老朱（2026-08-23 终稿拍板生效；欧阳锋终审 PASS A-）
audience: 六角色
status: pending_review
supersedes: null
amends: null
---

# KDO 文件流转规范 v1.0

> 把 charter §3.15「已交冻结与文件流转规范」总纲展开为可执行、可 lint 的条文。向前生效：生效日起的新文件必须合规，存量既往不咎（不回头改已交文件）。本规范自身 v1.0 起版，订正走本规范第 3 节。

## 1. 目的与适用范围

文件多写必出问题（E046 吞节实证：任务单被追加改写导致内容被吞）。本规范统一六角色文件协作的**命名 / 版本 / 时间戳 / 唯一编号 / 冻结纪律**，使文件流转可 lint、可追溯、可问责。

适用文件类型：
- 一次性交付物：建议书（`60_feedback/diagnosis/`）、审查意见书、诊断报告、洞察/建议文件
- 流转文件：任务单（`60_feedback/tasks/`）
- 资产文件：wiki 卡片（`30_wiki/`）、spec 卡（`30_wiki/agent-specs/`）、规范文档（`90_control/`）、复盘（`agent复盘/<角色>/daily-context/`）

## 2. 四件套总则（每个 agent 的文件流转统一）

| # | 要素 | 要求 |
|:--|:--|:--|
| 1 | **唯一编号** | 建议书/诊断/审查意见书 frontmatter 必填 `doc_id: D-YYYYMMDD-NNN`（当日三位序号，跨 agent 全局唯一，lint 查重）；任务单沿用队列号 #xxx；spec 卡沿用卡片 id。三套编号不混用（E045） |
| 2 | **版本号** | frontmatter `version: v1.0` 起版；订正/增补 = 另起新文件 v1.1/v1.2（`amends: <旧 doc_id>` 必填引用）；重大重写 = +1.0。**已交冻结文件的版本号永不变** |
| 3 | **日期时间节点** | `created_at` / `updated_at` 必填（ISO 8601）；冻结文件以 `updated_at` 为终态时间戳；`frozen_at` 可选标注进入看板流程时刻 |
| 4 | **命名方式** | `diag_YYYYMMDD_<author>-<slug>.md`、`task_YYYYMMDD_<assignee>-<slug>.md`；slug 禁路径词/空格（F-040 口径）；订正件 slug 加后缀 `-v1.1` 或 `-amend` |

## 3. 版本号细则

| 变更类型 | 动作 | 示例 |
|:--|:--|:--|
| 初始成文 | 起版 v1.0 | `version: v1.0` |
| 订正（小改：措辞/补例/数字修正） | **另起新文件** v1.1，`amends: <旧 doc_id>` 引用旧件 | `diag_20260823_x-xx-v1.1.md`（amends: D-20260823-001） |
| 增补（原件缺节/新场景） | 另起新文件 v1.2 或 `-amend` 后缀件，引用原件 | `-amend.md` |
| 重大重写（结构/口径重构） | +1.0（v2.0） | `version: v2.0` |

**红线**：已交冻结文件（见 §6）版本号永不变、正文永不回头改；订正/增补一律新件，原件留档作口径演进链。

## 4. 日期时间节点细则

- `created_at`：文件首次写入时间（ISO 8601，`YYYY-MM-DDTHH:MM:SS+08:00` 或 `YYYY-MM-DD` 起版允许）。
- `updated_at`：最后修改时间；**冻结文件以 updated_at 为终态时间戳**（冻结后不再更新）。
- `frozen_at`（可选）：进入看板流程的时刻（探针登记 / 队列 queued）。
- 复盘 `daily-context/YYYY-MM-DD.md` 用日期作文件名，时间戳在文件内。

## 5. 命名方式细则

| 文件类 | 模板 | 示例 | 禁项 |
|:--|:--|:--|:--|
| 建议书/诊断/审查 | `diag_YYYYMMDD_<author>-<slug>.md` | `diag_20260823_laowantong-disposal-keyword-misjudgment.md` | slug 禁路径词/空格（F-040） |
| 任务单 | `task_YYYYMMDD_<assignee>-<slug>.md` | `task_20260823_laowantong-file-flow-protocol.md` | 同上 |
| 订正件 | 原 slug + `-v1.1` / `-amend` | `diag_20260823_x-xx-v1.1.md` | 不覆盖原文件 |
| spec 卡 | `agent-spec-<role>.md` | `agent-spec-laowantong-producer.md` | 卡片 id 命名不混入 doc_id |
| wiki 卡 | `<type>-<域>-<slug>.md` | `framework-利润-利润优先经营框架.md` | 类型前缀（concept/case/dk/tool/framework/bridge） |

**E045 三套编号不混用**：doc_id（D-编号）只用于建议书/诊断/审查意见书；#队列号只用于任务单；卡片 id 只用于 wiki 卡。

## 6. 两类纪律细则（2026-08-23 老朱口径收严）

### 6.1 一次性交付物（建议书/诊断/审查意见书）：已交冻结

- **进入看板流程后一字不改**——「进入看板流程」= 落 `60_feedback/diagnosis/` 且被探针登记（或人工放入 PROPOSAL-PENDING 段）。
- 探针登记 / 王语嫣裁定划行**不构成对文件的修改**——看板行在队列文件，不在建议书内。
- 订正/增补一律另起新文件（新编号，`amends:` 引用旧件），已交文件永不回头改。

### 6.2 流转文件（任务单）：上板冻结

- **任务单一旦上看板（queued 及之后）不能再改、不能追加、不能删节**。
- 任何修订/增补一律新增任务单单独编排，原单冻结不动。
- **唯一例外**：frontmatter 状态字段归 `queue_transition.py` 独占（status/assignee/updated_at 流转脚本写入，人不得手改）。

### 6.3 冻结判定口径（什么算「已交」）

| 文件类 | 冻结触发点 | 备注 |
|:--|:--|:--|
| 建议书/诊断 | 落 diagnosis/ 并被探针登记（或人工放入 PROPOSAL-PENDING） | 登记即冻结 |
| 任务单 | 上看板（queued） | 流转状态字段例外 |
| spec/wiki 卡 | 提审（pending_review） | 终审退回后按 §6.4 |
| 复盘 | 落盘即冻结 | 历史文件不回改（Truman 格式收口对 08-22 后生效） |

### 6.4 复审退回后的补件方式

- **原则上补件也是新增件/新单**，不改原单正文——退回意见（P0/P1/P2）记录在任务单终审节（欧阳锋写入），生产者修复后**重提**走 queue_transition 状态机（pending_review → queued → claimed → pending_review），修复内容在交付物（卡/spec）内，不在任务单正文内。
- 例外：执行报告节（F-034）在 complete 前可由生产者填写（该节属于交付物的一部分，非任务单正文内容）。

## 7. 六角色文件清单表

| 角色 | 产出文件类型 | 纪律类型 | 命名模板 | 编号空间 |
|:--|:--|:--|:--|:--|
| 老顽童 | wiki 卡（五类）、spec 卡、完成报告、建议书 | 卡=提审冻结；报告=交付物 | `framework-利润-xxx.md` / `task_xxx-完成报告.md` / `diag_YYYYMMDD_laowantong-*.md` | 卡 id / #队列 / D-编号 |
| 欧阳锋 | 审查意见书、终审记录（写入任务单终审节） | 已交冻结 | `diag_YYYYMMDD_ouyangfeng-*.md` | D-编号 |
| 王语嫣 | 任务单、队列行、dashboard、规范 | 任务单=上板冻结；规范=定稿拍板冻结 | `task_YYYYMMDD_<assignee>-<slug>.md` | #队列 |
| 黄药师 | 基建脚本、工具文档、规范支撑 | 交付=代码+commit+生效验证三件套 | `kdo-tools/xxx.py` / `diag_YYYYMMDD_huangyaoshi-*.md` | D-编号 |
| 风清扬 | 建议书、审计报告、洞察 | 已交冻结 | `diag_YYYYMMDD_fengqingyang-*.md` | D-编号 |
| 老朱 | 终稿拍板、指令（CLI 通道） | 指令=对话通道（F-041），裁定落盘为规范 | — | — |

## 8. 可 lint 化条目（#450 工具落地清单）

| # | 检查项 | 规则 | 等级 |
|:--|:--|:--|:--|
| L1 | doc_id 查重 | 建议书/诊断 frontmatter 有 doc_id 且当日不重复 | error |
| L2 | doc_id 格式 | `D-YYYYMMDD-NNN` 正则 | error |
| L3 | 版本号存在 | 建议书/诊断 frontmatter 有 version | error |
| L4 | 时间戳存在 | created_at/updated_at 非空 | warning |
| L5 | 命名合规 | 文件名匹配模板（diag_/task_ + 日期 + author/assignee + slug） | warning |
| L6 | slug 禁路径词 | slug 不含路径/文件名/目录词（F-040） | warning |
| L7 | 冻结检测 | 已冻结文件（看板流程中）的 mtime 变化告警 | error |
| L8 | 版本引用 | 订正件 amends 指向存在且被引用旧件 | warning |
| L9 | 三套编号不混用 | 任务单 frontmatter 不含 doc_id；wiki 卡 frontmatter 不含 #队列号 | warning |

## 9. 生效规则

- 本规范经欧阳锋终审 + 老朱终稿拍板后 v1.0 生效；生效后 #450（工具支撑）开工。
- **向前生效**：生效日起的新文件必须合规；存量既往不咎（不回头改已交文件，charter §3.15 同款）。
- 修订本规范自身：按 §3 版本号细则走（订正=新文件 amends 引用本件）。

---

*老顽童主笔 · 2026-08-23 · 依据 charter §3.14/§3.15 + E046 吞节实证 + 黄药师 08-23 先例 + 欧阳锋 append-only 建议书；无出处不写入*
