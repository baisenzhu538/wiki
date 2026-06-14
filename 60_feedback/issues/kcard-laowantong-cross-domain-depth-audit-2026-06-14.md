# 老顽童非药柜专项域知识卡深度审计报告

- **审计对象**：30_wiki 中 `author: 老顽童` 或 `reviewed_by: 老顽童` 的非药柜卡片
- **排除范围**：`smart-medicine-cabinet-*` 系列（广冷电子/药柜域）
- **审计时间**：2026-06-14
- **审计方法**：
  1. 抽样精读代表性卡片；
  2. 并行子代理分域审查（AI 短剧域、建模能力域、其他零散域）；
  3. 交叉核对 source 引用精确性、案例密度、暗知识深度、Critique 质量。
- **报告路径**：`C:/Users/Administrator/Desktop/wiki/60_feedback/issues/kcard-laowantong-cross-domain-depth-audit-2026-06-14.md`

---

## 一、总体结论

**用户怀疑成立**：老顽童在非药柜多专项域的工作中，确实存在明显的「流于形式、暗知识和案例库挖掘不够深」的问题。但问题分布不均：

| 域 | 角色 | 深度评分 | 核心问题 |
|---|---|---:|---|
| 业务公式域 | 作者 | 2.0/5 | 案例库严重不足、暗知识提取不足、L5-L6 本质洞察缺失 |
| AI 短剧域 | 作者/审核 | 2.0/5 | 套模板产出、无真实短剧案例、source 引用流于形式、Critique 套路化 |
| 建模能力域 | 作者/审核 | 2.5/5 | 重框架轻案例、重概念轻暗知识；虽有 dark-knowledges 补充，但主卡整合不足 |
| 其他零散域综合卡 | 审核 | 3.0/5 | 王语嫣生成的草稿本身案例丰富、source 规范；但老顽童作为 reviewer 未推动标准 30_wiki 格式转换，也未补充暗知识 |
| AI PPT 工具 | 作者 | 1.0/5 | 草稿状态、source 薄弱、Critique 引用不可验证 |

**整体判断**：老顽童在「流程完整性」（卡片产出、source 注册、lint 通过）上表现合格，但在「内容深度」（案例库、暗知识、本质洞察、边界条件）上明显不足。其自撰卡片普遍存在「结构完整但内容空泛」的模板化倾向；作为 reviewer 时，对王语嫣综合卡的深度问题把关不严，未能推动其从「主题草稿」升级为「标准知识卡」。

---

## 二、分域详细发现

### 2.1 业务公式域（5 张新卡 + 1 张更新卡）

**卡片清单**：
- `30_wiki/frameworks/yt-business-formula-abc-model.md`
- `30_wiki/concepts/yt-business-formula-ten-paradigms.md`
- `30_wiki/concepts/yt-business-formula-parameter-iceberg.md`
- `30_wiki/concepts/yt-business-formula-six-level-logic.md`
- `30_wiki/cases/case-toc-ecommerce-formula-misjudgment.md`
- `30_wiki/concepts/yt-management-business-formula.md`（更新）

**主要问题**（详细见 `60_feedback/issues/fb_20260614_9e5a2c8b-老顽童业务公式域工作深度审计.md`）：

1. **案例库严重不足**：source 中至少包含 9 个完整案例（私域电商、ToB SaaS 续费、口腔诊所、连锁餐饮、在线教育、连锁健身等），但只产出 1 张案例卡。
2. **暗知识提取不足**：「先切分再拆转化」「+ 关系 = 有一个就够了」「× 关系 = 缺一不可」「满意度不是续卡率的直接原因」「每个定性参数需 3-5 个行为指标」等关键暗知识未被充分写入。
3. **L5-L6 本质洞察缺失**：未提取各行业的「魔法参数」/本质公式（如学习本质、客户成功本质、口腔诊所危机感知公式等）。
4. **十大范式组合应用未展开**：真实业务往往需要组合多个范式，但卡片只讲单个范式适用场景。

**评分**：2.0/5

---

### 2.2 AI 短剧域（7 张卡片）

**卡片清单**：
- `30_wiki/concepts/ai-short-drama-ice-fire-scripting-compass.md`
- `30_wiki/frameworks/ai-short-drama-ice-fire-dissection-compass.md`
- `30_wiki/tools/ai-short-drama-plot-three-axes.md`
- `30_wiki/tools/ai-short-drama-script-planning-three-axes.md`
- `30_wiki/tools/ai-short-drama-framework-three-axes.md`
- `30_wiki/tools/ai-short-drama-conflict-three-axes.md`
- `30_wiki/concepts/ai-short-drama-platform-policy-comparison.md`

**主要问题**：

1. **无真实短剧案例**：7 张卡片中没有引用任何真实短剧名称、平台数据、爆款拆解实例或代俊隆团队实际操盘细节。所有 Claims 都是对培训材料的概念转述。
2. **Source 引用流于形式**：部分 Claims 缺少精确行号，或只引用图片 OCR 摘要（`src_20260613_*-*.md:11-14`），未追溯到口述原文的具体段落。
3. **Critique 套路化**：每张卡片的「外部攻击」都是套用罗伯特·麦基、约瑟夫·坎贝尔、乔治·普罗蒂等名人，但这些引用与 source 无关，是模型生成的「标准批评模板」，缺乏对卡片内具体 Claims 的逐条反驳。
4. **Confidence 设置不合理**：6 张工具/框架卡清一色 `confidence: 0.75 / trust_level: medium`，未根据证据强度差异化。实际应降至 0.55-0.65。
5. **缺少暗知识**：未涉及短剧行业真实潜规则，如平台审核红线、题材生命周期、投放 ROI 与剧本过稿率的关系、AI 生成剧本的实际修改成本、编剧与平台买方的博弈等。

**评分**：2.0/5

---

### 2.3 建模能力域（5 张卡片 + 若干 dark-knowledges）

**卡片清单**：
- `30_wiki/concepts/modeling-capability-system.md`
- `30_wiki/frameworks/modeling-three-stages.md`
- `30_wiki/tools/modeling-level-map.md`
- `30_wiki/tools/modeling-weapon-library.md`
- `30_wiki/tools/process-modeling.md`

**主要问题**：

1. **重框架、轻案例**：卡片对「流程建模→抽象建模→本质提炼」的框架描述完整，但缺少 Truman 课程中的具体建模案例（如一堂如何把某一节课从经验沉淀为模型）。
2. **暗知识在主卡中整合不足**：虽然 domain 中存在 `dk-modeling-*` 系列暗知识卡（如及时复盘 session 窗口、解释性本质 vs 预测性本质、案例大爆炸的底气等），但这些暗知识未被有效链接和整合进主卡。
3. **Critique 深度不均衡**：`modeling-level-map` 和 `modeling-weapon-library` 有 Critique 但多为名人观点（Bloom、Tufte、Deming），`modeling-capability-system` 和 `modeling-three-stages` 只有 Open Questions，缺少系统反思。
4. **工具卡缺少具体使用步骤**：`modeling-weapon-library` 列出了清单、雷达图、冰山图等模型，但未给出每个模型的具体操作步骤、典型场景和常见错误。

**优点**：source 引用基本规范；dark-knowledges 系列补充了部分深度。

**评分**：2.5/5

---

### 2.4 其他零散域（10 张卡片）

**卡片清单**：
- `30_wiki/concepts/ai-hackathon-pitches.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/business-validation-models-collaboration.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/finance-legal-business-operations.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/industry-ai-cases.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/personal-growth-complex-systems.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/product-business-strategy.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/supply-chain-beverage.md`（王语嫣生成，老顽童 review）
- `30_wiki/concepts/yitang-methodology-system.md`（王语嫣生成，老顽童 review）
- `30_wiki/frameworks/ai-methodology-tools.md`（王语嫣生成，老顽童 review）
- `30_wiki/tools/yt-tool-ai-ppt-maker.md`（老顽童自撰）

**主要问题**：

1. **前 9 张是主题综合草稿，非标准 30_wiki 格式**：它们缺少标准知识卡的 `Claims / Constraints / Critique / Synthesis / Action Triggers` 结构，而是以「核心洞察 + 录音清单 + 六层验证 + 置信度分层」呈现。老顽童作为 reviewer，未推动其转换为标准格式。
2. **老顽童自撰的 `yt-tool-ai-ppt-maker.md` 质量最低**：处于 draft 状态，source 引用薄弱（无精确行号），Critique 引用 Edward Tufte 等名人但无法验证与 source 的关系，整体是早期模板化产物。
3. **口述数据独立验证不足**：多张综合卡包含「73% 满意度」「40% 付费意愿」「12 万订单」「800 万客户渠道」等数字，虽已回填 source 行号，但均为项目方自述，缺少独立审计或第三方验证。老顽童作为 reviewer 未要求补充「未验证口述数据」标注或第三方交叉验证。
4. **Theme summary 加工风险**：部分断言来自 `theme-*-summary.md` 的整合（如「效率提升 300%」「提前 2-3 年布局」「品牌溢价而非配方技术」），已被王语嫣在后续回填中发现并清理，说明老顽童初审时未能识别这些问题。
5. **药柜/医疗内容污染风险**：`finance-legal-business-operations.md`、`product-business-strategy.md`、`ai-methodology-tools.md`、`yitang-methodology-system.md` 等卡中均发现药柜/医疗相关内容混入，老顽童作为 reviewer 虽然标注了「建议移入药柜队列」，但未确保实际分离。

**评分**：
- 前 9 张王语嫣综合卡（老顽童 review）：3.0/5
- `yt-tool-ai-ppt-maker.md`（老顽童自撰）：1.0/5

---

## 三、共性问题

### 3.1 模板化写作倾向

老顽童自撰卡片（AI 短剧、建模、业务公式、AI PPT）呈现高度相似的结构：
- Visual Analysis → Claims → Constraints & Boundaries → Critique → Synthesis → Action Triggers → Sources
- 这种结构本身没问题，但内容填充多为概念复述，缺少真实案例支撑。

### 3.2 Critique 部分流于形式

Critique 中的「外部攻击」大量引用名人（麦基、坎贝尔、Tufte、Deming、Bloom 等），但这些引用：
- 并非来自 source 材料；
- 往往是通用批评，未针对卡片内的具体 Claims 进行反驳；
- 有时与主题关联度不高（如用罗兰·巴特批评短剧拆本罗盘）。

### 3.3 Confidence / Trust Level 设置僵化

老顽童自撰卡片的 confidence 高度集中在 0.75 / medium，未根据以下因素差异化：
- source 是否精确到行号；
- 是否有独立验证；
- 是否有具体案例；
- 是否有暗知识支撑。

### 3.4 暗知识与失败案例缺失

缺少以下类型的内容：
- 行业潜规则（短剧平台审核红线、建模中的常见坑）；
- 失败教训（业务公式拆解中的 L2/L4/L6 陷阱、短剧 AI 生成后的实际修改成本）；
- 边界条件（什么场景下工具不适用、什么前提下断言不成立）；
- 反事实测试（如果去掉某个要素会怎样）。

### 3.5 Reviewer 把关不严

对于王语嫣生成的 9 张综合卡，老顽童作为 reviewer：
- 未要求转换为标准 30_wiki 格式；
- 未要求补充更多暗知识和失败案例；
- 未推动口述数据的第三方验证；
- 对 theme summary 加工风险识别滞后（由王语嫣后续回填发现）。

---

## 四、返工优先级与建议

### 4.1 P0（立即返工）

1. **AI 短剧域 6 张主卡**
   - 补充至少 2-3 个真实短剧案例（可来自 `industry-ai-cases.md` 中的戴志龙分享或外部公开爆款）；
   - 将 Claims 的 source 引用精确到口述原文行号；
   - 重写 Critique，针对具体 Claims 进行反驳，删除无关名人引用；
   - 补充暗知识：平台审核红线、题材生命周期、AI 生成后的人工修改成本、编剧与平台买方的博弈等；
   - 重新校准 confidence（建议 0.55-0.65）。

2. **业务公式域 5 张新卡**
   - 按 `60_feedback/issues/fb_20260614_9e5a2c8b-老顽童业务公式域工作深度审计.md` 第 5 节执行；
   - 优先补充 3-5 张跨行业案例卡；
   - 在 ABC 模型卡和六层逻辑卡中补充暗知识小节和自检清单。

3. **`yt-tool-ai-ppt-maker.md`**
   - 重写为标准工具卡，补充精确 source 引用；
   - 验证 Critique 中名人引用的真实性；
   - 补充真实使用案例和失败教训。

### 4.2 P1（高优先级）

4. **建模能力域 5 张主卡**
   - 为每个阶段/工具补充 1-2 个具体案例（Truman 课程案例或企业应用案例）；
   - 将已有的 `dk-modeling-*` 暗知识整合进主卡或建立强链接；
   - 为 `modeling-weapon-library` 中的代表性模型补充使用步骤、典型场景、常见错误。

5. **王语嫣综合卡格式转换**
   - 将 9 张主题综合卡拆分为标准 30_wiki 概念卡/框架卡/工具卡/案例卡；
   - 或至少建立从综合卡到标准子卡的映射和链接。

### 4.3 P2（常规）

6. **口述数据独立验证**
   - 对「73% 满意度」「40% 付费意愿」「12 万订单」「800 万客户渠道」等数字标注「未验证口述数据」；
   - 补充第三方报告或公开数据交叉验证。

7. **药柜/医疗内容分离**
   - 确保 `finance-legal-business-operations.md`、`product-business-strategy.md`、`ai-methodology-tools.md`、`yitang-methodology-system.md` 中的药柜/医疗片段已移入药柜处理队列。

---

## 五、附录：老顽童非药柜卡片清单与评分

| 序号 | 文件路径 | 域 | 角色 | 深度评分 | 主要问题 |
|---|---|---|---|---:|---|
| 1 | `30_wiki/concepts/yt-business-formula-parameter-iceberg.md` | 业务公式 | 作者 | 2.0 | 暗知识、L5-L6 洞察、案例库不足 |
| 2 | `30_wiki/concepts/yt-business-formula-six-level-logic.md` | 业务公式 | 作者 | 2.0 | 失败模式缺少案例支撑 |
| 3 | `30_wiki/concepts/yt-business-formula-ten-paradigms.md` | 业务公式 | 作者 | 2.0 | 范式组合应用未展开 |
| 4 | `30_wiki/frameworks/yt-business-formula-abc-model.md` | 业务公式 | 作者 | 2.0 | 加法/乘法暗知识不足 |
| 5 | `30_wiki/cases/case-toc-ecommerce-formula-misjudgment.md` | 业务公式 | 作者 | 2.5 | 仅 1 张案例卡，案例库单薄 |
| 6 | `30_wiki/concepts/ai-short-drama-ice-fire-scripting-compass.md` | AI 短剧 | 作者/审核 | 2.0 | 无真实案例，confidence 偏高 |
| 7 | `30_wiki/frameworks/ai-short-drama-ice-fire-dissection-compass.md` | AI 短剧 | 作者/审核 | 2.0 | Claims 缺行号，Critique 套路化 |
| 8 | `30_wiki/tools/ai-short-drama-plot-three-axes.md` | AI 短剧 | 作者/审核 | 2.0 | 无精确 source，无案例 |
| 9 | `30_wiki/tools/ai-short-drama-script-planning-three-axes.md` | AI 短剧 | 作者/审核 | 2.0 | 模板化，缺真实项目对照 |
| 10 | `30_wiki/tools/ai-short-drama-framework-three-axes.md` | AI 短剧 | 作者/审核 | 2.0 | 缺 source 行号与案例验证 |
| 11 | `30_wiki/tools/ai-short-drama-conflict-three-axes.md` | AI 短剧 | 作者/审核 | 2.0 | 缺 source 行号与真实案例 |
| 12 | `30_wiki/concepts/ai-short-drama-platform-policy-comparison.md` | AI 短剧 | 作者/审核 | 2.5 | 未审计，可能较浅 |
| 13 | `30_wiki/concepts/modeling-capability-system.md` | 建模能力 | 作者/审核 | 2.5 | 无独立 Critique，缺具体案例 |
| 14 | `30_wiki/frameworks/modeling-three-stages.md` | 建模能力 | 作者/审核 | 2.5 | 缺阶段案例，无 Critique |
| 15 | `30_wiki/tools/modeling-level-map.md` | 建模能力 | 作者/审核 | 2.5 | C5 推断无 source，自评标准模糊 |
| 16 | `30_wiki/tools/modeling-weapon-library.md` | 建模能力 | 作者/审核 | 2.5 | 模型使用步骤和常见错误不足 |
| 17 | `30_wiki/tools/process-modeling.md` | 建模能力 | 作者/审核 | 3.0 | 相对较好，但缺失败教训 |
| 18 | `30_wiki/concepts/ai-hackathon-pitches.md` | 零散域 | 审核 | 3.0 | 草稿格式，口述数据待验证 |
| 19 | `30_wiki/concepts/business-validation-models-collaboration.md` | 零散域 | 审核 | 3.0 | 主题跨度大，需拆分 |
| 20 | `30_wiki/concepts/finance-legal-business-operations.md` | 零散域 | 审核 | 3.0 | 税务/合同需专业复核，药柜内容待剥离 |
| 21 | `30_wiki/concepts/industry-ai-cases.md` | 零散域 | 审核 | 3.0 | 短剧宏大叙事需第三方验证 |
| 22 | `30_wiki/concepts/personal-growth-complex-systems.md` | 零散域 | 审核 | 3.0 | 历史/医疗断言需修正和限定 |
| 23 | `30_wiki/concepts/product-business-strategy.md` | 零散域 | 审核 | 3.0 | 设备药柜污染风险 |
| 24 | `30_wiki/concepts/supply-chain-beverage.md` | 零散域 | 审核 | 3.0 | 需外部证据补充 |
| 25 | `30_wiki/concepts/yitang-methodology-system.md` | 零散域 | 审核 | 3.0 | 概念漂移（知识萃取二维模型） |
| 26 | `30_wiki/frameworks/ai-methodology-tools.md` | 零散域 | 审核 | 3.0 | 口述数据待验证 |
| 27 | `30_wiki/tools/yt-tool-ai-ppt-maker.md` | 零散域 | 作者 | 1.0 | draft，source 薄弱，模板化 |

**评分说明**：
- 5 分：深度充分，案例丰富，source 精确，暗知识完整；
- 4 分：较好，少量补充即可；
- 3 分：及格，有明显改进空间；
- 2 分：深度不足，流于形式；
- 1 分：草稿/不合格，需重写。

---

## 六、结论与下一步

老顽童在知识卡生产流程上已能稳定产出结构规范的卡片，但在**深度挖掘**层面存在系统性短板：

1. **自撰卡片**普遍存在模板化、案例库单薄、暗知识缺失、Critique 套路化的问题；
2. **作为 reviewer** 时，对王语嫣生成的综合卡把关不严，未推动其向标准 30_wiki 格式和深度知识卡升级；
3. **Confidence / trust_level 校准**能力不足，常设置过高。

**建议下一步**：
- 先执行 P0 返工（AI 短剧域、业务公式域、`yt-tool-ai-ppt-maker.md`）；
- 同时建立 reviewer checklist，要求老顽童在审核他人卡片时强制检查：source 精确性、案例密度、暗知识完整性、confidence 合理性、药柜污染隔离。

---

*审计完成时间：2026-06-14*  
*状态：已完成，待用户/架构师决策是否启动返工*
