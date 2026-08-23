---
id: diag_20260823_zijing-ag-dag-upgrade-9layer-landing
title: 产物级 DAG 升级 KDO F-047·九层深挖落地方案
type: diagnosis/research
author: 王语嫣
created_at: 2026-08-23
status: draft
audience: 老朱
method: framework-yitang-nine-layer-deep-dig
related:
  - diag_20260823_zijing-ag-product-outline-study
  - diag_20260823_zijing-ag-architecture-deep-dive
---
# 产物级 DAG 升级 KDO F-047·九层深挖落地方案

> 方法：一堂九层深挖法（`framework-yitang-nine-layer-deep-dig`，与 CIA ACH 同构）。从表面模型逐层深挖到可决策框架。
> 前置研究：①产品大纲 ②架构深挖（见 related）。本件用 9 层把"是否/如何把紫鲸产物级 DAG 借鉴进 KDO"挖透，L9 收敛为具体落地方案。
> ⚠️ 不含凭据。

## L1：表面业务公式 / 单元模型

**只问"是什么"**。KDO 当前编排与紫鲸产物级 DAG 的单元模型对比：

| 维度 | KDO 现状（任务级） | 紫鲸（产物级，借鉴源） |
|:--|:--|:--|
| 依赖载体 | 任务单 frontmatter `depends_on`（F-047，任务号列表） | 产物 `result_id` + `output_kind` + 邻接表 |
| 复用单位 | 任务（过程） | 产物（结果）——同一 script 喂 3 个内容形态 |
| 持久化 | vault 文件（markdown）+ git | 远程服务端（result_id 空间） |
| 编排感知 | queue_transition 状态机（计划态） | DAG 邻接表（产物态） |

**KDO 的"业务公式"**：素材诊断→编排→生产→终审→发布。每步产出：诊断报告(diag)/任务单(task)/卡片(card)/文章(article)/审查意见(review)/发布记录(delivery)。

**升级后单元模型**：每步产出带 `result_id` + `output_kind`（强类型），下游任务 frontmatter 用 `upstream_*_result_id` 显式取上游产物，实现"同一批卡片→多文章/多课程"复用。

**L1 增量**：明确 KDO 要从"任务依赖"升级到"产物依赖"——产物是结果、可复用；任务是过程、一次性。两者不是替换是叠加（KDO 既要任务状态机又要产物 result_id）。

## L2：假设审计

**检查 L1 每个升级前提的假设依据——事实/估算/愿望？**

| 假设 | 依据类型 | 敏感度 | 验证方法 |
|:--|:--|:--|:--|
| H1 产物级 DAG 能提升 KDO 编排可组合性 | 估算（紫鲸实证≠KDO 必然）| 中 | 试点 1-2 单验证下游能否取上游 |
| H2 KDO 任务单 frontmatter 能扩展承载 result_id/output_kind | 估算 | **高（最敏感）** | yaml.safe_load 兼容测试 + parse_queue/queue_transition 兼容 |
| H3 产物级 DAG 对外产品化有商业价值 | 愿望（未验证市场）| 低（对外是后话）| 对外产品化前再单独评估 |
| H4 升级不影响现有生产链 | 估算 | 中 | #390/#472 等已上板工具回归 |
| H5 result_id 能跨 session 持久化 | 估算（紫鲸服务端存，KDO 本地？）| **高** | 决定 result_id 落 vault 文件还是独立 DB |

**L2 增量**：最敏感是 H2（frontmatter 兼容）+ H5（result_id 持久化位置）。这两个不验证就不能 go。H5 是关键岔路：result_id 落 vault 文件（可溯源但 markdown 非结构化）vs 独立 DB（结构化但与"vault 是真相源"纪律冲突）。

## L3：政策 / 合规 / 监管边界

**影响升级的"不可抗力"**：

1. **charter v1.0 §3.15 文件纪律**：上板冻结 + append-only（E046/E047）——改任务单模板=改已上板规范？不是，模板是新建任务的规范，存量不回改（F-047 同律）。但改模板要走任务制。
2. **memory-registry 表1**：角色协议/规范真相源改动走任务制——任务单模板属 `90_control/templates/` 或 queue_transition 生成逻辑，改它需立项。
3. **queue_transition 协议**：`Manual edits forbidden`——result_id 字段不能手改，要脚本化流转。
4. **E040**：编排产物即写即 commit（result_id 落盘要 commit）。
5. **vault 是唯一真相源**（AGENTS.md Prime Directive）——result_id 若落独立 DB，与"vault 是真相源"可能冲突（需裁定：result_id 是 vault 的派生索引，还是独立真相源）。

**L3 增量**：升级必须走任务制立项（不能王语嫣自己改模板），且 result_id 持久化位置涉及"真相源"宪法级裁定——这是 L9 要老朱拍板的点。

## L4：失败模式库（最有价值的一层）

**找"为什么可能不行"——从紫鲸失败 + KDO 照搬失败 + KDO 已有失败三类提取：**

### A. 紫鲸的失败模式（从调研推断）
- F1 远程黑盒 MCP 信任问题（供应链）→ KDO 不照搬远程，只借鉴机制
- F2 DAG 无任务状态机（result_id 链无流转概念）→ KDO 已有状态机，互补不冲突
- F3 限时积分不可持续 → KDO 内部无计费，对外再说

### B. KDO 若照搬的失败模式（核心风险）
- **F4 result_id 持久化丢失**：紫鲸服务端存 result_id，KDO 本地若落 markdown 文件，跨 session/跨实例如何保证 result_id 可取？若落独立 DB，DB 与 vault 漂移（E017/E029 同族：配置被改≠生效）。
- **F5 强类型 output_kind 与现有卡片体系冲突**：KDO 卡是 markdown 文件（半结构化 frontmatter+正文），紫鲸 output_kind 是结构化对象。KDO 卡的"类型"已有（concept/framework/case/tool/dk/agent-spec），output_kind 要映射到现有卡片类型还是新增维度？
- **F6 邻接表维护负担**：每个任务单声明 upstream/downstream，编排者（王语嫣）维护成本增加——可能重蹈 E022（关键词≠域枚举，"以为覆盖≠覆盖"），邻接表写错=下游取不到上游。
- **F7 产物复用 vs 任务复用混淆**：KDO 任务是过程（流转），产物是结果（资产）。若把 result_id 塞进任务流转，混淆"过程态"与"产物态"——任务 cancelled/作废了，产物 result_id 还在吗？
- **F8 frontmatter 膨胀**：加 depends_on（F-047）+ result_id + output_kind + upstream_*_result_id，frontmatter 字段越来越多，parse_queue/lint 兼容风险（E017 正则跨字段误读同族）。

### C. KDO 已有失败模式（错误模式库对照）
- E022 关键词检索≠域枚举 → 邻接表也可能"以为声明了≠实际能取"
- E046 append-only 不吞节 → 改 frontmatter 加字段要小心
- E047 修订单越权 → 升级要新单不能改已上板 F-047 本体

**L4 增量**：核心风险是 F4（result_id 持久化）+ F7（产物 vs 任务混淆）。F4 是技术可行性命门，F7 是概念命门——KDO 不能把"产物 result_id"简单塞进"任务流转"，必须分清：任务状态机管过程，result_id 管产物资产。

## L5：隐性成本与替代方案

**显性成本之外的经济现实 + 替代方案压缩空间：**

### 隐性成本
- queue_transition.py/parse_queue 改造（兼容 result_id 字段，不破坏状态机）
- 任务单模板改 + 现有任务回填（或不回填，F-047 同律存量不回改）
- 编排者学习成本（邻接表思维）+ 老顽童产物落盘习惯改变（每张卡带 result_id）
- lint 扩展（result_id/output_kind 校验）

### 替代方案（用户不是在"升级 vs 不升级"间选，是在"升级 vs 所有替代"间选）
- **T1 不升级**：保持任务级 depends_on（F-047 现状），用 Obsidian wikilink 做软产物关联——成本 0，但跨任务产物复用（同一批卡→多文章）无显式机制
- **T2 轻量 result_id**：只在新建任务标 result_id（不强制邻接表/downstream），下游手动取——半步升级，低成本低收益
- **T3 完整产物级 DAG**：result_id + output_kind + 邻接表 + pack_only 双形态——高成本高收益，但 F4/F7 风险高
- **T4 复用紫鲸**：KDO 不自建，MCP 多挂紫鲸——前轮已判场景不匹配，否决

**L5 增量**：替代方案 T2（轻量 result_id）是关键中间态——避开 F4 持久化命门（result_id 只标在任务单 frontmatter，落 vault 文件，不引入独立 DB）+ 避开 F6 邻接表负担（不强制 downstream）。收益打折但风险骤降。

## L6：人与组织的执行能力

**模式需要的团队能力 vs 现能调动的人力：**

| 角色 | 升级需要的能力 | 现状 | 缺口 |
|:--|:--|:--|:--|
| 黄药师 | queue_transition/parse_queue 兼容 result_id；可选 result_id 索引脚本 | 已有 queue-archive/queue_batch_accept 模式可复用 | 低（复用既有模式）|
| 王语嫣 | 任务单模板加 result_id/output_kind；邻接表维护（若 T3）| 编排主力，frontmatter 熟悉 | 中（邻接表是新思维）|
| 老顽童 | 每张卡/文章产出带 result_id | 生产主力 | 中（习惯改变）|
| 欧阳锋 | 终审加"产物 schema 校验"维度 | 审查 SOP 已成熟 | 低（加一维度）|

**关键约束**：黄药师单一实例 + 禁止清单第7条（不准一轮派 ≥3 独立单）。当前黄药师已有 #477/#478/#479 三单排队——升级不能再塞黄药师独立大单，要排队或并入现有基建线。

**L6 增量**：执行能力够，但黄药师排队约束决定升级不能抢当前基建线（#479 #426 线优先）。升级宜"轻量试点"非"大改造"。

## L7：市场情绪 / 资本 / 招商骗局

**识别非理性放大器和陷阱：**

- **情绪陷阱1**："紫鲸很成熟=我们必须照搬"——紫鲸成熟≠KDO 必须照搬（场景不同，L8 边界）。调研报告已反复强调 KDO 多处更成熟（治理/状态机/记忆/门禁深度）。
- **情绪陷阱2**："产物级 DAG 是银弹"——技术幻觉。DAG 解决可组合性，不解决 KDO 的核心（知识沉淀+溯源+治理）。
- **情绪陷阱3**：紫鲸限时试用/积分是获客钩子，不是 KDO 要学的——KDO 内部无计费需求。
- **反向情绪**："我们比紫鲸成熟所以不用学"——也错。产物级 DAG 是 KDO 确实缺的维度（F-047 只是任务级）。

**L7 增量**：剥离情绪，产物级 DAG 的真实价值=可组合性+复用，不是"紫鲸做了所以要做"。要学的是机制不是产品。

## L8：边界案例与反例

**"看似能做但不能" vs "看似不能但可以"：**

### 边界1（看似能做但不能）：照搬紫鲸 result_id 空间
紫鲸 result_id 在远程服务端存（跨 session 稳定）。KDO 若照搬到"独立 DB 存 result_id"，看似能做，但与"vault 是唯一真相源"宪法冲突——result_id 会与 vault 文件漂移（DB 说有、vault 文件被删/改）。**不能照搬到独立 DB**。

### 边界2（看似不能但可以）：result_id 落 vault 文件 frontmatter
看似不能（markdown 非结构化，result_id 难索引），但实际可以——result_id 作为 frontmatter 字段（如 `result_id: card_20260823_xxx`），落 vault 文件，与现有 source_refs/wiki_refs 同层。索引靠 .kdo/state.sqlite 或 search_index.json（已有基建）。**这是 KDO 式的产物 result_id**——不引入独立 DB，复用现有索引基建。

### 边界3（关键区分）：任务流转 vs 产物资产
KDO 任务状态机（queued→claimed→pending_review→reviewed/cancelled）管"过程"。产物 result_id 管"资产"（卡片进 vault 后持久存在，与任务状态无关）。**两者是两个维度，不是二选一**——任务 cancelled 了，已产出的卡片（带 result_id）仍在 vault。这是 F7 失败模式的解：result_id 不绑任务状态，绑产物文件。

### 反例：KDO 已有 wikilink/source_refs，是否够用？
部分够用（卡片互链靠 wikilink）。但跨任务"产物复用"（同一批卡→多文章/多课程）缺显式机制——文章任务单不知道"这批卡是哪些 result_id 产的"。轻量 result_id 字段补的就是这个缺口，不是替代 wikilink。

**L8 增量**：确定 KDO 式产物 result_id = frontmatter 字段（落 vault）+ 复用现有索引，不引入独立 DB（边界1/2）。result_id 绑产物文件不绑任务状态（边界3 解 F7）。

## L9：整合为决策框架（具体落地方案）

**收敛为可执行判断 + 最大风险 + 最小验证路径 + 重新评估触发信号。**

### 决策：有条件 GO（轻量试点，非大改造）

**不照搬紫鲸完整产物级 DAG（T3），走 T2 轻量 result_id 试点**——避开 F4 持久化命门 + F6 邻接表负担，先验证产物复用价值。

### 具体落地方案

**第一步·立项（王语嫣编排，新单，不动 F-047 本体）**
- 立项新单 #481「KDO 产物 result_id 轻量试点」（assignee=黄药师，P2，排在 #479/#477/#478 之后，禁同轮并发）
- 任务单明确：只在**新建任务** frontmatter 加 `result_id` + `output_kind` 两字段；**存量不回改**（F-047 同律）；**不引入独立 DB**（result_id 落 vault frontmatter，索引复用 state.sqlite/search_index.json）

**第二步·契约定义（王语嫣起草，老朱拍板）**
- `result_id` 命名规范：`<output_kind>_<YYYYMMDD>_<short>`，如 `card_20260823_zijing-dag-upgrade`
- `output_kind` 映射现有卡片类型（concept/framework/case/tool/dk/agent-spec/article/diagnosis/review/delivery）——不新增维度，复用现有卡片类型轴
- 下游取上游：任务单 frontmatter `upstream_result_ids`（列表，软依赖，可选）——不强制邻接表 downstream（避 F6）

**第三步·基建改造（黄药师，复用 #453/#479 模式）**
- queue_transition.py/parse_queue 兼容 `result_id`/`output_kind`/`upstream_result_ids` 三字段（yaml.safe_load 解析，禁正则，E017）
- lint 扩展：result_id 命名规范校验 + output_kind 取值校验（合法类型集）
- **不**做 pack_only 双形态（KDO 产物就是文件，不需要小包/结构化双形态）
- **不**做 AG4-OPS gateway 自动路由（KDO 无运营规划系统）

**第四步·试点验证（2 单狗粮）**
- 试点1：#481 本身的 result_id（自举——这个落地方案任务单自己带 result_id + output_kind=diagnosis）
- 试点2：选一个跨任务产物复用场景（如半肥猫 A 档卡 #465 → B 档手册 #466 → C 档案例 #467，#466/#467 的 upstream_result_ids 取 #465 的 card result_id）
- 验证：①下游任务单能 frontmatter 取上游 result_id ②parse_queue 计数不变 ③lint 通过 ④state.sqlite/search_index 能按 result_id 查到产物

**第五步·L3 观察期（2 周）**
- 连续观察：result_id 有无人消费（无人消费=产物复用价值假设 H1 证伪）/ 邻接表负担（虽不强制 downstream，upstream 写错率）/ 与 wikilink 重复度
- 观察 2 周后老朱拍板：放量（T2→T3 加邻接表）还是止步（T1 回退）

### 最大风险点
**F4 result_id 持久化**——用"落 vault frontmatter + 复用现有索引"绕开独立 DB，但需验证 state.sqlite/search_index 按 result_id 查的命中率（若查不到=索引基建要补）。

### 最小验证路径
第一步（立项+契约）→ 第三步（基建兼容，黄药师排队等 #479 出）→ 第四步（2 单狗粮）→ 第五步（2 周观察）。**不验证到第四步不进入第五步**。

### 重新评估触发信号（任一触发即回到 L2 重审）
1. 试点 result_id 无人消费（产物复用价值不成立）
2. 邻接表/上游字段维护负担过重（编排者抱怨）
3. 与现有 wikilink/source_refs 高度重复（重复建设）
4. parse_queue/lint 兼容出问题（F8 frontmatter 膨胀实证）
5. 索引基建按 result_id 查命中率低（F4 持久化证伪）

### 不做的事（边界声明）
- 不照搬紫鲸远程黑盒 MCP（供应链风险）
- 不引入独立 result_id DB（与 vault 真相源冲突）
- 不做 pack_only 双形态（KDO 产物=文件）
- 不做 AG4-OPS gateway 自动路由（KDO 无运营规划系统）
- 不做积分计费（内部工厂无需求，对外再说）
- 不强制造 downstream 邻接表（避 F6，只做 upstream 软依赖）

### 需老朱拍板项
1. **result_id 持久化裁定**：落 vault frontmatter（T2 轻量）vs 独立 DB（T3 完整）——本方案建议 T2，但属宪法级（真相源）需老朱拍
2. **output_kind 映射**：复用现有卡片类型轴 vs 新增维度——本方案建议复用
3. **是否立项 #481**：黄药师当前 3 单排队，#481 排队等 #479 出审后

---
*王语嫣 · 2026-08-23 · 九层深挖法（framework-yitang-nine-layer-deep-dig）· L9 收敛 · 不含凭据 · 三件之一（产品大纲/架构深挖/本件落地）*
