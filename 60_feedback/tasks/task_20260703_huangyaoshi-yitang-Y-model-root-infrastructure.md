---
id: task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure
title: "Y模型根节点化：Schema + GraphRAG + 旧卡 deprecation 基础设施"
type: task
status: queued
priority: P1
assignee: 黄药师
reviewer: 欧阳锋
created_at: 2026-07-03
updated_at: 2026-07-03
expected_outputs:
  - "schema 支持 is_root_node / replaces / deprecated_by"
  - "kdo lint 新增 deprecation 校验规则"
  - "kdo index --rebuild 支持根节点权重和 theory/fact/practice 边类型"
  - "3 张旧卡正式 deprecated 并指向新卡"
  - "system-kdo-factory-as-Y-model.md 文档"
dependencies:
  - "[[task_20260703_laowantong-yitang-Y-model-foundation-production]]"
source_refs:
  - "[[framework-yitang-Y-model]]"
  - "[[agent-native-card-design]]"
  - "[[agent-external-brain-design]]"
  - "[[opc-ai-sales-agent-architecture]]"
related:
  - framework-yitang-Y-model
  - framework-yitang-shishi-qiushi
  - framework-yitang-jiefang-sixiang
  - yt-entrepreneur-scientific-method
  - yt-entrepreneur-truth-seeking
  - yt-model-liberate-thinking-layers
  - agent-native-card-design
  - agent-external-brain-design
  - opc-ai-sales-agent-architecture
---

# Y模型根节点化：Schema + GraphRAG + 旧卡 deprecation 基础设施

> 任务来源：黄药师提出 Y模型应成为整个 KDO 知识图谱的根节点；KDO 工厂本身是 Y模型的一个运行实例（理论臂 + 事实臂 + 知行合一轴）。
> 目标：在基础设施层面支持这一架构认知，不新增卡片，通过 schema、索引、文档让 Y模型自然成为查询入口。
> 依赖：`#51` 产出 `framework-yitang-Y-model` 等 7 张新卡后，本任务可立即执行；部分 schema 设计可与 #51 并行。

---

## 一、核心认知（已由王语嫣/黄药师/用户对齐）

```
                         ┌─────────────────┐
                         │  framework-yitang-Y-model  │
                         │    （KDO 知识图谱根节点）   │
                         └────────┬────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │  theory_arm         │  fact_arm           │
            │  理论臂             │  事实臂             │
    ┌───────┴───────┐     ┌───────┴───────┐
    │ framework     │     │ case           │
    │ concept       │     │ dark-knowledge │
    │ tool          │     │ agent-trace    │
    │ system        │     │ decision-record│
    └───────┬───────┘     └───────┬───────┘
            │                     │
            └───────────┬─────────┘
                        │ practice_axis
                        │ 知行合一轴
                        │
              王语嫣诊断 → 老顽童生产 → 欧阳锋审查 → 用户使用 → 反馈回流
```

**关键判断**：
1. Y模型不是 decision-science 域里的一张概念卡，而是整个 KDO 的根节点。
2. 所有 framework/concept/tool 卡通过 `theory_arm` 归属 Y模型。
3. 所有 case/dk/agent-trace/decision-record 通过 `fact_arm` 归属 Y模型。
4. diagnosis / task / agent-spec 走知行合一轴，连接两臂。
5. KDO 工厂的运行方式就是 Y模型的一个实例。

---

## 二、Schema 层改造

### 2.1 新增字段

| 字段 | 类型 | 适用卡片 | 说明 |
|:---|:---|:---|:---|
| `is_root_node` | boolean | framework / concept | 标记为知识图谱根节点，目前只有 `framework-yitang-Y-model` 为 true |
| `replaces` | list[string] | 所有新卡 | 本卡替代了哪些旧卡 |
| `deprecated_by` | string | 所有旧卡 | 本卡被哪张新卡替代 |

### 2.2 示例

新卡 `framework-yitang-Y-model` 的 frontmatter：

```yaml
is_root_node: true
replaces:
  - yt-entrepreneur-scientific-method
```

旧卡 `yt-entrepreneur-scientific-method` 的 frontmatter：

```yaml
deprecated_by: framework-yitang-Y-model
```

### 2.3 kdo lint 新增规则

- [ ] `is_root_node: true` 的卡片类型必须是 `framework` 或 `concept`。
- [ ] 全库只能有 1 个 `is_root_node: true` 的卡片（根节点唯一性）。
- [ ] `replaces` 中的 ID 必须存在，且被替换的卡必须有 `deprecated_by` 指向本卡。
- [ ] `deprecated_by` 中的 ID 必须存在，且该卡必须有 `replaces` 包含本卡。
- [ ] `deprecated_by` 与 `replaces` 不能形成循环引用。
- [ ] deprecated 卡片如果仍有新的入站 `related` 链接，发出 WARNING。

---

## 三、GraphRAG 索引层改造

### 3.1 根节点权重

- `kdo index --rebuild` 时，对 `is_root_node: true` 的卡片：
  - PageRank / 中心性初始权重设为最高。
  - 在图可视化中作为默认中心节点。
  - 查询扩散时优先经过根节点。

### 3.2 边类型扩展

在现有 `related` 边基础上，增加隐式边类型（由卡片 type 自动推断）：

| 边类型 | 起点类型 | 终点类型 | 含义 |
|:---|:---|:---|:---|
| `theory_arm` | framework / concept / tool / system | framework-yitang-Y-model | 理论臂归属 |
| `fact_arm` | case / dark-knowledge / report / agent-trace | framework-yitang-Y-model | 事实臂归属 |
| `practice_axis` | diagnosis / task / agent-spec | framework-yitang-Y-model | 知行合一轴 |
| `replaces` | 新卡 | 旧卡 | 替代关系 |
| `deprecated_by` | 旧卡 | 新卡 | 被替代关系 |

### 3.3 查询入口

- 支持 `kdo query --root framework-yitang-Y-model --arm theory` 查询理论臂卡片。
- 支持 `kdo query --root framework-yitang-Y-model --arm fact` 查询事实臂卡片。
- 默认查询优先经过根节点扩散。

---

## 四、旧卡 deprecation 执行

`#51` 生产完成后，对以下 3 张旧卡执行 deprecation：

| 旧卡 | 操作 |
|:---|:---|
| `yt-entrepreneur-scientific-method` | frontmatter 加 `deprecated_by: framework-yitang-Y-model`；正文顶部加迁移提示；related 加回链 |
| `yt-entrepreneur-truth-seeking` | frontmatter 加 `deprecated_by: framework-yitang-shishi-qiushi`；正文顶部加迁移提示；related 加回链 |
| `yt-model-liberate-thinking-layers` | frontmatter 加 `deprecated_by: framework-yitang-jiefang-sixiang`；正文顶部加迁移提示；related 加回链 |

---

## 五、KDO 工厂作为 Y模型实例 文档化

创建/更新 `30_wiki/systems/system-kdo-factory-as-Y-model.md`：

**必须包含的内容**：
1. KDO 工厂就是 Y模型实例的总论点。
2. 理论臂：framework / concept / tool / system 卡的生产与迭代。
3. 事实臂：case / dk / agent-trace / decision-record 的收集与回流。
4. 知行合一轴：王语嫣诊断 → 老顽童生产 → 欧阳锋审查 → 用户使用 → 反馈回流 → 升级理论臂。
5. 与 `agent-native-card-design.md` 中「Agent 迭代成果回流 KDO」的衔接。
6. 与 `opc-ai-sales-agent-architecture.md` 的衔接。
7. 一张流程图或 Mermaid 图。

---

## 六、验收标准

- [ ] `90_control/schemas/` 中相关 schema 已新增 `is_root_node`、`replaces`、`deprecated_by` 字段。
- [ ] `kdo lint` 新增 6 条 deprecation / root_node 校验规则，且测试通过。
- [ ] `kdo index --rebuild` 支持根节点权重提升和 theory/fact/practice 边类型推断。
- [ ] GraphRAG 重建后，`framework-yitang-Y-model` 成为图中心节点。
- [ ] 3 张旧卡已标记 deprecated，且与新卡双向链接完整。
- [ ] `30_wiki/systems/system-kdo-factory-as-Y-model.md` 已创建并通过 pre-submit。
- [ ] 欧阳锋终审通过。

---

## 七、与后续任务的关系

| 任务 | 关系 |
|:---|:---|
| `#51` | 本任务依赖 #51 产出新卡；schema 设计可与 #51 并行 |
| `#53`（待创建） | Agent 实测回流管线：`kdo trace` + `kdo reflux` + Pipeline 事实臂视图 |
| `#50` | #50 产出的 agent-trace 将成为 #53 的输入 |

---

## 八、队列位置

- **入队编号**：`#52`
- **状态**：`queued`
- **预计工时**：黄药师 2-3 天 + 欧阳锋终审 1 天

---

*王语嫣 2026-07-03*
