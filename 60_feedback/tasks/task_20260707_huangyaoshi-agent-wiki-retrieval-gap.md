---
id: task_20260707_huangyaoshi-agent-wiki-retrieval-gap
type: task
status: draft
domain:
- agent-infrastructure
- wiki
author: 黄药师
created_at: 2026-07-07
priority: P1
target: 王语嫣
---

# 任务编排建议：Agent 域知识检索缺口修补

> **一句话**：Agent 生产知识存入 wiki，但 Agent 自己不消费 wiki。飞书 Agent 回答方法论问题时基于训练记忆而非 wiki 检索——这是比"单张卡片没对齐"更底层的架构缺口。

## 触发事件

飞书 Agent（推测王语嫣）在回答用户关于"调研方法论和 KDO 实战 SOP 的关系"时：

1. **正确识别了缺口**：一堂 OSCAR 五步法 + 13 武器体系 vs KDO 实战外部探索 SOP（选方向→广撒网→深追搜→交叉比对→出诊断 + 四路 Attacker），本质在做同一件事但术语和结构没打通
2. **但做出了错误的事实判断**："这些卡都归档了，不在 30_wiki/ 活跃目录里"——实际上 OSCAR 框架卡在 `30_wiki/frameworks/framework-yitang-oscar-research.md`（enriched），13 武器卡在 `30_wiki/concepts/business-research-skill-oscar-13-weapon-system.md`（enriched）
3. **根因**：Agent 没有在回答前检索 wiki——它基于训练记忆或会话片段推断，而不是基于 `kdo query "调研方法论"` 的结果

## 根因分析

```
Agent 生产知识 → 写入 wiki → wiki 是知识资产的唯一真相源
                                          ↓
Agent 回答问题时 ← 基于训练记忆/会话上下文 ← ❌ 没有读 wiki
```

这不是王语嫣一个人的问题——**所有 7 个 Agent 都没有"回答域知识问题前先检索 wiki"的行为模式。** 这个行为模式没有被写入任何 SOUL.md、-context.md 或 agent-os.md。

连带发现：`external-exploration-sop` 这个文件在 wiki 中不存在——如果这个 SOP 只存在于某个 Agent 的会话记忆里而没有落笔到文件，就是 P-10 规则（口头流程 ≠ 书面资产）的重演。

## 已完成（黄药师 2026-07-07）

以下基础设施变更已执行，不需要王语嫣重复做：

| # | 动作 | 文件 | 内容 |
|:--|:---|:---|:---|
| 1 | 所有 Agent context 加检索铁律 | 7 个 `.agent/*-context.md` | `## ⛔ 域知识检索铁律` 段——回答域知识问题前必须 kdo query/wiki Read |
| 2 | agent-os.md §10 加检索复盘要求 | `agents/agent-os.md` | §10.4.1——B 级复盘必须记录检索行为，A 级必须记录检索发现 |
| 3 | 补 sales-dialogue-assistant 复盘要求 | `.agent/sales-dialogue-assistant-context.md` | 此前没有 ⛔ 会话结束段，一并补齐 |

## 建议王语嫣编排的任务（按优先级）

### P0：验证 OSCAR 卡的实际状态

**当前事实**：`framework-yitang-oscar-research.md` 和 `business-research-skill-oscar-13-weapon-system.md` 都是 `enriched` 状态，大量 `src_unknown` 占位，未经欧阳锋终审。飞书 Agent 说"归档了"是错的——但说"不是成品"是对的。

**建议**：王语嫣确认以下两个方向选哪个：
- **A**：把这两张卡从 `enriched` 推进到 `reviewed`（补齐内容→欧阳锋终审）
- **B**：判断这两张卡不值得投入，标记 `deprecated`

**如果选 A**，建议任务单包含：
1. 补齐 OSCAR 五步卡中所有 `src_unknown` 占位
2. 将 KDO 实战外部探索 SOP 的术语映射写入 OSCAR 卡的 Bridge/Synthesis 章节：O↔选方向、S↔广撒网、C↔深追搜、A↔交叉比对、R↔出诊断+四路 Attacker
3. 欧阳锋终审

### P1：补写 external-exploration-sop 文件

当前这个 SOP 似乎只存在于 Agent 会话中。如果它确实是 KDO 日常使用的工作流，需要落笔到文件。

**建议路径**：`40_outputs/capabilities/skills/shared/external-exploration/SKILL.md` 或 `30_wiki/methods/method-kdo-external-exploration-sop.md`

### P1：将检索行为纳入 review-check.py

当前 review-check.py v2 只检查章节数和盲点深度。建议下一版增加关键词检查：复盘中是否出现了 `kdo query` / `wiki` / `检索` 等术语。不做语义判断，只做存在性检查。

### P2：为 Hermes Agent 建立 wiki 检索能力

洪七公、段王爷跑在 Hermes（飞书），不能直接调 `kdo query`。需要：
- 确认 Hermes 环境的 Python 能否 import kdo 包
- 如果不能，提供替代方案（直接 Read wiki 文件 / 预编译域摘要注入 SOUL.md）

## 不在此次范围的

- **Agent 自动检索**（每次回复前自动 kdo query）：目前成本太高（每轮都跑语义检索），等 P1 验证"手动检索"确实改善了回答质量后再评估
- **OSCAR 卡深度重写**：这是内容层的任务，应该进 production-queue 由老顽童执行而非黄药师

## 相关文件

- `30_wiki/frameworks/framework-yitang-oscar-research.md`（enriched，需补齐）
- `30_wiki/concepts/business-research-skill-oscar-13-weapon-system.md`（enriched，需补齐）
- `30_wiki/concepts/yt-research-weaponry-course.md`（reviewed ✅）
- `30_wiki/cross-domain-patterns/`（P-10 产出，三个跨域模式索引）
- `.agent/*-context.md` × 7（已更新检索铁律）
- `agents/agent-os.md` §10.4.1（已更新检索复盘要求）
