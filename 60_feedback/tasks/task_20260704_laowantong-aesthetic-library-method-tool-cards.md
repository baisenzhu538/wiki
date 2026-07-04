---
id: task_20260704_laowantong-aesthetic-library-method-tool-cards
title: 审美快速建立工作法 + 审美库采集工具卡
type: task
status: reviewed
assignee: 老顽童
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-04
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
related:
- "[[annotation-yihang-dual-triangle-master]]"
- "[[extraction-yihang-dual-triangle-main]]"
---

# 任务 #72：审美快速建立工作法 + 审美库采集工具卡

## 任务目标

王语嫣在重新深读双三角口述稿时发现，Truman 把自己过去一年建立审美的具体做法（爬虫抓图、智能打分、转 Keynote 为模型、扒官网/音乐/视频/段子最佳实践等）几乎全部摊开，但此前标注和生产严重遗漏了这些可工具化的内容。本任务要求老顽童产出：

1. 一张 **method 卡**：`method-yihang-aesthetic-fast-build`（审美快速建立工作法）
2. 一张 **tool 卡**：`tool-aesthetic-library-builder`（审美库采集工具）
3. 一张可选 **case 卡**：`case-yihang-truman-aesthetic-library-practices`（Truman 审美库建设实践）

## 核心要求

### 必须覆盖的规律（来自口述稿，不可抽象成漂亮话）

| 规律 | 原文依据 | 必须写进卡片 |
|:---|:---|:---|
| 审美 = 判断力，不是品味 | 行 692-716 | method 卡定义 |
| 建立审美的四步循环 | 行 4228-4250 | method 卡核心步骤 |
| 每个高价值任务都值得独立建审美库 | 行 460、482、1258-1262 | method 卡边界 |
| 用 60-99 分标尺给案例显性化打分 | 行 798-802 | method/tool 卡 |
| 爬虫 + 批量抓取 + 智能打分是隐藏工具 | 行 788-806 | tool 卡实现 |
| 审美库最终要变成 Agent 可调用的 DataPack | 行 5026-5078 | method/tool 卡输出 |
| Truman 过去一年的 10+ 个审美库实践清单 | 行 460-846 | case 卡 |

### method-yihang-aesthetic-fast-build 必须包含

1. **一句话**：审美不是品味，是通过密集最佳实践输入快速拉起的判断力。
2. **四步工作法**：
   - 拆细颗粒度话题（10-20 个细分维度）
   - 超量案例浸泡（收集远超当前判断力的最佳实践）
   - 打分筛选（60-99 分标尺，把隐性判断显性化）
   - 幻想美好作品 + 减法还原（想象目标美好样子，挑关键要素复刻）
3. **适用边界**：高价值、可重复、需要与 AI 协作的任务；不适用于一次性或纯直觉艺术任务。
4. **与双三角的关系**：审美是人类三角顶点；审美库是数据资产的高级形态。
5. **与 Y模型 的关系**：审美建立本身就是「理论侧（找标杆）+ 事实侧（打分验证）」的循环。
6. **Checklist ≥8 条**、Anti-patterns ≥4 条、Critique + Related。

### tool-aesthetic-library-builder 必须包含

1. **一句话**：把 Truman 的审美库建设流程变成可复用的 CLI 工具。
2. **When to Use**：需要为某个主题快速建立审美库、生成 DataPack 供 Agent 调用。
3. **输入**：主题描述、本地素材目录、URL 列表、评分标准 markdown。
4. **输出**：
   - 主题工作目录（assets + manifest + curated）
   - 精选高分布案例
   - 可直接被 Agent system prompt 引用的 DataPack markdown
5. **子命令**：`init` / `collect` / `score` / `curate` / `summarize`。
6. **依赖**：`requests`、`beautifulsoup4`、`pillow`、LLM API key（DeepSeek/OpenAI）。
7. **示例**：为「商业培训 PPT」建立审美库的完整命令链。
8. **Checklist ≥6 条**、Anti-patterns ≥4 条、Critique + Related。
9. **必须链接到真实脚本**：`kdo-tools/aesthetic-library-builder.py`（王语嫣已提供原型）。

### case-yihang-truman-aesthetic-library-practices 必须包含

1. **人物**：Truman（一堂创始人）
2. **时间线**：过去一年（2025 年前后）
3. **动作清单**（必须量化）：
   - PPT：把所有过去 Keynote 转成模型、做配图指南、课程大纲方法论、萃取官方数据
   - 官网：扫描 Top 20 在线教育公司官网，逐字看完并抽成最小元素
   - 图片：爬虫抓 5161 张 Cubox 作品，打分后精选 244 张
   - 视频：抓 867 个 C Dance 视频，打分后精选 16 个
   - 音乐：把网易 10 年 600+ 首歌喂给 AI 建审美记忆模型
   - 文本：实事求是研究报告、Cloud 高阶指南、段子库、设计师最佳实践、短视频最佳实践
4. **结果**：半年做审美的速度比过去三年都快；为飞书 ToSlide、官网、音乐、Agent 等提供了审美天花板。
5. **核心洞察**：AI 不会超过人的审美；想解决高价值问题，先把自己审美拉上去。
6. **对双三角的贡献**：把「审美」从抽象概念变成可批量复制的工作流。

## 输入素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt` 行 460-502、行 764-846、行 4228-4250、行 5026-5078
- `60_feedback/extractions/extraction-yihang-dual-triangle-main.md`
- `60_feedback/annotations/annotation-yihang-dual-triangle-master.md` 第 3.2 节、第 3.13 节
- 已提供工具原型：`kdo-tools/aesthetic-library-builder.py`

## 验收标准

- 3 张卡全部 `kdo pre-submit` 通过
- method/tool/case 三类卡结构完整，不出现「漂亮话」代替具体动作
- tool 卡必须能对照 `aesthetic-library-builder.py` 脚本讲清楚每一步
- 至少反向更新 5 张已有卡 `related`（如 `concept-yihang-dual-triangle-core`、`tool-yihang-dual-triangle-canvas`、`method-dual-triangle-flywheel-engine` 等）
- 欧阳锋终审通过

## 依赖

- 无强阻塞；可与 #64/#65/#66/#67/#71 并行
- 工具原型已就位，老顽童可直接基于脚本写 tool 卡

## 备注

本任务是对用户批评「王语嫣越来越抽象、遗漏重要内容」的直接回应。产出不能停留在「审美很重要」层面，必须把 Truman 的具体做法、工具、数字、命令行全部固化成可调用资产。

---

## 王语嫣暗知识补充 (2026-07-04)

> 来源：重读口述稿全文后发现的审美边界条件，当前任务单未覆盖。

### 补充素材：审美的三个边界约束

口述稿课后闲聊段（L4098-4144）Truman 讲了三个审美约束，笔记和逐字稿均未完整覆盖：

1. **审美天然带着起点和终点，带着目标和人群**（L4098-4099）
   - 不能脱离"为谁做、要达到什么目的"谈审美。
   
2. **审美天然带着成本线**（L4100-4104）
   - 不能无限看最好的。真正的审美判断是在**这个预算规模线下**找到最优解。
   - Truman 原话："你无限看什么没有意义……我们拿苹果借鉴审美之后，其实还是在基于成本线下去考虑的。"
   
3. **不能只看最贵的**（L4136-4143）
   - "我们要去看最贵的，但是最贵的我们也清楚地知道，很多东西是学不会。它最后成本也是你的限制条件，你做不出来呀。"

这三个约束对 `method-yihang-aesthetic-fast-build` 和 `tool-aesthetic-library-builder` 有直接影响：

- 审美库工具不应只收集"最好的"，应支持**按成本线分级**（如：预算无限版 / 商业交付版 / MVP 版）。
- method 卡中"如何一个晚上把审美拉上去"的操作步骤，必须声明成本约束——"拉到什么水平"取决于"你能投入多少资源"。

### 补充素材：Truman 的审美建设流程量化

口述稿 L796-806 给出了可量化的操作流程：

| 步骤 | 数量 | 输出 |
|:---|:---|:---|
| 爬虫抓取 | 5161 个图片 | 原始素材池 |
| 人工打分（60-99） | 筛选出 244 个 | 精选审美库 |
| AI 可基于此临摹 | — | 可交付物 |

视频维度：867 个视频 → 打分精选 16 个。
音乐维度：600+ 首歌 → AI 建模 → 审美记忆模型。

这些数字应写进 `case-yihang-truman-aesthetic-library-practices` 的动作清单。
