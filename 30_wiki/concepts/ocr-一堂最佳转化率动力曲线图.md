---
title: "OCR: 一堂最佳转化率动力曲线图"
type: "concept"
status: "enriched"
source_refs: ["src_20260522_9557e4cb"]
created_at: "2026-05-21T20:13:56+00:00"
updated_at: "2026-05-22T07:24:30+00:00"
---



# OCR: 一堂最佳转化率动力曲线图

## Summary

原图: `00_inbox/一堂最佳转化率动力曲线图.

png` 一堂最佳转化率·动力三曲线 堂 YitangMotivationBoosting·Three-CurVeModel 名 互惠  Reciprocation Reputation 葉 葉 承诺一致 利 Commitmentand Consistency 社会认同 Benefit SocialProof 权 喜好 Right Liking 权威 情 Authority Emotion 稀缺 Scarcity 内在驱动力 外在影响力 DrivingForce Influence F.

利益 Feature Advantage Benefit 核心说服 一堂・坚持只做必修课 扫码辛苦学3天，不扫弯路走3年 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解

## Source Refs

- `src_20260522_9557e4cb` -> `10_raw/sources/src_20260522_9557e4cb-ocr-一堂最佳转化率动力曲线图.md`

## Reusable Knowledge

- 一堂最佳转化率动力模型包含三条核心曲线：内在驱动力、外在影响力和核心说服路径。
- 外在影响力基于西奥迪尼六大影响力原则：互惠、承诺一致、社会认同、喜好、权威、稀缺。
- 内在驱动力对应FAB销售法则：特性(Feature)、优点(Advantage)、利益(Benefit)。
- 说服设计需同时激活内在动机与外在影响力，形成双重驱动。
- 模型强调"核心说服"作为必修环节，暗示转化优化应聚焦关键路径而非分散投入。

## Open Questions

- 该模型的三条曲线（内在驱动力、外在影响力、核心说服）之间的具体作用机制与优先级关系是什么？是串联、并联还是动态交互？
- "核心说服"作为"必修环节"的判定标准是什么？如何量化区分"核心"与"非核心"说服要素？
- 西奥迪尼六大影响力原则与FAB法则的映射关系是否经过实证验证，还是仅为概念拼贴？
- 模型名称中的"最佳转化率"是否有对应的A/B测试数据或基准对照组支持，还是属于宣称性用语？
- OCR提取的"名/葉/权/情"等单字与六大原则的对应关系（如"名"对应互惠、"葉"对应承诺一致）是否符合原图视觉布局，是否存在误识导致的概念错位？
- "扫码辛苦学3天，不扫弯路走3年"这一行动号召的具体转化数据（扫码率、完课率、实际转化率）是否被追踪，如何证明该模型优于其他说服框架？
- 模型的适用边界未明确：该框架针对的是低涉入决策（如扫码）还是高涉入决策（如高价课程购买），不同情境下三条曲线的权重是否应调整？

## Output Opportunities

Content: <article: "一堂转化率动力模型的批判性拆解与验证框架" — 分析性文章，将OCR提取的"三曲线模型"与西奥迪尼影响力原则、FAB法则进行概念溯源，建立可证伪的评估维度表，回应Open Questions中关于"概念拼贴vs实证验证"的核心质疑>
Code: <script: `yitang-model-validator.py` — 工具脚本，输入一堂课程截图OCR文本，自动检测六大影响力原则与FAB要素的标注完整性，输出结构化解构报告（含置信度评分与缺失项标记），辅助判断模型是系统框架还是营销包装>
Capability: <workflow: "OCR知识资产入库校验流水线" — 整合PaddleOCR ONNX双模Skill与KDO协议，定义从图片→OCR提取→人工校对→结构化YAML→交叉引用→Open Questions生成的标准作业程序，解决视觉结构丢失与概念错位问题>
