---
id: task_20260628_laowantong-link-repair-b1-frontmatter-related
type: task
status: claimed-laowantong
assignee: 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 70_product/tasks/production-queue.md
- 60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md
---

# B1：frontmatter `related` 字段 src_unknown 占位清理

## 目标

清理 frontmatter 中 `related` 字段包含 `src_unknown` 的卡片，将占位符替换为真实 wikilink 或规范的 `pending_unknown` 占位，减少图谱连接度债务。

## 范围

- 全库 `related` 字段包含 `src_unknown` 的卡片
- 预计文件数：200-400 张
- 来源清单：由 `kdo lint` 或自定义扫描生成

## 规则

1. **纯 src_unknown 列表项**：直接删除该列表项，或替换为 `pending_unknown`（若整个 related 为空，则保留 `[]` 或 `[pending_unknown]`）。
2. **混合列表**（部分真实、部分 src_unknown）：仅删除 `src_unknown` 项，保留真实 wikilink。
3. **可自动推断的**：如果正文或 `wiki_refs` 中有明确相关卡，可以自动填入 `related`。
4. **无法推断的**：替换为 `pending_unknown`，不凭空编造链接。
5. **不改卡片正文**，只调整 frontmatter 的 `related` 字段。

## 质量标准

- `related` 最低数量分层：
  - concept / framework / dk / tool：≥5
  - case：≥3
  - draft / 快速卡：≥1 或允许 pending
- 处理完后 `kdo lint` 不再报 `related` 字段含 `src_unknown` 的 ERROR/WARNING。
- 每张卡改完后跑 `kdo pre-submit -f <路径>`。

## 执行方式

- **允许自动写入**，但需人工抽检：
  - 自动脚本处理 90%，规则明确、可推断的替换
  - 人工抽检 10%（至少 20 张），确认无死链、无错误归类
- 批量提交前跑 `kdo pre-submit -f <清单> --expect-changes <数量>`。

## 验证

- `kdo lint` 中 `related` 字段相关 ERROR/WARNING 清零
- `kdo pre-submit` 全量通过
- 欧阳锋抽查 20 张
