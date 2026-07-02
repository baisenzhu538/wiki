---
id: task_20260703_huangyaoshi-proposal-kdo-next-phase-orchestration
title: "黄药师建议书：KDO 下一阶段任务编排"
type: proposal
status: draft
author: 黄药师
target_reviewer: 王语嫣（方向把关）+ 欧阳锋（终审）
created_at: 2026-07-03
updated_at: 2026-07-03
domain:
  - kdo
  - infrastructure
source_refs:
  - 00_inbox/底层逻辑之一-Y模型/_processed/底层逻辑_整合笔记.md
  - 对话记录：2026-07-03 Y模型定位讨论
related:
  - "[[yt-decision-y-model]]"
  - "[[framework-kdo-self-attack]]"
  - "[[plan-state-json-to-sqlite-migration]]"
---

# 黄药师建议书：KDO 下一阶段任务编排

> 收件人：王语嫣（方向把关）
> 抄送：欧阳锋（终审）
> 背景：Y模型是知识库根节点，Agent实测启动事实臂，KDO进入方法论验证阶段

---

## 一、核心判断：Phase shift

KDO 此前在**理论臂**上建体系（框架/概念/工具/暗知识）。现在用户开始用 Agent 实测，**事实臂**启动。

任务编排应该从"多建卡"转向"让闭环转起来"。不是停止建卡——而是**建卡的优先级由 Agent 反馈决定**。

---

## 二、建议的三条线

### 线 A：Y模型根节点化（架构动作，1天）

| 做什么 | 谁 | 产出 |
|:---|:---|:---|
| `yt-decision-y-model` 卡重写升级 | 老顽童 | 从"决策域概念卡"升级为 KDO 根节点卡 |
| 所有 framework 卡 related 补 `[[yt-decision-y-model]]` | 老顽童（批量） | 理论臂归属清晰 |
| 所有 case/dk 卡 related 补 `[[yt-decision-y-model]]` | 老顽童（批量） | 事实臂归属清晰 |
| GraphRAG rebuild | 黄药师 | Y模型成为查询入口节点 |

不新建卡。不改目录结构。只补 related。

### 线 B：Agent闭环跑通（验证动作，持续）

| 做什么 | 谁 | 产出 |
|:---|:---|:---|
| 销售对话助手继续实测 | 用户 | 真实客户对话的反馈数据 |
| Agent 反馈回流 KDO | 王语嫣判断 + 老顽童执行 | 按回流规则表更新 agent-spec 卡/方法论卡/dk 卡 |
| 第一批回流记录写入 | 老顽童 | `tool-opc-sales-dialogue-assistant` 的迭代日志 |

这是事实臂的核心数据源。没有它，Y模型右臂是空的。

### 线 C：销售域卡片生产（内容动作，持续）

| 做什么 | 谁 | 产出 |
|:---|:---|:---|
| #44 销售专题 12-15 张卡 | 老顽童 | 按黄药师上次估算的范围 |
| 销售×Y模型桥接卡 | 老顽童 | 1 张——销售五步法如何映射到 Y模型两臂 |
| 暗知识补挖（Vikki+大馨） | 王语嫣 + 老顽童 | #42 已在队列中 |

---

## 三、建议不要做的事

- ❌ Y模型根节点化不要新建目录或 card type——只补 related
- ❌ Agent 闭环不需要黄药师建 `--agent-trace`——先用手工迭代日志
- ❌ 不要新增"跨域模式层"目录——P-10 继续停车场，等 Agent 反馈积累后再启动
- ❌ 不要为 Y模型建新卡——重写现有卡够了

---

## 四、入队建议

| 优先级 | 任务 | 依赖 |
|:---|:---|:---|
| P0 | 线 A：Y模型根节点化 | 无 |
| P0 | #44 销售域卡片生产 | 无 |
| P1 | Agent 闭环跑通 | 依赖 #44 部分卡产出 + 用户继续实测 |
| P1 | #42 暗知识补挖 | 无 |
| P2 | Y模型×各域桥接卡（时间管理/销售/Vikki/大馨） | 依赖线 A 完成 |

---

## 五、黄药师本周基建任务

| 做什么 | 说明 |
|:---|:---|
| GraphRAG rebuild | 线 A 完成后执行 |
| kdo pipeline 持续监控 | 观察 Agent 反馈是否产生新的 lint 信号 |
| 不新增工具 | Phase shift 后基建重心是"维护闭环"，不是"新建能力" |

---

*黄药师 2026-07-03*
