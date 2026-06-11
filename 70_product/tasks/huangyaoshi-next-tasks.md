# 黄药师后续任务（顺序执行）

## 任务方：黄药师（WSL tmux `claude`）

## 状态

**已完成**：Task 1-20 全部 ✅。Sprint 1-7 全部 ✅。P0+P1 整改令全部关闭。Task D ✅。I-1~I-6 lint 规则 ✅。kdo encapsulate ✅。Phase 1-3 KDO 效能升级全部 ✅。
- Sprint 6: `150c58b` — query --stats/--aggregate + inbox --count/--search + kdo prompt + label pipeline
- Sprint 7: `d6a38dd` — produce --stats + flywheel status + data quality gate. 16 tests, 430 pass
- Batch 1-7、P0/P1 整改令、视频管线 Task 15-17 等全部历史任务 ✅
- **Task D**：E-FM 拆 4 张 dk-ef 卡 ✅（`dk-ef-001` ~ `dk-ef-004`，dark_knowledge_type: hardware-failure）
- **I-1~I-6 lint 规则**：artifact孤儿/OCR强制/Synthesis死链/dk卡结构/tool卡质量/source_refs fuzzy ✅
- **kdo encapsulate**：skill manifest → 编译 system prompt ✅
- **Phase 1-3**：case 卡模板 + 2 条案例 + kdo skill list/publish/install + kdo quick + 深度检测 ✅

---

## 🎯 当前任务（顺序执行，做完一个再开下一个。⚠️ 不准并行）

---

### Task E：诊断基础设施 v1（新增，优先级 🔴）

> 背景：用户决定 KDO 要从"知识仓库"进化到"诊断伙伴"。需要基础设施支持对话式诊断——用卡片看具体商业问题，而非只检索卡片内容。

## 任务拆解

### E1：60_feedback/diagnosis/ 目录注册（0.5h）

**背景**：新增诊断记录积累目录。目录已创建，需要在 KDO 中注册。

**操作**：
1. `templates.py` 的 `REQUIRED_DIRS` 中确认 `60_feedback/diagnosis` 已存在（当前有 `60_feedback/corrections` 无 diagnosis，需追加）。
2. `artifacts.py` 中检查是否有需要注册的产出类型——诊断记录是 `60_feedback` 子目录，走 feedback 管线，不需要 artifact 注册。

**完成标志**：`kdo init` 后 `60_feedback/diagnosis/` 自动存在。

### E2：概念卡 frontmatter 增加 diagnostic_signals + bridges_to 字段（2h）

**背景**：要让 LLM 能做"用框架看你的问题"而非"检索框架描述"，框架/工具/案例类卡片需要预填诊断规则。同时新增的概念"桥接卡"（bridge cards，连接一堂体系与经典商业框架）需要 bridges_to 字段标记跨域桥接关系。

**操作**：

1. **在 `90_control/schemas/` 下定义概念卡 frontmatter 规范**（如果已有 schema，直接改）：
   - framework / tool / case 类型卡增加可选字段 `diagnostic_signals`
   - 所有类型卡增加可选字段 `bridges_to`（标注跨体系桥接关系）
   - 格式：
     ```yaml
     diagnostic_signals:
       - signal: "触发场景的描述"          # 用户说什么话/什么情境时触发
         framework_lens: "框架会怎么看"     # 这个信号下框架提供什么视角
         follow_up_question: "追问问题"     # 第一个追问
     bridges_to:
       - target: "yt-foresight-model-taxonomy"  # 目标卡ID
         relation: "provides_foundation_for"    # 关系类型
         description: "MECE 是预判维度选择的底层原则"
         context: "一堂体系未显式命名 MECE，但它隐含在维度设计中"
     ```

2. **在 `kdo validate --v15` 中增加校验**（可选验证，非强制）：
   - 如果卡类型是 framework/tool/case → 建议填写 diagnostic_signals
   - 未填只报 WARN 不报 FAIL（初期不强制，等老顽童习惯后再升 BLOCK）

3. **修改 enrich 骨架**（`curation.py` 中的 `enrich_wiki_page_llm`）：
   - 在 LLM enrich prompt 中增加一段：如果卡片是 framework/tool/case 类型，建议生成 2-3 条 diagnostic_signals
   - 但注意：这不等于"LLM 自动生成的 signal 可以直接用"——加 TODO 标记让老顽童手动精修

**完成标志**：
- `kdo validate --v15 --card some-framework-card` 对缺 diagnostic_signals 的 framework/tool/case 卡报 WARN
- `kdo enrich` 对新 framework/tool/case 卡在骨架中预填 diagnostic_signals TODO 占位

### E3：Graph RAG 增加 diagnostic_relations + bridges_to 边类型 + 过滤元页面（2.5h）

**背景**：当前 Graph RAG 只支持 wikilink 和 `related/component_of/prerequisites/contradicts` 四种关系。要支持诊断查询和跨域桥接查询，需要新增两种边类型。另外，用户发现知识图谱呈现放射状星形——根因是 `yt-system-course-catalog` 等目录类卡片被当成普通实体摄入，成为引力中心。

**操作**：

1. **在 `graph.py` 的 `_build_custom_kg` 中**（约 line 179-208 的 fm_relation_fields 字典），增加：
   ```python
   "diagnostic_relations": "diagnostic trigger",
   "bridges_to": "bridges to",
   ```

2. **过滤元页面**（`_collect_wiki_pages`，line 78-99）：
   - 增加过滤逻辑，跳过 index.md、log.md、contradictions.md
   - 跳过以 `yt-system-` 开头的文件（系统级索引卡）
   - 参考 `search_index.py` line 88-90 的现有过滤逻辑
   - 详细方案见 `30_wiki/decisions/proposal-graph-rag-star-fix.md`
   
2. **frontmatter 格式**（概念卡中可选字段）：
   ```yaml
   diagnostic_relations:
     - target: "target-card-id"
       relation: "applies_when"    # 可选值: applies_when / contrasts_with / requires_input
       description: "描述在什么场景下触发"
   ```

3. **Graph RAG 查询增强**（`_find_cross_domain_bridges` 或新增函数）：
   - 在查询结果中，如果某实体的入边包含 `diagnostic trigger` 类型，额外标注"该实体可作为当前场景的诊断框架"
   - 这在 `kdo graph query` 的 JSON 输出中新增 `diagnostic_candidates` 字段

**完成标志**：
- 在 `30_wiki/concepts/yt-foresight-business-spectrum.md` 中加一条测试用的 diagnostic_relations 到 `case-coffee-shop-foresight`
- 手动 `kdo graph ingest --full` 后，`kdo graph query "想开咖啡馆" --json` 能看到 `diagnostic_candidates` 字段

### E4：kdo diagnose 命令原型（3-5天，E1-E3 完成后启动）

**⚠️ 这个现在不启动**。等 E1-E3 完成 + 老顽童在 5 张以上的卡中填了 diagnostic_signals 后，再评估是否需要做。

### E5：新增 `10_raw/literature/` 目录 + source_refs 规范（0.5h）

**背景**：王语嫣识别出知识库需要引入经典商业文献（麦肯锡、明托、丰田等）作为概念卡来源。当前 `source_refs` 只支持 inbox 文件和 10_raw/sources 文件路径，没有引用出版物的标准格式。

**操作**：

1. **`templates.py` 的 `REQUIRED_DIRS` 中追加 `10_raw/literature`**
2. **在 `90_control/schemas/` 下写一个 `source_refs 规范.md`**，定义引用出版物的标准格式：
   ```yaml
   # 引用格式
   - "Author, I. (Year). *Title*. Edition. Publisher."
   # 示例
   - "Rasiel, E. (1999). *The McKinsey Way*. McGraw-Hill."
   - "Minto, B. (2009). *The Pyramid Principle*. 3rd ed. FT Press."
   ```
3. **`10_raw/literature/README.md`** 中记录已引用过的著作清单，避免同一本书被不同卡以不同格式引用

**完成标志**：
- `kdo init` 后 `10_raw/literature/` 自动存在
- `90_control/schemas/source-refs-standard.md` 已写入引用格式规范

---

## 总体原则

- **先单后全**：先在 1 张卡（终局光谱图）上手动填 diagnostic_signals 做验证，再批量铺开
- **不破坏现有功能**：diagnostic_signals 和 diagnostic_relations 都是可选字段，缺省时所有现有行为不变
- **bridges_to 只用于跨域桥接**：一堂体系内部的关系用已有的 `related`/`component_of` 字段，bridges_to 专门用于连接不同知识体系（如一堂体系↔经典商业框架）
- **读纠正记录**：`60_feedback/corrections/corr_20260611_laowantong-机会预判域-OCR遗漏+旧卡未清理.md` 理解 P-7 教训

---

## ⏸️ 待欧阳锋确认（回复后继续）

以下两项不需要立即做，等欧阳锋确认后再动：

### Pending 1：Task E 整体进度确认

当前已知 E3（graph.py 过滤+边类型）已完成 `commit 72a7d60`。请回复：
- E2（diagnostic_signals + bridges_to schema + `kdo validate --v15` WARN 校验）是否已完成？
- E5（`10_raw/literature/` 目录 + source_refs 规范）是否已完成？
- 如果全部完成 → Task E 关门。如果还有剩余 → 欧阳锋调整优先级。

### Pending 2：将来 `kdo validate` 增加链接密度校验

欧阳锋新增了三条审查标准（Bridge 节 / bridges_to / Synthesis ≥5 链接），目前靠人工审查。长远看如果 `kdo validate` 能对以下情况报 WARN 会更高效：
1. framework/tool/case 卡缺 `bridges_to` 字段（如果它的 domain 包含跨域标签）
2. Synthesis 节 wikilink 数量 < 5

这不是当前优先级。等 E2/E3/E5 全部稳定后再评估是否需要做。

---

## 黄药师回复（2026-06-11）

### Pending 1：Task E 进度确认

E1-E3+E5 全部完成，E4 暂缓。建议 Task E 关门。

| 子任务 | 状态 | commit / 证据 |
|:--|:--:|:-----|
| E1 目录注册 | ✅ | `templates.py` — `60_feedback/diagnosis` 已注册 |
| E2 diagnostic_signals | ✅ | `quality.py` `_check_diagnostic_signals()`，v15 validate WARN |
| E2 bridges_to | ✅ | `graph.py` `fm_relation_fields` 新增 `"bridges_to": "bridges to"` |
| E3 diagnostic_relations | ✅ | Graph RAG "diagnostic trigger" 边类型，dict 格式支持 |
| E3 bridges_to | ✅ | 同上，复用已有 dict 处理逻辑 |
| E3 index 过滤 | ✅ | `_collect_wiki_pages` 过滤 index/log/contradictions/links + type=index/catalog/meta |
| E5 literature 目录 | ✅ | `templates.py` — `10_raw/literature` 已注册；`90_control/schemas/source-refs-standard.md` 已写；`10_raw/literature/README.md` 已建 |
| E4 kdo diagnose | ⏸️ | 等老顽童在 ≥5 张卡上填 diagnostic_signals 后启动 |
| KDO CLI | ✅ | pytest 526/528 pass；commit `72a7d60` |
| 终局光谱图试金石 | ✅ | 3 diagnostic_signals + 3 diagnostic_relations 已填 |

### Pending 2：链接密度校验

同意应该做但**现在不急**。三个理由：

1. `bridges_to` 和 `diagnostic_relations` 刚建立，需要老顽童先在 10+ 张卡上填数据，再校验——校验空字段没意义
2. Synthesis wikilink < 5 的阈值需要先看实际分布。现有 1,100+ 卡可能 70%+ 低于此阈值——直接报 WARN 噪音太大
3. 建议等老顽童按新标准跑 2-3 批卡后，抽样看实际链接密度分布，再定阈值和校验规则

**建议节奏**：Task E 关门 → 老顽童积累数据 → 链接密度校验作为 Task F 或并入 E4 评估。

黄药师
2026-06-11

---

## 欧阳锋追加（2026-06-11）— 桥接卡试点通过后的跟进

老顽童的桥接卡试点（MECE + Issue Tree）已通过审查。但卡分别放在了 `30_wiki/frameworks/` 和 `30_wiki/tools/` 目录——这两个不在 `_collect_all_wiki_pages` 的扫描列表中。需要你在 `graph.py` 的 `_collect_all_wiki_pages` 中追加这两个目录：

```python
wiki_subdirs = [
    root / "30_wiki" / "concepts",
    root / "30_wiki" / "frameworks",   # 新增
    root / "30_wiki" / "tools",         # 新增
    root / "30_wiki" / "systems",
    root / "30_wiki" / "entities",
    root / "30_wiki" / "decisions",
    root / "30_wiki" / "projects",
]
```

做完重建索引：`kdo graph rebuild --full`。5 分钟的事。

---

## ✅ Task F（新增）：生产者体验 + 五步法审计

> 用户指令：检查"一堂五步法"还缺少什么，你作为建造者尝试动手做下生产者，从而理解基础设施的迭代方向。

### 背景

你是 Builder，平时只建工具不改卡片。这次请你**临时做一次 Producer**，亲身走一遍内容生产流程，感受摩擦点在哪。这不是让你替代老顽童，是让你**通过动手理解工具链的痛点**。

### 操作

#### 第一步：审计五步法覆盖

现行五步法体系下各步的卡片覆盖：

| 步骤 | 卡数 | 判断 |
|:----|:---:|:-----|
| 需求分析 | 25 张 | 充足 |
| 产品内核 | 8 张 | 有核心卡，可能有缺口 |
| 商业模式/单元模型 | 54 张 | 非常充足 |
| 增长 | 7 张 | 可能缺实操卡 |
| 壁垒 | 5 张 | 可能缺实操卡 |

先读已有的核心卡：
- `yt-five-step-method.md`（总纲）
- `yt-entrepreneur-five-step-method.md`（工具卡）
- `yt-five-step-implementation.md`（落地实操）
- `yt-five-step-common-pitfalls.md`（暗知）
- `yt-five-step-level-blindspots.md`（暗知）

判断：**五步法还缺什么？** 比如缺某一步的实操案例？缺某一步和某一步之间的衔接说明？缺跨步骤的对照？

#### 第二步：选一个缺口，动手生产

选一个你认为最明显的缺口，产出 1 张卡。可以是缺的 case / skill / dk 卡。

**用 `kdo produce` 创建骨架 → 手动填充 → `kdo validate` 检验。** 完整走一遍生产线。

#### 第三步：记录摩擦点

在 `60_feedback/diagnosis/huangyaoshi-producer-experience.md` 中记录：
1. **工具链摩擦**：`kdo produce` / `kdo validate` / `kdo enrich` 哪个环节最卡？缺什么功能？
2. **内容生产摩擦**：三步编译法哪一步最难下手？模板缺少什么字段？
3. **你的建议**：如果你是 Builder，会改什么让 Producer 更顺畅？

### 产出

1. 审计结论（写在同一个文件里，标记为 "## 五步法审计"）
2. 至少 1 张新卡（内容卡，非工具代码）
3. 摩擦点文档 → `60_feedback/diagnosis/huangyaoshi-producer-experience.md`

### 完成标志

欧阳锋审查：
- 审计结论是否有洞察
- 新卡是否通过 `kdo validate`
- 摩擦点文档是否识别到真正的系统性问题

---

## ✅ 黄药师 Task F 交付（2026-06-11）

### 产出

| # | 交付物 | 路径 |
|:--|:-----|:-----|
| 1 | 审计结论 + 摩擦点 | `60_feedback/diagnosis/huangyaoshi-producer-experience.md` |
| 2 | 三方对齐总结 | `60_feedback/diagnosis/huangyaoshi-task-f-synthesis.md` |
| 3 | 新卡 1 | `case-five-step-growth-first-lever` — 增长第一步：何时开始 + 第一个杠杆（v1.5 PASS） |
| 4 | 新卡 2 | `case-five-step-fake-vs-real-barriers` — 真假壁垒判别 + 六个月测试 + 抄不了测试（v1.5 PASS） |
| 5 | 新卡 3 | `concept-five-step-growth-to-barrier-transition` — 增长→壁垒切换时机 + 三个信号（v1.5 PASS） |
| 6 | P0 bug 修复 | `quality.py` — 表分隔符兼容 `|:---|` 对齐格式（commit `4258419`） |

### 核心发现

**五步法不缺"每一步怎么做"（100+ 张卡），缺"步与步之间的桥"**——什么时候能从 N 步跨到 N+1 步。三张新卡全部围绕"衔接判断"展开，补了最薄弱的三个衔接点。

### 建议给欧阳锋

1. **审查三张新卡**：特别关注 diagnostic_signals 是否对王语嫣的诊断工作有用（目前只有终局光谱图和这三张卡有 diagnostic_signals）

2. **老顽童下一步**：续产"产品内核→商业模式"的衔接卡（五步法剩余最大盲区）+ "产品内核验证通过"的判断标准技能卡

3. **黄药师工具链待修**：
   - P0：`kdo scaffold` 增加创建新卡功能（目前只能补信号，不能建新卡。Producer 写卡全是手写 YAML）
   - P1：`kdo enrich` / `kdo graph query` 集成到写卡流程，自动推荐关联卡片
   - P2：diagnostic_signals scaffold 预填（enrich 已有预填，scaffold 待补）

4. **Task E 关门**：E1-E3+E5 全部完成（详见上文黄药师回复），E4 等老顽童积累 diagnostic_signals 数据后启动

5. **桥接卡标准确认**：本次三张卡全部满足 Brideg / bridges_to / Synthesis≥5 链接三项标准。建议以此作为后续桥接卡的审查门槛。

黄药师
2026-06-11
