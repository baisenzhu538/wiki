---

id: dk-foresight-source-material-blindness
title: 暗知识：素材命名不一致导致完整口述稿被遗漏
type: dk
dark_knowledge_type: process-failure
domain:
- src_unknown
source_refs:
- 10_raw/sources/src_20260619_833c79d5_60_feedback_corrections_corr_20260611_laowantong_机会预判域_OCR遗漏_旧卡未清理.md
- 10_raw/sources/src_20260619_ad98829e_60_feedback_corrections_corr_20260611_hongqigong_机会预判域_OCR流程盲区.md
status: enriched
confidence: 0.95
difficulty: beginner
estimated_tokens: 1200
language: zh-CN
created_at: 2026-06-11
review_date: 2026-06-11
reviewed_by:
- src_unknown
- laowantong
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
wiki_refs:
- src_unknown
pipeline:
- src_unknown
- src_unknown
author: 欧阳锋
trust_level: medium-high
updated_at: '2026-06-16'
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---# 暗知识：素材命名不一致导致完整口述稿被遗漏

## 症状

机会预判域18张PNG幻灯片（`一堂-机会预判-*.png`）被完整OCR并写卡，但同域的核心文本素材——189KB的完整口述稿（`一堂-商业预判课-Truman-口述.txt`）——完全未被发现和使用。

结果：8张新卡全部基于幻灯片写成，卡片深度停留在"看图说话"水平，遗漏了口述稿中的大量结构化论述、案例细节、反例和论证逻辑。

## 根因

**搜索依赖文件名模式匹配，而非内容主题匹配。**

- src_unknown
- src_unknown

"机会预判"和"商业预判课"是同一个域的不同命名——Truman在课程中交替使用这两个词。但文件名不一致导致文件名搜索漏掉了核心素材。

## 正确做法

1. **新域素材消化的第一步不是"看文件名"，而是"搜内容"**——`grep -r "预判\|光谱\|终局\|机会" --include="*.txt" --include="*.md"` 全库搜索主题词
2. **文件名的搜索范围必须包括同义词**——"机会预判"≈"商业预判"≈"预判课"≈"forecast"≈"foresight"
3. **搜索完文件名后，必须搜索内容**——文件名是人起的，内容主题才是机器能找到的
4. **搜索范围不只是 `00_inbox/`**——`10_raw/sources/` 里可能已有已摄入的文本素材

## 关联事件

- src_unknown
- src_unknown

## 预防机制

- src_unknown
- src_unknown
- src_unknown

## Synthesis

- src_unknown
- src_unknown
