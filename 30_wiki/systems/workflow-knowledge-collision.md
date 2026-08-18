---
id: workflow-knowledge-collision
title: 知识碰撞工作流：产出前先碰撞知识库
type: system
domain:
- hermes
- kdo
status: enriched
created_at: '2026-06-14'
author: 周伯通
source_context: KDO internal decision record （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
source_refs:
- 'pending_archive: src_unknown'
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
related:
- '[[dk-f4-wrong-workdir]]'
- '[[three-party-data-alignment]]'
- '[[business-research-skill-oscar-13-weapon-system]]'
- '[[system-yitang-research-workflow]]'
- '[[modeling-capability-for-kdo]]'
- '[[yt-decision-ai-partner]]'
- '[[agent-external-brain-design]]'
- framework-doris-industry-report-4step
- tool-yitang-research-industry-scan
tags:
- src_unknown
- src_unknown
- src_unknown
- audience:manager
- scene:reference
- skill-level:intermediate
reviewed_by: pending
confidence: 0.7
trust_level: medium
updated_at: '2026-06-29'
discoverable_by:
- 知识碰撞
- 知识验证
- 框架测试
- 认知冲突
- 知识工作流
---
> 核心原则：在产出之前，先拿当前问题去碰撞知识库里的已有框架。不只是查定义——是测试框架在问题上的适用性，找出"对得上""对不上""缺什么"三个区域。



## 适用场景

| 场景 | 典型触发词 |
|:-----|:-----|
| 写作任务 | 写文章、读后感、总结、分析报告 |
| 商业分析 | 评估、调研、竞品、方案、建议 |
| 咨询问答 | 怎么看、怎么理解、给个建议 |
| AI 辅助产出 | 帮我生成、帮我分析、帮我写 |
| 跨领域学习 | 学一门新课、接触一个新领域 |

一句话：**只要任务涉及"理解 + 判断 + 产出"，就先搜 wiki。**

排除：纯机械操作（修格式、改日期）、纯信息检索（"XX 在哪里"）、已有明确指令的重复性任务。

---

## 三步法

### Step 1：搜索（30 秒）

用任务的核心概念搜索 `30_wiki/concepts/`、`frameworks/`、`tools/`：

```
search_files(pattern="<核心概念>", target="content", path="wiki/30_wiki/")
```

目标：找到 1-3 张最相关的卡片。两轮搜不到 → 标注"知识库暂无相关框架"，然后产出。

### Step 2：碰撞（3 分钟）— 关键步骤

拿找到的框架去"测试"当前任务。问三个问题：

| 问题 | 做法 | 示例 |
|:-----|:-----|:-----|
| **什么对得上？** | 当前任务中哪些现象可以用这个框架解释？ | 代俊隆的拆本罗盘 → 本质是"体系"在起作用 |
| **什么对不上？** | 框架的哪个维度在当前任务中没有对应？为什么不适用？ | 双三角模型缺少"创造力" → 短剧创作需要创造力 |
| **什么缺了？** | 当前任务中有什么重要维度是框架完全没覆盖的？ | KDO 产出物缺少"场景适配"——同一张卡在不同场景需要不同版本 |

> 只做 Step 1（找卡片→引用定义）不算知识碰撞。那叫信息检索。检索不产生新洞察，碰撞会。张力所在，就是洞察所在。

### Step 3：产出

碰撞完成后，产出物至少包含：

1. **一个明确的框架锚点**：引用具体卡片（`card-id`），不写"根据相关理论"
2. **至少一处碰撞发现**：写清楚"对得上/对不上/缺什么"中的至少一个
3. **一条行动含义**：不只是"理解了"，还有"所以接下来怎么做"

---

## 反面教材

以一篇 AI 短剧课读后感为例，三轮迭代的差距：

| 轮次 | 做法 | 结果 |
|:----:|:-----|:-----|
| 1 | 读完素材直接写，没查 wiki | 正确但平庸，和其他人写的没区别 |
| 2 | 查了 wiki 找到双三角，但只读定义就引用 | 理解错误（审美≠独立维度），没发现创造力缺失 |
| 3 | 拿短剧创作去碰撞双三角，发现对不上和缺失 | 产出有洞察，框架被扩展 |

差距不在"查没查 wiki"——**在"碰撞了没有"。**

---

## Agent 执行规范

1. 触发本工作流后，**先搜索 wiki，再开始产出**。不允许"边写边搜"。
2. 搜索范围优先 `concepts/` → `frameworks/` → `tools/` → `cases/`。
3. 产出中必须显式引用至少一张 wiki 卡片（wikilink 格式）。
4. 碰撞中发现框架缺陷或缺失，产出中必须明确标出。
5. 碰撞过程中产生的新洞察（如"这个框架缺了 X 维"），应作为 card-improvement 反馈写入对应卡片的 Critique 或 Constraints 节。

---

## 关联

- src_unknown
- src_unknown
- src_unknown
