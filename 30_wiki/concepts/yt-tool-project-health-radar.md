---
id: yt-tool-project-health-radar
created_at: 2026-05-31
domain:
- yitang
status: redirect
title: 项目健康度雷达
type: tool
diagnostic_signals:
- signal: 访问者是否被正确重定向到目标页面
  framework_lens: 重定向 / 信息架构
  follow_up_question: 目标页面 [[30_wiki/tools/yt-tool-project-health-radar]] 是否存在且最新？
- signal: 本卡是否不再作为决策依据使用
  framework_lens: 信息时效 / 单点真相
  follow_up_question: 是否有人仍在引用本 redirect 卡的旧内容做决策？
updated_at: '2026-06-16'
author: legacy
reviewed_by: pending
confidence: 0.75
trust_level: medium
source_refs:
- source_unknown
source_context: （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
---
> 本卡已迁移至 30_wiki/tools/yt-tool-project-health-radar。
>
> 原文内容请访问目标页面。

## Constraints & Boundaries

| 边界 | 适用 | 不适用 |
|---|---|---|
| 使用目的 | 告知本卡已迁移 | 作为原主题参考/决策依据 |
| 信息来源 | 仅指向目标页面 | 替代目标页面内容 |
| 维护责任 | 目标页面维护 | 本卡不再更新 |

### Common Failure Modes
1. **继续引用 redirect 卡** → 症状：做决策时只看了本卡；原因：未注意到迁移提示；修复：点击目标链接查看最新内容
2. **目标页面失效或陈旧** → 症状：链接打不开或内容过时；原因：目标页面未维护；修复：检查目标页面并更新链接

