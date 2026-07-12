---

id: case-yi-tang-ai-gao-kao-zhi-yuan-kernel-mismatch
title: 案例：AI高考志愿填报产品因内核错位而失敗
type: case
status: reviewed
domain:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
industry: 教育科技 / AI 工具
scale: 团队/公司
source_person: 一堂·Truman
source_context: 一堂-产品内核实操课（Truman 口述 + 笔记）
source_refs:
- 10_raw/sources/src_20260606_6fa04636-一堂-产品内核实操课-truman-笔记.md
- 10_raw/sources/src_20260619_e67b2222_00_inbox_一堂_产品内核实操课_Truman_口述.txt
created_at: '2026-06-08'
updated_at: '2026-06-28'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.9
trust_level: medium
related:
  - "[[tool-从案例中学习]]"
  - "[[ocr-一堂-案例拆解-课程清单]]"
  - "[[ocr-一堂-科学决策-深度-案例02]]"
  - "[[case-科学决策-深度案例06]]"
  - "[[ocr-一堂-科学决策-roi决策评估画布-案例02]]"
  - "[[case-科学决策-深度案例02]]"
  - "[[ocr-一堂-科学决策-roi决策评估画布-案例01]]"
  - "[[ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02]]"
  - "[[tool-纪浩-案例池构建法]]"
  - "[[case-科学决策-ROI案例03]]"
  - "[[tool-马易-业务问题AI化拆解-餐饮设计案例法]]"
  - "[[ocr-一堂-科学决策-深度-l4-案例01]]"
wiki_refs:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- lens: 产品内核从用户触点滑向产品触点
  follow_up: 列出用户选择该品类时的3个决定性要素，再检查现有卖点是否排在前列
- lens: 风险不对称设计
  follow_up: 如果推荐导致滑档/退档，产品能否给出可执行的补救方案和责任边界？
- lens: 信息不对称 + 信任缺口
  follow_up: 能否用第三方数据溯源、专家背书或人工复核把"不可验证"变成"可验证"？

---

# 案例：AI高考志愿填报产品因内核错位而失敗

> 老顽童整理 · 一堂产品内核实操课案例

## 一句话摘要

AI 高考志愿填报团队把"智能问答 + 算法推荐"当成产品内核，但家长真正为"信任、信息准确、防滑档"买单；内核错位导致产品难以被选择。

## 背景

- src_unknown
- src_unknown
- src_unknown

## 关键事件/决策点

1. **功能视角定位**：团队给自己定位为"AI 智能问答咨询"，并集结团队做小程序实现该功能（`src_20260619_e67b2222#654`）。
2. **对外宣传强调智能**：对外说法是"我们做了一个非常牛的高考填报系统，非常智能"（`src_20260619_e67b2222#676`）。
3. **用户真实反应**：家长质疑"我怎么敢让我的孩子使用这种产品去填报志愿"（`src_20260619_e67b2222#706`）。
4. **发现决策逻辑错位**：一堂指出，大家对高考报考志愿不了解，因此不是"不会问"，而是"无法判断 AI 答案是否可靠"（`src_20260619_e67b2222#718`）。
5. **重新识别内核**：家长选择志愿填报服务的决定性要素是**信任、信息全面性、防滑档**，而非"智能"本身。

| 维度 | 团队原先以为的内核 | 用户真正的决策逻辑 | 纠正后的内核要素 |
|:---|:---|:---|:---|
| 信任 | "我们的 AI 很聪明" | "如果推荐错了，有人能负责吗？" | 专家背书、责任承诺、官方数据来源 |
| 信息 | "我们的数据很全" | "你的分数线/专业设置是否准确？" | 数据准确性证明、实时更新机制 |
| 防滑档 | "我们的算法很准" | "如果滑档了怎么办？" | 多轮校验、保底院校方案、人工复核 |

## 结果

- src_unknown
- src_unknown
- src_unknown

## 复盘与洞察

1. **产品内核是用户选择逻辑，不是团队功能亮点**。再强的算法，如果解决不了用户"敢不敢用"的问题，就不是内核。
2. **高风险决策中，"责任"与"风险控制"是决定性要素，"智能"只是优化项**。高考志愿填报的错误成本不可逆，家长优先购买的是确定性而非炫酷体验。
3. **信息不对称会放大信任缺口**。当用户无法判断 AI 答案对错时，交互越"智能"，反而越让人不安；必须引入可验证的信任信号（数据来源、专家背书、人工复核）。
4. **切换视角的核心问句**："如果去掉这个功能，用户还会选我吗？"能回答"会"的，才是内核。

## 可迁移场景

| 可迁移场景 | 说明 |
|:---|:---|
| **技术驱动产品** | AI、大数据、算法类产品易从"功能视角"定义内核，需要回归用户决策逻辑。 |
| **高风险决策行业** | 医疗、金融、法律、教育等领域，信任与风险控制通常比"智能"更重要。 |
| **信息不对称行业** | 用户无法快速判断产品质量时，需要通过第三方证书、专家背书、责任承诺建立信任。 |

**不可复制场景**：

- src_unknown
- src_unknown
- src_unknown

## 教训

- src_unknown（待补充：从本案例学到的核心教训）

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:---|:---|:---|
| **功能至上误区（Feature-first fallacy）** | 把"智能问答""算法推荐"当核心卖点，忽视用户为何选择 | 用"去掉这个功能，用户还会选我吗"测试每一项卖点 |
| **信任缺失（Trust-neglect）** | 高风险场景中没有任何责任承担机制 | 明确责任主体、数据来源、专家背书与人工复核流程 |
| **风险不对称设计（Risk-asymmetric design）** | 用户承担大量潜在风险，产品只强调好处 | 提供保底方案、退换/补救机制，把风险与收益对齐 |

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown
  - src_unknown
  - src_unknown

## Feedback Path

应用本案例后，用以下问题循环复盘：

1. 我的目标用户在选择时最担心的风险是什么？
2. 我现在强调的"功能亮点"是否能够解决这个风险？
3. 如果我去掉这个功能，用户还会选我吗？
4. 用户真正愿意为之付费的是信任保障、风险控制，还是智能交互？
5. 我是否能用第三方证据或承诺增强信任？

- src_unknown

## 关键证据

| 证据点 | 来源 | 可检验性 |
|:---|:---|:---|
| src_unknown | src_unknown | src_unknown |
| src_unknown | src_unknown | src_unknown |
