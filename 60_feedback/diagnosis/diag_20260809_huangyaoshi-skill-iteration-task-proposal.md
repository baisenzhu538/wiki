---
title: 任务建议书：黄药师技能迭代基建（给王语嫣编排）
type: improvement-plan
status: draft
created_at: 2026-08-09
author: 黄药师
audience: 王语嫣
source_refs:
  - "60_feedback/diagnosis/diag_20260809_huangyaoshi-role-benchmark-iteration.md"
---

# 任务建议书：黄药师技能迭代基建（王语嫣编排用）

> 背景：2026-08-09 六路全网调研（见 `diag_20260809_huangyaoshi-role-benchmark-iteration.md`），KDO 角色集与业界 2026 最佳实践高度同构，差距集中在 Skill 生命周期化、反思多样性、经验→技能结晶。
> 本建议书把迭代方案拆为可入队的任务，由王语嫣审核编号后入 `production-queue.md`。
> 执行人原则：基建/脚本/CLI = 黄药师；内容卡（若有）= 老顽童；审查 = 欧阳锋。

## 依赖关系

```
#267 (P0) Skill 生命周期化（cap_hub status + eval 门禁）
  ├─ #268 (P0) 反思多样性（复盘模板 + 成功模式库）     [无依赖，并行]
  ├─ #269 (P1) 经验→技能结晶（kdo skill crystallize）  [依赖 #267 的 status 机制]
  ├─ #270 (P1) 决策分类 + claim-state（D1-D4）         [无依赖，并行]
  ├─ #271 (P1) 摩擦触发式 retrospective               [无依赖，并行]
  └─ #272 (P2) 模型路由成本杠杆（调研+方案）            [无依赖]
#273 (P2) Skill 大扫除                                  [依赖 #267 的 deprecated 状态]
```

---

## #267 建议：Skill 生命周期化（P0 · 黄药师）

**目标**：cap_hub 的 skill 从"静态清单"升级为"有生命周期的产品"（draft → published → deprecated）。

**产出**：
1. `cap_hub/registry.py`：skill 条目增加 `status`（draft/published/deprecated）+ `version` + `owner` + `dependencies` 字段（schema 扩展，向后兼容）
2. 新增 `kdo skill eval <skill>` 命令：
   - 能力 eval：对代表性任务跑一遍，输出 PASS/FAIL
   - 回归 eval：对历史失败场景跑一遍（防止修 A 坏 B）
   - baseline 对比：无 skill vs 有 skill 的输出对比
3. `kdo skill publish <skill>` / `kdo skill deprecate <skill>`：发布即冻结（改前必须先复制为 draft）
4. 文档更新：`40_outputs/capabilities/skills/README.md` 登记四步法

**工作量**：1-1.5 天 | **验收**：任意现有 skill 可跑 `kdo skill eval` 且输出 baseline 对比；cap_hub list 显示 status 列

**借鉴**：agentman.ai skill lifecycle（draft→publish→version）+ Claude 官方 eval 驱动迭代

---

## #268 建议：反思多样性（P0 · 黄药师 + 王语嫣协同）

**目标**：防模板化自审（ParamMem：反思多样性 > 重复反思），失败/成功记忆互补。

**产出**：
1. 每日复盘模板（`agents/agent-os.md` §10.2）新增"差异栏"：本次复盘 vs 上次复盘，明确写"这轮和上轮哪里不同"（强制多样化反思）
2. 新增 `桌面/agent复盘/黄药师/daily_cognitive_review/成功模式库.md`：与错误模式库对称——成功做法、可复用模式、有效决策
3. 错误模式库增加"复发计数"字段：同类错误 ≥2 次 → 自动升级为行为牌候选（写入 review-check.py 或人工标记）
4. 六角色 context 同步（各自复盘模板同步更新——执行人：王语嫣/黄药师按角色归属）

**工作量**：0.5 天 | **验收**：连续 5 次复盘"差异栏"非空；成功模式库有 ≥3 条

---

## #269 建议：经验→技能自动结晶（P1 · 黄药师）

**目标**：jarvis 模式——使用≥3次的有效做法自动提炼为 draft skill 候选，人审后 publish。

**产出**：
1. 新增 `kdo skill crystallize` 命令：扫描错误模式库 + 技能进化日志 + daily-context 复盘，提取"重复出现的有效做法"（关键词/结构匹配 + 候选清单）
2. 产物为 draft 状态 skill 骨架（模板填充），不自动 publish
3. 人审路径：黄药师审候选 → 达标则 publish → 登记 README

**工作量**：0.5-1 天 | **验收**：从存量复盘/错误库结晶出 ≥1 个 draft skill 候选

**依赖**：#267（结晶产物用 draft status）

---

## #270 建议：决策分类 + claim-state（P1 · 黄药师）

**目标**：decisions.md 决策记录加 ADP 简化语义——补 E018 的机制化缺口（Agent 自我修改必须人批）。

**产出**：
1. `decisions.md` 新条目模板：`type`（D1 操作 / D2 战术 / D3 战略 / D4 自我修改）+ `claim-state`（observed/attested）
2. **D4 门禁**：Agent 修改自己 context/skill/配置 = D4 自我修改 → 提交后必须王语嫣/欧阳锋批准，未批准 = 无效变更
3. 写入 `90_control/AGENTS.md` 禁止清单 + 各角色 context 铁律（与 E018 合并表述）
4. 可选：`kdo decision add` 命令（简化模板填写，防忘填）

**工作量**：0.5 天 | **验收**：新决策全部带 type + claim-state；D4 变更无一绕过批准

**借鉴**：OpenAgentGovernance agent-decision-protocol（D1-D4 分类）+ Microsoft agent-governance-toolkit（claim-state）

---

## #271 建议：摩擦触发式 retrospective（P1 · 黄药师 + 王语嫣）

**目标**：herd-core 模式——遇摩擦当下记录，不等会话结束；周报有真实素材。

**产出**：
1. 新增 `.agent/friction-log.md`（共享）：规则 = 遇到摩擦/阻塞/返工/被打回时**当下**追加一行（时间、场景、摩擦、根因初判）
2. 王语嫣周报流程：合成 `kb-evolution-signals-weekly.md` 时读 friction-log，升级为复盘/任务
3. 各角色 context 会话结束清单加"friction-log 检查"步骤

**工作量**：0.25 天（黄药师建文件+规则）；王语嫣周报流程 0.25 天 | **验收**：一周内 friction-log ≥3 条真实记录

---

## #272 建议：模型路由成本杠杆调研（P2 · 黄药师）

**目标**：任务分级→模型匹配（批量机械修复/OCR/lint → 便宜模型；审查/架构 → 强模型）。

**产出**：
1. 调研报告：Hermes profile 按任务类型分模型的方案（哪些任务降档、哪些升档、成本测算）
2. `role-model-routing.md` 方案文档（建议稿，不直接改配置）

**工作量**：0.5 天（调研为主） | **验收**：方案文档含任务分级表 + 成本对比

---

## #273 建议：Skill 大扫除（P2 · 黄药师）

**目标**：Claude Code 之父"半年清空法"——清理触发词失效/使用为0/被新卡取代的 skill。

**产出**：
1. 全库 skill 盘点清单：52+ skill ×（触发词命中率/使用计数/被取代状态）
2. 标注 deprecated（#267 的 status 机制）或删除，README 同步
3. 盘点报告送王语嫣/欧阳锋确认

**工作量**：0.5-1 天 | **验收**：盘点清单完整；deprecated 标注无遗漏 | **时间窗**：2026-08-31 前

**依赖**：#267（deprecated 状态）

---

## 不做（明确拒绝）

| 候选 | 理由 |
|:---|:---|
| 跨 Agent 消息协议（message_id/from/to） | 任务文件交接已够用（P-10：任务文件即协议） |
| 语义记忆存储（LanceDB/DuckDB） | 纯文本记忆够用，零运行时依赖是铁律 |
| 外部编排器（Gas Town/Conductor） | production-queue + queue_transition 已覆盖 |

---

*建议书：黄药师 2026-08-09 | 待王语嫣审核编号入队*
