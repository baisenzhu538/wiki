---

id: tool-ban-fei-mao-yong-ai-zuo-jie-gou-hua-yong-hu-diao-yan
title: 技能：用 AI 做结构化用户调研
type: tool
status: enriched
domain:
- src_unknown
- yitang- src_unknown
source_person: 半肥猫
source_context: AI俱学乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- src_unknown
- src_unknown
prerequisite_skills:
- src_unknown
related:
  - [[tool-纪浩-Agent技能市场设计法]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-28'
pipeline:
- src_unknown
- src_unknown
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- lens: 替代执行
  follow_up: 明确 AI 只能辅助设计框架/整理笔记，访谈执行必须由人类完成
- lens: 事实假设混淆
  follow_up: 要求 AI 将每个问题标注为"事实"或"假设"，并检查假设是否有数据支撑
- lens: 约束缺失
  follow_up: 在提示词中写明目标、范围、用户画像、业务场景后再让 AI 生成框架

---

# 技能：用 AI 做结构化用户调研

## 用一句话讲清楚

半肥猫提出的"AI 协助用户调研"方法：让 AI 负责调研的机械性前半段（定框架、列问题、整理笔记），人类保留需要共情和洞察力的后半段（执行访谈、解读非语言信号），用结构化约束避免 AI 把调研变成"水梯会上的庞统"。

## 核心要点

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 边界

| 维度 | 适用 | 不适用 |
|------|------|--------|
| 场景 | 快速设计调研框架、整理大量访谈记录、初步探索性调研 | 深度质性调研、敏感话题调研、需要行为观察/非语言信号的研究 |
| 用户 | 有基本调研判断力、能区分事实与假设的人 | 完全依赖 AI 输出、无法做 spot check 的人 |
| 数据 | 需要结构化问题清单、访谈大纲、笔记整理 | 需要真实用户情感、隐私场景、临场互动反馈 |

## 失败模式

| 失败信号 | 根因 | 修正动作 |
|----------|------|----------|
| 让 AI 代替访谈 | 混淆"辅助设计"与"替代执行" | 明确 AI 只能生成框架/整理笔记，访谈执行必须由人类完成 |
| 不区分事实和假设 | AI 默认混合事实与假设输出 | 要求 AI 标注每个问题是事实还是假设，并人工审查假设的数据支撑 |
| 约束不清晰 | 提示词缺少目标、范围、用户画像 | 在让 AI 生成框架前，先写明目标、用户群体、业务场景、时间/地域限制 |
| 问题清单过泛或偏离目标 | 未给足边界，AI 按概率填充通用问题 | 用"目标→约束→事实/假设"三段式约束提示词 |
| 把 AI 整理的笔记当最终洞察 | 缺少人类对上下文和情感的解读 | 将 AI 输出作为"素材稿"，最终洞察需人工提炼和交叉验证 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么有效

AI 在机械性任务上效率高于人类：生成问题清单、检查假设、整理笔记。人类在需要共情、洞察力、非语言觉察的任务上不可替代。两者合作能大幅提升调研效率。

## Critique

### 内部局限

- src_unknown

- src_unknown

- src_unknown

### 外部攻击

#### Shoshana Zuboff 的"监控资本主义"与"调研的权力不对等"

**Shoshana Zuboff**（*The Age of Surveillance Capitalism* 作者）从数据权力和隐私角度质疑：

- src_unknown

- src_unknown

- src_unknown

> **Zuboff 的拷问**："你说 AI 能帮助做结构化调研。但你想过吗——每次调研效率提升 10%，意味着你能做更多次调研、收集更多数据。这不是“更好的用户理解”，这是“更多的数据提取”。你在用 AI 构建一个更高效的监控机器，而用户在这个过程中的权力正在被削弱。"

#### Nassim Taleb 的"假设的危险"与"调研的虚假性"

**Nassim Taleb**（*The Black Swan* 作者）从认知论和黑天鹅角度质疑：

- src_unknown

- src_unknown

- src_unknown

> **Taleb 的拷问**："你说调研要“区分事实和假设”。但你知道吗？真正重要的事实——那些能改变游戏规则的事实——从不出现在用户访谈中。用户自己都不知道自己会怎么做。你在用 AI 来构建一个“用户行为的叙事”，然后用这个叙事来指导产品决策。这就是叙事谬误的定义。"

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown

## Feedback Path

- src_unknown
