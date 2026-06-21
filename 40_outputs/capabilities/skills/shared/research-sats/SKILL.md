---
name: research-sats
description: CIA SATs结构化分析技术——Key Assumptions Check/Devils Advocacy/Red Team/Indicators
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [SATs, 魔鬼代言人, Red Team, 关键假设, 结构化分析]
    related_skills: [research]
---

# SATs 结构化分析技术

CIA 情报分析工具箱——不是获取更多信息，而是更严谨地分析已有信息。

## Constraints

<hard_limits>
- SATs 是分析工具，不是信息获取工具。先确保有足够信息再调用
- Devil's Advocacy 必须真正攻击结论，不能敷衍
- Red Team 必须从竞对视角出发，不能带入自己的假设
</hard_limits>

## 技术决策树

| 需求 | 技术 | 耗时 |
|:--|:--|:--|
| 找出隐藏假设 | Key Assumptions Check | 15 分钟 |
| 攻击自己的结论 | Devil's Advocacy | 30 分钟 |
| 模拟竞对最优策略 | Red Team Analysis | 1 小时 |
| 设置"该重新评估了"的信号 | Indicators/Signposts | 20 分钟 |

## 四项核心技术

### 1. Key Assumptions Check（关键假设检查）

**何时用**：得出任何结论后，强制检查。

**步骤**：
1. 列出支撑结论的所有假设（通常 5-10 条）
2. 逐条问："如果这条假设不成立，结论会怎么变？"
3. 对每条假设标注：🔵 充分证据 / 🟡 部分证据 / 🔴 几乎无证据
4. 🔴 假设 → 必须补证据或修正结论

### 2. Devil's Advocacy（魔鬼代言人）

**何时用**：结论看起来"太对了"的时候。

**步骤**：
1. 假设结论是错的
2. 构建最强反驳论证——用事实，不用观点
3. 检查反驳是否击中了结论的核心假设
4. 如果反驳成立 → 修正结论

**执行模板**：
```
我现在的结论是：[一句话]
如果这个结论是错的，最可能是因为：
1. [假设A不成立，因为...]
2. [假设B不成立，因为...]
3. [数据C有误，因为...]
```

### 3. Red Team Analysis（红队分析）

**何时用**：需要预测竞对动作时。

**步骤**：
1. 扮演竞对的决策者
2. 从竞对的资源/约束/动机出发
3. 设计竞对的最优策略
4. 对比自己的假设——是否低估了竞对？

### 4. Indicators/Signposts（指标/信号）

**何时用**：需要持续监控、而不是一次性判断。

**步骤**：
1. 列出触发"需要重新评估"的可观测信号
2. 每个信号有明确的阈值（不是"市场变了"）
3. 设置检查频率

**示例**：
| 信号 | 阈值 | 检查频率 |
|:--|:--|:--|
| 竞对降价超过 20% | 连续两个季度 | 季度 |
| 新进入者拿到 B 轮 | 3 家以上 | 月 |
| 监管政策征求意见 | 任何相关 | 周 |

## 相关 wiki 卡片
- `framework-structured-analytic-techniques`
- `tool-key-assumptions-check`
- `tool-devils-advocacy`
- `tool-red-team-analysis`
- `tool-indicators-signposts`
- `research-cross-validation` — 交叉验证（互补）
