---
id: framework-truman-feature-thinking-core
title: 「框架：Feature思维——提升AI解题水平的最小实践单位」
type: framework
status: draft
confidence: 0.95
trust_level: high
domain:
  - ai-basic
  - methodology
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/AI学习-Feature思维解析（上）-口述.txt
  - 00_inbox/AI基本功/AI学习-Feature思维解析（下）-口述.txt
  - 10_raw/sources/feature-periodic-table-v0.8.json
source_person: Truman
source_context: Truman《AI学习·Feature思维解析》2026-08-07直播（上L462-590+1084-1218，下L816-858）
reviewed_by: 待审
aliases:
  - Feature思维
  - Feature四要素
  - T型F型分界
  - 五大学派
discoverable_by:
  - Feature思维
  - Feature四要素
  - T型F型
  - 五大学派
  - AI基本功
related:
  - framework-truman-feature-layered-system
  - concept-truman-feature-four-scenarios
  - concept-truman-feature-six-stages
  - tool-Truman-Feature特性层训练法
  - framework-一堂-关键假设
  - concept-一堂-基本功-刻意练习四要素
  - agent-spec-复盘教练
  - yt-decision-y-model
  - case-live258-zhihu-content-acquisition
  - case-live258-livestream-prompt-v1-v5
  - case-live258-fact-spread-18-bridges
  - case-live258-europe-cold-email
  - tool-feature-review-five-step
tags:
  - method:feature-thinking
  - method:ai-basic
  - method:decomposition
  - scene:ai-learning
  - audience:general
  - content-format:framework
  - source-person:Truman
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - principle
  - cited
diagnostic_signals:
  - signal: "学了很多AI工具但还是不会用AI解决实际问题"
    lens: 可能困在工具思维(T型)——以工具为单位学习，工具一变就归零
    follow_up: 切换到Feature思维——把能力建在Feature层而非工具层
  - signal: "团队讨论AI方案时各说各话"
    lens: 缺Feature作为共同语言——产品/技术/运营对同一个Feature有不同理解
    follow_up: 用四要素定义统一术语——每个Feature满足"AI范围+解题水平+实践单位+最小颗粒度"
---

> 本卡属于AI基本功域方法论根卡——Feature思维的定义、四要素、T-F分界、五大学派。Feature周期表见 `[[framework-truman-feature-layered-system]]`。

# Feature思维：提升AI解题水平的最小实践单位

> 一句话：Feature思维 = 把AI能力拆成最小实践原子，借工具之假、修能力之真。T型思维依赖工具→工具一变就归零；F型思维建在Feature层→工具变了Feature还在。

---

## 四要素定义

Feature = **提升AI解题水平的最小实践单位**（口述上L534-590）：

| 要素 | 含义 | 反例 |
|:---|:---|:---|
| **AI范围** | 必须是AI项目——非AI场景不适用 | "如何做好PPT排版"——不是AI范围 |
| **解题水平** | 能提升解决问题的水平——不是"知道"是"能做" | "知道了Prompt Engineering的概念"——没提升解题水平 |
| **实践单位** | 可执行的动作——不是理论、不是概念 | "AI能力体系"——不是可执行的动作 |
| **最小颗粒度** | 越小越好——越小越可迁移、越可测试、越容易练习 | "提示词工程"——太粗，应拆成"最终意图/负面限制/输出要求"等 |

> "Feature越小越好——因为越小测试越快，成本越低，越容易验证。"（口述上L614-620）

---

## T型 vs F型思维分界

| | T型思维（工具思维） | F型思维（Feature思维） |
|:---|:---|:---|
| 学习单位 | 工具（ChatGPT/Midjourney/Cursor） | Feature（最终意图/温度/状态机） |
| 迁移性 | 工具变了要重学 | Feature跨工具稳定 |
| 组合性 | 一大坨切换 | 原子Feature自由组合 |
| 长期价值 | 工具过时=能力归零 | Feature积累=复利增长 |
| 应对变化 | "新工具又出来了，焦虑" | "新工具=换个壳，Feature还是那些" |

> "工具思维以工具为单位学习，Feature思维关注工具背后的基本特性——这是从新手野路子到进阶体系态的思维分界线。"（口述上L462-510）

---

## 五大学派蛋黄图

AI学习五大流派（口述上L1084-1218）：

```
原理派 ← 工程派 ← Feature派 → 工具派 → 教程派/模板派
(最稳定/最难)                          (最实用/最容易)
              ↑  
        Feature派：取中间——平衡稳定+实用
```

| 流派 | 特点 | 问题 |
|:---|:---|:---|
| 原理派 | 学底层算法/注意力机制/Transformer | 最稳定但最难，普通人学不动 |
| 工程派 | 学上下文工程/Harness工程/评测工程 | 专业但门槛高 |
| **Feature派** | **拆成最小实践原子，跨工具稳定** | **本次课程核心——取左右之长** |
| 工具派 | 学具体工具（Cursor/Midjourney） | 实用但工具一变就归零 |
| 教程派/模板派 | 照教程一步步做 | 最易上手但不稳定、不能迁移 |

Feature派的独特价值：**既像左边一样稳定（Feature不随工具改变），又像右边一样实用（每个Feature是可执行的动作）**。

---

## Critique

### 内部局限
- 四要素的"最小"是方向性指引而非精确标准——什么算"最小"有主观判断空间
- Feature派虽然"平衡"，但学习门槛仍高于工具派——新人需要先走过工具派阶段才能理解Feature的价值

### 外部攻击者
**工具派**："我就想快速出活，搞什么Feature拆解？直接用工具不香吗？"

**回应**：短期直接用工具效率最高——但当你换了工具/场景/团队，你从零开始。Feature思维不是否定工具——是让你"借工具之假，修能力之真"。

**教程/模板派**："网上有现成的模板和教程，照着做不就行了？"

**回应**：教程能让你跑通一次——但遇到稍微不同的场景，模板就失灵了。Feature思维让你理解"为什么这个模板有效"——理解后的迁移能力，才是长期的价值。

## When NOT to Use
- 一次性任务（不值得建Feature库）
- 工具极其稳定且无需迁移（如某个行业内唯一标准工具）

## 预测属性：Feature的"化学元素周期表"留白

Truman（口述下L1812-1814）：

> "Feature还有预测属性——我把未来的一部分趋势也放到feature里面了。所以市场上出现这些东西，在我来讲相对来说是趋势内的东西。"

**Feature的预测属性 = 周期表留白设计**：周期表V0.8有8个格刻意留白（门捷列夫空位类比）——不是"不知道为什么填"，是"我们知道这里应该有东西，等实践验证"。预测属性的价值：不是预测"下一个工具是什么"，是预测"这个位置应该有一个什么样的Feature"。
