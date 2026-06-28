---
id: case-truman-ai-partner
title: 案例：Truman AI Partner（阿蕊老师）——从十年笔记到可售卖的 Agent
type: case
status: enriched
domain:
- src_unknown
- src_unknown
source_person: Truman
source_context: 一堂《AI时代清单体笔记》课程
source_refs:
- 10_raw/sources/src_20260606_575627a4-一堂-AI时代清单体笔记-Truman-口述-01.md
- 10_raw/sources/src_20260606_db4fc211-一堂-AI时代请单体笔记-Truman-口述-02.md
- 10_raw/sources/src_20260510_cfbce5d1-Truman的个人成长五步法.md
- 10_raw/sources/src_20260510_27fe5f0e-truman的选择：两条职业成长路线.md
tags:
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
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-06-07
updated_at: '2026-06-29'
related:
- - - yt-personal-checklist-notes
- - - case-ji-hao-skills-market
- - - pending_unknown
author: 老顽童
reviewed_by: 洪七公
confidence: 0.8
trust_level: medium
diagnostic_signals:
- framework_lens: AI Partner 不是替代判断，而是约束下协作
  follow_up_question: 你的 Agent 边界清单里，哪些判断必须人类做、AI 只做整理/提示？
- framework_lens: 知识资产化 ≠ 课程售卖，需要封装即时反馈机制
  follow_up_question: 你的方法论能否被拆成可校验的清单规则？学生练习后能否自动得到结构化反馈？
- framework_lens: AI 在语料不足或边界不清时会产生幻觉建议
  follow_up_question: 你的笔记库是否已有 100+ 同主题案例？Agent 的角色是 P 执行还是 C 共创？
---

# 案例：Truman AI Partner（阿蕊老师）

> Truman 用十年时间积累 1500+ 篇清单体模型笔记，将其编译为领域知识库，封装成一个 P 角色的 AI agent（内部代号"阿蕊老师"），在一堂内部使用并计划单独售卖。

## 问题：知道但做不到，专家时间无法规模化

Truman 在一堂教"清单体笔记"课程，学生在练习过程中需要反馈和指导。他对学生的笔记质量有明确的审美标准，但无法一对一辅导所有人。课程结束后，学生普遍处于"知道但做不到"的状态：

- src_unknown
- src_unknown
- src_unknown

真实锚点来自一堂真实学员的需求。Truman 看到学生在课程后"知道但做不到"，需要一个能在日常练习中持续提供反馈的工具。不是"AI 很火所以做一个"——是自己学生真需要。

## 方案：把十年笔记封装成有硬边界的 AI Partner

Truman 的解法不是做一个"更聪明的 AI"，而是做一个**角色被严格约束、反馈可结构化、训练可段位化**的 Agent。

### 1. 知识资产化：1500+ 篇清单体笔记 → 领域知识库

Truman 十年刻意练习积累了约 1500 篇模型笔记，以清单体格式为主。清单体的特点是：一行一点、层级缩进、边界清晰——这恰好是 AI 最容易消费的知识格式。Truman 将这些笔记按主题整理为"领域知识库"，作为 Agent 的语料来源。

### 2. 角色约束：P 角色，只管执行不探讨

Agent 被定义为 **P 角色（执行伙伴）**，核心边界：

- src_unknown
- src_unknown
- src_unknown

### 3. 反馈段位化：把 L2-L6 标准写入校验规则

Agent 的反馈不是泛泛的"不错"或"再改改"，而是对照一堂笔记法的段位体系（[[yt-personal-checklist-notes]]）：

| 段位 | 反馈焦点 | 示例反馈 |
|:---|:---|:---|
| L2 备忘 | 是否丢信息、是否分点 | "第 3 条建议补充来源" |
| L3 协作 | 阅读舒适度、层级清晰度 | "二级标题超过 7 项，建议再归类" |
| L4 内化 | 故事线是否成立 | "当前是时间线，建议改为问题→原因→方案线" |
| L5 思考 | 原创思考占比、好问题 | "你的观点占 20%，尝试把 Flag 提到 30%" |
| L6 萃取 | 现场建模、提炼能力 | "可进一步把这段访谈提炼为一个检查清单" |

### 4. 输入输出同构：清单体 I/O

Agent 的输入（学生交的笔记）和输出（反馈/训练计划）都是清单体。这种"同构"设计有两个效果：

- src_unknown
- src_unknown

## 结果：从"卖时间"到"卖 Agent"

| | Before | After |
|:---|:---|:---|
| 学生笔记反馈 | 无反馈，靠自己悟 | AI Partner 即时结构化整理 + 诊断 + 训练计划 |
| 方法论传播 | 靠上课讲，听完就忘 | 封装为 Agent，学生随时可用 |
| Truman 的时间 | 一对一辅导，不可规模化 | Agent 自动化 L1-L3，Truman 只做 L4-L5 |
| 知识资产化 | 笔记躺在 Obsidian 里 | 编译为可售卖产品 |

受益人：

- src_unknown
- src_unknown
- src_unknown

## 可迁移场景与使用边界

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 专家已沉淀 100+ 同主题结构化案例 | 方法论显性化程度高，Agent 才有可靠语料 |
| ✅ 练习场景可线上化、反馈标准可清单化 | 如笔记格式、代码规范、文案检查等，规则越清晰越适合 |
| ✅ 需要大量重复性 L1-L3 反馈 | 人类专家只做高阶判断，Agent 承接标准化诊断 |
| ❌ 领域依赖现场感知或强人际信任 | 如外科手术、面对面谈判、心理咨询，Agent 无法获取非语言信息 |
| ❌ 只想"蹭 AI 概念"而封装 | 没有真实用户痛点和付费意愿，四要素验证不通过时不做 |
| ❌ 方法论还在探索阶段 | 没有 50+ 已验证案例积累，Agent 输出不可靠 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| **Agent 越界替用户判断** | 用户问"这篇笔记好不好"，Agent 直接给"好/不好"并修改，用户不再自己思考 | 在 system prompt 中写死"只整理、不评价、不建议"；输出格式限定为"原文要点 + 可选故事线 + 待用户确认的问题" |
| **反馈同质化，学生麻木** | Agent 每次反馈都是"分点/分层/独立行"三件套，学生无法定位下一阶训练点 | 把 L2-L6 段位标准写入校验规则，每次输出标注"当前段位 + 下一阶 1-2 个具体动作" |
| **语料只重"量"不重"质"** | 1500 篇笔记里混有早期低质量笔记，Agent 输出出现"分点但无逻辑"等专家已淘汰的风格 | 建立"黄金语料池"，只选用近 2-3 年、经专家标记为"高价值"的笔记；定期用最新校正案例覆盖旧案例 |
| **AI Partner 当课程赠品，没有使用闭环** | 学生周末用几次后流失，Agent 数据没有回流课程迭代；产品无法单独售卖 | 设计"练习→反馈→段位打卡→下一课"闭环，把 Agent 输出作为课程作业必填项，并收集高频错误反哺课程内容 |

## 实操模板：个人 Agent 封装 Checklist

如果你想复制 Truman 的路径，可按以下清单自检：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 诊断信号：这个案例是否值得你参考？

1. **你是否有"知道做不到"的用户？** 如果有，继续看；如果没有，这个案例不是解药。
2. **你的方法论能否被拆成可校验的清单规则？** 如果不能，Agent 只能做整理，做不了教练。
3. **你是否愿意让 Agent 只做"半成品"，把高阶判断留给人？** 如果追求的是"最强 AI"，这个案例的设计哲学会与你冲突。

## 对 KDO 的启发

Truman 的 AI Partner 和纪浩的 Skills 市场（[[case-ji-hao-skills-market]]）是**同一模式的两个实例**：

| | Truman | 纪浩 |
|:---|:---|:---|
| 核心产品 | 单一 Agent（阿蕊老师） | Agent 分发平台 |
| 知识格式 | 清单体笔记 | 不限格式 |
| 方法论语料 | 1500+ 篇个人积累 | 团队协作积累 |
| KDO 等价物 | `kdo encapsulate` 编译单个 skill | `kdo skill list` + registry |

KDO 已经能走通 Truman 的单 Agent 路径（note-coach）。纪浩的平台模式是下一步——先把单个 skill 做扎实，再做分发层。

进一步可参考：
- src_unknown
- src_unknown
- src_unknown

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 教训

- src_unknown
- src_unknown
- src_unknown

---

## 失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|---|---|---|
| src_unknown | src_unknown | src_unknown |
