# 药柜主题知识库迁移草案

## 迁移标准

根据 `QUALITY-CONTROL.md` 第 6 节，同时具备以下条件方可考虑迁移至 `30_wiki/`：

1. 可信度评分 ≥ 0.78
2. 无概念性错误
3. 来源清晰可追溯
4. 已标注局限性和适用边界
5. 经过至少一轮外部交叉验证
6. 非严重依赖单一利益相关方来源

---

## 建议迁移至 30_wiki 的卡片（高可信）

以下 8 张卡片满足或接近迁移标准，建议优先迁移。

| 序号 | 当前文件名 | 当前完整路径 | 建议 30_wiki 路径 | 类型 | 置信度 | 迁移理由 | 注意事项 |
|------|-----------|-------------|-----------------|------|--------|---------|----------|
| 1 | `fact-national-policy-redlines.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/fact-national-policy-redlines.md` | `Desktop/wiki/30_wiki/concepts/medical-cabinet-national-policy-redlines.md` | 事实卡 | **0.88** | 48 号公告原文 + 官方政策解读，来源权威 | 政策会更新，建议设置 3 个月复核周期 |
| 2 | `concept-medical-cabinet-compliance-redlines.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-compliance-redlines.md` | `Desktop/wiki/30_wiki/concepts/medical-cabinet-compliance-redlines.md` | 概念卡 | **0.82** | 法规原文逐条对照，多源验证 | 需随政策更新 |
| 3 | `concept-medical-shortvideo-compliance-for-clinics.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-shortvideo-compliance-for-clinics.md` | `Desktop/wiki/30_wiki/concepts/medical-shortvideo-compliance-for-clinics.md` | 概念卡 | **0.82** | 平台官方规则 + 国家法规 + 处罚案例，外部验证充分 | 平台规则变化快，需定期复核 |
| 4 | `concept-regional-policy-map.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-regional-policy-map.md` | `Desktop/wiki/30_wiki/concepts/medical-cabinet-regional-policy-map.md` | 概念卡 | **0.82** | 基于多地政策文件和行业报告 | 地方政策动态变化，需标注更新时间 |
| 5 | `fact-o2o-cost-structure.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/fact-o2o-cost-structure.md` | `Desktop/wiki/30_wiki/facts/medical-cabinet-o2o-cost-structure.md` | 事实卡 | **0.82** | 平台费率可公开验证 | 费率可能调整，需标注生效时间 |
| 6 | `concept-medical-cabinet-fraud-detection.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-fraud-detection.md` | `Desktop/wiki/30_wiki/concepts/medical-cabinet-fraud-detection.md` | 概念卡 | **0.85** | 基于公开处罚案例和行业报告，纠偏了录音中的夸张案例 | 部分数据为案例归纳，非统计结论 |
| 7 | `insight-failure-patterns-case-library.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-failure-patterns-case-library.md` | `Desktop/wiki/30_wiki/insights/medical-cabinet-failure-patterns.md` | 洞察卡 | **0.80** | 多案例交叉，明确区分证据与推断 | 案例为概括性，需标注来源 |
| 8 | `insight-giants-why-not-clinic-cabinet.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-giants-why-not-clinic-cabinet.md` | `Desktop/wiki/30_wiki/insights/medical-cabinet-giants-why-not-clinic-cabinet.md` | 洞察卡 | **0.80** | 基于巨头公开财报/战略和监管逻辑推导 | 部分为推断，已标注 |

---

## 建议暂不迁移，留在 60_feedback 继续完善的卡片

以下 11 张卡片因置信度不足、依赖项目方单方数据、或关键假设待验证，建议留在 `60_feedback/itingnao/medical-cabinet-longterm/` 继续完善。

| 序号 | 当前文件名 | 完整路径 | 类型 | 置信度 | 暂不迁移理由 |
|------|-----------|---------|------|--------|-------------|
| 1 | `concept-pitch-vs-regulation-misalignment.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-pitch-vs-regulation-misalignment.md` | 概念卡 | 0.78 | 刚好踩线，但内容严重依赖项目推销方录音，建议再经一轮官方口径验证后迁移 |
| 2 | `insight-international-medical-cabinet-experience.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-international-medical-cabinet-experience.md` | 洞察卡 | 0.78 | 踩线，部分国家数据为二手归纳，建议补充更多当地法规原文 |
| 3 | `concept-clinic-cabinet-legal-relationships.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-clinic-cabinet-legal-relationships.md` | 概念卡 | 0.76 | 法律关系复杂，建议经律师审核后再迁移 |
| 4 | `method-medical-cabinet-site-selection.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-site-selection.md` | 方法卡 | 0.76 | 框架通用性好，但药柜场景数据不足，建议补充实地验证案例 |
| 5 | `concept-medical-cabinet-hardware-technology.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-hardware-technology.md` | 概念卡 | 0.72 | 技术细节来自项目方讨论，且 Windows/医保版本状态存在矛盾，需进一步验证 |
| 6 | `concept-medical-cabinet-payment-settlement.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-payment-settlement.md` | 概念卡 | 0.72 | 支付架构建议为通用方向，具体方案需财务/合规专业复核 |
| 7 | `concept-medical-cabinet-his-system.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-his-system.md` | 概念卡 | 0.74 | 3424604 云聚米直接信息有限，部分为通用医疗信息系统知识，需补充项目实际系统文档 |
| 8 | `method-single-point-financial-model.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/method-single-point-financial-model.md` | 方法卡 | 0.72 | 所有数字为估算，缺乏运营商真实数据 |
| 9 | `insight-consumer-willingness-medical-cabinet.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-consumer-willingness-medical-cabinet.md` | 洞察卡 | 0.72 | 消费者数据多为行业报告和间接推断，缺乏针对智能药柜的实地调研 |
| 10 | `method-medical-cabinet-business-model-decomposition.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-business-model-decomposition.md` | 方法卡 | 0.70 | 框架可信，但录音数据填充来源利益相关，需线下验证关键假设 |
| 11 | `medical-cabinet-contaminated-recordings-review.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/medical-cabinet-contaminated-recordings-review.md` | 辅助文件 | — | 过程文件，不适合进入 30_wiki |
| 12 | `medical-cabinet-field-validation-checklist.md` | `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/medical-cabinet-field-validation-checklist.md` | 辅助文件 | — | 任务清单，不适合进入 30_wiki |

---

## 迁移操作清单

### 立即迁移（8 张）

```bash
# 目标目录需先确认存在
mkdir -p "Desktop/wiki/30_wiki/concepts"
mkdir -p "Desktop/wiki/30_wiki/facts"
mkdir -p "Desktop/wiki/30_wiki/insights"

# 复制文件（不要移动，保留 60_feedback 原稿作为草稿/纠偏记录）
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/fact-national-policy-redlines.md" "Desktop/wiki/30_wiki/concepts/medical-cabinet-national-policy-redlines.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-compliance-redlines.md" "Desktop/wiki/30_wiki/concepts/medical-cabinet-compliance-redlines.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-shortvideo-compliance-for-clinics.md" "Desktop/wiki/30_wiki/concepts/medical-shortvideo-compliance-for-clinics.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-regional-policy-map.md" "Desktop/wiki/30_wiki/concepts/medical-cabinet-regional-policy-map.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/fact-o2o-cost-structure.md" "Desktop/wiki/30_wiki/facts/medical-cabinet-o2o-cost-structure.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/concept-medical-cabinet-fraud-detection.md" "Desktop/wiki/30_wiki/concepts/medical-cabinet-fraud-detection.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-failure-patterns-case-library.md" "Desktop/wiki/30_wiki/insights/medical-cabinet-failure-patterns.md"
cp "Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/insight-giants-why-not-clinic-cabinet.md" "Desktop/wiki/30_wiki/insights/medical-cabinet-giants-why-not-clinic-cabinet.md"
```

> **注意**：本草案仅列出操作命令，不实际执行迁移。是否迁移由老顽童审核后决定。

---

## 迁移前需老顽童确认的问题

1. **30_wiki 目录结构**：上述建议路径中的 `concepts/`、`facts/`、`insights/` 是否与现有 30_wiki 分类一致？
2. **命名规范**：是否采用 `medical-cabinet-*.md` 前缀以统一药柜主题？
3. **是否保留 60_feedback 原稿**：建议保留原稿并在 30_wiki 副本中标注"迁移来源"，便于后续复核。
4. **政策类卡片复核周期**：是否同意对政策/平台规则类卡片设置 3 个月复核周期？
5. **低可信卡片是否降级**：对 0.72 以下的卡片，是否需要添加"暂不建议使用"的醒目标注？

---

## 所有药柜主题文件完整路径

### 基础卡（19 张）

全部位于：`Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/`

1. `fact-national-policy-redlines.md`
2. `concept-regional-policy-map.md`
3. `method-single-point-financial-model.md`
4. `fact-o2o-cost-structure.md`
5. `concept-medical-cabinet-compliance-redlines.md`
6. `concept-pitch-vs-regulation-misalignment.md`
7. `insight-failure-patterns-case-library.md`
8. `concept-medical-cabinet-fraud-detection.md`
9. `concept-clinic-cabinet-legal-relationships.md`
10. `method-medical-cabinet-site-selection.md`
11. `insight-international-medical-cabinet-experience.md`
12. `insight-consumer-willingness-medical-cabinet.md`
13. `insight-giants-why-not-clinic-cabinet.md`
14. `concept-medical-cabinet-hardware-technology.md`
15. `method-medical-cabinet-business-model-decomposition.md`
16. `concept-medical-shortvideo-compliance-for-clinics.md`
17. `concept-medical-cabinet-payment-settlement.md`
18. `concept-medical-cabinet-his-system.md`

### 辅助/管理文件（4 份）

1. `Desktop/wiki/60_feedback/itingnao/medical-cabinet-roadmap.md`
2. `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/medical-cabinet-contaminated-recordings-review.md`
3. `Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/medical-cabinet-field-validation-checklist.md`
4. `Desktop/wiki/60_feedback/itingnao/kcards-v3/QUALITY-CONTROL.md`

---

## 老顽童取件说明

老顽童可直接在以下目录查看所有药柜主题文件：

```
Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/
```

重点审核文件：
- 迁移草案：`Desktop/wiki/60_feedback/itingnao/medical-cabinet-longterm/MIGRATION-DRAFT.md`
- 路线图：`Desktop/wiki/60_feedback/itingnao/medical-cabinet-roadmap.md`
- 高可信卡片（建议迁移的 8 张）已在迁移草案中列出完整路径

---

*生成时间：2026-06-13*  
*草案版本：v1.0*  
*状态：待老顽童审核*
