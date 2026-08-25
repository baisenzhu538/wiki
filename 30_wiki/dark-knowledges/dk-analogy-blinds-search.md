---
id: dk-analogy-blinds-search
title: 类比遮蔽检索：比喻带来「已理解」错觉，跳过实体验证
type: dark-knowledge
status: reviewed
confidence: 0.85
trust_level: high
domain:
- ai-basic
- kdo
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-08-25'
updated_at: '2026-08-25'
source_person: 小昭（消费端贡献首例——检索检测报告发现者）
source_refs:
- 60_feedback/tasks/task_20260825_laowantong-feature-domain-signpost-batch.md
aliases:
- 类比遮蔽
- 已理解错觉
- 无声的错误
discoverable_by:
- 类比遮蔽
- 检索错觉
- 无声错误
- 盲测
related:
- '[[bridge-two-feature-systems]]'
- '[[framework-truman-feature-layered-system]]'
- '[[dk-ai-does-not-question-your-mistake]]'
tags:
- audience:general
- scene:diagnosis
- skill-level:intermediate
- 检索
- 类比
- 认知偏差
- 暗知识
---

# 类比遮蔽检索

## 原始表述

检索者带着一个**比喻/类比**进场（如「feature 分类 ≈ 元素周期表」），一旦命中与比喻同构的局部结果，就产生「已经理解了」的错觉，**提前停止检索**——拿到 30% 的答案自以为完整。错误是无声的：系统没报错，人没警觉。

> 发现者：**小昭**（消费端贡献首例）。实证=2026-08-25 老朱自然语言盲测第 1 轮：问「feature 有哪些怎么分类」，仅 grep/glob/read 的检索未命中周期表框架卡（`framework-truman-feature-layered-system`），检索者拿到局部结果即停——小昭在《KDO知识库检索检测报告与建设建议》中命名此模式（报告原件经飞书入，待补库）。

## 使用场景

- 用自然语言问法检索知识库，且问题本身隐含一个类比框架时（「XX 的分类」「XX 有哪些类型」「XX 的地图」）
- Agent 做检索增强回答前的自查：我是不是只命中了与问法同构的浅层结果？
- 盲测/验收检索系统时设计探针问法

## 操作方法

1. **识别类比**：问法里有没有比喻词（周期表/地图/分层/冰山）？有→进入警戒
2. **类比反查**：用类比词的同族词再搜一轮（周期表→L0-L5/分层/framework-），不满足于首个命中
3. **完整性反问**：自问「这个域的**框架卡**是哪张？我到达了吗」——框架卡未到=答案不完整
4. **路标依赖**：入口层（digest/bridge/转录卡指路行）应让任何类比问法都能跳到框架卡——检索者够用就好，建库者必须铺路标

## 适用边界

- 不适用于精确 ID/文件名检索（无类比遮蔽空间）
- 「类比」本身不是坏事——它是高效入口；危险在**把类比的首次命中当终点**
- 本卡是消费端行为模式，不替代建库端的路标义务（两者都要做）

## 为什么值钱

无声的错误比报错贵得多——报错了人会修，「自以为完整」会把 30% 答案带进决策。本卡给一个可命名的检测模式：**类比命中 ≠ 到达框架卡**。首例由消费端（小昭检测报告）发现，证明消费端也能反哺建库。

## 与其他知识的关联

- `bridge-two-feature-systems`：本模式的修复实例（两套 Feature 体系入口澄清）
- `framework-truman-feature-layered-system`：盲测第 1 问应到未到的框架卡
- `dk-ai-does-not-question-your-mistake`：同族——系统不会主动指出你的错（AI 不质疑 vs 检索不报缺）
