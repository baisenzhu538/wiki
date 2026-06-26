---

id: framework-strategy-lean-validation
title: 战略假设的精益验证流程
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-23
created_at: 2026-06-23
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- strategy
- lean-startup
- yitang
source_refs:
- 00_inbox/战略专题/冉鹏战略课逐字稿_ocr.md
- 00_inbox/精益创业/transcript_低成本验证认知篇.md
- 60_feedback/audit/cross-domain-bridge-design-specs.md
related:
  - '[[framework-lean-pivot-decision]]'
  - '[[dk-yitang-business-model-risk-over-product-risk]]'
  - '[[framework-demand-lean-bridge]]'
  - '[[case-cross-yuanqi-forest]]'
  - '[[framework-five-step-lean-interface]]'
  - "[[framework-strategy-brm]]"
  - "[[framework-lean-false-model]]"
  - "[[framework-lean-abcd-model]]"
  - "[[yt-entrepreneur-key-hypotheses]]"
  - "[[yt-decision-y-model]]"
  - "[[strategy-domain-digest]]"
  - "[[lean-startup-domain-digest]]"
---

# 战略假设的精益验证流程

> 把战略选择翻译成一个可验证的假设清单，并用精益工具按优先级和成本排序验证。

## 触发问题

- “我们定了一个战略方向，但不知道哪里最可能错。”
- “战略会上讨论很嗨，但没人能说清楚先验证什么。”
- “老板想 all-in，我想先小步验证，怎么设计实验？”

## 端到端流程

```
战略输出（来自 strategy-domain）
  ├── 赛道选择      → 验证：市场容量、竞争格局、时机窗口
  ├── 定位选择      → 验证：目标用户是否认可差异化价值
  ├── 商业模式      → 验证：用户是否愿意按预期付费
  ├── 增长路径      → 验证：渠道成本/转化率是否成立
  └── 壁垒假设      → 验证：优势能否持续、能否被快速模仿
           ↓
    用 ABCD/假设金字塔排序关键假设
           ↓
    用 FALSE 模型选择最低成本验证工具
           ↓
    按十倍速公式设计实验 → 执行 → 学习 → 战略迭代
```

## 战略假设类型 → 待验证问题 → 精益工具 → 通过/不通过标准

| 战略假设类型 | 典型问题 | 推荐精益工具 | 通过标准示例 | 不通过标准示例 |
|:---|:---|:---|:---|:---|
| 赛道存在 | 这个市场真实存在且足够大吗？ | 假营销/新闻稿测试、竞品分析 | 100+ 有效线索 | 投放后 CTR < 0.5% |
| 需求真实 | 用户会为这个概念付费吗？ | 假产品页面、预售 | 预售转化率 > X% | 1000 UV 0 订单 |
| 方案有效 | 产品/服务能交付承诺价值吗？ | 人工 VIP、MVP | NPS > 40 | 复购率 < 5% |
| 商业模式 | 单元模型能跑正吗？ | 最小版本、小规模试运营 | LTV/CAC > 3 | 单客亏损且无法收窄 |
| 增长可扩展 | 这个渠道能放大吗？ | 灰度测试、组合测试 | CAC 随规模不上升 | CAC 翻倍而转化率不变 |
| 壁垒可持续 | 竞争优势能维持多久？ | 竞品对标、时间窗口验证 | 6 个月内无直接竞品 | 巨头 3 个月内进入 |

> 上表工具映射来自 [[framework-lean-false-model]] 与 [[framework-lean-abcd-model]] 的接口设计 [conf=0.85, source=60_feedback/audit/cross-domain-bridge-design-specs.md §2.4]。

## 与相邻卡的关系

- 入口：[[framework-strategy-brm]] 输出赛道/定位/模式/增长/壁垒假设；本卡负责把这些假设变成验证计划。
- 排序：[[framework-lean-abcd-model]] 决定“哪些假设先验”，[[yt-entrepreneur-key-hypotheses]] 提供关键假设剥离方法。
- 决策：[[yt-decision-y-model]] 用于实验结果 ambiguous 时判断 pivot / persevere / kill。
- 域图：[[strategy-domain-digest]]、[[lean-startup-domain-digest]] 提供两个域的完整索引。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 验证顺序错误 | 先验证商业模式，后发现需求不存在 | 按 A→B→C→D 优先级排序，A 类商业成败假设优先验证 |
| 把战略口号当假设 | “我们要做行业第一”不是可证伪假设 | 把口号改写成“如果……那么……”形式的预测句，并设定不通过标准 |
| 实验设计过度粗糙 | 用一个 landing page 验证需要深度访谈才能回答的问题 | 按 FALSE 成本光谱选择最省钱的“够好”工具 |
| 通过标准太软 | “用户很感兴趣”替代“用户付费” | 每个实验必须同时定义定量或强定性的通过/不通过信号 |

## 适用边界

- **适合**：战略方向已初步形成，但关键假设不确定性高的业务；需要把“战略讨论”转化为“验证计划”的团队。
- **不适合**：高度不确定性赛道（如全新品类）中所有假设都无法低成本验证；强政策依赖赛道中关键假设只能依赖政策解读而非实验 [conf=0.80, source=60_feedback/audit/cross-domain-bridge-design-specs.md §2.7]。

---

*老顽童 · 2026-06-23 · 跨域融合计划（策略 A）P0 桥接卡*
