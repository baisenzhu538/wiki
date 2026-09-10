---
id: diag_20260910_wangyuyan-feature-deep-card-gold-standard
title: 建议书：以 F040 金标准深卡为样板，重挖 AI 基本功与 AI 数据两节课
type: proposal
audience: 王语嫣
status: pending_orchestration
author: 小昭
created_at: 2026-09-10
updated_at: '2026-09-10'
assignee: wangyuyan
reviewer: 欧阳锋
decision_source: 老朱 2026-09-10 直接派单
domain:
  - ai-basic
  - ai-collaboration
related:
  - "[[concept-feature-f040-state-machine]]"
  - "[[ai-basic-domain-digest]]"
  - "[[framework-truman-feature-layered-system]]"
  - "[[concept-yihang-ai-feature-thinking]]"
  - "[[diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig]]"
---

# 建议书：以 F040 金标准深卡为样板，重挖 AI 基本功与 AI 数据两节课

> **给小昭的定位备忘**：我是外部协同，不直接派活。本建议书给王语嫣，由她判断是否编排任务、拉起哪个 agent。

---

## 一、触发：老板的一个问题暴露了入口层缺口

2026-09-10 老板问：「AI 基本功课程讲到 feature，提到状态机，它的详细解释有没有生成知识卡片？」

核查结论：**没有**。Feature 周期表 100 个 Feature 在库里只有**数据登记**（feature-periodic-table-v1.0.json）+ **3 处一笔带过**（layered-system/thinking-core/dual-track 三张卡各列了个名字），**没有任何一张对单个 Feature 做完整展开**。这与 2026-08-25 盲测第 1 问「feature 有哪些怎么分类」未命中（#526）是**同一个病**——入口层缺路标 + 高价值 Feature 无深卡。

## 二、已完成：F040 状态机金标准深卡（样板）

应老板要求，已按金标准补出首张 Feature 深卡：

- **卡片**：`30_wiki/concepts/concept-feature-f040-state-machine.md`
- **溯源**：口述上 L926-1030 完整推理链（问题→试错①里程碑→试错②工作流节点→转机→定义→实例→效果），每行引文逐字命中原文
- **门禁**：`kdo pre-submit` **PASS**（QUOTE_VERBATIM / ALIASES / TAGS / INDEX 全部清零；仅剩 1 条 CONCEPT_CROSSCHECK 提示制，不拦截）
- **索引**：已跑 `kdo index --incremental`（total 4277）

卡片含 13 段：定义 / 口述证据链 / 原理 / 操作法 / 口述 3 场景 / **应用场景（A 库内实证 + B 推演探索）** / 边界 / 反模式 / 落地模板 / Critique / Synthesis / Action Triggers / 溯源索引。

**应老板要求，重点做了应用场景探索**：除口述 3 场景、库内 7 处实证外，按状态机本质特征（多步骤+先后依赖+AI 易跳步+状态可编号+转移有条件）**推演了 7 个新场景**（问诊分诊/制造品控/销售对话/审批合规/客服工单/招聘面试/结对编程），每个给出状态编号示例+转移条件+AI 角色，标注 hypothesis 未经实证。这个「推演探索」方法可复制到所有 Feature。

## 三、金标准门禁避坑清单（这次踩坑换来的，后续 agent 直接用）

| # | 坑 | 正确做法 |
|:--|:--|:--|
| 1 | 引文里加 `**粗体**` | QUOTE_VERBATIM 拿带 ** 的文本去源文件找，必 FAIL——引文必须纯文本逐字 |
| 2 | 行文强调用引号 | 校验器把**所有带引号的**都当逐字引文查——行文强调改用粗体，引号只给源文件逐字引用 |
| 3 | 对其他卡片/JSON 的引用加引号 | 它们不在 source_refs 里，会判伪逐字——对卡片引用一律转述不带引号，引号只给 source_refs 里的原始素材 |
| 4 | 多行拼成一句加引号 | 伪逐字——引文必须是源文件**单一行**的完整子串 |
| 5 | 转写噪音直接删 | 保留原文并标注【转写存疑】（#250 诚实性原则） |
| 6 | aliases 不含源文件名 | ALIASES 警告「card will be undiscoverable」——aliases 补完整源文件名 |
| 7 | tags 全是维度前缀词 | TAGS 要求 5-8 个**普通内容词**（`method:` 等维度前缀不计数） |
| 8 | 编辑后没跑索引 | INDEX error「卡片比检索索引新」——最后一次编辑后必须 `kdo index --incremental` |

## 四、建议编排的任务

### 任务 A：AI 基本功课——Feature 深卡系列化

- **素材**：`00_inbox/AI基本功/`（Feature思维解析上 1374 行 + 下 2054 行 + Live258 优秀作业 3024 行 + 周期表 OCR）；数据源 `10_raw/sources/feature-periodic-table-v1.0.json`
- **现状**：ai-basic 域 53 张卡，但 Feature 深卡仅 F040 一张（其余为 framework/case/dk/tool）
- **建议**：周期表 verified=true 的 20 个 Feature（#255 报告：True 20 / False 80）优先，按 F040 模板逐个做深卡。F038 CoT、F031 最终意图、F026 Few-shot、F030 RAG 等高价值 Feature 排前
- **产出标准**：每卡过 `kdo pre-submit` 全绿（WARNING 清零，CONCEPT_CROSSCHECK 提示制除外），附避坑清单（上文三）

### 任务 B：AI 数据课——深度挖掘

- **素材**：`00_inbox/AI-study/AI数据/`（口述 01/02/03 + 闲聊篇共 ~4600 行 + AI数据理解第一课表格.md）
- **现状**：已有 `concept-data-three-constants-three-shifts`、`ai数据理解第一课`（疑为 OCR 转录卡，trust 待核）
- **建议**：先诊断现有卡对 4600 行素材的**覆盖度**（哪些主题已卡片化、哪些是空白），再按金标准补空白。数据课应有自己的核心概念/Feature 清单，参照 Feature 深卡结构做深卡

### 建议的 agent 分工

| 角色 | 任务 |
|:--|:--|
| 王语嫣 | 诊断两节课素材覆盖度，排出深卡优先级清单 |
| 老顽童 | 按 F040 模板批量生产 Feature 深卡（任务 A/B 执行） |
| 欧阳锋 | 终审，把避坑清单纳入验收口径 |

## 五、需要王语嫣先判断的三个问题

1. **深卡 vs 数据源的边界**：Feature 周期表原是「数据源 JSON + feature_menu.py 工具」形态，从未规划每 Feature 一卡。现在做深卡系列，是否会与「周期表=数据源」的设计冲突？建议：深卡只针对**高价值 Feature**（verified=true 优先），不全做，周期表仍是唯一数据源，深卡是其上层的「精读注释」。
2. **AI 数据课的卡片归属**：数据课素材在 `00_inbox/AI-study/AI数据/`，但现有相关卡散落在 cases/concepts，归 ai-basic 域还是单列？
3. **推演探索场景的验证**：F040 卡第六节 B 的 7 个推演场景（问诊分诊/制造品控等）标注 hypothesis——是否需要单独立项实证，还是暂存为探索清单？

---

> **小昭附言**：F040 卡是样板，不是终点。老板要的是「金标准的追求」——这张卡的 13 段结构、避坑清单、推演探索方法，都是为了让后续 Feature 深卡能**批量复制而不掉质量**。请王语嫣裁定是否编排，需要我补充素材盘点明细随时说。
