---
id: framework-wanghuan-harness-seven-stages
title: 王欢：Harness 七阶段 AI 构建流程
type: framework
status: enriched
author: 王语嫣
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
source_refs:
- "10_raw/sources/src_20260619_1ffb2cef_wanghuan_harness的七个阶段_示意图.md"
- "10_raw/sources/src_20260619_e4b35a3a_wanghuan_task_product_system_transcript.md"
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
updated_at: '2026-06-19'
diagnostic_signals:
- signal: 单 Agent 或单次提示词做出来的东西"看着像但用起来坏"
  lens: 生成者与验收者角色未分离
  follow_up: 引入独立评估者角色，按用户视角逐功能测试并回传问题清单
- signal: 复杂项目做到一半发现技术栈选错，被迫推倒重来
  lens: 规划与技术栈选型缺失
  follow_up: 在动手生成前，先用最强推理模型输出 product-spec.md 与 tech-stack.md
- signal: 产品功能做完但视觉、空状态、错误状态明显粗糙
  lens: 缺少审美精修阶段
  follow_up: 在 Ship 前固定插入一轮 Polish Sprint，切换评分权重到审美维度
- signal: 交付后用户按 README 跑不起来
  lens: 最终交付门控缺失
  follow_up: 增加 FreshCloneTester 与 AuditTrail，把"从零克隆能跑"作为硬性 Ship 条件
related:
- '[[framework-wanghuan-task-product-system]]'
- '[[framework-wanghuan-actor-director-mode]]'
- '[[concept-wanghuan-ai-native-definition]]'
- '[[concept-wanghuan-power-of-standards]]'
- '[[framework-wanghuan-bitcoe-prompt-framework]]'
tags:
- 王欢
- Harness
- 多智能体
- 软件构建
- 质量门控
---

# 王欢：Harness 七阶段 AI 构建流程

> **Burn line**: 把生成者和验收者分开，是 Harness 从"损坏的玩具"变"可玩的游戏"的关键。
>
> **来源**：王欢 AI 实战分享（2026-06-18）

---

## 用一句话讲清楚

Harness 把一次复杂 AI 构建分解为**初始化、规划、技术栈选型、Sprint 对抗循环、审美精修、最终交付**七个阶段，每个阶段有明确输入、输出和质量门控。

---

## 核心要点

1. **Phase 0 · 初始化 & 预检**
   - 创建 harness/ 目录，检测 CLI 工具，生成 budget.yml（默认 50 轮迭代、8 个 Sprint、4 小时墙时）。
   - 自动检测是否需要从 checkpoint 恢复。
2. **Phase 1 · Planner：产品规划（Opus 模型）**
   - 用最强推理模型只做一次产品规划，成本可控。
   - 输出 product-spec.md：功能优先级、审美方向、迭代计划，并标出所有高风险歧义。
3. **Phase 1.5 · TechStackSelector：技术栈选型（Opus 模型）**
   - Planner 结束后立即确定技术栈。
   - 输出 tech-stack.md：语言、框架、测试工具、构建工具、部署目标、选型理由；Generator 不得自行引入未列出的顶层依赖。
4. **Phase 2-5 · Sprint 对抗循环**
   - 每轮 Sprint：写 Sprint Contract → 启动 Workflow → Generator 构建 → 四个 Evaluator 并行评分 → 决策引擎判断继续、修复还是裁剪范围。
   - 评分通过条件：没有维度低于 3 分、加权平均 ≥ 4.0 分（取两个代码审查者中更严者）、零 CRITICAL 对抗发现。
5. **Phase 5.5 · Polish Sprint：审美精修**
   - 所有 PO 功能完成后，自动插入一轮 Polish：空状态、错误状态、加载动画、字体节奏、微交互。
   - 评分权重自动切换（审美维度上调到 3，功能维度下调到 1）。
6. **Phase 6 · Ship Pipeline：最终交付**
   - 顺序执行，每步互为门控：
     1. AestheticReviewer（Opus）整体审美评分 ≥ 4.0 才过；
     2. 文档生成器写 README + CHANGELOG + KNOWN_LIMITATIONS 并提交；
     3. FreshCloneTester 从零克隆、按 README 操作，确认真的能跑；
     4. AuditTrail 生成从 spec 到 ship 的完整旅程记录。
7. **关键设计：生成者与验收者分离**
   - 单 Agent：20 分钟 / 9 美元，界面像那么回事，但核心功能损坏。
   - Harness：6 小时 / 200 美元，16 个功能都能用，包括 AI 精灵图生成器、AI 关卡设计器，可以实际玩。
   - 成本贵 22 倍，但产出从"损坏的玩具"变成"可玩的游戏"。

---

## 边界

| 适用 | 不适用 |
|:---|:---|
| 复杂产品或系统构建，需要高质量交付 | 简单一次性任务，单次提示词即可解决 |
| 有明确功能清单和验收标准 | 需求极度模糊，连自己要什么都还没想清楚 |
| 有足够时间和预算投入（数小时到数天） | 几分钟内必须出原型的极紧迫场景 |
| 团队能定义技术标准、审美标准和红线 | 没有技术判断能力，无法评估 AI 输出质量 |
| 目标是从"能用"到"真的好" | 只需要演示效果、不在乎真实可用性 |

---

## 失败模式 / 常见走偏

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **生成者与验收者合一** | 自己写自己审，看不到盲点 | 引入独立 Evaluator 或让 AI 扮演挑剔用户 |
| **跳过规划直接写代码** | 做到一半发现方向错误，返工严重 | 强制 Phase 1 输出 product-spec.md 并通过审查 |
| **技术栈随意变更** | Generator 自行引入未评审依赖 | Phase 1.5 锁定 tech-stack.md，写入禁止引入未列出依赖的约束 |
| **没有质量门控** | 功能看起来完成，实际无法使用 | 每轮 Sprint 设置最低分、平均分、CRITICAL 发现三项硬门槛 |
| **忽视审美精修** | 功能全对，但空状态、错误状态、加载体验粗糙 | 固定插入 Phase 5.5 Polish Sprint，并切换评分权重 |
| **文档与测试缺失就交付** | 用户拿到后跑不起来 | Ship Pipeline 把 FreshCloneTester 和 AuditTrail 设为硬性门控 |

---

## 行动 Checklist

- [ ] 在项目根目录创建 harness/，写入 budget.yml 明确迭代上限与墙时预算。
- [ ] 用最强推理模型跑 Phase 1，输出 product-spec.md，并标出所有高风险歧义。
- [ ] 在动手生成前完成 Phase 1.5，输出 tech-stack.md 并锁定顶层依赖。
- [ ] 设计 Sprint Contract 模板，明确每轮输入、输出、评分维度与通过条件。
- [ ] 为每轮 Sprint 配置至少四个 Evaluator，并设置最低分、平均分、CRITICAL 发现三项门控。
- [ ] 所有功能完成后自动触发 Phase 5.5 Polish Sprint，重点检查空状态、错误状态、加载动画。
- [ ] Ship 前运行 FreshCloneTester：从零克隆、按 README 操作，确认能跑。
- [ ] 生成 AuditTrail，记录从 spec 到 ship 的完整决策与变更链路。

---

## 相关卡 / 互链

- [[framework-wanghuan-task-product-system]]：Harness 是任务→产品→系统跃迁在复杂构建中的具体实现。
- [[framework-wanghuan-actor-director-mode]]：导演思维是 Harness 中规划、验收角色分离的认知基础。
- [[concept-wanghuan-ai-native-definition]]：Harness 是把 AI 默认纳入复杂构建流程的典型案例。
- [[concept-wanghuan-power-of-standards]]：Harness 的门控和评分机制依赖清晰标准。
- [[framework-wanghuan-bitcoe-prompt-framework]]：每个 Phase 的输入输出都可以用 BTICOE 进一步结构化。

---

## Critique

**攻击者 1：成本敏感者**
> "Harness 要花 6 小时和 200 美元，单 Agent 只要 20 分钟和 9 美元。对于大多数原型验证来说，Harness 太重了。"

**回应**：Harness 的成本结构是"一次做对" vs. "反复修补"。如果目标只是快速验证一个想法，单 Agent 足够；但如果目标是交付一个可被他人使用、可维护、可扩展的产品，Harness 的 22 倍成本换来的是从"损坏的玩具"到"可玩的游戏"的质变。选择哪种方式取决于阶段目标，而不是绝对成本。

**攻击者 2：流程教条主义者**
> "七个阶段必须严格执行吗？小公司没这么多资源。"

**回应**：Harness 的核心不是"七个阶段一个不能少"，而是**规划、执行、评估三种角色的分离**。资源有限时，可以压缩阶段，但不能消除分离。哪怕只有一个 Agent，也要在每次拿到结果后切换成"挑剔用户"视角验收。

**攻击者 3：AI 能力乐观派**
> "未来模型更强了，是不是就不需要 Harness 这种复杂流程了？"

**回应**：模型越强，对标准的依赖越高。Harness 的价值不在于弥补模型能力不足，而在于**把人的判断、行业标准和验收机制结构化**。即使模型能一次写对代码，它仍然需要人告诉它"对"的定义是什么。

**不要用**
- 不要把它用于简单到单次提示词就能解决的任务。
- 不要在没有明确验收标准时启动 Harness，否则门控会流于形式。
- 不要让生成者和验收者长期由同一个模型或同一个人担任。
- 不要为了流程完整而牺牲交付节奏——可以裁剪阶段，但不可裁剪角色分离。

---

## Synthesis

Harness 是王欢对"如何用 AI 高质量构建复杂产品"给出的工程化答案。它的核心不是增加步骤，而是把一次构建中隐含的角色冲突显性化：规划者负责想清楚，执行者负责做出来，评估者负责挑剔地验收。当这三种角色被严格分离并通过质量门控循环时，AI 产出的就不再是"看起来像"的演示品，而是真正可用、可维护、可迭代的系统。

这套框架的实践价值在于可裁剪性：初创团队可以只做 Phase 0-1-6 的最小闭环，成熟团队可以跑满七阶段。但无论裁剪多少，"生成者与验收者分离"这一原则不可妥协。王欢用单 Agent 与 Harness 的对比说明：成本差异是 22 倍，但产出差异是"有没有东西"的本质区别。在 AI 能力快速进化的今天，Harness 保护的恰恰是那些模型无法自动生成的部分——人的判断、行业标准和验收意志。

---

*基于王欢 2026-06-18 AI 实战分享整理，经欧阳锋审核。*
