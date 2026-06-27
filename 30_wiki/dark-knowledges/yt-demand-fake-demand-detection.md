---
domain:
- src_unknown
id: yt-demand-fake-demand-detection
title: 伪需求识别：7个危险信号
type: dk
dark_knowledge_type: insight
status: enriched
confidence: 0.78
trust_level: medium
source_context: 一堂五步法需求分析口述——"最悲惨的结果是需求错了"
source_refs:
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-20'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
related:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- signal: src_unknown
  framework_lens: 伪需求信号1——兴趣≠需求
  follow_up_question: 用户说'不需要'时，是现在不需要，还是永远不需要？有没有替代方案？
- signal: src_unknown
  framework_lens: 伪需求信号2——口头需求≠付费意愿
  follow_up_question: 如果明天这个产品上线，用户会立刻付费吗？如果不会，阻碍是什么？
- signal: src_unknown
  framework_lens: 伪需求信号3——自我投射≠用户真实需求
  follow_up_question: 创始人之外，至少访谈了10个真实用户吗？有没有和创始人假设相反的证据？
- signal: src_unknown
  framework_lens: 伪需求信号4——竞品驱动≠需求验证
  follow_up_question: 竞品的这个功能服务的是他们的核心用户，还是边缘功能？你的用户有同样的需求吗？
- signal: src_unknown
  framework_lens: 伪需求信号5——技术能力≠用户需求
  follow_up_question: 这个功能解决的是用户的什么问题？不用这个功能，用户现在怎么解决？
- signal: src_unknown
  framework_lens: 伪需求信号6——报告数据≠真实需求
  follow_up_question: 报告中的'需求'是用户自述的，还是行为数据验证的？
- signal: src_unknown
  framework_lens: 伪需求信号7——满意度≠使用意愿
  follow_up_question: 用户说满意，但为什么不用？是场景不匹配，还是替代方案更好？
---
# 伪需求识别：7个危险信号

> 一堂五步法：超过30%甚至50%的项目失败，根源是伪需求。识别伪需求比发现真需求更重要。

## 原始表述

伪需求不是"没有需求"，而是"用户说需要，但实际不会付费或使用"。超过30%甚至50%的项目失败，根源是伪需求。识别伪需求比发现真需求更重要。

## 使用场景

- **新产品需求验证**：在产品开发前识别伪需求，避免投入浪费
- **用户访谈设计**：设计访谈问题时识别伪需求信号
- **创业方向选择**：验证创业方向是否是真需求
- **投资尽调**：评估项目需求真实性
- **产品功能优先级**：区分真需求和伪需求，合理分配资源

## 操作方法

1. **识别7个危险信号**：
   - 兴趣≠需求："挺好的，但我不需要"
   - 口头≠付费："想要"但不愿付费
   - 自我投射："我就是用户，我懂"
   - 竞品驱动："竞品做了，我们也得做"
   - 技术驱动："我们能做，所以做了"
   - 报告迷信："报告显示市场很大"
   - 满意度陷阱："满意度高但不用"
2. **验证方法**：
   - 问"如果现在没有这个，你会怎么解决？"
   - 问"愿意付多少钱？"测试付费意愿
   - 访谈10个外部用户，寻找反例
   - 对比行为数据（活跃度、留存）和满意度
3. **从伪需求到真需求**：
   - 追问"为什么需要更快？"→"我想更快到达目的地"
   - 追问"现在的CRM哪里不好？"→"我想减少销售跟进的时间"
   - 追问"为什么现在不健身？"→"我想找到低成本的健身方式"
4. **定期做"需求减法测试"**：去掉一个功能，看用户是否在意

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 新产品需求验证 | 成熟产品优化（已有数据反馈） |
| 用户访谈设计 | 技术可行性评估 |
| 创业方向选择 | 运营策略制定 |
| 投资尽调 | 品牌传播 |

## 为什么值钱

1. **避免项目失败**：超过30%甚至50%的项目失败根源是伪需求
2. **节省资源**：在投入前识别伪需求，避免大规模浪费
3. **找到真需求**：伪需求背后往往藏着真需求，追问能挖掘真实动机
4. **决策依据**：用可验证的标准替代主观感觉，提升决策质量

## 与其他知识的关联

- [[yt-five-step-method]]——一堂五步法，需求分析的系统化框架
- [[dk-tool-as-phased-validator]]——分阶段校验器，需求验证方法
- [[dk-mckinsey-hypothesis-driven-pitfalls]]——假设驱动陷阱，需求假设验证
- [[dk-wanghuan-spec-trap]]——王欢 Spec 陷阱，验收标准设计
- [[dk-ai-judgment-human-responsibility]]——人做判断 AI 做生产，需求判断的人类责任

---

## 失败模式

| 失败模式 | 症状 | 修复方法 |
|:---|:---|:---|
| **忽视沉默用户** | 只关注说"想要"的用户，忽视说"不需要"的用户 | 统计"不需要"的比例，分析原因 |
| **过早规模化** | 伪需求未识别，就大规模投入 | 先小范围验证，确认真需求后再扩展 |
| **数据自欺欺人** | 选择性地展示支持自己的数据 | 主动寻找反例，证明自己是错的 |
| **团队共识偏差** | 团队内部达成共识，但未经外部验证 | 至少访谈10个外部用户 |
| **伪需求堆叠** | 在一个伪需求上堆叠更多功能 | 定期做"需求减法测试" |
| **忽视时间维度** | 假设需求是静态的 | 需求会变化，定期重新验证 |

## 适用边界

| 适用场景 | 不适用场景 |
|:---|:---|
| 新产品需求验证 | 成熟产品优化（已有数据反馈） |
| 用户访谈设计 | 技术可行性评估 |
| 创业方向选择 | 运营策略制定 |
| 投资尽调 | 品牌传播 |

## 行动触发器

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 关联卡片

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源与验证

- src_unknown
- src_unknown
- src_unknown
