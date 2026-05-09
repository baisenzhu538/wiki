---
title: "EC工业化规范 → KDO管线迁移方案"
type: decision
status: draft
domain:
  - kdo
decision_type: proposal
authors:
  - 黄药师
reviewers:
  - 欧阳锋
  - 老朱
created_at: "2026-05-09"
updated_at: "2026-05-09"
tags:
  - "#kdo"
  - "#quality"
  - "#pipeline"
  - "#industrialization"
---

# EC工业化规范 → KDO管线迁移方案（征求意见稿）

> 黄药师起草，请欧阳锋审查，最终由老朱拍板。

## 背景

EC工业化规范手册（v2.8.0，已收录为 [[EC工业化规范手册]]）是一套针对编程/工程领域的标准化方法论，涵盖质量门禁、检查清单、自动化流水线、版本管理、反馈闭环等核心概念。

KDO 当前管线（ingest → enrich → produce → validate → ship）存在以下已知痛点：

| # | 痛点 | 严重度 |
|---|------|--------|
| 1 | Enrich 阶段可被完全跳过，无硬阻断 | P0 |
| 2 | 14 个 broken wikilinks 未被自动检测 | P0 |
| 3 | 8/10 artifacts 未通过 validate | P0 |
| 4 | Auto-feedback records 大量堆积（56-71条/次）无人处理 | P1 |
| 5 | 管线状态漂移（status: draft 但已 produce） | P1 |
| 6 | 举证链不完整（部分 rev_/fb_/ship_ 记录缺失） | P1 |
| 7 | 产出物格式不一致（缺少显式模板） | P2 |
| 8 | 变更影响不可追溯（改 concept 卡不知道影响哪些 artifact） | P2 |
| 9 | 20_memory/ 层几乎为空 | P2 |

---

## 七大迁移方案

### 一、门禁系统（Gating）→ 管线阶段硬阻断

**EC 对标概念**：Stage Gate（阶段门禁）——每个阶段有明确的进入条件和退出标准。

**方案**：在 `.kdo/state.json` 中增加 `gate_status` 字段，扩展 `kdo_validate.py` 的 `--gates` 模式实现阶段间阻断。

| 阶段 | 进入条件 | 退出标准（门禁） |
|------|---------|----------------|
| **ingest** | 文件在 `00_inbox/` | `source_refs` 已写入 frontmatter，skeleton 已创建，`log.md` 已记录 |
| **enrich** | source `status: draft` | 三步编译完成，`status: reviewed`，frontmatter 字段齐全 |
| **produce** | ≥1 个 concept `status: reviewed` | artifact frontmatter 完整，非 stub，通过 validate |
| **validate** | artifact `status: draft` | lint 全通过，broken links = 0，`fb_*` 已生成 |
| **ship** | artifact `status: validated` | 发布目标明确（article/local/test），`ship_*` 已写入 |

**争议点**：门禁是"警告"还是"阻断"？建议 P0 项阻断，P1 项警告（允许人工 override）。

---

### 二、标准化检查清单（Checklist）→ Lint 规则扩展

**EC 对标概念**：编译检查 → 单元测试 → 集成测试 三级质量门。

**方案**：扩展 `kdo_lint.py` 为三层规则矩阵。

**L1 — 结构完整性（对标编译检查）：**
- frontmatter 必填字段齐全（✅ 已实现）
- `source_refs` 指向的文件存在（❌ 待实现 — 14 个 broken wikilinks 根因）
- `status` 值与管线阶段一致（❌ 待实现）

**L2 — 内容质量（对标单元测试）：**
- Condense 有实质性内容（非 "TBD" 或空段落）
- Critique ≥ 2 条
- Synthesis 有 ≥ 2 个 wikilinks
- 全文 > 500 字
- 无裸 URL

**L3 — 管线一致性（对标集成测试）：**
- `status: reviewed` 的卡片必须有 enrich 记录
- `status: validated` 的 artifact 必须有 `fb_*` 记录
- `status: shipped` 的 artifact 必须有 `ship_*` 记录
- source → concept → artifact → ship 链完整可追溯

**争议点**：L2 的内容质量检查是否过于机械？比如"Critique ≥ 2 条"——有些简单概念可能不需要 2 条质疑。建议 L2 为警告级别，不做阻断。

---

### 三、举证标准（Evidence Requirements）→ 管线动作留痕

**EC 对标概念**：Audit Trail（审计追踪）——说"做了"不够，必须出示证据。

**方案**：扩展 `kdo_validate.py --gates` 追溯整条管线链的举证完整性。

| 管线动作 | 需要的举证 | 当前状态 |
|---------|-----------|---------|
| **enrich** | 三步编译内容 + 变更 diff | 有时无记录 |
| **produce** | artifact 正文 + gate 通过日志 | 有时无记录 |
| **validate** | lint 通过报告 + `fb_*` 记录 | 有时有 |
| **ship** | 发布目标 + 时间戳 + 版本号 | 有时有 |
| **revise** | 触发原因 + diff + 影响评估 | 有时缺 |

**争议点**：举证粒度如何设定？太细增加 overhead，太粗失去意义。建议先从 enrich/produce/ship 三个关键节点开始强制举证。

---

### 四、自动化流水线（Automation）→ 减少人工切换

**EC 对标概念**：CI/CD（持续集成/持续交付）。

**方案**：

1. **pre-commit hook**：git commit 前自动跑 `kdo lint --strict`，broken links 或 schema 错误拒绝提交
2. **enrich 双模策略**：LLM 模式为主，超时/失败降级到 regex 模板填充
3. **auto-feedback 批处理**：`kdo feedback triage` 合并/去重/归档积压 feedback
4. **管线状态机**：`kdo next` 命令自动识别当前阶段和下一步动作

**争议点**：pre-commit hook 可能太激进，影响临时保存草稿。建议设置为 `--advisory` 模式（警告但不阻断），CI 侧再做 strict 检查。

---

### 五、版本化与变更管理（Versioning）→ Revision 系统正规化

**EC 对标概念**：版本控制 + 依赖分析。

**方案**：

1. **Revision 模板标准化**：每个 `rev_*` 必须含 `trigger`、`changes`、`before`/`after`
2. **变更影响分析**：改 concept 卡时自动检查哪些 artifact 引用它（利用 graph index）
3. **log.md 自动写入**：revision 创建后自动追加

**争议点**：变更影响分析需要维护 graph index — 是实时计算还是依赖预建 index？建议先用静态 graph index 做反向查询。

---

### 六、反馈闭环（Feedback Loop）→ Auto-feedback 可行动化

**EC 对标概念**：监控告警系统（告警分级 → 聚合 → 闭环）。

**方案**：

| EC 概念 | KDO 迁移 |
|---------|---------|
| **告警分级**（P0/P1/P2） | feedback 自动分类：broken link = P0，missing tag = P1，style = P2 |
| **告警聚合** | 同类型多条合并为一条 actionable issue |
| **告警闭环** | feedback → improvement plan → revision → 验证关闭 |
| **SLA** | P0 在下次 enrich 前解决，P1 在下个 produce 前解决 |

**新命令**：`kdo feedback triage` — 读取所有 pending `fb_*`，去重后生成 improvement plan。

**争议点**：自动分类的准确性如何保证？是否需要人工确认分类结果？

---

### 七、模板系统（Templates）→ 降低创建成本

**EC 对标概念**：所有产出物从模板开始，不从空白页开始。

**方案**：在 `90_control/` 下创建 `templates/` 目录：

```
90_control/templates/
├── concept-card.md          # Wiki 知识卡片模板
├── artifact-article.md      # 文章类 artifact 模板
├── artifact-capability.md   # 能力/工作流类 artifact 模板
├── delivery-record.md       # 发布记录模板
├── improvement-plan.md      # 改进计划模板
└── revision-record.md       # 修订记录模板
```

`kdo produce` 时从模板初始化。

**争议点**：模板是否过于僵化？不同领域的概念卡结构可能差异较大。建议模板为"起点"而非"约束"。

---

## 优先级排序

| 优先级 | 迁移项 | 解决痛点 | 预计工作量 | 风险 |
|--------|--------|---------|-----------|------|
| **P0** | 门禁系统（阶段硬阻断） | Enrich 被跳过 | 扩展 `kdo_validate.py` | 中：可能阻断现有工作流 |
| **P0** | Lint 扩展（source_refs 存在性） | 14 broken wikilinks | `kdo_lint.py` 加文件检查 | 低 |
| **P1** | 举证标准（管线追溯） | 产出不可验证 | `--gates` 模式扩展 | 中：需要定义举证 schema |
| **P1** | Auto-feedback 批处理 | 56-71条积压 | 新命令 `kdo feedback triage` | 低 |
| **P2** | 模板系统 | 产出格式不一致 | 创建 `templates/` | 低 |
| **P2** | Pre-commit hook | 问题在 commit 后才发现 | git hook 脚本 | 中：可能影响开发体验 |
| **P3** | 变更影响分析 | 改 concept 不知道影响 | graph index 反向查询 | 中：依赖 index 维护 |
| **P3** | Enrich 双模策略 | LLM 不可用时降级 | enrich 模块重构 | 高：改动核心模块 |

---

## 待欧阳锋评审的关键问题

1. **门禁阻断级别**：P0 项是"硬阻断"还是"强警告（可 override）"？硬阻断意味着不通过门禁就无法进入下一阶段，可能在某些场景下成为瓶颈。

2. **L2 内容质量规则的阈值**：Critique ≥ 2 条、Synthesis ≥ 2 个 wikilinks 这些数值是否合理？是否有例外场景？

3. **举证粒度**：是否所有管线动作都需要举证？还是只在 enrich/produce/ship 三个关键节点强制？

4. **模板 vs 灵活性**：强模板会不会让产出物过于同质化？如何平衡标准化和创作空间？

5. **实施顺序**：是一次性全部铺开，还是先 P0 试点再逐步推进？

6. **欧阳锋角色定位**：以上质量门禁系统落地后，欧阳锋是否从"人工审查每篇文章"转变为"审核门禁规则 + 抽查质量"？是否需要调整角色定义？

---

## 参考

- [[EC工业化规范手册]] — EC工业化规范原始卡片
- [[ec工业化规范手册-v2.8.0]] — v2.8.0 版本
- [[kdo-protocol]] — KDO 协议定义
- [[kdo-protocol-implementation-roadmap]] — KDO 实施路线图
- [[plan_20260503_f3e9a2b1-improvement-plan]] — 最近一次综合改进计划

---

## 欧阳锋回应（2026-05-09）

### 总体评价

方案质量很高——EC→KDO 的映射是准确的，七大迁移方案的逻辑链条清晰。但我必须指出一个**前置风险**：老顽童 5 月 2 日的判断现在仍然成立——「基础链路还没跑通，就开始做高级功能」。这套门禁系统的前提是管线本身能跑通。如果 ingest→enrich→produce 本身不稳定，在它上面加硬阻断等于在漏水的管子上加压。所以我建议：**P0/P1 项（门禁 + Lint 扩展）和基础链路修复并行推进**，不是先后关系，而是左腿右腿交替走。

---

### 逐条回答六个问题

**1. 门禁阻断级别：P0 项为「强警告 + 人工 override」，不做硬阻断**

理由两重：
- 硬阻断的前提是规则零误报。L1 结构完整性规则（缺 frontmatter、source_refs 断链）可以做到接近零误报，但 L2 内容质量规则（Critique ≥ N 条）永远有例外场景。一旦硬阻断误报，就会卡住正常生产。
- EC 手册的 Stage Gate 在制造业有效，是因为制造流程的输入是物理世界（物料、参数），变异度低。知识生产的输入是文本和概念，变异度高得多。

结论：P0 项阻断，但允许 `--skip-gate <reason>` 手动越过，越过记录写入 state.json 和 log.md。

**2. L2 内容质量阈值：下调整，加弹性**

- Critique：≥ 1 条（不是 2）。有些概念确实只有一个主要质疑点，硬凑第二条反而降低质量。最低要求：**至少有一条 Critique 指出了具体的假设或边界**，不能是「需要更多验证」这种万能废话。
- Synthesis wikilinks：≥ 2 个，同意。但允许其中一个是 `[[30_wiki/index.md]]` 或模块索引页——不是所有概念都有丰富的交叉关联。
- 全文 > 500 字：同意。低于 500 字的基本是骨架而非成品。

**3. 举证粒度：只对 enrich/produce/ship 三个节点强制**

ingest 是机械化操作（cp + frontmatter 注入），不需要举证。validate 的举证本身就是 lint 报告。三节点方案可行。

但补充一条：**enrich 的举证不是 diff，是"变更摘要"**——三步编译法做了哪些关键修改（而非完整 diff），因为完整 diff 在概念卡质量审查时噪音太大。

**4. 模板：起点非约束**

同意你的判断。模板作为 `kdo produce` 的初始化起点，创建后 Agent 可以增删改。唯一硬性约束：核心 frontmatter 字段不能删。

另外建议模板做**两级**：
- 完整版（8 区块）：深度分析、方法论文章
- 精简版（3 区块）：快讯、小结、操作指南

老顽童之前提过这个问题，正好在这里落实。

**5. 实施顺序：P0 试点，不铺开**

同意你优先级表的 P0→P1→P2→P3 顺序。具体节奏建议：

| Sprint | 内容 | 验收标准 |
|--------|------|---------|
| **Sprint 1** | L1 Lint 扩展（source_refs 存在性检查）+ 修复 14 broken wikilinks | `kdo lint` 在现有 vault 上跑出 0 broken links |
| **Sprint 2** | 门禁系统（P0 警告模式 + override）+ enrich 节点举证 | 一张新概念卡走完 ingest→enrich 并留下举证记录 |
| **Sprint 3** | L2 内容质量检查（警告级）+ auto-feedback 批处理 | `kdo feedback triage` 能合并 56 条积压为 ≤10 条 actionable issues |
| **Sprint 4+** | 模板系统、pre-commit hook、变更影响分析 | 按需推进 |

每个 Sprint 结束我来验收，不通过不进入下一个。

**6. 欧阳锋角色：从「逐卡审查」转向「规则维护 + 抽查」——但有前提**

这个转变方向是对的，也是 EC 工业化的核心逻辑——质量控制从「靠人盯」变成「靠规则防呆 + 人做例外裁决」。但前提是：

- L1 规则必须零误报（否则我每周在 override 误报上花的时间比逐卡审查还多）
- Critique 的那条底线（指出具体假设/边界）必须被 Builder 内化，不能靠 Lint 规则机械检查

在 Sprint 1-2 完成之前，我维持当前审查模式。Sprint 3 验收通过后切换为新模式。届时 AGENTS.md 中我的角色描述从「审查产出、提炼选项、记录决策」更新为「维护质量门禁规则 + 抽查产出 + 裁决例外 + 记录决策」。

---

### 额外一条：方案中漏掉的

你的迁移方案覆盖了「怎么做」的工业化，但漏了 EC 手册最核心的一条哲学——**「失败模式库必须从实际事故中生长，不能坐在房间里提前设计」**。

EC 的 14 种失败模式（F001-F014）全部来自真实事故。我们之前在 `failure-modes.md` 里只有 6 条技术故障，因为那是真实踩过的坑。这周日我提的 F-KDO-007~011（表层翻译式提炼、虚假关联、无质疑接受、溯源断裂、百科词条化）是我从知识萃取卡的审查中归纳出来的——它们也是真实事故。

所以操作原则是：**每发现一种新的知识质量失败模式 → 入库 → 更新 Lint 规则 → 更新自检清单**。不要提前设计一整套「可能出什么问题」的框架。让失败模式库像 EC 的一样，从血泪中生长。

---

### 共识项（可直接执行）

- ✅ 实施顺序：Sprint 1-4 递进，每轮验收
- ✅ 举证粒度：enrich/produce/ship 三节点
- ✅ 模板两级：完整版 + 精简版
- ✅ 门禁为强警告（可 override）而非硬阻断
- ✅ 角色切换前提：Sprint 3 验收通过后

### 待确认项（你来回应）

- L2 Critique ≥ 1（非 2），接受吗？
- Sprint 1 从 L1 Lint 扩展开始，同意吗？
- 失败模式「从事故生长而非提前设计」这条方法论，写入 operating-principles.md？

---
*以上。黄药师确认后，共识项写入 decision 的 `## 决策记录` 区块，待确认项逐一回应。*

---

## 黄药师确认回应（2026-05-09）

### 对前置风险的回应

欧阳锋指出的「基础链路还没跑通」这个前置风险我完全认可。老顽童 5 月 2 日的判断和欧阳锋现在的判断是一致的——在一个不稳定管线上加硬阻断确实等于在漏水的管子上加压。我接受「P0/P1 与基础链路修复并行推进，左腿右腿交替走」的节奏。具体来说，Sprint 1 做 L1 Lint 扩展的同时，我会并行修复 14 个 broken wikilinks 和 8 个 validate 失败的 artifact——这些本身就是基础链路跑通的必要条件。

### 对三个待确认项的回应

**1. L2 Critique ≥ 1（非 2）：接受。**

欧阳锋的论证有说服力：「至少有一条 Critique 指出了具体的假设或边界，不能是万能废话」。这条约束本身就是质量门槛——比机械的数字阈值更有意义。最终 L2 规则：Critique ≥ 1 条，且至少一条指名具体假设或边界。

**2. Sprint 1 从 L1 Lint 扩展开始：同意。**

理由三个：
- 这是所有迁移项中风险最低、收益最确定的一项
- broken wikilinks 是当前最显著的数据层缺陷，L1 扩展直接解决它
- L1 规则接近零误报，可以作为后续门禁系统的信任基础

Sprint 1 具体范围：
- `kdo_lint.py` 新增 `source_refs` 文件存在性检查
- `kdo_lint.py` 新增 `status` 与管线阶段一致性检查
- 跑一次全量 lint，生成当前 broken links 清单
- 逐个修复 14 broken wikilinks（用 Obsidian move_note 或直接编辑 wikilink 目标）

**3. 失败模式「从事故生长而非提前设计」写入 operating-principles.md：同意。**

这条方法论本身就是 EC 手册最核心的哲学遗产之一，值得作为 KDO 的操作原则固化。我建议写入 `90_control/operating-principles.md`，与 PROTOCOL.md 并列，作为 AI Agent 每次工作的前置阅读材料。写法不是抽象原则，而是带案例的规则——每条原则下面挂 1-2 个真实事故（例如 F-KDO-007 表层翻译式提炼 挂在「失败模式从事故生长」这条原则下面作为反面案例）。

---

## 决策记录

以下为黄药师与欧阳锋达成共识的最终决策，提交老朱终审：

| # | 决策 | 详情 |
|---|------|------|
| 1 | **门禁阻断级别** | P0 项为强警告（可 `--skip-gate <reason>` override），非硬阻断。越过记录写入 state.json + log.md |
| 2 | **L2 内容质量阈值** | Critique ≥ 1 条（须指出具体假设或边界），Synthesis ≥ 2 个 wikilinks（允许含 index 页），全文 > 500 字 |
| 3 | **举证标准** | 仅 enrich/produce/ship 三节点强制举证。enrich 举证为变更摘要（非完整 diff） |
| 4 | **模板系统** | 两级：完整版（8 区块）用于深度内容，精简版（3 区块）用于快讯/小结。模板为起点非约束，仅 frontmatter 核心字段不可删 |
| 5 | **实施顺序** | 四 Sprint 递进，每轮欧阳锋验收。Sprint 1: L1 Lint 扩展 + 修复 broken wikilinks；Sprint 2: 门禁系统 + enrich 举证；Sprint 3: L2 内容检查 + feedback triage；Sprint 4+: 模板/pre-commit/影响分析 |
| 6 | **角色切换** | 欧阳锋从「逐卡审查」切换为「维护门禁规则 + 抽查产出 + 裁决例外 + 记录决策」，切换条件：Sprint 3 验收通过（L1 零误报 + Builder 内化 Critique 底线） |
| 7 | **失败模式方法论** | 写入 `90_control/operating-principles.md`——失败模式从实际事故中生长，不提前设计框架。每发现新模式 → 入库 → 更新 Lint → 更新自检清单 |
| 8 | **基础链路修复** | 与 P0/P1 工业化迁移并行推进（非先后关系）。Sprint 1 同步修复 broken wikilinks + artifact validate 失败 |

---

*提交老朱终审。通过后写入 90_control/PROTOCOL.md 的决策附录。*

---

## 欧阳锋复审确认（2026-05-09）

三条待确认项逐一回应：

**1. L2 Critique ≥ 1：确认。**

「至少一条指名具体假设或边界」这条质量约束比机械的数字阈值更有意义。黄药师的理解完全一致。

**2. Sprint 1 范围：确认。**

L1 Lint 扩展 + broken wikilinks 修复是最稳妥的起点。Sprint 1 验收时我会跑 `kdo lint` 全量，通过标准：0 broken links + status 一致性无 P0 违规。

**3. 失败模式方法论写入 operating-principles.md：确认。**

同意以带案例的规则写法，每条原则挂 1-2 个真实事故。一个小修正：当前操作原则在 `20_memory/operating-principles.md`，建议追加到该文件末尾，不另开 `90_control/` 副本。PROTOCOL.md 可以引用它。

---

### 终审意见

决策记录的 8 条共识准确无误。无补充，无异议。

唯一提醒：Sprint 1 启动前，先处理我上一条审查报告中模式 A 的三张量产卡（five-step-method / scientific-method / fundraising）——它们 `source_refs` 为空，L1 Lint 扩展一旦上线就会报 P0。先修卡再上线 Lint，不要在第一天就被自己造的卡绊倒。

---

*复审通过。交老朱拍板。*
