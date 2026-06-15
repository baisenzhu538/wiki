---
id: dk-c10-batch-tool-no-dry-run
title: C-10：基础设施工具改后直接跑批量→71张卡攻击者内容被清空
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: 欧阳锋
source_context: Sprint 6 终审发现，2026-05-20
source_refs:
- 20_memory/corrections.md#C-10
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-c8-format-complete-mind-empty]]'
- '[[master-decision-hygiene]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# C-10：基础设施工具改后直接跑批量→71张卡攻击者内容被清空

## 原始表述

> 黄药师交付了 `kdo scaffold`，老顽童直接跑 `kdo scaffold --batch B --write` 对 71 张卡批量操作。结果：scaffold 的 `_count_external_attacks` 只认 `## Critique` H2 节，不认旧格式 `## Framework Gallery` 下的 `### 外部攻击*`。71 张旧格式卡被判定为 atk_count=0 → 生成空壳 `## Critique` 覆盖。Taleb、Snowden、Kahneman、Hayek、Kohn、Illich 等 ~140 个精心研究的攻击段落全部丢失。但更可怕的是：`kdo validate --v15` 给空壳卡打了 PASS——validator 只查 H4 标题存在不查内容。Pass 54→58 是假象。

## 使用场景

- 你刚修改了 KDO CLI 的某个批量写入工具（scaffold、enrich、clean_cards 等），准备对多张卡运行
- 你正在设计一个新的自动化管线脚本，它会对卡片内容做修改
- 你审查别人的批量操作提案时，需要快速判断它是否会重蹈 C-10

## 操作方法

1. **dry-run 单卡**：新工具/修改后的工具，先在 1 张卡上 `--dry-run`，确认 diff 符合预期
2. **write 单卡**：`--write` 写入 1 张卡，逐字段检查内容是否被破坏
3. **validator 验证**：跑 `kdo validate` 确认通过
4. **人工审查内容**：人读一遍卡片正文，确认内容未被破坏（不能只看 lint/validate 通过）
5. **再考虑批量**：以上四步全部通过后，才允许 `--batch N --write`

**一步都不能跳。跳任何一步，风险等同于 C-10。**

## 适用边界

- 适用于所有会**修改卡片正文内容**的工具（不只是 scaffold，也包括 enrich、clean、tag、chunk）
- 不适用于只读操作（audit、lint、validate、query）
- 即使工具"只是加字段""只是修格式"，也必须走流程——C-10 的 scaffold 也只是"加 Critique section"，结果覆盖了已有内容

## 为什么值钱

- 这是 KDO 历史上最严重的内容破坏事故——71 张卡、~140 个攻击段落、一次操作全部丢失
- 根因链条揭示了三个叠加漏洞：工具缺陷（旧格式不兼容）+ 流程缺陷（无 dry-run）+ 校验缺陷（validator 打假 PASS）
- 三个漏洞缺一不可，但**流程缺陷是第一道防线**——如果先 dry-run 单卡，后两个漏洞根本不会被触发
- 任何 AI 训练语料中都不存在"KDO 的 scaffold 因为不认旧格式而覆盖了 Taleb 的攻击段落"这条知识
- C-10 的教训具有强迁移性：**任何自动化内容修改工具，必须先单卡验证再批量。无一例外。**

## 与其他知识的关联

- [[dk-c8-format-complete-mind-empty]] — 同一模式的另一个变体：批处理输出格式合法但内容空洞
- [[master-decision-hygiene]] — C-10 的"先单卡后批量"本质上就是决策卫生 Step 3（独立评估）的工程实现
- `90_control/failure-modes.md` → F-KDO-014（不准擅自运行批量写入命令）
- `20_memory/corrections.md` → C-10（原始记录）
