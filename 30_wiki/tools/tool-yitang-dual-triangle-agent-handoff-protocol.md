---
id: tool-yitang-dual-triangle-agent-handoff-protocol
title: 子域 Agent 转交协议
type: tool
status: pending_review
author: 老顽童
reviewer: 欧阳锋
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
language: zh-CN
domain:
- yitang
- ai-collaboration
source_refs:
- 60_feedback/diagnosis/diag_20260708_yitang-dual-triangle-cross-domain-agent.md
related:
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
- '[[tool-yitang-dual-triangle-scenario-router]]'
- '[[tool-yitang-dual-triangle-domain-registry]]'
- '[[tool-yihang-dual-triangle-canvas]]'
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-yitang-y-model-dual-triangle-synergy]]'
created_at: 2026-07-08
updated_at: '2026-07-08T17:05:49+00:00'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# 子域 Agent 转交协议

> **一句话**：定义跨域双三角诊断 Agent 把用户问题转交给子域 Agent 时必须携带的信息包、上下文压缩规则、回退机制与再诊断入口。

---

## 目的

在 Agent 军团入口完成六要素扫描和子域匹配后，用户需要进入更专业的子域 Agent 继续深入。本协议确保转交时信息不丢失、不冗余、不变形：子域 Agent 能快速理解用户原始意图、已确诊的短板、约束边界和成功标准，避免重复询问和方向漂移。同时规定何时应回退到诊断 Agent，以及子域输出后如何再回到元诊断层校准。

---

## When to Use

- 诊断 Agent 已完成六要素扫描，并依据 [[tool-yitang-dual-triangle-scenario-router]] 决定进入子域。
- 需要在多个 Agent 之间维持会话连续性，避免用户反复复述背景。
- 子域 Agent 需要知道「用户真正想问什么」「当前最大瓶颈是什么」「不能碰的边界是什么」。
- 子域 Agent 输出后需要判断：是否已解决、是否需要回退、是否需要跨域迁移。

---

## When NOT to Use

- **一次性单轮任务**：无需跨 Agent 转交，直接调用子域 Agent 或通用 Agent 更快。
- **子域 Agent 已在前序对话中掌握完整上下文**：重复转交会增加噪音。
- **用户明确拒绝跨 Agent 流转**：应尊重用户选择，在诊断 Agent 内继续服务。
- **诊断结论置信度低于 0.60**：应先回到 [[concept-yihang-dual-triangle-core]] 补扫描，而不是强行转交。
- **目标子域尚未注册**：未注册域不应直接转交，应先走 [[tool-yitang-dual-triangle-domain-registry]]。

---

## 操作步骤

1. **构建信息包（Handoff Package）**：按下方字段模板收集并填充。
2. **上下文压缩**：将原始对话压缩到长度限制内，保留诊断结论和行动触发点，删除闲聊与重复追问。
3. **注入约束与成功标准**：明确子域 Agent 必须遵守的边界和交付标准。
4. **触发子域 Agent**：以信息包作为 system/user 上下文的开头，启动子域会话。
5. **子域输出质检**：子域 Agent 第一轮输出必须回应信息包中的「成功标准」和「最短板」。
6. **回退判断**：若触发以下任一条件，立即回退到诊断 Agent：
   - 子域 Agent 要求用户重复已提供的核心信息；
   - 子域输出偏离原始命题；
   - 用户表示「这不是我想要的」；
   - 子域 Agent 发现自己无法处理当前问题。
7. **再诊断入口**：子域输出后，向用户提供一句话入口：「是否需要回到跨域诊断 Agent，检查这个结果是否解决了你的真问题？」

---

## 示例/模板

### 信息包字段（Handoff Package）

| 字段 | 必填 | 说明 | 示例 |
|:---|:---:|:---|:---|
| `handoff_id` | 是 | 本次转交的唯一标识，便于回溯 | `dh-20260708-001` |
| `source_agent` | 是 | 发起转交的 Agent ID | `agent-spec-yitang-dual-triangle-cross-domain-diagnostician` |
| `target_agent` | 是 | 接收转交的子域 Agent ID | `agent-spec-demand-iceberg-coach` |
| `user_proposition` | 是 | 重述后的用户命题 | 「评估 AI 合同审查工具在律师行业的需求强度」 |
| `original_ask` | 是 | 用户原始输入，保留原话 | 「我想做一款 AI 工具帮律师审合同，靠谱吗？」 |
| `six_element_scan` | 是 | 六要素状态（有/无/弱/未知） | 审美:弱 / 体系:无 / 创造力:未知 / 场景:弱 / 数据:无 / 基本功:有 |
| `bottleneck_elements` | 是 | 1–2 个最短板 | `场景`, `数据` |
| `matched_scenario` | 否 | 路由表匹配到的场景编号与名称 | `#1 创业/业务方向模糊` |
| `constraints` | 否 | 必须遵守的边界（预算、时间、合规、不讨论范围） | 不替代法律专业判断；先验证需求再讨论产品功能 |
| `success_criteria` | 是 | 子域 Agent 输出应满足的 1–3 条标准 | 输出 3–5 张战略机会卡片；指出最危险假设；标注需用户验证的猜测 |
| `context_summary` | 是 | 压缩后的对话摘要，≤ 400 tokens | 用户有法律 SaaS 背景，未做过用户访谈，预算 3 个月，关注 MVP 形态 |
| `next_minimal_action` | 是 | 转交后子域 Agent 应推动的第一步 | 用需求冰山模型完成 L1–L3 定位 |
| `fallback_trigger` | 是 | 触发回退的具体条件 | 若用户否定目标用户群假设，立即回退 |

### 完整组装示例：AI 合同审查需求诊断 → 需求冰山教练

> 场景：用户问「我想做一款 AI 工具帮律师审合同，靠谱吗？」跨域诊断 Agent 完成六要素扫描后，决定转交给需求分析域的「需求冰山教练」。

```yaml
handoff_id: dh-20260708-001
source_agent: agent-spec-yitang-dual-triangle-cross-domain-diagnostician
target_agent: agent-spec-demand-iceberg-coach
user_proposition: 评估 AI 合同审查工具在律师行业的需求强度与切入点
original_ask: 我想做一款 AI 工具帮律师审合同，靠谱吗？
six_element_scan:
  审美: 弱       # 用户能感知合同审查痛点，但未形成产品审美判断
  体系: 无       # 缺乏律师行业工作流与合规体系的系统认知
  创造力: 未知   # 尚不清楚差异化功能应如何设计
  场景: 弱       # 有模糊场景（律师审合同），但具体角色、频次、付费主体不清
  数据: 无       # 未积累合同语料、错误案例、审查标准
  基本功: 有     # 用户本人有法律 SaaS 背景，懂合同审查基础
bottleneck_elements:
  - 场景
  - 数据
matched_scenario: "#1 创业/业务方向模糊"
constraints:
  - 不替代法律专业判断，产品定位只能是「辅助审查」
  - 先验证需求再讨论产品功能
  - 预算窗口 3 个月，需先跑通 MVP 需求验证
success_criteria:
  - 明确 2–3 个最可能的细分用户群（如独立律师 / 中小律所 / 企业法务）
  - 指出当前命题里最危险的 3 个假设
  - 给出下一步可验证的 1–2 个最小动作
context_summary: |
  用户有法律 SaaS 背景，未做过系统用户访谈，预算 3 个月，关注 MVP 形态。
  已确认：合同审查是高频刚需；未确认：目标用户是否愿付费、数据从哪来、合规边界在哪。
next_minimal_action: 用需求冰山模型完成 L1（现象）– L3（底层需求）定位，输出 3 张战略机会卡片
fallback_trigger: |
  若用户否定「律师愿意为 AI 合同审查付费」这一假设，
  或用户表示「我不是想做产品，只是想了解技术可行性」，立即回退到诊断 Agent。
```

**子域 Agent 收到后的第一句话示例**：

> 我已收到诊断 Agent 的转交包。你的核心命题是「评估 AI 合同审查工具在律师行业的需求强度」，当前最短板是 **场景** 和 **数据**。下面我们用需求冰山模型从 L1 现象层开始，先不讨论产品功能，只定位真需求。

### 上下文压缩规则

- **保留**：用户原始命题、六要素扫描结论、最短板、约束、成功标准、已确认的关键事实。
- **压缩**：把多轮追问压缩成 1–2 句摘要；删除问候、致谢、重复确认。
- **删除**：与当前子域无关的历史话题、用户临时发散的闲聊、诊断 Agent 的自我说明。

### 回退条件清单

| 条件 | 症状 | 动作 |
|:---|:---|:---|
| 输入缺失 | 子域 Agent 反复索要已提供信息 | 回退并补全信息包 |
| 方向漂移 | 子域输出偏离原始命题 | 回退重新匹配场景或校准命题 |
| 用户否定 | 用户表示结果不是想要的 | 回退做再诊断 |
| 子域过载 | 子域 Agent 声明无法处理 | 回退并标记为未来域 |
| 跨域需求 | 子域过程中发现需要另一个域的能力 | 回退到诊断 Agent 做跨域迁移判断 |

### 再诊断入口话术模板

```markdown
子域 Agent 已完成第一轮输出。你可以选择：
1. 继续在「{target_agent}」深入；
2. 回到跨域诊断 Agent，检查这个结果是否回应了你的原始命题；
3. 把当前输出作为源域，迁移到另一个域（如从需求分析迁移到产品内核设计）。
```

---

## Critique

### 内部局限

1. **压缩必然损失信息**：任何上下文压缩都会丢掉部分语境，尤其是用户未明说但反复暗示的偏好。子域 Agent 可能因此给出「技术上对、情境上错」的输出。
2. **回退条件依赖子域 Agent 自我报告**：如果子域 Agent 不主动声明无法处理或方向漂移，诊断 Agent 很难自动发现，需要人在环质检。
3. **跨 Agent 身份切换造成摩擦**：用户可能不习惯在不同 Agent 之间跳转，信息包再完整也可能被感知为「又要从头说一遍」。

### 外部攻击

**[Lucy Suchman，情境行动理论]**

> 计划（plan）与 situated action 之间存在根本张力。你把用户问题压缩成一个信息包，假设子域 Agent 能基于这个静态包继续推进。但真实协作是 messy 的，子域 Agent 在对话中会发现包里没有写到的关键情境。

**回应**：信息包不是静态契约，而是「起点协议」。子域 Agent 可以在执行中补充问题，但所有重大偏离必须触发回退或再诊断入口。

**[Brendan Dolan-Gavitt，上下文工程]**

> 上下文长度限制迫使我们做有损压缩，但决定哪些信息该丢、哪些该留，本身就是一个高认知负荷的判断。如果压缩规则太机械，会系统性地删掉那些「听起来不重要但很关键」的上下文。

**回应**：压缩规则采用「保留诊断结论 + 约束 + 成功标准」的硬清单，其余上下文由子域 Agent 按需追问，而不是一次性全部提供。

**[Jaron Lanier，Agent 过度中介]**

> 多个 Agent 之间转来转去，会让用户感到自己被一套自动化流程推着走，而不是在和一个能理解自己的协作者对话。Agent 军团的价值应该是隐形的，而不是让用户为架构买单。

**回应**：协议要求转交时向用户说明「为什么进这个 Agent」以及「随时可以说不满意并回退」，保持用户的控制感和退出权。

---

## Synthesis

本协议是 [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] 与子域 Agent 之间的接口标准。它上游依赖 [[tool-yitang-dual-triangle-scenario-router]] 的路由结论，下游依赖各子域 Agent 能读取并响应信息包字段。协议的健壮性不取决于单个子域 Agent 的能力，而取决于诊断 Agent 能否持续校准信息包的完整性和准确性。它与 [[tool-yitang-dual-triangle-domain-registry]] 联动：未注册域不应出现在 `target_agent` 字段中，避免把用户问题交给未准备好的 Agent。

---

## Related

- [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] — 发起转交的入口诊断 Agent
- [[tool-yitang-dual-triangle-scenario-router]] — 决定 target_agent 的路由表
- [[tool-yitang-dual-triangle-domain-registry]] — 新域注册与扩展协议
- [[tool-yihang-dual-triangle-canvas]] — 六要素扫描的输入来源之一
- [[concept-yihang-dual-triangle-core]] — 六要素框架定义
- [[framework-yitang-y-model-dual-triangle-synergy]] — 跨域迁移与迭代发动机
- [[agent-spec-demand-iceberg-coach]] — 子域 Agent 示例（需求分析域）
