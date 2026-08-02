---
id: dk-modeling-checklist-formatting-rules
title: 清单体写不好，模型就建不好：换行、分层、优先级、完备
type: dk
dark_knowledge_type: workflow
status: reviewed
domain:
- yitang
- ai-saas
source_person: Truman
source_context: 一堂建模能力培训，2026-06-12
aliases:
  - 优先级
  - 分层
  - 换行
  - 模型就建不好
  - 清单体写不好
  - 清单体写不好，模型就建不好：换行、分层、优先级、完备
source_refs:
- pending_archive:src_20260614_8269ccdb-一堂-建模能力培训-truman-口述
- pending_archive:src_20260614_8269ccdb-一堂-建模能力培训-truman-口述
confidence: 0.8
trust_level: medium
related:
- '[[yitang-domain-digest]]'
- '[[tool-分层标注重点信息]]'
- '[[tool-月白-AIGC海报信息优先级排序法]]'
- '[[tool-使用优先级快筛卡锁定核心矛盾]]'
- '[[tool-Truman-AI能力分层学习路径]]'
- '[[tool-决策深度-L1优先级定性]]'
- '[[tool-深度分层学习]]'
- '[[tool-推行分层标准化策略]]'
- '[[tool-马易-隐私安全分层解决]]'
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-06-15'
updated_at: 2026-06-28
diagnostic_signals:
- signal: src_unknown
  framework_lens: 清单体格式四规则至少一条失效
  follow_up_question: 逐条审计：是否一行一点？超过7条是否分层？决策点是否分级？建模目标是否完备？
- signal: src_unknown
  framework_lens: 信息揉在一起，行动项与责任人未分行
  follow_up_question: 按"换行即分点+决策必分级"重写，把结论、行动项、负责人、截止时间分行列出
- signal: src_unknown
  framework_lens: AI容易生成"有形式无分级/无完备性"的伪清单
  follow_up_question: 人工检查是否有优先级分级、是否MECE、是否每个条目对应一个可执行动作
- signal: src_unknown
  framework_lens: 清单缺少分层或分级标准未共识
  follow_up_question: 为清单增加二级分类，并对S/A/B/C或P0/P1/P2的定义达成书面共识# 清单体写不好，模型就建不好：换行、分层、优先级、完备
- 建模能力培训
---

## 原始表述

> 我能接受的是但凡你遇到了换行，但凡换行就有分解……超过七八个就分层……优先级，遇到决策就分级……建模要完备。

## 深度洞察

Truman 把清单体写作拆成四条硬规则：换行即分点、超过七八个就分层、遇到决策就分级、建模要完备。这些不是排版洁癖，而是**模型能否被大脑处理、能否指导决策**的关键。清单体是流程建模（60 分）阶段最基础也最高频的输出，基础不牢，后面的抽象建模和本质建模都会站不住。

更深层：这四条规则对应建模段位 L1→L5 的跃迁——

- src_unknown
- src_unknown
- src_unknown
- src_unknown

AI 时代这条规则反而更值钱：AI 能生成"看起来像清单"的输出，但**不会自动判断它是否满足这四条规则**。人必须做最后的格式审计和逻辑完备性判断。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **换行即分点**
   每一行只承载一个信息点。如果一个长句里包含两个动作，拆成两行。

2. **超过七八个就分层**
   7 条以下可以平铺；7 条以上必须找二级分类，否则人脑处理不了。

3. **遇到决策就分级**
   凡是涉及取舍、资源分配、优先级，必须标出 S/A/B/C 或 P0/P1/P2。

4. **建模要完备**
   如果是为了后续建模，最好做到 MECE（不重不漏）；如果是为了工作流里程碑，最好体现出逻辑链。

## 清单体格式错误前后对比

以下四组对比展示同一段信息在"格式错误"与"格式正确"两种状态下的差异。

### 对比 1：换行即分点

**❌ Before（一大坨不换行）**

> 周会结束后要整理会议纪要、确认下一步行动、把任务分配给相关同学、并在周五前跟进一次进度。

**✅ After（一行一点）**

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 对比 2：超过七八个就分层

**❌ Before（12 条平铺）**

1. 确认直播主题
2. 确认主讲人
3. 准备开场 PPT
4. 准备案例 PPT
5. 准备结尾转化页
6. 测试推流
7. 测试麦克风
8. 测试灯光
9. 准备互动问题
10. 准备福利资料
11. 发布预告海报
12. 直播前 30 分钟再次检查

**✅ After（分层：内容准备 / 技术测试 / 运营预热 / 临场检查）**

**一、内容准备**
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**二、技术测试**
- src_unknown
- src_unknown
- src_unknown

**三、运营预热**
- src_unknown
- src_unknown

**四、临场检查**
- src_unknown

### 对比 3：遇到决策就分级

**❌ Before（无优先级）**

本周待办：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**✅ After（P0/P1/P2 分级）**

本周待办：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 对比 4：建模要完备

**❌ Before（清单有了，但缺边界和逻辑链）**

客户分层：
- src_unknown
- src_unknown
- src_unknown

**✅ After（MECE + 分级标准 + 对应动作）**

客户分层（按年合同金额）：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 清单体四规则自检清单

发布或分享一份清单/SOP 前，逐项检查：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| 适用于流程类/清单类/SOP 类建模 | 创意发散、头脑风暴阶段不必硬套 |
| 适用于需要反复调用或多人协作的清单 | 一次性、个人临时备忘不必过度结构化 |
| 适用于清单条目 ≥5 或涉及多个决策点 | 三五个点的简单清单保持简单即可 |
| 分级标准必须提前共识 | 否则 P0/P1 会变成无休止的争论 |
| 不能替代底层逻辑思考 | 清单体只是载体，背后仍需逻辑洁癖和 MECE |
| 对新手必须给样例 | 只给规则不给样例，执行会千人千面 |

| 失败模式 | 典型症状 | 可执行修复 |
|:-----|:------|:-----------|
| 一大坨不换行 | 一段里塞 3-4 个动作，阅读者无法判断遗漏 | 强制一行一点；每点只包含一个动作或一个判断 |
| 20 条平铺不分层 | 看的人头皮发麻，找不到结构，执行时跳步 | 按阶段/模块/角色拆成二级标题；同级条目控制在 7±2 条 |
| 有清单无优先级 | 所有点看起来一样重要，资源冲突时无法取舍 | 标注 P0/P1/P2 或 SABC；P0 必须有明确的"不做就崩"标准 |
| 为了完备而硬凑 MECE | 条目冗余、互相纠缠、反而增加决策负担 | 先保证"对决策有用"，再追求不重不漏；定期删除从未被调用的条目 |
| 分级标准未共识 | 同一事项在不同人眼里优先级不同，会议反复拉扯 | 把分级定义写成清单的附录，评审前花 5 分钟对齐 |
| 把清单当终点 | 写完清单不再迭代，错误模式变了清单没变 | 每次执行或评审后 10 分钟内补充/调整条目；设清单 owner |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
