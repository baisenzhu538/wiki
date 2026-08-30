---
id: tool-ai-agent-feature-comparison
title: 「AI Agent 工具对比：Claude Code / Hermes / Codex / CodeBuddy / OpenClaw / DeepSeek Harness 的 Feature 差异」
type: tool
status: pending_review
domain:
- ai-basic
- ai-collaboration
author: 老朱（一手体感）/ 黄药师（补全 OpenClaw + DeepSeek Harness 两列）
source_person: 老朱
source_context: 2026-08-08 对话（四工具一手体感）+ 2026-08-30 战略笃定篇口述（OpenClaw/Harness + 三分法，王语嫣编排 #576 补全）
source_refs:
- 00_inbox/AI基本功/给王语嫣的任务编排建议书-深度使用版.md
- 30_wiki/tools/agent-spec-basic-skills-coach.md
- 30_wiki/tools/tool-ai-feature-inventory.md
- 30_wiki/tools/agent-spec-codex-teammate.md
- 00_inbox/我用一堂做一堂/战略笃定-一堂AI转型复盘-口述.txt
confidence: 0.85
trust_level: high
reviewed_by: 待审
aliases:
- Agent工具对比
- Claude Code对比
- Codex对比
- Hermes对比
- CodeBuddy对比
- OpenClaw对比
- DeepSeek Harness对比
- 六工具Feature
- 三分法选型
discoverable_by:
- Agent工具对比
- Claude Code
- Codex
- Hermes
- CodeBuddy
- OpenClaw
- 龙虾
- DeepSeek Harness
- Harness
- 三分法
- 养员工
- 造工具
- 打短工
- 瑞士军刀
- 马拉松选手
related:
- agent-spec-basic-skills-coach
- tool-ai-feature-inventory
- agent-spec-codex-teammate
- framework-truman-feature-thinking-core
- bridge-dual-track-feature-system
- framework-openclaw-vs-harness-selection
tags:
- method:tool-comparison
- scene:tool-selection
- audience:general
- skill-level:intermediate
created_at: 2026-08-08
updated_at: 2026-08-30
quality_labels:
- actionable
diagnostic_signals:
- signal: 用户问'用哪个 AI 工具 / Claude 还是 Codex？'
  severity: medium
  implication: 工具思维征兆——先对齐 Feature 差异，再选工具（课程：工具背后是 Feature）
- signal: 用户困惑'为什么这个工具在某类任务上表现不好'
  severity: low
  implication: 每个工具各有 Feature 强项和边界——匹配任务类型比换工具更重要
- signal: 用户问'什么情况用 OpenClaw / 什么情况用 Harness'
  severity: medium
  implication: 先过三分法（养员工/造工具/打短工），再看本卡逐工具 Feature 明细——与选型决策树卡互补
---

> **定位**：属于 [[framework-truman-feature-thinking-core]] 的应用层——用 Feature 四要素拆解六个主流 AI Agent 工具的能力边界，供工具选型时"点菜式"匹配。完整框架是"先问 Feature 需求，再选工具"，本卡是选型对照表。选型决策视角（三分法决策树 + 触发场景 + 反例）见配套卡 `framework-openclaw-vs-harness-selection`，本卡专注**逐工具 Feature 明细**。

# AI Agent 工具 Feature 对比

> 一句话：**Claude Code 是瑞士军刀（Feature 最全但需会组合）、Hermes 是工厂传送带（7×24 值守）、Codex 是马拉松选手（云端长跑不占本地）、CodeBuddy 是贴身秘书（最懂人且嵌研发流程）、OpenClaw 是养成的员工（长期记忆+角色身份+主动汇报）、DeepSeek Harness 是自建工作台（组件化"Everything is a Plugin"）。**

---

## 一、三分法总纲（选型第一问：养员工 / 造工具 / 打短工）

> 来源：2026-08-30 战略笃定篇口述（L1376-1392）——Truman 把六工具按"用它做什么"归三类，比逐个比 Feature 更快定位。

| 三分法 | 隐喻 | 特征 | 工具 |
|:--|:--|:--|:--|
| **项目制** | 打短工 | 一次性 Session，做完就关，无长期记忆/角色/进化 | Codex / Claude Code（CodeBuddy 属此类，但带研发流程记忆） |
| **Agent 级** | 养员工 | 长期记忆 + 角色身份 + 主动汇报 + 陪伴进化 | **OpenClaw** / **Hermes** |
| **工作台** | 造工具 | 组件化 + 插件可改 + 跨平台 + 多机部署 | **DeepSeek Harness** |

**判断口诀**：任务做完就结束、下次从零开始 → 打短工；要长期记住你、当人养、主动找你 → 养员工；要定制一套自己的 Agent 工作台、多机部署 → 造工具。

---

## 二、六工具定位（一句话版）

| 工具 | 比喻 | 核心定位 |
|:--|:--|:--|
| **Claude Code** | 瑞士军刀 | Feature 最全，但你需要知道怎么组合 |
| **Hermes** | 工厂传送带 | 唯一能 7×24 跑在飞书上的，多 bot 同时在线 |
| **Codex** | 马拉松选手 | 云端跑长任务，不占你电脑，睡一觉回来干完了 |
| **CodeBuddy** | 贴身秘书 | 最懂你，嵌在你的研发流程里——Issue/PR/CI 就是它的记忆，不需要你喂上下文 |
| **OpenClaw** | 养成的员工 | 长期记忆 + 角色身份（真人名/岗位/边界）+ 主动汇报，像养一个会进化的员工 |
| **DeepSeek Harness** | 自建工作台 | 组件化到"官方都组件化"，插件可改，造你自己的 Agent 工作台 |

## 三、双视角 Feature 差异（用户体感 × 口述交叉印证）

| Feature 维度 | **Claude Code** | **Hermes** | **Codex** | **CodeBuddy** | **OpenClaw** | **DeepSeek Harness** |
|:--|:--|:--|:--|:--|:--|:--|
| **编排能力**（拆任务/定流程/想清楚怎么做） | ★★★★☆ 最会编排 | ★★☆☆☆ 按配置执行 | ★★☆☆☆ 编排不行 | ★★★★☆ 懂人、会排 | ★★★★☆ 主动调度（写任务书分发） | ★★★☆☆ 组件编排需自己搭 |
| **执行能力**（代码/内容落地） | ★★☆☆☆ 干活一般 | ★★★☆☆ 稳定但不会思考 | ★★★★★ 很会干活 | ★★★★☆ 干活 + 电脑结合好 | ★★★☆☆ 靠调度的研究员 | ★★★★☆ 组件化插件执行 |
| **7×24 值守** | ✗ 本地 CLI | ✓ 唯一常驻 bot | ✗ 云端任务但需触发 | ✗ 本地 CLI | ✓ 常驻 + 主动心跳汇报 | ✓ 常驻工作台 |
| **多 bot / 多 Agent** | 子代理 | 多 bot 并行（老顽童/洪七公/段王爷） | 子 Agent 自检 + 多线程 | Team/Agent 工具 | ✓✓ 角色团队（一龙虾钓几个 Hermes） | ✓ 多机多 Agent |
| **长任务（不占本地）** | ✗ | ✗ | ✓ 云端长跑 | ✗ | ✗ | △ 多机部署可扩展 |
| **研发流程嵌入**（Issue/PR/CI 记忆） | 一般 | ✗ | ✓ | ✓✓ 最强，不用喂上下文 | ✗（陪伴进化非研发流） | △ 定制工作台可接流程 |
| **了解用户/记忆** | 一般 | ✗ | 一般 | ★★★★★ 最懂人 | ★★★★★ 长期记忆（多维） | ★★★☆☆ Data Pack 数据包 |
| **Skill 生态** | ★★★★★ 最成熟（marketplace） | ✗ | ★★★★（官方插件+第三方） | ★★★（plugins/skills） | —（角色即能力） | ★★★★☆ Everything is a Plugin |

### 三.5 新增两工具差异化 Feature（上表 8 维度之外的专属维度）

> 来源：战略笃定篇口述（第七轮 OpenClaw「灵魂赋能/10 角色硅基团队」+ Harness「把个人定制工作台门槛打掉」）；GitHub 实证 deepseek-harness 官方定位 = "Everything is a Plugin"。

**OpenClaw（养员工）专属 Feature**：

| 专属维度 | 说明 |
|:--|:--|
| **长期记忆（多维）** | 把它当"一个封装过的人"养——记忆跨会话留存，不是一次性 Session |
| **角色身份（真人名/岗位/边界）** | 给 Agent 起真人名、定岗位职责、划权限边界，像配员工 |
| **主动做动作（心跳/主动汇报）** | 会主动汇报、写任务书、分发调度，不等你问 |
| **陪伴进化** | 一点点养、越用越懂你、越用越强 |
| **局限** | 局部最优（单个角色优化，不擅全局重搭）；上下文久崩（超长上下文会退化） |

**DeepSeek Harness（造工具）专属 Feature**：

| 专属维度 | 说明 |
|:--|:--|
| **组件化** | 连官方都组件化——Everything is a Plugin，插件可改可替换 |
| **定制化** | 造自己的 Agent 工作台，把"个人定制工作台"的门槛打掉 |
| **跨平台** | Linux / Windows / 指令集，部署面广 |
| **多机部署** | 内网穿透，可多机分布式部署 |
| **局限** | 尚在入门期（老朱手操验证中，未实跑定论） |

## 四、实战匹配建议（什么时候用哪个）

| 任务类型 | 首选 | 理由 |
|:--|:--|:--|
| 需要先想清楚怎么做、拆解规划 | **Claude Code** | 编排最强 |
| 明确的长代码任务、跑一夜 | **Codex** | 云端长跑、执行强 |
| 需要常驻值守、飞书自动响应 | **Hermes** | 唯一 7×24 |
| 涉及自己的研发流程（Issue/PR/CI） | **CodeBuddy** | 嵌在流程里，无需喂上下文 |
| 需要理解用户偏好、贴身协作 | **CodeBuddy** | 最懂人 |
| 需要全面能力但自己知道怎么组合 | **Claude Code** | Feature 最全 |
| 要长期记住你、当员工养、主动汇报 | **OpenClaw** | 长期记忆 + 角色 + 主动 |
| 要定制一套自己的 Agent 工作台、多机部署 | **DeepSeek Harness** | 组件化 + 跨平台 + 多机 |

## 五、关键结论

1. **编排 ≠ Feature 数量**：Claude 功能最全但编排是"需要人告诉它怎么组合"；Codex 执行强但编排弱——两者不矛盾。
2. **Hermes 是唯一具备 L5 硅基组织形态的**（常驻服务 + 多 bot + 密钥池），其他三个是本地/云 CLI。
3. **CodeBuddy 的差异化 Feature 是"懂人 + 嵌流程"**：记忆来自研发流程而非人工喂上下文——这是它和 Claude/Codex 的本质区别。
4. **OpenClaw 的差异化 Feature 是"长期记忆 + 角色身份 + 主动"**：它和 Hermes 同属"Agent 级/养员工"层（一个龙虾钓几个 Hermes 是 Truman 的实操），区别在于 OpenClaw 侧重"把 Agent 当人养到有岗位有边界"，Hermes 侧重"多 bot 常驻值守"。
5. **DeepSeek Harness 的差异化 Feature 是"组件化 + 定制工作台 + 多机"**：官方都组件化（Everything is a Plugin），是"造工具"层，适合要定制自己 Agent 工作台、多机部署的场景。
6. **共同短板（都缺的 Feature）**：都没有 KDO 知识库直连消费协议——"点菜式"从周期表提 Feature 的能力。谁跑通谁获得差异化（见 AI基本功教练 #252 试点）。

## 六、失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| 工具思维选型 | 问"Claude 还是 Codex"，不问"这个任务需要什么 Feature" | 先列任务 Feature 需求，再匹配工具 |
| 单一工具依赖 | 把所有任务压在一个工具上，任务类型不匹配时抱怨"工具不行" | 按任务类型切换工具（§四） |
| 只看书面定位 | 拿文档角色定位选型，忽略实际体感差异 | 以实战体感为准（用户体感 > 文档） |
| 跳过三分法直接比 Feature | 逐个工具比 8 维度，越比越晕 | 先过 §一三分法定位到"养员工/造工具/打短工"，再查明细 |

## 七、Critique

**[工具最大主义者]**
> "六个工具换来换去太累，选一个最好的不就行了？"

**回应**：没有"最好的工具"——每个工具在特定 Feature 上是强项。Swiss army knife 也不可能取代传送带。真正的效率来自**按任务类型匹配工具**，而不是押注单一工具。

**[效率派]**
> "搞这么细的对比，不如直接上手用。"

**回应**：本卡的价值正是帮你快速上手时选对方向——避免"在 Hermes 上试长任务、在 Codex 上试值守"这类不匹配。先看 Feature 边界，再动手。

**[三分法质疑者]**
> "70% Feature 都重叠，分这么细干嘛？"

**回应**：正因为 70% 重叠（Truman 原话：这套 70% Feature 一样，每个有额外 10-30 个差异化 Feature），才更要用三分法先锁定"用它做什么"，再看那 10-30 个差异化 Feature——重叠部分不值得纠结，差异部分才是选型依据。

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:--|:--|
| 要选工具跑新任务 | 先过 §一三分法（养员工/造工具/打短工）定位，再列出 Feature 需求，查 §四 |
| 用户问"哪个 AI 工具好" | 反问任务类型 + Feature 需求，再给匹配建议（不要直接推荐） |
| 用户问"OpenClaw 还是 Harness" | 先三分法定位：长期养员工→OpenClaw，定制工作台/多机→Harness |
| 某个工具在某类任务上表现差 | 查 §三确认是不是 Feature 不匹配——换工具而不是怪工具 |

*老朱一手体感 + 战略笃定篇口述 · 2026-08-08 起 · 黄药师补全 OpenClaw/Harness 2026-08-30*
