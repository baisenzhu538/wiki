---

id: sk-ai-problem-validation
title: 技能：问题验证三维度法
type: "tool"
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论分享，2026-06
source_refs:
  - 10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md
wiki_refs:
- '[[sk-ai-question-problem-checklist]]'
- '[[ai-collaboration-mindset-shift]]'
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tags:
- '#method/prompt-engineering'
- '#domain/ai-saas'
- '#method/workflow'
created_at: '2026-06-06'
updated_at: '2026-06-18'
tools_required:
- 表格工具（Excel / 画布等）
- 数据管理工具（Notion / Airtable 等）
prerequisite_skills: []
related:
- '[[sk-ai-question-problem-checklist]]'
- '[[ai-collaboration-mindset-shift]]'
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
  - 标题为「三维度法」，但正文使用四要素框架，存在命名与结构不一致
  - 失败模式与边界仅基于单一路源笔记，未经过多场景实证

---

# 技能：问题验证三维度法

## 用一句话讲清楚

在向 AI 派任务前，用「前后对比、真实锚点、受益对象、可解性」四要素验证这是一个值得解决的**真问题**，而非伪需求。

## 核心要点

一个真正的 problem 需要同时满足四个要素，缺一不可：

| 要素 | 填写问题 | 示例（好） | 示例（坏） |
|------|--------|---------|---------|
| **前后对比** | 解决前是什么状态？解决后希望是什么状态？ | 之前每天花 2 小时写报告，之后希望压缩到 30 分钟 | 提高写报告效率 |
| **真实锚点** | 这个问题在真实世界中有具体场景吗？ | 每周一的销售数据报告 | 企业数字化转型 |
| **受益对象** | 解决后谁会受益？ | 销售主管每周节省 30 分钟 | 全体员工 |
| **可解性** | 你相信这个问题是可解的吗？有因果链和能力支撑吗？ | 有报告模板+数据来源+验证过的方法 | 希望 AI 帮我思考 |

## 边界

- **适用场景**
  - 要给 AI 派一个新任务，但不确定这个任务是否值得投入
  - AI 执行完成后，业务结果没有变化
  - 团队开会讨论 AI 落地方向时需要客观标准

- **不适用场景**
  - 已经有明确验收标准、只需执行的纯工具任务
  - 探索性、发散性创意任务（如头脑风暴、风格探索）

## 行动 Checklist

- [ ] 拿到任务描述后，先填入四要素表格
- [ ] 检查「前后对比」是否有可量化的 before/after
- [ ] 检查「真实锚点」是否有具体场景、频率、触发条件
- [ ] 检查「受益对象」是否具体到人或岗位
- [ ] 检查「可解性」是否具备数据、模板、方法或因果链
- [ ] 任意一栏填不出来 → 回退到问题定义，不进入 AI 执行
- [ ] 四栏填满 → 将表格作为上下文一并提交给 AI，并附加验收标准

## 失败模式

| 失败信号 | 根因 | 纠偏动作 |
|----------|------|----------|
| 四要素中任意一栏填不出来 | 问题本身定义模糊，仍是愿望陈述 | 回退到问题定义，用更具体的场景和指标重新描述 |
| 「受益对象」写成「全体员工」「公司」 | 受益者泛化，无法衡量价值 | 聚焦到具体岗位、具体人的具体动作 |
| 「可解性」写成「希望 AI 帮我思考」 | 缺乏因果链与能力支撑 | 先人工梳理已知方法、数据、模板，再交给 AI |
| 跳过验证直接让 AI 执行 | 把 AI 当万能解药 | 强制先填表，填不完不进入执行 |
| 表格填完但不作为上下文提交给 AI | AI 缺少问题边界，输出偏离 | 将填好的表格作为 system/user 上下文的一部分加载 |

## 相关卡/互链

- [[sk-ai-question-problem-checklist]]：问题-疑问区分检查清单，可与本卡组合使用
- [[ai-collaboration-mindset-shift]]：AI 协作心态转变，帮助理解为何要先验问题

## 来源

- 纪浩，AI俱乐部-AI协作方法论分享，2026-06
- 原始笔记：10_raw/sources/src_20260606_42e11f09-ai需要练那个ai时代要不要练笔记.md

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
