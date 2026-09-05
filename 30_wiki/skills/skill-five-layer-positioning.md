---
id: skill-five-layer-positioning
title: "五层定位自检 Skill——新任务入口七问清单体（草案）"
type: skill
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.8
trust_level: high
language: zh-CN
created_at: 2026-09-06
updated_at: 2026-09-06
domain:
- ai-collaboration
aliases:
- 五层定位自检
- 层级选择七问
- 新任务入口七问
- src_wechat_4b6327b374540e2e
- AI实战路径-五个层级全解析-口述
- d1-aidahangha-oral-notes
source_person: 一堂创始人（AI实战路径 L44/L84/L86-88/L492-504）
source_context:
- 本卡为草案（诊断 §三.1 指定产出）；行为化（40_outputs/capabilities/skills/shared/ SKILL.md）走 skills-assistant P1-P4 产线，本卡先立内容规格
- 清单体结构按手册 §12.2.1（#639）
source_refs:
- 00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:44
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:84-88
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:492-504
- 60_feedback/diagnosis/working/d1-aidahangha-oral-notes.md
related:
- '[[framework-ai-five-layer-architecture]]'
- '[[framework-ai-native-working-paradigm]]'
- '[[framework-encapsulation-methodology]]'
- '[[skill-demand-analysis]]'
- '[[agent-spec-kouspeng-task-decomposer]]'
- '[[bridge-yitang-kdo-document-over-session]]'
- '[[agent-spec-skills-assistant]]'
discoverable_by:
- 五层定位
- 层级选择
- 新任务入口
- 七问
- 选层
- 任务分类
- 心流
quality_labels:
- actionable
- cited
- insight
tags:
- 五层架构
- 层级经济学
- 实操
- 方法
- 口述
- 编排
- AI Native
- 避坑
---

# 五层定位自检 Skill（草案）

> **定位声明**：本卡是 [[framework-ai-five-layer-architecture]] 的入口级执行件（诊断 §三.1 指定）——把「接到任务先定层」做成一张 7 问清单。它属于五层框架的**使用前置步骤**：框架回答「五层是什么」，本 Skill 回答「手上的这个任务在哪层」。草案状态：内容规格已定，行为化（SKILL.md 进 shared/）待 skills-assistant 产线。
>
> **一句话**：先定层，再动手——用 2 分钟的七问，避免 2 天的层级错配返工。

## 使用场景

- 接到任何要用 AI 的新任务/新项目，开工前。
- 团队成员「投入大产出小」，怀疑层级错配时，做诊断入口。
- 评审别人的 AI 方案时，快速定位方案的主战场层。

## When NOT to Use

- 任务 < 10 分钟且一次性（过七问的成本大于收益，直接做）。
- 已有明确 SOP 的常规任务（SOP 已隐含定层）。
- 纯工具故障排查（走 debug 流程，与选层无关）。

## 新任务入口七问（清单体）

| # | 问题 | 判定 | 依据锚 |
|:--|:--|:--|:--|
| 1 | 这个任务对应哪一层？（对话/项目/资产/员工/团队） | 写下主战场层 | L492-494 五层映射口诀 |
| 2 | 能不能在更低一层解决？ | 能→降层，写下低层判据为什么满足/不满足 | L44「如果我们真的可以在这一层用好，就没必要用上面的工具」；L84 判据 |
| 3 | 心流要求是什么？（需要 10 秒级来回，还是可容忍分钟级停滞） | 对话型任务避免迁到停滞感重的工具 | L86-88 心流维度 |
| 4 | 上下文就绪度？（Agent 能否自助取到背景：文档/知识库/数据包） | 缺→先补上下文文档再开工 | L180-182 上下文模式 |
| 5 | 有没有封装机会？（做完后什么东西可复用） | 有→收尾时按六层形态封装 | L362 频次引擎；[[framework-encapsulation-methodology]] |
| 6 | 复用预期？（同类问题预计还会来几次） | ≥2 次→值得封装；1 次→不封 | [[framework-encapsulation-methodology]] 封装优先级判据 |
| 7 | 升级触发条件？（什么信号出现才上更高一层） | 写下明确信号，防默认上高层 | L344-352 跳级失败模式 |

## 操作步骤（90 秒版）

1. 口头回答七问，允许「不知道」——第 4/7 问不知道就是答案（先补再干）。
2. 把 1/2/7 三问的答案写进任务单开头（一行即可）。
3. 干完后回看第 5/6 问：封装动作做没做。

## 判断标准（什么算"定对了层"）

- 主战场层 ≠ 最高层：如果答案总是第五层，说明第 2 问没认真答。
- 升级有信号：能说出「出现 X 信号才上高层」，而不是「感觉这个任务复杂」。
- 心流匹配：对话型任务没有被迁到会停滞的工具上。
- 封装闭环：任务结束回答得出「固化了什么」或「无可封装」。

## 常见失败模式（本 Skill 特有）

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 七问变成仪式 | 每问都答「看情况」，开工层和平时一样 | 只强制写 1/2/7 三问答案，写不出=没定层 |
| 用复杂度替代判据 | 「这个任务很复杂所以上高层」 | 复杂度不是判据，L84 的能力覆盖判据才是 |
| 定层一次定终身 | 中途任务性质变了仍按原层干 | 升级触发条件（第 7 问）命中即重跑七问 |
| 定完层不补上下文 | 第 4 问答「缺」但照样开工 | 第 4 问答案为「缺」时，开工前置动作=建上下文文档 |

## 与既有 Skill 的关系

- 与 [[skill-demand-analysis]]：那是「需求怎么挖」，本 Skill 是「任务在哪层」——需求分析在第二层跑，本 Skill 在它之前。
- 与 [[agent-spec-kouspeng-task-decomposer]]：分解官接管「拆任务」，本 Skill 管「放哪层」——先定位再分解。
- 行为化路径：本卡过审后由 [[agent-spec-skills-assistant]] 走 P1-P4 产线生成 shared/ SKILL.md，本卡退为内容规格真相源。

## Synthesis

本 Skill 的价值密度在第 2 问（能不能降层）和第 7 问（升级触发条件）——两问合起来构成对「默认上高层」偏好的双向钳制：事前压不住升级冲动，事后锁不住降级空间。七问里唯一非一堂素材原生的是第 6 问（复用预期），来自本库封装优先级判据，用于防止「什么都封」的镜像病。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 接到新 AI 任务 | 跑七问，写 1/2/7 答案进任务单 | 任务单头部出现定层行 |
| 方案评审 | 问主战场层+升级信号 | 评审纪要含层位声明 |
| 任务中途变向 | 重跑第 1/2/7 问 | 层位变更被记录而非默认漂移 |

## 迭代日志

- 2026-09-06 v1.0：#654 batch1 草案，七问结构按诊断 §三.1；每问挂实战路径行号锚；行为化待 skills-assistant 产线。
