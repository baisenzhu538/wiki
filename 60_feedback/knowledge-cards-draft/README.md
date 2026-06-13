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

### 一线验证素材

| 文件 | 用途 |
|---|---|
| `field-validation-toolkit.md` | 厂商访谈提纲、消费者问卷、药监/医保电话咨询脚本、药店供应链访谈提纲、数据记录表 |

---

## 与 `30_wiki/` 的迁移关系

本目录下的知识卡草稿采用与 `30_wiki/` 一致的 YAML frontmatter 格式，可直接用于迁移。迁移前建议：

1. 由熟悉医药监管的同事复核 P0-1、P0-2 政策合规内容。
2. 由财务/投资背景的同事复核 P0-3 财务模型假设和测算。
3. 由法务/风控同事复核 P0-4 招商骗局识别清单。
4. 由 O2O/零售运营同事复核 P0-5 平台抽成和毛利结构。

---

## 关联文件

- `corr_20260613_smart-medicine-cabinet-knowledge-cards-proposal.md`（知识卡建议清单）
- `corr_20260613_smart-medicine-cabinet-research-gaps-and-validation-needs.md`（待验证缺口清单）
- `corr_20260613_smart-medicine-cabinet-iteration-7-supplemental-deep-dive.md`（第七轮深挖报告）
