---
id: task_20260704_wangyuyan-dual-triangle-ai-review-method
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[method-dual-triangle-flywheel-engine]]'
- '[[yt-decision-y-model]]'
---

# 任务 #85：双三角 AI 辅助复盘法 method 卡

## 来源

口述稿 L2220-2312。Truman 现场演示了用双三角让 AI 复盘协作过程的完整操作。

## 任务目标

产出 1 张 method 卡，把 Truman 的操作固化成可复用的方法论。每个 Agent 协作结束后都可以走这套流程。

## 核心内容

### 1. Truman 的操作流程

1. 完成一次高质量的 AI 协作任务
2. 对 AI 说一段提示词（口述稿 L2228-2247 有完整版本）
3. AI 去知识库学双三角→复盘整个协作→映射每一轮对话到六要素→画飞轮→做对照实验
4. 产出复盘报告

### 2. 提示词模板

从口述稿提取的标准提示词：

> "你去学一下双三角模型，这个模型是用来解读人与AI高水平协作的框架。帮我还原一下刚才咱们所有的工作过程，你做了什么，我做了什么，以及咱们两个如何互补的。如果没有人与AI会怎么样？如果没有AI人会怎么样？为什么应用双三角模型会有如此巨大的产出？帮我做一个完整的复盘，注意总分总的结构。"

### 3. 复盘产出包含

- 每一轮对话映射到双三角六要素
- 人和 AI 各自的贡献分布
- 飞轮识别（几轮对话里几个飞轮）
- 对照实验（没有人 vs 没有 AI vs 人+AI）
- 给团队分享的教学材料版本
- AI 自我改进建议（"下次你还能做什么更好"）

### 4. 对 KDO 的应用

- Agent trace 复盘：每次 agent-spec 运行结束后自动走这套流程
- 飞轮日志自动生成：复盘报告 → `dual-triangle-flywheel-log.md`
- 实测数据积累：复盘报告可以作为 agent-spec 迭代的输入

## 验收标准

- `kdo pre-submit` PASS
- `kdo lint` 0 新增 ERROR
- 含完整提示词模板（可复制粘贴使用）
- 含复盘产出结构说明
- related ≥ 4
- 欧阳锋终审通过
