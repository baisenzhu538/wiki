# 知识卡质量控制清单

## 1. 纠偏记录

### FDE 模式概念错误（严重）

- **错误时间**：2026-06-14
- **错误内容**：将"FDE"误解为"Factory Direct / 直供模式"，并生成两张错误知识卡。
- **正确内容**：FDE = Forward Deployed Engineer（前沿部署工程师），源自 Palantir，硅谷 AI 创业公司广泛采用。
- **处理措施**：
  - 将错误文件重命名为 `*-WRONG-deprecated.md`
  - 重新生成正确的 `concept-fde-model.md` 和 `method-fde-implementation.md`
  - 在正确卡片中加入"纠偏说明"
  - 更新本质量控制清单，记录错误原因
- **错误原因分析**：
  - 仅凭"FD"二字主观推断为 Factory Direct，未回到原始录音核实。
  - 未进行外部交叉验证就生成知识卡。
  - 对硅谷新兴概念缺乏敏感度。
- **预防措施**：
  - 任何概念卡生成前，必须至少通过 2 个独立外部来源验证概念定义。
  - 对缩写词必须找到全称和原始出处。
  - 对录音中不明确的概念，先标记为"待核实"，不要直接写入知识卡。

## 2. 可信度分层标准

| 可信度评分 | 信任等级 | 含义 | 处理方式 |
|-----------|---------|------|---------|
| ≥0.85 | 高 | 多源交叉验证，事实清楚 | 可直接使用 |
| 0.75-0.84 | 中高 | 有来源支持，但存在局限 | 可使用，需标注局限 |
| 0.60-0.74 | 中 | 来源单一或部分推断 | 需进一步核验 |
| 0.40-0.59 | 中低 | 证据不足，主观成分重 | 不建议进入 wiki |
| <0.40 | 低 | 基本不可信或待验证 | 必须重新核验或删除 |

## 3. 第三阶段知识卡可信度复核

### 3.1 高可信度（≥0.85）

| 文件名 | 评分 | 说明 |
|--------|------|------|
| concept-fde-model.md | 0.88 | 多源验证（YC/Palantir/36氪/腾讯云） |
| method-fde-implementation.md | 0.84 | 接近高可信，基于 FDE 多源资料 |

### 3.2 中高可信度（0.75-0.84）

| 文件名 | 评分 | 说明 |
|--------|------|------|
| concept-believability-weighted-decision.md | 0.78 | 《原则》+ 批评来源 |
| concept-market-entry-mode.md | 0.76 | 国际商务理论 + 实践 |
| concept-narrative-fallacy.md | 0.80 | 塔勒布原著 |
| concept-personal-company-boundary.md | 0.78 | 公司法/税法 |
| concept-prompt-to-agent-evolution.md | 0.76 | 技术文档 + 实践 |
| fact-medicinal-food-market-2025.md | 0.82 | 官方+多源 |
| fact-micro-short-drama-market-2025.md | 0.80 | 广电总局官方 |
| method-3min-pitch-structure.md | 0.76 | 通用路演方法 |
| method-ai-landing-impact-evaluation.md | 0.76 | 通用评估框架 |
| method-lean-startup-hypothesis-validation.md | 0.78 | 经典理论 |
| method-private-money-control.md | 0.80 | 已补充法律依据、9种合法情形、真实处罚案例 |
| concept-ai-landing-organizational-fit.md | 0.78 | 已补充 TOE/TAM 理论框架对照 |
| concept-multi-agent-system.md | 0.78 | 已补充 Wooldridge、Shoham & Leyton-Brown 等学术定义 |
| method-eliminate-fuzziness.md | 0.76 | 已补充决策疲劳/自我损耗研究引用 |
| method-ai-native-workflow-design.md | 0.76 | 已补充 CTO Academy 人机协作三阶段框架 |
| method-strategic-direction-tradeoff.md | 0.75 | 通用战略框架 |
| concept-y-model-yitang.md | 0.75 | 一堂课程资料 + JTBD |

### 3.3 中可信度（0.60-0.74）— 需要进一步核验

| 文件名 | 评分 | 待核验问题 | 优先级 |
|--------|------|-----------|--------|
| fact-double-grapefruit-juice-cost-structure.md | 0.74 | 价格数据已外部验证，成本数据仍无公开来源 | 高 |
| method-ai-landing-five-steps.md | 0.74 | 通用框架，需要更多企业案例支撑 | 低 |
| method-cost-taste-balance.md | 0.74 | 已补充食品饮料配方设计通用流程和优化策略 | 中 |
| insight-ai-landing-high-value-scenes.md | 0.72 | 场景特征为案例归纳，非统计结论 | 中 |
| insight-ai-pitch-key-elements.md | 0.72 | 基于观察和案例，非投资数据 | 低 |
| insight-going-global-localization-trap.md | 0.72 | 案例为概括性，未具体到企业 | 低 |
| insight-stock-era-marketing-logic.md | 0.72 | 奢侈品案例到大众品类的迁移需谨慎 | 中 |
| method-ipo-learning-loop.md | 0.72 | 一堂课程资料，通用性待验证 | 中 |
| insight-human-machine-replacement-path.md | 0.74 | 已补充餐饮自动化市场数据和 McDonald's/Chipotle/Starbucks 案例 | 中 |
| insight-super-individual-income-reality.md | 0.70 | 中国本地数据不足，但已补充国外基准和中国个体户数据 | 高 |
| insight-super-individual-survivorship-bias.md | 0.65 | 主要为逻辑推理，缺乏具体收入数据 | 高 |
| method-ai-assisted-difficult-conversation.md | 0.70 | AI 辅助沟通效果缺乏实证研究 | 中 |

### 3.4 中低可信度（0.40-0.59）

| 文件名 | 评分 | 说明 |
|--------|------|------|
| fact-smart-kitchen-device-roi.md | 0.74 | 已通过行业报告/研究报告验证价格、市场规模、渗透率 |

### 3.5 已废弃（错误）

| 文件名 | 说明 |
|--------|------|
| concept-fd-model-WRONG-deprecated.md | 概念错误 |
| method-fd-partnership-negotiation-WRONG-deprecated.md | 概念错误 |

## 4. 待核验任务清单

### 高优先级

- [x] `fact-double-grapefruit-juice-cost-structure.md`：终端价格已外部验证，原料成本公开数据仍待补充
- [x] `insight-super-individual-income-reality.md`：已补充国外自由职业者基准和中国个体户数据，中国本地"超级个体"收入中位数仍待
- [ ] `insight-super-individual-survivorship-bias.md`：补充具体案例和数据支撑
- [x] `fact-smart-kitchen-device-roi.md`：价格、市场规模、渗透率已通过行业报告验证，具体项目 ROI 仍待补充

### 中优先级

- [ ] `concept-ai-landing-organizational-fit.md`：与 TOE/TAM 等学术框架对照
- [ ] `concept-multi-agent-system.md`：与学术文献中的 MAS 定义对照
- [ ] `insight-human-machine-replacement-path.md`：补充更多行业案例
- [ ] `method-ai-native-workflow-design.md`：与 HCI/流程再造文献对照
- [ ] `method-cost-taste-balance.md`：补充食品饮料开发公开方法论
- [ ] `method-eliminate-fuzziness.md`：与心理学/精力管理研究对照
- [ ] `method-ipo-learning-loop.md`：与行动学习/PDCA 文献对照

### 低优先级

- [ ] `insight-ai-pitch-key-elements.md`：补充投资人视角数据
- [ ] `insight-going-global-localization-trap.md`：补充具体企业出海失败/成功案例
- [ ] `insight-stock-era-marketing-logic.md`：补充不同行业存量化数据
- [ ] `method-ai-landing-five-steps.md`：补充企业 AI 转型公开案例

## 5. 质量控制规则（铁律）

1. **概念必须溯源**：每个概念卡必须找到原始出处或至少 2 个独立定义来源。
2. **事实必须多源**：每个事实卡必须有至少 2 个独立来源，或 1 个官方权威来源。
3. **洞察必须区分证据与推断**：洞察卡必须明确哪些部分有证据，哪些是归纳推断。
4. **方法必须标注适用边界**：方法卡必须说明适用场景和不适用场景。
5. **录音表述必须复核**：所有来自录音的数据和观点，必须回到录音原文复核。
6. **利益相关度标记**：培训方、卖课方、厂商提供的数据必须降级处理。
7. **错误卡片必须废弃而非删除**：保留错误版本作为纠偏记录，防止再次生成。
8. **定期复核**：每批知识卡生成后必须进行可信度复核。

## 6. 建议进入 30_wiki 的标准

同时具备以下条件方可考虑迁移至 `30_wiki/`：

1. 可信度评分 ≥ 0.78
2. 无概念性错误
3. 来源清晰可追溯
4. 已标注局限性和适用边界
5. 经过至少一轮外部交叉验证
6. 非严重依赖单一利益相关方来源
