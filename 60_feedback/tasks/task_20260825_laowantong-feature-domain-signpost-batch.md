---
id: 526
assignee: laowantong
status: queued
updated_at: '2026-08-24T20:10:00+00:00'
version: v0.1
instance: laowantong
code_files:
  - 10_raw/ocr-cards/ocr-一堂-ai学习-truman自用的ai-featureset.md
  - 30_wiki/frameworks/framework-truman-feature-layered-system.md
  - 30_wiki/frameworks/framework-truman-feature-thinking-core.md
  - 30_wiki/bridges/bridge-two-feature-systems.md
  - 30_wiki/domains/ai-basic-domain-digest.md
  - 30_wiki/dark-knowledges/dk-analogy-blinds-search.md
---

# #526 Feature 域入口路标收尾批（盲测报告建议 1/2/3/7 + 类比遮蔽 dk 卡）

- **任务号**：#526
- **状态**：queued
- **assignee**：laowantong（内容批；欧阳锋批次验收）
- **优先级**：P2（入口层收尾——低成本高收益，盲测同口径复测预期全绿）
- **立项**：2026-08-25 王语嫣（小昭《KDO知识库检索检测报告与建设建议》裁定；老朱对齐确认+每日一问节奏拍板）

## 背景

老朱自然语言盲测 4 问（小昭仅 grep/glob/read）：第 1 问「feature 有哪些怎么分类」未命中周期表框架卡（无声的错误=拿到 30% 答案自以为完整）。根因=入口层缺路标：OCR 转录卡 related 空、自然问法未注册、两套 Feature 体系无澄清、digest 无资产地图。原件在 inbox 三处落点（AI-study/paddle_batch/ocr_ingest），检索者从哪层进来哪层就要有路标。

## 任务

1. **转录卡挂链**：`10_raw/ocr-cards/ocr-一堂-ai学习-truman自用的ai-featureset.md` 补 related→framework-truman-feature-layered-system；正文加指路行（自用精简版 30+ vs 完整周期表 100/L0-L5，数据源 v1.0.json）
2. **inbox 三处副本指路注释**：`00_inbox/AI-study/一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.txt`、`00_inbox/paddle_batch/同名.md`、`00_inbox/ocr_ingest/src_ocr_一堂_AI学习_truman自用的AI_FeatureSet.md` 各加一行指路（轻量注释，不改原内容）
3. **问法回填 discoverable_by**（复用 #315 模式）：layered-system 卡增 `truman的feature分类`/`feature有哪些`/`feature怎么分`/`周期率表`（笔误也收）；feature-thinking-core 卡增 `feature思维`/`T型F型`/`feature和工具的区别`
4. **澄清卡** `bridge-two-feature-systems`：cap_hub/features.json（KDO 工程 Feature）vs feature-periodic-table（AI 能力 Feature）一句话区分+互指，防 grep 互相污染
5. **digest 路标**：`30_wiki/domains/ai-basic-domain-digest.md` 头部加「本域核心资产路标」（Feature 思维根卡/周期表/v1.0.json/feature_menu.py）
6. **dk 卡** `dk-analogy-blinds-search`：类比遮蔽检索——比喻带来「已理解」错觉跳过实体验证；发现者署名小昭（消费端贡献首例），实证=本次盲测第 1 轮

## 边界

- 只加路标/挂链/回填，不改资产本体内容；OCR 卡维持 10_raw 层不升 30_wiki（流转规范：OCR 默认 10_raw，trust=low）
- 问法回填只收本次实证问法，不臆造同义词

## 验收

- 复测第 1 轮问法（grep「truman feature 分类」类自然问法）能经任一层路标到达 layered-system 框架卡（附检索路径输出）
- 澄清卡/dk 卡过欧阳锋批次验收（dk 卡走三方法口径按 P2 卡从简）
- 欧阳锋终审
