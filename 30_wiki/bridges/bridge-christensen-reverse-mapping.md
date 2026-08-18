---
id: bridge-christensen-reverse-mapping
title: Christensen反向映射：60+卡引用→原著依据回填清单
type: bridge
status: reviewed
domain: strategy
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-08-02
confidence: 0.9
trust_level: medium
aliases:
- src_20260802_创新者的窘境_秦鹏拆书
- diag_20260802_创新者的窘境_秦鹏拆书
- 创新者的窘境
- Christensen
source_refs:
- 10_raw/sources/src_20260802_创新者的窘境_秦鹏拆书.txt
- 60_feedback/diagnosis/diag_20260802_创新者的窘境_秦鹏拆书.md
related:
- framework-christensen-disruptive-innovation
- framework-christensen-value-network
- concept-christensen-rpv-model
- yt-panproduct-execution-roi-analysis
- yt-panproduct-execution-low-cost-mvp
- tool-马易-风口痛点识别法
created_at: 2026-08-02
updated_at: 2026-08-02
quality_labels: cited
tags:
- method:反向映射
- scene:跨域溯源
- audience:方法
- content-format:bridge
- source-person:秦鹏
discoverable_by:
- Christensen引用都有哪些
- 破坏性创新在wiki里怎么用的
- 创新者的窘境哪张卡引了
diagnostic_signals:
- signal: 60+ 文件引用Christensen但0张原著卡
  severity: critical
  implication: 所有引用都是二手引用，缺原著框架作为理论锚点
- signal: Christensen多为Critique节的攻击武器
  severity: moderate
  implication: 正反两面都引用，但正面理论从未被系统拆解
---

> **定位**：属于 `framework-christensen-disruptive-innovation` 的 Wave 0 前置桥接卡，连接 wiki 存量 60+ Christensen 引用到即将产出的原著框架卡。

# Christensen反向映射：60+卡引用→原著依据回填清单

## 核心发现

**wiki 存量 190 个文件引用 Christensen/破坏性创新，但 0 张原著卡。** 这是典型的"高引用低覆盖"——每个人都引用 Christensen 作为 Critque 节的"外部攻击武器"，但原书三大框架从未被系统拆解为独立知识卡。

### 引用类型分布

| 引用方式 | 典型位置 | 数量估计 | 风险 |
|:--|:--|:--|:--|
| **Critique 节·外部攻击** | `## Critique` section | 30+ | 正反两面都在引用，但攻击者本身未被理解——失去批判基础 |
| **正文·理论引用** | `## 原始表述` / `## Evidence` | 20+ | 引用 Christensen 概念但无原著出处锚定——可信度下降 |
| **案例/方法类比** | `## 操作方法` / `## Synthesis` | 10+ | 类比可能失准——未区分 Christensen 原意 vs 中文二次传播 |
| **tools 卡·前置知识** | `related` / 前置概念列表 | 部分 | 链接到 Christensen 但指向不存在的卡——死链隐患 |

### 三个发现

1. **Christensen 被当成"万能攻击武器"**。大部分引用集中在 Critque 节——用"颠覆性创新"来挑战 ROI 分析、MVP 验证、规模前倾等方法的适用边界。但攻击者自身是什么，从未被建立过。

2. **引用深度极不均**。`yt-panproduct-execution-roi-analysis.md` 深度引用（"ROI分析是颠覆性创新最精准的杀手"），而多数工具卡只是旁注式一笔带过。

3. **"创新者的窘境"作为标签失准**。190 个文件中，大部分匹配的是"破坏性创新/颠覆性创新"这些术语，真正的 Christensen 理论引用集中在大约 60 个文件。

---

## 四列映射表：引用文件 → 引用概念 → 原著位置 → 回填判定

### 深度引用文件（已在 Critique/正文中大量使用 Christensen 理论）

| 引用文件 | 引用的 Christensen 概念 | 原著中位置 | 是否需要回填依据 |
|:--|:--|:--|:--|
| `yt-panproduct-execution-roi-analysis.md` | "ROI分析是颠覆性创新最精准的杀手"——破坏性创新初期无法做ROI | 《窘境》第7章：创新者的任务（商业案例讨论）| 🟡 当前引用精准，但缺原著页码/章节锚点。建议补 `（Christensen 1997, Ch.7）` |
| `yt-panproduct-execution-low-cost-mvp.md` | "颠覆性创新无法被现有客户验证" | 《窘境》第8章：如何评价市场新技术的市场策略（主流客户的需求会误导破坏性创新）| 🟡 同上，建议补原著锚点 |
| `tool-马易-风口痛点识别法.md` | "追逐现有风口是延续性创新思维" | 《窘境》第2章：价值网络决定了企业看到的"机会"范围 | 🟢 概念使用正确，需确认是否标注了来源 |
| `tool-遵循规模前倾原则设计组织架构.md` | Christensen 批评规模前倾假设 | 《窘境》第5章：给予破坏性技术的正确范围（小市场不能解决大公司的增长需求）| 🟢 引用合理 |
| `tool-水水-保持系统冗余.md` | 冗余在经济下行期首先被削减——Christensen关于资源分配 | 《窘境》第9章：性能提供，市场选择与破坏性技术的起点 | 🔴 引用点不够精确——Christensen 讲的是资源分配流程（RPV中的P），不是"冗余"概念。需要确认引用准确性 |

### 中等引用文件（Critique 节引用，或一笔带过）

| 引用文件 | 引用的 Christensen 概念 | 原著中位置 | 是否需要回填依据 |
|:--|:--|:--|:--|
| `yt-tool-unit-model-selection.md` | 破坏性创新对单元模型的影响 | 《窘境》第2章+第7章 | 🟡 概念引用正确但深度不足 |
| `yt-tool-strategy-workshop.md` | 价值网络对战略选择的影响 | 《窘境》第2章 | 🟡 建议补充跨卡链接 |
| `yt-product-kernel-mvp-design.md` | 产品内核与颠覆性创新的关系（一堂特有概念嫁接） | 《窘境》第6章+一堂 product kernel 框架 | 🟡 这是一堂特有框架对 Christensen 的映射，需在原著卡中阐明这种映射关系 |
| `yt-demand-quantitative-estimation.md` | 颠覆性创新的市场规模不可预测 | 《窘境》第7章 | 🟢 引用合理 |
| `yt-demand-level-assessment.md` | 需求层次与价值网络的关系 | 《窘境》第2章 | 🟢 引用合理 |

### Wave 1-5 卡片将覆盖的 Christensen 原文框架

| 原著框架 | 原著章节 | 对应 Wave 1-2 卡片 | 回填到哪些引用文件 |
|:--|:--|:--|:--|
| **破坏性创新理论** | 第1-4章（延续vs破坏、S曲线、五大原则）| `framework-christensen-disruptive-innovation` | 所有引用"破坏性创新/颠覆性创新"的 Critque 节 → 把该卡加入 reviewed_by 攻方来源 |
| **价值网络理论** | 第2章（价值网络定义、企业生命周期）| `framework-christensen-value-network` | `yt-tool-strategy-workshop.md`、`yt-demand-level-assessment.md`、`five-step-barrier` 相关卡 |
| **RPV模型** | 第9章（资源-流程-价值观）| `concept-christensen-rpv-model` | RPV 相关引用文件（组织设计/战略决策） |
| **Jobs-to-be-Done** | 后续著作《创新者的解答》第3章 | `concept-christensen-jtbd-link`（Wave 5）| `case-demand-milkshake-jtbd.md` 等 JTBD 引用文件 |

---

## 回填优先级

### 🔴 P0：必须回填（深度引用但缺原著锚点）
1. `yt-panproduct-execution-roi-analysis.md` — 补 Christensen 1997 Ch.7 页码/段落锚点
2. `yt-panproduct-execution-low-cost-mvp.md` — 补 Christensen 1997 Ch.8 锚点

### 🟡 P1：建议回填（引用合理但可增强）
3. `tool-水水-保持系统冗余.md` — 确认"冗余"概念是否准确对应 Christensen 原文
4. `yt-product-kernel-mvp-design.md` — 阐明"一堂产品内核→Christensen破坏性创新"的映射关系

### 🟢 P2：自动关联（Wave 1 卡片完成后 related 自动覆盖）
> 其余 60+ 引用文件在 Wave 1 三张框架卡入库后，通过 `related` 字段建立双向链接。不需要手工逐一回填。

---

## 与 Wave 1-5 卡片的关系

本 bridge 卡是 Wave 0 的前置产出，为后续卡片提供：
1. **related 锚点清单**：Wave 1 框架卡需要反向链接到这些深度引用文件
2. **术语统一基线**：所有卡片统一使用"破坏性创新"（对齐 Christensen 原文），标注"颠覆创新"为同义
3. **引用质量诊断**：识别出 190 个引用中最需要回填原著的 Top 10 文件

---

## 方法

本映射通过以下步骤完成：
1. 正则扫描 `30_wiki/` 全部 `.md` 文件，搜索 `Christensen|christensen|创新者的窘境|破坏性创新|颠覆性创新|disruptive.*innovation` → 命中 190 文件
2. 手工审查前 100 个文件中 Christensen 引用的深度和准确性
3. 结合诊断报告 `diag_20260802_创新者的窘境_秦鹏拆书.md` 中六层交叉验证的结论
4. 对照 Christensen 1997 原书目录结构，给出原著位置映射

---

## Critique

### 外部挑战
- **Jill Lepore（2014,《纽约客》）**：Christensen 的"颠覆性创新"理论建立在精选的历史案例上。硬盘行业的叙事有选择性——有些被归类为"延续创新"的公司其实也做了破坏性的事。本映射表可能延续了这种选择性叙事。
- **King & Baatartogtokh（2015, MIT Sloan）**：对 77 个 Christensen 自称的"破坏性创新"案例进行系统审核，仅 9% 完全符合他的四项标准。这意味着 wiki 中引用的"破坏性创新"概念可能比实际适用范围更广。

### 内部局限
- **190 个命中但仅审查前 100**：后 90 个文件未逐一手工审查引用质量。可能存在遗漏的关键引用。
- **缺少原著页码级别的精确锚点**：当前映射到"章"级别（如 Ch.7），未精确到节/段。对严格溯源来说精度不够。
- **"破坏性创新"与中文语境**：Christensen 原文 `disruptive innovation` 在中文翻译中同时被译为"破坏性创新"和"颠覆性创新"。wiki 中的引用可能混杂两者而不自知。

---

## Action Triggers

1. **立即可做**：将本卡中的 P0 回填项（2 个文件）发给老顽童，在 Wave 1 之前或并行完成
2. **Wave 1 完成后**：`framework-christensen-disruptive-innovation` 入库后，在 `yt-panproduct-execution-roi-analysis.md` 的 Critique 节中将"Christensen"引用替换为 `[[framework-christensen-disruptive-innovation]]` 精确卡链
3. **定期维护**：每次有新卡引用 Christensen 时，检查是否已在四列映射表中登记
