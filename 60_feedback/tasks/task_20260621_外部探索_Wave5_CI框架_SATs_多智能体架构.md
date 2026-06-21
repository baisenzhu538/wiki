---
id: "task_20260621_外部探索三个新盲区_Wave5"
type: "production_task_list"
created_at: 2026-06-21
author: "王语嫣"
reviewer: "欧阳锋（已裁决——全部通过 ✅）"
executor: "老顽童"
dependency: "diag_20260621_外部知识探索_三个新盲区.md"
priority_rule: "欧阳锋排期建议：Wave 0→4 先完成，Wave 5 后排。不因重要性而因上下文连续性。"
---

# 生产任务清单：Wave 5 — CI框架 + SATs + 多智能体架构

> 欧阳锋裁决：12 🟢 + 1 🟡 全部通过。Swarm 卡条件通过——需标注时间敏感性。

---

## Wave 5a：盲区 A — CI 框架（3张卡）

| # | 卡片 ID | 类型 | 素材来源 | 验收标准 |
|:--|:---|:---|:---|:---|
| W5-1 | `framework-ci-operating-model` | framework | diag §盲区A + web: BestBootcamps CI Framework Guide + Competitive Intelligence Alliance | Define→Gather→Analyze→Implement 四阶段循环 / 每阶段的决策问题和输出物 / 与一堂三层八模块的映射表（Gather=模块1-8，Define=无，Implement=无）/ "If output doesn't change a decision, you gathered trivia" |
| W5-2 | `tool-ci-define-phase` | tool | diag §盲区A + web: KITs/KIQs methodology | KITs（Key Intelligence Topics）和 KIQs（Key Intelligence Questions）定义方法 / 区分"想知道"和"需要知道" / 决策驱动的问题定义 / 示例：从"调研竞对"到"竞对的新定价是否会在Q3影响我们的win rate？" |
| W5-3 | `tool-ci-implement-phase` | tool | diag §盲区A + web: CI distribution best practices | 洞见嵌入运营节奏的方法 / battlecard 制作标准 / CI 资产度量（win rate impact / battlecard adoption rate / time saved）/ forecast call / QBR 嵌入模式 |

**关联要求**：
- `framework-ci-operating-model` → 链 `framework-yitang-research-weapon-system`（说明 CI 框架与一堂武器库的映射）
- `tool-ci-define-phase` / `tool-ci-implement-phase` → 链 `framework-ci-operating-model`
- `tool-ci-implement-phase` → 链 `tool-yitang-research-continuous-tracking`（持续跟踪是 Implement 的子集）

---

## Wave 5b：盲区 B — SATs 工具包（5张卡）

| # | 卡片 ID | 类型 | 素材来源 | 验收标准 |
|:--|:---|:---|:---|:---|
| W5-4 | `framework-structured-analytic-techniques` | framework | diag §盲区B + Heuer & Pherson "Structured Analytic Techniques for Intelligence Analysis" | SATs 8 类技术分类（诊断/contrarian/想象力/指标/假设检验/因果/冲突管理/决策）/ 每类选 1-2 代表 / 与一堂方法论的映射（九层深挖=ACH，交叉验证=多源验证） |
| W5-5 | `tool-key-assumptions-check` | tool | diag §盲区B + SATs 文献 | 系统性发现隐藏假设的四步法 / 案例（一堂进入 Skill 市场时的隐藏假设：企业客户愿意为内部工具付费？）/ Agent 如何自动列出和质疑假设 |
| W5-6 | `tool-devils-advocacy` | tool | diag §盲区B + SATs 文献 | 魔鬼代言人操作步骤 / Agent 如何自动扮演挑战者 / 模板："我们最大的风险是______，因为______" / 与"交叉验证"的区别（交叉验证是多源，魔鬼代言人是单一结论的主动反驳） |
| W5-7 | `tool-red-team-analysis` | tool | diag §盲区B + SATs 文献 | 竞对视角模拟四步法 / "如果我是竞对CEO"清单 / 与第3掌竞对跟踪的互补（跟踪=观察，Red Team=模拟决策） / 案例（如果竞对知道你正在做的事，他们会怎么反应？） |
| W5-8 | `tool-indicators-signposts` | tool | diag §盲区B + SATs 文献 | 定义"什么信号出现时假设需重新评估" / 可观测指标 vs 滞后指标 / Agent 如何自动监控 signals / 案例（一堂假设"企业客户会为 Skill 付费"→观察到的信号是什么？） |

**关联要求**：
- `framework-structured-analytic-techniques` → 链 `framework-yitang-nine-layer-deep-dig`（九层深挖=ACH 同构）
- `framework-structured-analytic-techniques` → 链 `framework-yitang-18-strategy-cards` 第 15 掌交叉验证
- `tool-devils-advocacy` / `tool-red-team-analysis` → 链 `skill-半肥猫-ai-research-validation`（纠偏概念）
- 每张 SATs 工具卡 → 链 `framework-structured-analytic-techniques`

---

## Wave 5c：盲区 C — 多智能体架构（4张卡）

| # | 卡片 ID | 类型 | 素材来源 | 验收标准 |
|:--|:---|:---|:---|:---|
| W5-9 | `framework-multi-agent-research-architecture` | framework | diag §盲区C + web: LangChain benchmark + Paiteq multi-agent guide + Lushbinary orchestration patterns | 四种模式对比矩阵（Supervisor/Swarm/Pipeline/Hybrid）/ 选择决策树 / 生产 failure modes / LangChain benchmark 数据（Swarm 比 Supervisor 少 40% token） |
| W5-10 | `tool-agent-research-supervisor` | tool | diag §盲区C + LangGraph supervisor pattern docs | Supervisor 模式操作步骤 / Agent 调研总指挥设计 / 可靠性保障 / 适用场景（合规分析、报告生成）/ 不适用场景（高并发探索） |
| W5-11 | `tool-agent-research-swarm` | tool | diag §盲区C + Kimi Deep Research Swarm | Swarm 模式操作步骤 / 并行探索+自动交叉验证 / ⚠️ 标注："2026年中快速演化领域，最佳实践可能半年后过时" / 与 Kimi Deep Research Swarm 的对比 / token 优势（-40% vs Supervisor） |
| W5-12 | `tool-agent-research-pipeline` | tool | diag §盲区C + OSCAR 五步法 | Pipeline 模式对应 OSCAR 五步法 / 每步的 Agent 实现 / 与"人手动 OSCAR"的差异 / 适用场景（依赖明确的串行任务） |

**关联要求**：
- `framework-multi-agent-research-architecture` → 链 `tool-agent-native-overview`（工具层→架构层）
- `framework-multi-agent-research-architecture` → 链 `concepts/kimi-深度调研集群方法论-deep-research-swarm`（参考案例）
- `tool-agent-research-pipeline` → 链 `framework-yitang-oscar-research`（OSCAR 对接）
- 每张架构卡 → 链 `framework-multi-agent-research-architecture`

---

## Wave 6：交叉链接与索引更新

| # | 任务 | 操作 |
|:--|:---|:---|
| W6-1 | `framework-yitang-research-weapon-system` related 补齐 | 新增：framework-ci-operating-model / framework-structured-analytic-techniques / framework-multi-agent-research-architecture |
| W6-2 | `framework-yitang-18-strategy-cards` 关联更新 | 第1-3掌（假设验证）→ 链 tool-key-assumptions-check / 第15掌（交叉验证）→ 链 tool-devils-advocacy |
| W6-3 | `30_wiki/index.md` 更新 | 添加 Wave 5 全部 12 张卡 |
| W6-4 | 与 Wave 0-4 的交叉链接一致性检查 | 确保两批卡之间没有死链或重复链 |

---

## 阻塞项

| 阻塞 | 状态 |
|:---|:---:|
| Wave 0-4 完成 | 老顽童已产 16/17 卡，4 项清理待完成 |
| Wave 5 依赖 | 无硬依赖——可与 Wave 0-4 清理并行，但欧阳锋建议串行以保持上下文连续性 |

---

## 卡片质量标准（同前）

每张 tool/framework 卡必须包含：
- [ ] 操作步骤（分步、可执行）
- [ ] 失败模式表
- [ ] 适用边界
- [ ] Action Triggers
- [ ] Agent 执行指令（CLI/API/MCP）
- [ ] 来源标注（source_refs 不含 `00_inbox` 路径）

---

*任务清单生成人：王语嫣 | 日期：2026-06-21 | 欧阳锋裁决：全部通过 | 老顽童排期：Wave 0→4 完成后执行*
