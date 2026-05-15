---
title: "内容工厂的工业化手册"
type: "control"
status: "stable"
version: "1.6"
created_at: "2026-05-09"
updated_at: "2026-05-16"
author: "欧阳锋"
source: "EC工业化规范手册 v2.8.0 → KDO 领域迁移 + Sprint 1-3 实践经验"
supersedes: ["kdo-industrialization-manual-v1.0"]
based_on:
  - "[[EC工业化规范手册]]"
  - "[[ec工业化规范手册-v2.8.0]]"
  - "[[kdo-ec-industrialization-migration-proposal]]"
  - "[[high-density-composite-compilation-strategy]] (v2.0)"
---

# 内容工厂的工业化手册 v1.6

> **定位**：KDO 知识生产管线的工业化操作标准——将知识萃取、编译、交付、行为转化过程升级为可重复、可审计、防呆的标准化流程。
> **编制**：欧阳锋（Architect）| 初版 2026-05-09 | v1.6 2026-05-16
> **范围**：KDO 工作空间全部知识生产活动
> **对标**：EC 工业化规范手册 v2.8.0（编程领域 → 知识生产领域迁移）

---

## 一、核心哲学

### 1.1 知识生产是管线，不是手艺

EC 手册的核心洞见——"将软件工程从手艺升级为制造"——对知识生产同样成立。一堂课程的知识萃取不是凭感觉的精雕细琢，而是可拆解、可验证、可复用的标准化流水线：

```
capture → ingest → enrich → produce → validate → ship → feedback → improve
```

每阶段有明确的进入条件、退出标准、举证要求。知识卡片不是"写得好"或"写得不好"的主观判断，而是通过三层质量门禁的客观验证。

### 1.2 审而不改

对标 EC 手册「只测不修」铁律（§27）：测试者发现 Bug 只能报告，不能自己动手修。

KDO 对应原则：**Architect（欧阳锋）审查产出 → 指出问题 → 黄药师修正 → Architect 复审**。Architect 不直接编辑黄药师的产出文件——审查和执行的分离防止"自己审自己"的盲区。

唯一的例外：Architect 可以直接修改 `90_control/` 下的控制文件（本手册、AGENTS.md、failure-modes.md 等），因为这些是 Architect 的职责域。

### 1.3 失败模式从事故事实中生长

对标 EC 手册 §13 的 14 种失败模式（F001-F014）——全部来自真实事故，没有一条是坐在房间里提前设计的。

KDO 操作原则：**每踩一次坑 → 入库一种模式 → 更新 Lint 规则 → 更新禁止清单**。不提前设计「可能出什么问题」的框架。失败模式库（`90_control/failure-modes.md`）从血泪中生长，不是从想象中构建。

### 1.4 Agent 优先：细粒度卡片优于复合大卡

**这个知识库的主要用户是 AI agent，不是人类。** 设计原则与人类导向的 wiki 根本不同：

| 维度 | 人类读者 | AI Agent |
|------|---------|----------|
| 信息消费 | 线性阅读，需要上下文连贯 | RAG 检索，按需拉取相关片段 |
| 最佳粒度 | 中长篇文章（5000-10000 字） | 单概念卡片（500-2000 字），精确命中 |
| 关联方式 | 目录 + 章节导航 | wiki-link 图遍历 + 向量检索 |
| 最大风险 | 碎片化 → "看不到全貌" | 大卡 → 检索上下文爆炸 |

**原则：保持细粒度独立卡片，通过 Hub Page（导航页）提供宏观定位。** 每张知识地图 → 一张概念卡。每份口述稿 → 一张概念卡。Hub Page 只写概览 + wiki-link 列表（<3000 字），不做内容搬运。

详细策略见：[[high-density-composite-compilation-strategy]]（v2.0，v1.0 复合编译方案已废弃）。

### 1.5 视觉信息的优先级

知识地图的核心价值在视觉结构中——空间层级、分组逻辑、阅读路径、视觉强调、留白含义。OCR 文字只能捕获图中的显式文字，丢失了：
- 哪些概念是并列、因果、前提条件（空间位置暗示）
- 同色块/同区域内的分类体系（分组暗示）
- 箭头/编号/排列暗示的顺序关系（阅读路径）
- 放大/加粗/高亮的视觉权重（强调暗示）
- 刻意分开的区域是否暗示对立或独立（留白含义）

**原则：知识地图必须看了原图再提炼，不得仅依赖 OCR 文字。** OCR 文字是补充，不是替代。

### 1.6 知识生产的目标不是组织知识，是改变行为

对标 AI 思维卡的「认知升级系统 v3.2」方法论，知识生产管线在 ship 之后缺失了最关键的一环：**行为转化**。

AI 思维卡的十步框架（IDENTITY→MODEL→EVIDENCE→CONTRAST→ACTION→REFLECTION→MY TAKE→ICAP→CTA→FOLLOWUP）在 MODEL 之后有三个我们完全没有的环节：

- **ACTION**：具体场景 + 触发器 + 追问清单——"老板甩来新项目，别急着点头，先问 PEAS 三个问题"
- **CTA**：今晚就做，三选一，5 分钟内能启动——"找张纸，把最焦虑的项目按 PEAS 拆完"
- **FOLLOWUP**：三周后回来复诊——"哪些洞察实际调用了？哪些完全没用过？为什么？"

**原则：每篇产出必须包含至少一个"今晚能做的动作"。** 知识不转化为行为就是死知识。这条写入 content quality gate P0。

### 1.7 卡片层的三个行为转化要件

v1.4 在产出层（content gate P0 + KF-023）建立了行为转化标准——但黄药师分析 AI 思维卡后指出：行为转化不应等到 produce 阶段才介入。卡片层就应该种下行为的种子，让 agent 在检索卡片时就能获取"什么时候用、什么时候千万别用、第一个动作是什么"。

以下三个要件适用于 **方法（tool）/ 工具（tool）/ 框架（framework）** 三类卡片。概念卡和索引卡不受此约束——它们不承载操作指令。

#### 要件 1：Critique → 外部攻击子节

在 `[Critique]` 节的现有"内部局限性"之外，新增"外部攻击"子节：

```
### 外部攻击
至少 1 条：该方法的反对者/竞争学派会怎么批评它？（不带 straw man）
```

**本质**：不是自己想象的假反驳——必须引用真实的外部批评。这是论证质量的第二道门禁，超越"作者自述的局限性"。Sprint 9 的 Constraints 去模板化只做了"加一条特有边界"，没做"从敌人视角找漏洞"——这是升级版。

**引证启发法**：对任何声称"X 可以结构化/方法化"的框架，找该领域最著名的**反方法化**学者——他主张 X 的本质不可被步骤化（Sprint 12 Batch A 25 张卡验证有效）：

| 卡片领域 | 反对者来源 | 核心张力 |
|---------|-----------|---------|
| **管理/组织** | Mintzberg（手艺论）、Pfeffer（领导力产业批判） | 管理是手艺 vs 管理是可建模的系统 |
| **学习/教育** | Freire（被压迫者教育学）、Illich（去学校化）、Papert（建构主义） | 学习是解放/建构 vs 学习是可标准化的流程 |
| **心理/决策** | Kahneman（噪声审计）、Klein（RPD 自然决策）、Argyris（防御性推理） | 人是非理性主体，框架深度 ≠ 行为改变 |
| **产品/设计** | Norman（以用户为中心）、Papanek（设计伦理） | 品味中心 vs 用户中心；精英审美 vs 社会责任 |
| **创业/创新** | Taleb（Knight 不确定性）、Blank（客户开发） | 不确定性不可建模 vs 方法化创业 |
| **AI/技术** | Marcus（深度学习局限）、Bender（随机鹦鹉） | 涌现能力 vs 符号推理；语言模型 vs 统计模式匹配 |

**操作步骤**：
1. 识别卡片的核心主张（"X 可以通过 Y 方法系统化地做到"）
2. 搜索"谁反对把 X 方法化"——找该领域最著名的反方法化/反系统化学者
3. 引用该学者的具体论证（哪本书/哪篇论文，他具体说了什么），而非"XX 学派不同意"
4. Straw man 检测：如果你引用的学者本人看到这段话，他会不会说"这不是我的立场"？如果是 → 重写

#### 要件 2：Synthesis → "不要用的场景"表

在 `[Synthesis]` 节新增固定的"不要用的场景"子节：

```
### 不要用的场景
| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| ...  | ...       | ...     |
```

2-3 条。每条回答三个问题：什么具体场景下这个工具会失效？失效机制是什么？该用什么替代？

**本质**：知道什么时候不用 = 真正理解了。适用边界和核心内容是一级信息的两个面。和 Sprint 9 的 Constraints 边界分析配合——Constraints 说"这个工具本身的局限"，"不要用的场景"说"对用户而言什么时候该放下这个工具换别的"。

**质量三信号**（Sprint 12 Batch A 审查总结，每条逐项检查）：

| # | 维度 | ✅ 达标 | ❌ 不达标 |
|---|------|---------|----------|
| 1 | **场景具体性** | "创意发散/头脑风暴阶段"——可识别、可遇到 | "创造性工作"——太宽泛，覆盖一半使用场景 |
| 2 | **失效因果** | "结构化追问是收敛工具，会把思维过早钉死在框架上"——解释为什么失效 | "不适合创新场景"——没说为什么 |
| 3 | **替代指名** | "IDEO brainstorming 规则——延迟判断、追求数量"——指名具体方法/来源 | "可以使用更灵活的方式"——没给替代方案 |

**反模式**："根据情况灵活运用""需要结合实际情况判断"——这类表述等于没写。如果替代方案不能指名具体方法/框架/人名，重写。

#### 要件 3：Action Triggers 节

在卡片 body 中新增 `## Action Triggers` 节（位于 Synthesis 之后）：

```
## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 场景描述（用户实际会遇到的情况） | 5分钟内可启动的1个动作 | 怎么知道做对了 |
```

3 个触发场景 + 对应的第一动作 + 可验证的成功指标。

**本质**：从"知道这个工具"到"在真实场景中调用它"的桥梁。对标 KF-023：知识必须能转化为今晚的行为。三列结构——触发场景（什么时候该想起这张卡）→ 第一个动作（想起之后第一步做什么）→ 成功指标（怎么知道不是自欺欺人）。

**与 v1.4 产出层 ACTION 锚点的关系**：产出层的 ACTION 锚点面向人类读者（"读完这篇文章后做什么"），卡片层的 Action Triggers 面向 agent 检索（"agent 检索到这张卡时，该给用户什么操作指令"）。两者配合：卡片提供原料 → produce 组装为读者可执行的动作。

**成功指标的三种可验证模式**（Sprint 12 Batch A 25 张卡总结）：

| 模式 | 特征 | 示例 | 反例 |
|------|------|------|------|
| **数量型** | 数得出来 | "≥3条具体事实（带时间/数据/行为描述）"；"列出≥3个过去3个月接触的领域内最好事物" | "了解更多" |
| **时间型** | 掐得了表 | "≤2分钟内定位领域并选定1个工具"；"L1感受≤5行写完" | "更快" |
| **频率型** | 记得了数 | "一天中≥3次在给答案之前先问了一个澄清问题"；"团队连续4周每周完成1次拆解会" | "养成习惯" |

**不可接受的指标**："理解更深入了""能力提升了""团队更好了"——这些是结果不是指标。指标必须可被第三方验证（别人看同样的数据能得出相同的通过/不通过结论）。

**"第一个动作"的 5 分钟可启动测试**：Builder 写完第一个动作后自问——"我现在放下手里的活，能不能在 5 分钟内开始做这个动作？"如果不能（如"建立一套完整的复盘体系"），拆解为更小的第一步（如"找一张纸，写下最近一个项目的 L1 感受"）。

### 1.8 Agent 原生设计——卡片是知识图谱节点

**30_wiki/ 是 agent 的知识基座，不是人类的阅读材料。** 消费链路：

```
30_wiki（Agent 消费）──查询/遍历──▶ Agent ──生成──▶ 40_outputs（人类阅读）
```

因此卡片设计遵循「微型知识图谱节点」原则：frontmatter 是 API 面，claims 是原子知识单元，图边支撑 Graph RAG 遍历。

**三步编译在 agent-native 格式下的映射**：

| 三步编译 | 人类叙事格式（旧） | Agent 结构化格式（新） |
|---------|-----------------|---------------------|
| Condense | 叙事段落 | Claims 列表，每条 `claim:NN [conf=X]` 可独立引用 |
| Critique | 推理段落 | Constraints & Boundaries + per-claim confidence |
| Synthesis | 文章内 wikilink | Synthesis 关系表 + frontmatter 图边 |

**卡片类型体系**（详见 [[agent-native-card-design]]）：

| type | 用途 | Claims 范围 | 行数上限 |
|------|------|:--:|:--:|
| `composite-concept` | 多源聚合 | 15-30 | ≤500 |
| `framework` | 知识地图结构化描述 | 5-15 | ≤300 |
| `case` | 案例卡 | 5-10 | ≤200 |
| `tool` | 检查清单/画布/模板 | 3-10 | ≤150 |

**拆分规则**：单卡 Claims > 30 或 >500 行或 estimated_tokens >5000 → 触发拆分。

### 1.9 批量回溯升级执行节奏

当需要为已有卡片批量追加新节（如 v1.5 三要件回溯）时，按以下节奏执行（Sprint 12 Batch A 25 张卡验证有效，补充 KF-022）：

**每轮流程**：

```
1. 选卡：按 estimated_tokens 升序取 ≤5 张（先小后大，降低单轮上下文压力）
2. 逐张追加：只追加新节，不改原有 Claims / Constraints / frontmatter 字段
3. 门禁检查：kdo lint 确认 0 new errors（非预存错误）
4. 记录：在任务文件中录入本轮完成表（卡片 + 外部攻击来源 + 不要用场景数 + Action Triggers 数）
```

**全批完成后**：

```
5. Architect 抽检 20%（或每域 ≥2 张），检查理解门禁三信号：
   - 反例具体性（外部攻击是否引用真实学者和具体论证）
   - 案例筛选（不要用场景是否具体、失效机制是否有因果解释）
   - 跨域连接（替代方案是否指名具体方法/框架/人名）
6. 审查通过 → 启动下一批。不通过 → 退回修正，修正后再审。
```

**分批策略**：按 `type` 分组执行（framework → tool → concept），同 type 内按域或字母序均可。不同 type 的升级内容不同（concept 卡豁免外部攻击），分批避免规则混淆。

**节奏设计原则**：5 张/轮是 KF-022 的上限，不是目标。如果单张卡体量大（>300 行或 >3000 tokens），降到 3 张/轮。质量不向速度妥协——本轮发现的问题本轮修正，不留给后续轮次。

---

## 二、角色体系

对标 EC 的四角色循环（设计者/协调者/开发者/测试者），KDO 采用三角色分工：

| 角色 | 对标 EC | 职责 | 红线 |
|------|---------|------|------|
| **用户（老朱）** | 设计者 + 协调者 | 定方向、定优先级、定角度、终决拍板 | 不参与内部辩论细节 |
| **Architect（欧阳锋）** | 审查者 | 设计规则、审查产出、维护门禁、裁决例外、记录决策、**迭代维护本手册** | **审而不改**——不直接编辑黄药师的产出文件 |
| **Builder（黄药师）** | 开发者 | 执行流水线、高质量内容提炼、KDO 开发、**复合编译执行** | 不主动发起架构讨论，有问题报给 Architect |

**协作协议**：完整定义在 [[debate-protocol.md]]。核心原则——Architect + Builder 的辩论不消耗用户注意力。达成共识的事项直接执行。辩论升级到用户时压缩为 ≤3 选项的选择题。

**唯一信息枢纽**：对标 EC 的协调者中枢，KDO 的协调者是**文件系统本身**——Architect 和 Builder 在同一文件中 append 辩论，用户通过 Obsidian 查看。不需要人工转发。

### 2.1 Agent-in-the-loop 模式

当任务需要多模态能力（如分析知识地图原图的视觉结构）时，可调用本地 agent 辅助：

```
Builder 提交（原图 + OCR文字）→ Agent 分析视觉结构 → Builder 核实 → 写入卡片
```

**约束**：
- Agent 分析不是替代人工判断——最终由 Builder 决定哪些视觉关系值得写入卡片
- Agent 只能辅助 Builder，不能绕过 Builder 直接修改 wiki 文件
- Agent 的输入必须包含原图（不可降级为仅 OCR 文字）

---

## 三、管线阶段门禁

对标 EC 的 Stage Gate 体系。每个管线阶段有进入条件和退出标准（门禁）。

### 3.1 标准管线

| 阶段 | 进入条件 | 退出标准（门禁） | 门禁级别 |
|------|---------|----------------|:------:|
| **ingest** | 文件在 `00_inbox/` | `source_refs` 已写入 frontmatter，skeleton 已创建，`log.md` 已记录 | P0 警告 |
| **enrich** | source `status: draft` | 三步编译完成，`status: enriched`，frontmatter 字段齐全，source_refs 非空 | **P0 阻断** |
| **produce** | ≥1 个 concept `status: enriched` | artifact frontmatter 完整，非 stub，通过 validate | P0 警告 |
| **validate** | artifact `status: draft` | L1 全通过，broken links = 0，`fb_*` 已生成 | P0 警告 |
| **ship** | artifact `status: validated` | 发布目标明确（article/local/test），`ship_*` 已写入 | P0 警告 |

### 3.2 高密度素材 enrich 变体

当 ingest 产出大量（>20 张）来源相同主题的素材时，enrich 分两步走：

**步骤 A：细粒度质量达标**

每张知识地图 → 一张独立概念卡。每份口述稿 → 一张独立概念卡。每张卡必须通过标准质量门禁：

| 动作 | 退出标准 |
|------|---------|
| 源文件归档 | 图片从 `00_inbox/` → `10_raw/sources/`，source_refs 更新 |
| 三步编译 | Condense ≥3 / Critique ≥1（指名假设或边界） / Synthesis ≥2 |
| Visual Analysis | 每张知识地图原图五维分析（层级/分组/路径/强调/留白），至少覆盖三维 |
| 验证 | `kdo lint --wiki-path` 0 warning |

**步骤 B：导航层构建**

质量达标后，按工具箱/主题聚类建 Hub Page：

| 动作 | 退出标准 |
|------|---------|
| 写概览 | 3-5 句话说明该模块是什么、解决什么问题 |
| 建导航 | 列出所有子卡片的 wiki-link + 一句话定位 |
| 三步编译 | Critique 针对模块整体 / Synthesis 链接模块外概念 |
| 大小控制 | <3000 字（不做内容搬运，子卡内容不复制到 Hub） |

> 详细模板和聚类方案见 [[high-density-composite-compilation-strategy]] v2.0。

**门禁阻断规则**：
- P0 项为**强警告（可 override）**，非硬阻断。使用 `--skip-gate <reason>` 手动越过，越过记录写入 state.json + log.md
- P1 项警告不阻断
- enrich 阶段的 `source_refs` 非空为唯一硬阻断——无源文件溯源的知识卡片不得标记为 enriched

---

## 四、三层质量门禁

对标 EC 的三层质量防护体系（设计防护 → 过程防护 → 审查防护），KDO 定义三层 Lint 规则：

### L1 — 结构完整性（对标编译检查）

| 规则 | 严重度 | 状态 |
|------|:------:|:----:|
| frontmatter 必填字段齐全（title, type, status, source_refs, created_at） | 🔴 P0 | ✅ 已实现 |
| `source_refs` 指向的文件存在（非 broken wikilink） | 🔴 P0 | ✅ 已实现（Sprint 1） |
| `status` 值与管线阶段一致（draft/enriched/validated/shipped） | 🔴 P0 | ✅ 已实现（Sprint 1） |
| `source_refs` 不得指向 `00_inbox/` 临时路径（须指向 `10_raw/sources/`） | 🟠 P1 | ⚠️ 手动检查（待自动化） |
| 无裸 URL（链接必须用 markdown 或 wikilink） | 🟡 P2 | ❌ 待实现 |
| 无 BOM 字符导致的 frontmatter 解析错误 | 🔴 P0 | ✅ 已修复（KDO 源码级） |

### L2 — 内容质量（对标单元测试）

| 规则 | 严重度 | 阈值 |
|------|:------:|------|
| Condense 有实质性内容（非 "TBD" 或空段落） | 🟠 P1 | ≥3 条核心结论；若为 agent-native 格式则 Claims ≥5 条，每条带 `[conf=X]` |
| Critique ≥ 1 条，且至少一条**指名具体假设或边界**；方法/工具/框架卡须含"外部攻击"子节（≥1 条真实外部批评） | 🟠 P1 | 禁止"需要更多验证"式万能废话；若为 agent-native 格式则 Constraints ≥1 条 boundary claim |
| Synthesis 有 ≥ 2 个 wikilinks（允许含 index 页）；方法/工具/框架卡须含"不要用的场景"表（≥2 条场景+失效机制+替代方案） | 🟡 P2 | agent-native 格式额外检查 frontmatter 图边字段（prerequisites/component_of/related）非空 |
| 全文 > 500 字 | 🟡 P2 | — |
| **Visual Analysis**：知识地图原图必须分析视觉结构 | 🟠 P1 | 层级/分组/路径/强调/留白 至少覆盖三个维度 |
| **Agent-native frontmatter 完整**（新增） | 🟠 P1 | id、type、domain、query_triggers(≥3)、estimated_tokens、所有图边字段非空 |
| **体量合规**（新增） | 🟡 P2 | 不超过对应 type 的 Claims 数和行数上限 |
| **Action Triggers 节**（v1.5 新增）— 方法/工具/框架卡必填 | 🟠 P1 | ≥3 个触发场景，每条含第一动作 + 成功指标 |
| **EVIDENCE 审计**（v1.4 新增） | 🟡 P2 | 至少一条 claim 标注其论据的偏差类型（选择性举证/作者偏向/简化），至少引用一个真实外部批评 |

L2 全部为**警告级别**，不做阻断。

**Critique 质量底线**：至少一条 Critique 必须指名具体假设或边界——「这门方法论的 XX 前提在 YY 场景下不成立」——而非「需要更多验证」「目录层级有限」等万能废话。方法/工具/框架卡另须含至少一条**真实外部批评**（不带 straw man）——该方法的反对者/竞争学派实际提出过什么质疑？

**EVIDENCE 审计标准**（v1.4）：在 Constraints 节的边界分析之外，鼓励标注论据质量：
- **偏差标注**：至少指出一条核心 claim 的论据有什么选择性（选择性举证/作者偏向/过度简化/幸存者偏差/确认偏误）
- **外部攻击**：引用至少一个真实的外部批评（谁说这条不对？他为什么这么说？）——非自己想象的假反驳
- **反事实测试**：去掉这个案例/论据，模型还成立吗？测试每个论据的实际承载重量

**Burn line**（v1.4）：framework 和 composite-concept 卡片建议在 `## Synthesis` 上方添加一行 `> **Burn line**: 一句话烧到骨髓`。牺牲精确换可记忆——不是每张卡都需要，但顶层框架卡应该有。

### L3 — 管线一致性（对标集成测试）

| 规则 | 严重度 |
|------|:------:|
| `status: enriched` 的卡片必须有 enrich 阶段的举证记录 | 🟠 P1 |
| `status: validated` 的 artifact 必须有 `fb_*` 记录 | 🟠 P1 |
| `status: shipped` 的 artifact 必须有 `ship_*` 记录 | 🟠 P1 |
| source → concept → artifact → ship 链路完整可追溯 | 🟠 P1 |

**质量公式**：`交付质量 = 结构完整性 × 内容质量 × 管线一致性`

---

## 五、举证标准

对标 EC 的 Audit Trail（审计追踪）——说"做了"不够，必须出示证据。

| 管线动作 | 强制举证 | 举证内容 | 粒度 |
|---------|:------:|---------|------|
| **enrich** | ✅ 强制 | 变更摘要（三步编译做了哪些关键修改），非完整 diff | 三节点之一 |
| **enrich（复合编译）** | ✅ 强制 | 变更摘要 + 每张原图的 Visual Analysis 记录 + 源文件归档确认 | 三节点之一 |
| **produce** | ✅ 强制 | artifact 正文 + gate 通过日志 | 三节点之一 |
| **validate** | — | lint 报告即为举证，不另要求 | — |
| **ship** | ✅ 强制 | 发布目标 + 时间戳 + 版本号 | 三节点之一 |
| **ingest** | — | 机械化操作（cp + frontmatter 注入），不需举证 | — |

**举证粒度原则**：仅 enrich/produce/ship 三个关键节点强制举证。enrich 举证为变更摘要而非完整 diff——完整 diff 在概念卡质量审查时噪音太大。

**源文件归档举证**（复合编译专用）：enrich 完成后必须确认：
1. 所有引用图片已从 `00_inbox/` 复制到 `10_raw/sources/`
2. `source_refs` 全部指向 `10_raw/sources/`（无 `00_inbox/` 引用残留）
3. 口述稿引用的 source 文件（非 inbox 临时 MD）

---

## 六、铁律

对标 EC 的 20 条核心铁律（CF-001~020），定义 KDO 工业化铁律（KF-001~022）。

### 设计阶段

| 编号 | 铁律 | 对标 EC | 严重度 |
|:----:|------|:------:|:------:|
| KF-001 | **核心规范双重签发**：本手册和 AGENTS.md 的变更须 Architect 提案 + 用户批准 | CF-020 | 🔴 |
| KF-002 | **AGENTS.md 优先原则**：任何单次操作指令不得与 AGENTS.md 冲突。如有冲突，先更新 AGENTS.md | CF-002 | 🔴 |
| KF-003 | **禁止事项强制列明**：AGENTS.md 的禁止清单必须与 failure-modes.md 保持同步，每条禁止行为必须对应一个已知失败模式 | CF-003 | 🔴 |
| KF-004 | **验收标准可量化**：质量门禁规则不可含"合理""基本""较好"等模糊词。每条规则必须可被程序或人工明确判定通过/不通过 | CF-004 | 🔴 |
| KF-005 | **溯源强制**：`source_refs` 必须指向存在的文件。空数组 = P0 违规，卡片不得标记为 enriched | CF-005 | 🔴 |

### 执行阶段

| 编号 | 铁律 | 对标 EC | 严重度 |
|:----:|------|:------:|:------:|
| KF-006 | **禁止 git add -A**：不得使用 `git add -A` 或 `git add .`。只 stage 明确列出的文件 | CF-007 | 🔴 |
| KF-007 | **批量修改前全量 Lint**：修改 ≥3 个文件前，先跑 `kdo lint` 全量确认基线状态 | CF-008 | 🟠 |
| KF-008 | **每阶段退出前跑门禁**：离开 enrich/produce/ship 阶段前必须跑对应门禁并记录结果 | CF-009 | 🟠 |
| KF-009 | **疑问不滞留**：Architect 与 Builder 无法达成共识时，24小时内升级到用户。不得在评估文件中长期搁置 | CF-010 | 🟠 |
| KF-010 | **Ship 前全量检查**：`kdo lint --strict` + `kdo validate` 全通过后方可 ship | CF-011 | 🔴 |
| **KF-024** | **卡片层行为转化三要件**（v1.5 新增）：方法/工具/框架类卡片必须包含：(1) Critique 外部攻击子节 ≥1 条真实外部批评，(2) Synthesis "不要用的场景"表 ≥2 条（场景+失效机制+替代方案），(3) Action Triggers 节 ≥3 个触发场景+动作+成功指标。概念卡和索引卡豁免 | F-KDO-016 | 🟠 |

### 审查阶段

| 编号 | 铁律 | 对标 EC | 严重度 |
|:----:|------|:------:|:------:|
| KF-011 | **审而不改**：Architect 审查产出时只指出问题，不直接修改 Builder 的产出文件。审查和执行的分离防止盲区 | CF-012 | 🔴 |
| KF-012 | **事故必入库**：每次知识生产事故（D 级卡、broken link、source_refs 为空等）必须在 failure-modes.md 中追加入库。事故不入库 = 白踩坑 | CF-013 | 🔴 |
| KF-013 | **D 级卡打回**：三张模式 A（模板填充式 Condense + 复制粘贴式 Critique + source_refs 为空）的卡片必须退回 draft | CF-014 | 🟠 |
| KF-014 | **审查结论双轨记录**：Architect 的审查结论同时记录在评估文件（`60_feedback/assessments/`）和被审查文件的决策记录区块 | CF-015 | 🟠 |

### 变更阶段

| 编号 | 铁律 | 对标 EC | 严重度 |
|:----:|------|:------:|:------:|
| KF-015 | **源文件不可删**：禁止删除有 `source_refs` 指向的 `10_raw/sources/` 文件。源文件是唯一真相 | CF-016 | 🔴 |
| KF-016 | **规范更新同步门禁**：本手册更新后，受影响的 Lint 规则和质量门禁必须在同一 Sprint 内同步更新 | CF-017 | 🟠 |
| KF-017 | **新规则 1-Sprint 灰度**：新质量规则先在 warning 模式运行 1 个 Sprint，确认零误报后升级为阻断 | CF-019 | 🟡 |
| KF-018 | **禁止清单增量**：新增约束必须同时写入 AGENTS.md 禁止清单，并在 failure-modes.md 中有对应的失败模式 | — | 🟠 |

### 高密度素材专用（v1.1 新增，v1.2 修订）

| 编号 | 铁律 | 来源 | 严重度 |
|:----:|------|------|:------:|
| **KF-019** | **知识地图必须看原图**：提炼知识地图内容时，必须逐张打开原图分析视觉结构。不得仅依赖 OCR 文字提炼知识——OCR 丢失了空间层级、分组逻辑、阅读路径、视觉强调和留白含义 | 2026-05-10 审查发现 | 🔴 |
| **KF-020** | **source_refs 不得指向临时路径**：所有引用（图片、口述稿）的 `source_refs` 必须指向 `10_raw/sources/`（不可变源文件）。禁止指向 `00_inbox/`（临时暂存区）。enrich 前必须完成源文件归档 | 2026-05-10 审查发现 | 🔴 |
| **KF-021** | **Hub Page 不得搬运内容**：导航页（Hub Page）只写概览 + wiki-link 列表（<3000 字）。禁止将子卡内容复制到 Hub Page——子卡内容独立维护，Hub 只做导航 | v2.0 策略 | 🟠 |
| **KF-022** | **单次会话批量上限**：Builder 单次会话质量修复 ≤5 张卡，或 Hub Page 构建 ≤2 张。超过上限会导致 context overload 死锁 | F-KDO-012/F-KDO-015 | 🟠 |
| **KF-023** | **产出必须含行为锚点**（v1.4 新增）：每篇 article 或 capability 产出必须包含至少一个读者今晚能执行的动作——5 分钟内可启动、有可验证的成功指标。禁止"分享/关注/点赞"等无行为改变的 CTA。知识不转化为行为就是死知识 | F-KDO-016 | 🟠 |

🔴=必须（违反必出事故）| 🟠=重要（违规扣分）| 🟡=参考

---

## 七、防呆机制

对标 EC 的六大工业化防呆机制，KDO 定义六项防呆：

| # | EC 防呆 | KDO 防呆 | 说明 |
|:--:|---------|---------|------|
| 1 | 强制字段防呆 | **Frontmatter 必填校验** | `kdo lint` 检查 title/type/status/source_refs/created_at 必填 |
| 2 | 参考代码骨架 | **三步编译结构强制** | 知识卡片必须含 Condense / Critique / Synthesis 三个区块 |
| 3 | 禁止清单 | **AGENTS.md 禁止清单** | 7 项已造成事故的行为被明确禁止，每次事故后增量 |
| 4 | 契约输出标准化 | **Artifact 质量门** | Content/Code/Capability 三类 artifact 各有通过标准 |
| 5 | 失败模式库 | **失败模式库** | F-KDO-001~015 已入库，每次 Agent session 启动时必读 |
| 6 | — | **源文件路径防呆**（v1.1 新增） | `kdo lint` 检测 `source_refs` 是否含 `00_inbox/` 路径，发现即告警 |
| — | 环境锁定（EC 独有） | — | KDO 不适用（纯文本知识库无运行时环境依赖） |

### 7.1 新增防呆机制详解

**源文件路径防呆**：enrich 完成后，Architect 审查时逐条检查 `source_refs`：
- 图片引用 → 必须以 `10_raw/sources/` 开头（非 `00_inbox/`）
- 口述稿引用 → 必须指向 source 文件（非 inbox 临时 MD）
- 发现 `00_inbox/` 引用 → 退回 draft，不通过审查

**Visual Analysis 遗漏防呆**：审查时检查每张引用知识地图原图的卡片是否在 `## Visual Analysis` 节中有对应分析。遗漏 → 退回。

**Hub Page 大小防呆**：审查时检查 Hub Page 字数是否 <3000。超限 → 警告（可能搬运了子卡内容）。

---

## 八、失败模式库

对标 EC 的 14 种失败模式（F001-F014 + F033）。

KDO 失败模式库完整定义在 [[failure-modes.md]]，此处列出索引：

### 技术故障类（F-KDO-001~006）

| 编号 | 名称 | 严重度 | 状态 |
|:----:|------|:------:|:----:|
| F-KDO-001 | CJK regex 静默零返回 | 🔴 | 已知，无自动化防御 |
| F-KDO-002 | 非 .md 文件 ingest 静默跳过 | 🟠 | 已知，无自动化防御 |
| F-KDO-003 | state.json 覆盖写竞态 | 🔴 | 已修复代码 |
| F-KDO-004 | 错误工作目录执行 pipeline 命令 | 🟠 | 已知，无自动化防御 |
| F-KDO-005 | 过期 feedback 引用残留 | 🟡 | 已知，手动清理 |
| F-KDO-006 | 骨架页面 CJK 内容损毁 | 🟠 | 设计约束，手动绕过 |

### 知识质量类（F-KDO-007~011）

| 编号 | 名称 | 严重度 | 来源 |
|:----:|------|:------:|------|
| F-KDO-007 | 表层翻译式提炼 | 🟠 | 2026-05-08 审查——Condense 段把目录改写当浓缩 |
| F-KDO-008 | 虚假关联 | 🟡 | 2026-05-08 审查——Synthesis wikilink 自己或灌水关联 |
| F-KDO-009 | 无质疑接受 | 🟠 | 2026-05-08 审查——Critique 段"万能废话"三卡共用 |
| F-KDO-010 | 溯源断裂 | 🔴 | 2026-05-08 审查——source_refs 为空数组 |
| F-KDO-011 | 百科词条化 | 🟡 | 概念卡写成百科词条（定义+分类+特征），非三步编译 |

### 执行过载类（F-KDO-012）

| 编号 | 名称 | 严重度 | 来源 |
|:----:|------|:------:|------|
| F-KDO-012 | Builder 上下文过载死锁 | 🔴 | 2026-05-09——单次会话处理 ≥3 个独立任务或读取 ≥5 个规范文件 |

### 高密度素材专用（F-KDO-013~015，v1.2 修订）

| 编号 | 名称 | 严重度 | 来源 |
|:----:|------|:------:|------|
| **F-KDO-013** | **OCR-only 知识提炼** | 🔴 | 2026-05-10——只依赖 OCR 文字提炼知识地图，未打开原图分析视觉结构。丢失空间层级、分组逻辑、阅读路径等核心信息 |
| **F-KDO-014** | **源文件路径污染** | 🟠 | 2026-05-11——`source_refs` 指向 `00_inbox/` 临时路径而非 `10_raw/sources/`。inbox 文件可能被清理，导致溯源断裂 |
| **F-KDO-015** | **批量 enrich 上下文过载** | 🔴 | 2026-05-11——单次会话处理超量卡片（>5 张质量修复或 >2 张 Hub Page），每张需读取原图+口述稿，总上下文超过窗口容量导致死锁 |
| **F-KDO-016** | **知识产出无行为锚点**（v1.4 新增） | 🟠 | 2026-05-15——产出内容组织完善但读者读完没有任何可执行动作。CTA 为"分享/关注"或缺失。对标 AI 思维卡：知识不转化为今晚的行为就是死知识 |

### 失败模式入库协议

```
发现新模式
  → 分配编号 F-KDO-NNN
  → 写入 failure-modes.md（表现/根因/触发信号/防御/关联文件）
  → 更新本手册索引表
  → 更新 AGENTS.md 禁止清单（如涉及禁止行为）
  → 更新执行前自检清单
```

退役规则：当防御措施已自动化（如代码修复 + CI 门禁），将状态改为"已退役"而非删除。

---

## 九、模板系统

对标 EC「所有产出物从模板开始，不从空白页开始」。

### 9.1 模板目录结构

```
90_control/templates/
├── concept-card-full.md       # 知识卡片—完整版（8 区块）
├── concept-card-compact.md    # 知识卡片—精简版（3 区块）
├── hub-page.md                # Hub Page 导航页（v1.2 新增，5 区块）
├── artifact-article.md        # 文章类 artifact
├── artifact-capability.md     # 能力/工作流类 artifact
├── delivery-record.md         # 发布记录
├── improvement-plan.md        # 改进计划
└── revision-record.md         # 修订记录
```

### 9.2 三级知识卡片模板

| 级别 | 适用场景 | 区块 |
|------|---------|------|
| **完整版（8 区块）** | 深度分析、方法论文章、核心概念 | Summary → Condense → Critique → Synthesis → 知识体系定位 → 跨学科锚点 → Open Questions → Output Opportunities |
| **精简版（3 区块）** | 快讯、小结、操作指南、轻量概念 | Summary → Condense → Critique |
| **Hub Page（5 区块）**（v1.2 新增） | 导航页——串联散卡，提供模块概览 | 概览 → 核心概念（wiki-link 列表）→ 知识体系定位 → Critique（针对模块整体）→ Synthesis（链接模块外概念） |

Hub Page 模板详情见 [[high-density-composite-compilation-strategy]] §Hub Page 模板。

### 9.3 模板使用规则

- **起点非约束**：模板作为 `kdo produce` 的初始化起点，创建后 Agent 可以增删改区块
- **唯一硬性约束**：核心 frontmatter 字段（title/type/status/source_refs/created_at）不可删
- **Hub Page 硬性约束**：字数 <3000 字，禁止复制子卡完整内容。只写概览 + wiki-link 导航
- `kdo produce` 时从模板初始化

---

## 十、反馈闭环

对标 EC 的监控告警系统（告警分级 → 聚合 → 闭环）。

### 10.1 反馈分级

| 级别 | 触发条件 | 处理 SLA |
|:----:|---------|---------|
| **P0** | broken link、source_refs 为空、source_refs 指向 00_inbox/、status 不一致 | 下次 enrich 前解决 |
| **P1** | missing tag、Critique 万能废话、举证缺失、Visual Analysis 遗漏 | 下个 produce 前解决 |
| **P2** | style 问题、裸 URL、字数不足 | 下个 ship 前解决 |

### 10.2 闭环流程

```
kdo feedback triage（合并去重积压 feedback）
  → improvement plan（生成改进计划到 30_wiki/decisions/）
  → revision（黄药师执行修正）
  → verify（Architect 复审关闭）
```

### 10.3 关键命令

- `kdo feedback triage`：读取所有 pending `fb_*`，去重后合并为 ≤10 条 actionable issues
- `kdo improve --apply`：应用改进计划中的自动修复项
- `kdo lint --strict`：验证修复结果

---

## 十一、技术笔记：平台的坑

以下问题已在 KDO 源码层面修复，但值得记录以防止回退。

### 11.1 parse_frontmatter BOM/CRLF 处理

**事故**：2026-05-10，PowerShell `Out-File -Encoding utf8` 产生的文件带 UTF-8 BOM（`﻿`）和 CRLF 行尾，导致 `parse_frontmatter()` 无法识别 `---` frontmatter 分隔符。第一轮 ingest 产生的 128 个 wiki 骨架标题全部是垃圾（取了 transcript 正文第一行）。

**根因**：Python 的 `str.startswith("---\n")` 在 `\r\n` 和 `﻿` 面前失效。

**修复**（`kdo/workspace.py`）：
```python
def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    text = text.replace('\r\n', '\n')          # Windows CRLF → LF
    if text.startswith('﻿'):              # UTF-8 BOM
        text = text[1:]
    if not text.startswith("---\n"):
        return {}, text
    # ...
```

**教训**：Windows + PowerShell + Python 的组合下，BOM/CRLF 是默认潜伏的坑。任何文本解析器在处理来自 PowerShell 的文件时，必须在入口处做这两步处理。

---

## 十二、Agent 原生知识卡编译规范（v1.3）

本章从 [[agent-native-card-design]] 和 [[high-density-composite-compilation-strategy]] v2.0 提取可执行的规则和标准。

> **v1.0 的复合编译方案（合并为大卡）已被废弃**。v1.3 起，所有知识卡片按 agent-native 格式编译。详细的 frontmatter 规范和 body 结构见 [[agent-native-card-design]]。本章只提取可执行的规则部分。

### 12.1 核心架构：分层知识图谱

```
         ┌─────────────────────────────┐
         │  composite-concept (1-2张)   │  ← 方法论顶层（10-15 claims）
         │  泛产品设计方法论             │
         └──────────┬──────────────────┘
                    │ component_of
         ┌──────────┼──────────────────┐
         ▼          ▼                  ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │framework │ │framework │ │framework │  ← 工具箱层（10-15 claims）
   │需求工具箱 │ │审美工具箱 │ │落地工具箱 │
   └─────┬────┘ └────┬─────┘ └─────┬────┘
         │ related   │ related     │ related
    ┌────┴───┐  ┌────┴───┐   ┌────┴───┐
    ▼        ▼  ▼        ▼   ▼        ▼
  [tool] [tool] ...    ...   ...    ...  ← 单张知识地图（3-10 claims）
```

**原则**：
1. 单张知识地图 → type: `tool`（细粒度节点）
2. 知识地图集群 → type: `framework`（工具箱级聚合）
3. 方法论顶层 → type: `composite-concept`（不超过 1-2 张，控制体量）
4. 导航靠 frontmatter 图边（`component_of`/`related`），不需要单独的 Hub Page

### 12.2 质量标准

按 card type 分层：

| type | Claims | Visual Analysis | Constraints | 行数 |
|------|:--:|:--:|:--:|:--:|
| `composite-concept` | 10-15（不超 30） | 每张嵌入原图 | ≥1 boundary claim | ≤500 |
| `framework` | 5-15 | 同 | ≥1 boundary claim | ≤300 |
| `case` | 5-10 | 如有原图 | ≥1 boundary claim | ≤200 |
| `tool` | 3-10 | 如有原图 | ≥1 boundary claim | ≤150 |

所有卡片共通：kdo lint 0 warning / source_refs → 10_raw/ / query_triggers ≥3 / frontmatter 图边非空。方法/工具/框架卡另须含外部攻击子节 + 不要用场景表 + Action Triggers 节（§1.7），概念卡和索引卡豁免。

### 12.3 禁止事项

- ❌ 不要将多张知识地图合并为超过体量上限的巨卡
- ❌ 不要只依赖 OCR 文字——必须打开原图分析视觉结构
- ❌ source_refs 不要指向 `00_inbox/`（KF-020）
- ❌ 不要跳过 Constraints 或 Visual Analysis
- ❌ 单次会话升级 ≤5 张 framework 或 ≤2 张 composite-concept（KF-022）

详细 frontmatter 规范和 body 模板见 [[agent-native-card-design]]。

---

## 附录 A：相关控制文件索引

| 文件 | 用途 | 与本手册关系 |
|------|------|------------|
| [[AGENTS.md]] | Agent 行为规则 + 禁止清单 | 禁止清单由本手册铁律 KF-003 驱动 |
| [[debate-protocol.md]] | Architect/Builder 协作协议 | 实现本手册角色体系的日常协作 |
| [[failure-modes.md]] | 失败模式库（F-KDO-001~015） | 本手册 §八 的详细展开 |
| [[operating-principles.md]] | 知识库运作原则 | 原则层的补充，本手册是规则层 |
| [[agent-native-card-design]] | Agent 原生知识卡设计规范 | 本手册 §十二 的 frontmatter 和 body 模板来源 |
| [[corrections.md]] | 已验证的错误与修正 | 事故库，本手册技术笔记的来源 |

## 附录 B：实施路线图

| Sprint | 内容 | 验收标准 | 状态 |
|:------:|------|---------|:----:|
| **Sprint 1** | L1 Lint 扩展（source_refs 存在性 + status 一致性） + 修复 broken wikilinks | `kdo lint` 在现有 vault 上跑出 0 broken links | ✅ 已完成 |
| **Sprint 2** | 门禁系统（P0 警告 + override）+ enrich 节点举证 | 一张新概念卡走完 ingest→enrich 并留下举证记录 | ✅ 已完成 |
| **Sprint 3** | L2 内容质量检查（警告级）+ `kdo feedback triage` | 56 条积压合并为 ≤10 条 actionable issues | ✅ 已完成 |
| **Sprint 4** | 模板系统 + pre-commit hook | 模板就位，hook 可用 | ⏳ 待启动 |
| **Sprint 5**（v1.3） | Agent-native 格式落地——composite-concept #1 + 6 张 framework 卡升级 | 1 张 composite-concept + 6 张 framework 通过 agent-native 质量门禁 | ⏳ 黄药师执行中 |
| **Sprint 6** | 33 张 tool 卡批量修复（source_refs + type 重分类） + Visual Analysis 补全 | 33 张 tool 卡 source_refs → 10_raw/ + type 修正 | ⬜ |
| **Sprint 7+** | L1 source_refs 路径检查自动化、Graph RAG 索引接入 | `kdo lint` 自动检测 00_inbox/ 引用 | ⬜ |

## 附录 C：术语对照

| EC 工业化规范 | 内容工厂工业化规范 | 差异说明 |
|-------------|--------------|---------|
| EC 卡（Execution Card） | 知识卡片（Concept Card） | EC 卡是代码作业指导书，KDO 卡是知识编译单元 |
| 三层质量防护 | 三层 Lint 规则（L1/L2/L3） | 同构，适应知识生产领域调整阈值 |
| 六大防呆 | 六项防呆 | 去掉"环境锁定"，增加"源文件路径防呆"和"体量上限防呆" |
| 四角色循环 | 三角色分工 + Agent-in-the-loop | 去掉测试者角色，增加多模态 Agent 辅助模式 |
| 14 种失败模式 | 15 种失败模式（6 技术 + 5 知识质量 + 1 执行过载 + 3 高密度素材） | KDO 增加知识质量类、执行过载类和高密度素材专用类 |
| Stage Gate（阶段门禁） | 管线阶段门禁（标准 + 高密度素材 enrich 变体） | 同构，增加细粒度质量达标 + Hub Page 构建子流程 |
| CF-001~020 铁律 | KF-001~022 铁律 | 18 条对标 + 4 条 KDO 新增（KF-019~022） |
| 只测不修 | 审而不改 | 完全同构 |
| — | **Agent 原生设计** | KDO 独有：卡片是知识图谱节点，结构化 frontmatter + Claims + 图边 |
| — | **Visual Analysis 方法论** | KDO 独有：知识地图五维视觉结构分析 |

## 附录 D：版本历史

| 日期 | 版本 | 变更 | 作者 |
|------|------|------|------|
| 2026-05-09 | 1.0 | 初版——从 EC 工业化规范手册 v2.8.0 迁移核心框架到 KDO 知识生产领域 | 欧阳锋 |
| 2026-05-11 | 1.1 | 手册更名、复合编译哲学、Visual Analysis、KF-019~022、F-KDO-013~015、技术笔记 | 欧阳锋 |
| 2026-05-11 | 1.2 | 废弃复合编译，转向细粒度+导航层架构（被 v1.3 取代） | 欧阳锋 |
| 2026-05-11 | 1.3 | **Agent-native 标准落地**——采纳 [[agent-native-card-design]]：frontmatter 图边、Claims [conf=X][src]、query_triggers、estimated_tokens。废弃 Hub Page。新增 §1.6 Agent 原生设计。更新 L2 门禁和 §十二 | 欧阳锋 |
| 2026-05-15 | 1.4 | **行为转化层 + EVIDENCE 审计**——对标 AI 思维卡「认知升级系统 v3.2」方法论：新增 §1.6 知识生产目标=行为改变、ACTION 锚点写入 P0 门禁（KF-023）、EVIDENCE 审计标准（偏差标注+外部攻击+反事实）、Burn line、F-KDO-016 | 欧阳锋 |
| 2026-05-15 | 1.5 | **卡片层行为转化三要件**——黄药师 AI 思维卡分析建议经欧阳锋裁决采纳：新增 §1.7（Critique 外部攻击子节 + Synthesis 不要用场景表 + Action Triggers 节），适用方法/工具/框架卡。新增 KF-024 铁律。更新 L2 门禁规则。概念卡和索引卡豁免 | 欧阳锋 |
| 2026-05-16 | 1.6 | **三要件执行质量标准 + 回溯升级节奏**——Sprint 12 Batch A（25 张 framework 卡）审查后迭代：§1.7 要件 1 补充外部攻击引证启发法（按领域→反方法化学者映射表）；要件 2 补充不要用场景质量三信号（场景具体性/失效因果/替代指名）；要件 3 补充成功指标三种可验证模式（数量型/时间型/频率型）和 5 分钟可启动测试；新增 §1.9 批量回溯升级执行节奏（≤5 张/轮 + lint + 审查抽检 20%） | 欧阳锋 |

---

> **维护规则**：本手册由 Architect（欧阳锋）维护。变更须经用户批准（KF-001）。每次变更后在附录 D 记录版本历史。所有积累的经验必须迭代合并到本手册——这是 Architect 的主要职责之一。
