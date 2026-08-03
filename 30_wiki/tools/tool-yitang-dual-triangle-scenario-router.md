---
id: tool-yitang-dual-triangle-scenario-router
title: 双三角场景路由表
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
- 30_wiki/concepts/concept-yihang-dual-triangle-core.md
aliases:
  - 双三角场景路由表
  - 角场景路由表
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-yitang-y-model-dual-triangle-synergy]]'
- '[[tool-yihang-dual-triangle-canvas]]'
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
- '[[tool-yitang-dual-triangle-agent-handoff-protocol]]'
- '[[tool-yitang-dual-triangle-domain-registry]]'
created_at: 2026-07-08
updated_at: '2026-07-08T17:05:49+00:00'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# 双三角场景路由表

> **一句话**：一张把用户模糊问题快速映射到双三角六要素短板，并推荐对应子域 Agent/框架卡的决策表。

---

## 目的

解决跨域双三角诊断 Agent 在分诊阶段「知道问题属于哪类、该进哪个子域」的映射问题。通过把常见输入模式、六要素扫描重点和推荐子域 Agent/框架卡显式化，减少用户在不同 Agent/工具之间反复试错的成本，同时为新域预留扩展槽，避免路由表变成封闭分类。

---

## When to Use

- 用户问题模糊，可能跨越多个知识域，需要先做一次「元诊断」。
- 需要向用户解释「为什么推荐这个 Agent/框架卡」，而不是直接给答案。
- 在 [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] 的工作流中，完成六要素扫描后进入子域匹配阶段。
- 团队要新增子域 Agent，需要先在路由表中为其找到位置。
- 组织级 AI 落地前做全局分诊，判断各业务线该进入哪个子域流程。

---

## When NOT to Use

- **一次性简单任务**：如「帮我写一封邮件」，直接调用通用 Agent 更快。
- **未经六要素扫描的问题**：如果还没判断短板，路由表只是随机匹配。
- **已明确属于单域且上下文完整**：无需再经过诊断 Agent 转一道。
- **需要法律/医疗/合规最终判断**：路由表只给建议，不做最终裁决。
- **未来域尚未注册**：强行把未注册域塞入已有分类会导致错配，应先走 [[tool-yitang-dual-triangle-domain-registry]]。

---

## 操作步骤

1. **问题重述**：把用户原始输入转写为可分析的命题，明确目标与边界。
2. **六要素快速扫描**：按 [[concept-yihang-dual-triangle-core]] 对审美、体系、创造力、场景、数据、基本功做「有 / 无 / 弱 / 未知」四级标注。
3. **短板识别**：找出当前最大瓶颈，通常不超过 2 个要素。
4. **查表匹配**：根据输入模式与短板，在下表中找到最接近的场景行。
5. **输出路由建议**：给出推荐子域 Agent/框架卡、置信度、风险提示与下一步最小动作。
6. **未匹配处理**：若无法匹配已知域，标记为「未来域」并给出临时处理建议，提示用户补充域注册信息。

---

## 示例/模板

### 七类高频场景 × 六要素扫描重点 × 推荐子域 Agent/框架卡

| # | 高频场景 | 典型用户输入 | 六要素扫描重点 | 推荐子域 Agent / 框架卡 | 置信度 |
|---|:---|:---|:---|:---|:---:|
| 1 | 创业/业务方向模糊 | 「我想做一款 AI 工具帮律师审合同，靠谱吗？」 | 场景 > 审美 > 数据 | [[agent-spec-demand-iceberg-coach]]、[[framework-yitang-y-model-dual-triangle-synergy]] | 0.80 |
| 2 | 子域 Agent 输出质量不稳定 | 「需求分析 Agent 给的需求总感觉很虚。」 | 数据 > 审美 > 体系 | [[tool-yihang-dual-triangle-canvas]]、[[agent-spec-dual-triangle-canvas-filler]] | 0.82 |
| 3 | 跨域迁移 | 「销售前三秒话术能不能用到内容钩子设计？」 | 体系 > 创造力 > 基本功 | [[framework-yitang-y-model-dual-triangle-synergy]]、[[tool-yitang-dual-triangle-agent-handoff-protocol]] | 0.78 |
| 4 | 组织级 AI 落地前全局诊断 | 「公司想全面拥抱 AI，先从哪块业务切入？」 | 场景 > 数据 > 体系 | [[method-dual-triangle-flywheel-engine]]、[[framework-yihang-AI-native-dual-triangle-kernel]] | 0.75 |
| 5 | 个人 AI 协作成长导航 | 「学了很多 AI 工具，越学越乱。」 | 审美 > 体系 > 基本功 | [[framework-yihang-dual-triangle-weapon-library]]、[[tool-yihang-dual-triangle-canvas]] | 0.80 |
| 6 | 复盘失败项目 | 「上一个 AI 项目三个月没跑通，问题在哪？」 | 数据 > 体系 > 场景 | [[method-dual-triangle-flywheel-engine]]、[[tool-yitang-project-retro-value-mining]] | 0.77 |
| 7 | 判断 Agent/工具是否值得投入 | 「这个新的 AI coding 工具我们要不要接？」 | 基本功 > 场景 > 数据 | [[framework-yihang-dual-triangle-ai-landing-five-steps]]、[[tool-纪浩-AI工具脚本化约束]] | 0.76 |
| — | **未来域扩展槽** | 任何尚未注册的新域问题 | 先用六要素做最小扫描 | 临时建议 + [[tool-yitang-dual-triangle-domain-registry]] | 0.60 |

### 路由输出模板

```markdown
- **用户命题**：{重述后的可分析问题}
- **六要素扫描**：审美({状态}) / 体系({状态}) / 创造力({状态}) / 场景({状态}) / 数据({状态}) / 基本功({状态})
- **最短板**：{要素 1}、{要素 2（如有）}
- **匹配场景**：#{编号} {场景名称}
- **推荐 Agent/框架卡**：`{卡片 ID}`
- **置信度**：{0.00-1.00}
- **风险提示**：{为什么可能错配}
- **下一步最小动作**：{一个具体动作 + 成功指标}
```

---

## Critique

### 内部局限

1. **启发式而非因果模型**：路由表基于已观察到的七类高频场景归纳而来，并未证明这些场景在统计上覆盖全部用户输入。新增域的分布可能迅速改变表的可用性。
2. **维护成本被低估**：扩展槽只是占位符，真正要让新域接入，需要持续更新触发关键词、评估问题和推荐卡，否则路由表会随子域 Agent 迭代而失效。
3. **六要素状态判断依赖主观**：同一问题由不同诊断 Agent 扫描，可能得到不同的「有 / 无 / 弱 / 未知」标注，导致路由结果不一致。

### 外部攻击

**[Herbert Simon，有限理性]**

> 路由表给人一种「正在做最优选择」的错觉。实际上它只是在有限信息和有限计算能力下给出一个满意解。如果用户把它当成最优解，会忽略那些未被表覆盖但可能更适合的 Agent。

**回应**：明确标注每行「置信度」和「风险提示」，并在未匹配时强制进入未来域处理流程，不让表成为唯一决策依据。

**[Karl Weick，意义建构理论]**

> 用户在对话过程中会不断重构自己的问题。一张静态路由表无法捕捉问题的涌现性。今天看起来是「创业方向模糊」，三轮对话后可能变成「个人成长导航」。

**回应**：路由表在每个回合都可被重新调用，不是一次性分诊。同时保留再诊断入口，允许子域 Agent 输出后回到诊断 Agent 校准。

**[Don Norman，情境化设计]**

> 任何分类系统都会制造错配。把「销售话术迁移到内容钩子」归到「跨域迁移」类，可能漏掉其背后真正的需求是「 brand voice 统一」或「团队培训」。

**回应**：表中「典型用户输入」只是触发线索，不是诊断结论。诊断 Agent 仍需完成六要素扫描和短板识别，再决定是否采纳推荐。

---

## Synthesis

本路由表是 [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] 运行时的工作手册之一：诊断 Agent 先调用 [[concept-yihang-dual-triangle-core]] 做六要素扫描，再查本表匹配场景，最后通过 [[tool-yitang-dual-triangle-agent-handoff-protocol]] 把上下文转交给子域 Agent。当遇到未注册域时，应使用 [[tool-yitang-dual-triangle-domain-registry]] 完成注册，而不是强行塞入已有分类。它与 [[framework-yitang-y-model-dual-triangle-synergy]] 的关系是：Y模型 提供「迭代升级基础框架认知」的发动机，路由表则是当前迭代版本中沉淀下来的一张可操作的框架性认识。

---

## Related

- [[concept-yihang-dual-triangle-core]] — 六要素官方定义与结构关系
- [[framework-yitang-y-model-dual-triangle-synergy]] — Y模型 × 双三角协同工作法
- [[tool-yihang-dual-triangle-canvas]] — 六宫格画布，扫描阶段的操作入口
- [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] — 使用本路由表的入口 Agent
- [[tool-yitang-dual-triangle-agent-handoff-protocol]] — 路由后的子域 Agent 转交协议
- [[tool-yitang-dual-triangle-domain-registry]] — 未来域接入规范
- [[method-dual-triangle-flywheel-engine]] — 项目复盘与飞轮日志方法
- [[framework-yihang-AI-native-dual-triangle-kernel]] — AI 原生组织级落地框架
