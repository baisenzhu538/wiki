---
id: pending_unknown
title: 待补充链接（占位符）
type: system
domain:
  - meta
status: placeholder
author: system
reviewed_by: system
confidence: 0
trust_level: placeholder
created_at: 2026-06-28
updated_at: 2026-06-28
related: []
---

# 待补充链接（占位符）

> **此卡为系统占位符，不是真实知识卡片。** 当某张卡片的 `related` 字段或正文链接无法推断目标卡片时，使用 `[[pending_unknown]]` 作为临时占位，待后续人工补充真实链接后替换。

## 用法

- 在 frontmatter `related` 字段中：`- [[pending_unknown]]`
- 在正文 Synthesis section 中：`- 待补充链接`（纯文本形式，避免触发 wikilink 检查）

## 替换规则

1. 高置信度推荐（≥0.8）→ 直接替换为真实 wikilink
2. 中置信度推荐（0.5-0.8）→ 人工判断是否替换
3. 无法推断 → 保留 `[[pending_unknown]]`，标注为待补充