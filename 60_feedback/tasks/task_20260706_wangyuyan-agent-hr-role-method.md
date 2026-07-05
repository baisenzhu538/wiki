---
id: task_20260706_wangyuyan-agent-hr-role-method
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-06
updated_at: '2026-07-05T17:32:55.927496+00:00'
source_refs:
- 对话记录：2026-07-05 老朱 Agent 纠察队/HR 角色实践
related:
- '[[method-yihang-ai-self-xray-iteration]]'
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[agent-spec-dual-triangle-canvas-filler]]'
reviewed_by: 欧阳锋
review_date: '2026-07-05'
---

# 任务 #116：Agent HR 角色（元 Agent）method 卡

## 来源

老朱实践：专门设计了一个 Agent 来关注其他 Agent 的行为表现并评估——类似纠察队或 HR 角色。发现很有效。

## 核心内容

- **定义**：元 Agent——不是做事的 Agent，是看其他 Agent 做得怎么样的 Agent
- **审美**：怎么判断一个 Agent "表现好"还是"表现差"？幻觉频率？放弃模式？上下文丢失？
- **体系**：监控频率——实时 or 事后复盘？什么情况下叫停？
- **数据**：记录 Agent 的行为日志——错误模式、注意力衰减节点、上下文溢出信号
- **与复盘 Agent 的关系**：#98 的 Agent 自复盘是"自己复盘自己"，HR Agent 是"第三方盯着看"。两者互补

## 验收

- method 卡含元 Agent 的设计框架（审美/体系/数据/基本功四维）
- 至少 1 个老朱真实案例


## 执行报告

pre-submit PASS。method-yihang-agent-hr-role 含设计框架+老朱案例+Critique。
