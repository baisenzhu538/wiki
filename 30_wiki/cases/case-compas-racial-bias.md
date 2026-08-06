---
id: case-compas-racial-bias
title: COMPAS 再犯算法种族偏见
type: case
status: enriched
created_at: 2026-06-28
updated_at: '2026-06-29'
author: 老顽童
reviewed_by: 待审
confidence: 0.8
trust_level: medium
language: zh-CN
domain:
  - ai-collaboration
  - critical-thinking
  - business-judgment
source_refs:
- 00_inbox/拆书会第208期：《AI 2041：预见未来二十年》逐字稿（完整版）.md
- 60_feedback/diagnosis/diag_20260624_wangyuyan_ai2041-annotation.md
- 60_feedback/decisions/dec_20260624_wangyuyan-ai2041-card-plan.md
aliases:
  - COMPAS再犯算法种族偏见
  - 再犯算法种族偏见
  - 算法种族偏见
discoverable_by:
  - COMPAS 再犯算法种族偏见
  - 再犯算法种族偏见
related:
- '[[ai-short-drama-ice-fire-dissection-compass]]'
- '[[ai-short-drama-ice-fire-scripting-compass]]'
- '[[pending_unknown]]'
- tool-ai-cross-reading-method
- tool-ai-critical-reading-three-layers
tags:
- audience:general
- scene:reference
- skill-level:intermediate
---
# COMPAS 再犯算法种族偏见

> **Burn line**：一份被包装成“科学中立”的再犯风险评分，把美国刑事司法历史中的种族差异重新编码为数字，让黑人被告在“没犯罪却被判高风险”和“犯罪却被判低风险”两个错误方向上遭受不对称伤害。
>
> **来源**：王欢《AI 2041》拆书会第四幕；ProPublica 2016 调查；Northpointe/Equivant 官方回应与后续学术讨论。

---

## 核心洞察

COMPAS 不是“故意写了一条歧视代码”，而是**用历史逮捕/再犯数据训练出的模型把系统性的种族差异自动化了**。它在“校准”意义下可以声称公平（同分不同种族的真实再犯率相近），但在“错误率平等”意义下显著不公平——黑人被告被误标为高风险的概率几乎是白人的两倍 [conf=0.90, source=ProPublica 2016]。

这一案例最尖锐的启示是：**“公平”没有一个唯一的技术定义**。Northpointe 选择优化预测 parity（校准），必然接受不同群体间错误率的不平等；ProPublica 选择关注错误率平等，则必然质疑现有数据本身携带的历史偏见 [conf=0.85, source=Northpointe rebuttal / 后续公平性学术研究]。因此，算法公平不仅是工程问题，更是**谁有权定义公平的权力问题** [conf=0.70, source=王欢原创]。

---

## 来源人与来源语境

| 字段 | 内容 |
|:---|:---|
| source_person | 王欢（AI 协作域作者、拆书家） |
| source_context | 王欢在《AI 2041》拆书会第四幕以 COMPAS 作为“AI 外部性”的现实对照，用来说明算法如何在“无歧视意图”的情况下产生“歧视性效果”。本卡在王欢逐字稿基础上补充了 ProPublica 原文与 Northpointe 辩护要点，避免仅复制王欢说法。 |

---

## 事迹/背景

### 事件是什么

COMPAS（Correctional Offender Management Profiling for Alternative Sanctions）是由美国公司 Northpointe（现 Equivant）开发的再犯风险评估软件。它通过一份包含 137 个问题的问卷及犯罪记录，为被告打出 1–10 分的风险分数，供法官、假释官和缓刑官在量刑、保释、假释决策中参考 [conf=0.85, source=ProPublica 2016]。

### 涉及主体

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 时间线

| 时间 | 事件 |
|:---|:---|
| 1998 年左右 | Northpointe 开始开发 COMPAS 风险评估工具 [conf=0.80, source=学术/行业二手资料] |
| 2013 | Wisconsin 州法官在 State v. Loomis 案中引用 COMPAS 分数判处被告 Eric Loomis 六年监禁 [conf=0.85, source=公开判例报道] |
| 2016-05-23 | ProPublica 发布《Machine Bias》与配套方法学文章，指出 COMPAS 对黑人被告存在系统性偏见 [conf=0.90, source=ProPublica 2016] |
| 2016-07 | Northpointe 发布官方回应，质疑 ProPublica 统计方法，强调 COMPAS 满足校准与预测 parity [conf=0.85, source=Northpointe rebuttal] |
| 2016-07 | ProPublica 再次回应，指出 Northpointe 的辩护在技术上成立，但回避了错误率不平等的问题 [conf=0.85, source=ProPublica follow-up] |
| 2018 年以后 | 学术界围绕“公平性不可能定理”展开大量讨论；多个司法管辖区限制或停用 COMPAS [conf=0.80, source=学术二手资料] |

---

## 关键数字

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 关键证据表

| 核心主张 | 证据 | 来源 | 可信度 |
|:---|:---|:---|:---:|
| COMPAS 对黑人被告的误标率显著更高 | 黑人未再犯者被标高风险 44.9%，白人仅 23.5%；黑人再犯者被标低风险 28.0%，白人 47.7% | ProPublica "Machine Bias" | [conf=0.90] |
| 控制犯罪史与再犯事实后，种族仍是评分显著预测因子 | 逻辑回归中 Black 系数在一般/暴力再犯模型均显著为正 | ProPublica methodology | [conf=0.90] |
| COMPAS 整体预测准确度有限 | ProPublica 估计 concordance 63.6%，Northpointe 自报 68% | ProPublica methodology | [conf=0.85] |
| Northpointe 以“校准”作为公平标准辩护 | 同分不同种族的真实再犯率相近；COMPAS 对黑白被告整体准确率相近 | Northpointe rebuttal | [conf=0.85] |
| 两种公平定义不可同时满足 | 当群体基础再犯率不同时，预测 parity 与错误率平等存在数学冲突 | Kleinberg et al. / Chouldechova 后续研究 | [conf=0.85] |
| 算法黑箱阻碍被告质证 | Northpointe 未公开具体计算逻辑，称系商业机密 | ProPublica 2016 | [conf=0.85] |

---

## 失败/成功原因

### 失败原因（为什么造成伤害）

1. **目标函数过窄**：COMPAS 优化的只是“预测再犯概率”，没有把“种族错误率平等”“被告可质证权”“量刑比例性”等社会价值纳入目标 [conf=0.70, source=王欢原创]。
2. **历史数据的结构性偏见**：再犯标签来自逮捕记录，而逮捕率本身受执法强度、社区警力、保释能力等因素影响，黑人社区被过度逮捕的历史被模型学习并固化 [conf=0.85, source=ProPublica 2016 / 学术讨论]。
3. **算法黑箱与权力不对等**：被告和公众无法审查模型逻辑，而法官往往把分数当作“科学”参考，削弱了正当程序 [conf=0.85, source=ProPublica 2016 / Wisconsin v. Loomis 讨论]。
4. **“中立”叙事掩护责任归属**：因为“没有程序员写歧视代码”，责任被分散到数据、模型、采购方、使用方之间，最终无人负责 [conf=0.70, source=王欢原创]。

### 成功原因（为什么问题被曝光）

1. **调查记者公开数据与方法**：ProPublica 不仅讲故事，还公布了数据集和分析代码，使结论可被复现和攻击 [conf=0.90, source=ProPublica 2016]。
2. **法律案例制造公共议程**：Wisconsin v. Loomis 等案件把算法评分引入宪法讨论，让抽象公平问题变成可诉讼的权利问题 [conf=0.85, source=公开判例报道]。
3. **学术共同体接力**：公平性机器学习研究迅速把 COMPAS 作为经典案例，提炼出公平性指标冲突、公平性不可能定理等通用框架 [conf=0.80, source=学术二手资料]。

---

## 失败模式

在借鉴或审计 COMPAS 式算法系统时，常见的踩坑方式与避免方法：

| 失败模式 | 表现 | 避免方法 |
|:---|:---|:---|
| **只看整体准确率** | 认为“模型整体 61% 准确率可接受”，忽视不同族群的错误率差异 | 强制拆分 false positive / false negative，并按受保护群体报告 |
| **把公平性外包给供应商** | 直接采用 Northpointe 定义的“校准公平”，不做独立审计 | 采购前明确本组织的公平标准，要求供应商提供分群错误率 |
| **混淆意图与效果** | 因代码里没有种族变量，就认为不存在歧视 | 检查 proxy 变量（邮编、教育、就业、社交关系）是否携带族群信息 |
| **把统计辩护当道德辩护** | 用“算法只是辅助法官”淡化评分对实际判决的影响 | 做影响评估：法官在多大程度上依赖分数？被告是否有质证机制？ |
| **只曝光不建设** | 批评算法偏见后没有给出替代流程 | 配套设计人工复核、申诉通道、模型下架触发条件 |

---

## 可迁移场景

COMPAS 的结构——“用历史数据训练 → 把社会差异编码为分数 → 以中立名义做出高影响决策”——在以下场景反复出现：

| 场景 | 分数/标签 | 潜在伤害 |
|:---|:---|:---|
| 招聘筛选 | “文化契合度”“离职风险”评分 | 对特定性别、族裔、年龄的系统性低估 |
| 信用与贷款 | 违约概率模型 | 对弱势群体的信贷可得性差异 |
| 保险定价 | 健康/驾驶风险评分 | 把社会经济不平等重新定价为“个人风险” |
| 医疗分诊 | 再入院风险、优先级评分 | 对少数族裔或低收入患者的服务不足 |
| 教育评估 | 学业风险预警 | 对边缘学生的标签化与自我实现预言 |

迁移判断标准：只要一个系统满足 **(1) 高影响决策 + (2) 用历史数据做预测 + (3) 声称客观中立 + (4) 受影响方缺乏质证权**，就应当引入 COMPAS 式审计 [conf=0.70, source=王欢原创]。

---

## 教训与预警信号

1. **预警信号一：把“没有歧视意图”当作“没有歧视效果”**。当团队只检查代码里是否写了种族变量，而不检查不同群体的错误率时，偏见可能已经通过 proxies（邮编、教育、就业史、社交关系）进入模型。
2. **预警信号二：用单一准确率指标掩盖分配性伤害**。整体 accuracy 61% 可以包装成“比随机好”，但它对黑人被告和白人被告的误伤方向截然相反。审计时必须拆分错误率。
3. **预警信号三：把“公平”交给供应商定义**。Northpointe 选择校准作为公平标准，是因为这对它的产品最有利。采购方和使用方必须自己定义受保护群体、可接受错误率差异、申诉渠道。
4. **预警信号四：黑箱模型进入高影响决策**。当被告无法知道分数怎么算、无法有效质证时，算法评分就构成了程序正义风险，即使它在统计上有一定预测力。

---

## 对立面/争议

| 维度 | ProPublica 立场 | Northpointe / 技术辩护立场 |
|:---|:---|:---|
| 公平标准 | 应关注错误率平等（equalized odds）：不同群体的假阳性率、假阴性率应接近 | 应关注预测 parity / 校准（calibration）：同分意味着同概率再犯，不论种族 |
| 核心数字 | 黑人被告被误标高风险的概率是白人的近两倍；暴力再犯评分上高 77.3% | 在同等分数下，黑白被告的真实再犯率几乎相同；整体预测准确度对两组一致 |
| 方法论批评 | 用回归控制犯罪史与再犯事实，隔离种族效应 | 批评 ProPublica 使用“不恰当的分类统计”，未考虑不同族群的基线再犯率差异 |
| 责任归属 | 算法系统及其使用者应对歧视性效果负责 | 模型只是工具，最终决策权在法官；模型已满足统计学公平标准 |
| 隐含前提 | 历史逮捕数据本身携带种族偏见，不能作为中立训练集 | 数据反映真实犯罪分布，模型在此基础上做最优预测 |
| 结论 | COMPAS 存在种族偏见，应被严格监管或停用 | COMPAS 满足公平性标准，问题出在公平定义的选择 |

这场争议的关键不在于“谁算错了”，而在于**哪一种公平定义应当被优先采纳**。当两个公平定义在数学上不可兼得时，选择本身就是一种价值判断和政治决策 [conf=0.85, source=Kleinberg et al. / Chouldechova 公平性不可能定理相关研究]。

---

## 与王欢框架的映射

| 王欢概念 | 在 COMPAS 案例中的体现 |
|:---|:---|
| 选择点探测器 | 法官/假释官面对的“是否采信算法评分”是一个具体选择点，影响被告刑期与人生 [conf=0.70, source=王欢原创] |
| 椅子决定视角 | Northpointe 的“校准公平”与其商业利益一致；ProPublica 的调查记者位置决定其关注错误率不平等 [conf=0.70, source=王欢原创] |
| 中立的暴政 | COMPAS 用数学分数包装“中立观察”，使种族差异变得难以被质疑 [conf=0.70, source=王欢原创] |
| 三层拆书法 | 还原：COMPAS 是一个再犯预测工具；审计：数据与方法存在族群差异；生长：公平定义的选择权应归属受影响者 [conf=0.70, source=王欢原创] |

---

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 延伸阅读与来源

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

*基于王欢《AI 2041》拆书会逐字稿整理，补充 ProPublica 与 Northpointe 双向来源。老顽童生产，待审。*
