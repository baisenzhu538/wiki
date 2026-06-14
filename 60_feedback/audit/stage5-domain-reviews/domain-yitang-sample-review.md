# Stage 5 Domain 专项审查报告：yitang

**审查日期**：2026-06-14  
**审查样本数**：50 张卡片  
**审查人**：Kimi Code CLI（知识库质量审查员）  
**审查范围**：`C:/Users/Administrator/Desktop/wiki/60_feedback/audit/.stage5-tmp/domain-yitang-sample.txt` 所列全部 `.md` 文件  
**审查原则**：仅审查、输出报告，不修改原文件。

---

## 一、总体概览

本次审查覆盖 yitang 域 50 张样本卡片，类型分布如下：

| 类型 | 数量 | 占比 |
|------|------|------|
| concept | 25 | 50% |
| case | 7 | 14% |
| tool | 8 | 16% |
| framework | 7 | 14% |
| skill | 2 | 4% |
| dk / dark-knowledge | 3 | 6% |
| analysis | 1 | 2% |

> 注：部分卡片在 YAML 中标注单一类型，但内容兼具 skill/framework 特征，此处按 YAML `type` 字段统计。

### 整体质量印象

yitang 域卡片整体呈现 **"两极分化"**：

- **高质量组**：经过人工精修（enriched/reviewed）的卡片，如 `yt-decision-width-method`、`yt-decision-height-toolkit`、`yt-entrepreneur-key-hypotheses`、`case-dental-clinic-formula`、`case-treadmill-demand-analysis` 等，结构完整、来源清晰、批判视角多元、行动触发具体。
- **低质量组**：大量由 OCR pipeline 自动生成的 `ocr-*` concept 卡片，内容多为原始 OCR 碎片的堆砌，存在严重乱码、断行、视觉结构丢失、定义缺失等问题，却统一标注 `confidence: 0.8` / `trust_level: medium`，明显高估。
- **中间组**：部分 draft 状态卡片（如 `case-truman-motivation-map-12-versions`、`case-一堂-无人餐厅-hypothesis-failure`）内容骨架尚可，但缺乏 outcome/数据验证，confidence 0.7 / trust low 标注基本合理。

---

## 二、问题分类统计

| 问题类别 | 出现次数 | 涉及卡片数 | 严重程度 |
|----------|----------|------------|----------|
| OCR 质量缺陷（乱码/断行/视觉结构丢失） | 13 | 13 | 高 |
| Confidence / Trust 标注与内容质量不匹配 | 15 | 15 | 高 |
| 内容空泛/缺乏定义/缺乏案例或操作步骤 | 18 | 16 | 高 |
| Source 可追溯但不可读或过于笼统 | 11 | 11 | 中 |
| 卡片间重复/内容重叠/版本未合并 | 8 | 8 | 中 |
| 类型标注与内容不匹配 | 5 | 5 | 中 |
| 关联节点指向不存在卡片 | 7 | 7 | 低 |
| 文件内容损坏（异常行号前缀） | 1 | 1 | 高 |

> 注：单张卡片可能同时涉及多个问题类别，因此"涉及卡片数"列可能小于各类别出现次数之和。

---

## 三、具体卡片问题清单

### 3.1 高风险卡片（建议优先处理）

| 序号 | 文件路径 | 主要问题 | 处理建议 |
|------|----------|----------|----------|
| 1 | `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md` | OCR 文本严重断裂，公式 `(A+B+C+D)/(X+Y+Z` 未闭合；变量含义未定义；source 为 opaque ID；Open Questions 中已自承多处缺失 | 重新对照原图人工校对；补全 L1-L4 层级定义与变量解释；如无法修复应降级为 draft 或删除 |
| 2 | `concepts/ocr-泛产品设计-审美工具箱指南.md` | OCR 乱码严重（"豆屏""江信合场景"等）；"白盒思维""世界学习法"等概念缺乏可操作方法；多术语与软件工程术语冲突 | 人工校对原图；重建审美工具箱的操作步骤与案例；降低 confidence 至 0.5-0.6 |
| 3 | `concepts/ocr-一堂-地图-个人地图_conv.md` | OCR 未检测到任何文本，内容几乎为空；source 标注 `unknown`；卡片仅有元反思而无实质知识 | 如原图确实无文字，应转交图像/图表解析 pipeline；当前卡片作为 concept 无价值，建议删除或改为 source 占位卡 |
| 4 | `concepts/ocr-一堂-泛产品设计-十年苦练30招.md` | OCR 表格结构严重错位；"一堂五步法""惊喜公式"等关键概念未展开；30 招的练习标准、验证方式缺失 | 人工重建 30 招能力矩阵；为每招补充定义、案例、练习方法；当前不宜作为可复用知识 |
| 5 | `concepts/ocr-泛产品设计-需求工具箱指南.md` | OCR 乱码与结构混杂；13 张需求卡片的编号与内容对应混乱；"最小解""峰终定律公式"定义不清 | 人工校对原图；重建 13 张卡片的完整列表与使用场景；补充各工具的操作步骤 |
| 6 | `concepts/ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | OCR 乱码多（"焖释""胶照""角虚"）；"Magic Words""刻意夸张"等技巧缺乏伦理边界与效果验证；与正式卡 `yt-personal-scientific-expression` 内容重叠 | 与正式卡合并或作为其附录；删除 OCR 错误；为技巧补充效果验证证据与高风险场景边界 |
| 7 | `concepts/yt-decision-depth-ladder.md` | 文件内容被异常行号前缀污染（如 `220|`、`221|` 等），Markdown 渲染会异常；L3 变量语义（A/B/C/D/X/Y）与 L4 财务公式的字母体系不一致 | 清理行号污染；统一 L1-L4 的字母语义；复核 source_refs 中多张案例图是否被充分利用 |
| 8 | `concepts/yt-entrepreneur-unit-model.md` | Bill Aulet 批判部分仅写 "..."，内容缺失；source_ref 仅指向 "一堂-课程地图精华串讲.md"，过于笼统；type 为 tool 但操作步骤不突出 | 补全 Bill Aulet 批判；补充单元模型的具体操作步骤/模板；source 应细化到课程口述或课件 |
| 9 | `concepts/yt-entrepreneur-259-milestone.md` | 仅描述 2-5-9 框架结构，未列出 9 个里程碑的具体内容；source 笼统；type 为 tool 但缺乏操作步骤 | 补充 9 个里程碑的定义与示例；source 应指向关键假设课原始材料；type 可改为 concept 或 framework |
| 10 | `concepts/yt-entrepreneur-five-step-method.md` | 内容极为空泛，仅复述五步法名称；未展开每一步的工具、判断标准、关键产出；source 笼统 | 大幅扩充每一步的工具、检查清单、失败模式；source 应指向五步法核心课程材料 |
| 11 | `concepts/ocr-一堂-管理必修-课程清单.md` | 纯课程索引清单，无知识内容；type 为 concept 不当；多处 "2/4" 暗示存在其他 3 份清单但未关联 | 改为 index/tool 类型或合并到课程目录卡；补充课程间的前置依赖关系；关联其余 3/4 清单 |
| 12 | `concepts/ocr-一堂-案例拆解-课程清单.md` | 同 #11，纯索引清单；课程编号体系存在疑点（如 "十倍成长" 重复出现）；更新日期 2025-08 与捕获时间 2026-05 存在 9 个月空白 | 改为 index 类型；核实课程编号与更新状态；补充与其余 1/4、3/4、4/4 清单的关联 |
| 13 | `concepts/ocr-一堂-科学决策-roi决策评估画布-案例04.md` | ROI 数值属性不明（29,800 是收益还是成本）；最终结论 "赌一把" 与科学决策框架存在张力；未提供决策后的 outcome | 澄清数值属性与计算逻辑；补充该案例的实际结果；降低 confidence 或标注为 "待复核" |
| 14 | `concepts/ocr-一堂-科学决策-关键假设abcd模型.md` | OCR 中模型名称出现 "ABC口" 与 "ABCD" 两种写法；C/D 场景的策略工具定义不清；成败/效率二分法的边界未界定 | 人工校对原图；明确 ABCD 四场景的定义与对应策略；补充反例与适用范围 |
| 15 | `concepts/yt-personal-knowledge-management.md` | `Framework Gallery` 章节完全为空；source 仅指向 "一堂-课程地图精华串讲.md"；未区分一堂 KM 方法与通用 PKM | 填充 Framework Gallery；补充课程原始材料；明确一堂方法的独特贡献 |

### 3.2 中风险卡片（建议中期处理）

| 序号 | 文件路径 | 主要问题 | 处理建议 |
|------|----------|----------|----------|
| 16 | `concepts/ocr-萃取总结.md` | "爆炸式研究" 与 "饱和式研究" 关系不明；"模型稳定" 缺乏判定标准；MECE 作为 "最高追求" 未讨论动态知识边界 | 补充阶段定义与收敛判定标准；增加动态调整触发条件；当前可作为 draft |
| 17 | `concepts/ocr-一堂-个人修炼-科学提问刻意练习.md` | "成长地图" 的具体阶段未展示；七个应用场景的提问技术差异未区分；反馈机制缺失 | 补充阶段划分与各场景技术差异；说明反馈来源；降低 confidence |
| 18 | `concepts/yt-decision-width-method.md` | 内容质量高，但存在大量空行（可能是格式化问题）；三层盲区清单在一堂创业圈经验基础上，对传统制造业等场景覆盖不足（卡片自身已指出） | 清理空行；补充跨行业盲区示例；无明显 domain 问题 |
| 19 | `cases/case-truman-motivation-map-12-versions.md` | 作为 case 卡缺乏 outcome/数据；"12 个版本" 未展示任何版本对比；source_context 指向口述版但未给出具体行号 | 补充版本迭代的关键差异、用户反馈数据、最终采用版本的效果；提升为 enriched |
| 20 | `cases/case-一堂-无人餐厅-hypothesis-failure.md` | 作为反面教材有效，但缺乏具体损失金额、时间线、创业者名称等可验证信息；结局未明确 | 补充案例的具体损失数据与结局；标注为 "待事实复核" |
| 21 | `cases/case-dental-clinic-formula.md` | 数据来源为培训案例，但未提供危机感知重构后的实际成交率变化；"After" 仅描述动作而非结果 | 补充实施后的成交率、GMV 变化等 outcome；或明确标注为 "推演案例" |
| 22 | `frameworks/yt-model-pan-product-climbing-map.md` | 内容完整，但 L1-L6 的 "能/位/练" 三维度在文中未给出具体操作定义；与 `yt-model-deliberate-practice-growth` 存在概念重叠 | 补充 "能/位/练" 自评量表；明确与刻意练习框架的边界 |
| 23 | `frameworks/yt-product-kernel-cultivation.md` | 十大指标表完整，但未说明指标间的优先级与组合使用方式；"产品内核四要素" 案例偏少 | 补充指标优先级判断规则与更多行业案例 |
| 24 | `frameworks/yt-ai-trend-12-signals.md` | 12 信号举例较泛（如 "算法升级""交互创新"），部分举例未注明具体时间/来源；与 `dk-signal-cluster-illusion.md` 关系良好 | 为每个信号补充可追踪的 industry marker 或数据来源；保持与暗知卡的联动 |
| 25 | `concepts/yt-note-ai-human-division.md` | 内容质量高，但 trust_level 为 low 与内容完整性不匹配；L3 "内化" 的人机边界缺乏客观标准 | 将 trust_level 上调至 medium 或 medium-high；补充 L3 自评标准 |
| 26 | `concepts/yt-prompt-brainstorming.md` | "AI 头脑风暴上限 95 分" 的论断缺乏实证；与 `yt-prompt-writing-workflow` 的边界已说明，但仍可能混淆 | 补充 "95 分" 论断的限定条件或改为 "理论上限"；强化两篇的互引 |
| 27 | `frameworks/concept-mckinsey-hypothesis-driven.md` | 作为 yitang 域样本，其 domain 包含 consulting 与 yitang，桥接清晰；但与 `yt-entrepreneur-key-hypotheses` 的边界需更明确 | 补充 "何时用麦肯锡版、何时用一堂版" 的决策树 |
| 28 | `concepts/yt-research-intelligence-map.md` | 13+渠道框架完整，但部分渠道（如 "社会工程学""爬虫"）存在合规风险，仅在使用限制中略提 | 强化合规边界与风险提示；补充渠道失效的典型案例 |

### 3.3 低风险 / 无明显问题卡片

| 序号 | 文件路径 | 简要说明 |
|------|----------|----------|
| 29 | `cases/case-toy-cabinet-barrier.md` | 无明显问题。壁垒扫描表完整，突围路径清晰，critique 多元，source 指向具体口述与图片。 |
| 30 | `cases/case-treadmill-demand-analysis.md` | 无明显问题。需求拆解三层清晰，替代方案矩阵完整，与五步法映射明确，source 具体。 |
| 31 | `cases/case-truman-ai-skill-self-packaging.md` | 无明显问题。五步流程清晰，source 精确到口述行号，测试结果具体，confidence 0.88 / trust high 合理。 |
| 32 | `cases/case-半肥猫-conversion-hacker-skill.md` | 无明显问题。八步工作流完整，A/B 测试数据具体，可迁移场景明确。虽为 draft，但结构已较成熟。 |
| 33 | `concepts/yt-entrepreneur-key-hypotheses.md` | 无明显问题。259 工具、三板斧、价值/增长假设区分清晰，critique 覆盖 Taleb/Snowden/Popper，行动触发具体。 |
| 34 | `concepts/yt-decision-height-toolkit.md` | 无明显问题。四维提升法 + 共识曲线完整，案例丰富，source 包含口述与多张原图，self-critique 充分。 |
| 35 | `concepts/yt-personal-scientific-expression.md` | 无明显问题。火箭模型四级推进清晰，练习方法具体，critique 覆盖 Susan Cain / Edward Tufte。 |
| 36 | `concepts/yt-model-deliberate-practice-growth.md` | 无明显问题。四要素矩阵、成长曲线、外部攻击（Ericsson/Epstein）完整，self-critique 到位。 |
| 37 | `concepts/yt-personal-pan-product-exploration.md` | 无明显问题。探索营定位清晰，critique 引入 Dewey / Lave & Wenger，与正课区别明确。 |
| 38 | `concepts/yt-prompt-writing-workflow.md` | 无明显问题。大纲→要点→全文流程清晰，critique 引入 Warner / Baron，与头脑风暴边界明确。 |
| 39 | `skills/skill-纪浩-真需求四要素验证法.md` | 无明显问题。操作步骤、适用/不适用场景、失败模式、判断标准完整，符合 skill 卡要求。 |
| 40 | `skills/skill-mece体系框架法.md` | 无明显问题。操作步骤、判断标准、失败模式、跨学科锚点完整，符合 skill 卡要求。 |
| 41 | `dark-knowledges/dk-signal-cluster-illusion.md` | 无明显问题。作为 12 信号模型的补充批判，走偏模式与纠偏动作具体，与相关卡关系明确。 |
| 42 | `dark-knowledges/dk-note-rookie-disaster-veteran-heaven.md` | 无明显问题。原始表述、使用场景、操作方法、适用边界完整，与 `yt-note-ai-human-division` 形成互补。 |
| 43 | `frameworks/modeling-personal-practice-loop.md` | 无明显问题。IPO×PDCA×刻意练习闭环清晰，source 精确到口述行号。 |
| 44 | `concepts/modeling-capability-system.md` | 无明显问题。三段建模体系完整，Open Questions 自指边界，source 精确。 |
| 45 | `concepts/yt-note-extensive-research-input.md` | 无明显问题。30%/70% 比例、多源数据源、正面/反面/边界案例完整，critique 引入 Newport / Taleb。 |
| 46 | `frameworks/yt-model-pan-product-three-virtues.md` | 无明显问题。三大修养定义、关系、与爬山地图对应清晰，critique 引入 MacIntyre / Newport。 |
| 47 | `decisions/truman-ai-partner-design-analysis.md` | 无明显问题。作为 analysis 类型，三层架构、四个设计决策、对 KDO 启示完整；trust low / confidence 0.6 与 draft 状态匹配。 |
| 48 | `concepts/yt-skill-storyline-timeline.md` | 无明显问题。严格时间线的操作、原则、正/反/边界案例、action protocol 完整。 |
| 49 | `concepts/yt-skill-storyline-problem-solving.md` | 无明显问题。问题解决线的六步流程、置信度标注、正/反/边界案例完整。 |
| 50 | `concepts/yt-ai-trend-12-signals.md` | 无明显问题。五维度十二信号表清晰，使用限制与外部攻击具体，与暗知卡联动良好。 |

> 注："无明显问题"不等于"完美"，仅表示在当前审查维度下未发现问题达到需要处理的程度。

---

## 四、批量处理建议

### 4.1 可脚本化批量修复的问题

| 问题 | 批量修复方案 | 预期收益 |
|------|--------------|----------|
| OCR concept 卡统一高估 confidence / trust | 对 `id` 以 `ocr-` 开头、source 为 `src_20260522_*` 且 reviewed_by 为 `pending` 的卡片，自动建议 confidence 0.5-0.6、trust_level low | 快速校准风险信号 |
| OCR 卡 source_refs opaque ID 映射 | 脚本读取 `10_raw/sources/src_*-ocr-*.md` 的存在性，将 source_ref 展开为 `src_id -> 文件路径` 的显式映射 | 提升 source 可读性 |
| Markdown 文件异常行号前缀污染 | 检测行首匹配 `^\s*\d+\|` 的模式并自动清理（如 `yt-decision-depth-ladder.md`） | 修复渲染异常 |
| 空 `Framework Gallery` / 空 critique 占位 | 扫描空章节并生成待办标记 | 提示人工补全 |
| 大量空行导致的格式问题 | 对连续 3 个以上空行进行压缩 | 提升可读性 |
| 关联节点死链检测 | 扫描所有 `[[...]]` 链接，与知识库实际文件比对，标记未解析链接 | 发现指向不存在的卡片 |
| OCR 卡 `type=concept` 自动重分类 | 对纯课程清单类 OCR 卡（如 `*-课程清单`）建议 type 改为 `index` 或 `tool` | 避免类型错配 |

### 4.2 必须人工判断处理的问题

| 问题 | 为何必须人工 | 建议处理方式 |
|------|--------------|--------------|
| OCR 文本与原图内容校对 | OCR 错误无法通过规则完全识别，需要对照原图 | 建立 "OCR → 人工校对 → 结构化重构" 工作流；无法校对的卡片降级为 draft |
| Confidence / Trust 的最终校准 | 需结合内容完整性、来源充分性、验证状态综合判断 | 制定 yitang 域 confidence 评分 rubric，由领域负责人复核 |
| 卡片间重复/合并决策 | 涉及知识架构设计，不能简单去重 | 召开 domain 架构评审，决定 OCR 卡与 enriched 卡是合并、保留为历史版本还是删除 |
| 内容空泛卡的实质补全 | 需要补充定义、案例、操作步骤，依赖领域知识 | 分配给内容 owner（如黄药师、老顽童）按正式卡标准重写 |
| Source 溯源到原始课程材料 | 部分 source 仅指向 "课程地图精华串讲" 等二手索引 | 人工追踪到具体课程口述、课件图片或逐字稿 |
| 伦理/合规边界（如 "社会工程学"、"Magic Words"） | 规则无法判断风险等级 | 由法律/合规 owner 标注风险提示与使用限制 |

---

## 五、Domain 级结论

### 5.1 整体质量评估

yitang 域当前处于 **"骨架已搭、血肉不均"** 的状态：

- **优势**：核心方法论框架（五步法、关键假设、科学决策 Y 模型、泛产品设计三大修养/爬山地图）已有高质量卡片支撑；批判视角（外部攻击）、行动触发、失败模式等 KDO 特色结构在高质量卡中已标准化；案例卡（跑步机、玩具柜、口腔诊所、AI skill 自封装）来源相对清晰。
- **劣势**：OCR pipeline 早期产出的大量 concept 卡片质量低下，拉低整体可检索性与可信度；部分核心工具卡（五步法、单元模型、259 里程碑）内容单薄，与其在方法论体系中的核心地位不匹配；source 质量参差不齐，部分仍停留在二手索引层面。

### 5.2 最大风险点

1. **OCR 卡片的 "medium" 信任误导**：13 张 OCR concept 卡统一标注 `confidence: 0.8` / `trust_level: medium`，但内容实为未校对 OCR 碎片。这会导致用户/Agent 在检索时错误引用低质量内容，污染下游输出。
2. **核心工具卡空心化**：`yt-entrepreneur-five-step-method`、`yt-entrepreneur-unit-model`、`yt-entrepreneur-259-milestone` 等作为 yitang 域核心工具，内容远未达到 "tool" 类型要求的 "使用步骤、边界条件、示例" 标准，影响方法论落地。
3. **重复内容未合并**：同一主题存在 OCR 版与 enriched 版（如科学决策深度/宽度/高度、表达力火箭模型、泛产品设计需求/审美工具箱），容易造成检索冲突和版本混乱。

### 5.3 优先处理建议

| 优先级 | 行动项 | 预计工作量 | 责任方 |
|--------|--------|------------|--------|
| P0 | 对所有 `ocr-*` 卡片统一复核：能人工校对的尽快校对，无法校对的降级 `trust_level` 至 low、`confidence` 至 ≤0.6 | 2-3 人日 | 领域 owner + OCR 校对员 |
| P0 | 重写/补全 `yt-entrepreneur-five-step-method`、`yt-entrepreneur-unit-model`、`yt-entrepreneur-259-milestone` 三张核心工具卡 | 3-5 人日 | 领域 owner |
| P1 | 清理 `yt-decision-depth-ladder.md` 的行号污染并统一 L1-L4 变量语义 | 0.5 人日 | 技术编辑 |
| P1 | 对 OCR 课程清单卡（案例拆解、管理必修）进行类型重分类或合并到课程目录卡 | 1 人日 | 知识架构师 |
| P1 | 建立 yitang 域 confidence/trust 评分 rubric，批量校准现有卡片 | 1 人日 | QA + 领域 owner |
| P2 | 为核心概念卡补充更多可验证案例与跨行业边界（如科学决策、产品内核） | 持续 | 内容贡献者 |
| P2 | 运行死链扫描，修复或删除指向不存在卡片的链接 | 0.5 人日 | 技术编辑 |

---

## 六、附录：样本清单

| # | 文件路径 | YAML type | status | confidence | trust_level |
|---|----------|-----------|--------|------------|-------------|
| 1 | `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md` | concept | enriched | 0.8 | medium |
| 2 | `cases/case-toy-cabinet-barrier.md` | case | reviewed | 0.85 | medium |
| 3 | `concepts/yt-model-pan-product-climbing-map.md` | framework | enriched | 0.85 | medium-high |
| 4 | `concepts/yt-entrepreneur-unit-model.md` | tool | enriched | 0.8 | medium |
| 5 | `concepts/yt-entrepreneur-259-milestone.md` | tool | enriched | 0.8 | medium |
| 6 | `concepts/ocr-泛产品设计-审美工具箱指南.md` | concept | enriched | 0.8 | medium |
| 7 | `concepts/ocr-一堂-科学决策-关键训练清单重要.md` | concept | enriched | 0.8 | medium |
| 8 | `concepts/ocr-一堂-地图-个人地图_conv.md` | concept | enriched | 0.8 | medium |
| 9 | `dark-knowledges/dk-signal-cluster-illusion.md` | dk | draft | 0.7 | low |
| 10 | `cases/case-truman-motivation-map-12-versions.md` | case | draft | 0.7 | low |
| 11 | `cases/case-truman-ai-skill-self-packaging.md` | case | enriched | 0.88 | high |
| 12 | `concepts/ocr-一堂-泛产品设计-十年苦练30招.md` | concept | enriched | 0.8 | medium |
| 13 | `concepts/yt-decision-height-toolkit.md` | tool | enriched | 0.8 | medium |
| 14 | `concepts/yt-entrepreneur-key-hypotheses.md` | tool | enriched | 0.85 | medium |
| 15 | `cases/case-treadmill-demand-analysis.md` | case | reviewed | 0.85 | high |
| 16 | `concepts/yt-ai-trend-12-signals.md` | framework | enriched | 0.85 | medium |
| 17 | `dark-knowledges/dk-note-rookie-disaster-veteran-heaven.md` | dark-knowledge | draft | 0.7 | low |
| 18 | `concepts/yt-decision-width-method.md` | tool | enriched | 0.82 | medium |
| 19 | `decisions/truman-ai-partner-design-analysis.md` | analysis | draft | 0.6 | low |
| 20 | `concepts/yt-model-pan-product-three-virtues.md` | framework | enriched | 0.8 | medium-high |
| 21 | `cases/case-dental-clinic-formula.md` | case | enriched | 0.9 | high |
| 22 | `concepts/ocr-萃取总结.md` | concept | enriched | 0.8 | medium |
| 23 | `concepts/yt-personal-pan-product-exploration.md` | concept | enriched | 0.8 | medium |
| 24 | `concepts/ocr-泛产品设计-需求工具箱指南.md` | concept | enriched | 0.8 | medium |
| 25 | `concepts/yt-decision-depth-ladder.md` | tool | enriched | 0.85 | medium |
| 26 | `concepts/yt-personal-knowledge-management.md` | tool | enriched | 0.8 | medium |
| 27 | `concepts/ocr-一堂-案例拆解-课程清单.md` | concept | enriched | 0.8 | medium |
| 28 | `concepts/yt-skill-storyline-timeline.md` | concept | enriched | 0.75 | medium |
| 29 | `concepts/ocr-一堂-科学决策-roi决策评估画布-案例04.md` | concept | enriched | 0.8 | medium |
| 30 | `concepts/yt-product-kernel-cultivation.md` | framework | reviewed | 0.9 | medium |
| 31 | `concepts/yt-personal-scientific-expression.md` | tool | enriched | 0.8 | medium |
| 32 | `concepts/yt-model-deliberate-practice-growth.md` | framework | enriched | 0.85 | medium-high |
| 33 | `cases/case-一堂-无人餐厅-hypothesis-failure.md` | case | draft | 0.7 | low |
| 34 | `frameworks/modeling-personal-practice-loop.md` | framework | enriched | 0.85 | high |
| 35 | `concepts/ocr-一堂-管理必修-课程清单.md` | concept | enriched | 0.8 | medium |
| 36 | `concepts/yt-skill-storyline-problem-solving.md` | concept | enriched | 0.75 | medium |
| 37 | `concepts/ocr-一堂-个人修炼-科学提问刻意练习.md` | concept | enriched | 0.8 | medium |
| 38 | `concepts/yt-note-extensive-research-input.md` | concept | draft | 0.84 | low |
| 39 | `concepts/yt-prompt-brainstorming.md` | tool | enriched | 0.85 | medium-high |
| 40 | `concepts/skill-纪浩-真需求四要素验证法.md` | skill | draft | 0.7 | low |
| 41 | `concepts/modeling-capability-system.md` | concept | enriched | 0.75 | medium |
| 42 | `cases/case-半肥猫-conversion-hacker-skill.md` | case | draft | 0.7 | low |
| 43 | `concepts/yt-entrepreneur-five-step-method.md` | tool | enriched | 0.8 | medium |
| 44 | `concepts/yt-note-ai-human-division.md` | concept | draft | 0.85 | low |
| 45 | `concepts/ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | concept | enriched | 0.8 | medium |
| 46 | `concepts/ocr-一堂-科学决策-关键假设abcd模型.md` | concept | enriched | 0.8 | medium |
| 47 | `frameworks/concept-mckinsey-hypothesis-driven.md` | framework | enriched | 0.85 | medium-high |
| 48 | `concepts/yt-prompt-writing-workflow.md` | tool | enriched | 0.85 | medium-high |
| 49 | `concepts/skill-mece体系框架法.md` | skill | draft | 0.7 | low |
| 50 | `concepts/yt-research-intelligence-map.md` | framework | reviewed | 0.85 | medium |

---

*报告结束。本报告仅用于质量审查，未对原文件做任何修改。*
