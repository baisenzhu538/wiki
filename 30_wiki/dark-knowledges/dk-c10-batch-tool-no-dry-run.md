---

id: dk-c10-batch-tool-no-dry-run
title: C-10：基础设施工具改后直接跑批量→71张卡攻击者内容被清空
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: 欧阳锋
source_context: Sprint 6 终审发现，2026-05-20
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- [[dk-small-format-error-cascades-to-system-failure]]
- [[dk-f4-wrong-workdir]]
- [[dk-infrastructure-guardrails-over-checklist]]
- [[dk-c8-format-complete-mind-empty]]
- [[modeling-to-kdo-toolchain]]
- [[dk-c8-format-complete-mind-empty]]
- [[master-decision-hygiene]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown# C-10：基础设施工具改后直接跑批量→71张卡攻击者内容被清空
---
## 原始表述/核心洞察

> 黄药师交付了 `kdo scaffold`，老顽童直接跑 `kdo scaffold --batch B --write` 对 71 张卡批量操作。结果：scaffold 的 `_count_external_attacks` 只认 `## Critique` H2 节，不认旧格式 `## Framework Gallery` 下的 `### 外部攻击*`。71 张旧格式卡被判定为 atk_count=0 → 生成空壳 `## Critique` 覆盖。Taleb、Snowden、Kahneman、Hayek、Kohn、Illich 等 ~140 个精心研究的攻击段落全部丢失。但更可怕的是：`kdo validate --v15` 给空壳卡打了 PASS——validator 只查 H4 标题存在不查内容。Pass 54→58 是假象。

核心洞察：**任何会修改正文内容的自动化工具，必须先单卡验证、再批量执行；validator 通过不等于内容安全**。C-10 是三重漏洞叠加——工具缺陷（旧格式不兼容）+ 流程缺陷（无 dry-run）+ 校验缺陷（validator 打假 PASS）——但流程缺陷是第一道防线，单卡 dry-run 本可以阻止后续两个漏洞被触发。

## 使用场景

- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **dry-run 单卡**：新工具/修改后的工具，先在 1 张卡上 `--dry-run`，确认 diff 符合预期
2. **write 单卡**：`--write` 写入 1 张卡，逐字段检查内容是否被破坏
3. **validator 验证**：跑 `kdo validate` 确认通过
4. **人工审查内容**：人读一遍卡片正文，确认内容未被破坏（不能只看 lint/validate 通过）
5. **再考虑批量**：以上四步全部通过后，才允许 `--batch N --write`

**一步都不能跳。跳任何一步，风险等同于 C-10。**

## 适用边界

- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 跳过 dry-run 直接批量写入 | 工具改动后立刻跑 `--batch --write` | 误以为"只是加字段/修格式"不会破坏正文 | 新工具或改动后，先在 1 张卡上 `--dry-run` 并核对 diff |
| 把 validator PASS 当安全证明 | `kdo validate` 绿灯即放行 | validator 只查字段/标题存在，不查语义或内容完整性 | 人工读一遍单卡正文，确认关键段落未被覆盖或清空 |
| 旧格式兼容未验证 | 新工具只认新 H2，旧格式 H3/H4 内容被忽略 | 解析逻辑未覆盖历史格式或边缘结构 | dry-run 时故意挑 1 张旧格式卡，检查其 diff 是否正常 |
| 批量权限缺乏审批/复核 | 单个人即可对大批量卡片执行 `--write` | 缺少分级管控或双人复核机制 | 批量写入前增加审批节点，关键域引入双人复核 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
