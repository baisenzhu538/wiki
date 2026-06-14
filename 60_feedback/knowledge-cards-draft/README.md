# 智能药柜/智慧药房推广 · P0 知识卡草稿与一线验证素材包

**日期**：2026-06-13  
**角色**：王语嫣（Consultant / 诊断咨询者）  
**输出边界**：只写 `60_feedback/`，不修改 `30_wiki/`  
**状态**：草稿，待段誉/知识库维护团队复核后迁移至 `30_wiki/`

---

## 文件清单

### P0 级知识卡草稿（必须优先补充）

| 文件 | 标题 | 类型 | 核心内容 |
|---|---|---|---|
| `kc_p0_01_national-policy-redlines.md` | 自助售药机国家政策与红线 | concept | 国家 48 号公告解读：仅乙类 OTC 可售，禁止甲类 OTC 和处方药 |
| `kc_p0_02_regional-policy-map.md` | 各省市自助售药机政策差异地图 | concept | 陕西、黑龙江、南京、四川/成都、湖北、重庆、吉林等地政策对比 |
| `kc_p0_03_financial_model.md` | 智能药柜单点财务模型与回本测算表 | tool | 设备成本、固定成本、变动成本、保本销售额、不同场景回本周期估算 |
| `kc_p0_04_fraud_detection.md` | 智能药柜/智慧药房招商骗局识别清单 | tool | 修正未来药房骗局拆解、8 大识别信号、合作前必查清单 |
| `kc_p0_05_o2o_cost_structure.md` | 医药 O2O 成本与毛利结构 | concept | 平台抽成 15%–25%、连锁药店毛利率、药柜作为 O2O 前置仓的可行性 |
| `kc_p0_06_clinic-cabinet-risk-observation.md` | 诊所 + 智能药柜协同模式：一线观察与风险提示 | case | 诊所访谈交叉验证结果：推销方话术、三大合规风险、第八轮深挖新增反证 |

### P1/P2 级知识卡草稿（深化分析）

| 文件 | 标题 | 类型 | 核心内容 |
|---|---|---|---|
| `kc_p1_09_giants_why_not_clinic_cabinet.md` | 巨头为何不做诊所+智能药柜 | analysis | 阿里/京东/美团/叮当/平安均未进入诊所+药柜的六维壁垒分析 |
| `kc_p1_10_medical_shortvideo_compliance_for_clinics.md` | 诊所医疗短视频/个人 IP 合规边界 | tool | 抖音/视频号/小红书/快手医疗内容规则、MCN 代运营禁令、AI 文案风险 |
| `kc_p1_11_clinic_cabinet_legal_relationships.md` | 诊所+智能药柜合作的法律关系与合同要点 | tool | 五种法律关系对比、合同核心条款、利润分成税务处理 |
| `kc_p1_12_site_selection_deep_dive.md` | 智能药柜选址深度指南：场景、指标与验证方法 | tool | 五大场景选址对比、关键量化指标、低成本验证方法 |
| `kc_p1_13_failure_patterns_case_library.md` | 智能药柜失败模式案例库 | case | 修正未来药房、广西试点、叮当关城、政策收紧等失败案例共因分析 |

### 一线验证素材

| 文件 | 用途 |
|---|---|
| `field-validation-toolkit.md` | 厂商访谈提纲、消费者问卷、药监/医保电话咨询脚本、药店供应链访谈提纲、数据记录表 |

---

## 与 `30_wiki/` 的迁移关系

本目录下的知识卡草稿采用与 `30_wiki/` 一致的 YAML frontmatter 格式，可直接用于迁移。

每张知识卡的 `related` 字段已补充与现有 `30_wiki/` 知识库的关联：

| 知识卡 | 关联的现有知识库卡片 |
|---|---|
| `kc_p0_01_national-policy-redlines` | `master-decision-hygiene`、`master-systems-thinking` |
| `kc_p0_02_regional-policy-map` | `master-decision-hygiene` |
| `kc_p0_03_financial_model` | `yt-unit-model-three-tools`、`yt-five-step-method`、`master-cognitive-bias-checklist`、`master-antifragile-checklist` |
| `kc_p0_04_fraud_detection` | `master-cognitive-bias-checklist`、`master-decision-hygiene` |
| `kc_p0_05_o2o_cost_structure` | `yt-unit-model-three-tools`、`master-antifragile-checklist` |
| `kc_p0_06_clinic-cabinet-risk-observation` | `master-antifragile-checklist`、`master-cognitive-bias-checklist`、`master-decision-hygiene`、`master-systems-thinking` |
| `kc_p1_09_giants_why_not_clinic_cabinet` | `master-systems-thinking`、`master-decision-hygiene`、`master-antifragile-checklist` |
| `kc_p1_10_medical_shortvideo_compliance_for_clinics` | `master-cognitive-bias-checklist`、`master-decision-hygiene` |
| `kc_p1_11_clinic_cabinet_legal_relationships` | `master-decision-hygiene`、`master-antifragile-checklist` |
| `kc_p1_12_site_selection_deep_dive` | `yt-unit-model-three-tools`、`master-decision-hygiene` |
| `kc_p1_13_failure_patterns_case_library` | `master-cognitive-bias-checklist`、`master-antifragile-checklist` |

迁移前建议：

1. 由熟悉医药监管的同事复核 P0-1、P0-2 政策合规内容。
2. 由财务/投资背景的同事复核 P0-3 财务模型假设和测算。
3. 由法务/风控同事复核 P0-4 招商骗局识别清单。
4. 由 O2O/零售运营同事复核 P0-5 平台抽成和毛利结构。
5. 由医疗合规/诊所运营同事复核 P0-6 诊所+药柜风险观察、P1-10 医疗短视频合规、P1-11 法律关系与合同要点。
6. 由战略/投资同事复核 P1-09 巨头竞争格局分析。
7. 由零售运营/选址专家复核 P1-12 选址深度指南。
8. 由风控/投资同事复核 P1-13 失败模式案例库。

---

## 关联文件

- `corr_20260613_smart-medicine-cabinet-executive-summary.md`（决策层执行摘要）
- `corr_20260613_smart-medicine-cabinet-knowledge-cards-proposal.md`（知识卡建议清单）
- `corr_20260613_smart-medicine-cabinet-research-gaps-and-validation-needs.md`（待验证缺口清单）
- `corr_20260613_smart-medicine-cabinet-iteration-8-synthesis.md`（第八轮深挖综合总结）
- `corr_20260613_guangzhou-phone-inquiry-scripts.md`（广州医保/卫健电话咨询脚本）
- `corr_20260613_vendor-evidence-request-checklist.md`（推销方实证索取清单）
- `corr_20260613_clinic-interview-bias-correction-report.md`（诊所访谈偏见纠偏报告）
