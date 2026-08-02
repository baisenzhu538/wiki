---
id: framework-structured-analytic-techniques
title: 结构化分析技术（SATs）总览
type: framework
domain:
tags:
source_person: Richards J. Heuer Jr. + Randolph H. Pherson + Truman（一堂）
source_context: SATs 文献综述 + 一堂九层深挖/交叉验证的 SATs 同构映射
aliases:
  - Richards J. Heuer Jr. + Randolph H. Pherson + Truman（一堂）
  - 三个新盲区
  - 分析技术
  - 外部知识探索
  - 构化分析技术
  - 构化思维方法
  - 析技术
  - 策分析技术
  - 结构化分析技术SATs总览
source_refs:
related:
discoverable_by:
  - "结构化分析技术"
  - "SATs"
  - "决策分析技术"
  - "结构化思维方法"
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-06-28'
quality_labels:
created_at: '2026-06-28'
updated_at: '2026-06-28'
confidence: 0.78
trust_level: medium
---
# 结构化分析技术（SATs）总览

## 原始表述

CIA 有一套完整的 **Structured Analytic Techniques (SATs)** 工具包，远不止 ACH（竞争性假设分析）。

一堂的"交叉验证"只是直觉版，SATs 是系统版。

> **ACH 的核心原则与直觉相反**：不是找支持你的证据，而是找反驳你的证据。"被最少证据反驳的假设是最稳健的"——这与一堂"找到信息验证假设"的思维方向**相反**。

---

## 使用场景

### 适合使用 SATs 的情境

- 面临复杂决策，多种假设都成立，无法判断哪个最稳健
- 团队已经被固有认知锁定，需要系统性打破（ACH / Devil's Advocacy）
- 需要模拟竞对或对手视角（Red Team Analysis）
- 需要定义"什么信号出现时，我们的假设需要重新评估"（Indicators）

### 不适合的情境

- 决策简单明确，只有一种合理解释（用不着结构化技术）
- 时间极度压缩（ACH 需要 2-4 小时完整执行）
- 团队成员不理解"假设"概念（需要先做认知偏差培训）

---

## SATs 八类技术分类

| 类别 | 作用 | 代表技术 | 一堂对应物 |
|:---|:---|:---|:---|
| **诊断类** | 系统性发现隐藏假设 | Key Assumptions Check | ❌ 无——一堂有"关键假设"概念但无结构化检验流程 |
| **反向类** | 主动挑战主流结论 | Devil's Advocacy / Red Team Analysis | ❌ 无 |
| **想象力类** | 突破固有认知框架 | What If? Analysis / Alternative Futures | ⚠️ 第16掌"场景推演"有部分覆盖 |
| **指标类** | 定义可观测的验证信号 | Indicators & Signposts | ❌ 无 |
| **假设检验类** | 矩阵化评估多假设 | Analysis of Competing Hypotheses (ACH) | ⚠️ 九层深挖法有同构映射 |
| **因果类** | 区分相关与因果 | Causal Layering / Impact Persistence | ⚠️ 单元模型域有部分覆盖 |
| **冲突管理类** | 整合多人/多源分歧 | Starbursting / Structured Debate | ❌ 无 |
| **决策类** | 把分析结果转化为决策 | Decision Matrix / War Gaming | ⚠️ 第17掌"归一总结"有部分覆盖 |

---

## 操作方法：如何选择合适的技术

### 决策树

```
你的核心问题是什么？
│
├─ "我们是不是漏掉了什么隐藏假设？"
│   → Key Assumptions Check（诊断类）
│
├─ "团队已经被某个结论锁定，需要挑战"
│   ├─ 需要一个人专门挑战 → Devil's Advocacy（反向类）
│   └─ 需要模拟对手视角 → Red Team Analysis（反向类）
│
├─ "有多个假设都成立，无法判断哪个最稳健"
│   → ACH（假设检验类）
│
├─ "假设成立的前提条件是什么？什么信号能告诉我们假设失效了？"
│   → Indicators & Signposts（指标类）
│
└─ "如果某个关键因素突然变化，会发生什么连锁反应？"
    → What If? Analysis（想象力类）
```

### 与一堂方法论的映射关系

| SATs 技术 | 一堂对应物 | 映射关系 | 缺口 |
|:---|:---|:---|:---|
| **ACH** | 九层深挖法 | ✅ 同构映射——都是"多假设矩阵化评估" | 九层深挖没有"找反驳证据"的系统性步骤 |
| **交叉验证** | 第15掌"交叉验证" | ✅ 同构映射——都是"多源验证" | 一堂交叉验证是直觉版，SATs 是系统版 |
| **Key Assumptions Check** | 第1-3掌"关键假设" | ⚠️ 概念同源，但无结构化检验流程 | ❌ 完全缺失——需要补工具卡 |
| **Devil's Advocacy** | 第11掌"自攻击" | ⚠️ 概念相似，但 SATs 有标准操作步骤 | ❌ 完全缺失——需要补工具卡 |
| **Red Team Analysis** | 第3掌"竞对跟踪" | ❌ 不对——"跟踪"是观察，"Red Team"是模拟决策 | ❌ 完全缺失 |

---

## 为什么值钱

1. **打破认知锁定**：SATs 是系统性"强制自己考虑相反证据"的方法，不是靠"保持开放心态"这种虚的口号。
2. **可教学**：每个 SATs 技术都有标准操作步骤，可以教给团队，不是依赖某个人"思考能力强"。
3. **与一堂方法论同构**：ACH = 九层深挖，交叉验证 = 多源验证，不需要重造轮子，只需升级到 SATs 级别。

---

## 与其他知识的关联

- **[[framework-yitang-nine-layer-deep-dig]]**

← ACH（竞争性假设分析）和九层深挖法是同构映射，本卡是 SATs 总览，九层深挖是具体实现

- **[[tool-key-assumptions-check]]**

→ 诊断类 SATs 的工具化实现——系统性发现隐藏假设

- **[[tool-devils-advocacy]]**

→ 反向类 SATs 的工具化实现——魔鬼代言人操作步骤

- **[[tool-red-team-analysis]]**

→ 反向类 SATs 的工具化实现——竞对视角模拟

- **[[tool-indicators-signposts]]**

→ 指标类 SATs 的工具化实现——定义假设失效的信号

---

## 适用边界

### SATs 生效的前提

- 决策者愿意让"挑战主流结论"成为正式流程（否则 Devil's Advocacy 会被视为"不合作"）
- 有时间执行完整流程（ACH 需要 2-4 小时，不是 10 分钟快速决策工具）
- 团队理解"假设"和"证据"的区别（否则 ACH 会变成"找支持证据"的变形版）

### 常见误用

- **"ACH 是打分表"** → 错误。ACH 的核心是"找反驳证据"，不是给假设打分。
- **"SATs  replacing 直觉"** → 错误。SATs 是结构化直觉，不是替代直觉。
- **"一次用一个以上 SATs"** → 不推荐。一次只用一个，完整执行，再考虑是否需要补充。

---

## 失败模式

| 失败模式 | 症状 | 根因 | 修正方法 |
|:---|:---|:---|:---|
| **"打分表症"** | ACH 变成了"给假设打分的表格"，没有"找反驳证据"的步骤 | 只学了一半 ACH——学会了矩阵格式，没学会核心原则 | 重读 Heuer 原著：ACH 的核心是"被最少证据反驳的假设最稳健" |
| **"形式化症"** | SATs 变成了"流程仪式"，但没有改变实际决策 | 为了用 SATs 而用 SATs，不是为了改变决策 | 每个 SATs 执行前，先明确"这个技术要改变什么决策" |
| **"过度分析症"** | 用 5 个 SATs 分析一个简单决策 | 没有根据问题复杂度选择技术 | 用决策树选择——简单问题不用 SATs |

---

## Action Checklist

- [ ] 盘点当前最容易被固有认知锁定的 1-2 个决策场景
- [ ] 选择 1 个 SATs 技术（优先 Key Assumptions Check 或 ACH），在下一个重要决策中完整执行
- [ ] 执行后复盘：SATs 有没有改变决策？如果没有，为什么？
- [ ] 把 SATs 加入团队决策流程（例如：所有 >50 万的投资决策，必须用 ACH 评估）

---

## 来源与验证

| 断言 | 来源 | 可信度 |
|:---|:---|:---|
| SATs 八类技术分类 | Heuer & Pherson《Structured Analytic Techniques for Intelligence Analysis》| A（权威原著） |
| ACH 核心原则"找反驳证据" | 同上 | A |
| 一堂九层深挖与 ACH 同构映射 | diag_20260621_外部知识探索_三个新盲区.md | A（诊断报告，已交叉验证） |
| 一堂缺少 Key Assumptions Check / Devil's Advocacy 工具卡 | 同上 + 现有卡片库搜索确认 | A（可验证） |

---

## 口述数据标注

> 来源：Heuer & Pherson SATs 文献 + 一堂诊断报告交叉验证。SATs 八类技术分类有原著支撑，可信度 A。一堂与 SATs 的映射关系基于诊断报告，已通过现有卡片库搜索交叉验证。
>
> ⚠️ "ACH 需要 2-4 小时完整执行"——此为 CIA 培训标准时间，实际耗时取决于假设数量和证据复杂度，可根据实际情况调整。
