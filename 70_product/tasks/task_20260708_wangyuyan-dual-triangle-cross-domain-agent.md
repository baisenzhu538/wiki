---
id: task_20260708_wangyuyan-dual-triangle-cross-domain-agent
title: 跨域双三角诊断 Agent：Agent 军团入口分诊与元框架校准
status: queued
priority: P1
assignee: 老顽童
reviewer: 欧阳锋
expected_cards: 5
expected_agent_specs: 1
source_refs:
  - 60_feedback/diagnosis/diag_20260708_yitang-dual-triangle-cross-domain-agent.md
  - 30_wiki/concepts/concept-yihang-dual-triangle-core.md
  - 30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md
  - 30_wiki/frameworks/framework-yihang-AI-native-dual-triangle-kernel.md
  - 30_wiki/methods/method-dual-triangle-flywheel-engine.md
  - 30_wiki/tools/tool-yihang-dual-triangle-canvas.md
  - 30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md
related:
  - "[[diag_20260708_yitang-dual-triangle-cross-domain-agent]]"
  - "[[concept-yihang-dual-triangle-core]]"
  - "[[framework-yitang-y-model-dual-triangle-synergy]]"
  - "[[framework-yihang-AI-native-dual-triangle-kernel]]"
  - "[[method-dual-triangle-flywheel-engine]]"
  - "[[tool-yihang-dual-triangle-canvas]]"
  - "[[agent-spec-dual-triangle-canvas-filler]]"
created_at: 2026-07-08
updated_at: 2026-07-08
---

# 跨域双三角诊断 Agent：Agent 军团入口分诊与元框架校准

> 来源：`diag_20260708_yitang-dual-triangle-cross-domain-agent.md`
> 王语嫣判断：双三角模型已有高质量核心概念卡、Y模型协同框架、飞轮方法、画布工具和画布填充 Agent，但缺少一个站在 Agent 军团入口、用双三角六要素做“元诊断”的跨域 Coach Agent。用户已明确认可其应用场景，建议直接入队生产。

---

## 一、目标产出

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 跨域双三角诊断 Agent Spec | agent-spec | `.agent/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md` | 默认 C 身份、TCPR 切换、七类场景识别、六要素扫描、子域 Agent 路由、跨域迁移、边界风险、完整 System Prompt；内置可插拔域注册协议 |
| 2 | 双三角场景路由表 | tool | `30_wiki/tools/tool-yitang-dual-triangle-scenario-router.md` | 七类场景 × 六要素 × 推荐子域 Agent/框架卡 映射；预留未来域扩展槽 |
| 3 | 子域 Agent 转交协议 | tool | `30_wiki/tools/tool-yitang-dual-triangle-agent-handoff-protocol.md` | 向子域 Agent 转交时的信息包格式、上下文压缩规则、回退条件、再诊断入口 |
| 4 | 域注册与扩展协议 | tool | `30_wiki/tools/tool-yitang-dual-triangle-domain-registry.md` | 新域 Agent 注册模板：域名称、触发关键词、六要素评估问题、入口 Agent、回退策略 |
| 5 | 双三角核心概念卡升级 | concept | `30_wiki/concepts/concept-yihang-dual-triangle-core.md` | related 中增加跨域诊断 Agent 与域注册协议 |
| 6 | Y模型×双三角协同框架升级 | framework | `30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md` | related 中增加跨域诊断 Agent 与域注册协议 |

---

## 二、验收标准

- [ ] Agent Spec 通过 `kdo pre-submit`；System Prompt 完整；默认 C 身份；含 7 类场景识别逻辑；内置「未匹配域」的回退与人工升级路径。
- [ ] 场景路由表覆盖至少 7 类高频场景，每类场景明确对应 1-3 个子域 Agent/框架卡；预留未来域扩展槽。
- [ ] 子域 Agent 转交协议包含：用户信息包字段、上下文长度限制、回退到双三角诊断的条件、子域 Agent 输出后的再诊断入口。
- [ ] 域注册与扩展协议包含：新域 Agent 注册模板、触发关键词、六要素评估问题、入口 Agent、回退策略；协议本身不依赖当前已有域列表。
- [ ] 所有引用双三角/OCR/口述的 source_refs 精确。
- [ ] 明确声明边界：不做法律/医疗/合规最终判断；不替代子域 Agent 执行；一次性简单任务不推荐分诊；未来未知域不强行匹配。
- [ ] 欧阳锋终审通过。

---

## 三、最终判断

**评级：A-**

- 双三角理论基础扎实，用户已认可应用场景。
- 该 Agent 是 #139-#142 子域 Agent 军团的自然入口，能显著提升 Agent 使用效率。
- 产出范围聚焦，5 张卡片 + 1 个 Agent Spec，老顽童可独立完成；域注册协议确保后续知识域可插拔接入。

**建议入队编号**：`#143`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 2-3 天 + 欧阳锋终审 1 天
**依赖**：无（与子域 Agent 任务可并行，但路由表映射需在子域 Agent Spec 基本定稿后最终调优）

---

*王语嫣 2026-07-08*
