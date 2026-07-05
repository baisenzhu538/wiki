---
id: task_20260705_huangyaoshi-proposal-yai-canvas-agent-v3
title: "黄药师建议书：画布Agent v3升级 + EC分库方案"
type: proposal
status: draft
author: 黄药师
target_reviewer: 王语嫣（方向把关 + 任务编排）
created_at: 2026-07-05
updated_at: 2026-07-05
domain:
  - kdo
  - ai-collaboration
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角partner的对话记录20260705.md
  - 对话记录：2026-07-05 老朱×YAI Partner 双三角画布对话
related:
  - "[[agent-spec-dual-triangle-canvas-filler]]"
  - "[[canvas-agent.py]]"
  - "[[plan-kdo-multi-repo-architecture]]"
---

# 黄药师建议书：画布Agent v3 + EC分库

> 收件人：王语嫣
> 来源：老朱×YAI Partner 双三角画布对话，完整蒸馏

---

## 一、画布 Agent v3 升级（#69 迭代）

YAI Partner 的四样模式需写入 `agent-spec-dual-triangle-canvas-filler` v3：

| # | 模式 | KDO 当前 | 需改为 |
|:---|:---|:---|:---|
| 1 | 开场姿态 | 逐格提问 | "你想到什么说什么，我负责接住和归类，不做强弱判断" |
| 2 | 状态标注 | [确认]/[假设]/[空白] | 增加"贯穿约束""暂放""有方向待补"四种精确状态 |
| 3 | 排序减法 | 无 | 每轮更新后标主挖角/副挖角/贯穿约束/暂放 |
| 4 | 追问升级 | 无 | "我能验证"→追问→"其他AI也能接手"的升级链 |

**建议人**：黄药师改 `canvas-agent.py`，老顽童更新 agent-spec 卡。
**优先级**：P1——画布Agent是KDO Agent化的第一个试点，明天就要用。

---

## 二、EC（工程能力）分库方案

### 背景

老朱的真实场景：10年智能医药代码库（5G，.NET+Vue，无文档，强耦合），需要一人+AI梳理重构。这不是"学方法论"——是**用AI做工程**。当前 wiki 主库存方法论，不适合放代码分析数据、SVN日志、EC规范手册（30万字）。

### 方案

单独建一个 Obsidian vault：`C:\Users\Administrator\Desktop\ec-vault\`

| 目录 | 内容 | 与主库关系 |
|:---|:---|:---|
| `20_memory/` | EC规范手册、20条铁律、踩坑记录 | 从主库 `card-reader.py` 读取方法论卡 |
| `30_wiki/` | 代码模块分析、架构图、资产包 | 按双三角六要素组织 |
| `00_inbox/` | AI分析原始输出、SVN日志 | 同上 |
| `agents/` | 代码考古员Agent、交叉验证Agent | 加载主库的 agent-os.md |

### 跨库桥接

主库的 card-reader.py（`localhost:8899/read?path=...`）已就位。EC库的Agent通过HTTP读取主库方法论卡。两个库不需要在同一台电脑——主库方法论卡是编译后的prompt，EC库启动时注入。

### 与停车场的对接

分库方案在 P-5/P-9 停车场。EC库可以作为**第一个副库试点**——验证"主库存方法论、副库存应用"的跨库协作模式。

---

## 三、建议入队顺序

| 优先级 | 任务 | 说明 |
|:---|:---|:---|
| P0 | 画布Agent v3 | 明天就要用。黄药师改代码，老顽童改卡 |
| P1 | EC分库建立 | 老朱已经有30万字EC手册+真实代码库，不需要等 |
| P2 | 跨库bridge验证 | card-reader.py已就位，EC库Agent加载主库方法论 |

---

*黄药师 2026-07-05*
