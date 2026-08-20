---
id: 378
assignee: hermes
status: reviewed
updated_at: '2026-08-19T14:36:26.326530+00:00'
title: 一刷卡补强 6 项 + 双向回链（P2，老朱 08-19 拍板）——#376 补强清单落地
priority: P2
dependency: []
reviewed_by: 欧阳锋
review_date: '2026-08-19'
grade: A
---

# #378 一刷卡补强 6 项 + 双向回链（P2）

## 任务目标

#376 深挖笔记尾部 6 项一刷卡补强建议，老朱 2026-08-19 拍板立项执行。只补不删、不改原意；补完后做新卡↔旧卡双向回链。

## 素材

- 补强清单（含行号）：`00_inbox/AI知识库/深挖笔记_二刷_20260819.md` 尾部"一刷卡补强建议清单"
- 口述原文：`00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt`（引用前查 `理解_口述+逐字稿消化.md` §7 ASR 对照表）

## 执行范围（6 项，逐条）

| # | 目标卡 | 补什么 | 口述行号 |
|:--|:--|:--|:--|
| 1 | tool-top-level-document | "没有顶层文档就骂负责人"倒逼机制 + 每年至少 100 个 + "先写顶层文档再开工"制度化前置 | L694、L708-710 |
| 2 | tool-skill-packaging-eight-steps | 逼出 10 ToDo + 10 NoToDo 清单步骤 | L1040-1042 |
| 3 | case-vibecoding-one-week-delivery（或 15 秒做图对应卡） | 三上下文公式"指向=上下文开关"表述 | L1234-1240 |
| 4 | framework-patrolkit-radar | 巡查输入话术示例（"查询本地核心知识库，看看团队最近一周都干啥了"） | L2466-2480 |
| 5 | concept-session-vs-memory-vs-document | 全量复盘文档=session 终态（五万字文档后可扔 session） | L1594-1616 |
| 6 | framework-ai-deliberate-practice-loop（或 yitang-deliberate-practice 对应卡） | "刻意练习笔记"角度：练技能也记笔记（100 小时讲课练习，笔记成熟=讲课成熟） | L526-532 |

回链：6 张被补强旧卡 → 在 related 补链相关二刷新卡（如 dk-ai-self-evolution-prompt / dk-context-patching-recipe / dk-doc-numbering-business-logic 等，按内容相关性选）；新卡侧已链旧卡的做双向验证，缺哪侧补哪侧。

## 边界（这 6 张是欧阳锋终审过的卡，动它们=二次过审）

- 只增补段落/条目，不删不改已有正文原意；每处补强带口述行号溯源
- 数字人名以逐字稿为准；2 处待核矛盾（莫非老师/半肥猫、元旦年份）规避口径同 #376
- 补强后每卡 `kdo pre-submit` 0 ERROR；改完送欧阳锋**复终审**（写审分离不变）

## 内容价值判断（PROTOCOL §7 合规声明）

- 本任务只对 6 张已点名卡片做增补，无删除/移动/废弃动作；不动任何 `00_inbox/` 素材
- 批量三问：①动手前 diff 预览 6 卡改动范围并声明 ②预期变更=仅上述清单内增补 ③非空值不覆盖（已有内容只追加不覆写）

## 验收标准

1. 6 项补强逐条落地，每条带口述行号溯源，原意零篡改（diff 可验：只增不删）
2. 双向回链：6 旧卡 related 含相关新卡 + 新卡侧反向验证无死链
3. 6 卡 `kdo pre-submit` 全 0 ERROR
4. diff 逐卡贴任务单执行报告

## 交付

1. 6 卡改动 diff + 回链验证记录
2. 送欧阳锋复终审

---

## 执行报告（2026-08-19 老顽童 hermes 实例）

### 完成概要
6 项补强逐条落地 + 双向回链完成，全部 pre-submit 0 ERROR。

### 6 卡补强明细（diff：6 文件 +51/-11，只增不删；-11 为 framework-ai-deliberate-practice-loop related: null→列表展开格式）
| # | 卡 | 补强内容 | 口述行号 |
|:--|:--|:--|:--|
| 1 | tool-top-level-document | 新增"5.5 制度强化"节：没有顶层文档就骂负责人（倒逼）/ 先写顶层文档再开工 / 每年至少 100 个 | L694、L710、L708 |
| 2 | tool-skill-packaging-eight-steps | 步骤 5 后补"逼出双清单"（10 ToDo + 10 NoToDo 封边界） | L1040-1042 |
| 3 | case-vibecoding-one-week-delivery | 可迁移场景补"指向=上下文开关"（三上下文公式：我是谁/检索文档/设计宪法） | L1234-1240、L2236-2238 |
| 4 | framework-patrolkit-radar | 使用步骤补"巡查输入话术示例"（查本地知识库看团队最近一周都干啥了） | L2466-2480 |
| 5 | concept-session-vs-memory-vs-document | 应用方法补"全量复盘文档=Session 终态"（五万字导出后可扔 session） | L1594-1616 |
| 6 | framework-ai-deliberate-practice-loop | Step 6 后补"刻意练习笔记"角度（练技能也记笔记，笔记成熟=讲课成熟） | L526-532、L538 |

### 双向回链
- 6 旧卡 related 补新卡：tool-top-level-document→dk-doc-numbering-business-logic/dk-shoulu-yixia-culture；tool-skill-packaging→dk-aesthetic-redline-doc/dk-context-patching-recipe；case-vibecoding→dk-context-patching-recipe/dk-occhams-knife-tool-migration；patrolkit-radar→dk-doc-explosion-slowdown/dk-ai-self-evolution-prompt；session-vs-memory-vs-document→dk-ai-self-evolution-prompt/dk-one-sentence-handover；deliberate-practice-loop→dk-collection-vs-assets/dk-context-patching-recipe/dk-ai-self-evolution-prompt（原 related: null 一并补全）
- 新卡侧反向验证：13 张新卡 related 已含旧卡（tool-top-level-document/case-vibecoding/framework-multi-agent-collab-chain-six/dk-one-sentence-handover/dk-model-demystification 等），pre-submit WIKILINK 0 死链验证

### 验证
- 6 卡 kdo pre-submit **✅ PASS**（WIKILINK/DOMAIN/DK_SECTION/OUTLINK 全 0；framework-ai-deliberate-practice-loop 的 tags/source_refs 警告为历史遗留，非本任务引入）
- diff 可验：只增不删（+51/-11，-11 为 related: null 展开）

### 待欧阳锋复终审
- 6 卡补强（二次过审）
- 历史遗留提示：framework-ai-deliberate-practice-loop source_refs 为 arXiv 引用（5/5 unreachable）+ tags 缺失——建议另立项修补
