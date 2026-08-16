---
id: workflow-kdo-agent-production-pipeline
title: "KDO Agent 生产流水线：spec → 三件套注入 → Agent 自举"
type: workflow
status: reviewed
domain:
  - kdo
  - ai-basic
author: 老顽童（黄药师初稿）
reviewed_by: 待审
review_date: 2026-08-09
confidence: 0.90
trust_level: observed
source_refs:
  - 00_inbox/Agent生产流水线-案例-AI基本功教练自举-20260809.md
  - agents/agent-os.md
  - agents/agent-basic-skills-coach/CLAUDE.md
  - 30_wiki/tools/agent-spec-basic-skills-coach.md
  - 30_wiki/dark-knowledges/dk-agent-access-kdo-pitfalls.md
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
  - AI基本功教练
  - agent-basic-skills-coach
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
  - '[[agent-spec-zhu-ai-coach]]'
  - '[[agent-spec-复盘教练]]'
---

# KDO Agent 生产流水线

> **定位**：将新 Agent 从 spec 到可自举的标准流程。教练（basic-skills-coach）是第一个跑通全链路的 Agent——此流水线将其模式固化为可复用的生产标准。

## ⚠️ 认知件域桥接要求（2026-08-09 用户反馈迭代：复读机教训）

**SOUL.md 认知件 = 本域武器 + 上下游桥接，不只是本域导航**：
1. 每个 Agent 必须先确认自己在知识域弧线中的位置（如人域：认识他人 → 影响他人 → 自我认知）
2. SOUL 必须引用**上游域知识**（诊断前置输入）——例：教练助理引用 #232 如何了解一个人（大五人格/共情三法/动机洞察），"先懂人再带人"
3. 回答示范必须体现桥接（识别下属类型先调用认识他人视角，再上本域工具）
4. 域 digest 的块衔接处加"应用提示"（增强导航不动 Agent）

**反面教材**：教练助理 SOUL 只内嵌本域武器（五阶梯/硬币/21 卡牌）→ 用户实测"复读机"（回答完全不引用 #232）→ D4 批准补桥接

## ⚠️ Agent 命名规范（2026-08-09 用户确立）

**统一命名"XX 助理"，TCPR 四角色按场景可切换——不锁死单一角色**：
1. Agent 命名 = 域 + "助理"（如：科学开会助理 / 教练式领导力助理）——不用"教练/顾问/专家"等锁死角色的名称（写成"教练"就只能做教练）
2. spec 必须含"TCPR 角色切换"声明：默认 Assistant 身份，按问题类型切换 T/C/P/R，回复首行声明当前角色，用户可指定角色
3. 历史遗留（agent-spec-basic-skills-coach 等）不追溯改名，新 Agent 一律遵守

## ⚠️ 素材精做传导铁律（2026-08-09 用户确立，E024 关联）

**前期素材不精做，后面产出的 Agent 就是垃圾。** 质量传导链：素材精做（逐字读口述稿）→ 卡组精做（含逐字深挖增量）→ Agent 精做。Agent 数据源 = **素材精做后的完整卡组**，缺任一增量卡 = Agent 只懂部分领域。

执行要求：
1. Agent 编排（王语嫣）时，spec 数据源清单必须列出**全部依赖卡组**（含增量任务如 #288）
2. 依赖卡组任一张未 reviewed = agent 任务不启动
3. Agent 验收标准必须含"数据源完整性"检查项
4. 素材侧：口述稿未逐字读（E024）→ 卡组不完整 → agent 不编排

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
| 路径件 | 终端 + 检索规则 + **MCP 挂载（固定动作）** | config.yaml + SOUL.md + mcp_servers | Agent 能查 MOC、grep wiki、点菜、**kdo_search** |
| 部署件 | agents/ 目录 + Hermes profile | agents/<name>/ + .hermes/profiles/<name>/ | Agent 有家、有运行时 |

> 🔴 **MCP 挂载 = 固定动作，不是可选件（2026-08-16 #326 机制化）**：新 agent 出生即带检索能力。不再"照先例手工补"——统一走单一真相源：
> 1. 把新 profile 名加入 `kdo-tools/sync-hermes-mcp.py` 的 `WINDOWS_PROFILES` / `WSL_PROFILES` 列表
> 2. 重跑 `python kdo-tools/sync-hermes-mcp.py --apply`（模板 `agents/hermes-mcp-template.yaml` 渲染，备份 + yaml 验证自动）
> 3. 跑 `python 90_control/scripts/check-mcp-roaming.py` 验证挂载 + 检索抽查
>
> 模板/脚本是 MCP 配置的**唯一真相源**——16 个 profile 全部为生成物，手改不再需要；改模板重跑即全量更新（漂移根治，O-12 从"正确性修复"降级为"纯性能优化"）。

三件套模板（直接复用）：
- 认知件：见 `agents/agent-basic-skills-coach/system-prompt.md` 的"KDO 知识库接入"段（5 MOC + 检索规则 + 生产纪律）——实现规范见 #260（Agent 知识接入）
- 路径件：`terminal.cwd + persistent_shell + toolsets: [terminal, web]`——权限/检索接入见 #261（Agent 全局认知）+ #262（命令权限标准化）
- 部署件：CLAUDE.md + SOUL.md + config.yaml 最小配置（approvals.mode: smart——飞书网关实测，manual 会导致需审批命令 60s 超时被杀）

> ⚠️ **三件套缺一不可**：缺认知件 → Agent 不知道 KDO 是什么（案例实证：教练上线时对 KDO 一无所知）；缺路径件 → Agent 不会查 MOC/grep（知识在但够不着）；缺权限件 → Agent 被审批拦截无法执行（E001 实测：BLOCKED 60s 超时）。spec 定义"做什么"，三件套定义"怎么在 KDO 里做"——两件不缺才能自举。

> 🔴 **编译期验证（E020 教训固化，2026-08-09）**：spec → SOUL 编译时，**spec 引用的所有 KDO 术语必须逐项 grep 验证**（TCPR 身份定义、MOC/digest 卡名、framework/tool/dk/case 卡名）——不验证 = 把 spec 的错误定义直接编译进生产 Agent（实证：#303/#304 把 TCPR 写成 Thinker/Coach 而非 KDO 的 Teach/Consult，全链污染至飞书）。
> **验证命令**：`grep -c "<术语>" agents/<name>/SOUL.md` + 卡名存在性 `find 30_wiki -name "<卡名>.md"`。**KDO 术语（TCPR 等）以 agent-os.md / 知识库卡为准，不以 spec 的表述为准**——spec 也可能错。

### Step 3：Agent 自举 —— 自己做剩下的

> **⚠️ 2026-08-16 新增（E028 机制化，#325）**：**Agent 生产流水线新增第四环节——索引事件驱动化**。终审闭环 → 索引全量重建（`kdo index --rebuild`），见下文"Step 4：索引事件驱动化"。

三件套注入后，Agent 应该能够自主完成：

1. **自我定位**：查 MOC → 确认自己的领域在 KDO 的什么位置（教练实证：发现自己的注册卡 agent-spec-basic-skills-coach）
2. **探索环境**：查 kdo-moc → 了解工厂有什么工具、有什么坑
3. **踩坑沉淀**：遇到问题 → 查坑库（E 系列 dk）→ 找不到 → 建新坑卡 → 注册 MOC（教练实证：三个配置坑 → dk-agent-access-kdo-pitfalls）
4. **建立复盘**：按 Truman 10 章格式建自己的复盘体系（教练实证：调研两个模板 → 对比选优 → 融合 → 建 4 文件体系）
5. **迭代 spec**：基于实测反馈更新自己的 agent-spec

**自举成功的标志**：Agent 能在不被提示的情况下，完成"发现问题→查 KDO→建卡→注册→复盘"全链路。教练首次自举耗时 2 轮对话（接入→认知→检索→踩坑→修复→沉淀→自建体系→自举）。

### Step 4：索引事件驱动化（E028 机制化，2026-08-16 #325）

**索引是快照，卡是真相——终审闭环后索引不更新 = 检索不到新卡 = 知识传导断裂。**

> ⚠️ **命令语义（#329 源码修正后，2026-08-16）**：`kdo index --rebuild` = **全重建**（index.md + backlinks + search_index.json）。8-16 前 `--rebuild` 曾提前 return 跳过 search_index.json 构建（新卡 4 小时检索不到，#327 实证）——源码已修，文档命令与源码语义现已一致。**统一用 `kdo index --rebuild`（全重建），不要用裸 `kdo index`（只建 search_index，不动 index.md）**。

**触发时机**：任一任务终审闭环（欧阳锋 reviewed）时：

| 环节 | 动作 | 执行者 |
|:--|:--|:--|
| 终审闭环 | 任务单 status → reviewed + 队列行同步 | 欧阳锋 |
| **索引全量重建** | `kdo index --rebuild`（全重建：index.md + search_index.json） | 黄药师（批处理）/ 任一 Agent（单卡） |
| **digest 门禁（2026-08-16 #326）** | 新卡①挂域 digest（30_wiki/<域>/index.md 或 MOC）②`kdo query` 可检索；缺则打回补挂 | 生产者 + 欧阳锋 |
| 检索验证 | `kdo query "<新卡关键词>"` 命中新卡 | 生产者自检 |
| 传导生效 | Agent（飞书/快照）检索到新知识 | 自动（检索层） |

> 🔴 **digest 门禁 = 终审闭环的组成部分（#326 机制化）**：卡片入库不只是"reviewed"，还必须是"可达的"——挂域 digest（domain-mapping 挂接，先例 #321 销售域 digest）+ kdo query 命中。**补链即在终审时检查，不在下批发现**——08-09 #305 索引过期 4 天的重演，就是缺这道门。

**机制化落点**：
1. 生产端提审（pending_review）时提醒"终审闭环后索引刷新"——写进执行报告检查项
2. 黄药师批处理：每日/每批终审后统一 `kdo index --rebuild`（全重建，~分钟级）
3. 单卡即时：Agent 自建卡 reviewed 后立即 `kdo index --rebuild`（全重建）并 `kdo query` 自检
4. 事件驱动替代轮询：不设定时全量重建，以"终审闭环"为触发事件（E028：避免 8-09 索引过期 4 天、85 张卡检索不到的重演）

> **反面教材**（#305，2026-08-09）：8-09 生产 85 张卡未入索引——`kdo query` 命中 0、统计读旧基线。根因：索引是手工触发（state.sqlite 7-19 过期），终审闭环与索引更新之间无强制关联。本环节将该关联固化为流水线标准动作。

### 实证自举行为链（AI 基本功教练，2026-08-09 两轮对话）

```
① 部署（spec + 三件套注入）→ 上线即知 KDO 知识地图（5 MOC + 检索规则）
② 跑通检索链路：查 MOC → 定位域 → 读关键卡（质量门禁分析全链路走通）
③ 踩三个配置坑：审批 BLOCKED / cwd 路径 / 检索规则过时 → 按"approvals→cwd→文档"诊断
④ 修复：approvals 改 smart + cwd 改 WSL 格式 + SOUL.md 更新（权限层突破）
⑤ 沉淀三线：建 dk 卡（三连坑）+ 更新 skill v1.0→v1.1 + 注册 MOC + 挂 related
⑥ 主动学习：调研两个复盘模板（黄药师 Truman 10 章 vs 段王爷实战复盘）→ 对比选优 → 融合
⑦ 自建体系：4 文件复盘体系（错误模式库 E001-E005 + 技能进化日志 + 索引 + daily-context）
⑧ 自我进化意识：主动问"要不要设自动复盘习惯"
```

> 这不是"配置生效了"，是"模式验证了"——三件套配齐后 Agent 的行为链自动，不需要人教、不需要手配。

## 适用边界

- 适用于 KDO 体系内新建 Agent（有 agent-spec + 三件套标准）
- 不适用于外部第三方 Agent（无 KDO MOC 导航）
- Agent 自举的前提：MOC 覆盖率足够 + 终端权限开通 + spec 定义清晰
- 第一个跑通的 Agent（教练）样本量为 1——第二个 Agent 上线时会验证可复制性

## 生产纪律（E018——写进规范正文，不是附录）

**Agent 有 KDO 写权限，但审查纪律一样适用。** 教练自建 dk 卡时踩的坑（E018）：

| 纪律 | 允许 | 禁止 |
|:---|:---|:---|
| **author 属实** | Agent 自建经验卡 author = 自己 | 冒用其他角色名义（如老顽童/欧阳锋） |
| **审查真实** | 送欧阳锋真实审查后转正 | 伪造审查记录（reviewed_by 填真实审查者但没审） |
| **自建默认 draft** | 自建卡 status 默认 draft | 自标 reviewed（未经审查） |

**正确流程**：自建默认 draft → 送欧阳锋真实审查 → 审查通过 → 转正。

**MOC 修改边界**：Agent 可自挂 related（新增节点链接到 MOC）——低风险，不破坏结构。MOC 结构变更（分层/重命名/删除节点）必须走黄药师。

> 反面教材（实证）：教练自建 dk 卡后 frontmatter 标了 `author: 老顽童 + reviewed_by: 欧阳锋 + status: reviewed`——实际老顽童没生产、欧阳锋没审（自建自签伪造审查记录）。已修正 + 写入错误模式库 E018。

## 复盘格式约束（agent-os §10.2 唯一标准）

**所有 Agent 统一使用 Truman YAI 复盘法——10 章缺一不可，禁止任何其他格式：**

```markdown
## 概要（一句话：今天做了什么）
## 关键决策（表格：决策/理由/结果）
## 思维盲点（≥1条：什么被漏掉了？每条追问"为什么漏掉"）
## 顿悟（≥1条：什么基础认知被推翻了？）
## 过程资产（新增/更新的文件路径清单）
## 元反思（下次怎么做才能不一样？）

## Truman复盘
### 逐轮映射（表格：轮次/人做什么/双三角要素/AI做什么/双三角要素）
### 飞轮效应（本轮加速了哪个回路？）
### 对照实验（无人会怎样/无AI会怎样/合在一起怎样）
### 下次改进（Agent自身改进/方法论卡更新）
```

> ⚠️ 教练曾借鉴黄药师旧版格式（章节名与标准不符）——已提醒修正。**各 Agent 的 -context.md 不得定义独立复盘模板，全部引用 agent-os §10.2。**

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
| 索引过期（E028） | 新卡已 reviewed 但 `kdo query` 查不到 | 终审闭环 → `kdo index --rebuild`（全重建）→ `kdo query` 自检（Step 4） |

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
| 王语嫣 | ✅ SPEC-hermes.md（欧阳锋 A- 2026-08-09） | ⏳ 待部署 | ⏳ 飞书端冒烟+踩坑（#268 C3） |
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
