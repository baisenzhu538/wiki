---

id: pending_unknown
title: 待补充链接（占位符）
type: system
domain:
  - meta
status: placeholder
author: system
reviewed_by: 欧阳锋
confidence: 0
trust_level: placeholder
created_at: 2026-06-28
updated_at: 2026-06-28
related: []
source_refs:
- pending_archive: src_unknown
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
## 补充说明

该文件记录了「待补充链接（占位符）」的相关内容。从知识管理的角度看，这类信息需要经过结构化提炼才能有效复用。

### 核心要点

1. **概念理解**：待补充链接（占位符）的核心定义和关键要素，需要在具体场景中理解其适用边界。
2. **实践应用**：在实际工作中，该知识点可以帮助团队更好地理解和解决问题。
3. **关联知识**：与一堂方法论体系中的其他模块存在关联，建议结合上下文理解。

### 注意事项

- 知识卡片的价值在于复用，而非记录本身——需要在实践中验证和迭代。
- 不同场景下的适用性可能不同，使用前需确认前提条件是否满足。
- 建议定期回顾和更新，确保知识与实际业务保持同步。
