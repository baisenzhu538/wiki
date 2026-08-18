---
id: tool-ai-agent-feature-comparison
title: 「AI Agent 工具对比：Claude Code / Hermes / Codex / CodeBuddy 的 Feature 差异」
type: tool
status: draft
domain:
- ai-basic
- ai-collaboration
author: 老朱（一手体感）/ CodeBuddy（整理）
source_person: 老朱
source_context: 2026-08-08 对话——老朱一手使用体感 + Claude Code 交叉自评 + CodeBuddy 整理
source_refs:
- 00_inbox/AI基本功/给王语嫣的任务编排建议书-深度使用版.md
- 30_wiki/tools/agent-spec-basic-skills-coach.md
- 30_wiki/tools/tool-ai-feature-inventory.md
- 30_wiki/tools/agent-spec-codex-teammate.md
confidence: 0.85
trust_level: high
reviewed_by: 待审
aliases:
- Agent工具对比
- Claude Code对比
- Codex对比
- Hermes对比
- CodeBuddy对比
- 四工具Feature
discoverable_by:
- Agent工具对比
- Claude Code
- Codex
- Hermes
- CodeBuddy
- 瑞士军刀
- 马拉松选手
related:
- agent-spec-basic-skills-coach
- tool-ai-feature-inventory
- agent-spec-codex-teammate
- framework-truman-feature-thinking-core
- bridge-dual-track-feature-system
tags:
- method:tool-comparison
- scene:tool-selection
- audience:general
- skill-level:intermediate
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
- actionable
diagnostic_signals:
- signal: 用户问'用哪个 AI 工具 / Claude 还是 Codex？'
  severity: medium
  implication: 工具思维征兆——先对齐 Feature 差异，再选工具（课程：工具背后是 Feature）
- signal: 用户困惑'为什么这个工具在某类任务上表现不好'
  severity: low
  implication: 每个工具各有 Feature 强项和边界——匹配任务类型比换工具更重要
---

> **定位**：属于 [[framework-truman-feature-thinking-core]] 的应用层——用 Feature 四要素拆解四个主流 AI Agent 工具的能力边界，供工具选型时"点菜式"匹配。完整框架是"先问 Feature 需求，再选工具"，本卡是选型对照表。

# AI Agent 工具 Feature 对比

> 一句话：**Claude Code 是瑞士军刀（Feature 最全但需会组合）、Hermes 是工厂传送带（7×24 值守）、Codex 是马拉松选手（云端长跑不占本地）、CodeBuddy 是贴身秘书（最懂人且嵌研发流程）。**

---

## 一、四工具定位（一句话版）

| 工具 | 比喻 | 核心定位 |
|:--|:--|:--|
| **Claude Code** | 瑞士军刀 | Feature 最全，但你需要知道怎么组合 |
| **Hermes** | 工厂传送带 | 唯一能 7×24 跑在飞书上的，多 bot 同时在线 |
| **Codex** | 马拉松选手 | 云端跑长任务，不占你电脑，睡一觉回来干完了 |
| **CodeBuddy** | 贴身秘书 | 最懂你，嵌在你的研发流程里——Issue/PR/CI 就是它的记忆，不需要你喂上下文 |

## 二、双视角 Feature 差异（用户体感 × Claude 交叉自评）

| Feature 维度 | **Claude Code** | **Hermes** | **Codex** | **CodeBuddy** |
|:--|:--|:--|:--|:--|
| **编排能力**（拆任务/定流程/想清楚怎么做） | ★★★★☆ 最会编排 | ★★☆☆☆ 按配置执行 | ★★☆☆☆ 编排不行 | ★★★★☆ 懂人、会排 |
| **执行能力**（代码/内容落地） | ★★☆☆☆ 干活一般 | ★★★☆☆ 稳定但不会思考 | ★★★★★ 很会干活 | ★★★★☆ 干活 + 电脑结合好 |
| **7×24 值守** | ✗ 本地 CLI | ✓ 唯一常驻 bot | ✗ 云端任务但需触发 | ✗ 本地 CLI |
| **多 bot / 多 Agent** | 子代理 | 多 bot 并行（老顽童/洪七公/段王爷） | 子 Agent 自检 + 多线程 | Team/Agent 工具 |
| **长任务（不占本地）** | ✗ | ✗ | ✓ 云端长跑 | ✗ |
| **研发流程嵌入**（Issue/PR/CI 记忆） | 一般 | ✗ | ✓ | ✓✓ 最强，不用喂上下文 |
| **了解用户/记忆** | 一般 | ✗ | 一般 | ★★★★★ 最懂人 |
| **Skill 生态** | ★★★★★ 最成熟（marketplace） | ✗ | ★★★★（官方插件+第三方） | ★★★（plugins/skills） |

## 三、实战匹配建议（什么时候用哪个）

| 任务类型 | 首选 | 理由 |
|:--|:--|:--|
| 需要先想清楚怎么做、拆解规划 | **Claude Code** | 编排最强 |
| 明确的长代码任务、跑一夜 | **Codex** | 云端长跑、执行强 |
| 需要常驻值守、飞书自动响应 | **Hermes** | 唯一 7×24 |
| 涉及自己的研发流程（Issue/PR/CI） | **CodeBuddy** | 嵌在流程里，无需喂上下文 |
| 需要理解用户偏好、贴身协作 | **CodeBuddy** | 最懂人 |
| 需要全面能力但自己知道怎么组合 | **Claude Code** | Feature 最全 |

## 四、关键结论

1. **编排 ≠ Feature 数量**：Claude 功能最全但编排是"需要人告诉它怎么组合"；Codex 执行强但编排弱——两者不矛盾。
2. **Hermes 是唯一具备 L5 硅基组织形态的**（常驻服务 + 多 bot + 密钥池），其他三个是本地/云 CLI。
3. **CodeBuddy 的差异化 Feature 是"懂人 + 嵌流程"**：记忆来自研发流程而非人工喂上下文——这是它和 Claude/Codex 的本质区别。
4. **共同短板（都缺的 Feature）**：都没有 KDO 知识库直连消费协议——"点菜式"从周期表提 Feature 的能力。谁跑通谁获得差异化（见 AI基本功教练 #252 试点）。

## 五、失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| 工具思维选型 | 问"Claude 还是 Codex"，不问"这个任务需要什么 Feature" | 先列任务 Feature 需求，再匹配工具 |
| 单一工具依赖 | 把所有任务压在一个工具上，任务类型不匹配时抱怨"工具不行" | 按任务类型切换工具（§三） |
| 只看书面定位 | 拿文档角色定位选型，忽略实际体感差异 | 以实战体感为准（用户体感 > 文档） |

## 六、Critique

**[工具最大主义者]**
> "四个工具换来换去太累，选一个最好的不就行了？"

**回应**：没有"最好的工具"——每个工具在特定 Feature 上是强项。Swiss army knife 也不可能取代传送带。真正的效率来自**按任务类型匹配工具**，而不是押注单一工具。

**[效率派]**
> "搞这么细的对比，不如直接上手用。"

**回应**：本卡的价值正是帮你快速上手时选对方向——避免"在 Hermes 上试长任务、在 Codex 上试值守"这类不匹配。先看 Feature 边界，再动手。

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:--|:--|
| 要选工具跑新任务 | 先列出任务的 Feature 需求（值守/长跑/编排/懂人/嵌流程），再查 §三 |
| 某个工具在某类任务上表现差 | 查 §二确认是不是 Feature 不匹配——换工具而不是怪工具 |
| 用户问"哪个 AI 工具好" | 反问任务类型 + Feature 需求，再给匹配建议（不要直接推荐） |

*老朱一手体感 + Claude Code 交叉自评 · 2026-08-08 · CodeBuddy 整理*
