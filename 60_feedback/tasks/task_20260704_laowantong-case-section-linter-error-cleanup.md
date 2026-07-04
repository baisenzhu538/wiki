---
id: task_20260704_laowantong-case-section-linter-error-cleanup
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-04
updated_at: '2026-07-04T18:20:47.640236+00:00'
source_task: task_20260629_kimi-lint-content-debt-by-domain
related:
- '[[case-yihang-dual-triangle-beike-ai-outbound]]'
reviewed_by: 欧阳锋
review_date: '2026-07-04'
---

# 任务 #96：linter 规则升级暴露的 56 张 case 卡标准 section 补全

## 背景

kdo linter 规则更新：case 卡缺少 4 个标准 section（`## 关键证据`/`## 可迁移场景`/`## 教训`/`## 失败模式`）从 WARNING 升级为 ERROR。56 张老 case 卡被暴露——这些卡在规则变更前就已存在，之前的审查基于旧规则。

**与 WorkBuddy #28 WARNING 清理无关**——ERROR 增长是 linter 规则变更导致，不是 WorkBuddy 引入的回归。#28 继续跑，不打断。

## 任务

为 56 张 case 卡补齐 4 个标准 section：

| Section | 处理方式 |
|:---|:---|
| `## 关键证据` | 有素材→填充；无素材→`待补充（src_unknown）` |
| `## 可迁移场景` | 有素材→填充；无素材→`待补充（src_unknown）` |
| `## 教训` | 有素材→填充；无素材→`待补充（src_unknown）` |
| `## 失败模式` | 有素材→填充；无素材→`待补充（src_unknown）` |

## 约束

- **非空不覆盖**：已有内容的 section 不改动
- **draft 卡可占位**：VLM draft 卡无素材的，用 `src_unknown` 占位，不强行编造
- **reviewed 卡优先**：优先处理 status=reviewed 的 case 卡（如有），这些是之前审查漏掉的

## 验收

- 56 张卡 `kdo lint` case section ERROR 清零
- `kdo pre-submit` 通过
- 欧阳锋抽检 5 张

## 依赖

- 无阻塞。P2，排在 #91/#93 等 P0/P1 主线任务之后
