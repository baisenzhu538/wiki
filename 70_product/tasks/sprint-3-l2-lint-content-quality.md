---
title: "Sprint 3 L2 内容质量 Lint"
type: task
status: completed
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


## 执行人疑问 (2026-05-10)

验证要求「检出三张模式 A 卡（five-step-method / scientific-method / fundraising）」，但当前 vault 的 `30_wiki/concepts/` 下无此三张卡片。检查结果：

- `five-step-method` — 无匹配文件
- `scientific-method` — 无匹配文件  
- `fundraising` — 无匹配文件

已按任务规则对全 vault 跑 `kdo lint`，四条 L2 规则均生效（+57 warnings），但无法验证「模式 A」具体卡片。请确认：缺失卡片是否需先通过 ingest 创建？或可用其他已有卡片替代验证？

## 欧阳锋回应 (2026-05-10)

卡片没丢，文件名有 `yt-` 前缀：

| 搜索词 | 正确路径 |
|------|------|
| five-step-method | `30_wiki/concepts/yt-entrepreneur-five-step-method.md` |
| scientific-method | `30_wiki/concepts/yt-entrepreneur-scientific-method.md` |
| fundraising | `30_wiki/concepts/yt-entrepreneur-fundraising.md` |

跑 `kdo lint --wiki-path 30_wiki/concepts/yt-entrepreneur-five-step-method.md` 验证单张能检出后再通知我。57 warnings = 规则已生效，确认三张都检出即可。
