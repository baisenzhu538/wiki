---
id: framework-yitang-research-quality-gate
title: 调研质量自检框架：六维门禁——判断调研是否"足够好"
type: framework
status: reviewed
confidence: 0.92
trust_level: high
domain:
- src_unknown
source_refs:
- 30_wiki/domains/yitang-research-domain-digest.md
- 30_wiki/frameworks/framework-yitang-six-layer-cross-validation.md
- 00_inbox/调研专题/一堂-调研武器库培训-口述.txt
- 90_control/scripts/kcard-quality-gate.py
created_at: '2026-06-21'
updated_at: '2026-06-29'
author: 黄药师
reviewed_by: 欧阳锋
related:
- '[[framework-yitang-18-strategy-cards]]'
- '[[framework-yitang-channel-exploration-4step]]'
- '[[framework-yitang-channel-industrialization]]'
- '[[framework-kdo-self-attack]]'
- '[[framework-ouyangfeng-review-methodology]]'
- framework-yitang-high-level-plan
- framework-yitang-oscar-research
diagnostic_signals:
- framework_lens: 六维门禁——逐项自检
  follow_up_question: 六维中哪一维最薄弱？薄弱项回补后再提交
- framework_lens: 对照六维找缺口
  follow_up_question: 驳回理由对应六维中的哪一维？
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---

# 调研质量自检框架：六维门禁

> 调研做完 ≠ 调研做完了。六维门禁是提交前的最后一道自检——每个维度答不上来就不能交。

## 六维门禁

### 门禁 1：目标清晰度（O — Objective）

| 自检问题 | 不合格信号 |
|:--|:--|
| 调研目标能用一句话说清吗？ | "了解一下这个行业" |
| 目标对应哪个具体决策？ | 说不清调研结果用来干什么 |
| 假设是什么？要验证什么？ | 没有假设，只是"收集信息" |

> 引用：`framework-yitang-high-level-plan` — OSC：锁定目标是第一步

### 门禁 2：范围完整度（S — Scope）

| 自检问题 | 不合格信号 |
|:--|:--|
| 时间范围明确了？（近3年/近5年？） | "最近的"——没有具体日期 |
| 地域范围明确了？（全国/某省/某城市？） | 笼统说"中国市场"但没分区域 |
| 竞品/对标范围明确了？（≥3家？） | 只看了1-2家就下结论 |
| 是否声明了"不在本次调研范围内"的内容？ | 没说边界，用户以为全覆盖了 |

> 引用：`framework-yitang-high-level-plan` — 缩小范围

### 门禁 3：信源可靠度（L — List + Source）

| 自检问题 | 不合格信号 |
|:--|:--|
| 关键数字的来源层级？（L1官方/L2权威/L3多源?） | 数字来自一篇自媒体 |
| 核心结论≥2个独立来源？ | 单源结论未标注 ⚠️ |
| 信源时效？ | AI/融资领域引用超过30天的来源 |
| 有没有标注"口述待独立核实"？ | 讲师口述数字当事实用 |

> 引用：`framework-yitang-six-layer-cross-validation` — 六层验证

### 门禁 4：工具覆盖率（A — Acquire）

| 自检问题 | 不合格信号 |
|:--|:--|
| 用了几个武器？（标准≥5，深度尽调≥10） | 全程只用 WebSearch |
| 有没有尝试爬虫/OSINT/数据库/专家访谈？ | 只用了一种信息获取方式 |
| 穷尽了公开渠道吗？ | 没查过招股书/监管文件/行业报告 |

> 引用：`framework-yitang-research-weapon-system` — 武器库覆盖率

### 门禁 5：对立面检验（R — Reason + Counter）

| 自检问题 | 不合格信号 |
|:--|:--|
| 结论的反面可能性被检验过吗？ | 报告只有正面论证 |
| "如果这个结论是错的，最可能的原因是什么？"答得上来吗？ | 没有 Pre-Mortem |
| 有没有找过否定性证据？ | 只找了支持假设的证据 |

> 引用：`framework-yitang-nine-layer-deep-dig` — 自我纠错 + SATs Devil's Advocacy

### 门禁 6：可操作性（Output — Action）

| 自检问题 | 不合格信号 |
|:--|:--|
| 报告能否直接支持一个决策？ | "需要更多研究"结尾 |
| 读者今晚能执行的具体动作是什么？ | 结论是"这个行业很有前景" |
| 有没有标注置信度（高/中/低）？ | 所有结论平铺，没有优先级 |

> 引用：`framework-yitang-high-level-execution` — AR：获取情报→正确归因

## 自检流程

```
调研完成
  ↓
逐维自检（6个问题答不上→回补）
  ↓
全部通过 → 标注置信度等级
  ↓
提交报告
```

## 不合格处理

| 不合格维度 | 回补动作 | 时间 |
|:--|:--|:--|
| 目标不清 | 回 OSC：重新定义目标和假设 | 30 分钟 |
| 范围不全 | 补声明："本次不包括XX" | 10 分钟 |
| 信源薄弱 | 追加 2 个独立来源交叉验证 | 1-2 小时 |
| 武器不足 | 追加 1-2 个信息获取渠道 | 1-4 小时 |
| 无对立检验 | 做一次 Pre-Mortem | 30 分钟 |
| 不可操作 | 加一个"立即行动"建议 | 15 分钟 |

## 与 KDO 质量门禁的关系

| 层 | 工具 | 检查什么 |
|:--|:--|:--|
| 格式层 | `kdo lint` / `kcard-quality-gate.py` | frontmatter / source_refs / dangling links |
| 内容层 | **本卡（六维门禁）** | 目标 / 范围 / 信源 / 武器 / 对立 / 可操作 |
| 理解层 | 欧阳锋审查 | 三信号：反例具体性 / 案例区分度 / 跨域连接 |

## 多门禁失败时的修复优先级

如果多个门禁同时不通过，按以下顺序修复——前序修复后，后续可能自动改善：

| 优先级 | 门禁 | 先修它的原因 |
|:--|:--|:--|
| **1** | 门禁 1：目标清晰度 | 目标不清 → 范围必不全 → 信源必发散 → 不可操作。是所有下游问题的根 |
| **2** | 门禁 3：信源可靠度 | 信源薄弱 → 结论不可信，修好后再看其他门禁是否仍失败 |
| **3** | 门禁 5：对立面检验 | 如果对立检验发现了致命漏洞 → 其他门禁的修复方向都可能改变 |
| 4 | 门禁 2/4/6 | 前三项通过后，这四项通常是"补全"而非"重做" |

## 轻量模式

对小型调研（< 2 小时投入），使用轻量门禁——只查三维：

| 门禁 | 检查 |
|:--|:--|
| 目标 | 一句话能说清？ |
| 信源 | 关键数字有来源？ |
| 对立 | 想过反面可能性？ |

三维全通过 → 标注"轻量门禁通过"。完整六维留给 ≥4 小时的深度调研。

## 外部参考

本框架设计参考了以下外部质量体系：
- src_unknown
- src_unknown
- src_unknown

---

*黄药师 · 2026-06-21 · 调研域架构层整合 · 自攻击迭代 v1.1*
