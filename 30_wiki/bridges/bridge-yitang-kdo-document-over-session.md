---
id: bridge-yitang-kdo-document-over-session
title: "桥接：一堂「少用 Session 多用文档」 × KDO .agent/ 文档体系——上下文显性复利"
type: bridge
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-09-06
updated_at: 2026-09-06
domain:
- ai-collaboration
- kdo
aliases:
- 少用Session多用文档
- 文档胜Session
- 上下文显性复利
- Session记忆文档三层
- src_wechat_4b6327b374540e2e
- AI实战路径-五个层级全解析-口述
- 宣讲会：一堂-2026下半年AI大航海-口述
- d1-aidahangha-oral-notes
source_person: 一堂创始人（实战路径 L210-212 + 宣讲会 L408-416 + IMG5 视觉主图）× KDO .agent/ 体系（09-03 顿悟互证）
source_context:
- 三源互证桥：实战路径主锚句+宣讲会三层定义+IMG5 视觉公式（Session≪AI记忆≪文档知识库），KDO 侧为 .agent/ 公共记忆体系（CLAUDE.md：禁止用 /memory 替代 .agent/ 文件）
- dk「上下文显性复利」挂靠本卡
source_refs:
- 00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:210-212
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:408-416
- 00_inbox/AI大航海20260905/session和AI记忆还有文档知识库.png
- CLAUDE.md
- 60_feedback/diagnosis/working/d1-aidahangha-oral-notes.md
related:
- '[[framework-encapsulation-methodology]]'
- '[[framework-ai-five-layer-architecture]]'
- '[[bridge-yitang-kdo-skill-center-network]]'
- '[[case-360-overnight-course-rebuild]]'
- '[[bridge-yitang-kdo-gate-philosophy]]'
- '[[skill-five-layer-positioning]]'
- '[[framework-kdo-modeling-methodology]]'
- '[[concept-session-vs-memory-vs-document]]'
discoverable_by:
- Session
- 文档
- 上下文
- 显性复利
- 记忆三层
- 公共记忆
- 顿悟
- agent体系
quality_labels:
- insight
- principle
- cited
- quotable
tags:
- 上下文工程
- 复利
- 机制
- 避坑
- 口述
- 实操
- 互证
- 知识沉淀
review_date: 2026-09-06
---
# 桥接：一堂「少用 Session 多用文档」 × KDO .agent/ 文档体系

> **定位声明**：本桥记录第三组互证——一堂给个人 AI 用户的资产化建议（少用 Session 多用文档），与本库的组织级制度（.agent/ 是唯一真相源、禁止用工具私有记忆替代）是同一个原理的两个应用尺度。本卡同时承载 dk「上下文显性复利」。
>
> **同口径前证（#654 抽检发现）**：库内 [[concept-session-vs-memory-vs-document]]（2026-08-16，楚门 AI 知识管理探索营口述）已载同一三层口径——与本桥同源同讲者、间隔三周独立再现，构成口径稳定性的复证；两卡分工：该卡=个人知识管理视角的完整论述，本桥=KDO 组织制度的对读与 dk 挂靠。

## 一堂端：三层定义（三源合一）

1. **主锚句**（实战路径:L210-212，逐字回验）：「尽量降低对于 Session 的依赖少用 Session」「多用文档」——Session 里形成的那些「看不着的」东西「随着时间会消失」；「文档长期来说是最可靠的」。
2. **三层精确版**（宣讲会:L408-410，逐字回验）：Session=「一次对话啊，开个会临时的啊，一会儿就消失了」；记忆=员工自己记本儿上，「的确也记了，的确也能找着，但是呢，长此以往他也就没了」——**记没记你不知道，是它的东西**；文档=团队桌面公共现场（背景/事实/规则），重要得多。
3. **视觉公式**（IMG5 直读）：Session ≪ AI 记忆 ≪ 文档知识库——价值和复利的差距，本质是上下文能不能被看见、被协作、被复用；**上下文越显性，复利越强**。

### dk：上下文显性复利
- **维度标签**：复利机制
- 一句话：上下文的复利率与它的显性度成正比——Session（隐性、随人消失）＜AI 私有记忆（半显性、不可协作）＜文档（全显性、人与 AI 共读共写有版本史）；把上下文从左往右搬一次，就是一次复利升级。
- 锚：IMG5（session和AI记忆还有文档知识库.png）+ 宣讲会:L408-416 + 实战路径:L210-212
- 使用边界：判断「该不该写下来」的默认判据；不适用于真正一次性的摩擦性信息（写了也无人读的，留着比维护便宜）。

## KDO 端：同一原理的组织化

| 一堂建议 | KDO 制度化 |
|:--|:--|
| 少用 Session 多用文档 | CLAUDE.md：禁止用 Claude Code `/memory` 替代 `.agent/` 文件——`/memory` 是工具私有记忆，换工具就丢；`.agent/` 跟着 git 走，是唯一真相源 |
| 记忆是「它的东西」，长此以往也没了 | 各角色 context 文件（.agent/<role>-context.md）+ 跨会话失忆恢复文件——把「记性」外置成仓库内文件 |
| 文档=公共现场 | `.agent/context.md` 共享状态 + `90_control/todos/<role>.md` 队列落盘——角色之间不靠群聊靠文件 |
| 约束指令落笔到任务文件（口头=不存在） | 铁律 #3：口头审查意见=不存在，换会话就丢（P-10） |
| 上下文文档微操+任何 Agent=生产力飞跃（宣讲会:L416） | 启动即读三件套：CAPSULE_STARTUP → startup.md → context——任何实例开机即恢复全部上下文 |

**09-03 顿悟互证**（见诊断编排计划 `60_feedback/diagnosis/diag_20260906_wangyuyan-aidahangha-orchestration-plan.md`）：本库在 09-03 已独立完成同一顿悟——「agent 的记性不在模型里，在仓库里」。本桥把这次顿悟与一堂的三层公式对接，确认它不是局部偏好而是普遍结构。

## 为什么 AI 时代「文档 > 记忆」更极端

1. **人会追问，Agent 不会**：人类的 Session 记忆丢了还能靠同事口口相传找回来；Agent 的新实例是真正的白纸——不落盘的上下文是永久丢失。
2. **记忆不可审计**：宣讲会三层定义里记忆的致命伤是「记没记你不知道」——不可审计的记忆在门禁体系里等于不存在（与 [[bridge-yitang-kdo-gate-philosophy]] 的锚点纪律同构：无锚点=不可核查=不可采信）。
3. **文档是并行的前提**：360 案例里「所有 AI 读完这个文档几乎就可以干活」（实战路径:L126-128）——多 Agent 协作的本质是让所有参与者（人与 AI）围着同一份显性文档工作，而不是各自带着私有记忆开会。

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 用工具记忆替代仓库文档 | 换工具/换机后 AI「失忆」，重建成本高 | 记忆一律落 .agent/ 或 30_wiki/，工具记忆只做缓存 |
| 文档写完不维护 | 文档与现状漂移，读者按过时信息决策 | 关键文档带 updated_at 与失效条件；过期即改或标废 |
| 只把结论写文档 | 过程与摩擦丢失，复盘无从下手 | 决策+分歧+依据一起落盘（决策记录口径） |
| 把 Session 当备份 | 重要结论只在对话里 | 会话结束三问强制落盘（新资产/新阻塞/下次记住什么） |

## Synthesis

本桥把一个个人效率建议升级为组织设计判据：**上下文显性复利**（dk）给出的是一条可排序的迁移方向——任何信息，问一句「它在哪一层」（Session/私有记忆/文档），能往右搬就往右搬。KDO 的特殊性在于把这条判据制度化了：任务流转走 queue 文件、角色记忆走 .agent/、知识走 30_wiki/、经验教训走 pitfalls/ corrections——全部在复利最高的那一层。一堂的学员需要被劝「多用文档」，KDO 的成员没有这个选择（禁止清单兜底）——制度把判断变成默认。与 [[framework-encapsulation-methodology]] 的关系：文档化是封装的第一步（先显性，再抽象）；与 [[bridge-yitang-kdo-skill-center-network]] 的关系：显性文档是能力可流通的前提。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 对话里出现重要结论 | 会话结束前落盘到对应文件 | 结论 24h 内可被未参会者检索到 |
| 发现自己在重复交代背景 | 把背景写成文档而不是再讲一遍 | 下次同类任务开头零交代 |
| 工具记忆里有有价值内容 | 迁移进仓库文件 | 工具清空不损失资产 |
| 文档与现实打架 | 以现状改文档或标废 | 无「明知过时仍引用」的决策 |

## 迭代日志

- 2026-09-06 v1.0：#654 batch1 生产，三源合一（实战路径 L210-212 + 宣讲会 L408-416 + IMG5）；引语逐字回验。
