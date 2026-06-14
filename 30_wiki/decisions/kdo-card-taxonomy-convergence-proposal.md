---
title: "KDO 卡片类型体系收敛建议：明确四卡体系与 Agent-native 类型的关系及迁移规则"
type: decision
status: proposed
domain:
  - master
created_at: "2026-06-13"
updated_at: "2026-06-13"
target_roles:
  - 欧阳锋（Architect）
  - 黄药师（Builder）
  - 老顽童（Producer）
reviewer: 欧阳锋
author: Kimi Code CLI
related:
  - "[[kdo-system-manual]]"
  - "[[kdo-industrialization-manual]]"
  - "[[PROTOCOL]]"
  - "[[AGENTS]]"
  - "[[agent-native-card-design]]"
  - "[[high-density-composite-compilation-strategy]]"
tags:
  - "#kdo"
  - "#architecture"
  - "#taxonomy"
trust_level: medium
---

# KDO 卡片类型体系收敛建议

> **触发**：在执行 yt-* 概念卡 L2 精修（237 张）和七件事集团素材入库过程中，发现控制文件对卡片类型的描述存在不一致，执行者难以判断应以哪套体系为准。
> **目的**：请求欧阳锋裁决并统一 KDO 的卡片类型体系，避免后续量产和 lint 规则继续漂移。

---

## 一、观察到的张力

当前控制文件对 KDO 知识原子的定义存在两套并行体系：

| 维度 | 四卡体系 | Agent-native 体系 |
|------|---------|------------------|
| **来源文件** | `kdo-system-manual.md` §三 | `kdo-industrialization-manual.md` §十二 |
| **核心类型** | concept / skill / dk / case | composite-concept / framework / tool / case |
| **设计假设** | 按知识用途分类 | 按知识图谱节点层级分类 |
| **粒度导向** | 四卡协作描述完整方法论 | 细粒度节点 + frontmatter 图边 |
| **当前状态** | 系统手册仍在引用 | 工业化手册 v1.3 起已宣布为正式标准 |

**具体矛盾点**：

1. `kdo-system-manual.md`（v1.2.0，2026-06-09）§三仍说"四卡体系描述完整方法论"，§十角色分工也引用四卡。
2. `kdo-industrialization-manual.md`（v1.9，2026-05-31）§十二明确说"v1.0 的复合编译方案（合并为大卡）已被废弃"，"所有知识卡片按 agent-native 格式编译"。
3. `PROTOCOL.md` v0.3 §3 的 Entity Types 只列了 concept / entity / comparison / decision / improvement-plan / system / trend，未直接对应上述两套体系。
4. 实际目录中 `30_wiki/concepts/` 里既有标准 concept 卡，也有 framework/tool 卡，还有 pan-product concept、research concept、catalog index 等变体（工业化手册 §1.10 已识别 4 种结构）。

---

## 二、不收敛的风险

| 风险 | 表现 | 触发场景 |
|------|------|---------|
| **执行者无所适从** | 老顽童量产时不知道新卡该标 `type: concept` 还是 `type: framework` | 每次创建新卡 |
| **lint 规则漂移** | 四卡体系的规则与 agent-native 体系的规则同时存在，可能互相冲突 | 跑 `kdo lint` 时 |
| **飞轮摩擦增加** | 欧阳锋审查时发现卡片的 type/结构不符合自己心中的标准，但标准未书面统一 | 每次审查 |
| **存量卡迁移悬置** | 旧四卡体系下的卡片是否需要迁移？何时迁移？没有规则 | 批量升级时 |
| **skill 封装困难** | `kdo encapsulate` 需要明确的卡片类型来路由知识注入，类型模糊会导致 system prompt 构建不稳定 | 发布 skill 时 |

---

## 三、建议方案

### 方案 A（推荐）：明确以 Agent-native 体系为唯一当前标准，四卡体系降级为历史概念

**具体动作**：

1. **在 `kdo-system-manual.md` 中更新 §三**：
   - 说明四卡体系是 v1.0 设计，v1.3 起已被 agent-native 体系取代。
   - 保留四卡作为"人类理解视角"的映射表，但明确不用于 frontmatter `type` 字段。

2. **统一 frontmatter `type` 枚举**：
   - `composite-concept`
   - `framework`
   - `tool`
   - `case`
   - `entity`
   - `decision`
   - `improvement-plan`
   - `system`
   - `trend`
   - （`concept` 是否保留作为复合概念的别名或顶层统称，需欧阳锋裁决）

3. **新增"类型选择决策树"到 `kdo-industrialization-manual.md` §十二或 `agent-native-card-design`**：
   - 一张知识地图 → `tool`
   - 多张知识地图/工具箱 → `framework`
   - 方法论顶层 → `composite-concept`
   - 真实案例 → `case`
   - 企业/人物/产品 → `entity`
   - 领域趋势 → `trend`

4. **制定存量卡迁移规则**：
   - 新卡严格走 agent-native 体系。
   - 旧 `type: concept` 卡不必一次性全改，但在每次 L2/L3 升级时按结构类型重分类（参考工业化手册 §1.10 的 4 种结构）。
   - 旧的 `type: skill` 卡逐步拆分为 `tool` 或 `framework`。
   - 旧的 `type: dk`（暗知识）卡保留独立类型或并入 `case`/`tool`，需欧阳锋裁决。

5. **同步更新 lint 规则**：
   - `kdo lint` 对 `type` 字段做白名单校验。
   - 不同 type 的体量和必填节段规则与 agent-native 手册一致。

### 方案 B：保留双轨制，但明确各自使用场景

- 四卡体系用于**人类沟通**和**粗略分类**。
- Agent-native 体系用于**frontmatter `type`** 和 **skill 封装**。

**风险**：双轨制会增加认知负担，长期可能再次漂移。

### 方案 C：回归四卡体系，废弃 agent-native

- 不建议。agent-native 是更底层、更适配 RAG/skill 封装的设计，回归四卡会损失当前的技术优势。

---

## 四、推荐方案的收益与成本

| 收益 | 成本 |
|------|------|
| 执行者不再纠结 type 选择 | 需要更新 2-3 份控制文件 |
| lint 规则可以精确 enforcing | 需要一次存量卡盘点（非迁移） |
| skill 封装路由更稳定 | 需要向老顽童/黄药师做一次规则同步 |
| 减少审查摩擦 | — |
| 为下一步自动化卡片分类打基础 | — |

---

## 五、实施清单（如方案 A 被采纳）

- [ ] 欧阳锋确认最终 `type` 枚举和白名单
- [ ] 黄药师更新 `kdo-system-manual.md` §三及 §十中关于四卡的表述
- [ ] 黄药师在 `kdo-industrialization-manual.md` §十二新增"类型选择决策树"
- [ ] 黄药师更新 `PROTOCOL.md` §3 Entity Types 与最终枚举对齐
- [ ] 黄药师更新 `kdo lint` 的 `type` 白名单校验规则
- [ ] 老顽童在后续 L2/L3 升级中按结构类型重分类存量卡
- [ ] 欧阳锋审查更新后的控制文件并关闭本 decision

---

## 六、请求欧阳锋裁决

请欧阳锋就以下两点给出决策：

1. **是否采纳方案 A**（以 agent-native 为唯一当前标准）？若否，倾向方案 B 还是另有方案？
2. **`type: concept` 是否保留**？若保留，是作为 `composite-concept` 的别名、顶层统称，还是继续作为独立类型？

---

*Kimi Code CLI · 2026-06-13 · 基于对 KDO 控制文件和实际执行体验的观察*
