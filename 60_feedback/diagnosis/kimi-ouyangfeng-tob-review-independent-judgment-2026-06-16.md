---
id: kimi-ouyangfeng-tob-review-independent-judgment-2026-06-16
title: 对欧阳锋徐剑 ToB 审查意见的独立判断
type: report
status: draft
domain:
- kdo-quality
author: kimi
reviewed_by: pending
confidence: 0.85
trust_level: medium-high
source_refs:
- src_20260616_0e684368
- src_20260616_5f991553
created_at: '2026-06-16'
updated_at: '2026-06-16'
---

# 对欧阳锋徐剑 ToB 审查意见的独立判断

## 背景

欧阳锋对老顽童产出的徐剑 ToB 五步法域 13 张卡片给出审查意见：8/10，A- 级，高于精益创业域（B+）。提出 2 项必修补 + 1 项可选修补。

Kimi 在欧阳锋处理后做独立复核，判断其评分是否准确、是否有遗漏。

## 复核方法

1. 深度阅读 3 张关键卡片：`yt-tob-revenue-is-customer-cost`、`yt-tob-core-characteristics`、`yt-tob-product-kernel`。
2. 抽查 `yt-tob-demand-metrics` 修改后的敏感性分析。
3. 检查 12 张卡片的 source_refs 注册情况和 related 链接有效性。
4. 对比精益创业域和徐剑 ToB 域的执行一致性。

## 复核结果

### 1. source_refs 与 related 链接

- **source_refs**：12 张卡片均引用 `src_20260616_0e684368` 和 `src_20260616_5f991553`，两个 src_ID 均已在 `.kdo/source_id_map.json` 注册 ✅
- **related 链接**：抽查 12 张卡片，所有 wikilink 目标均存在于 `30_wiki/` 中 ✅

### 2. 欧阳锋 3 项修补的执行情况

| # | 问题 | 欧阳锋建议 | Kimi 复核 | 处理结果 |
|---|---|---|---|---|
| 1 | `yt-tob-customer-sabc` type=tool 但放 concepts/ | 移入 tools/ 或改 type | 合理，tools/ 目录存在且已有 tool 类型卡片 | ✅ 已移入 `30_wiki/tools/` |
| 2 | `yt-tob-sales-unit-model` type=skill 但放 concepts/ | 移入 tools/ 或改 type | 可接受改 type；concepts/ 下已有大量 skill-* 卡，但本卡内容更偏概念 | ✅ type 改为 concept |
| 3 | 天花板公式缺少敏感性分析 | 补充说明 | 合理，原卡公式确实容易被当作精确财务预测 | ✅ 已补充 2.3 节 |

### 3. 欧阳锋未指出但 Kimi 发现的问题

#### 3.1 概念归属不清（与精益创业域同类问题）

12 张卡片的标题均未体现"一堂徐剑版"或"一堂 To B 五步法"，容易被误认为是通用 To B 方法论。例如：

- `yt-tob-revenue-is-customer-cost` 标题为"To B 收入本质 = 客户成本"
- `yt-tob-core-characteristics` 标题为"To B 三大核心特性：角色分离、务实理性、周期较长"

这些表述在内容上是徐剑基于 20 年 To B 经验和一堂课程框架的提炼，不是 To B 通识。与精益创业域一样，存在"一堂方法论被写成通用知识"的风险。

**建议**：在 title 或 frontmatter 中增加 source_person/source_context 的显性标注，或在 title 前缀加"一堂徐剑版"。例如：
- "一堂徐剑版：To B 收入本质 = 客户成本"
- "一堂徐剑版：To B 三大核心特性"

#### 3.2 部分表述仍偏绝对化

虽然卡片整体已较规范，但仍有个别表述接近普遍规律：

- `core-characteristics` 标题将"角色分离、务实理性、周期较长"称为"三大核心特性"，暗示这是 To B 的全部或主要特性。
- 更严谨的说法应为"徐剑观察到的 To B 三大关键特性"或"一堂 To B 五步法强调的三大特性"。

#### 3.3 与经典 To B/B2B 方法论缺少对话

卡片未提及 Crossing the Chasm、SPIN Selling、Challenger Sale、MEDDIC、BANT 等经典 To B 销售/产品方法论，也未说明徐剑框架与这些经典框架的关系。知识库价值在于建立知识网络，而非仅积累课程笔记。

## 独立评分

| 维度 | 欧阳锋评分 | Kimi 独立评分 | 差异说明 |
|---|---|---|---|
| 执行一致性 | 高 | 高 | 一致；13 张全部 enriched、diagnostic 全覆盖 |
| 内容深度 | 高 | 高 | 一致；revenue-is-customer-cost、product-kernel 确实有洞察 |
| 来源边界 | 中 | 中偏低 | 欧阳锋未强调概念归属问题 |
| 与通用知识对话 | 未评价 | 低 | 缺少经典 To B 方法论关联 |
| 信源处理 | 高 | 高 | 一致；矛盾标注规范 |

**Kimi 综合评分：7.5/10**（欧阳锋 8/10）。

差异主要来自：
1. 概念归属问题未解决（扣 0.5 分）
2. 缺少与经典 To B 方法论的对话（扣 0.5 分）

## 是否通过的裁决

**建议：有条件通过**。

已通过条件：
- ✅ 欧阳锋提出的 3 项修补已完成
- ✅ source_refs 已注册
- ✅ related 链接有效
- ✅ 质量门禁 P0=0, P1=0

建议追加的非阻塞改进：
1. **概念归属标注**：在 12 张卡片的 title 或 frontmatter 中明确"一堂徐剑版"来源
2. **经典对话**：在 `core-characteristics`、`product-kernel`、`growth-channel` 等卡中增加"与经典 To B 方法论的关系"小节
3. **aliases 字段**：等黄药师 S4-1 完成后，为这些卡添加 aliases（如"B2B 收入本质"、"ToB 三大特性"）

## 与精益创业域的横向对比

| 维度 | 精益创业域 | 徐剑 ToB 域 |
|---|---|---|
| 卡数 | 15 | 13 |
| status enriched | 80% | 100% ✅ |
| diagnostic_signals 覆盖率 | 93% | 100% ✅ |
| source_refs 注册 | ✅ | ✅ |
| related 链接有效性 | ✅ | ✅ |
| 概念归属问题 | 有 | 有（同样存在） |
| 与经典知识对话 | 不足 | 不足 |
| 信源矛盾处理 | 较好 | 更好 ✅ |
| 平均 confidence | 0.80 | 0.83 |

**结论**：徐剑 ToB 域的执行一致性确实优于精益创业域，但在"概念归属"和"经典对话"两个维度上仍有同类问题。差距没有 8 vs B+ 那么大，更准确的评价是"徐剑域 B+~A-，精益域 B~B+"。

## 下一步建议

1. **黄药师**：在 S4-1 aliases 字段落地后，为 ToB 卡片批量添加 aliases。
2. **老顽童**：在 title 或 frontmatter 中补充"一堂徐剑版"来源标注（非阻塞，可后续迭代）。
3. **欧阳锋**：抽检时重点验证案例数字和概念边界，不要只看形式指标。
4. **Kimi**：下次入口质量门报告中增加"概念归属"和"经典对话"两列检查项。
