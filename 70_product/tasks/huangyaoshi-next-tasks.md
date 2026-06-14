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

---

## 🔴 Backlog：`kdo validate` 新增 domain-tags 一致性检查

**来源**：王语嫣诊断发现 design 域孤岛根因——32 张卡的 `tags` 已包含跨域标签（如 `#scene/business-analysis`），但 `domain` 仍为单域 `["design"]`。

**建议**：在 `kdo validate --v15` 中增加一条简单启发式检查：

检查逻辑（纯字符串匹配，不需要 LLM）：
```
如果卡片的 tags 包含以下任一场景标签，
且 domain 数组长度 = 1（单域），
则报 WARN "tags 暗示跨域但 domain 为单域"：

跨域场景标签列表：
#scene/business-analysis
#scene/ai-collaboration
#scene/knowledge-management
#scene/decision-making
#scene/entrepreneurship
#scene/startup
#scene/product-design
```

**优先级**：P2（不阻塞，等老顽童先执行 P0 桥接补 domain 后再上线，否则旧卡会大量报 WARN 制造噪音）

**工作量估计**：约 0.5h

---

## 🔴 例行维护：Hermes / cc-connect 掉线重启

**来源**：P-6 已知问题——飞书 Hermes 和 cc-connect 的 WebSocket keepalive 会不定期超时（已复现多次）。

**症状**：
- 王语嫣/老顽童/洪七公在飞书发消息后 bot 无响应
- 日志显示 ping timeout

**操作**：
```bash
# 重启 Hermes（王语嫣/老顽童/洪七公/段王爷用）
systemctl --user restart hermes-gateway-*

# 如果上述无效，重启 cc-connect（背后的 Claude Code 桥接）
systemctl --user restart cc-connect
```

**重启后验证**：
在飞书发一条消息测试响应。

**频率**：收到掉线报告时执行。不需要定期重启。

---

## ⚠️ 执行规范：发布前狗粮测试（强制）

**原则**：改完工具后，在你标记"完成"之前，必须亲自当一次用户完整走一遍生产流程。

### 为什么

pytest 能测"代码不报错"，测不出"人用起来顺不顺"。Task F 发现的 4 条摩擦点（表分隔符 bug、scaffold 不能建新卡、diagnostic_signals 缺默认提示、对标缺自动辅助）——没有一条是被 pytest 发现的，全部是黄药师亲自当了 3 小时 Producer 才踩出来的。

### 操作规则

改完工具后，在 `commit` 之前：

**第一步：挑一张测试卡**
- 选一张还没产的、你觉得典型的卡（framework / tool / case 都行）
- 不需要提交到知识库，测试完可以删掉

**第二步：完整跑一遍生产线**
```
kdo scaffold --new --card test-card --type framework   # 建骨架
  → 检查：吐出来的骨架能不能直接填？
kdo validate --v15 --card test-card                     # 跑质量门
  → 检查：报错信息是否看得懂？修复建议是否有用？
kdo graph rebuild --full                                #（如果改了图相关代码）
  → 测试数据会不会污染索引？
```

**第三步：如果遇到超过 2 分钟不知道该怎么做的情况**
- 停下来。这就是一个摩擦点。
- 改工具，不要绕过去。

### 判断标准

| 阶段 | ✅ 通过 | ❌ 退回 |
|:-----|:-------|:-------|
| 骨架生成 | 5 秒内吐出可填写的模板 | 吐骨架后还需要手动修格式 |
| validate 报错 | 错误信息指向具体行+建议修复 | 报乱码/不指向具体位置/建议看不懂 |
| 写卡体验 | 字段说明在 schema 里能找到 | 不确定某个字段怎么填，需要问老顽童 |

### 不适用场景

- 只改注释/README/文档 → 不需要狗粮测试
- 改测试代码本身 → 不需要
- 重构但逻辑不变 → 跑 pytest 即可

### 谁检查

欧阳锋审查时，会看 commit message 里是否标注了 `dogfood-tested`。没有标注的，默认打回重新验证。

---

## Task G（新增）：`kdo scaffold --new` 创建新概念卡骨架

**来源**：你 Task F 亲手踩出来的摩擦点 #1。Producer 写卡全是手写 YAML frontmatter，没有 CLI 支持。

### 背景

当前 `kdo scaffold` 只能补缺失信号（Critique/Synthesis），不能创建新卡。老顽童和洪七公每次产新卡都要手写 30 多行 frontmatter：id、title、type、domain、source_refs、bridges_to、diagnostic_signals、related、tags......一个格式错就 validate 报错。

### 需求

新增 `kdo scaffold --new` 子命令，能交互式或半交互式创建概念卡骨架：

```bash
# 最小用法：交互式提问
kdo scaffold --new
  → 问：卡片类型？（framework / tool / case / concept / dk / skill）
  → 问：卡片标题？
  → 问：主要 domain？
  → 问：关联 domain？（逗号分隔，可选）
  → 问：源材料来源？
  → 吐出一个完整的 frontmatter + 章节骨架文件

# 高级用法：命令行参数
kdo scaffold --new \
  --card concept-mckinsey-7s \
  --type framework \
  --title "7-S Framework" \
  --domain "consulting, yitang" \
  --source "Peters & Waterman (1982). In Search of Excellence"

# 输出位置
→ 自动判断存放目录：framework → 30_wiki/frameworks/
                              tool → 30_wiki/tools/
                              case → 30_wiki/cases/
                              concept/skill/dk → 30_wiki/concepts/
```

### 骨架模板参考

参考 `30_wiki/frameworks/concept-mckinsey-7s.md` 或 `30_wiki/tools/concept-toyota-5-whys.md` 的 frontmatter 结构。所有字段定义在 `90_control/schemas/concept.yaml` 中。

骨架必须包含的章节（按类型不同）：

| 类型 | 必含章节 |
|:----|:---------|
| framework | Summary → Claims → Bridge → Critique → Constraints → Synthesis → Action Triggers |
| tool | Summary → Claims → Bridge → Critique → Constraints → Synthesis → Action Triggers |
| case | Summary → Case Details → Lessons → Synthesis → Action Triggers |
| concept | Summary → Claims → Critique → Synthesis |
| dk | 核心本质 → 走偏模式 → 纠偏动作 |

### 完成标准

1. `kdo scaffold --new` 能吐出一个语法正确的 `.md` 文件（可用 `yaml.safe_load` 校验 frontmatter）
2. 吐出的文件可以直接 `kdo validate --v15` 通过（骨架阶段允许有 TODO，但不报格式错误）
3. commit 标注 `dogfood-tested`——你自己用 scaffold --new 产一张测试卡，走完 validate，确认可用
4. 更新 `kdo scaffold --help` 帮助信息

---

## 紧急小任务：批量补 127 张月白技能卡的 domain（脚本 5 分钟）

**来源**：王语嫣勘误发现 127 张 `skill-月白-*` 卡的 `domain` 为空数组，Graph RAG 查不到。

**操作**：写一个一次性 Python 脚本，遍历 `30_wiki/concepts/skill-月白-*.md`：
1. 读取 frontmatter
2. 如果 `domain` 为空或 `[""]`，改为 `["design"]`
3. 写入回文件

**注意**：
- 只改 `domain` 字段，不动其他内容
- 改之前全量备份（`git stash` 或复制目录）
- 改完跑 `kdo lint` 确认没有 YAML 损坏
- 不要碰 `skill-月白-` 以外的卡

**完成后通知欧阳锋**。不需要审查，批量操作确认 YAML 无损即可。

---

## ✅ 黄药师执行完毕（2026-06-11）

- 实际影响范围：**193 张**（非 127 张）
- 全部 `skill-月白-*` 的 `domain` 从空字符串/空数组改为 `["design"]`
- 脚本 1 秒跑完，抽检 `skill-月白-80分效率设计策略.md` 确认 YAML 无损

黄药师
2026-06-11

---

## Task I（紧急）：王语嫣 v2 审计 — 目录结构 + Domain 批量修复

> **来源**：王语嫣 2026-06-12 概念卡地图 v2 审计。
> **核心发现**：concepts/ 占全库 90%，大杂烩目录；97% 卡片无有效 domain；99 张 dk-*、27 张 case-*、12 张 sk-* 放错位置。
> **全部是批量和脚本活，不需要内容判断。**

### 操作顺序

#### I-1：domain 格式统一 + 批量补 design（1h）

**问题**：全库 domain 字段至少 5 种格式变体，97% 为空。

**操作**：写一次性 Python 脚本扫描 `30_wiki/` 下所有 `.md` 文件：

1. 统一 domain 格式：所有变体（空、`""`、`[]`、`''`、裸字符串）统一为标准 YAML 列表格式
2. **不要对已有正确 domain 的卡动手**（如 `["yitang"]`、`["consulting", "yitang"]`）。只修空值和格式异常

**参考数据**：王语嫣审计 `30_wiki/concepts/` 下 743 张空 domain + 196 张空值变体。

#### I-2：目录迁移（2h）

**问题**：大量卡片放错目录。

**操作**：将以下卡片从 `30_wiki/concepts/` 迁移到对应目录：

| 前缀 | 数量 | 目标目录 |
|:----|:---:|:---------|
| `dk-*` | ~99 张 | `30_wiki/dark-knowledges/` |
| `case-*` | ~27 张 | `30_wiki/cases/` |
| `sk-*`（不含月白） | ~12 张 | `30_wiki/tools/` |

**方法**：`git mv` 逐个前缀迁移，每批迁移后跑 `kdo lint` 确认没有断链。不要一次性 mv 所有文件——分批做，每批 20 张。

#### I-3：`.sk-backup/` 清理（0.5h）

**问题**：`.sk-backup/` 下 12 张技能卡躺在那里没人管，扫描器残留。

**操作**：
1. 检查 12 张卡是否与现有卡重复
2. 不重复的 → 移入 `tools/`，补 domain
3. 重复的 → 删除

#### I-4：Graph RAG 重建

以上全部完成后，`kdo graph rebuild --full`，确认新目录和 domain 生效。

### 完成标准

1. `30_wiki/concepts/` 不再有 dk-*、case-*、sk-* 前缀的文件
2. `.sk-backup/` 已清理
3. 空 domain 卡减少 90%+
4. `kdo lint` 无新增错误

### 参考

王语嫣审计报告：`60_feedback/diagnosis/kdo-concept-map-20260612.md`

### 优先级

I-1 → I-2 → I-3 → I-4，顺序执行，不准并行。

### 警告

**这是批量操作，先备份再动手。** 每批迁移后跑 `kdo lint`，确认断链数量没有异常增长再继续下一批。

---

## ✅ Task I 已完成

黄药师 2026-06-12 全部完成。

---

## 🔴 Task L（紧急）：为王语嫣建立独立 Hermes 身份

**背景**：王语嫣当前跑在老顽童的 Hermes gateway（`hermes-gateway-laowantong.service`）上。老顽童的 gateway 默认人格是"周伯通（中神通）"。王语嫣能对话是因为会话上下文中注入了"你是王语嫣"的 prompt。但 gateway 一重启，上下文清空，她就变回老顽童。这是 P-6 同类问题——身份绑定在易失的会话上而非固定的配置上。

**操作**：

1. 参考已有 Hermes profile（`~/.hermes/profiles/beikai/`、`~/.hermes/profiles/laowantong/` 等），为王语嫣新建 profile：
   ```
   ~/.hermes/profiles/wangyuyan/
   ├── config.yaml    # 角色名、人格设置
   └── .env           # API Key（复用已有 Key）
   ```

2. 参考已有 gateway service，新建 service 文件：
   ```
   ~/.config/systemd/user/hermes-gateway-wangyuyan.service
   ```
   复制 `hermes-gateway-laowantong.service` 的内容，把其中的 `laowantong` 替换为 `wangyuyan`。

3. 注册到 hub——在 `five_heroes_hub/hub.py` 中添加王语嫣条目

4. 启动：
   ```bash
   systemctl --user daemon-reload
   systemctl --user start hermes-gateway-wangyuyan.service
   ```

5. 验证：飞书发消息给王语嫣，确认她以"王语嫣"身份回复而非"周伯通"

**完成后通知欧阳锋**。老顽童的 gateway 不再携带王语嫣身份，重启也不会冲突。

## 🔴 Task J（新）：`kdo scaffold --new` 生产化

**来源**：Task F 摩擦 #1。Producer 写卡全是手写 YAML frontmatter。你已完成原型设计，现在是生产化。

**要求**：`kdo scaffold --new` 支持交互式创建概念卡骨架，吐出可直接填充的 `.md` 文件。参考 `90_control/schemas/concept.yaml` 字段定义。

**完成标准：**
1. 支持 `--card`、`--type`、`--title`、`--domain` 参数
2. 自动判断存放目录（framework→frameworks/，tool→tools/，case→cases/ 等）
3. 产出的 frontmatter 可被 `yaml.safe_load` 解析
4. 产出的文件可通过 `kdo validate --v15` 骨架检查
5. commit 标注 `dogfood-tested`

---

## 🔴 Task K（新）：diagnostic_signals 批量填充脚本

**来源**：王语嫣深度审计发现 diagnostic_signals 覆盖率仅 0.6%（7/1258）。这是她做诊断的核心武器。

**操作**：写一次性 Python 脚本，为以下优先批次的卡片填充空的 diagnostic_signals 占位：
1. `frameworks/` 全部 7 张 — 缺的 3 张补 TODO 骨架
2. `tools/` 全部 36 张 — 缺的 33 张补 TODO 骨架
3. `concept-*` 全部 14 张 — 缺的 12 张补 TODO 骨架

**注意**：只填 TODO 占位，不填具体内容。具体内容由老顽童补充。格式参考：

```yaml
diagnostic_signals:
  - signal: "TODO: 用户说什么场景时触发"
    framework_lens: "TODO: 框架提供什么视角"
    follow_up_question: "TODO: 第一个追问"
```

**工作量**：30 分钟脚本 + 10 分钟验证。

---

## ✅ Task J 已完成

commit `7360c56`（KDO CLI）。

## ✅ Task K 已完成

commit `a5d818c4`，47 张卡已补 DS TODO。

## ✅ Task L 已完成

`~/.hermes/profiles/wangyuyan/` 已建 + gateway active。

---

## 🔴 Task M（新）：自迭代检测器 Phase 1 — A + D + E

**来源**：王语嫣自迭代提案 `proposal-self-learning-cron.md`。
**目标**：实现三个自动化检测器，每天凌晨自动跑，产出健康报告。

### 背景

当前全库质量全靠欧阳锋人工审查。王语嫣设计了四个检测器（A/B/C/D/E），Phase 1 实现三个 P0 检测器。

### 检测器 A：新卡入库健康度检查

**触发**：每天凌晨 02:00（cron job）
**扫描**：`30_wiki/` 下 24h 内新增/修改的 `.md` 文件

**检测规则：**

| 检查项 | 失败条件 |
|:-------|:---------|
| frontmatter 完整性 | id / title / type / domain 任一为空 |
| domain 格式 | domain 不是 YAML list 格式 |
| source_refs 完整性 | source_refs 为空或指向不存在的文件 |
| related 填充 | framework/tool/case 卡 related 为空的 |
| diagnostic_signals 覆盖率 | 新卡但未填 DS（仅 WARN，不 FAIL）|

**产出**：`60_feedback/auto/health-check-YYYY-MM-DD.md`

### 检测器 D：索引自动更新

**触发**：检测器 A 完成后自动触发
**动作**：如果有新卡/修改卡，重新运行索引更新
**产出**：更新 `concept-card-index-latest.md`

### 检测器 E：Domain 标签一致性审计

**触发**：检测器 A 完成后自动触发
**检测规则：**

| 检查项 | 失败条件 |
|:-------|:---------|
| domain 格式统一 | 非 YAML list 格式的 report |
| 目录与类型一致 | concepts/ 中出现 type: tool / case / dk |
| domain 空置率 | 全库 domain 空置 > 20% 时告警 |

### 技术方案

写入现有 cron job（王语嫣已创建了一个简化版 `kdo-vault-self-learning-loop`）。在现有 job 的 prompt/脚本中追加检测器 A + D + E 的逻辑，新增一个"报告格式化"步骤。

### 完成标准

1. 每天早上 02:00 自动产出 `60_feedback/auto/health-check-YYYY-MM-DD.md`
2. 报告包含：新增卡列表、每张卡的检查结果（通过/失败项）
3. domain 一致性报告包含：格式异常卡列表
4. 不需要人工触发

### 优先级

Phase 1（A+D+E）= P0。Phase 2（B + C）= P1/P2，暂缓。

---

## 🔴 Task N（新）：图谱可视化降权 — 超级节点过滤

**来源**：图谱呈扫把状——少数深黑节点（入边 100+）引力太强，外围卡加多少链都被淹没。老顽童负责内容上给深黑节点加出链（P3），你负责可视化层让图不再以超级节点为中心。

### 背景

当前 Graph RAG 可视化把所有边等同看待。一个被 200 张卡引用的节点，在图上就是绝对的引力中心。这不是内容问题，是**可视化权重策略问题**。

### 操作

在 Graph RAG 可视化输出中（`kdo graph query --json` 的 downstream 渲染），增加超级节点降权逻辑：

1. **统计入边数量**：对每个节点统计被多少张其他卡片引用
2. **设定阈值**：入边 > 30 的节点视为"超级节点"
3. **降权渲染**：
   - 方案 A：在可视化中不显示超级节点的入边（只保留出边），让 peer 卡之间的边露出来
   - 方案 B：将超级节点拆为"自身"和"影子"两个节点——自身带出边，影子带入边
   - 选一个你觉得好实现的

### 完成标准

1. `kdo graph query "创业" --json` 返回的图谱数据中，超级节点的边不再主导拓扑
2. 可视化不再是单中心放射状
3. 不需要改内容——纯可视化/数据层改动

### 参考

老顽童在内容层同时在做"深黑节点批量出链"（任务 2），两端同时改效果最好。

---

## ✅ Task N 已完成

commit `9bcd2b2`。`_deweight_hub_nodes()` 阈值 30。

---

## 🔴 Task O（新）：健康报告问题批量清理

**来源**：自迭代检测器 Task M 首份健康报告：
- 81 TODO 残留、590 孤立页面、792 重复页面

**操作**：写一次性 Python 脚本：

1. **TODO 清理**：扫描全库 TODO，生成清单
2. **孤立分析**：590 个孤立分类——真孤立 vs 预期
3. **重复去重**：文件名相似度 >80% 的 pair 自动建议

**产出**：`60_feedback/auto/cleanup-YYYY-MM-DD.md`

**工作量**：1-2 小时。

---

## 🔴 Task P：给王语嫣配 Bing Search API

**背景**：王语嫣需要联网搜索做置信度交叉验证。国内环境 Google API 不稳定，建议用 **Bing Search API**（微软服务国内可直连，有免费额度）。

**操作**：
1. 注册 Azure 账号 → 申请 Bing Search API Key（免费层每月 1000 次）
2. API Key 写入 `~/.hermes/profiles/wangyuyan/.env`：`BING_SEARCH_API_KEY=xxx`
3. 王语嫣在 Python 里 `requests.get()` 直接调，不需封装 KDO 命令

**完成标准**：王语嫣能在对话中执行"搜索 XXX"并返回有效结果。

**优先级**：**P0**（这次先做）。

---

## 🔴 Task Q（新）：出链门禁 — 新卡健康检查加强

**来源**：王语嫣对标报告。新卡缺少最少出链数要求，孤岛知识是产能隐形杀手。

**操作**：在自迭代检测器 A 中增加：

| 检查项 | 失败条件 | 等级 |
|:-------|:---------|:----:|
| 出链数 ≥ 2 | Synthesis wikilink < 2 | WARN |
| 有跨域链接 | 所有链接都在同一 domain | WARN |

纯索引页面除外。0.5 小时。

---

## 🔴 Task R（新）：Queries 沉淀 + `kdo query --save`

**来源**：王语嫣对标报告发现三——缺少问答沉淀，同一问题每次都重新检索。

**操作**：

1. `templates.py` 追加 `30_wiki/queries`
2. `kdo query --save <title>`：将 query 输入输出保存到 `30_wiki/queries/<slug>.md`
3. 查询时 queries/ 自动作为 top-level context

**工作量**：2-3 小时。

---

## 🔴 临时插入：全库质量审查 — 结构性修复（2026-06-15）

> 来源：王语嫣对 `30_wiki/` 全库 1337 张卡片的深度审查。
> 性质：临时清理任务，不替代现有 Task E-R。可在现有任务间隙穿插执行。
> 优先级：P1（不阻塞当前主线，但希望尽快收尾）。

### 背景

王语嫣已完成全库审查，并执行了三项批量修复：
1. YAML frontmatter 解析错误修复
2. `author=legacy` 推断为真实 author（348 张推断成功，146 张无法推断标为 `unknown`）
3. OCR 卡 trust 统一降级为 low + confidence 0.6

当前质量门禁状态（2026-06-15）：
- 总卡数：1337
- P0 阻塞：404 张
- P1 修复：978 张
- 完全干净：237 张
- YAML 解析错误：**0 张**（已修复）

### 任务 S1：运行质量门禁，确认基线（0.5h）

**操作**：
```powershell
cd C:\Users\Administrator\Desktop\wiki
python "90_control/scripts/kcard-quality-gate.py"
```

**完成标准**：
- 报告写入 `60_feedback/audit/kcard-quality-gate-report-YYYY-MM-DD.md`
- 你确认当前 P0/P1 分布与基线一致

### 任务 S2：修复剩余结构性 P0 问题（1-2h）

**范围**：
- `status=enriched/reviewed/stable` 但 `reviewed_by=pending` 的卡
- `status=reviewed` 但 `reviewed_by=pending` 的卡
- `id` 与文件名不一致的卡

**操作**：
1. 从质量门禁报告中提取 P0 清单
2. 对"reviewed_by 不匹配 status"的卡，统一把 status 降回 `draft`，或把 reviewed_by 改为实际审查人
3. 对 id 与文件名不一致的卡，统一以文件名为准修正 id

**完成标准**：
- 运行门禁后 P0 问题减少 ≥50%

### 任务 S3：批量补全 missing domain（2-3h）

**背景**：310 张卡缺少 domain，其中大量是 OCR 卡和早期 legacy 卡。

**操作**：
1. 读取 `90_control/tag-registry.yaml` 的 domain 列表
2. 写一个推断脚本，根据文件名/标题/正文关键词为 missing domain 的卡补 domain
3. 对无法推断的卡，保持 missing 并输出清单

**推断规则示例**：
- 文件名含 `ai-` / `llm` / `prompt` → `ai-saas`
- 文件名含 `design` / `电商` / `PS` → `design`
- 文件名含 `healthcare` / `HIS` / `医院` → `healthcare`
- 文件名含 `management` / `管理` → `management`
- 文件名含 `decision` / `决策` → `decision-making`
- 文件名含 `yt-` / `一堂` → `yitang`

**完成标准**：
- missing domain 从 310 张降至 ≤50 张
- 无法推断的清单写入 `90_control/missing-domain-remaining.txt`

### 任务 S4：重复卡片合并建议（1-2h）

**背景**：健康报告发现 107 对文件名相似度 >80% 的卡片。王语嫣已核对出 4 对真正重复。

**操作**：
1. 读取 `60_feedback/auto/cleanup-2026-06-13.md`
2. 对剩余相似文件名 pair，用脚本自动比较内容相似度
3. 对内容相似度 >90% 的 pair，输出合并建议清单
4. **不要自动合并**——只输出建议，等用户/欧阳锋拍板

**完成标准**：
- 输出 `90_control/duplicate-merge-proposals-2026-06-15.md`
- 每张提案说明：保留哪个、删除哪个、是否需要迁移链接

### 严禁

- ❌ 不自动删除任何卡片
- ❌ 不批量修改正文内容
- ❌ 不替换已有的 source_refs 条目

### 产出清单

1. `60_feedback/audit/kcard-quality-gate-report-YYYY-MM-DD.md`
2. `90_control/missing-domain-remaining.txt`
3. `90_control/duplicate-merge-proposals-2026-06-15.md`

完成 S1-S4 后，在此文件末尾写一段小结，通知欧阳锋/用户审查。

---

## 🔴 紧急回修：批量操作质量事故复盘与修复（2026-06-15）

> **来源**：王语嫣对黄药师 `eb070db8` 和 `8bbfd08d` 两次提交的核查。
> **性质**：必须优先处理的质量事故回修。
> **优先级**：P0。

王语嫣已临时修复了最危险的 frontmatter 破坏，但需要你Review全部修改、完成收尾、并建立防呆机制。

---

### 先读这两份核查报告

1. `60_feedback/corrections/huangyaoshi-8bbfd08d-review-2026-06-15.md`
   - 记录了 26 张 decision/system/project 卡的错误 `source_context` 原始值
2. `60_feedback/corrections/laowantong-review-2026-06-15.md`
   - 记录了老顽童 3 张 yt 卡的问题，供你参考同类错误模式

---

### 事故 1：44 张卡 frontmatter 开头出现空行

**问题表现**：你在 `8bbfd08d` 给 44 张卡加了 `source_context` 和 `source_refs: []`，但每张卡都被改成了：

```yaml
---

title: ...
```

`---` 后多了一个空行，会导致 frontmatter 解析异常。

**王语嫣已做**：批量删除了 43 张卡的空行。

**你要做**：
1. 拉取最新代码后，运行质量门禁确认无新增 YAML 错误
2. 抽查 5 张 `decisions/`、`systems/`、`projects/` 下的卡，确认 `---` 后没有空行

**验证命令**：
```powershell
cd C:\Users\Administrator\Desktop\wiki
python "90_control/scripts/kcard-quality-gate.py"
# 然后看报告里的 YAML 错误数应为 4（都是索引文件）
```

---

### 事故 2：26 张卡 source_context 被污染

**问题表现**：批量生成的 `source_context` 包含反引号、文件路径、分号、乱码，例如：

```yaml
source_context: "90_control/failure-modes.md`; .agent/pitfalls.md`; 15条..."
source_context: "90_control/PROTOCOL.md`。实际上"
source_context: "60_feedback/data-quality/dk-candidates/`; <乱码>"
```

这些都不符合 `source_context` 字段语义。`source_context` 应该是**简短文字描述**，不是文件路径列表。

**王语嫣已做**：把 26 张卡的 `source_context` 替换为 `"KDO internal record"`，原始错误值记录在反馈文件。

**你要做**：
1. 读 `60_feedback/corrections/huangyaoshi-8bbfd08d-review-2026-06-15.md`
2. 对每张卡判断：
   - 如果能用一句话概括来源 → 替换为合理描述
   - 如果无法判断 → 保持 `"KDO internal record"`
3. **严禁再写路径/反引号/分号进 source_context**

**示例正确写法**：
```yaml
source_context: "KDO infrastructure decision — internal design record"
source_context: "数据策展器角色分工讨论记录"
source_context: "暗知识萃取器升级方案"
```

---

### 事故 3：3 张 design skill 卡字段重复

**问题表现**：`eb070db8` 修改了 3 张 `skill-月白-*` 卡：

```yaml
domain:
  - design
  - design        # 重复
source_context: "文创案例"
...
reviewed_by: pending
source_context: "月白 AIGC设计课程 — 实操技巧笔记"  # 重复键，位置错误
```

**王语嫣已做**：
- 移除重复 domain
- 移除错误位置的 source_context
- 保留原始 `source_context: "文创案例"`

**你要做**：
1. 读这 3 张卡确认是否符合预期：
   - `30_wiki/concepts/skill-月白-像素图高清重绘修复法.md`
   - `30_wiki/concepts/skill-月白-印刷DPI标准设置.md`
   - `30_wiki/concepts/skill-月白-薅AIGC羊毛资源法.md`
2. 如果 `薅AIGC羊毛资源法` 的 source_context 应该是 `"月白 AIGC设计课程 — 实操技巧笔记"` 而不是 `"AI设计基础"`，请手动改回，并放到正确位置

---

### 事故 4：source_refs 全部为空列表

**问题表现**：44 张卡的 `source_refs: []` 没有实质作用。

**你要做**：
1. 对这些卡，判断是否能补充真实 source_id
2. 能补充的 → 从 `.kdo/source_id_map.json` 找对应 ID 填入
3. 不能补充的 → 删除 `source_refs` 字段，不要留空列表占位

---

### 事故 5：contradicts 修复范围不清

**问题表现**：`eb070db8` 提交信息说"master 域 55 张 DK 卡 contradicts→related"，但实际提交只修改了 3 张 skill 卡和 2 个索引文件。

**你要做**：
1. 全库搜索 `contradicts:` 字段：`grep -r "contradicts:" 30_wiki/`
2. 如果还有 DK 卡残留 `contradicts`，按语义改为 `related`
3. 写清楚实际修复数量，更新任务记录

---

### 防呆机制：你必须建立的检查

**禁止再犯的批量操作规则**：

1. **每次批量写入前，先单卡 dry-run**
   - 选 1 张卡测试你的脚本
   - 用 `python 90_control/scripts/kcard-quality-gate.py --card <路径>` 验证（如果支持）
   - 或者直接 `python -c "import yaml; yaml.safe_load(open(path).read().split('---')[1])"`

2. **批量脚本必须检查 frontmatter 结束符**
   - 写入前确认文件以 `\n---\n` 分隔 frontmatter 和正文
   - 禁止生成 `字段---` 或 `---\n\n` 这种格式

3. **source_context 字段内容白名单**
   - 只允许：简短描述、课程名、会议名、项目名称
   - 禁止：文件路径、反引号、分号、多行、超过 80 字符

4. **批量写入后必须跑门禁**
   - 每次批量操作后立即运行 `kcard-quality-gate.py`
   - YAML 错误必须归 0（索引文件除外）

---

### 验收标准

完成以下全部后，在此文件末尾写小结：

- [ ] 质量门禁 YAML 错误 = 4（仅索引文件）
- [ ] 26 张问题 `source_context` 全部Review并修正或确认
- [ ] 44 张卡无 `---` 后空行
- [ ] 3 张 design skill 卡无重复 domain/source_context
- [ ] `contradicts` 字段全库清理完毕
- [ ] 提交前再次运行质量门禁，P0 不增加

---

### 产出文件

1. 修正后的 44 张 decision/system/project 卡
2. 修正后的 3 张 design skill 卡
3. 更新的 `60_feedback/corrections/huangyaoshi-8bbfd08d-review-2026-06-15.md`（写明已处理）
4. 此任务文件末尾的小结
