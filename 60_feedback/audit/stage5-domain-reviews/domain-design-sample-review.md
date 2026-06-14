# 30_wiki 阶段 5 Domain 专项审查报告：design

- **审查样本数**：40 张卡片
- **Domain**：design（为主），少量涉及 ai-saas / business-strategy / yitang
- **审查日期**：2026-06-14
- **审查人**：Kimi Code CLI（知识库质量审查员）
- **审查范围**：`C:/Users/Administrator/Desktop/wiki/60_feedback/audit/.stage5-tmp/domain-design-sample.txt`

---

## 一、整体统计

| 维度 | 数量/比例 |
|---|---|
| 审查卡片总数 | 40 |
| skill 类型 | 37 |
| concept 类型 | 1 |
| dark-knowledge 类型 | 3 |
| 状态为 draft | 39（仅 1 张为 enriched） |
| source_refs 为空 | 37（占 92.5%） |
| confidence 0.6 / trust low | 37 |
| confidence 0.7-0.8 / trust low-medium | 3 |
| 发现明显问题 | 38 张 |
| 暂无明显问题 | 2 张 |

---

## 二、问题分类统计

| 问题分类 | 涉及卡片数 | 主要表现 |
|---|---|---|
| **Source 可验证性不足** | 37 | `source_refs` 为空，正文来源仅写“月白，XX 案例/实操/基础”，无原始材料路径、时间戳或章节定位 |
| **内容完整性不足** | 约 30 | 步骤空泛、缺少具体案例/数据/outcome、术语未解释、工具未列全 |
| **类型特定检查缺陷（skill）** | 36 | 多数 skill 缺验收标准/练习方法/示例；常见失败模式千篇一律 |
| **卡片间重复/冲突** | 8 组 | 同主题多张卡片重复建设，核心观点相近；个别存在事实冲突 |
| **Confidence / Trust 不一致** | 3 | pipeline 含 `confidence-verified-by-case`，但正文无 case/outcome 支撑 |
| **Domain 一致性/标注问题** | 2 | design 标签过于宽泛；个别卡片偏学习方法论 |
| **事实性 / 合规性风险** | 3 | 印刷 DPI 标准疑似与行业常识相反；电商“人工过审”规避检测；薅 AIGC 羊毛 |

> 注：同一卡片可能同时归属多个分类。

---

## 三、具体卡片问题清单

### 3.1 高风险 / 需优先处理

| # | 文件路径 | 问题描述 | 处理建议 |
|---|---|---|---|
| 1 | `30_wiki/concepts/skill-月白-印刷DPI标准设置.md` | **事实性风险**：常规线下印刷建议 150dpi，大幅面（1-2 米以上）建议 300dpi，与常规印刷认知相反（通常常规印刷 300dpi，大幅户外广告可降至 72-150dpi）。 | 请印刷专业人员复核；补充行业规范出处；若确实为月白原话，应标注“待验证”并给出常见标准对照表。 |
| 2 | `30_wiki/concepts/skill-月白-AI电商图人工过审处理.md` | **合规与伦理风险**：主张通过人工加图层破坏 AI 特征以“规避平台检测”，且断言平台无法逐张数字水印检测。内容 assertive 但 trust_level 为 low。 | 增加风险提示与平台政策说明；如保留，需明确法律/平台规则边界，改为“提升人工精修质感”而非“过检测”。 |
| 3 | `30_wiki/concepts/skill-月白-薅AIGC羊毛资源法.md` | **合规与可持续性风险**：依赖“免注册免付费 AIGC 网站”和课程资源集合，未列具体站点；可能违反各平台 ToS；资源窗口期会过期。 | 补充可验证资源清单及使用条款；或改写为“低成本试用/免费额度使用指南”，弱化“薅羊毛”导向。 |
| 4 | `30_wiki/concepts/skill-月白-课程问题预埋法.md` | **Confidence 不一致**：pipeline 含 `confidence-verified-by-case`，但正文无任何 case、outcome 或数据。 | 移除 `confidence-verified-by-case` 并降为 draft；或补充真实课程迭代案例与效果反馈。 |
| 5 | `30_wiki/concepts/skill-月白-线下实体门店设计真实体感验证.md` | **Confidence 不一致**：pipeline 含 `confidence-verified-by-case`，但正文无 case/outcome/数据。 | 同上；补充门店验证案例或移除 verified 标记。 |

### 3.2 重复 / 关系待梳理

| # | 文件路径 | 问题描述 | 处理建议 |
|---|---|---|---|
| 6 | `30_wiki/concepts/skill-月白-精准提示词撰写法.md` | 与 `skill-月白-精准共用提示词撰写.md` 核心方法高度重复（删除情绪词、客观描述、可量化特征、测试迭代）。 | 合并为一张卡片，或明确差异化定位：前者面向个人精准提示词，后者面向团队共享模块库。 |
| 7 | `30_wiki/concepts/skill-月白-精准共用提示词撰写.md` | 同上，与 `skill-月白-精准提示词撰写法.md` 重复。 | 同上。 |
| 8 | `30_wiki/concepts/skill-月白-多语言提示词降幻觉法.md` | 与 `skill-月白-AI自动生成多语种专业名词提示词.md` 主题重叠，均涉及多语言提示词。 | 合并或互加 `wiki_refs`；`降幻觉法` 中的“幻觉无限接近于零”属过度断言，需弱化。 |
| 9 | `30_wiki/concepts/skill-月白-AI自动生成多语种专业名词提示词.md` | 同上，与 `skill-月白-多语言提示词降幻觉法.md` 重叠。 | 同上。 |
| 10 | `30_wiki/concepts/skill-月白-批量生成多视角素材.md` | 与 `skill-月白-视角替换专用提示法.md` 同属“多视角/视角控制”主题。 | 建立互链：一张讲“批量许愿”，一张讲“精确控制”；在适用场景中互相引用。 |
| 11 | `30_wiki/concepts/skill-月白-视角替换专用提示法.md` | 同上；且引用“预设代码行 14-18”“视觉场景重构专家”模板，外部读者无法复现。 | 补充模板文件链接或内嵌示例；与批量生成卡片互链。 |
| 12 | `30_wiki/concepts/skill-月白-产品替换式场景合成法.md` | 与 `skill-月白-精准改图提示词写法.md` 同属“图生图/元素替换”。 | 互加 `wiki_refs`，并在适用场景中区分：前者是多图场景合成，后者是单元素替换。 |
| 13 | `30_wiki/concepts/skill-月白-精准改图提示词写法.md` | 同上。 | 同上。 |
| 14 | `30_wiki/concepts/skill-月白-最佳实践素材收集法.md` | 与 `skill-月白-灵感画布建立法.md`、`skill-月白-设计参考图精准定位法.md` 主题重叠，均为“找参考/建素材库”。 | 合并或分工：`最佳实践素材收集法` 讲日常习惯，`灵感画布` 讲项目启动，`参考图定位` 讲人群驱动选参考；互链。 |
| 15 | `30_wiki/concepts/skill-月白-灵感画布建立法.md` | 同上；且“用自己的审美标准筛选，规避版权风险”缺少版权判断方法。 | 同上；补充版权合规检查要点。 |
| 16 | `30_wiki/concepts/skill-月白-设计参考图精准定位法.md` | 同上；且步骤 3 的“拆推评算”未在卡片内解释。 | 同上；补充“拆推评算”定义或链接到相关概念。 |
| 17 | `30_wiki/concepts/skill-月白-眼高手低训练法.md` | 与 `skill-月白-设计基本功回归法.md`、`dark-knowledges/dk-yb10-theory-moat-designer.md` 主题重叠，都强调基本功/审美。 | 互链；避免重复论述；`眼高手低训练法` 可侧重“训练路径”，`基本功回归法` 可侧重“知识体系”。 |
| 18 | `30_wiki/concepts/skill-月白-设计基本功回归法.md` | 同上；且“复习大学设计理论书籍”过于笼统。 | 同上；补充推荐书目或知识模块清单。 |
| 19 | `30_wiki/concepts/skill-月白-PPT全AI生成工作流.md` | 与 `skill-月白-PPT风格锁定工作流.md` 同属 PPT AI 工作流。 | 合并为“PPT AI 生成与风格锁定工作流”或拆分：前者讲生成，后者讲风格一致性。 |
| 20 | `30_wiki/concepts/skill-月白-PPT风格锁定工作流.md` | 同上；内容较空泛，缺少风格提示词示例。 | 同上；补充示例与输出截图说明。 |
| 21 | `30_wiki/concepts/skill-月白-商业项目AI模型选型决策.md` | 与 `skill-月白-Token效价比决策公式.md` 同属“AI vs 人工 / 成本效果权衡”。 | 互加 `wiki_refs`；前者聚焦模型选择，后者聚焦任务切换。 |
| 22 | `30_wiki/concepts/skill-月白-Token效价比决策公式.md` | 同上；公式单位混用（时间×时间？），缺少示例计算。 | 补充统一计量方式（如折算为工时或人民币）和至少一个案例。 |

### 3.3 Source / 可验证性问题

| # | 文件路径 | 问题描述 | 处理建议 |
|---|---|---|---|
| 23 | `30_wiki/concepts/skill-月白-商业项目AI模型选型决策.md` | `source_refs` 为空；来源仅“月白，文创案例”。 | 补充原始材料路径、章节或课程回放时间戳。 |
| 24 | `30_wiki/concepts/skill-月白-AI逆向反推描述法.md` | `source_refs` 为空；步骤 3 建议直接截取 AI 反推结果使用，未提示版权/质量风险。 | 补充来源；增加版权与二次创作提示。 |
| 25 | `30_wiki/concepts/skill-月白-薅AIGC羊毛资源法.md` | `source_refs` 为空；“10+ 免注册免付费 AIGC 网站”无法验证。 | 补充资源清单及来源；或改为通用策略。 |
| 26 | `30_wiki/concepts/skill-月白-产品反光修复术.md` | `source_refs` 为空；无 before/after 示例。 | 补充来源与示例图说明。 |
| 27 | `30_wiki/concepts/skill-月白-设计文件八要素命名法.md` | `source_refs` 为空；缺完整命名示例与文件树示例。 | 补充来源；给出 1-2 个完整命名案例。 |
| 28 | `30_wiki/concepts/skill-月白-精准改图提示词写法.md` | `source_refs` 为空。 | 补充来源。 |
| 29 | `30_wiki/concepts/skill-月白-AI去文字-稿定设计快速出图法.md` | `source_refs` 为空。 | 补充来源。 |
| 30 | `30_wiki/concepts/skill-月白-眼高手低训练法.md` | `source_refs` 为空；3 个步骤偏口号化。 | 补充来源；细化训练计划与验收指标。 |
| 31 | `30_wiki/concepts/skill-月白-精准共用提示词撰写.md` | `source_refs` 为空。 | 补充来源；处理与“精准提示词撰写法”的重复问题。 |
| 32 | `30_wiki/concepts/skill-月白-AI自动生成多语种专业名词提示词.md` | `source_refs` 为空；无示例术语表或代码片段。 | 补充来源与示例。 |
| 33 | `30_wiki/concepts/skill-月白-最佳实践素材收集法.md` | `source_refs` 为空。 | 补充来源。 |
| 34 | `30_wiki/concepts/skill-月白-AI电商图人工过审处理.md` | `source_refs` 为空。 | 补充来源；处理合规风险。 |
| 35 | `30_wiki/concepts/skill-月白-批量生成多视角素材.md` | `source_refs` 为空。 | 补充来源。 |
| 36 | `30_wiki/concepts/skill-月白-基于白底图做动作延展.md` | `source_refs` 为空；无 IP/动作案例。 | 补充来源与案例。 |
| 37 | `30_wiki/concepts/skill-月白-产品替换式场景合成法.md` | `source_refs` 为空；虽有 Leo 小人等示例，但仍需原始出处。 | 补充来源。 |
| 38 | `30_wiki/concepts/skill-月白-精准提示词撰写法.md` | `source_refs` 为空。 | 补充来源；处理重复。 |
| 39 | `30_wiki/concepts/skill-月白-设计基本功回归法.md` | `source_refs` 为空。 | 补充来源与推荐书单。 |
| 40 | `30_wiki/concepts/skill-月白-泛产品设计能力迁移法.md` | `source_refs` 为空；“一堂/学一堂等商业思维课程框架”未解释。 | 补充来源；解释引用框架或删除。 |
| 41 | `30_wiki/concepts/skill-月白-PPT全AI生成工作流.md` | `source_refs` 为空；GPT-4o image generation 直接生成完整 PPT 的说法未验证。 | 补充来源；说明是生成图片式 PPT 还是可编辑文件。 |
| 42 | `30_wiki/concepts/skill-月白-设计参考图精准定位法.md` | `source_refs` 为空；“拆推评算”未解释。 | 补充来源与术语解释。 |
| 43 | `30_wiki/concepts/skill-月白-AIGC餐饮海报优化一抽流.md` | `source_refs` 为空；虽有餐饮细节但无 outcome 数据。 | 补充来源与 AB 测试结果。 |
| 44 | `30_wiki/concepts/skill-月白-AIGC文字大小精确控制.md` | `source_refs` 为空。 | 补充来源。 |
| 45 | `30_wiki/concepts/skill-月白-创作与执行双模式切换.md` | `source_refs` 为空；步骤抽象，缺切换触发条件。 | 补充来源与具体检查清单。 |
| 46 | `30_wiki/concepts/skill-月白-多语言提示词降幻觉法.md` | `source_refs` 为空。 | 补充来源。 |
| 47 | `30_wiki/concepts/skill-月白-AI人物特征精准描述法.md` | `source_refs` 为空；虽详细但缺最终成品示例。 | 补充来源与 case。 |
| 48 | `30_wiki/concepts/skill-月白-AI需求拆解咨询法.md` | `source_refs` 为空。 | 补充来源。 |
| 49 | `30_wiki/concepts/skill-月白-灵感画布建立法.md` | `source_refs` 为空。 | 补充来源。 |
| 50 | `30_wiki/concepts/skill-月白-设计项目MVP拆解法.md` | `source_refs` 为空；缺项目验证案例。 | 补充来源与 case。 |
| 51 | `30_wiki/concepts/skill-月白-线下实体门店设计真实体感验证.md` | `source_refs` 为空。 | 补充来源与 case。 |
| 52 | `30_wiki/concepts/skill-月白-文创材质成本调研与精益选择.md` | `source_refs` 为空；“海量调研市面”“AI 计算基础费用”不可验证。 | 补充来源、价格区间参考与成本计算模板。 |

### 3.4 内容完整性 / 类型检查问题

| # | 文件路径 | 问题描述 | 处理建议 |
|---|---|---|---|
| 53 | `30_wiki/concepts/skill-月白-商业项目AI模型选型决策.md` | 缺具体模型对比案例、成本计算表、效果提升百分比示例。 | 补充案例与决策表格。 |
| 54 | `30_wiki/concepts/skill-月白-AI逆向反推描述法.md` | 缺提示词示例、版权说明、输出结果校准方法。 | 补充示例与风险提示。 |
| 55 | `30_wiki/concepts/skill-月白-薅AIGC羊毛资源法.md` | 缺具体网站清单、授权说明、长期可用性评估。 | 补充清单与免责声明。 |
| 56 | `30_wiki/concepts/skill-月白-产品反光修复术.md` | 仅一句指令，缺不同材质示例与失败对比。 | 补充示例与对照图描述。 |
| 57 | `30_wiki/concepts/skill-月白-视角替换专用提示法.md` | 依赖未提供的“代码行 14-18”模板。 | 内嵌模板或链接。 |
| 58 | `30_wiki/concepts/skill-月白-眼高手低训练法.md` | 步骤口号化，缺训练周期、素材清单、验收标准。 | 细化为 7/14/30 天训练计划。 |
| 59 | `30_wiki/concepts/skill-月白-AI自动生成多语种专业名词提示词.md` | 缺示例术语表与系统提示词代码。 | 给出 1-2 领域示例。 |
| 60 | `30_wiki/concepts/skill-月白-课程问题预埋法.md` | 作为 skill 缺练习/验收标准；pipeline 与内容不一致。 | 补充作业模板与迭代案例。 |
| 61 | `30_wiki/concepts/skill-月白-Token效价比决策公式.md` | 公式单位不统一，缺计算示例。 | 统一度量并给出案例。 |
| 62 | `30_wiki/concepts/skill-月白-AI电商图人工过审处理.md` | “20% 人工调整”武断；缺具体操作清单与合规边界。 | 改为可操作检查清单并加风险说明。 |
| 63 | `30_wiki/concepts/skill-月白-批量生成多视角素材.md` | 虽具体但缺筛选标准与质量验收。 | 补充筛选清单。 |
| 64 | `30_wiki/concepts/skill-月白-基于白底图做动作延展.md` | 步骤抽象，缺动作描述示例与 IP 案例。 | 补充示例。 |
| 65 | `30_wiki/concepts/skill-月白-PPT全AI生成工作流.md` | 未说明 GPT-4o 输出的是图片还是可编辑 PPT；缺提示词示例。 | 澄清输出形态并给出示例。 |
| 66 | `30_wiki/concepts/skill-月白-设计参考图精准定位法.md` | “拆推评算”未解释；缺目标人群分析示例。 | 补充定义与案例。 |
| 67 | `30_wiki/concepts/skill-月白-创作与执行双模式切换.md` | 缺切换触发条件、检查清单、时间盒规则。 | 补充具体工具模板。 |
| 68 | `30_wiki/concepts/skill-月白-多语言提示词降幻觉法.md` | “幻觉无限接近于零”过度断言。 | 改为“显著降低”。 |
| 69 | `30_wiki/concepts/skill-月白-AI需求拆解咨询法.md` | 作为 skill 可执行，但缺少示例对话与输出样例。 | 补充示例 prompt 与 AI 输出样例。 |
| 70 | `30_wiki/concepts/skill-月白-灵感画布建立法.md` | 缺分类维度示例与版权检查方法。 | 补充模板。 |
| 71 | `30_wiki/concepts/skill-月白-设计项目MVP拆解法.md` | 缺真实项目验证数据。 | 补充 case 与迭代记录。 |
| 72 | `30_wiki/concepts/skill-月白-线下实体门店设计真实体感验证.md` | 缺门店验证 case、打印规格与观察距离标准。 | 补充案例。 |
| 73 | `30_wiki/concepts/skill-月白-文创材质成本调研与精益选择.md` | “海量调研”“AI 计算费用”不可复现；缺价格区间。 | 补充成本模板与调研渠道。 |

### 3.5 暂无明显问题的卡片

| # | 文件路径 | 评估说明 |
|---|---|---|
| 74 | `30_wiki/concepts/视觉prompt三层操作系统-srom-visual-os.md` | 类型为 concept，`source_refs` 完整，定义清晰，有适用范围、平台适配、组合打法与开放问题；结构完整。建议：开放问题较长，可作为后续迭代清单。 |
| 75 | `30_wiki/dark-knowledges/dk-yb17-product-lifestyle-photography.md` | dark-knowledge insight，来源文件明确，有原始表述、场景、方法、边界与关联知识；质量较高。 |
| 76 | `30_wiki/dark-knowledges/dk-yb10-theory-moat-designer.md` | 来源明确，结构完整；与 skill 基本功/眼高手低卡片主题相关，建议互链。 |
| 77 | `30_wiki/dark-knowledges/dk-yb7-design-demand-80-10-10.md` | 来源明确，有数据化分层判断与边界说明；质量较高。建议与相关设计管理/AI 工具采购卡片互链。 |
| 78 | `30_wiki/dark-knowledges/dk-yb12-ai-image-analysis-replace-training.md` | 来源明确，步骤具体；与 `AI逆向反推描述法` 主题相近，建议互链并区分使用场景。 |
| 79 | `30_wiki/concepts/skill-月白-AIGC餐饮海报优化一抽流.md` | 虽 `source_refs` 为空，但操作步骤具体、有餐饮场景细节与 AB 测试意识，是 skill 中质量较好的一张。建议补充来源与 outcome。 |
| 80 | `30_wiki/concepts/skill-月白-AI人物特征精准描述法.md` | 虽 `source_refs` 为空，但步骤详细、特征维度丰富、有抽卡数量与修图流程，skill 类型检查基本满足。建议补充来源与 case。 |

> 注：以上“暂无明显问题”的卡片仍建议补充 `source_refs` 与跨卡片链接，但核心内容质量已达到可用水平。

---

## 四、批量处理建议

### 4.1 可脚本化批量检测/标记（无需人工判断内容真伪）

1. **空 `source_refs` 扫描**：列出所有 `source_refs` 为空且类型为 skill/concept/framework/tool/case 的卡片，生成待补充清单。
2. **Pipeline 与内容一致性检查**：扫描 pipeline 含 `confidence-verified-by-case` 但正文中无 `case/outcome/数据/AB测试` 等关键词的卡片。
3. ** boilerplate 检测**：检测“常见失败模式”是否完全相同或高度雷同、是否出现大量“待补充”关联技能。
4. **重复主题聚类**：基于标题关键词（如“提示词”“多语言”“PPT”“视角”“参考图”“基本功”“MVP”）做相似度聚类，输出疑似重复卡片对。
5. **Domain 标签校验**：检测 `domain` 是否仅含 `design` 一张标签，建议增加 `ai-design`、`prompt-engineering`、`ecommerce`、`print`、`workflow` 等更细粒度标签。
6. **confidence/trust 规则校验**：如 `source_refs` 为空且 status=draft，confidence 不应高于 0.6；如存在 verified-by-case 但无 case，自动降级。

### 4.2 必须人工判断/处理

1. **事实性核查**：`印刷DPI标准设置` 的数值是否正确，需要印刷/印前专业人员复核。
2. **合规与伦理审查**：`AI电商图人工过审处理`、`薅AIGC羊毛资源法` 是否需要改写或加风险免责声明。
3. **重复卡片合并决策**：`精准提示词撰写法`/`精准共用提示词撰写`、`多语言提示词降幻觉法`/`AI自动生成多语种专业名词提示词`、`PPT全AI生成工作流`/`PPT风格锁定工作流` 等，需要内容负责人决定是否合并。
4. **来源补充**：37 张 skill 卡片的 `source_refs` 需要回到原始课程/口述稿中定位，无法由脚本自动填充。
5. **案例与 outcome 补全**：真实项目效果数据、AB 测试结果、成本计算案例只能人工采访或查阅原始材料。
6. **跨卡片关系梳理**：`wiki_refs` 的填充与主题分工需要人工判断业务优先级。

---

## 五、Domain 级结论

### 5.1 整体质量

- **design Domain 样本整体呈现“头轻脚重”**：3 张 dark-knowledge + 1 张 concept 卡片质量较高（来源明确、结构完整）；37 张 skill 卡片大量源自同一套模板，**`source_refs` 几乎全空**，内容同质化、 boilerplate 严重，可操作性参差不齐。
- 多数 skill 处于 **draft / confidence 0.6 / trust low** 状态，虽然与当前内容质量基本匹配，但意味着该 domain 距离“可信任执行”还有较大差距。

### 5.2 最大风险点

1. **source 不可验证风险（最高）**：92.5% 的 skill 卡片无法追溯到原始材料，导致知识无法审计、无法更新、难以复用。
2. **误导性技术建议风险**：`印刷DPI标准设置` 如果数值确实与行业常识相反，会在实际印刷中造成直接经济损失。
3. **合规与平台规则风险**：`AI电商图人工过审处理` 教授规避检测技巧，`薅AIGC羊毛资源法` 鼓励绕过平台付费机制，存在法律、账号、品牌声誉风险。
4. **知识重复与检索噪音**：同一主题多张卡片重复建设，使用者难以判断该用哪张，降低知识库信噪比。

### 5.3 优先处理建议

1. **P0：补齐 source_refs**  
   对全部 37 张空 source 的 skill 卡片，回溯到 `00_inbox/design/`、`10_raw/sources/` 或课程回放，补充具体文件路径/时间戳/章节。这是后续所有审查与信任升级的基础。

2. **P0：事实与合规核查**  
   - 请印前专业人员复核 `印刷DPI标准设置`；  
   - 对 `AI电商图人工过审处理` 和 `薅AIGC羊毛资源法` 进行合规改写或加显著风险提示。

3. **P1：合并/拆分重复主题**  
   对 8 组重复卡片执行“合并或互链+差异化定位”，减少检索噪音。重点处理提示词类、PPT 类、参考图收集类。

4. **P1：补充可操作案例与验收标准**  
   对 skill 卡片统一要求：至少 1 个完整案例、1 个可执行检查清单或验收标准。优先补全餐饮海报、人物特征、MVP 拆解等已具潜力的卡片。

5. **P2：统一模板与 metadata 规则**  
   - 禁止 boilerplate “常见失败模式” 全文复制；  
   - `pipeline` 含 `confidence-verified-by-case` 必须强制要求正文出现 case/outcome；  
   - 增加 `wiki_refs` 字段，建立卡片间关系网。

---

## 六、附录：审查样本完整列表

| 序号 | 文件路径 |
|---|---|
| 1 | `30_wiki/concepts/skill-月白-商业项目AI模型选型决策.md` |
| 2 | `30_wiki/concepts/skill-月白-AI逆向反推描述法.md` |
| 3 | `30_wiki/concepts/skill-月白-薅AIGC羊毛资源法.md` |
| 4 | `30_wiki/concepts/skill-月白-产品反光修复术.md` |
| 5 | `30_wiki/concepts/skill-月白-设计文件八要素命名法.md` |
| 6 | `30_wiki/concepts/skill-月白-视角替换专用提示法.md` |
| 7 | `30_wiki/concepts/skill-月白-精准改图提示词写法.md` |
| 8 | `30_wiki/concepts/skill-月白-AI去文字-稿定设计快速出图法.md` |
| 9 | `30_wiki/concepts/skill-月白-眼高手低训练法.md` |
| 10 | `30_wiki/concepts/skill-月白-精准共用提示词撰写.md` |
| 11 | `30_wiki/concepts/skill-月白-AI自动生成多语种专业名词提示词.md` |
| 12 | `30_wiki/concepts/skill-月白-最佳实践素材收集法.md` |
| 13 | `30_wiki/concepts/skill-月白-课程问题预埋法.md` |
| 14 | `30_wiki/concepts/skill-月白-Token效价比决策公式.md` |
| 15 | `30_wiki/concepts/skill-月白-AI电商图人工过审处理.md` |
| 16 | `30_wiki/concepts/skill-月白-批量生成多视角素材.md` |
| 17 | `30_wiki/concepts/skill-月白-基于白底图做动作延展.md` |
| 18 | `30_wiki/concepts/skill-月白-产品替换式场景合成法.md` |
| 19 | `30_wiki/concepts/skill-月白-精准提示词撰写法.md` |
| 20 | `30_wiki/concepts/skill-月白-设计基本功回归法.md` |
| 21 | `30_wiki/concepts/skill-月白-泛产品设计能力迁移法.md` |
| 22 | `30_wiki/concepts/skill-月白-PPT全AI生成工作流.md` |
| 23 | `30_wiki/concepts/skill-月白-设计参考图精准定位法.md` |
| 24 | `30_wiki/concepts/skill-月白-印刷DPI标准设置.md` |
| 25 | `30_wiki/concepts/视觉prompt三层操作系统-srom-visual-os.md` |
| 26 | `30_wiki/dark-knowledges/dk-yb10-theory-moat-designer.md` |
| 27 | `30_wiki/concepts/skill-月白-AIGC餐饮海报优化一抽流.md` |
| 28 | `30_wiki/concepts/skill-月白-PPT风格锁定工作流.md` |
| 29 | `30_wiki/concepts/skill-月白-AIGC文字大小精确控制.md` |
| 30 | `30_wiki/concepts/skill-月白-创作与执行双模式切换.md` |
| 31 | `30_wiki/concepts/skill-月白-多语言提示词降幻觉法.md` |
| 32 | `30_wiki/dark-knowledges/dk-yb7-design-demand-80-10-10.md` |
| 33 | `30_wiki/concepts/skill-月白-AI人物特征精准描述法.md` |
| 34 | `30_wiki/concepts/skill-月白-AI需求拆解咨询法.md` |
| 35 | `30_wiki/concepts/skill-月白-灵感画布建立法.md` |
| 36 | `30_wiki/concepts/skill-月白-设计项目MVP拆解法.md` |
| 37 | `30_wiki/dark-knowledges/dk-yb12-ai-image-analysis-replace-training.md` |
| 38 | `30_wiki/dark-knowledges/dk-yb17-product-lifestyle-photography.md` |
| 39 | `30_wiki/concepts/skill-月白-线下实体门店设计真实体感验证.md` |
| 40 | `30_wiki/concepts/skill-月白-文创材质成本调研与精益选择.md` |
