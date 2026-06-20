---
title: "九层深挖法"
type: framework
status: draft
confidence: 0.85
domain:
  - research-methodology
author: wangyuyan
reviewed_by: pending
source_refs:
  - "case-smart-medicine-cabinet-failure-patterns-library"
  - "smart-medicine-cabinet-financial-model"
  - "smart-medicine-cabinet-national-policy-redlines"
created_at: "2026-06-16"
updated_at: "2026-06-20"
diagnostic_signals:
  - "迭代深挖"
  - "自我纠错"
  - "逻辑缺口驱动"
  - "多层补齐"
related:
  - "[[framework-yitang-oscar-research-5step]]"
  - "[[recursive-deepen]]"
  - "[[yt-five-step-method-complete]]"
---

# 九层深挖法

王语嫣从智能药柜案例分析中总结的商业分析迭代法。核心洞见：高质量分析不是一次性输出，而是不断发现逻辑缺口、调用知识补缺口、发现新矛盾、再补缺的自我纠错过程。

## 与 OSCAR 的分工

- **OSCAR**：调研获取信息（前端——怎么找信息）
- **九层深挖**：分析信息（后端——怎么把信息挖透）

两者组合：OSCAR拿信息→九层深挖分析→决策。

## 九层结构

| 层 | 目标 | 核心问题 |
|:--:|:-----|:---------|
| L1 | 业务公式/单元模型 | 收入=什么×什么？成本结构？回本周期？ |
| L2 | 假设审计 | 每个数字是事实、估算还是愿望？哪个最敏感？ |
| L3 | 政策/合规边界 | 受哪些政策红线约束？政策在收紧还是放松？ |
| L4 | 失败模式库 | 真实失败案例的共因是什么？预警信号是什么？ |
| L5 | 隐性成本与替代方案 | 显性成本之外还有什么？用户有什么替代方案？ |
| L6 | 执行能力 | 这个模式对团队的要求现实吗？普通人执行会怎样？ |
| L7 | 市场情绪/骗局 | 有没有"躺赚""半年回本"等危险信号？ |
| L8 | 边界案例与反例 | 什么情况下前面的结论会失效？ |
| L9 | 决策框架 | go/no-go结论 + 最大风险 + 最小验证路径 + 重评触发信号 |

## 停止条件

满足任一即停止：
- 各层逻辑自洽，无矛盾
- 新一层增量信息 < 10%
- 知识库缺口明确无法补齐
- 已产出可执行决策框架（L9完成）

### [Critique]

- **Boundary**：九层深挖适用于"信息不充分但可以通过知识库+推理补齐"的场景。对于完全陌生的新领域（知识库无任何覆盖），深挖效果取决于推理能力上限
- **Reliability**：High——药柜案例实战验证，9层迭代产出了可用决策框架

### [Synthesis]

- 对接 OSCAR：调研→深挖→决策的完整链路
- 对接递归深挖法(`recursive-deepen`)：九层是商业专用，递归是通用版
- 对接一堂五步法：九层深挖覆盖了五步法中"需求验证→商业模式判断→壁垒识别"的分析层

---

*作者：王语嫣 · 来源：智能药柜案例九轮迭代分析实战*
