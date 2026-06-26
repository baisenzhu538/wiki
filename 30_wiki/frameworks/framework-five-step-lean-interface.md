---

id: framework-five-step-lean-interface
title: 五步法与精益验证的接口
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
- yitang
- lean-startup
- strategy
source_refs:
- 00_inbox/精益创业/transcript_低成本验证认知篇.md
- 00_inbox/精益创业/truman-精益创业-false模型_ocr_text.md
- 60_feedback/audit/cross-domain-bridge-design-specs.md
related:
  - '[[framework-ai-accelerated-strategy-cycle]]'
  - '[[framework-strategy-lean-validation]]'
  - '[[dk-yitang-business-model-risk-over-product-risk]]'
  - '[[framework-lean-pivot-decision]]'
  - '[[framework-demand-lean-bridge]]'
- "[[yt-five-step-method]]"
- "[[yt-entrepreneur-five-step-method]]"
- "[[framework-lean-false-model]]"
- "[[concept-一堂-kernel-validation]]"
- "[[tool-泛产品落地-低成本测试MVP]]"
- "[[framework-strategy-business-design]]"
- "[[framework-wanghuan-harness-seven-stages]]"
- "[[five-step-domain-digest]]"
- "[[lean-startup-domain-digest]]"
---

# 五步法与精益验证的接口

> 把一堂五步法（需求→产品内核→商业模式→增长→壁垒）的每一步，映射到对应的精益验证工具和通过标准。

## 触发问题

- “我知道要做五步法，但每一步怎么验证？”
- “产品内核画布填完了，怎么知道填得对不对？”
- “商业模式设计了很多版本，先测哪一个？”

## 五步法每一步 → 待验证假设 → 精益工具 → 通过标准

| 五步法阶段 | 核心问题 | 待验证假设 | 精益工具 | 通过标准 |
|:---|:---|:---|:---|:---|
| 需求 | 用户要解决什么任务？ | 这个需求真实且重要 | 客户访谈、假营销、搜索词验证 | 访谈中用户主动描述痛苦 |
| 产品内核 | 最小可交付价值是什么？ | 产品能交付承诺价值 | 假产品、人工 VIP、MVP | 早期用户愿意复购/推荐 |
| 商业模式 | 怎么赚钱？ | 单元模型成立 | 预售、最小版本试运营 | LTV/CAC 可算且为正 |
| 增长 | 怎么放大？ | 渠道可扩展 | 灰度测试、组合测试 | CAC 可控，边际成本不激增 |
| 壁垒 | 怎么守住？ | 优势可持续 | 竞品动态监测、时间窗口验证 | 6–12 个月护城河可见 |

> 工具映射参考 [[framework-lean-false-model]] 的 F/A/L/S/E 成本光谱 [conf=0.85, source=60_feedback/audit/cross-domain-bridge-design-specs.md §3.3]。

## 与相邻卡的关系

- 上游框架：[[yt-five-step-method]]（总纲）、[[yt-entrepreneur-five-step-method]]（创业者实操版）给出五步法的完整逻辑；本卡只回答“每一步用什么精益工具验证”。
- 内核验证：[[concept-一堂-kernel-validation]] 与 [[tool-泛产品落地-低成本测试MVP]] 聚焦第二步“产品内核”的验证细节。
- 战略接口：[[framework-strategy-business-design]] 在战略层定义“为谁创造什么价值”，五步法在业务层验证这些选择。
- AI 构建接口：[[framework-wanghuan-harness-seven-stages]] 把五步法思想落地到 AI 原生复杂产品构建流程中，强调生成者与验收者分离。
- 域图：[[five-step-domain-digest]]、[[lean-startup-domain-digest]] 提供两个域的完整索引。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 跳步验证 | 需求没验证就做 MVP | 在需求阶段拿到“用户主动描述痛苦”信号前，不得进入产品内核验证 |
| 工具错配 | 用 landing page 测产品内核（应该用人工 VIP） | 对照 FALSE 光谱：测需求用 F，测内核用 A/L，测模式用 E |
| 通过标准不一致 | 不同步骤用不同口径判断“成功” | 统一使用“通过/不通过”二元信号，避免模棱两可 |
| 把验证当终点 | 验证通过后直接全量投入，缺少“螺旋上升” | 每轮验证后更新假设地图，再决定下一轮是继续、转向还是终止 |

## 适用边界

- **适合**：已经了解五步法框架，但需要把每一步落地为具体验证动作的团队。
- **不适合**：强监管行业中某些步骤的验证受合规限制，需用调研或监管沟通替代部分精益实验 [conf=0.80, source=60_feedback/audit/cross-domain-bridge-design-specs.md §3.6]；成熟行业的微创新可能不需要完整五步法验证。

---

*老顽童 · 2026-06-23 · 跨域融合计划（策略 A）P0 桥接卡*
