# 冉鹏战略专题知识卡片实施状态

> 质量负责人：王语嫣（CLI） | 审核：欧阳锋 | 最后更新：2026-06-22

---

## 一、总体进度

| 类型 | 已完成数量 | 本次新增 | 路径 |
|--|--:|:--|--|
| Framework（框架） | 8 | +2 | `30_wiki/frameworks/framework-strategy-*` |
| Tool（工具） | 11 | +1 | `30_wiki/tools/tool-strategy-*` |
| Case（案例） | 11 | +5 | `30_wiki/cases/case-strategy-*` |
| **合计** | **30** | **+8** | — |

> 注：统计口径为本次围绕冉鹏战略课新创建/富化的卡片；仓库中另有老顽童此前创建的相关卡片。

---

## 二、Framework 框架卡（8 张）

| id | 标题 | 来源幻灯片 | 批次 |
|--|--|--|--|
| framework-strategy-business-design | 业务设计六要素框架 | _104, _294 等 | 第 1 批（已有 v2） |
| framework-strategy-pyramid | 战略金字塔 | _16, _21, _22 等 | 第 2 批 |
| framework-strategy-blm | IBM BLM 业务领导力模型 | _68, _70, _74 等 | 第 2 批 |
| framework-strategy-five-forces | 波特五力分析框架 | _74 等 | 第 2 批 |
| framework-strategy-ansoff | 安索夫增长矩阵 | _79 等 | 第 2 批 |
| framework-strategy-three-horizons | 麦肯锡三地平线增长模型 | _80 等 | 第 2 批 |
| framework-strategy-mckinsey-7s | 麦肯锡 7S 组织一致性框架 | _81 等 | 第 4 批 |
| framework-strategy-kai-innovation-directions | 凯纳创新方向分类框架 | _90 | 第 5 批追加 |

---

## 三、Tool 工具卡（11 张）

| id | 标题 | 来源幻灯片 | 批次 |
|--|--|--|--|
| tool-strategy-customer-selection | 客户选择工具 | _100-_135 等 | 第 1 批（已有 v2） |
| tool-strategy-value-proposition | 价值主张设计工具 | _106-_115 等 | 第 1 批 |
| tool-strategy-value-capture | 价值获取（盈利模式）工具 | _115-_118 等 | 第 1 批 |
| tool-strategy-activity-scope | 活动范围工具 | _119-_121 等 | 第 1 批 |
| tool-strategy-control-points | 战略控制点工具 | _122-_125 等 | 第 1 批 |
| tool-strategy-risk-management | 风险管理工具 | _126-_129 等 | 第 1 批 |
| tool-strategy-fishbone | 鱼骨图根因分析工具 | _42, _44, _48 等 | 第 3 批 |
| tool-strategy-ksf | 关键成功因素（KSF）工具 | _60-_63 等 | 第 3 批 |
| tool-strategy-core-competence-matrix | 核心能力矩阵 | _88, _89 等 | 第 3 批 |
| tool-strategy-swot | SWOT 分析工具 | _73 等 | 第 3 批 |
| tool-strategy-lifecycle | 产品生命周期工具 | _76-_78 等 | 第 3 批 |
| tool-strategy-blue-ocean-canvas | 蓝海战略画布（价值曲线工具） | _112 | 第 5 批追加 |

---

## 四、Case 案例卡（11 张）

| id | 标题 | 来源幻灯片 | 批次 |
|--|--|--|--|
| case-strategy-practice-ranpeng-milk-powder | 一米八八儿童奶粉——从零到20亿的细分垄断 | 逐字稿 §39 | 已有 |
| case-strategy-fangte-disney | 方特 vs 迪士尼：集团战略的范围经济 | 逐字稿 §21-22 | 已有 |
| case-strategy-longzhong-plan | 隆中对：中国最著名的战略规划 | 逐字稿 §19-20 | 已有 |
| case-strategy-practice-ranpeng-crossborder | 美区 TikTok 跨境电商——3个月一单没卖 | 逐字稿 §17 | 已有 |
| case-strategy-li-ka-shing | 李嘉诚分筋错骨手：逆势并购→等涨 | 逐字稿 §23 | 已有 |
| case-strategy-walmart-vs-costco-pyramid | 沃尔玛 vs 好市多：同样的"性价比第一"，不同的战略金字塔 | _21 | 第 5 批 |
| case-strategy-retailer-activity-scope | 零售商 A/B/C：客户选择、价值主张与活动范围的三角对齐 | _121 | 第 5 批 |
| case-strategy-m-brand-profit-model | M 品牌：从直营到代理加盟的连锁扩张盈利模式选择 | _117 | 第 5 批 |
| case-strategy-snack-business-design | 零食企业业务设计示例：从大众散货到家庭健康亲子零食专家 | _131, _104, _66 | 第 5 批 |
| case-strategy-model-selection-quiz | 10情境战略模型选择练习：什么情境配什么工具 | _203, _204 | 第 5 批 |

---

## 五、已解决的原待确认项

| 待确认项 | 状态 | 说明 |
|--|:--|--|
| 凯纳创新框架 | ✅ 已创建 | 在 _90 中找到，标题"创新往哪里找"，三层创新方向分类 |
| 蓝海战略四步动作框架 | ✅ 已创建（价值曲线工具） | 在 _112 中找到"蓝海战略战略画布"，以价值曲线形式呈现；四步动作作为工具卡补充 |

---

## 六、Parser 修复状态

- 修复者：黄药师（Claude Code）
- 状态：✅ 已完成，parse error 归零
- 王语嫣贡献：`repair-vlm-parse-errors.py` 状态机引号修复函数作为参考

---

## 七、下一步建议

1. **交叉链接补全**：检查所有卡片 `related` 字段的双向链接是否完整（例如 tool 卡应回链 framework 卡）。
2. **检索剩余高潜幻灯片**：_66/_67 零食产业链、_93 零售品类规划、_132 业务设计模板、_263 平台商业模式地图等尚未卡片化，可视优先级继续。
3. **全文讲义对齐**：将已创建卡片的关键结论与 `引擎点火20260110 战略破局（冉鹏）(1)_ocr.md` 讲义原文逐条核对，确保无 VLM 误读。
4. **质量复核**：由欧阳锋对新增 8 张卡片进行抽样复核，重点检查 source_refs、confidence、trust_level 是否自洽。
