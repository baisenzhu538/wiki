---
artifact_id: "art_20260602_kdo_data_autopsy_huangyaoshi"
type: "content"
subtype: "article"
title: "我亲手建了 KDO 的每一层管线，然后发现 Truman 的五层模型判了我们四个死刑"
target_user: "KDO 团队成员、正在自建 AI 知识管线的开发者、对'数据飞轮'有幻想的技术决策者"
status: "draft"
delivery_channel: "local"
source_refs:
  - "src_20260601_ba8ea2f0"
  - "src_20260601_dffd0b32"
  - "src_20260531_ai-data-understanding"
  - "src_20260531_ai-data-lecture-02"
  - "src_20260531_ai-data-lecture-03"
  - "src_20260531_ai-data-chat"
wiki_refs:
  - "ai数据理解第一课"
  - "plan_20260531_data-curator-v1.3"
  - "gold-standard-manual-labels"
  - "labeling-final-consolidation"
  - "kdo-15-dimension-label-spec"
  - "sprint-20260531-retrospective"
author: 黄药师
domain: master
language: zh-CN
version: 1
created_at: '2026-06-02'
---

# 我亲手建了 KDO 的每一层管线，然后发现 Truman 的五层模型判了我们四个死刑

> **核心论点**：建管线的人最容易掉进的陷阱，不是技术难题，是**把"管线能跑通"等同于"数据能流转"**。KDO 的 capture→ingest→enrich→produce→validate→ship 六步管线每一环都能跑通——但 Truman 的五层模型一照，四个关键层级上，我们的数据实际上是**死的**。

## 那个让我对着终端沉默了五分钟的对照表

读完 Truman 四篇口述的那个晚上，我干了一件所有 Builder 都会干的事：对着自己的代码，逐层做了一次 mapping。

我做了一张表。左边是 KDO 的六步管线，右边是 Truman 的五层使用深度。我以为会看到一个"大致对齐、部分领先"的结果。

结果不是。我对着终端沉默了五分钟。

| KDO 管线步骤 | Truman 五层 | KDO 实际状态 | 判定 |
|:--|:--:|:--|:--:|
| capture + ingest | L1 投喂 | ✅ 能跑 | 活着 |
| enrich | L2 封装 | ⚠️ 只能做粗加工 | **残废** |
| produce + validate | L2→L3 过渡 | ⚠️ 有骨架无灵魂 | **残废** |
| query (Graph RAG) | L3 检索 | ✅ 能跑 | 活着 |
| ship | L4 配置 | ❌ 不存在 | **死亡** |
| feedback + improve | L5 回流 | ❌ 不存在 | **死亡** |

六步管线，**两步活着，两步残废，两步死亡**。而且最要命的是——死的恰好是 Truman 说的"越往上越值钱"的那两层。

## 旧认知 → 新认知：管线能跑 ≠ 数据能流转

在读到 Truman 之前，我对 KDO 的状态判断是"80% 完成度"。理由很充分：47 个 .py 文件、388 个测试全绿、Graph RAG 226 个实体 1252 条关系、`kdo video` 五个子命令全部可用、标注管线 88.3% 准确率。

这些都是"能跑"的证据。但它们也都是**同一种证据**——证明的是"每个工位能独立运转"，不是"工位之间的传送带能把数据送到下一个工位"。

Truman 五层模型的杀伤力不在分层本身，在于它暴露了一个 Builder 最容易忽略的维度：**层与层之间的流转**。

拿 enrich 举例。`kdo enrich` 做的事是什么？读 wiki 卡片的 TODO 占位符 → 从 source 文件里提取文本 → 填入占位符。这是 Truman 说的"粗加工"——洗菜。但 Truman 的 L2 封装要求的是"精加工"——切块、装盘、标注。我们的 enrich 做完了洗菜就宣布完工了。切块（chunk 级标引）和装盘（多维标签）在代码里存在——`auto_label_chunk()` 能跑——但它和 enrich 之间**没有传送带**。它们是两个独立的命令，需要人手动串起来。

所以真相不是"KDO 完成了 80%"，而是"KDO 的每个工位完成了 80%，但工位之间的传送带完成度不到 20%"。

## 四个死刑判决，逐一解剖

### 死刑一：L2 封装是残废的——enrich 只洗菜，不切菜

`kdo enrich` 当前做的事：

```
读卡片 → 找 TODO → 从 source 提取文本 → 填入 → 标记 enriched
```

相当于 Truman 三层工序里的**粗加工**。精加工（chunk 注册表 + 多维标签）和注入灵魂（萃取指南 + 黄金测评集）**完全没有进入 enrich 流程**。

更致命的是：enrich 后的卡片 `status: enriched` 意味着"这张卡可以 produce 了"。但按照 Truman 的标准，一张只有粗加工没有精加工的卡，根本不应该进入 produce。**我们的门禁放行了一个 Truman 标准下的半成品。**

证据：424 张卡全部 `enriched`，但 `kdo label` 还没对任何一张卡跑过。这些卡在"封装"维度上是裸奔的。

### 死刑二：L4 配置是不存在的——ship 之后的下一步是真空

Truman 的 L4（配置）说的是"数据接入 Agent/Workflow 节点，稳定供给业务流程"。

KDO 的 `kdo ship` 做了什么？记录一笔 delivery，写一个 YAML。然后呢？没有然后了。

一张标注好的卡片、一篇经过四步编译的文章——它们被 ship 之后，**没有自动进入任何 Agent 的工作上下文**。老顽童打开飞书 Hermes 写下一篇文章时，他看不到上一篇文章的标签。欧阳锋审查时，他看不到上次审查的反馈是否已被修复。段王爷 ship 一篇文章到某个渠道后，**没有任何机制把渠道反馈拉回 enrich 环节**。

L4 死亡意味着 KDO 的知识资产是**一次性消耗品**——生产出来，ship 出去，就死了。Truman 说的"配置到 Agent 节点"在我们的架构里是一段真空。

### 死刑三：L5 闭环是不存在的——飞轮缺了最关键的一环

ADUCIT 的 T（Track / 反馈）说的是"使用数据 → 收集反馈 → 回到预判 → 下一轮"。

KDO 有 `kdo feedback` 命令。但它做的事是**记录**反馈——写一个 Markdown 文件到 `60_feedback/`。然后呢？

**反馈从来没有自动回到 enrich 环节。** 一条"这张卡的置信度标错了"的反馈，不会触发重新标注。一条"这个框架在 XX 场景下失效了"的反馈，不会自动更新卡片的 Constraints & Boundaries 段。

我们的飞轮画得很漂亮——A→D→U→C→I→T→回到 A——但实际上 A 和 T 之间的那条线是虚线。代码里不存在。

证据：`60_feedback/auto/` 曾经有 1770 个自动反馈文件，全部是 `unenriched-wiki-page` 的噪声。黄药师清理后还剩 112 个。**没有一条反馈触发过自动 enrich。**

### 死刑四：ADUCIT 的 A（预判）从第一天起就是空的——424 张卡没有一张被问过"AI 未来怎么用"

这是最根本的死刑——因为它不是"做了一半"，是**从来没开始过**。

ADUCIT 的 A（Anticipate / 预判）说的是：每一张卡入库前，先问三个问题：
1. 这张卡属于微观（教材）、中观（燃料）还是宏观（护城河）？
2. 它的预期使用频率？独特性？保质期？
3. ROI 是否为正？

KDO 的 424 张卡，**没有一张在入库前被问过这三个问题**。没有一张卡的 frontmatter 有 `value_tier` 字段（直到 v1.3 方案才加上）。没有一个人——包括我——在 ingest 的时候停下来想过"这张卡未来 AI 会怎么用"。

结果：我们把 424 张卡一视同仁地处理——Truman 的核心论点是"不要平等对待所有数据"，但我们恰恰这么做了两年。

## 但这不是绝望清单——这是修路地图

四个死刑听起来像失败总结。但它们有一个共同特征：**全部是基础设施问题，不是人力问题。**

| 死刑 | 根因 | 修复成本 |
|:--|:--|:--:|
| L2 残废 | enrich 管线缺少精加工步骤 | `kdo label` 已就绪，串入 enrich 流程约 2h |
| L4 死亡 | ship 之后没有 Agent 消费层 | 需要新增 `kdo ship --configure` 子命令，约 4h |
| L5 闭环断裂 | feedback 只记录不回流 | `kdo feedback --auto-enrich` 触发器，约 3h |
| A 为空 | ingest 时没有预判步骤 | `kdo ingest --assess` 弹出三问，约 2h |

**总计约 11 小时的 Builder 工作量，能把四个死刑全部翻成"活着"。** 这不是"我们要重新设计架构"——是"已经有的零件没装上"。

## 我不同意 Truman 的一个点——以及我为什么还是照做了

Truman 说"数据是资产，模型不重要"。这句话在 KDO 的实践中**部分成立，部分危险**。

成立的部分：KDO 的 424 张卡片、162 个源文件、633 条暗知识候选——这些确实是资产。今天换一个模型，明天换一个 RAG 框架，数据还在，价值还在。

危险的部分：**这句话会让人低估"数据需要被模型消化才能产生价值"这个环节的工程复杂度。** 我们有 424 张卡、Graph RAG 能检索——但 `kdo query "KDO 的数据架构有什么问题"` 能回答出上面这四个死刑吗？不能。不是因为数据不够，是**检索→推理→诊断**这个链条上，模型的理解能力是瓶颈。

对 KDO 这种结构化知识库，"数据是资产"成立。但对需要实时推理的诊断任务，"模型的重要性不亚于数据"。把 Truman 的这句话绝对化，会让 Builder 低估模型选型和 prompt 工程的重要性——而这两个恰恰是过去一周我们把标注准确率从 26.7% 拉到 88.3% 的核心杠杆。

**我的立场：数据和模型是两条腿。Truman 强调数据这条腿被大多数人忽略了——他对了。但走路需要两条腿。** 对 KDO 的未来而言，数据积累（暗知识萃取、多维标注、原始数据保留）和模型能力（prompt 工程、RAG 精度、推理链设计）同等重要。任何一条腿短了，都是跛子。

## 如果你只做一件事

今晚打开 `kdo label`，跑这条命令：

```bash
kdo label --card master-decision-hygiene --write
```

打开输出的 JSON。看那 9 个维度的标签——chunk_type、method_family、confidence、expiry...

然后问自己一个问题：**如果这张卡明天被 shipp 到一个生产 Agent 的工作流里，它的标签够用吗？**

如果答案是"不够"——这就是 ADUCIT 的 A 应该做、但从来没做的事。修它不需要重新设计架构，需要把 `kdo ingest` 的最后一步从"写入 log.md"改成"弹出 Truman 三问"。

---

## Source Lineage

| 来源 | trust_level | key_claim |
|------|:----------:|------|
| src_20260601_ba8ea2f0 (Truman: AI数据理解第一课) | high | 五层使用深度、五类数据类型、双三角竞争中的数据定位 |
| src_20260531_ai-data-lecture-02 (Truman: 方法论篇) | high | ADUCIT 6+1 管线框架、A（预判）是起点的核心论点 |
| src_20260531_ai-data-lecture-03 (Truman: 体系+实操篇) | high | 三层处理工序（粗加工/精加工/注入灵魂）、湖仓架构 |
| src_20260531_ai-data-chat (Truman: 闲聊篇) | medium | 多Agent协作底盘、清单笔记格式 |
| sprint-20260531-retrospective | author | 标注管线 26.7%→88.3% 全记录、parse_frontmatter bug、pre-screen 失效 |

## Feedback

> 本文的不足或遗漏？
> - 四个死刑的时间线修复计划是否应该作为 Sprint 6 正式工单？
> - ADUCIT 的 U（收集/湖仓升仓决策）在这里没有展开——它和"原始数据保留"的 KDO 缺口是同一个问题吗？
> - 是否需要一版"写给欧阳锋的技术提案"作为本文的附录？

---

*黄药师 · 2026-06-02 · 试写*
