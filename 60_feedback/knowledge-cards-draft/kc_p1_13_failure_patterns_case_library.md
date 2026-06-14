---
id: "kc-p1-13-failure-patterns-case-library"
component_of: "smart-medicine-cabinet-promotion"
confidence: 0.82
created_at: 2026-06-13
difficulty: "intermediate"
domain:
  - "healthcare"
  - "pharmaceutical-retail"
  - "failure-analysis"
estimated_tokens: 1700
language: "zh-CN"
prerequisites: "kc-p0-04-fraud-detection"
query_triggers:
  - "智能药柜为什么失败"
  - "修正未来药房怎么了"
  - "无人药房失败案例"
  - "药柜加盟失败"
  - "自动售药机为什么做不好"
related:
  - "kc-p0-03-financial-model"
  - "kc-p0-04-fraud-detection"
  - "kc-p0-06-clinic-cabinet-risk-observation"
  - "kc-p1-12-site-selection-deep-dive"
  - "master-cognitive-bias-checklist"
  - "master-antifragile-checklist"
reviewed_by: ""
source_refs:
  - "corr_20260613_smart-medicine-cabinet-iteration-3-failure-cases.md"
  - "corr_20260613_smart-medicine-cabinet-iteration-6-supplemental-deep-dive.md"
  - "corr_20260613_smart-medicine-cabinet-iteration-7-supplemental-deep-dive.md"
  - "corr_20260613_smart-medicine-cabinet-iteration-8-operating-data-and-failures.md"
  - "corr_20260613_smart-medicine-cabinet-iteration-8-synthesis.md"
status: "draft"
title: "智能药柜失败模式案例库"
trust_level: "high"
type: "case"
updated_at: 2026-06-13T16:00:00
version: 1
tags:
  - #scene/healthcare/pharmaceutical-retail
  - #scene/failure-patterns
  - #scene/smart-medicine-cabinet
pipeline:
  - #boundary/requires-human-judgment
---

# 智能药柜失败模式案例库

> **核心定位**：汇总公开渠道可获取的智能药柜/无人药房失败案例，提炼失败模式共因，为投资决策和风险管理提供反面教材。

---

## Summary

智能药柜/无人药房行业 failures 高度集中于五类模式：

1. **招商加盟骗局**：以高收益承诺吸引投资者，实际无运营能力。
2. **点位质量失败**：人流不足、需求虚假、O2O 替代强。
3. **政策合规失败**：违规销售处方药/甲类 OTC、医保违规。
4. **运营能力不足**：设备故障、不补货、无维护、SKU 受限。
5. **商业模式结构性失败**：低频低价乙类 OTC 无法覆盖固定成本。

> **核心判断**：失败不是个案，而是行业结构性问题的集中体现。任何新的药柜项目都必须先排除这五类失败模式。

---

## Claims

### 1. 案例一：修正未来智慧药房（招商加盟骗局典型）

| 维度 | 详情 |
|---|---|
| **时间** | 约 2022–2024 年 |
| **主体** | 海南清修智能药柜科技有限公司（修正集团授权） |
| **模式** | 招商加盟，投资者购买设备，公司承诺点位、运营、分润 |
| **承诺** | "投资 7 万元/台，预估年收益分润 6 万余元，1 年多回本" |
| **现实** | 投资者月收益仅几元、十几元；汉中 31 台机器 2022.4–2023.11 月均销售 **151 元/台** |
| **投诉** | 黑猫投诉 155+ 条：虚假宣传、不履行合同、拖欠违约金 |
| **司法** | 海南清修被列为被执行人；法定代表人徐国梁被限制高消费；与上海家营物业合同纠纷法院终本 |
| **失败模式** | 招商骗局 + 虚假点位 + 运营缺位 |
| **教训** | 品牌背书不等于项目可靠；必须实地考察点位、访谈真实加盟商 |

### 2. 案例二：广西自动售药机五年仅 92 台（政策与需求双重制约）

| 维度 | 详情 |
|---|---|
| **时间** | 2019–2024 年 |
| **主体** | 广西全区自动售药机试点 |
| **数据** | 五年累计仅 92 台自动售药机 |
| **失败模式** | 政策限制（仅乙类 OTC）+ 需求不足 + 运营成本未被充分认识 |
| **教训** | 政策只允许乙类 OTC 严重限制 SKU；消费者对自助购药的信任度和使用习惯尚未养成 |

### 3. 案例三：叮当健康关闭多城业务（商业模式承压）

| 维度 | 详情 |
|---|---|
| **时间** | 2024 年 |
| **主体** | 叮当健康（09886.HK） |
| **事件** | 暂停重庆、南京、济南、福州业务，聚焦北上广深 |
| **财务** | 2024 年智慧药房及医疗服务收入下滑 |
| **失败模式** | 前置仓模式重资产、高履约成本，低线城市订单密度不足 |
| **教训** | 即使是上市公司，低线城市的即时医药零售也难以盈利；药柜模式更难 |

### 4. 案例四：院内智慧药房上市公司收入下滑（医院端已规模化但承压）

| 维度 | 详情 |
|---|---|
| **时间** | 2024 年 |
| **主体** | 艾隆科技（-14.42%）、健麾信息（-56.84%）智慧药房收入 |
| **失败模式** | 医院端采购周期波动、竞争加剧、集采压缩利润空间 |
| **教训** | 院内智慧药房是成熟市场但增长承压；院外药柜市场更不成熟 |

### 5. 案例五：各地政策收紧导致早期试点失效

| 地区 | 早期政策 | 后续变化 | 失败模式 |
|---|---|---|---|
| 成都 | 2020 年允许甲类 OTC | 2025 年底文件到期，省级办法收紧为仅乙类 OTC | 政策红利消失 |
| 重庆 | 曾允许非处方药（含甲类 OTC） | 2024 年 11 月新细则收紧为仅乙类 OTC | 政策红利消失 |
| 陕西 | 2024 年征求意见稿拟允许处方药/甲类 OTC | 正式文件未找到 | 政策不确定性 |

### 6. 失败模式共因提炼

| 失败模式 | 具体表现 | 预警信号 | 规避方法 |
|---|---|---|---|
| **招商骗局** | 高收益承诺、虚假点位、不履约 | "躺赚""半年回本""知名品牌背书" | 实地考察、访谈加盟商、查司法风险 |
| **点位质量差** | 人流不足、夜间无人、O2O 替代强 | 周边无 24 小时需求、远离居住区 | 人流计数、O2O 测试、竞品观察 |
| **SKU 受限** | 仅乙类 OTC，低频低价 | 政策限乙类 OTC、无处方药销售能力 | 确认当地可售品类，不以乙类 OTC 单一品类为主 |
| **运营缺位** | 设备故障、不补货、无维护 | 招商方无运维团队、无补货记录 | 要求运维 SLA、实地考察已运营点位 |
| **医保/合规违规** | 销售处方药、甲类 OTC、个账支付违规 | 推销方暗示可绕过监管 | 向药监/医保部门书面确认 |
| **成本失控** | 设备、租金、运维、合规成本超预算 | 低估隐性成本、无资金储备 | 做保守财务模型，预留 6–12 个月运营资金 |

### 7. 诊所+药柜模式特有的失败风险

| 风险 | 说明 | 案例/证据 |
|---|---|---|
| **处方来源违规** | "大医院处方照方开药"违反《处方管理办法》 | 推销方话术，已被法规对照否定 |
| **跨科销售** | 诊所药柜销售非执业科目药品 | 违反《医疗机构管理条例》 |
| **个账支付风险** | 原研药超出部分刷个账，上海已明确禁止 | 上海 2026 年 5 月政策 |
| **院内药柜利益输送** | "利润反哺医院"涉嫌商业贿赂 | 违反药房托管禁令 |
| **法律关系不清** | 利润分成、责任划分不明 | 尚无专门司法判例 |

---

## Critique

### 局限性

1. **案例样本偏差**：公开渠道更容易获取负面案例，正面案例可能未被报道。
2. **数据不完整**：多数失败案例缺乏完整的财务数据，只能定性分析。
3. **时间动态**：行业仍在变化，未来可能出现新的成功模式。

### 与已有知识的联系

- **认知偏差视角**：失败案例是对"幸存者偏差"和"故事偏误"的重要纠正。参考 `master-cognitive-bias-checklist`。
- **反脆弱视角**：通过研究失败模式，可以设计更具韧性的商业模式。参考 `master-antifragile-checklist`。
- **招商骗局识别**：修正未来药房案例是 `kc-p0-04-fraud-detection` 的核心素材。参考 `kc-p0-04-fraud-detection`。
- **选址视角**：点位质量失败是 `kc-p1-12-site-selection-deep-dive` 的重要输入。参考 `kc-p1-12-site-selection-deep-dive`。
- **诊所风险观察**：诊所+药柜特有风险在 `kc-p0-06-clinic-cabinet-risk-observation` 中有更详细展开。参考 `kc-p0-06-clinic-cabinet-risk-observation`。

### 使用建议

- 在投资或合作前，用本卡的"失败模式共因"逐项自检。
- 对每个新项目追问："这个项目与已失败的案例有何不同？不同之处是否足以避免失败？"
- 将本卡与 `kc-p0-04-fraud-detection`、`kc-p1-12-site-selection-deep-dive` 联用，形成完整的风险评估框架。

---

## Sources

1. `corr_20260613_smart-medicine-cabinet-iteration-3-failure-cases.md`
2. `corr_20260613_smart-medicine-cabinet-iteration-6-supplemental-deep-dive.md`
3. `corr_20260613_smart-medicine-cabinet-iteration-7-supplemental-deep-dive.md`
4. `corr_20260613_smart-medicine-cabinet-iteration-8-operating-data-and-failures.md`
5. `corr_20260613_smart-medicine-cabinet-iteration-8-synthesis.md`
6. 黑猫投诉平台、企查查/天眼查、中国裁判文书网、上市公司年报
