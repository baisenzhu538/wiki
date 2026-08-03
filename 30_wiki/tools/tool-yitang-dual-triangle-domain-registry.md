---
id: tool-yitang-dual-triangle-domain-registry
title: 双三角域注册与扩展协议
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
aliases:
  - 双三角域注册与扩展协议
  - 角域注册与扩展协议
related:
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
- '[[tool-yitang-dual-triangle-scenario-router]]'
- '[[tool-yitang-dual-triangle-agent-handoff-protocol]]'
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-yitang-y-model-dual-triangle-synergy]]'
- '[[tool-yihang-dual-triangle-canvas]]'
created_at: 2026-07-08
updated_at: '2026-07-08T17:05:49+00:00'
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
---

# 双三角域注册与扩展协议

> **一句话**：一个与当前已有域列表无关、可插拔的新域 Agent 注册模板，确保未来知识域能按统一协议接入双三角诊断入口。

---

## 目的

把「未来域」从例外处理变成可预期、可复用的扩展接口。任何新域 Agent 只要按本协议填写注册模板，就能被 [[tool-yitang-dual-triangle-scenario-router]] 识别、被 [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] 调用、并通过 [[tool-yitang-dual-triangle-agent-handoff-protocol]] 完成转交。协议本身不依赖当前已有域列表，因此不会因域数量增加而过时。

---

## When to Use

- 发现新的高频场景，现有路由表中无合适匹配。
- 需要为新的业务域（如法律、医疗、教育、设计）设计接入规范。
- 子域 Agent 版本升级导致触发条件或入口发生变化。
- 组织内部出现新的能力域，需要纳入 Agent 军团入口。
- 复盘时发现某类问题反复出现，值得独立成一个域。

---

## When NOT to Use

- **仅在单域内做优化**：不需要改变域的接入方式时，不必重新注册。
- **域定义尚不清晰**：如果连域名称、触发关键词、评估问题都无法稳定描述，强行注册只会增加噪音。
- **为一次性活动创建域**：临时活动不需要进入路由表，直接走通用流程即可。
- **绕过现有诊断流程**：注册不是为了让某个域跳过六要素扫描，而是为了让它被正确扫描后接入。

---

## 操作步骤

1. **提出注册申请**：由域 Agent 设计者或维护者填写注册模板。
2. **定义域名称与 ID**：使用 `agent-spec-<域>-<角色>` 或 `tool-<域>-<功能>` 的命名规范。
3. **编写触发关键词**：列出用户输入中高频出现、且能区分于其他域的 5–10 个关键词或短语。
4. **设计六要素评估问题**：为审美、体系、创造力、场景、数据、基本功各写 1–2 个诊断问题。
5. **指定入口 Agent 与回退策略**：明确用户进入本域后由哪个 Agent 接待，以及什么情况下应回退到诊断 Agent。
6. **审核与冻结**：由 欧阳锋 或指定架构审核人批准后，模板状态从 `draft` 转为 `registered`。
7. **接入路由表与转交协议**：审核通过后，由路由表维护者把新域加入 [[tool-yitang-dual-triangle-scenario-router]]，并更新 [[tool-yitang-dual-triangle-agent-handoff-protocol]] 的信息包字段说明。

---

## 示例/模板

### 新域 Agent 注册模板

```yaml
# 域注册模板（双三角域注册与扩展协议 v1.0）
domain_id: <唯一标识，如 legal-contract-review>
domain_name: <人类可读的域名称，如 法律合同审查>
status: draft          # draft / registered / deprecated
created_at: 2026-07-08
updated_at: 2026-07-08

# 1. 域定位
domain_purpose: |
  一句话说明本域解决什么问题、为谁服务、与相邻域的区别。

# 2. 触发关键词（用户输入中高频出现的信号）
trigger_keywords:
  - "关键词 1"
  - "关键词 2"
  - "短语示例"

# 3. 六要素评估问题（用于诊断 Agent 扫描阶段）
six_element_questions:
  审美: "本域中『好结果』的行业标准是什么？用户是否具备判断能力？"
  体系: "本域是否有成熟的标准流程或合规要求？"
  创造力: "本域内有哪些被默认接受但可以被挑战的隐含假设？"
  场景: "AI 在本域哪个细分环节最能创造价值，同时风险可控？"
  数据: "本域有哪些可复用的正负案例、法规条文、Domain Knowledge？"
  基本功: "本域需要哪些 AI 工具或技术特性才能落地？"

# 4. 入口 Agent
entry_agent:
  id: <agent-spec-xxx 或 tool-xxx>
  path: <文件路径>
  description: "进入本域后第一个被调用的 Agent"

# 5. 回退策略
fallback_strategy:
  when:
    - "用户问题超出本域边界"
    - "用户需要跨域迁移判断"
    - "子域 Agent 无法处理当前输入"
  to: "agent-spec-yitang-dual-triangle-cross-domain-diagnostician"
  message: "当前问题需要回到跨域诊断 Agent 重新分诊。"

# 6. 边界声明
boundary:
  - "不做最终法律/医疗/合规判断"
  - "不替代持证专业人员"
  - "输出需经人工确认后方可执行"

# 7. 相关卡片
related:
  - "[[concept-yihang-dual-triangle-core]]"
  - "[[tool-yitang-dual-triangle-scenario-router]]"
  - "[[tool-yitang-dual-triangle-agent-handoff-protocol]]"
```

### 已注册域状态流转

| 状态 | 含义 | 谁可以操作 |
|:---|:---|:---|
| `draft` | 模板已填写，待审核 | 域设计者 |
| `registered` | 审核通过，已接入路由表 | 架构审核人 |
| `deprecated` | 域已下线或合并，不再接收新流量 | 架构审核人 |
| `future` | 仅作为占位，触发条件尚不明确 | 诊断 Agent 自动标记 |

---

## Critique

### 内部局限

1. **协议不保证域质量**：模板再完整，也挡不住一个设计糟糕的子域 Agent 被注册。协议只是接口标准，不是能力标准。
2. **审核瓶颈**：所有注册都需要人工审核，当域数量快速增长时，审核队列可能成为阻塞点。
3. **六要素评估问题的普适性有限**：某些专业域（如医疗影像）的评估问题可能无法被通用用户理解，需要领域专家参与翻译。

### 外部攻击

**[Clayton Christensen，创新者窘境]**

> 一个正式的域注册协议会让组织倾向于服务已有主流域，而忽视那些刚开始很小、但未来可能颠覆主流程的新兴域。未来域扩展槽如果审核太严，会变成创新的阻力。

**回应**：协议保留 `future` 状态，允许诊断 Agent 自动标记未注册域并给出临时建议，而不必等待完整注册流程。

**[Melvin Conway，康威定律]**

> 任何组织设计的系统，其架构都反映组织的沟通结构。你的域注册协议看起来中立，但审核权集中在架构审核人手中，最终路由表会偏向审核人熟悉的域。

**回应**：协议要求每个新域必须包含「与相邻域的区别」和「触发关键词」，让审核标准显性化；同时保留社区反馈路径，允许用户通过失败案例提出重新分类。

**[Elinor Ostrom，公共池塘资源]**

> 当多个 Agent/域共享同一个入口时，容易出现「公地悲剧」——每个域都想扩大自己的触发范围，导致路由边界模糊、用户被错误分类。

**回应**：协议要求每个域明确写出「不处理的场景」和「回退条件」，并在审核时检查触发关键词与其他域的重叠度，避免边界侵蚀。

---

## Synthesis

本协议是双三角 Agent 军团的「扩展插槽标准」。它与 [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]、[[tool-yitang-dual-triangle-scenario-router]]、[[tool-yitang-dual-triangle-agent-handoff-protocol]] 形成闭环：诊断 Agent 扫描问题，路由表匹配已知域，未匹配时标记为未来域并提示用户按本协议注册，注册完成后通过转交协议接入。协议的设计原则来自 [[framework-yitang-y-model-dual-triangle-synergy]] 的迭代发动机思想——域列表会不断演进，但接入协议保持稳定，使框架性认识（协议）与具体域（内容）解耦。

---

## Related

- [[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]] — 使用本协议识别未来域的入口 Agent
- [[tool-yitang-dual-triangle-scenario-router]] — 注册完成后接入的目标路由表
- [[tool-yitang-dual-triangle-agent-handoff-protocol]] — 注册域的转交接口标准
- [[concept-yihang-dual-triangle-core]] — 六要素评估问题的理论来源
- [[framework-yitang-y-model-dual-triangle-synergy]] — 协议稳定、域列表迭代的解耦思想
- [[tool-yihang-dual-triangle-canvas]] — 域注册前做六要素扫描的工具入口
