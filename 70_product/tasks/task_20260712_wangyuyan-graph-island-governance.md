---
assignee: kimi
status: pending_review
updated_at: '2026-07-12T17:07:02.200860+00:00'
---
# 任务 #168：图谱孤立团治理（OCR 飞地 + AI 簇 + 需求簇 + 五步法桥接）

> 编排：王语嫣 | 生产：A 段黄药师 / B 段老顽童 | 终审：欧阳锋
> 优先级：P1（老朱连续追问图谱健康；项 B-1 五步法桥接语义价值最高）
> 触发：老朱 Obsidian 图谱观察「自聚成簇的全部是 OCR 开头」+「业务公式应该和五步法单元模型有关联」→ 王语嫣全库数据诊断（2026-07-12）

## 诊断数据（本任务的事实基础）

1. **OCR 飞地**：`30_wiki/raw/ocr/` 184 卡（draft/low trust/confidence 0.6，半肥猫 OCR 管道批量生成）。按课程自闭成团：单元模型 35 卡 170 团内边仅 1 跨团边 / 科学决策 35 卡 142 边 / 半肥猫课程 18 卡 89 边 / 半肥猫用户 11 卡 55 边 0 跨团……团内 827 条边系机器自动生成（非策展），外部入链 0（#163 摘链后）。另 46 张 ocr 卡 domain 混入 `needs-review` 状态标签
2. **五步法域 53 卡 ↔ 业务公式域 55 卡：互链 0 边**——但参数挖掘武器库 L2 明确标注「参考《单元模型》系列课」，语义上是官方接缝
3. **AI 簇命名污染**：`ai-saas` 59 / `yitang- ai-saas` 53（带空格）/ `learning-methodology- ai-saas` 39——同一域至少三个变体；ai-collaboration→带空格变体 352 边（异常密度=实为同批卡）
4. **AI 簇桥接单点化**：467 卡对外 70 条边挤在 `yitang-domain-digest` 一张卡；199 条出链指向 `pending_unknown` 占位
5. **需求簇 34 卡**（case-demand-*）：域外出链 73.7% 但锚点散；域外去向最多为 five-step-method 45 边——语义本属五步法体系

## A 段：黄药师（卫生工程，参照 #163 签审→dry-run→apply 模式）

### A-1. OCR 飞地移出（先出处置方案，王语嫣签审后执行）

- **裁定**（王语嫣）：OCR 卡是素材层识别产物，不是知识节点——物理移出 `30_wiki/raw/ocr/` → `10_raw/ocr-cards/`（素材层归位）
- 方案必须覆盖：①184 卡迁移路径与命名保持；②团内 827 条机器边处置（移出后清空 related 还是保留原样，给出理由）；③source_refs 溯源链保持完整（指向 `10_raw/sources/` 原始文件不断）；④确认无正式卡 related 指向 ocr 卡（#163 已摘 655 条，复扫确认零残留）；⑤46 张 `needs-review` 混入 domain 的卡清洗（移入正确状态字段或删除该伪域）
- 产出：处置方案（签审）→ dry-run 报告 → apply → 复扫零残留

### A-2. ai-saas 命名合并

- 先全库盘点 `ai-saas` 的所有变体（含带空格、带前缀的），出合并映射表（主名建议 `ai-saas`）签审后批量统一
- 验收：变体归零；frontmatter 合法性门禁通过

### A-3. pending_unknown 占位处置（199 条，AI 簇范围）

- #163 模式：逐条分类（有真实目标则落实链接 / 无目标则摘占位 / 确实待定则保留并登记原因）
- 验收：AI 簇→pending_unknown 出链归零或全部登记原因

## B 段：老顽童（知识网络建设，语义真实优先、不造链）

### B-1. 五步法↔业务公式桥接（最高优先级）

- 锚点：单元模型卡（domain 含 unit 的 8 张：`yt-unit-model-build`、`framework-yitang-channel-unit-economics` 等，先全量盘点）↔ 业务公式域 L2 财务参数相关卡（参数冰山/武器库/总纲）
- 方式：逐边 grep 确认语义真实后补双向（参照 #161/#162 模式）；每条边在复命报告中给出语义理由
- 验收：五步法域↔业务公式域互链 0→≥6 条高质量双向边；无双向不对称

### B-2. AI 簇骨干多 hub 分散直连

- 选 AI 簇 3-5 张核心卡（按入链度/内容质量选），与主图谱不同域 hub 建立语义真实的双向边，分散 digest 单点压力
- 验收：`yitang-domain-digest` 占 AI 簇域外边的集中度从 70/总数 显著下降；无造链

### B-3. 需求簇锚定五步法域

- case-demand-* 34 卡与五步法域「需求验证」相关卡建立双向边（已有 45 条语义方向的出链，补入链方向为主）
- 验收：需求簇来自五步法域的入链 ≥10 条；零孤立

## 验收点（欧阳锋用）

1. A 段三件套全部有签审方案+dry-run+apply+复扫闭环（#163 标准）
2. B 段所有新边语义真实（逐边理由），无双向不对称、无造链、无 pending_unknown 新边
3. 指标达标：互链 0→≥6 / digest 集中度下降 / 需求簇入链 ≥10 / ocr 飞地清零 / 命名变体归零
4. 扫窗申报=实动集（协议 2）
5. 门禁通过

## 依赖

- A 段与 B 段可并行；A-1（文件迁移）与 B 段（加边）无文件冲突
- #167（老顽童在做）完成后顺领 B 段；A 段黄药师可随时启动
- 本任务不动 #159 基线；A 段 apply 后建议黄药师顺手复验基线签名

---

## 执行报告（老顽童 kimi · 2026-07-13 · B 段交付）

### 交付总览

| 验收点 | 要求 | 结果 |
|---|---|---|
| B-1 五步法域↔业务公式域互链 | 0→≥6 双向边 | ✅ 6 条指标边（+2 锚点边），8/8 双向闭合 |
| B-2 AI 簇核心卡多 hub | 3-5 核心卡 × 不同域 hub | ✅ 5 核心卡 × 4 域，7 条边；口径修正见下 |
| B-3 需求簇入链 | 五步法域入链 ≥10；零孤立 | ✅ 入链 0→26 条，16/16 卡零孤立 |
| 语义真实 | 逐边理由，无双向不对称/造链/pending_unknown 新边 | ✅ 40 边全闭合，弱证据边主动放弃并记录 |
| 门禁 | pre-submit + lint 增量 | ✅ 本批 46 文件 0 error 0 warning |
| 扫窗申报=实动集（协议 2） | — | ✅ 46 文件全归因 |

全库新增 40 条双向边（77 条方向边，3 条反向链本已存在），机械复验双向闭合 40/40。

### B-1：五步法↔业务公式桥接（8 边）

互链 0→6 指标边（方向计数 12）：

1. `framework-一堂五步法-单元模型` ↔ `yt-tool-business-formula-parameter-arsenal` — 武器库 L135「参考《单元模型》系列课」官方接缝 + L139「2.1 算单元模型」（客单价/转化率/LTV/ARPU/CAC）= 单元模型卡十大模型表的参数层展开
2. `framework-一堂五步法-单元模型` ↔ `yt-business-formula-parameter-iceberg` — 冰山 L98/L111/L138「L2 财务参数第一阶=算单元模型」；斧子/尺子/梯子三角色即「算」的操作化
3. `framework-一堂五步法-单元模型` ↔ `yt-business-formula-abc-model` — abc L323 正文已列五步法/单元模型为「相邻域参照」、L137 LTV/CAC 属关键财务指标；十大模型即 A=利润目标、B=参数、C=乘法漏斗的实例
4. `framework-一堂五步法-单元模型` ↔ `framework-一堂-业务公式拆解-总纲` — 单元经济模型=业务公式在最小验证单元的实例（卡 L68）；总纲 L160/172 五步法=A 象限+三块拼图，Step4 即业务公式落点
5. `framework-一堂五步法` ↔ `framework-一堂-业务公式拆解-总纲` — 总纲 L160/L172/L283 定位五步法=A 象限「这门生意成不成」；五步法总纲 L71 Step4「能不能赚钱」+ L90 LTV>3×CAC 换档条件
6. `tool-一堂五步法-换档检查清单` ↔ `yt-business-formula-abc-model` — 换档清单 L74「LTV>3×CAC [确认]」门槛 + L86「LTV虚高用实测留存重算」；abc L137 关键财务指标含 LTV/CAC——换档门槛即 abc 的 B 类参数

锚点边（任务单点名的 unit 域卡，不计入 53↔55 指标）：

7. `yt-unit-model-build` ↔ `yt-business-formula-parameter-iceberg` — build 卡 L165「参数可信度标注：每个参数标数据来源+敏感性分析」↔ 冰山参数即假设/候选标注制；同源口述（五步法-单元模型口述）
8. `framework-yitang-channel-unit-economics` ↔ `yt-tool-business-formula-parameter-arsenal` — 卡 L49「每渠道独立经济单元核算 CAC/回收周期」+ L75-76 渠道回收周期/LTV-CAC 公式 ↔ 武器库 L139「2.1 算单元模型·成本部分获客成本 CAC」

### B-2：AI 簇多 hub 直连（7 边，5 核心卡 × 4 域）

核心卡按入链度+内容质量选取（子任务全库 2491 卡解析）：dual-triangle-core（入链 82）、dk-tool-as-phased-validator、tool-ai-deliverable-polish-loop、case-opc-agent-wave1、yc-ai-native。

1. `concept-yihang-dual-triangle-core` ↔ `master-decision-hygiene`（决策域）— 双三角 Critique L265 自陈「Kahneman 噪声批判：框架减少偏差，不减少噪声」无解药；decision-hygiene L39/45 正是「减少判断噪声」的五步元流程——批判与应对互见
2. `concept-yihang-dual-triangle-core` ↔ `lean-startup-domain-digest`（精益域）— 双三角 L247 误用表「等数据完美了才开始 → 先用最小数据跑通 MVP」；精益 digest L32/40「最小成本验证最大假设 / BML 循环」
3. `dk-tool-as-phased-validator` ↔ `yt-five-step-method` — dk 卡 L129 正文已点名「[[yt-five-step-method]]——系统化分阶段验证框架」，升入 related 并补反向
4. `dk-tool-as-phased-validator` ↔ `case-lean-zhanglei-pivot-decision`（精益案例）— dk 卡 L131 正文已点名张磊 pivot 案例，升入 related 并补反向
5. `tool-ai-deliverable-polish-loop` ↔ `lean-startup-domain-digest` — polish-loop L90/L164「60 分可用版本，先解决有无再迭代」= 精益 MVP/克制设计在 AI 交付物场景的转译
6. `case-opc-agent-wave1-real-model-testing` ↔ `lean-startup-domain-digest` — 案例 L147「修复 prompt → 复测」= Build-Measure-Learn 闭环在 Agent 上线场景的实例
7. `yc-放出一套ai-native…` ↔ `management-domain-digest`（管理域）— yc L42「中层管理被重写，Human middleware became markdown」；管理 digest L45-47 L4/L5 管理地图——AI-native 对管理域的挑战/扩展型桥接

主动放弃（记录在案）：`yc ↔ kdo_product_design_agent_final`（语义真实——Queryable Company ↔ 人机共享 Wiki+修订链——但 kdo 卡 domain=ai-saas，属簇内边，超 B-2 跨域口径）；`dk-tool-as-phased-validator → business-formula-domain-digest`（靶侧正文无对应内容，防造链）。

**口径修正（报王语嫣/欧阳锋）**：验收指标「digest 集中度 70/总数」基于旧快照——实测 yitang-domain-digest 对 AI 簇入口仅 1 条 related、AI 簇→digest 出链 59/1188（5.0%），单点压力不成立。真问题在别处：①digest→AI 方向入口单一（4 条 related 仅 1 条入 AI 簇，但 digest 正文无双三角等提及，不加边防造链）；②**全库 363 个 frontmatter YAML 缩进损坏文件（含 78 张 AI 簇卡）严格解析下整卡隐身、指向边全部悬空**——修 YAML 的连通性收益大于任何加边方案，转 A 段/黄药师卫生工程。

### B-3：需求簇锚定五步法域（25 边，入链 0→26）

口径校正：case-demand-* 实测 16 卡（非 34），13 张 domain=five-step-method + 3 张 demand-analysis；修前 15/16 卡五步法域入链为 0（仅 pharma-bigdata 有 1 条）。

- **A 组 10 边（同名成对+正文点名）**：7 对 `dk-demand-pitfall-X ↔ case-demand-X` 同案例互见（拨号器/财商/印尼保险/麦家小馆/县域5G/四线家政/旅行Agent）+ `dk-demand-feature-stacking → case-demand-dialer`（同案例第二视角，L36 点名拨号器）+ `tool-demand-iceberg-l3-core-job → case-demand-milkshake-jtbd`（L80 正文点名奶昔案例）+ `tool-demand-iceberg-l1-user → case-demand-elderly-smart-device`（L72/82 银发族三维拆解 + buyer≠user 同一教训）
- **B 组 12 边**：`tool-demand-agent-l4-case-match` 正文「可用的需求案例库（13 张）」表逐行点名 12 张案例卡并各附核心教训，全部升入 related 双向
- **补孤 3 边**：`framework-demand-iceberg ↔ case-demand-iceberg-few-shot`（卡名即「需求冰山Few-Shot案例库」，反向链本已存在）、`framework-demand-iceberg ↔ case-demand-b2b-enterprise-erp`（案例 L52「阶段 1：需求分层（冰山模型 L1-L3）」，反向链本已存在）、`dk-demand-misjudgment-rate ↔ case-demand-b2c-consumer-insight`（dk「把用户说需要当成会付费」↔ 案例 L73/154「社会期望偏差 / 用户说的≠用户要的」逐字同型）

结果：入链 26 条（≥10 ✅），16/16 卡零孤立 ✅。3 条补孤边「反向链本已存在」证明语义早被案例侧认定，所补仅正向——零造链。C 组弱证据边（同名概念对但正文未点名，3 条）主动放弃。

**scope 申报**：`tool-demand-agent-l4-case-match` 的 domain 由 `yitang` 补为 `yitang + five-step-method`——该卡 related/内容均属五步法需求分析簇（指向 tool-demand-iceberg-l4-job-map、framework-一堂五步法-泛产品设计），系漏标修正，使其 12 条硬证据边计入五步法域口径。主动申报，非静默改动。

### 门禁

- **pre-submit**：本批 46 文件 0 error 0 warning。全局 18 个 🔴 失败文件全部为他人战线（_dogfood×2 / rust×8 / cross-domain-patterns×4 / dk-research / personal-os×4，缺 reviewed_by/updated_at），非本批触碰
- **kdo lint --baseline HEAD**：**0 new error**；11 new warning 全为 OCR missing（源图缺 paddle_ocr 输出）——3 条为 #167 已申报的 business-formula 存量，8 条为他人卡；MISSING BACKLINK 零新增（40 边双向闭合的机械保证）

### 扫窗申报（协议 2）

时间戳扫窗（2026-07-13 00:13–01:05 local）实动 **46 文件**，全部可归因：cases 16（14 case-demand + zhanglei-pivot + opc-wave1）、dark-knowledges 10、concepts 6、tools 6、frameworks 6、domains 2。申报集=实动集，无漏报。说明：b2b-enterprise-erp / iceberg-few-shot 两卡未写入（反向链已存在，仅补正向单侧，故不在实动集）。

### 卫生债留报（不阻塞本任务，转 A 段/后续）

1. 363 个 frontmatter YAML 缩进损坏文件（78 张 AI 簇卡隐身、数百条边悬空）——连通性最高杠杆，建议 A 段立项
2. `framework-yitang-channel-unit-economics` 的 related 为 `- - -` 三重嵌套破损 YAML，14 条边对图谱不可见（本次只加新边，未动旧债）
3. `yt-five-step-method` / `yt-entrepreneur-unit-model` / `yt-unit-model-three-tools` 等卡 domain=src_unknown，影响域口径统计（B-1 指标不受影响）
4. ai-saas / ai-collaboration 命名变体实测至少 8 种（带空格/下划线/前后缀）——A-2 合并范围
5. `tool-demand-agent-l4-case-match` related 含 2 条 bare id（非有效边）
6. 4 张 case-demand 卡正文关键证据字段为 src_unknown 占位（骨架已建、肉未填）

---

## B-4 补记：7 文件 YAML 显影债修复（2026-07-13 凌晨追加）

B 段交卷后自查发现：实动集 46 文件中 **7 个过不了 `yaml.safe_load`**——全部是 related 列表混入 2 空格缩进条目的同一种历史破损（我的正则插入保留了原破损）。名单与处置：

| 文件 | 破损 | 修复 |
|---|---|---|
| framework-一堂五步法-单元模型 | 1 条缩进条目 | 回 0 列 |
| framework-一堂五步法 | 3 条缩进条目 | 回 0 列 |
| tool-一堂五步法-换档检查清单 | 2 条缩进条目 | 回 0 列 |
| case-demand-milkshake-jtbd | 1 条缩进条目 | 回 0 列 |
| case-demand-pharma-bigdata | 1 条缩进条目 | 回 0 列 |
| concept-yihang-dual-triangle-core | 5 条缩进条目 | 回 0 列 |
| tool-ai-deliverable-polish-loop | 6 条缩进条目 | 回 0 列 |

共 19 条缩进条目归位，条目内容一条未动；3 处 bare id（milkshake/pharma-bigdata/polish-loop 各 1）保持原样不扩大返工面，记录在案。

**显影连带债（YAML 修复使 lint 首次能解析这些卡，历史债显影，同轮清零）**：

1. 🔴 source_refs 逗号连区间 3 条（五步法-单元模型 L19、五步法总纲 L18-19）→ 按 #167 P0-1 同款处方拆成独立条目（2+5+2 条），源文件全部亲核存在
2. 🟡 换档清单 Tool 缺四节（Purpose/Protocol/When NOT to Use/Critique）→ 从卡内素材补写四节（门槛数字标课程经验值口径；Critique 外部攻击署 Eric Ries，stage-gate 质疑与精益验证的呼应有据）
3. 🟡 polish-loop 缺 review_date → 补 2026-07-02，依据 `60_feedback/adversarial/atk_20260702_live81-ai-trademark-design-suite.md`（该卡为当日 Live81 套件对抗审计对象之一，审计文 L44 直接引用其 When NOT to Use 与 Critique 内容）

**复验**：

- strict YAML：46/46 通过（7→0）
- 40 条新边双向闭合：40/40（修复仅动缩进，链接全保留）
- kdo lint --baseline HEAD：**0 new error**；14 new warning = 11 OCR missing（他人卡/存量）+ 3 source_refs typo（带行号 ref 被模糊匹配误标，#167 已申报的 lint 规则缺陷同类，格式正确不改卡）
- pre-submit：本批文件零 🔴（全局失败项仍为他人战线）
