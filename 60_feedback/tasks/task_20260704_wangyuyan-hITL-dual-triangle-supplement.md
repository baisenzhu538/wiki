---
id: task_20260704_wangyuyan-hITL-dual-triangle-supplement
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_laowantong-human-in-the-loop-dual-triangle-relation
related:
- '[[concept-yihang-human-in-the-loop-dual-triangle]]'
- '[[annotation-yihang-dual-triangle-master]]'
---

# 任务 #77：#66 人在环×双三角关系卡 追补

## 任务目标

对 #66 已产出的 `concept-yihang-human-in-the-loop-dual-triangle` 卡进行**单点追补**——补入一条被遗漏的关键原文和历史定位。

**不是返工，不是重做。** 只改一处，加一个小节。

## 追补内容：人在环的历史定位

口述稿 L4557（课后闲聊段）Truman 说了一句话，在原始任务单素材清单中未被标注：

> "人机协作在之前好像只有一个主流，只有一个这个人在环，人在环也不是为了AI准备的啊。"

### 这句话拆解出的三层信息

1. **"人机协作之前只有一个主流"**——在双三角出现之前，业界讨论人机协作，只有一个公认框架，就是 human-in-the-loop。
2. **"人在环也不是为了AI准备的"**——HITL 是一个更古老的系统工程/机器学习概念，最初设计场景是模型训练中的人工标注和校验，不是 AI 协作。
3. **隐含结论**——双三角是**第一个专门为 AI 时代人机协作设计**的框架。填补了 HITL 未覆盖的空白。

### 卡片中的具体修改

在概念澄清表（或独立小节）中加入第四行：

| 概念 | 定义 | 历史定位 |
|:---|:---|:---|
| 双三角的历史定位 | 第一个专门为 AI 时代设计的人机协作框架 | 在双三角之前，业界只有"人在环"一个主流概念，且人在环不是为 AI 协作准备的（口述稿 L4557）；双三角填补了这个空白 |

或在卡片中新增一个独立小节（3-5 行即可）：

```
## 历史定位

在双三角之前，人机协作领域只有一个主流框架——人在环（Human-in-the-loop）。
但 Truman 指出："人在环也不是为了 AI 准备的"（口述稿 L4557）。
HITL 最初是系统工程/ML 领域的概念，设计场景是模型训练中的人工校验。
双三角是第一个专门为 AI 时代人机协作设计的科学框架。
```

## 原始素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt` L4557
- 已产出卡片：`concept-yihang-human-in-the-loop-dual-triangle`

## 验收标准

- 卡片中新增历史定位小节（或概念澄清表新行），含口述稿 L4557 原文引用
- `kdo pre-submit` 仍通过
- `kdo lint` 0 新增 ERROR
- source_refs 追加口述稿路径
- 欧阳锋终审通过

## 边界说明

- **只改这一处**。不改卡片结构、不改其他章节、不重新审查全卡。
- 如果欧阳锋终审认为不需要加，可以 reject 并 close。
