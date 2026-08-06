---

id: tool-indicators-signposts
title: Indicators & Signposts（指标与信号）
type: tool
domain:
discoverable_by:
  - Indicators & Signposts指标与信号
  - Signposts指标与信号
tags:
source_person: Richars J. Heuer Jr. + Trumen（一堂）
source_context: SATs 指标类技术工具化实现
aliases:
  - Indicators&Signposts指标与信号
  - Richars J. Heuer Jr. + Trumen（一堂）
  - Signposts指标与信号
  - [[yt-decision-y-model]]
  - [[yt-research-intelligence-map]]
  - 三个新盲区
  - 外部知识探索
  - 指标与信号
source_refs:
related:
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-06-28'
created_at: '2026-06-28'
updated_at: '2026-06-29'
confidence: 0.78
trust_level: medium
---
# Indicators & Signposts（指标与信号）

## 原始表述

> "Most intelligence failures are not due to lack of information, but to failure to recognize the significance of information that was already available."
> ——Sherman Kent, CIA 首席分析师

**Signposts** 是 SATs 指标类技术的核心工具——**事先定义"什么信号出现时，我们的假设需要重新评估"**，而不是等"事实证明我们错了"再反应。

一堂有"持续跟踪"（第18掌），但**无"信号 → 假设失效"的映射关系**。本工具卡填补这个缺口。

---

## 使用场景

### 适合使用本工具的情境

- 基于关键假设做了战略决策（进入新市场、产品方向调整、竞品应对）
- 需要定义"什么信号能告诉我们'我们的假设可能错了'"
- 团队说"我们得持续关注竞品"，但说不清"关注什么信号"
- 需要建立自动化监控（Agent 可以自动追踪的信号）

### 不适合的情境

- 假设已经验证过（不需要再定义信号）
- 决策是一次性的（不需要持续监控）
- 完全没有信息来源（无法定义可观测的信号）

---

## 操作方法

### 第一步：从假设导出 Indicators（不是从"感兴趣"导出）

**核心原则**：Indicator 必须对应一个**具体的假设**，不是泛泛的"关注竞品动态"。

**示例（一堂进入 Skill 市场）**：

| 假设 | 如果假设错了，会观察到什么信号？（Indicators） | 信号类型 |
|:---|:---|:---|
| 企业客户愿意为内部工具付费 | ① 5 个目标客户中 ≥3 个拒绝付定金 ② 试点客户使用后 NPS <0 | 可观测指标 |
| 一堂的"方法论 IP"可以产品化 | ① 咨询项目交付时间 >3 个月（无法标准化） ② 客户说"你们的人好，但不是工具" | 行为信号 |
| 竞品（混沌/得到）不会快速跟进 | ① 混沌招聘"企业培训产品经理" ② 得到上线"企业内部学习"功能 | 可观测指标 |

### 第二步：区分 Leading Indicators 和 Lagging Indicators

| 类型 | 含义 | 示例 | actionability |
|:---|:---|:---|:---|
| **Indicators**（先行指标） | 假设**即将**失效的信号 | 竞品开始招聘相关岗位 | 高——可以提前应对 |
| **Indicators**（滞后指标） | 假设**已经**失效的信号 | 竞品已经发布竞品，我们丢了订单 | 低——已经晚了 |

**核心原则**：**Leading Indicator**，否则监控只告诉你"已经晚了"。

### 第三步：定义"信号触发阈值"（什么时候算"信号出现了"）

**错误示例**："关注竞品动态" → 太模糊，无法触发行动。
**正确示例**："竞品在 30 天内招聘 2 个以上相关岗位 + 官网更新'企业版'定价页" → 可触发行动。

**阈值定义模板**：
```
当 [信号描述] 出现 [次数/时间段]，
且 [补充条件]，
则触发 [具体行动]。
```

**示例（续）**：
```
当 竞品在 30 天内招聘 2 个以上"企业培训产品经理"，
且 官网出现"企业版"定价页（之前只有"个人版"），
则触发：更新 Battlecard + forecast call 上报告竞品动作。
```

### 第四步：建立 Signposts（路标）清单

**Signpost** = 比 Indicator **更早的信号**——"如果竞品要做 X，他们会先做什么？"

**示例**：
```
竞品要做"企业版" → Signpost 清单：
1. 招聘"企业培训"相关岗位（Leading Indicator）
2. 创始人/高管在公开场合讲"企业市场"（更早的 Signpost）
3. 官网 Careers 页面出现"企业客户成功经理"（更早的 Signpost）
```

---

## 与"持续跟踪"的区别

| 维度 | 一堂"持续跟踪"（第18掌） | Indicators & Signposts（SATs） |
|:---|:---|:---|
| **目标** | 持续收集竞品/市场动态 | 定义"什么信号能告诉我们假设失效" |
| **操作** | 定期更新竞品档案 | 从假设导出 Indicators，定义触发阈值 |
| **核心缺口** | 没有"信号 → 假设失效"的映射 | 有——这就是本工具的价值 |
| **补完方式** | 本工具卡 | 对接 CI Implement 阶段（Battlecard 更新触发） |

**关系**：持续跟踪是**输入**（收集信号），Indicators 是**映射**（信号 → 假设失效），Implement 是**输出**（触发行动）。

---

## 为什么值钱

1. **把"持续关注"变成"可触发的监控"**：泛泛的"关注竞品"不会产生行动，明确的"信号触发阈值"会。
2. **可教学**：Indicator 定义有四步标准流程，可以教给团队，不是依赖某个人"嗅觉好"。
3. **AI 可自动化部分**：Agent 可以自动监控公开信号（招聘信息、官网变动、新闻稿），触发通知。

---

## 与其他知识的关联

- **[[framework-structured-analytic-techniques]]**

← 本工具是 SATs 八类技术中「指标类」的代表工具

- **[[tool-key-assumptions-check]]**

← Indicators 是 Key Assumptions Check 的**延伸**——假设列出并验证后，定义"什么信号能告诉我们假设失效"

- **[[tool-red-team-analysis]]**

← Red Team 输出的"竞品可能动作"，可以直接转化为 Indicators（"如果竞品要打我们，会出现什么信号？"）

- **[[tool-ci-implement-phase]]**

→ Indicators 触发后，需要 Implement 阶段的交付物更新（Battlecard 更新、forecast call 报告）

---

## 适用边界

### 有效使用的条件

- 有明确的关键假设（否则 Indicator 没有锚点）
- 有能力监控信号（至少是人工定期查看，更好的是自动化监控）
- 信号触发后有**明确的行动**（否则监控只会产生焦虑）

### 常见误用

- **"Indicators = 竞品动态监控"** → 错误。Indicators 必须对应**具体假设**，不是泛泛的"关注竞品"。
- **"只有 Leading Indicators 就够了"** → 错误。需要同时定义 Leading（提前应对）和 Lagging（验证假设确实失效了）。
- **"Indicators 定义一次就永久有效"** → 错误。假设变化时，Indicators 需要更新。

---

## 失败模式

| 失败模式 | 症状 | 根因 | 修正方法 |
|:---|:---|:---|:---|
| **"泛泛症"** | Indicator 写成"关注竞品动态" | 没有从**具体假设**导出 | 每个 Indicator 必须写明"对应哪个假设" |
| **"滞后症"** | 所有 Indicators 都是 Lagging（已经晚了） | 没有故意思考"竞品**要做** X 之前会先做什么" | 强制"每个假设至少 1 个 Leading Indicator" |
| **"无行动症"** | Indicator 触发了，但没人知道该做什么 | 没有定义"触发阈值"和"具体行动" | 用"当...则触发..."模板定义每个 Indicator |

---

## Action Checklist

- [ ] 列出当前最重要决策背后的 1-3 个核心假设
- [ ] 对每个核心假设，导出 2-3 个 Indicators（至少 1 个 Leading）
- [ ] 定义每个 Indicator 的"触发阈值"和"具体行动"
- [ ] 建立 Signposts 清单（比 Indicators 更早的信号）
- [ ] 决定监控方式：人工定期查看 vs Agent 自动监控
- [ ] 复盘：上次假设失效时，有没有提前信号？为什么我们没注意到？

---

## 来源与验证

| 断言 | 来源 | 可信度 |
|:---|:---|:---|
| Indicators & Signposts 是 SATs 指标类核心工具 | Heuer & Pherson《Structured Analytic Techniques》 | A（权威原著） |
| "假设 → Indicator → 触发行动"映射关系 | 同上 + CIA 情报分析培训材料 | A |
| 一堂缺少"信号 → 假设失效"映射 | diag_20260621_外部知识探索_三个新盲区.md + 现有卡片搜索确认 | A（可验证） |

---

## 口述数据标注

> 来源：SATs 文献 + 一堂诊断报告交叉验证。Indicators & Signposts 四步法有原著支撑，可信度 A。一堂与 SATs 的映射关系基于诊断报告，已通过现有卡片库搜索交叉验证。
>
> ⚠️ "Leading Indicator 至少 1 个"——此为 SATs 最佳实践建议，具体数量取决于假设复杂度，可根据实际情况调整。
> ⚠️ "30 天内招聘 2 个以上"——此类具体阈值需根据行业和公司规模调整，不是固定标准。

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？

**Daniel Kahneman** 可能会质疑：这个工具依赖的 **信号噪声比、认知偏差、滞后指标、因果混淆** 是否已经被充分验证？

- 指标可能把滞后信号当成领先信号，导致行动时机错误。
- 团队容易选择支持既有观点的指标，忽视反面信号。

- 使用前应明确本工具的 **具体假设**、适用 **边界**、潜在 **反例** 和隐含 **前提**，避免把模板输出直接当成战略结论。
