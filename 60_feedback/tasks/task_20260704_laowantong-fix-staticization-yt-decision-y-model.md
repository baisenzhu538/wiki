---
id: task_20260704_laowantong-fix-staticization-yt-decision-y-model
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_laowantong-cross-domain-framework-iteration-audit
related:
- "[[yt-decision-y-model]]"
- "[[method-yitang-y-model-engine-cycle]]"
- "[[framework-yitang-y-model-dual-triangle-synergy]]"
- "[[audit-framework-staticization-20260704]]"
---

# 任务 #68-P0：修复 yt-decision-y-model 静态化

## 任务目标

对 KDO 根节点 `yt-decision-y-model` 做引擎化升级——从静态四层结构重定位为迭代发动机。

## 审计发现（摘要）

`yt-decision-y-model` 在跨域审计中得分 4/12（高风险）。核心问题：
1. 引擎层语言完全缺失——卡片把 Y模型 呈现为四层静态结构
2. 五步法被写成线性流程（1→2→3→4→5），缺少循环箭头
3. 案例是"Y模型可以用于 XX 场景"，不是"XX 案例推动了 Y模型 框架本身的进化"

参照标准：`method-yitang-y-model-engine-cycle`（12/12）和 `framework-yitang-y-model-dual-triangle-synergy`（12/12）

## 修复内容

### 必须改（P0）

1. **在"核心框架"节之前增加"引擎层 vs 工具层"小节**（约 10-15 行）
   - 明确 Y模型 首先是迭代发动机，其次才是分析框架
   - 引用 Truman 原话："列出来你对这个问题的基础框架认知，列出来多条，不完整也没关系，会不断迭代的"
   - 链接到 `method-yitang-y-model-engine-cycle`（操作层）和 `framework-yitang-y-model-dual-triangle-synergy`（领域实例）

2. **将五步法改为循环图**（修改现有 ASCII 图或新增循环图）
   - 第 5 步"知行迭代" → 箭头回到第 1 步"明确核心问题"
   - 标注：每轮循环后，核心问题本身可能被重新定义

3. **为每个跨域迁移示例加迭代标注**（约 5-8 行）
   - 在五个场景示例的末尾各加一句："本轮循环后，对该领域的框架认知从___升级为___"

### 建议改（P1）

4. **增加"朴素起点"小节**（约 5-8 行）
   - 说明 Y模型 循环的起点不是"已经理解问题"，而是"我有一个粗糙的、可能错误的框架认知"
   - 链接到 `method-yitang-y-model-engine-cycle` 步骤 2

5. **在 Critique 的内部局限中增加一条**
   - "引擎层被忽略：多数学习者把 Y模型 当静态分析模板，忽略了它的迭代发动机本质"

## 不改的部分

- 四层结构图保留——它是 Y模型 的概念骨架
- 一堂其他课程关系表保留——它是导航资产
- KDO 根节点映射保留——它是系统架构文档
- 哲学呼应保留——它是文化锚定

## 验收标准

- `kdo pre-submit` 通过
- "引擎层 vs 工具层"小节存在且引用 Truman 原话
- 五步法有循环箭头或"回到第 1 步"说明
- 跨域迁移示例有迭代标注
- 欧阳锋终审通过
