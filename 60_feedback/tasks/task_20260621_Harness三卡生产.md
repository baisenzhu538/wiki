---
id: "task_20260621_Harness三卡生产"
type: "production_task_list"
created_at: 2026-06-21
author: "王语嫣（综合欧阳锋裁决）"
executor: "老顽童"
---

# 生产任务：Harness Engineering 三卡 + 两更新 + 源归档

> 欧阳锋裁决：3 🟢 通过 + 2 🟡 降级为已有卡更新。

---

## 任务 1：三张新卡

### H-1：concept-harness-cattle-not-pets

- **路径**：`30_wiki/concepts/concept-harness-cattle-not-pets.md`
- **类型**：concept
- **核心内容**：
  - 定义：每轮迭代换全新 Generator 实例，从 checkpoint 重建状态，消灭代码情感依附
  - 对比：传统模式（同一 Agent 持续修改）vs 牲口模式（新实例无包袱）
  - 适用边界：质量敏感任务（代码/报告/方案）——简单一次性任务不需要
  - 桥接：调研域 Swarm 模式同样受益（每次探索用新 Worker 实例）
- **关联链接**：
  - → `framework-wanghuan-gan-three-roles`
  - → `framework-wanghuan-harness-seven-stages`
  - → `framework-multi-agent-research-architecture`
- **素材来源**：`diag_20260621_Harness Engineering文档诊断.md` §G1 + 源文章 §Sprint内部循环

### H-2：tool-harness-adversarial-tester

- **路径**：`30_wiki/tools/tool-harness-adversarial-tester.md`
- **类型**：tool
- **核心内容**：
  - 定义：对抗测试员——成功标准是"找到 bug"，找不到算失职
  - 攻击方法：空值/超长字符串/SQL注入/并发竞争/恶意输入
  - 与 SATs 的区别：Red Team = 模拟竞对策略（战略层），Adversarial Tester = 攻击具体产出（执行层）
  - Agent 执行指令：对抗测试 Prompt 模板
- **关联链接**：
  - → `tool-red-team-analysis`（SATs Red Team）
  - → `tool-devils-advocacy`（逻辑漏洞攻击）
  - → `framework-wanghuan-gan-three-roles`
- **素材来源**：`diag_20260621_Harness Engineering文档诊断.md` §G4 + 源文章 §主动攻击vs被动审查

### H-3：concept-harness-scoring-anchors

- **路径**：`30_wiki/concepts/concept-harness-scoring-anchors.md`
- **类型**：concept
- **核心内容**：
  - 1-5 分制 vs 1-10 分制——为什么 1-5 更好（LLM 评估者在 1-10 下集中打 7-8 分）
  - 语义锚点：每档必须写死含义，评估者无法和稀泥
  - "取较低值"原则：取两个评审者的较低分而非平均分——短板决定质量
  - 跨域可迁移性：调研六维门禁、案例评审、任何多评估者场景
- **关联链接**：
  - → `framework-yitang-research-quality-gate`（调研门禁可借鉴）
  - → `framework-wanghuan-harness-seven-stages`
- **素材来源**：`diag_20260621_Harness Engineering文档诊断.md` §G2 + 源文章 §评分体系

---

## 任务 2：两张已有卡更新

### 更新 A：framework-wanghuan-harness-seven-stages

- **路径**：`30_wiki/frameworks/framework-wanghuan-harness-seven-stages.md`
- **补充内容**：
  - Sprint 内部循环详图（Generator → 冒烟检查 → 4 Evaluator → 合并评估 → PASS/FAIL）
  - 评分体系的锚定规则（1-5 语义锚点 + "取较低值" + 零 CRITICAL 门槛）
  - 文件系统新组件：events.jsonl（时间机器）、lessons.md（错误记忆飞轮）
  - 模型分工详情：Opus(Phase0-1/1.5/6) / Sonnet(Phase2-5) / Codex+Gemini(评审)
  - 美学全链路：design-taste.md → Planner美学参考 → Adversarial查"AI烂活" → Polish Sprint → Aesthetic Reviewer
- **素材来源**：源文章 §Sprint内部循环 + §评分体系 + §文件系统 + §美学与品味

### 更新 B：framework-wanghuan-gan-three-roles

- **路径**：`30_wiki/frameworks/framework-wanghuan-gan-three-roles.md`
- **补充内容**：
  - "牲口而非宠物"模式（related 节新增 → `concept-harness-cattle-not-pets`）
  - 对抗测试员的显式激励结构（related 节新增 → `tool-harness-adversarial-tester`）
- **素材来源**：诊断报告 §G1 + §G4

---

## 任务 3：源文件归档

| # | 操作 | 路径 |
|:--|:---|:---|
| 1 | 移入 source 目录 | `00_inbox/Harness Engineering-让 AI 像团队一样写出生产级代码.md`（已就位）→ `10_raw/sources/src_20260621_harness-engineering-wanghuan.md` |
| 2 | 三张新卡 source_refs 均引用此 source | `src_20260621_harness-engineering-wanghuan.md` |

---

## 任务 4：跨域桥接链接

新卡创建后：

| 操作 | 文件 |
|:---|:---|
| `concept-harness-cattle-not-pets` 的 related → 链 `framework-multi-agent-research-architecture` | H-1 |
| `tool-harness-adversarial-tester` 的 related → 链 `tool-red-team-analysis` + `tool-devils-advocacy` | H-2 |
| `concept-harness-scoring-anchors` 的 related → 链 `framework-yitang-research-quality-gate` | H-3 |
| 反向：`tool-red-team-analysis` 的 related → 链 `tool-harness-adversarial-tester` | SATs 工具卡 |
| 反向：`framework-multi-agent-research-architecture` 的 related → 链 `concept-harness-cattle-not-pets` | 多智能体架构卡 |

---

## 卡片质量标准

每张卡必须包含：
- [ ] 一段话讲清楚
- [ ] 与相似概念的区分（如 Adversarial Tester vs Red Team vs Devil's Advocacy）
- [ ] 适用边界
- [ ] 跨域桥接（related 链接到另一域）
- [ ] source_refs 用 `10_raw/sources/` 路径

---

*王语嫣综合欧阳锋裁决 | 2026-06-21*
