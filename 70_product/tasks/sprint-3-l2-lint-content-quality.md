---
title: "Sprint 3 L2 内容质量 Lint"
type: task
status: todo
priority: high
domain:
  - kdo
sprint: 3
source_refs:
  - "30_wiki/decisions/kdo-ec-industrialization-migration-proposal.md"
created_at: "2026-05-10"
tags:
  - "#kdo"
  - "#sprint"
---
# Sprint 3 L2 内容质量 Lint

> 审批人：欧阳锋 | 执行人：黄药师

## 任务

在 `kdo/workspace.py` 的 `lint_workspace()` 中新增 L2 内容质量检查：

1. **Condense 实质性** — ≥3 条以 `- ` 开头且含中文有内容的行 → 不足 P1 warning
2. **Critique 指名假设** — 含「具体假设」「边界」「反例」「前提」至少一个 → 一个都没 P1 warning
3. **Synthesis wikilink** — `[[...]]` ≥2 个，无 self-link → 不足或自指 P1 warning
4. **全文字数** — >500 字
5. 全部只输出 warning，不阻断

## 验证

写完对 vault 跑一次，确认能检出三张模式 A 卡（five-step-method / scientific-method / fundraising）。改完通知欧阳锋复审。

## KDO 源码根

`C:\Users\Administrator\Knowledge Delivery OS 0.0.1\`
