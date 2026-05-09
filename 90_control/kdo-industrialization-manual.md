---
title: "KDO 工业化规范手册"
type: "control"
status: "stable"
version: "1.0"
created_at: "2026-05-09"
updated_at: "2026-05-09"
author: "欧阳锋"
source: "EC工业化规范手册 v2.8.0 → KDO 领域迁移"
supersedes: []
based_on:
  - "[[EC工业化规范手册]]"
  - "[[ec工业化规范手册-v2.8.0]]"
  - "[[kdo-ec-industrialization-migration-proposal]]"
---

# KDO 工业化规范手册 v1.0

> **定位**：KDO 知识生产管线的工业化操作标准——将知识萃取、编译、交付过程升级为可重复、可审计、防呆的标准化流程。
> **编制**：欧阳锋（Architect）| 初版 2026-05-09
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

唯一的例外：Architect 可以直接修改 `90_control/` 下的控制文件（本手册、PROTOCOL.md、failure-modes.md 等），因为这些是 Architect 的职责域。

### 1.3 失败模式从事故事实中生长

对标 EC 手册 §13 的 14 种失败模式（F001-F014）——全部来自真实事故，没有一条是坐在房间里提前设计的。

KDO 操作原则：**每踩一次坑 → 入库一种模式 → 更新 Lint 规则 → 更新禁止清单**。不提前设计「可能出什么问题」的框架。失败模式库（`90_control/failure-modes.md`）从血泪中生长，不是从想象中构建。

---

## 二、角色体系

对标 EC 的四角色循环（设计者/协调者/开发者/测试者），KDO 采用三角色分工：

| 角色 | 对标 EC | 职责 | 红线 |
|------|---------|------|------|
| **用户（老朱）** | 设计者 + 协调者 | 定方向、定优先级、定角度、终决拍板 | 不参与内部辩论细节 |
| **Architect（欧阳锋）** | 审查者 | 设计规则、审查产出、维护门禁、裁决例外、记录决策 | **审而不改**——不直接编辑黄药师的产出文件 |
| **Builder（黄药师）** | 开发者 | 执行流水线、高质量内容提炼、KDO 开发 | 不主动发起架构讨论，有问题报给 Architect |

**协作协议**：完整定义在 [[debate-protocol.md]]。核心原则——Architect + Builder 的辩论不消耗用户注意力。达成共识的事项直接执行。辩论升级到用户时压缩为 ≤3 选项的选择题。

**唯一信息枢纽**：对标 EC 的协调者中枢，KDO 的协调者是**文件系统本身**——Architect 和 Builder 在同一文件中 append 辩论，用户通过 Obsidian 查看。不需要人工转发。

---

## 三、管线阶段门禁

对标 EC 的 Stage Gate 体系。每个管线阶段有进入条件和退出标准（门禁）。

| 阶段 | 进入条件 | 退出标准（门禁） | 门禁级别 |
|------|---------|----------------|:------:|
| **ingest** | 文件在 `00_inbox/` | `source_refs` 已写入 frontmatter，skeleton 已创建，`log.md` 已记录 | P0 警告 |
| **enrich** | source `status: draft` | 三步编译完成，`status: enriched`，frontmatter 字段齐全，source_refs 非空 | **P0 阻断** |
| **produce** | ≥1 个 concept `status: enriched` | artifact frontmatter 完整，非 stub，通过 validate | P0 警告 |
| **validate** | artifact `status: draft` | L1 全通过，broken links = 0，`fb_*` 已生成 | P0 警告 |
| **ship** | artifact `status: validated` | 发布目标明确（article/local/test），`ship_*` 已写入 | P0 警告 |

**门禁阻断规则**（EC 决策第 1 条）：
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
| `source_refs` 指向的文件存在（非 broken wikilink） | 🔴 P0 | ❌ 待实现（Sprint 1） |
| `status` 值与管线阶段一致（draft/enriched/validated/shipped） | 🔴 P0 | ❌ 待实现（Sprint 1） |
| 无裸 URL（链接必须用 markdown 或 wikilink） | 🟡 P2 | ❌ 待实现 |

### L2 — 内容质量（对标单元测试）

| 规则 | 严重度 | 阈值 |
|------|:------:|------|
| Condense 有实质性内容（非 "TBD" 或空段落） | 🟠 P1 | ≥3 条核心结论 |
| Critique ≥ 1 条，且至少一条**指名具体假设或边界** | 🟠 P1 | 禁止"需要更多验证"式万能废话 |
| Synthesis 有 ≥ 2 个 wikilinks（允许含 index 页） | 🟡 P2 | — |
| 全文 > 500 字 | 🟡 P2 | — |

L2 全部为**警告级别**，不做阻断。

**Critique 质量底线**（EC 决策第 2 条）：至少一条 Critique 必须指名具体假设或边界——「这门方法论的 XX 前提在 YY 场景下不成立」——而非「需要更多验证」「目录层级有限」等万能废话。

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
| **produce** | ✅ 强制 | artifact 正文 + gate 通过日志 | 三节点之一 |
| **validate** | — | lint 报告即为举证，不另要求 | — |
| **ship** | ✅ 强制 | 发布目标 + 时间戳 + 版本号 | 三节点之一 |
| **ingest** | — | 机械化操作（cp + frontmatter 注入），不需举证 | — |

**举证粒度原则**（EC 决策第 3 条）：仅 enrich/produce/ship 三个关键节点强制举证。enrich 举证为变更摘要而非完整 diff——完整 diff 在概念卡质量审查时噪音太大。

---

## 六、铁律

对标 EC 的 20 条核心铁律（CF-001~020），定义 KDO 工业化铁律（KF-001~018）。

### 设计阶段

| 编号 | 铁律 | 对标 EC | 严重度 |
|:----:|------|:------:|:------:|
| KF-001 | **核心规范双重签发**：本手册和 PROTOCOL.md 的变更须 Architect 提案 + 用户批准 | CF-020 | 🔴 |
| KF-002 | **PROTOCOL.md 优先原则**：任何单次操作指令不得与 PROTOCOL.md 冲突。如有冲突，先更新 PROTOCOL.md | CF-002 | 🔴 |
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

🔴=必须（违反必出事故）| 🟠=重要（违规扣分）| 🟡=参考

---

## 七、防呆机制

对标 EC 的六大工业化防呆机制，KDO 定义五项防呆：

| # | EC 防呆 | KDO 防呆 | 说明 |
|:--:|---------|---------|------|
| 1 | 强制字段防呆 | **Frontmatter 必填校验** | `kdo lint` 检查 title/type/status/source_refs/created_at 必填 |
| 2 | 参考代码骨架 | **三步编译结构强制** | 知识卡片必须含 Condense / Critique / Synthesis 三个区块 |
| 3 | 禁止清单 | **AGENTS.md 禁止清单** | 6 项已造成事故的行为被明确禁止，每次事故后增量 |
| 4 | 契约输出标准化 | **Artifact 质量门** | Content/Code/Capability 三类 artifact 各有通过标准（见 PROTOCOL.md §6） |
| 5 | 失败模式库 | **失败模式库** | F-KDO-001~011 已入库，每次 Agent session 启动时必读 |
| — | 环境锁定（EC 独有） | — | KDO 不适用（纯文本知识库无运行时环境依赖） |

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

### 知识质量类（F-KDO-007~011）⚠️ 待入库

| 编号 | 名称 | 严重度 | 来源 |
|:----:|------|:------:|------|
| F-KDO-007 | 表层翻译式提炼 | 🟠 | 2026-05-08 审查——Condense 段把目录改写当浓缩 |
| F-KDO-008 | 虚假关联 | 🟡 | 2026-05-08 审查——Synthesis wikilink 自己或灌水关联 |
| F-KDO-009 | 无质疑接受 | 🟠 | 2026-05-08 审查——Critique 段"万能废话"三卡共用 |
| F-KDO-010 | 溯源断裂 | 🔴 | 2026-05-08 审查——source_refs 为空数组 |
| F-KDO-011 | 百科词条化 | 🟡 | 概念卡写成百科词条（定义+分类+特征），非三步编译 |

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
├── artifact-article.md        # 文章类 artifact
├── artifact-capability.md     # 能力/工作流类 artifact
├── delivery-record.md         # 发布记录
├── improvement-plan.md        # 改进计划
└── revision-record.md         # 修订记录
```

### 9.2 两级知识卡片模板

| 级别 | 适用场景 | 区块 |
|------|---------|------|
| **完整版（8 区块）** | 深度分析、方法论文章、核心概念 | Summary → Condense → Critique → Synthesis → 知识体系定位 → 跨学科锚点 → Open Questions → Output Opportunities |
| **精简版（3 区块）** | 快讯、小结、操作指南、轻量概念 | Summary → Condense → Critique |

完整版模板 = 三步编译法 + 知识体系定位 + 跨学科锚点 + 输出机会。精简版模板 = 三步编译法最小集。

### 9.3 模板使用规则

- **起点非约束**（EC 决策第 4 条）：模板作为 `kdo produce` 的初始化起点，创建后 Agent 可以增删改区块
- **唯一硬性约束**：核心 frontmatter 字段（title/type/status/source_refs/created_at）不可删
- `kdo produce` 时自动从模板初始化

---

## 十、反馈闭环

对标 EC 的监控告警系统（告警分级 → 聚合 → 闭环）。

### 10.1 反馈分级

| 级别 | 触发条件 | 处理 SLA |
|:----:|---------|---------|
| **P0** | broken link、source_refs 为空、status 不一致 | 下次 enrich 前解决 |
| **P1** | missing tag、Critique 万能废话、举证缺失 | 下个 produce 前解决 |
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

## 附录 A：相关控制文件索引

| 文件 | 用途 | 与本手册关系 |
|------|------|------------|
| [[PROTOCOL.md]] | KDO 管线操作协议 | 本手册是 PROTOCOL.md 的工业化增强层 |
| [[AGENTS.md]] | Agent 行为规则 + 禁止清单 | 禁止清单由本手册铁律 KF-003 驱动 |
| [[debate-protocol.md]] | Architect/Builder 协作协议 | 实现本手册角色体系的日常协作 |
| [[failure-modes.md]] | 失败模式库（F-KDO-001~011） | 本手册 §八 的详细展开 |
| [[operating-principles.md]] | 知识库运作原则 | 原则层的补充，本手册是规则层 |

## 附录 B：实施路线图

| Sprint | 内容 | 验收标准 | 状态 |
|:------:|------|---------|:----:|
| **Sprint 1** | L1 Lint 扩展（source_refs 存在性 + status 一致性） + 修复 broken wikilinks | `kdo lint` 在现有 vault 上跑出 0 broken links | ⏳ 待启动 |
| **Sprint 2** | 门禁系统（P0 警告 + override）+ enrich 节点举证 | 一张新概念卡走完 ingest→enrich 并留下举证记录 | ⬜ |
| **Sprint 3** | L2 内容质量检查（警告级）+ `kdo feedback triage` | 56 条积压合并为 ≤10 条 actionable issues | ⬜ |
| **Sprint 4** | 模板系统 + pre-commit hook | 模板就位，hook 可用 | ⬜ |
| **Sprint 4+** | 变更影响分析、enrich 双模策略 | 按需推进 | ⬜ |

## 附录 C：术语对照

| EC 工业化规范 | KDO 工业化规范 | 差异说明 |
|-------------|--------------|---------|
| EC 卡（Execution Card） | 知识卡片（Concept Card） | EC 卡是代码作业指导书，KDO 卡是知识编译单元 |
| 三层质量防护 | 三层 Lint 规则（L1/L2/L3） | 同构，适应知识生产领域调整阈值 |
| 六大防呆 | 五项防呆 | 去掉"环境锁定"（KDO 无运行时环境） |
| 四角色循环 | 三角色分工 | 去掉测试者角色（知识生产无独立测试阶段） |
| 14 种失败模式 | 11 种失败模式（6 技术 + 5 知识质量） | KDO 增加知识质量类失败模式 |
| Stage Gate（阶段门禁） | 管线阶段门禁 | 同构，KDO 用强警告替代硬阻断 |
| CF-001~020 铁律 | KF-001~018 铁律 | 16 条直接对标 + 2 条 KDO 新增 |
| 只测不修 | 审而不改 | 完全同构 |

---

## 附录 D：版本历史

| 日期 | 版本 | 变更 | 作者 |
|------|------|------|------|
| 2026-05-09 | 1.0 | 初版——从 EC 工业化规范手册 v2.8.0 迁移核心框架到 KDO 知识生产领域 | 欧阳锋 |

---

> **维护规则**：本手册由 Architect（欧阳锋）维护。变更须经用户批准（KF-001）。每次变更后在附录 D 记录版本历史。
