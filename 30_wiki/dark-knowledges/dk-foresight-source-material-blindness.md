---
id: dk-foresight-source-material-blindness
title: 暗知识：素材命名不一致导致完整口述稿被遗漏
type: dk
dark_knowledge_type: process-failure
domain:
- yitang
aliases:
- 命名不一致导致完整口述稿被遗漏
- 暗知识
- 暗知识：素材命名不一致导致完整口述稿被遗漏
- 素材命名不一致导致完整口述稿被遗漏
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
trust_level: high
updated_at: '2026-06-16'
discoverable_by:
- 暗知识：素材命名不一致导致完整口述稿被遗漏
- 暗知识
- 素材命名不一致导致完整口述稿被遗漏
related:
- '[[tool-yitang-supply-chain-research]]'
- '[[dk-ji-hao-logs-fastest-ignored]]'
- '[[dk-ji-hao-ai-cant-design-structure]]'
- '[[yt-five-step-method]]'
- '[[dk-tool-as-phased-validator]]'
- '[[dk-wanghuan-output-equals-standard-times-iteration]]'
- '[[yitang-domain-digest]]'
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
- 旧卡未清理
- 机会预判域
- 流程盲区
---

# 暗知识：素材命名不一致导致完整口述稿被遗漏

## 原始表述

机会预判域18张PNG幻灯片（`一堂-机会预判-*.png`）被完整OCR并写卡，但同域的核心文本素材——189KB的完整口述稿（`一堂-商业预判课-Truman-口述.txt`）——完全未被发现和使用。

结果：8张新卡全部基于幻灯片写成，卡片深度停留在"看图说话"水平，遗漏了口述稿中的大量结构化论述、案例细节、反例和论证逻辑。

**根因**：搜索依赖文件名模式匹配，而非内容主题匹配。"机会预判"和"商业预判课"是同一个域的不同命名——Truman在课程中交替使用这两个词。但文件名不一致导致文件名搜索漏掉了核心素材。

## 使用场景

- **新域素材消化**：新域素材消化的第一步不是"看文件名"，而是"搜内容"
- **文件名搜索**：文件名的搜索范围必须包括同义词
- **内容搜索**：搜索完文件名后，必须搜索内容
- **素材库管理**：搜索范围不只是 `00_inbox/`，`10_raw/sources/` 里可能已有已摄入的文本素材
- **团队协作**：多人协作时，统一命名规范或建立同义词映射

## 操作方法

1. **内容优先搜索**：
   - `grep -r "预判\|光谱\|终局\|机会" --include="*.txt" --include="*.md"` 全库搜索主题词
   - 先搜内容，再搜文件名
2. **同义词映射**：
   - "机会预判"≈"商业预判"≈"预判课"≈"forecast"≈"foresight"
   - 建立同义词映射表，避免遗漏
3. **全库搜索范围**：
   - 搜索范围包括 `00_inbox/` 和 `10_raw/sources/`
   - 文件名是人起的，内容主题才是机器能找到的
4. **素材审查流程**：
   - 新域素材消化前，先全库搜索主题词
   - 确认没有遗漏核心素材后再开始写卡

## 适用边界

| 场景 | 是否适用 | 说明 |
|:
|:---|:---|
| 新域素材消化 | ✅ 适用 | 必须先搜内容再搜文件名，避免遗漏核心素材 |
| 文件名搜索 | ✅ 适用 | 搜索范围必须包括同义词 |
| 内容搜索 | ✅ 适用 | 文件名是人起的，内容主题才是机器能找到的 |
| 素材库管理 | ✅ 适用 | 搜索范围不只是 `00_inbox/`，`10_raw/sources/` 也可能有素材 |
| 团队协作 | ✅ 适用 | 统一命名规范或建立同义词映射 |
| 单一素材来源 | ⚠️ 部分适用 | 素材来源单一，遗漏风险较低 |

## 为什么值钱

1. **避免核心素材遗漏**：文件名不一致导致核心素材被遗漏，影响卡片深度
2. **提升卡片质量**：基于完整素材写卡，避免"看图说话"水平
3. **系统化搜索**：内容优先搜索比文件名搜索更可靠
4. **团队协作**：统一命名规范或同义词映射，避免协作中的遗漏

## 与其他知识的关联

- [[dk-ji-hao-logs-fastest-ignored]]——纪浩日志管理，素材管理是日志管理的一部分
- [[dk-ji-hao-ai-cant-design-structure]]——纪浩 AI 不会搞结构设计，素材管理需要人设计结构
- [[yt-five-step-method]]——一堂五步法，系统化素材管理框架
- [[dk-tool-as-phased-validator]]——分阶段校验器，素材审查是验证的一部分
- [[dk-wanghuan-output-equals-standard-times-iteration]]——输出=标准×迭代，素材质量是标准的一部分

---

## 失败模式 / 常见走偏

| 失败模式 | 症状 | 纠正 |
|:---|:---|:---|
| 只看文件名 | 文件名不一致导致核心素材遗漏 | 先搜内容再搜文件名 |
| 忽略同义词 | "机会预判"和"商业预判课"被视为不同域 | 建立同义词映射表 |
| 只搜 `00_inbox/` | `10_raw/sources/` 里的素材被遗漏 | 全库搜索，包括所有素材目录 |
| 依赖文件名模式匹配 | 搜索依赖文件名模式匹配，而非内容主题匹配 | 内容优先搜索 |
| 素材审查缺失 | 新域素材消化前未审查素材完整性 | 建立素材审查流程，确认无遗漏后再写卡 |
