---
id: case-科学决策-深度案例06
title: 案例：电话外呼的ROI分析
type: case
status: reviewed
created_at: 2026-06-28
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.7
trust_level: medium-low
language: zh-CN
domain:
- yitang
- decision-science
source_refs:
- 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-深度-案例06_vlm_desc.md
- 10_raw/ocr-cards/ocr-一堂-科学决策-深度-案例06.md
related:
- '[[yitang-domain-digest]]'
- '[[decision-science-domain-digest]]'
- '[[pending_unknown]]'
- '[[case-ai-assisted-review]]'
- '[[case-ban-fei-mao-from-assignment-to-tool]]'
- '[[case-candy-problem-os-vpn]]'
- '[[case-child-drawing-rhyme]]'
- '[[case-course-milestone-model]]'
- '[[case-demand-ai-fitness-four-forces]]'
- '[[case-demand-dialer]]'
- '[[case-demand-elderly-smart-device]]'
- '[[case-demand-equestrian-three-tasks]]'
- '[[case-demand-financial-literacy]]'
- '[[case-demand-indonesia-insurance]]'
- '[[case-demand-milkshake-jtbd]]'
- '[[case-demand-pharma-bigdata]]'
- '[[case-demand-restaurant-hiring]]'
- '[[case-demand-rural-5g]]'
- '[[case-demand-silver-parenting]]'
- '[[case-demand-tier4-housekeeping]]'
- '[[case-demand-travel-agent]]'
- '[[case-essence-entrepreneurship]]'
- '[[case-essence-humanity-trap]]'
- '[[case-ether-online-acquisition]]'
- '[[case-guang-leng-dian-zi-hx-smj]]'
- '[[case-jh-yitang-vs-sqlhelper]]'
- '[[case-ji-hao-skills-market]]'
- '[[case-modeling-abstraction-reliability-ladder]]'
- '[[case-modeling-abstraction-yitang-models]]'
- '[[case-modeling-essence-levels]]'
- '[[case-modeling-essence-schools]]'
- '[[case-modeling-process-livestream-prep]]'
- '[[case-modeling-process-livestream-roles]]'
- '[[case-modeling-process-sop-examples]]'
- '[[case-nine-pm-livestream-survey]]'
- '[[case-personal-map-modeling]]'
- '[[case-strategy-failure-01-cosmetics]]'
- '[[case-strategy-failure-02-supermarket]]'
- '[[case-strategy-failure-03-cleaning]]'
- '[[case-strategy-failure-04-appliance]]'
- '[[case-strategy-failure-09-boeing]]'
- '[[case-strategy-practice-10-turnaround]]'
- '[[case-strategy-practice-11-third-place]]'
- '[[case-strategy-practice-12-zero-loss]]'
- '[[case-strategy-practice-ranpeng-crossborder]]'
- '[[case-strategy-revival-13-bestore]]'
- '[[case-strategy-revival-14-gucci]]'
- '[[case-truman-sales-report-structure]]'
- '[[case-yi-tang-ai-gao-kao-zhi-yuan-kernel-mismatch]]'
- '[[case-yitang-double-triangle-confidence]]'
- '[[case-yitang-model-asset-inventory]]'
- '[[case-yitang-model-valuation-flywheel]]'
- '[[case-yitang-radar-chart-selection]]'
- '[[case-yitang-tob-grinding-machine]]'
- '[[case-zhangyang-anchor-sop-three-locks]]'
- '[[case-一堂-陈贤敏汉堡-hypothesis-validation]]'
- concept-X型Y型决策习惯
- concept-发现决策
updated_at: '2026-06-29'
review_date: '2026-06-29'
---

# 案例：电话外呼的 ROI 分析

## 案例来源

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 核心洞察

**外呼团队的 ROI 不仅取决于"每人每月能打多少通电话"，更取决于"线索质量 × 接通率 × 转化率"的全漏斗假设。** 这个案例暴露了产能规划与漏斗数字之间的一致性问题：按 40 人 × 100 通/天 × 20% 有效 × 20% 邀约成功，只能得到 3520 个体验课用户，与宣称的 4000 个存在缺口。

## 事迹/背景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关键数字

| 项目 | 数值 | 说明 | 可信度 |
|:---|:---|:---|:---:|
| 采购线索成本 | 10 万/月 | 单价按最低 1 元/条估算 | [conf=0.65, source=原图/VLM描述] |
| 外呼团队成本 | 24 万/月 | 团队综合成本 | [conf=0.60, source=原图/VLM描述] |
| 团队规模 | 40 人 | 配置依据未披露 | [conf=0.55, source=原图/VLM描述] |
| 人均日外呼量 | 100 通 | 产能假设 | [conf=0.55, source=原图/VLM描述] |
| 线索有效率 | 20% | 漏斗第一层转化率 | [conf=0.50, source=原图/VLM描述] |
| 邀约成功率 | 20% | 漏斗第二层转化率 | [conf=0.50, source=原图/VLM描述] |
| 目标体验课用户 | 4000 个/月 | 宣称收益 | [conf=0.50, source=原图/VLM描述] |
| 理论最大产出 | 3520 个/月 | 40×100×22×20%×20% | [conf=0.60, source=案例推演] |

## 关键证据表

1. **成本结构清晰**：线索采购 + 团队成本两大类，月度现金流出可识别。
2. **漏斗分层**：从外呼量 → 有效线索 → 邀约成功，展示了 L3 定量公式的思路。
3. **品牌负收益被识别**：外呼可能带来品牌伤害，虽然难量化但被记录。
4. **内部一致性存疑**：理论最大产出 3520 < 目标 4000，缺口 480 个未解释。

## 失败/成功原因

**如果决策成功**：
1. 用漏斗模型把外呼产能拆解到可管理的关键假设。
2. 区分了验证数据与假设数据，为后续 A/B 测试留出接口。

**失败/风险因素**：
1. **产能与目标不匹配**：按给定参数无法达成 4000 个目标。
2. **"最低 1 元/条"假设来源不明**：实际单价可能更高，对 ROI 影响大。
3. **人均日外呼 100 通未验证**：未考虑接通率、有效通话时长、人员流失。
4. **转化率未与行业基准对比**：20%→20% 是否乐观或保守无从判断。
5. **团队配置逻辑反推问题**：40 人是基于 4000 目标反推，还是先有人再定目标？
6. **品牌负收益未建模**：仅标注"存在，很难量化"，未尝试 NPS、流失率等替代指标。

## 对立面/争议

- src_unknown
- src_unknown
- src_unknown

## 可迁移场景

- src_unknown
- src_unknown
- src_unknown

## 教训与预警信号

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与王欢/一堂框架的映射

- src_unknown
- src_unknown
- src_unknown

## Critique

> 本节基于 OCR 原文中的攻击者视角与一堂科学决策框架推理生成。

- src_unknown
- src_unknown

---

*2026-06-26 重写：基于 VLM 描述、OCR 文本与一堂框架推理补充 9 层案例结构。*

## 关键证据

| 证据点 | 来源 | 可检验性 |
|:---|:---|:---|
| src_unknown | src_unknown | src_unknown |
| src_unknown | src_unknown | src_unknown |

## 教训

- src_unknown（待补充：什么时候应该学这个案例（正面））

## 失败模式

- src_unknown（待补充：常见的踩坑方式和避免方法（反面））
