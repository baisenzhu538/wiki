---
id: workflow-kdo-agent-production-pipeline
title: "KDO Agent 生产流水线：spec → 三件套注入 → Agent 自举"
type: workflow
status: draft
domain:
  - kdo
  - ai-basic
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-09
confidence: 0.90
trust_level: observed
source_refs:
  - 30_wiki/tools/agent-spec-basic-skills-coach.md
  - 30_wiki/dark-knowledges/dk-agent-access-kdo-pitfalls.md
  - agents/agent-basic-skills-coach/
created_at: 2026-08-09
updated_at: 2026-08-09
tags:
  - audience:huangyaoshi
  - audience:laowantong
  - audience:wangyuyan
  - scene:reference
  - skill-level:advanced
aliases:
  - Agent生产流水线
  - Agent自举
  - Agent三件套
discoverable_by:
  - Agent生产流水线
  - Agent自举
  - 三件套
diagnostic_signals:
  - signal: '新 Agent 上线没有标准化流程——每次都是黄药师手配，配置质量参差不齐'
    severity: high
    implication: '王语嫣/洪七公/段王爷的 SOUL.md 缺 KDO 知识地图——教练试出来的缺口，全厂都有'
  - signal: 'Agent 能力边界 = spec + 三件套——缺任一件则 Agent 无法自举'
    severity: high
    implication: 'spec 定义"做什么"，三件套定义"怎么在 KDO 里做"——两件不缺才能自举'
related:
  - '[[agent-spec-basic-skills-coach]]'
  - '[[dk-agent-access-kdo-pitfalls]]'
  - '[[concept-kdo-feature-registry]]'
  - '[[system-kdo-quality-framework]]'
  - '[[kdo-moc]]'
  - '[[workflow-cross-agent-fact-dispute]]'
---

# KDO Agent 生产流水线

> **定位**：将新 Agent 从 spec 到可自举的标准流程。教练（basic-skills-coach）是第一个跑通全链路的 Agent——此流水线将其模式固化为可复用的生产标准。

## 使用场景

- 王语嫣完成新 Agent 的编排（spec 定义）
- 老顽童完成 agent-spec 卡的生产
- 黄药师收到 #部署任务

## 操作步骤

### 流水线三步

### Step 1：老顽童 —— 写 agent-spec 卡

产出 `30_wiki/tools/agent-spec-<name>.md`，最小字段：

```yaml
id: agent-spec-<name>
title: "Agent 名称"
type: agent-spec
domain: [<领域>, agent-capability]
author: 老顽童
```

spec 只需定义：角色身份（TCPR）+ 核心能力 + 输入输出格式。不需要写"怎么在 KDO 里操作"——那是三件套的事。

### Step 2：黄药师 —— 注入三件套

| 件 | 内容 | 注入位置 | 作用 |
|:--|:--|:--|:--|
| 认知件 | KDO 知识地图（5 MOC + AI基本功域） | SOUL.md | Agent 知道 KDO 是什么、知识在哪 |
| 路径件 | 终端 + 检索规则 | config.yaml + SOUL.md | Agent 能查 MOC、grep wiki、点菜 |
| 部署件 | agents/ 目录 + Hermes profile | agents/<name>/ + .hermes/profiles/<name>/ | Agent 有家、有运行时 |

三件套模板（直接复用）：
- 认知件：见 `agents/agent-basic-skills-coach/system-prompt.md` 的"KDO 知识库接入"段
- 路径件：`terminal.cwd + persistent_shell + toolsets: [terminal, web]`
- 部署件：CLAUDE.md + SOUL.md + config.yaml 最小配置

### Step 3：Agent 自举 —— 自己做剩下的

三件套注入后，Agent 应该能够自主完成：

1. **自我定位**：查 MOC → 确认自己的领域在 KDO 的什么位置
2. **探索环境**：查 kdo-moc → 了解工厂有什么工具、有什么坑
3. **踩坑沉淀**：遇到问题 → 查坑库（E 系列 dk）→ 找不到 → 建新坑卡 → 注册 MOC
4. **建立复盘**：按 Truman 10 章格式建自己的复盘体系
5. **迭代 spec**：基于实测反馈更新自己的 agent-spec

**自举成功的标志**：Agent 能在不被提示的情况下，完成"发现问题→查 KDO→建卡→注册→复盘"全链路。教练首次自举耗时 2 轮对话。

## 适用边界

- 适用于 KDO 体系内新建 Agent（有 agent-spec + 三件套标准）
- 不适用于外部第三方 Agent（无 KDO MOC 导航）
- Agent 自举的前提：MOC 覆盖率足够 + 终端权限开通 + spec 定义清晰
- 第一个跑通的 Agent（教练）样本量为 1——第二个 Agent 上线时会验证可复制性

## 为什么值钱

1. **Agent 生产成本从"手配半天"降到"注入三件套 5 分钟"**——黄药师不需要为每个 Agent 写定制 prompt
2. **Agent 质量上限从"黄药师能想到的"变成"Agent 自己能探索的"**——教练自己查到 MOC、自己建 dk 卡、自己建复盘体系，这些黄药师没教过
3. **可复制**：三件套是模板——下一个 Agent（如复盘教练 #246）只需换 spec，三件套原样注入

## 与其他知识的关联

- agent-spec-basic-skills-coach → 第一个跑通全链路的 Agent 注册卡
- dk-agent-access-kdo-pitfalls → Agent 自举过程中踩的坑——已沉淀为 dk 卡
- concept-kdo-feature-registry → Agent 的武器库——13 个 Feature 是 Agent 了解 KDO 能力的入口
- kdo-moc → Agent 的导航地图——自举第一步就是查这个

## 验收标准

1. Agent 在飞书/CLI 端能响应"你知道 KDO 吗？"→ 命中 MOC 导航
2. Agent 能自主调用 `kdo feature` / `grep` 检索 KDO 知识库
3. Agent 首次踩坑后能自主建 dk 卡并注册 MOC（不需要黄药师手配）
4. Agent 建立自己的复盘目录（`agent复盘/<name>/`）

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 缺认知件 | Agent 说"我不知道 KDO 是什么" | 补 SOUL.md 知识地图段 |
| 缺路径件 | Agent 所有命令 BLOCKED | 查 approvals.mode + cwd 路径格式 |
| 认知件过时 | Agent 查不到新 MOC | 更新 SOUL.md 的知识地图清单 |
| 三件套不全 | Agent 能对话但不能检索 | 查 toolsets 是否含 terminal |

## 与卡片生产流水线的对比

| | 卡片生产 | Agent 生产 |
|:--|:--|:--|
| 谁产骨架 | 老顽童 | 老顽童（agent-spec） |
| 谁注入基建 | 黄药师（lint/门禁） | 黄药师（三件套） |
| 谁 enrich | 老顽童 | **Agent 自己** |
| 谁审查 | 欧阳锋 | 欧阳锋（spec 审查）+ Agent 实测 |

## 已跑通的 Agent

| Agent | spec | 三件套 | 自举 |
|:--|:--|:--|:--|
| 基本功教练 | ✅ | ✅ | ✅ 建 dk 卡 + 注册 MOC + 建复盘体系 |
| 王语嫣 | ❌ 无 Hermes spec | ✅ 刚补认知件 | ⏳ 待验证 |
| 洪七公 | ❌ | ✅ 刚补认知件 | ⏳ |
| 段王爷 | ❌ | ✅ 刚补认知件 | ⏳ |
| 欧阳锋 | ❌ | ✅ 刚补认知件 | ⏳ |

## Critique

### 内部局限
- 教练是第一个验证品——样本量为 1，"可复制"尚未在第二个 Agent 上验证
- 自举质量取决于 MOC 的完整度——如果 MOC 覆盖不全，Agent 探索效率下降
- 三件套的"认知件"需要随 KDO 演进同步更新——MOC 清单是静态快照

### 外部挑战
- "Agent 自举 = 不需要人了？"——不是。spec 的方向定义和审查仍然需要欧阳锋/王语嫣。Agent 自举的是执行层，不是决策层
- "三件套是天花板吗？"——当前三件套只覆盖检索+终端。未来可扩展：MCP 桥（Agent 调 kdo_search）、自动入队（Agent 产出→王语嫣编排）
