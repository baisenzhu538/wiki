---

id: framework-lean-pivot-decision
title: 精益验证结果如何触发战略/产品 pivot
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
- decision
- yitang
source_refs:
- 60_feedback/audit/cross-domain-bridge-design-specs.md
- 00_inbox/精益创业/张磊教练《精益测试关键问题》AMA精华 副本.md
- 00_inbox/精益创业/张磊-精益方法论-AMA-口述-01.txt
- 00_inbox/精益创业/张磊-精益方法论-AMA-口述-02.txt
related:
  - [[framework-lean-abcd-model]]
  - [[yt-decision-y-model]]
  - [[strategy-domain-digest]]
  - [[lean-startup-domain-digest]]
  - [[yitang-domain-digest]]
---

# 精益验证结果如何触发战略/产品 pivot

> 当精益实验结果不理想时，用决策框架判断是 pivot（转型）、persevere（坚持）还是 kill（终止）。

## 触发问题

- src_unknown
- src_unknown
- src_unknown

## 端到端流程

```
精益实验输出（来自 lean-startup-domain）
  ├── 需求层信号    → 诊断：用户是否真实存在且愿意付费
  ├── 方案层信号    → 诊断：产品内核能否交付承诺价值
  ├── 商业模式信号  → 诊断：单元模型能否跑正
  ├── 增长层信号    → 诊断：渠道是否可扩展
  └── 壁垒层信号    → 诊断：优势是否可持续
           ↓
    用 ABCD 模型区分假设优先级与致命程度
           ↓
    用 Y 模型/决策框架评估 pivot / persevere / kill
           ↓
    输出战略动作 → 更新假设地图 → 进入下一轮验证
```

## 实验结果诊断矩阵

| 实验结果 | 对战略假设的影响 | 建议动作 | 决策检查清单 |
|:---|:---|:---|:---|
| 需求不存在 | 战略基础崩塌 | Pivot 或 Kill | 是否有其他用户群体？是否有相邻需求？ |
| 需求存在但方案弱 | 产品内核不成立 | Pivot 方案 | 能否用更 sharp 的解决方案？ |
| 需求/方案都成立但模式不成立 | 商业模式不成立 | Pivot 商业模式 | 定价、渠道、成本结构哪个错？ |
| 模式成立但增长不可扩展 | 增长假设失败 | Pivot 增长路径 | 是否有其他渠道？ |
| 都成立但壁垒弱 | 长期价值受威胁 | Persevere + 建壁垒 | 能否在窗口期内建立护城河？ |
| 都成立 | 方向正确 | Persevere + 放大 | 进入十倍速增长阶段 |

> 上表决策矩阵来自跨域桥接设计稿 [conf=0.85, source=60_feedback/audit/cross-domain-bridge-design-specs.md]。

## 从信号到动作的核心映射

| 输入信号 | 关键区分问题 | 决策输出 | 下一步验证 |
|:---|:---|:---|:---|
| 数据低于预期 | 是执行问题还是假设错误？ | 执行失败 → 优化后复测；假设错误 → Pivot | 用更小成本重跑同一实验 |
| 用户热情但不付费 | 需求真实但支付意愿弱？ | 商业模式 Pivot 或定价调整 | 测试不同价格/付费模式 |
| 单一群体反馈好 | 是普遍需求还是小众偏好？ | 小众 → Pivot 用户群体 | 扩大样本或切换细分人群 |
| 连续 3 次实验失败 | 假设链是否已无法修复？ | 是 → Kill；否 → 降级假设后重测 | 回到 ABCD 排序，重找前置假设 |

> "连续 3 次失败"是常见止损启发，非绝对标准；具体阈值需结合业务资金窗口与机会成本设定 [conf=0.75, source=00_inbox/精益创业/张磊-精益方法论-AMA-口述-02.txt]。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 把执行失败当方向错误 | 一次实验操作粗糙就宣布 pivot | 区分"实验设计问题"与"假设不成立"，必要时低成本复测 |
| 把方向错误当执行失败 | 多次失败仍坚持"再优化一下" | 用 [[framework-lean-abcd-model]] 重新评估假设致命程度，设置硬性 kill 条件 |
| 沉没成本绑架决策 | "已经投了 X 万，不能停" | 用 [[yt-decision-y-model]] 的机会成本视角，把过去投入从未来收益计算中剔除 [conf=0.80, source=00_inbox/精益创业/张磊-精益方法论-AMA-口述-02.txt] |
| 忽略情绪与 ego | 创始人将 pivot 视为个人失败 | 建立"投资人视角"——假设今天刚认识这家公司，是否还会投资 [conf=0.80, source=00_inbox/精益创业/张磊-精益方法论-AMA-口述-02.txt] |

## 与相邻卡的关系

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 适用边界

- src_unknown
- src_unknown

---

*老顽童 · 2026-06-23 · 跨域融合计划（策略 A）P1 桥接卡*
