---
id: dk-foresight-source-material-blindness
title: 暗知识：素材命名不一致导致完整口述稿被遗漏
type: dark-knowledge
dark_knowledge_type: process-failure
domain:
- yitang
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
- 黄药师
- laowantong
query_triggers:
- 素材遗漏
- 命名不一致
- 搜索盲区
- 口述稿没找到
- 文件名搜索
wiki_refs:
- '[[yt-foresight-15-char-mantra]]'
pipeline:
- confidence-source-cited
- confidence-verified-by-incident
author: 欧阳锋
trust_level: medium-high
updated_at: '2026-06-16'
---
# 暗知识：素材命名不一致导致完整口述稿被遗漏

## 症状

机会预判域18张PNG幻灯片（`一堂-机会预判-*.png`）被完整OCR并写卡，但同域的核心文本素材——189KB的完整口述稿（`一堂-商业预判课-Truman-口述.txt`）——完全未被发现和使用。

结果：8张新卡全部基于幻灯片写成，卡片深度停留在"看图说话"水平，遗漏了口述稿中的大量结构化论述、案例细节、反例和论证逻辑。

## 根因

**搜索依赖文件名模式匹配，而非内容主题匹配。**

- 幻灯片命名模式：`一堂-机会预判-*.png`
- 口述稿命名：`一堂-商业预判课-Truman-口述.txt`

"机会预判"和"商业预判课"是同一个域的不同命名——Truman在课程中交替使用这两个词。但文件名不一致导致文件名搜索漏掉了核心素材。

## 正确做法

1. **新域素材消化的第一步不是"看文件名"，而是"搜内容"**——`grep -r "预判\|光谱\|终局\|机会" --include="*.txt" --include="*.md"` 全库搜索主题词
2. **文件名的搜索范围必须包括同义词**——"机会预判"≈"商业预判"≈"预判课"≈"forecast"≈"foresight"
3. **搜索完文件名后，必须搜索内容**——文件名是人起的，内容主题才是机器能找到的
4. **搜索范围不只是 `00_inbox/`**——`10_raw/sources/` 里可能已有已摄入的文本素材

## 关联事件

- **P-7（OCR强制检查遗漏）**：同一批素材的另一个流程失败——即使找到了18张PNG，也没跑OCR。两个失败叠加：先没找到文本素材，找到了图片素材又没OCR。
- **P-9（Glob漏扫子目录）**：同一个模式——单一工具/单一搜索维度的阴性结果被当成了"不存在"。

## 预防机制

- [ ] 新域素材消化的第一步改为：`grep` 全文搜索主题词 → 按内容聚类 → 再看文件名
- [ ] `kdo lint` 增加检测：如果 card source_refs 全部是 `.png` 且无 `.txt`/`.md`，WARN "可能遗漏了文本源素材"
- [ ] 写卡模板增加自检：`source_refs` 中是否包含口述稿/笔记/文本素材（不仅是图）？

## Synthesis

- [[dk-note-rookie-disaster-veteran-heaven]] — 同一个模式的另一个案例：新手按文件名找 vs 老兵按内容找
- dk-yt-checklist-max-common-divisor — AI和人类在素材处理上的分工：AI更适合做"全量内容搜索"这类不怕累的活
