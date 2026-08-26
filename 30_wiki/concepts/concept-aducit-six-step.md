---
id: concept-aducit-six-step
title: ADUCIT 六步数据飞轮：预判→识别→收集→处理→使用→反馈（+治理贯穿）
type: concept
status: draft
confidence: 0.9
trust_level: high
domain:
- yihang
- kdo
author: 老顽童
reviewed_by: 待审
created_at: '2026-08-26'
updated_at: '2026-08-26'
source_person: Truman（一堂）；KDO 本土化演绎见关联
source_context: 官方版英文全称锚 plan_20260531_data-curator-v1.3.md:81（一堂数据飞轮 6+1）；KDO 本土演绎锚 art_20260602_three_deep_questions.md:91
source_refs:
- 30_wiki/decisions/plan_20260531_data-curator-v1.3.md:81
- 40_outputs/content/articles/art_20260602_three_deep_questions.md:91
aliases:
- ADUCIT
- 数据飞轮六步
- 一堂数据飞轮
- 6+1管线框架
discoverable_by:
- ADUCIT
- 数据飞轮
- 数据管线
- 预判识别收集处理使用反馈
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[framework-kdo-modeling-methodology]]'
- '[[concept-kdo-component-library]]'
tags:
- audience:general
- scene:reference
- skill-level:intermediate
- ADUCIT
- 数据飞轮
- 数据治理
- 双三角
- 概念
---

# ADUCIT 六步数据飞轮

> 本卡属于 `concept-yihang-dual-triangle-core` 双三角体系的**「数据」顶点展开方法**——AI 三角（场景/数据/基本功）中数据顶点的操作化框架；数据顶点四阶进化的第四阶=飞轮闭环（本框架即飞轮的管线形态）。

## 一句话

ADUCIT = **A**nticipate（预判）→ **D**etect（识别）→ **U**nearth（收集）→ **C**lean（处理）→ **I**mplement（使用）→ **T**rack（反馈），外加 **G**overnance（治理）贯穿全程——一堂数据飞轮 6+1 管线框架：从「预判价值」开始，以「闭环飞轮」结束。

## 官方版全称（锚 plan_20260531_data-curator-v1.3.md:81，逐字母对账）

| 字母 | 英文 | 中文 | 定义 |
|:--|:--|:--|:--|
| A | **Anticipate** | 预判 | 以终为始——先想清楚数据未来怎么用，从「预判价值」开始（而非从「有什么卡」开始） |
| D | **Detect** | 识别 | 发现隐藏的高价值数据（扫描/翻看素材找线索） |
| U | **Unearth** | 收集 | 把值得的数据挖掘出来（升仓决策的素材基础） |
| C | **Clean** | 处理 | 清洗加工为可用资产 |
| I | **Implement** | 使用 | 投入真实场景使用 |
| T | **Track** | 反馈 | 使用→反馈→回到预判，闭环飞轮 |
| +1 | **Governance** | 治理 | 合规/安全/隐私/反污染，贯穿全程非独立环节 |

> ⚠️ 考证警示（#539）：小昭曾断言「ADUCIT 英文全称全库零命中」并用 VLM 推断补全（6 错 4）——实际官方版一直在 `plan_20260531_data-curator-v1.3.md:81`。**推断版本（U/C/I/T 错误版）不得引用**，已进复盘当反面教材。先查库再断言「库里没有」（域知识检索铁律）。

## 关键辨析：线性框架 vs 循环依赖（KDO 本土演绎）

ADUCIT 官方是线性顺序，但 KDO 实践发现 **D 和 U 存在鸡生蛋循环**：不翻看素材不知道值不值得（U），不判断值不值得不知道翻看哪些（D）。KDO 解法（art_20260602）：D 和 U **同时启动**——冷启动手动选 5-10 个高价值素材先入仓，之后靠 C 加工过程中的发现自动驱动下一轮（D→U→C→加工中发现新线索→回到 D），稳态后无需全量扫描。

> 注意分层：「U=升仓决策」是 **KDO 本土演绎**（art 文档语境），官方定义 U=收集（Unearth）。引用时区分官方版与本土版。

## 与 KDO 管线的对应

KDO 知识工厂本身就是 ADUCIT 活体：A=任务单诊断预判（王语嫣）→ D=素材扫描/探针 → U=inbox→10_raw 升仓 → C=老顽童产卡精加工 → I=kdo query/Agent 消费 → T=60_feedback 复盘回流 → 治理=rules-core/写审分离/pre-submit 门禁贯穿。

## 与其他知识的关联

- `concept-yihang-dual-triangle-core`：本卡是双三角 AI 三角「数据」顶点的展开方法（权威版 AI 三角=场景/数据/基本功）
- `framework-kdo-modeling-methodology`：KDO 建模管线与 ADUCIT 的映射
- `concept-kdo-component-library`：治理层（G）在 KDO 的组件化实现

## 源债登记（停车场）

itingnao 7685126（原始口述全文）未拉取——按 #539 边界登记为源债，拉到后补时间戳进本卡。
