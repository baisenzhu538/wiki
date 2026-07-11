---
id: task_20260711_wangyuyan-fundamentals-dual-triangle-factory-buildout
title: 一堂·苦练基本功 × 双三角/cap_hub 工厂改造：AI-基本功顶点扩展 + cap_hub三环过滤器 + 段位合并 + 飞轮补全（建工厂线）
status: in_progress
priority: P0
assignee: huangyaoshi-claude
reviewer: 欧阳锋
expected_cards: 5
expected_agent_specs: 0
source_refs:
- 70_product/tasks/task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration.md
- 70_product/tasks/task_20260711_wangyuyan-fundamentals-domain-production.md
- 30_wiki/concepts/concept-yihang-dual-triangle-core.md
- 30_wiki/frameworks/framework-yihang-dual-triangle-weapon-library.md
- 30_wiki/methods/method-dual-triangle-flywheel-engine.md
- 70_product/tasks/task_20260708_huangyaoshi-capability-hub-phase1.md
related:
- '[[task_20260711_wangyuyan-fundamentals-domain-production]]'
- '[[task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration]]'
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-yihang-dual-triangle-weapon-library]]'
- '[[method-dual-triangle-flywheel-engine]]'
- '[[task_20260708_huangyaoshi-capability-hub-phase1]]'
created_at: '2026-07-11'
updated_at: '2026-07-11T14:17:42.939651+00:00'
---

# 基本功 × 双三角/cap_hub 工厂改造（建工厂线 · 黄药师）

> 来源：黄药师 `task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration.md`（原始诉求）+ 王语嫣全局裁定。
>
> **王语嫣全局裁定（把关者视角）**：黄药师建议书**作为诉求清单采纳，作为"整体迁移进双三角/不建独立域"方案否决**。理由：① KDO 给 agent 用 ≠ 全挂双三角——agent 入口多元（双三角/管理/刻意练习/cap_hub），双三角是坐标系之一不是唯一；② 基本功是组织能力元层（土壤），双三角是 AI 协作体系（作物），元层不被任一上层域私有化；③ 黄药师是 KDO **工厂建设者**、老顽童是**主力生产者**，两者任务性质不同，应分线编排而非混为"迁移"。
>
> **编排结论**：按性质拆两线——**#150 老顽童产内容本体**（基本功域独立，管理/团队子域，已 queued）；**本任务 #151 黄药师建工厂**（改双三角/cap_hub/飞轮既有工厂卡，引用 #150 内容卡）。**一个本体（基本功域），多个索引（双三角/管理/刻意练习/cap_hub）**；索引可加，本体不迁。
>
> **承接人纠偏**：黄药师原建议书 `assigned_to: 王语嫣` 不成立——王语嫣只编排不写 30_wiki 卡。本任务 `assignee: 黄药师`（建工厂），#150 `assignee: 老顽童`（产内容）。

---

## 〇、依赖与阻塞说明（铁律）

- **状态**：`status: queued`（待领取）。
- **强依赖**：本任务所有"内容填充"=**wikilink 引用 #150 老顽童产的基本功域 concept 卡**，故实质填充**依赖 #150 对应卡 reviewed**。
- **可先做的部分（不依赖内容）**：黄药师 claim 后可先搭**工厂机制框架/钩子**——cap_hub 三环过滤器的接口骨架、双三角 AI-基本功顶点扩展的占位结构、段位合并的层级框架、飞轮补全的插入位。这些"建工厂的脚手架"不依赖 #150 内容，可并行。
- **必须等的部分（依赖内容）**：脚手架里填具体内容（AI-基本功四新项的展开、三环 checklist 的判定话术、段位 L1-L6 的定义、演化路径 A→F 的步骤、科学练习四要素）= **引用 #150 老顽童产的对应 concept 卡**，须等 #150 那些卡 reviewed 后接入。
- **领取建议**：黄药师可 claim 先搭脚手架；若 #150 核心卡尚未 reviewed，本任务在内容填充前自然停顿，不返工。

---

## 一、目标产出（建工厂 · 改既有卡 + 1 新组件卡）

| 编号 | 产出 | 性质 | 改/建的文件 | 引用 #150 哪张卡 |
|---|---|---|---|---|
| B-1 (P0) | **AI-基本功顶点扩展**：在双三角 AI-基本功顶点加入 上下文工程/智能体协作/全网调研（提示词工程已有） | 改既有工厂卡 | `concept-yihang-dual-triangle-core.md` 的 AI-基本功定义 + `framework-yihang-dual-triangle-weapon-library.md` 的 AI-基本功章节 | `concept-一堂-AI时代基本功变与不变`（#150 P1 #15 卡） |
| B-2 (P0) | **cap_hub 三环过滤器**：把三环（务实=input/output spec、可练=独立验证脚本、价值=高频复利）落成 cap_hub 能力注册准入 checklist | **新建工厂组件卡** | `30_wiki/tools/tool-three-ring-capability-filter.md`（新）+ 接入 #144 cap_hub 注册流程（接口对齐，等 Phase 2 Skill 注册标准） | #150 三环六维 concept 卡 |
| B-3 (P1) | **段位合并**：双三角武器库补"个人单项基本功 L1-L6 纵向成长阶梯"，写清岗位段位（SABC，团队配置）vs 单项段位（L1-L6，个人刻意练习）的使用场景 | 改既有工厂卡 | `framework-yihang-dual-triangle-weapon-library.md` 段位章节 | #150 段位 concept 卡（SABC+L1-L6） |
| B-4 (P1) | **飞轮补全**：演化路径 A→F（模糊→拆解→命名→建模→阶梯化→制度化）作为"L1→L4 操作指南"，科学练习四要素（套路/非舒适区/大量重复/及时反馈）补进"练"环节 | 改既有工厂卡 | `method-dual-triangle-flywheel-engine.md` | #150 演化路径 concept 卡 + 科学练习四要素 concept 卡 |

**产出规模**：1 张新工厂组件卡 + 4 张既有工厂卡升级。估时 4-6h（黄药师熟自有工厂）。

---

## 二、与 #150 的边界（文件不重叠，无冲突）

| 维度 | #150 老顽童（产内容） | #151 黄药师（建工厂） |
|---|---|---|
| 改/建的文件 | **只新增**基本功域本域卡（`30_wiki/concepts|frameworks|tools|methods|cases|domains` 内 `yt-...-fundamentals-*` / `concept-一堂-*` 等本域文件 + `domains/management-domain-digest.md`） | **只改**双三角/cap_hub/飞轮**既有**工厂卡（`concept-yihang-dual-triangle-core` / `framework-yihang-dual-triangle-weapon-library` / `method-dual-triangle-flywheel-engine`）+ **新建 1 工厂组件**（`tool-three-ring-capability-filter`） |
| 是否动双三角 core | 否（只在 related 里 wikilink） | **是**（扩展 AI-基本功顶点定义） |
| 是否动 cap_hub | 否（不替 cap_hub 立规） | **是**（B-2 加三环过滤器，归 #144 领地） |
| 是否动基本功域本体 | **是**（本体就在这建） | 否（只引用，不迁本体） |
| 40 卡六要素标签 | **主列拆建推练 + 辅列六要素**（在 #150 40 卡导航里完成，多入口索引） | 不重做，引用 #150 的 40 卡导航 |

**铁律**：黄药师**不**改/删/迁基本功域任何本域卡；老顽童**不**改双三角/cap_hub/飞轮任何工厂卡。两线文件零重叠。

---

## 三、引用协议（核心：引用不迁移）

1. 黄药师所有内容填充 = `[[wikilink]]` 引用 #150 老顽童产的 concept 卡 + 一句话承接，**不复制内容、不重复造卡、不把本体搬进双三角**。
2. B-1 AI-基本功顶点扩展：在双三角 core 的 AI-基本功定义处加"（扩展见 `[[concept-一堂-AI时代基本功变与不变]]`：上下文工程/智能体协作/全网调研）"+ 顶点列表补四项，**展开内容留在 #150 卡**。
3. B-2 三环过滤器：`tool-three-ring-capability-filter` 首句"本过滤器是 `[[#150 三环六维 concept]]` 在 cap_hub 能力注册场景的应用"，checklist 三项的"为什么"link 回 #150 三环卡，工具卡只写"怎么判定（spec/脚本/频率）"。
4. B-3/B-4 同理：工厂卡写"体系如何承载"，内容定义 link 回 #150。
5. 完成后，黄药师在 #150 相关本域卡的 `related` 里**反向补 link** 到本任务改的工厂卡（双向可达，agent 从任一端都能命中）。反向 link 由黄药师顺手补，或通知老顽童在 #150 收尾时补——由欧阳锋终审时检查双向闭环。

---

## 四、验收标准（欧阳锋终审）

- [ ] 双三角 AI-基本功顶点含四项（提示词工程/上下文工程/智能体协作/全网调研），且展开内容 wikilink 到 #150 卡，无双写。
- [ ] `tool-three-ring-capability-filter` 为可执行 checklist（务实/可练/价值各一条客观判定），并注明与 #144 cap_hub 注册流程的接入点（Phase 2 Skill 注册标准未到位则注明挂起）。
- [ ] 武器库段位章节含岗位段位（SABC）+ 单项段位（L1-L6）双轨及使用场景说明。
- [ ] 飞轮引擎含演化路径 A→F + 科学练习四要素，且与 Truman 复盘协议（agent-os.md §10）对接点已标注。
- [ ] **无文件越界**：黄药师未改任何基本功域本域卡。
- [ ] **双向 link 闭环**：本任务改的工厂卡 ↔ #150 对应 concept 卡互相 wikilink。
- [ ] pre-submit 通过（YAML/WIKILINK/DOMAIN/DK_SECTION/OUTLINK，`reviewed_by: 欧阳锋`）。

---

## 五、原 migration 建议书的处置

- `task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration.md`（黄药师原始建议书）**保留归档**，作为本任务的诉求来源与映射分析参考（其 §2 四字诀→六要素映射、§2.6 40 卡归类表仍有检索价值，agent 可读）。
- 其**执行部分由本任务 #151（建工厂线）+ #150（产内容线）取代**：原 P0-1（术语桥接）→ 并入 #150 总纲卡术语边界节；原 P0-3（40 卡六要素归类）→ 并入 #150 40 卡导航辅列；原 P0-2/P0-4/P1-1/P1-2 → 本任务 B-1~B-4。
- 其**"整体迁移进双三角/不建独立域/assigned_to=王语嫣"** 三处裁定**否决**（见头部全局裁定）。

---

## 六、最终判断

- 评级：**A-**（建工厂线清晰、文件边界零重叠、引用协议闭环、依赖明确）。
- 价值：把黄药师的双三角/cap_hub 局部诉求，纳入全局坐标系落地——既让 agent 从双三角/cap_hub 入口能命中基本功（多入口索引），又守住基本功域本体独立（元层不被私有化）。
- 风险：依赖 #150 内容卡 reviewed 才能填充，若 #150 延期本任务填充同步延期（脚手架可先搭，不阻塞黄药师开工）。
- 编号 **#151**，与 #150 同批待领取：老顽童领 #150（地基，可立即干），黄药师领 #151（先搭脚手架，填充等 #150）。

*王语嫣编排 · 2026-07-11*
