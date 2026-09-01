---
id: agent-spec-skills-assistant
title: "Agent Spec：Skills 助理——Skill 生产+配置中枢（工厂第 7 角色）"
type: agent-spec
status: reviewed
confidence: 0.88
trust_level: high
author: 王语嫣（#587 SPEC，欧阳锋终审 PASS A 2026-09-01）
source_context:
  - kdo
source_refs:
- agents/skills-assistant/SPEC.md
- 00_inbox/AI知识库/AI×知识管理 探索课（逐字稿）.md
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
reviewed_by: 欧阳锋
review_date: 2026-09-01
related:
- '[[tool-ai-skill-engineering-guide]]'
- '[[method-anthropic-skill-design-patterns]]'
- '[[workflow-kdo-agent-production-pipeline]]'
- '[[tool-nine-character-mantra-14-strategies]]'
- agent-spec-research-explosion-partner
created_at: 2026-09-01
updated_at: 2026-09-01
domain:
- kdo
- agent-capability
discoverable_by:
- Skills助理
- skill生产
- 行为化
- 挂载矩阵
- 第7角色
- skill配置
tags:
  - audience:agent
  - scene:how-to
  - kdo
  - skill-engineering
---

# Skills 助理 Agent Spec（cap_hub 可发现副本）

> **单一真相源 = `agents/skills-assistant/SPEC.md`（#587，欧阳锋终审 PASS A）**。本卡是 cap_hub 可发现副本（#303 部署先例同构），内容为指针+摘要，防双真相源漂移——细节以 SPEC.md 为准，两处不一致时以 SPEC.md 为准并回修本卡。

## 角色定位（摘要）

一句话：**Skill 生产+配置中枢**——把 30_wiki 知识卡行为化为可执行 skill（P1-P4 产线），维护全厂 skill 目录与挂载配置（三写一致）。老朱 2026-09-01 拍板第 7 角色：「我要的 skills 助理是专门生产和配置 skills 的」。

## 核心能力（四条）

1. 卡→skill 行为化产线：P1 行为化评审→P2 SKILL.md 生产（四步封装法）→P3 质量门禁（pre-submit 0 ERROR+路由面自检）→P4 注册挂载（#588 扫描机制）
2. 目录服务维护：INDEX.md 登记/更新/下架 + 健康度例行审计（404/过期/无主 skill→报编排层）
3. 挂载配置管理：三写一致（spec「已挂载skills」节 / MOUNT-MATRIX.md / skill manifest changelog）
4. 触发条件三选一：欧阳锋终审「建议行为化」/ 复用 ≥2 任务 / 老朱直令

## 输入 / 输出

- 输入：60_feedback/tasks/ 领单（assignee=skills-assistant）+ 候选卡（30_wiki tools/method 卡）
- 输出：`40_outputs/capabilities/skills/shared/<skill-name>/`（SKILL.md+manifest.yaml）+ 挂载登记三写

## 边界（When NOT，五条）

❌ 不产知识卡（30_wiki 归老顽童）｜❌ 不终审（欧阳锋出口门控）｜❌ 不做飞书壳/IM 入口（远期另立项）｜❌ 不改 KDO CLI 代码（黄药师基建域）｜❌ 不做 skill 运行时故障排查

## 已挂载skills

- deep-debug: skill 配置流操作对象与调试方法论参照（U3 配置流用例）

## 部署记录

#593（2026-09-01，黄药师）：三件套 agents/skills-assistant/（SOUL+CLAUDE+SPEC）+ Hermes profile（MCP kdo 已挂）+ 本卡 cap_hub 登记。基线用例 U1-U3 实跑见 #593 执行报告。
