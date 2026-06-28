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
- src_unknown
- src_unknown
domain:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-28'
diagnostic_signals:
- lens: 生成者与验收者角色未分离
  follow_up: 引入独立评估者角色，按用户视角逐功能测试并回传问题清单
- lens: 规划与技术栈选型缺失
  follow_up: 在动手生成前，先用最强推理模型输出 product-spec.md 与 tech-stack.md
- lens: 缺少审美精修阶段
  follow_up: 在 Ship 前固定插入一轮 Polish Sprint，切换评分权重到审美维度
- lens: 最终交付门控缺失
  follow_up: 增加 FreshCloneTester 与 AuditTrail，把"从零克隆能跑"作为硬性 Ship 条件
related:
- '[[concept-harness-scoring-anchors]]'
- '[[tool-harness-adversarial-tester]]'
- '[[plan_20260621_kdo-quality-harness-upgrade]]'
- '[[concept-harness-cattle-not-pets]]'
- '[[pending_unknown]]'
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
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
   - src_unknown
   - src_unknown
2. **Phase 1 · Planner：产品规划（Opus 模型）**
   - src_unknown
   - src_unknown
3. **Phase 1.5 · TechStackSelector：技术栈选型（Opus 模型）**
   - src_unknown
   - src_unknown
4. **Phase 2-5 · Sprint 对抗循环**
   - src_unknown
   - src_unknown
5. **Phase 5.5 · Polish Sprint：审美精修**
   - src_unknown
   - src_unknown
6. **Phase 6 · Ship Pipeline：最终交付**
   - src_unknown
     1. AestheticReviewer（Opus）整体审美评分 ≥ 4.0 才过；
     2. 文档生成器写 README + CHANGELOG + KNOWN_LIMITATIONS 并提交；
     3. FreshCloneTester 从零克隆、按 README 操作，确认真的能跑；
     4. AuditTrail 生成从 spec 到 ship 的完整旅程记录。
7. **关键设计：生成者与验收者分离**
   - src_unknown
   - src_unknown：6 小时 / 200 美元，16 个功能都能用，包括 AI 精灵图生成器、AI 关卡设计器，可以实际玩。
   - src_unknown

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

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 相关卡 / 互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Sprint 内部循环（实现细节）

每个 Sprint 的内部执行流程：

```
Generator（Sonnet）→ 生成代码
    ↓
冒烟检查：代码能跑吗？不能→PASS回退给Generator
    ↓
4 Evaluator 并行评审：
  ├─ Code Reviewer（Gemini）：逻辑/安全/性能
  ├─ Adversarial Tester（Codex）：空值/边界/恶意输入攻击
  ├─ Aesthetic Reviewer：AI烂活检测、视觉一致性
  └─ FreshCloneTester：从零克隆→安装→运行
    ↓
合并评估 → 评分（1-5语义锚点，取较低值）
    ↓
零CRITICAL？→ PASS：进入下一阶段
有CRITICAL？→ FAIL：退回Generator修复
```

---

## 评分体系锚定规则

| 分数 | 语义锚点 | 动作 |
|:---:|:---|:---|
| 5 | 生产就绪，可直接部署 | PASS |
| 4 | 小问题，修复<5分钟 | PASS |
| 3 | 中等问题，修复<1小时 | FAIL（退回） |
| 2 | 严重问题，需重新设计 | FAIL |
| 1 | 推倒重来 | FAIL |

**取较低值**：两个评审者取较低分，而非平均分。短板决定质量。
**零CRITICAL门槛**：任何CRITICAL bug → 自动FAIL，不论其他维度得分。

---

## 文件系统新组件

| 文件 | 作用 | 机制 |
|:---|:---|:---|
| `events.jsonl` | 时间机器——记录每轮迭代的完整输入输出 | 状态恢复、审计追溯、问题定位 |
| `lessons.md` | 错误记忆飞轮——记录每个bug和解决方案 | 后续Sprint自动参考历史教训 |
| `design-taste.md` | 美学参考——定义视觉风格和品质标准 | Planner和Aesthetic Reviewer的锚定 |

---

## 模型分工

| Phase | 主力模型 | 原因 |
|:---|:---|:---|
| Phase 0-1（规划+技术选型） | Opus | 最强推理，需要深度思考 |
| Phase 1.5（Sprint规划） | Opus | 分解任务需要全局视角 |
| Phase 2-5（生成+评审循环） | Sonnet | 性价比最优，代码生成质量高 |
| 代码评审 | Gemini | 异构模型交叉，避免"自己审自己" |
| 对抗测试 | Codex | 擅长攻击性测试 |
| Phase 6（最终门控） | Opus | 最高标准验收 |

**核心原则**：Generator和执行者用同一模型是合理的（Sonnet），但Evaluator必须用不同模型——"自己审自己的代码"是质量崩溃的根源。

---

## 美学全链路

```
design-taste.md（定义美学标准）
    ↓
Planner 读取 design-taste.md → 美学参考嵌入任务描述
    ↓
Generator 生成（受美学约束）
    ↓
Adversarial Tester 专门检查"AI烂活"：圆角不对/字体不统一/空白过多
    ↓
Polish Sprint：切换评分权重到审美维度（代码逻辑权重降到20%）
    ↓
Aesthetic Reviewer 最终审美验收
```

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
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Synthesis

Harness 是王欢对"如何用 AI 高质量构建复杂产品"给出的工程化答案。它的核心不是增加步骤，而是把一次构建中隐含的角色冲突显性化：规划者负责想清楚，执行者负责做出来，评估者负责挑剔地验收。当这三种角色被严格分离并通过质量门控循环时，AI 产出的就不再是"看起来像"的演示品，而是真正可用、可维护、可迭代的系统。

这套框架的实践价值在于可裁剪性：初创团队可以只做 Phase 0-1-6 的最小闭环，成熟团队可以跑满七阶段。但无论裁剪多少，"生成者与验收者分离"这一原则不可妥协。王欢用单 Agent 与 Harness 的对比说明：成本差异是 22 倍，但产出差异是"有没有东西"的本质区别。在 AI 能力快速进化的今天，Harness 保护的恰恰是那些模型无法自动生成的部分——人的判断、行业标准和验收意志。

---

*基于王欢 2026-06-18 AI 实战分享整理，经欧阳锋审核。*
