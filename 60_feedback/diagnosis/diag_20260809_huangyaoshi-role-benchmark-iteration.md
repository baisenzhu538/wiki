---
title: 黄药师角色对标调研与技能迭代方案
type: improvement-plan
status: draft
created_at: 2026-08-09
author: 黄药师
source_refs:
  - "https://github.com/herd-ag/herd-core"
  - "https://www.tembo.io/blog/claude-code-multi-agent-orchestration"
  - "https://agentman.ai/blog/skill-building-best-practices-draft-publish-version"
  - "https://arxiv.org/abs/2602.23320"
  - "https://github.com/microsoft/agent-governance-toolkit/discussions/276"
  - "https://github.com/bounce12340/agent-governance"
---

# 黄药师角色对标调研与技能迭代方案（2026-08-09）

> 调研先行原则执行：六路全网调研（多 Agent 知识工厂 / Claude Code 子代理 / Skill 生命周期 / 自我进化记忆 / Agent 治理 / 中文实践）。
> 结论先行：**KDO 五绝分工与业界 2026 最佳实践高度同构，领先项是治理框架；主要差距在 Skill 生命周期化、反思多样性、经验→技能结晶三个方向。**

## 一、角色对标：KDO 五绝 vs 业界

| 业界角色（2026） | KDO 对应 | 差距 |
|:---|:---|:---|
| Orchestrator（hub-and-spoke 唯一协调点） | 欧阳锋 | ✅ 一致 |
| Strategist/Planner（选题定角度） | 王语嫣 | ✅ 一致 |
| Architect/Outliner | 欧阳锋（审查）+ 老顽童（生产） | 🟡 无独立 outliner |
| Writer/Producer（只写不研究） | 老顽童 | ✅ 一致 |
| Editor/QA（与生产隔离的事实核验） | 欧阳锋终审 + 王语嫣复核 | ✅ 一致（写审分离已制度化） |
| Publisher | 段王爷 | ✅ 一致 |
| **Builder/DevOps（开发+质量门+基建）** | **黄药师** | 🟡 业界是 builder+planner+ops 组合，KDO 黄药师已融合但缺"模型路由成本杠杆" |
| Research Agent（带源移交） | 老顽童/王语嫣素材消化 | 🟡 无结构化 handoff 契约 |

**结论**：KDO 角色集 2026 年仍先进。黄药师对标业界 = **builder/implementer + DevOps + harness engineer**（质量门=harness 层）。业界对我们的启发不在角色划分，在**角色内部的工作方法**。

## 二、六路调研关键发现

### 1. Skill 生命周期（agentman.ai + Claude 官方）——差距最大
- **draft → publish → version**：draft 是活的 workshop（边用边改），publish 冻结，version 可回滚
- **eval 驱动迭代**：能力 eval + 回归 eval + baseline 对比（无 skill vs 有 skill），按迭代轮次组织
- **Observe first, add later**：只有模型反复失败才加指令，不预先膨胀
- **Delete aggressively**：Claude Code 之父建议**每半年清空一次 claude.md/skills/hooks**——与 KDO"52 个 skill 越积越多"形成对比
- **SKILL.md < 500 行**，progressive disclosure
- **自改进循环**：Claude 读自己失败 transcript → 提议修复 → 重跑 eval 门禁——人从作者变 reviewer

### 2. 自我进化记忆（ParamMem / FORGE / R²-Mem / Anthropic Dreaming）
- **反思多样性 > 重复反思**（ParamMem：反思多样性与成功率正相关）——模板化每日复盘有"重复自审"风险
- **失败案例是更强纠正信号**（R²-Mem / ManimAgent），成功与失败记忆互补
- **Read-Write 反思循环**（Memento-Skills）：读阶段选相关技能，写阶段更新技能库
- **Dreaming 模式**：会话间隙跑 eval 回顾历史、找模式，产出新工作方法**供人审核后采纳**（不改原始库）
- FORGE：失败 → 规则/示例/混合三类知识制品

### 3. Agent 治理（herd-core / 三权分立 / ADP）——KDO 领先
- KDO 已具备：三权分立（AGENTS.md 宪法 + 王语嫣立法/任务单 + 老顽童行政 + 欧阳锋司法）、写审分离、testable-before-executable、git 字节 > 审查报告
- **差距**：
  - **决策分类缺失**（ADP D1-D4：D4 自我修改必须人批——Agent 改自己 context/skill 无门禁）
  - **决策记录无 claim-state**（absent/observed/attested 语义）
  - **摩擦触发式 retrospective 缺失**（herd-core：遇到摩擦立刻 file，leader 合成周报）
  - **维度数据缺失**（QA 拒绝率、返工率、token 花费——herd-core 全记录）

### 4. 中文实践（jarvis / 魔搭 Ultron / 腾讯 Team Memory）
- **jarvis 经验→技能结晶**：经验使用 ≥3 次自动提炼为 Skill——KDO 技能进化日志是手动追加，无自动结晶
- **Ultron HOT/WARM/COLD 热度分层**：高频验证记忆自动"结晶"为技能
- **腾讯四类记忆资产 + 四级可见性**（Private/Team/Restricted/Agent）
- 平凯 Loop：角色=岗位说明（prompt+知识库权限+工具授权）——KDO 同构 ✅

## 三、黄药师迭代方案（按优先级）

### P0-1：Skill 生命周期化
| 项 | 动作 |
|:---|:---|
| skill 注册表 | cap_hub 增加 status（draft/published/deprecated）+ version + owner + dependencies 字段 |
| eval 门禁 | 新增 `kdo skill eval <skill>`：能力 eval（代表性任务）+ 回归 eval（历史失败场景）+ baseline 对比 |
| 发布流程 | 修改 skill 前先复制为 draft，验证通过才 publish；发布即冻结 |
| 清理机制 | 每季度 skill 体检：触发词命中率、使用计数、被新卡取代 → 废弃列表 |

### P0-2：反思多样性（改每日复盘）
| 项 | 动作 |
|:---|:---|
| 差异维度 | 复盘模板加"本次 vs 上次复盘差异"栏，强制多样化反思（防模板化自审） |
| 成功记忆 | 错误模式库之外补"成功模式库"（ManimAgent：成功/失败记忆互补） |
| 失败升级 | 错误模式库加"复发计数"字段——同类错误 ≥2 次自动升级为行为牌候选 |

### P1-1：经验→技能结晶（jarvis 模式）
- 脚本：`kdo skill crystallize`——扫描错误模式库 + 技能进化日志 + 复盘文件，提取"使用≥3次的有效做法"→ 生成 draft skill 候选 → 人审后 publish
- 与 P0-1 的 cap_hub status 联动：结晶产物默认 draft

### P1-2：决策分类 + claim-state（ADP 简化版）
- 新决策写入 decisions.md 时带：type（D1 操作 / D2 战术 / D3 战略 / **D4 自我修改**）+ claim-state（observed/attested）
- **D4 门禁**：Agent 修改自己 context/skill/配置 = 自我修改 → 必须王语嫣/欧阳锋批准（对应 E018 铁律的机制化）

### P1-3：摩擦触发式 retrospective（herd-core 模式）
- 规则：遇到摩擦/阻塞/返工，**当下**记一行到 `.agent/friction-log.md`（不等会话结束）；王语嫣合成周报时汇总
- 与现有 Truman 10章复盘衔接：friction-log 是素材，复盘是成品

### P2-1：模型路由成本杠杆
- 简单任务（批量机械修复/OCR/lint）→ 便宜模型；审查/架构决策 → 强模型
- 落地：Hermes profile 按任务类型分模型，黄药师提交 `role-model-routing.md` 方案

### P2-2：Skill 大扫除（Claude 之父半年清空法）
- 2026-08-31 前：全库 skill 盘点 → 触发词失效/使用为 0/被新卡取代 → 标注 deprecated

## 四、不做的（明确拒绝）

| 候选 | 拒绝理由 |
|:---|:---|
| 跨 Agent 消息协议（message_id/from/to/task_id） | KDO 已用任务文件交接，协议化收益 < 成本（P-10 教训：任务文件即协议） |
| 语义记忆存储（LanceDB/DuckDB） | KDO 纯文本记忆已够用，零运行时依赖是铁律 |
| 外部编排器（Gas Town/Conductor 等） | KDO 生产队列 + queue_transition 已覆盖，且团队已跑通 |

## 五、验证方式

1. P0-1 完成标志：任意 skill 可跑 `kdo skill eval` 且输出 baseline 对比
2. P0-2 完成标志：连续 5 次复盘"差异栏"非空
3. P1-1 完成标志：从存量复盘/错误库结晶出 ≥1 个 draft skill 候选
4. 全部完成后：欧阳锋审查 + 用户验收
