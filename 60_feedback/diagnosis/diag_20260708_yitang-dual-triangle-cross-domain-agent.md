---
id: diag_20260708_yitang-dual-triangle-cross-domain-agent
title: 跨域双三角诊断 Agent 场景诊断与入队建议
type: diagnosis
status: active
source: 30_wiki 双三角核心卡族 + Y模型跨域融合诊断
source_refs:
  - 30_wiki/concepts/concept-yihang-dual-triangle-core.md
  - 30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md
  - 30_wiki/frameworks/framework-yihang-AI-native-dual-triangle-kernel.md
  - 30_wiki/methods/method-dual-triangle-flywheel-engine.md
  - 30_wiki/tools/tool-yihang-dual-triangle-canvas.md
  - 30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md
  - 60_feedback/diagnosis/diag_20260708_yitang-y-model-cross-domain-fusion-deep-dive-v2.md
reviewer: 欧阳锋
created_at: 2026-07-08
updated_at: 2026-07-08
related:
  - "[[concept-yihang-dual-triangle-core]]"
  - "[[framework-yitang-y-model-dual-triangle-synergy]]"
  - "[[framework-yihang-AI-native-dual-triangle-kernel]]"
  - "[[method-dual-triangle-flywheel-engine]]"
  - "[[tool-yihang-dual-triangle-canvas]]"
  - "[[agent-spec-dual-triangle-canvas-filler]]"
  - "[[diag_20260708_yitang-y-model-cross-domain-fusion-deep-dive-v2]]"
---

# 跨域双三角诊断 Agent 场景诊断与入队建议

## 执行摘要

双三角模型已有高质量核心概念卡、Y模型协同框架、飞轮方法、画布工具和画布填充 Agent。当前缺口是：**缺少一个站在 Agent 军团入口、用双三角六要素做“元诊断”的跨域 Coach Agent**。该 Agent 不替代子域 Agent（需求分析、五步法、销售、时间管理、产品内核等），而是帮用户判断“当前问题卡在六要素的哪个角”“应该进入哪个子域 Agent”“是否需要跨域迁移”。

用户已认可该 Agent 的应用场景，建议直接入队 #143，P1 优先级，预计产出 1 张 Agent Spec + 1 张场景映射工具卡 + 1 张子域 Agent 调用协议卡。

---

## 一、现有覆盖度

| 类型 | 代表卡 | 状态 | 作用 |
|---|---|---|---|
| concept | `concept-yihang-dual-triangle-core` | draft | 双三角六要素、飞轮、暗知识 |
| framework | `framework-yitang-y-model-dual-triangle-synergy` | reviewed | Y模型 如何驱动双三角生成 |
| framework | `framework-yihang-AI-native-dual-triangle-kernel` | reviewed | AI 原生是结果，双三角是引擎 |
| method | `method-dual-triangle-flywheel-engine` | draft | 三回路飞轮与制度化运行 |
| tool | `tool-yihang-dual-triangle-canvas` | draft | 六宫格画布三版合一 |
| agent-spec | `agent-spec-dual-triangle-canvas-filler` | draft | 画布填充 Agent |

**缺口**：没有一张 `.agent/prompts/` 下的跨域诊断/路由 Agent Spec。

---

## 二、目标应用场景（已获用户认可）

| # | 场景 | 典型输入 | Agent 输出 |
|---|---|---|---|
| 1 | 创业/业务方向模糊 | “我想做一款 AI 工具帮律师审合同，靠谱吗？” | 双三角六要素扫描 + 最短板识别 + 推荐子域 Agent |
| 2 | 子域 Agent 输出质量不稳定 | “需求分析 Agent 给的需求总感觉很虚。” | 诊断是人的输入问题还是 Agent 配置问题 + 改进行动 |
| 3 | 跨域迁移 | “销售前三秒话术能不能用到内容钩子设计？” | 抽象源域模式 + 目标域映射 + 迁移假设与风险 |
| 4 | 组织级 AI 落地前全局诊断 | “公司想全面拥抱 AI，先从哪块业务切入？” | 各业务线六要素扫描 + 优先级矩阵 + 小切口建议 |
| 5 | 个人 AI 协作成长导航 | “学了很多 AI 工具，越学越乱。” | 六要素现状诊断 + 下一步成长路径 |
| 6 | 复盘失败项目 | “上一个 AI 项目三个月没跑通，问题在哪？” | 六要素缺口定位 + 下一轮优先补的 1-2 个要素 |
| 7 | 判断 Agent/工具是否值得投入 | “这个新的 AI coding 工具我们要不要接？” | 六要素 readiness 评估 + 建议 |

---

## 三、跨域双三角诊断 Agent 设计

### 3.1 定位

- **名称**：`agent-spec-yitang-dual-triangle-cross-domain-diagnostician`
- **一句话**：站在 Agent 军团入口，用双三角六要素做元诊断和子域路由的 Coach。
- **边界**：不做最终商业/专业判断，不替代子域 Agent 执行，只负责分诊、校准、迁移建议。

### 3.2 TCPR 身份

- **默认身份**：C（Coach/教练）——帮用户定位问题。
- **切换规则**：
  - 用户问“某个要素怎么做” → T（Teacher）
  - 用户要一起填画布/拆业务 → P（Partner）
  - 用户有数据要诊断 → R（Researcher）
  - 用户想直接跳到子域方案 → C→T，先用双三角纠偏

### 3.3 工作流

1. **边界确认**：声明只做元诊断和路由。
2. **问题重述**：把用户模糊问题转写为可分析的命题。
3. **六要素快速扫描**：判断每个要素的“有/无/弱/未知”。
4. **短板识别**：找出当前最大瓶颈（通常 1-2 个）。
5. **子域匹配**：根据短板推荐子域 Agent/框架卡；若无法匹配已知域，标记为「未来域」并给出临时处理建议。
6. **跨域迁移判断**：如果用户想跨域迁移，输出映射与风险。
7. **输出行动清单**：下一步最小动作 + 成功指标 + 风险提示；若涉及未注册域，提示用户补充域注册信息。

### 3.4 调用卡与转交 Agent

- `concept-yihang-dual-triangle-core`
- `framework-yitang-y-model-dual-triangle-synergy`
- `tool-yihang-dual-triangle-canvas`
- `agent-spec-dual-triangle-canvas-filler`
- 子域 Agent：`agent-spec-demand-iceberg-coach`、`agent-一堂五步法教练`、`agent-personal-time-management-coach` 等

### 3.5 边界风险

1. 一次性简单任务直接拒绝分诊，推荐通用 Agent。
2. 不替用户做法律/医疗/合规最终判断。
3. 不把六要素机械一一对应到 Y模型/实事求是/解放思想。
4. 跨域迁移时明确列出 source 与 target 的关键差异。
5. 子域 Agent 输出质量差时，先诊断输入质量再怪 Agent。
6. 遇到未注册的未来知识域，不强行匹配，而是标记为「待注册域」并给出临时处理建议。

---

## 四、建议新建 / 升级清单

| # | id | 类型 | 优先级 | 说明 |
|---|---|---|---|---|
| 1 | `agent-spec-yitang-dual-triangle-cross-domain-diagnostician` | agent-spec | P0 | 跨域双三角诊断 Agent Spec；内置可插拔域注册协议 |
| 2 | `tool-yitang-dual-triangle-scenario-router` | tool | P1 | 七类场景 × 六要素 × 子域 Agent 映射表；预留未来域扩展槽 |
| 3 | `tool-yitang-dual-triangle-agent-handoff-protocol` | tool | P1 | 向子域 Agent 转交时的信息包格式、上下文压缩、回退与再诊断规则 |
| 4 | `tool-yitang-dual-triangle-domain-registry` | tool | P1 | 新域 Agent 注册模板：域名称、触发关键词、六要素评估问题、入口 Agent、回退策略 |
| 5 | `concept-yihang-dual-triangle-core` | concept | P2 | related 中增加跨域诊断 Agent 与域注册协议 |
| 6 | `framework-yitang-y-model-dual-triangle-synergy` | framework | P2 | related 中增加跨域诊断 Agent 与域注册协议 |

---

## 五、最终判断

**评级：A-**

- 双三角核心卡族质量高，理论基础扎实。
- 用户已明确认可应用场景，需求真实。
- 该 Agent 是 #139-#142 子域 Agent 军团的自然入口，能显著提升 Agent 使用效率。

**建议入队编号**：`#143`
**任务名称**：`task_20260708_wangyuyan-dual-triangle-cross-domain-agent`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：1 Agent Spec + 3 工具卡 + 2 张现有卡 related 更新
**依赖**：无（与子域 Agent 任务可并行，但建议在子域 Agent Spec 定稿后调优路由映射；域注册协议确保未来知识域可插拔接入）

---

*王语嫣 2026-07-08*
