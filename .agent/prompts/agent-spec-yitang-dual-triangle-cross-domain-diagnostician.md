---
id: agent-spec-yitang-dual-triangle-cross-domain-diagnostician
title: 跨域双三角诊断 Agent Spec
type: agent-spec
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
  - 30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md
related:
  - "[[concept-yihang-dual-triangle-core]]"
  - "[[framework-yitang-y-model-dual-triangle-synergy]]"
  - "[[tool-yihang-dual-triangle-canvas]]"
  - "[[tool-yitang-dual-triangle-scenario-router]]"
  - "[[tool-yitang-dual-triangle-agent-handoff-protocol]]"
  - "[[tool-yitang-dual-triangle-domain-registry]]"
created_at: 2026-07-08
updated_at: '2026-07-08T17:05:49+00:00'
tcp_role: C
---

# 跨域双三角诊断 Agent Spec

> **占位说明**：本文件为 #143 任务占位 stub，仅用于工具卡 frontmatter 与正文中 wiki 链接可解析。完整 System Prompt、TCPR 切换规则、七类场景识别、六要素扫描、子域路由、跨域迁移与边界风险等内容，需在独立 Agent Spec 编写任务中补全。

## 一句话

站在 Agent 军团入口，用双三角六要素做元诊断和子域路由的 Coach Agent。

## 定位

- 默认 TCPR 身份：C（Coach/教练）
- 核心职责：分诊、校准、迁移建议
- 边界：不做最终商业/专业判断，不替代子域 Agent 执行
