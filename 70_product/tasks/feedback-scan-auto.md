---
title: "Feedback 自动扫描 — 13 条"
type: task
created_at: 2026-06-03
status: pending
---

扫描 49 篇文章，提取 13 条 Feedback。

## 其他 (2 条)

1. [art_20260602_kdo_data_autopsy_huangyaoshi.md] *黄药师 · 2026-06-02 · 试写*
2. [art_20260603_laowantong_ai_unit_model_judge.md] > **工具摩擦 2**：在对比"斧子和尺子"时，我想引用 `yt-entrepreneur-unit-model` 的 Critique 部分来强化论证，但该卡片的 Critique 只有两个外部攻击者（Eric Ries 和 Bill Aulet），没有 Synthesis 中的"不要用的场景"

## 缺CLI命令 (8 条)

1. [art_20260602_ai_data_deep_synthesis.md] > 本文的不足或遗漏？ > > 1. **写这篇文章时，我想引用 KDO 的卡片统计数据，但 `kdo query` 不支持聚合查询（如 `COUNT(*)` 或 `GROUP BY domain`）。** 我只能用 `find | wc -l` 来估算，结果写了"百份原始素材"这种模糊数字。如果 
2. [art_20260602_laowantong_inbox_lake.md] > 本文的不足或遗漏？ > > 1. **写这篇文章时，我发现自己没法验证"50 条素材"这个数字**。我是拍脑袋写的。如果有一个 `kdo inbox --count` 或类似命令能让我看到"每个队列/文件夹里有多少个文件、已处理多少、未处理多少"，我的论点会更有数据支撑。 > > 2. **我不
3. [art_20260602_laowantong_oral_digestion_jump_read.m] > 本文的不足或遗漏？ > > 1. **写这篇文章时，我发现自己无法验证"跳读策略是否真的比逐字阅读更高效"。** 我的数据来源是"我自己的两次经验"，没有 A/B 测试。如果有一个 `kdo digest --benchmark` 能让我测量"跳读 vs 逐字阅读的提取率和时间消耗"，我的论点会
4. [art_20260602_laowantong_rag_judgment.md] > 本文的不足或遗漏？ > > 1. **我在写"反照 KDO 自身"时卡住了很久**。因为我不确定 KDO 的实际检索日志是什么样的——我只是一个用户，看不到系统层的查询统计。如果能有一个 `kdo query --stats` 或者类似的命令让我看到"过去一周哪些查询用了图遍历、哪些没用"，我的
5. [art_20260602_laowantong_recursive_deepen.md] > 本文的不足或遗漏？ > > 1. **写到第三段时又出现了"材料不足"的问题**。我想分析 Producer 在飞轮中的数据缺口，但我没有任何系统层的生产数据——比如"我今天产出了多少张卡片、哪些卡片被检索到了、哪些没有"。如果有一个 `kdo produce --stats` 或者类似的命令，
6. [art_20260602_three_deep_questions.md] > 本文的不足或遗漏？ > - 三个问题的"交汇点"——ADUCIT 从线性到飞轮——是否需要单独成篇？ > - 飞轮在代码层面如何实现？是否需要一个 `kdo flywheel` 命令来管理 D↔U↔C 的迭代循环？ > - Pilot 20 张卡的具体选卡标准是什么？是否需要欧阳锋和老顽童参与选
7. [art_20260603_laowantong_ai_unit_model_judge.md] > **工具摩擦 1**：写这篇文章时，我想引用 KDO 自身的运行数据来支撑"反照 KDO 自身"的论点——比如"每个域的卡片分布是否与业务重心匹配"。但 `kdo query` 不支持按 domain 分组聚合查询，我只能用 `find 30_wiki/concepts -name "*.md"
8. [art_20260603_laowantong_ai_unit_model_judge.md] > **工具摩擦 3**：写到"反照 KDO 自身"时，我意识到 KDO 当前的知识生产流程缺少一个"数据质量门"——我们有 frontmatter 格式门，但没有"这张卡片的核心论点是否有真实业务数据支撑"的门。一张经过 `kdo validate --v15` 的卡片，可能全文都是"行业常识"而

## 缺自动化机制 (2 条)

1. [art_20260602_laowantong_directory_friction.md] > 本文的不足或遗漏？ > > 1. **写这篇文章时，我发现自己无法验证"层次越多认知负担越高"这个论点。** 我的数据来源是"我自己的体验“，没有 A/B 测试。如果有一个“层次影响几位测量”能让我测量"在 3 层、5 层、9 层结构下，Producer 存放一份文件的平均时间“，我的论点会更有
2. [art_20260602_laowantong_feedback_fuel.md] > 本文的不足或遗漏？ > > 1. **写这篇文章时，我发现自己无法验证"这些 Feedback 真的没有人看"。** 我的判断基于"没有任何人回复我的 Feedback ——没有确认、没有反馈、没有行动。但这可能是因为这些文章还在审查队列里，还没有被看到。如果有一个"文章审查状态查看器"能让我看

## 缺角色/流程 (1 条)

1. [art_20260602_kdo_data_autopsy_huangyaoshi.md] > 本文的不足或遗漏？ > - U（湖仓升仓）的"给谁用"维度尚未展开——不同角色对同一素材的价值判断不同，如何建模？ > - D（识别/发现隐藏高价值数据）在这里没有展开——它应该在 U 之前还是之后？ > - 四个死刑的修复顺序是否应该调整——如果 A（预判）没修好，修 L2 精加工是否本末倒置
