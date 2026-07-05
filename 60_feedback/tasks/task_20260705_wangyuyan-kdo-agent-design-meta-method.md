---
id: task_20260705_wangyuyan-kdo-agent-design-meta-method.md
type: task
status: reviewed
assignee: wangyuyan
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-05
updated_at: '2026-07-05T20:08:20.407681+00:00'
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-yihang-ai-self-xray-iteration]]'
- '[[method-yihang-dual-triangle-ai-review]]'
reviewed_by: 欧阳锋
review_date: '2026-07-05'
---

# 任务 #105：KDO Agent 设计元方法——用双三角加速 Agent 建设

## 问题

KDO 已有 Agent 建设的散落工具（#69 画布 Agent、#98 自复盘、#97 自我拆解）但没有一张卡把"如何用双三角设计 KDO Agent"本身做成可复用的方法论。

Truman 做 partner 的速度是"3-5 天一个，下饺子"。KDO Agent 建设能否达到同样速度？

## 核心方法：Agent 建设三步

### 第一步：画 Agent 自身的双三角（动手前）

```
每个 Agent 在设计前必须填自己的双三角画布：
  H.审美 —— 这个 Agent 输出"好"的标准是什么？
  H.体系 —— 它执行任务的稳定流程是什么？
  H.创造力 —— 它的边界在哪？什么情况下它该说自己不知道？
  A.场景 —— 它解决什么问题？不为哪些场景设计？
  A.数据 —— 它需要什么数据包？从哪些 wiki 卡编译？
  A.基本功 —— 它用什么模型/工具？Feature 组合是什么？
```

画布填满 = 可以承诺交付。这不是计划工具——是风险判断。

### 第二步：Y模型引擎迭代（动手后）

```
Agent v0 → 真实场景测试 → trace复盘 → 暴露缺口
  → 回画布：哪个角不够？补上
  → Agent v0.1 → 再测 → 再复盘
```

不是一次性设计好——是第一版足够粗糙但可跑，然后每天迭代。

### 第三步：Agent 自复盘（每次运行后）

```
会话结束 → Agent 自己跑复盘 → 映射本轮对话到六要素
  → 画飞轮 → 自我改进建议 → 存入 trace
  → 下次会话作为 data pack 加载
```

## KDO Agent 设计速度对照

| 当前 | 目标（Truman 速度） |
|:---|:---|
| 每个 Agent 从零设计 prompt | 从已有 Agent 画布模板开始 |
| 迭代靠人发现问题 | Agent 自复盘暴露缺口 |
| 知识手动注入 prompt | 知识从 wiki 卡编译（#59 + #84） |
| 每次改 prompt 靠人测试 | Trace 回放自动验证 |

## 输出物

- 1 张 method 卡，固化三步法
- 1 个 Agent 设计画布空白模板
- 用 #69（画布 Agent）作为第一个走完三步法的试点

---

## 执行报告

- 产出物：`30_wiki/methods/method-kdo-agent-design-meta.md`（已入库）
- 全网调研：6 个独立框架交叉验证（MongoDB Canvas/Abundly/Anthropic/Gulli21/MASS）
- 6层交叉验证：L1-L6 全过，A 级可信
- 9层深挖：5 个失败模式 + "不该用 Agent"清单 + Trigger/Interface 维度补充
- pre-submit PASS

## 依赖

- #69（画布 Agent CLI）
- #97（AI 自我 X 光）
- #98（Agent 自复盘）
