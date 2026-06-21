---
id: "diag_20260621_Harness Engineering文档诊断"
type: "diagnosis_record"
created_at: 2026-06-21
author: "王语嫣"
source: "00_inbox/Harness Engineering_让 AI 像团队一样写出生产级代码.md"
---

# 诊断报告：Harness Engineering 文档

## 0. 素材性质

| 维度 | 内容 |
|:---|:---|
| 来源 | 王欢（基于 Claude Code 的 Harness 多 Agent 编排系统） |
| 形式 | 飞书长文（含架构图、流程图、评分雷达图、模型分工图） |
| 与已有关系 | wiki 已有 7 张王欢卡（来源于 2026-06-18 授课），本文件是同一体系的**实现细节深化版** |

---

## 1. 与已有知识库交叉比对

### 已有覆盖（不重复建设）

| 已有卡 | 覆盖内容 | 新文档对应 |
|:---|:---|:---|
| `framework-wanghuan-gan-three-roles` | 三角色架构、异构判别器、合成器 | §核心架构 |
| `framework-wanghuan-harness-seven-stages` | 七阶段流程、Sprint循环、交付管道 | §整体工作流、§交付管道 |
| `framework-wanghuan-three-tier-dev-architecture` | 三层开发架构 | — |
| `concept-wanghuan-adversarial-generation` | 对抗式生成概念 | — |

### 真正盲区（已有卡未覆盖）

| # | 新知识点 | 已有覆盖度 | 价值判断 |
|:--|:---|:---:|:---|
| G1 | **"牲口而非宠物"**——每轮迭代换全新 Generator 实例 | ❌ 零覆盖 | 🔴 高——这是 Harness 最反直觉且最关键的设计决策 |
| G2 | **1-5 锚定评分制**——为什么不用 1-10 + 语义锚点 + "取较低值" | ❌ 零覆盖 | 🟡 中高——实现细节，但"取较低值"是通用原则 |
| G3 | **模型分工策略**——Opus(规划/美学)/Sonnet(生成)/Codex+Gemini(评审) | ⚠️ seven-stages 提了 Opus 做规划，但未完整展开 | 🟡 中——成本最优化的具体方案 |
| G4 | **对抗测试员的成功标准**——"找到 bug 才算成功" | ❌ 零覆盖 | 🔴 高——这是 SATs 中 Adversarial Tester 在代码域的落地 |
| G5 | **美学作为持续压力**——design-taste.md + Planner 美学参考 + Adversarial 查"AI烂活" | ⚠️ seven-stages 有 Polish Sprint 但未展开美学全链路 | 🟡 中 |
| G6 | **双模式治理**——自动 vs 监督 | ❌ 零覆盖 | 🟡 中——Agent 自主决策 vs 人工审批的工程化治理 |
| G7 | **文件系统**——.harness/ 完整目录结构 + events.jsonl 时间机器 | ⚠️ seven-stages 提了 harness/ 目录和 budget.yml，但 events.jsonl/lessons.md 等未覆盖 | 🟢 低——实现细节 |

---

## 2. 六层交叉比对

| 层 | 评估 | 说明 |
|:---|:---:|:---|
| L1 可证伪 | A +0.15 | 王欢有实际运行数据（"6小时/200美元/16功能能用"），可验证 |
| L2 行为一致 | A +0.15 | 文中给了具体命令（`/harness build`）、目录结构、评分数据——言行一致 |
| L3 多源验证 | B 0 | 单一来源（王欢），但内部有多模型交叉验证逻辑。外部独立验证待补充 |
| L4 情绪标记 | B -0.05 | 写作风格有推广性（"不是魔法，是工程"），但数据具体不空洞 |
| L5 时间稳定 | A +0.10 | 2026年中的方法，基于稳定架构原则（GAN对抗、角色分离），非临时抱怨 |
| L6 利益相关 | C -0.05 | 王欢推广自己的方法论，有中度利益。但数据透明（200美元/22倍成本自曝） |

**综合置信度**：0.5 + 0.15 + 0.15 + 0.0 + (-0.05) + 0.10 + (-0.05) = **0.80 → 🟢 high**

---

## 3. 建议卡片

### 核心原则：不新建已有框架的重复卡，只补盲区

| # | 卡片 ID | 类型 | 来源 | 置信度 | 一句话 |
|:--|:---|:---|:---|:---:|:---|
| H-1 | `concept-harness-cattle-not-pets` | concept | G1 | 🟢 0.88 | "牲口而非宠物"——每轮迭代换全新 Generator 实例，消除代码情感依附 |
| H-2 | `tool-harness-adversarial-tester` | tool | G4 | 🟢 0.85 | 对抗测试员的显式激励结构——"找到 bug 才算成功"，与 SATs 的 Red Team 互补 |
| H-3 | `concept-harness-scoring-anchors` | concept | G2 | 🟢 0.82 | 1-5 锚定评分 + "取较低值"——防止评估者"中间偏好"和"高分冲平低分" |
| H-4 | `tool-harness-model-division-of-labor` | tool | G3 | 🟡 0.78 | 模型分工策略——Opus做规划/美学，Sonnet做生成，Codex+Gemini跨家族评审 |
| H-5 | `concept-harness-aesthetics-as-pressure` | concept | G5 | 🟡 0.75 | 美学作为持续压力而非事后装饰——design-taste.md + 对抗检查"AI烂活" |

### 已有卡更新（非新建，标注补充）

| 卡 | 补充内容 | 来源 |
|:---|:---|:---|
| `framework-wanghuan-harness-seven-stages` | 补充 Sprint 内部循环详图 / 评分体系的锚定规则 / events.jsonl / lessons.md | G2, G7 |
| `framework-wanghuan-gan-three-roles` | 补充"牲口而非宠物"模式 / 对抗测试员的显式激励 | G1, G4 |

---

## 4. 准入清单

### 🟢 建议放行（3 张——高价值、零覆盖）

| # | 卡片 ID | 理由 |
|:--|:---|:---|
| H-1 | `concept-harness-cattle-not-pets` | 反直觉设计模式，与已有 GAN 框架互补不重叠 |
| H-2 | `tool-harness-adversarial-tester` | 与 SATs 域（Red Team/Devil's Advocacy）直接桥接——是 SATs 在代码域的落地 |
| H-3 | `concept-harness-scoring-anchors` | "取较低值"是通用评审原则，可跨域复用（不限于代码评审） |

### 🟡 待审核（2 张——有价值但已有部分覆盖或需验证）

| # | 卡片 ID | 待审核原因 |
|:--|:---|:---|
| H-4 | `tool-harness-model-division-of-labor` | 模型分工依赖具体模型版本和价格，变化快——建议作为 `framework-wanghuan-harness-seven-stages` 的更新而非独立卡 |
| H-5 | `concept-harness-aesthetics-as-pressure` | 与 seven-stages 的 Polish Sprint 有重叠——建议合并更新而非独立卡 |

### 🔴 不建议独立入库

（无）

---

## 5. 域间桥接

本批次卡片的关键价值：**连接调研域与工程域**。

| 新卡 | 桥接到 |
|:---|:---|
| `tool-harness-adversarial-tester` | → `tool-red-team-analysis`（SATs Red Team 在代码域的落地） |
| `tool-harness-adversarial-tester` | → `tool-devils-advocacy`（攻击自己代码的逻辑漏洞） |
| `concept-harness-scoring-anchors` | → `framework-yitang-research-quality-gate`（调研域六维门禁可借鉴锚定评分） |
| `concept-harness-cattle-not-pets` | → `framework-multi-agent-research-architecture`（Swarm 模式也可用新鲜实例策略） |
| 全量 | → `concept-wanghuan-adversarial-generation` / `framework-wanghuan-gan-three-roles`（已有王欢域卡片） |

---

## 6. 与老顽童发现的关系

Harness = 老顽童多智能体架构发现（Supervisor/Swarm/Pipeline）的**生产级实现参考**。它不是新架构，而是 Supervisor 模式在软件工程域的一个完整落地案例——包含评分体系、模型分工、对抗测试、文件系统、交付管道。

---

*诊断人：王语嫣 | 2026-06-21 | 下一步：欧阳锋审核准入清单*
