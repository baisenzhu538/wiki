---
title: "黄药师体验任务：AI学习域全管线走通 → 2篇文章"
assigned_to: "黄药师 (Builder)"
priority: "P1"
created_at: "2026-05-24"
reviewer: "欧阳锋"
status: "done"
depends_on: []
blocks: []
---

# 黄药师体验任务：AI学习域全管线走通 → 2篇文章

## 背景（重要，先读）

黄药师这一年多来一直在**建工厂**——KDO CLI、质量门、Graph RAG、scaffold、video、lint、self-check。工厂建得很好（379 tests pass，0 回归），但有一个盲区：**你从来没有用过自己建的工厂从头到尾产出过一篇文章。**

这导致两个后果：
1. 你做基础设施决策时，靠的是"推理"而非"体感"。你不知道 `kdo clean-transcript` 在真实口述稿上效果到底如何，因为你没跑过 200KB 的口述稿。
2. 你不知道从 `00_inbox/` 里的转录稿到 `40_outputs/` 里的文章，中间有多少个步骤是丝滑的、有多少个步骤是磨人的。

这个任务不是要改变你的角色——你依然是 KDO 基础设施唯一负责人，不接量产。这是一次性的**狗粮任务（dogfooding）**：自己吃一口自己做的饭。

## 素材

```
00_inbox/AI-study/
├── 一堂-AI学习-AI工具应用AMA口述.txt        140KB  口述稿
├── 一堂-AI学习-AI时代判断力口述.txt          206KB  口述稿
├── 一堂-AI学习-科学提问口述.txt              131KB  口述稿
├── asking-the-right-questions-critical-thinking.md  14KB  书摘（已结构化）
├── [11张知识地图/框架图 .png]
00_inbox/
└── ai-native-five-levels.md                    26KB  AI Native 五层框架（用户原创）
```

## 做什么

走完整条 KDO 管线，产出 **2 篇文章**：

### 文章 1：《学会提问》批判性思维工具

- 素材：`科学提问口述.txt` + `asking-the-right-questions-critical-thinking.md` + 提问相关图片（好问题VS坏问题/提问工程化/提问进化路线图等）
- 方向：从布朗&基利的批判性思维框架出发，结合一堂科学提问方法论，给出一套可操作的提问检核清单

### 文章 2：AI 时代的判断力

- 素材：`AI时代判断力口述.txt` + `ai-native-five-levels.md` + 相关图片
- 方向：AI 时代什么变了、什么没变——判断力的底层逻辑与 AI 工具的边界

### 执行流水线（按顺序，不许跳）

| 步骤 | 动作 | 工具 |
|:--:|------|------|
| 1 | 清理三份口述稿（去噪+去口头禅+断句+术语标注） | `kdo clean-transcript` |
| 2 | 三张关键知识图 OCR（提问进化路线图/提问工程化/FeatureSet） | PaddleOCR |
| 3 | ingest 清理后的全部素材 → source + wiki 骨架 | `kdo ingest` |
| 4 | enrich：三步编译法（Condense → Critique → Synthesis） | `kdo enrich` + 手动补 Critique |
| 5 | produce 两篇文章 | `kdo produce content/article` |
| 6 | validate 通过质量门 | `kdo validate` |
| 7 | 写一份体验笔记（见下方） | 手动 |

## 体验笔记（第 7 步产出）

做完后，写一段话记录以下问题（不用结构化，想到哪写哪）：

- **哪个步骤最痛苦？** 是哪个工具不好用、哪个文档不清楚、哪个错误信息让你困惑？
- **哪个步骤根本不存在？** 你期望有但还没有的工具/命令是什么？
- **哪个体感最意外？** 用自己建的工具时，什么和你想的不一样？
- **如果每天要做 10 篇这样的文章，你会先修什么？**

这份笔记比两篇文章更重要——它直接决定你下一批基础设施工单的优先级。

## 验收

| # | 验收项 | 判定 |
|:--:|------|:--:|
| 1 | 三份口述稿完成 `kdo clean-transcript`，可读 | 人工 |
| 2 | 素材完成 `kdo ingest` → `10_raw/sources/` | 文件存在 |
| 3 | AI学习域概念卡（≥3张）完成 enrich（含 Critique + wikilinks） | `kdo validate --v15 --domain ai-learning` PASS |
| 4 | 两篇文章产出到 `40_outputs/content/articles/` | 文件存在 + 非空 |
| 5 | 文章通过 `kdo validate` 质量门 | exit 0 |
| 6 | 体验笔记写入 `60_feedback/corrections/huangyaoshi-dogfood-ai-study-2026-05-24.md` | 文件存在 |

## 不做什么

- **不做** 单元模型域（那个留给老顽童）
- **不做** VA 分析（你不是洪七公，图片 OCR 就够了）
- **不做** 此域全部卡片（重点做出两篇文章需要的 3-5 张卡即可）
- **不影响** Batch 7 基础设施任务（那些已完成）

## 时间预期

这是一个体验任务，不是产能任务。预计 2-3 小时，不赶工。重点是**过程中的感受**，不是产出量。

---

*欧阳锋 · 2026-05-24*
*这是一次性体验式任务，不影响黄药师的主要职责（KDO 基础设施）*
