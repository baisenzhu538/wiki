---
id: task_20260628_laowantong-lint-batch2-dk-sections
type: task
status: in_progress
assignee: WorkBuddy 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 90_control/.tmp/lint_20260628_1620.log
- 90_control/.tmp/lint_batch2_dk_section.json
---

# lint Batch 2-B：dark-knowledge 卡 section 标准化（43 文件）

## 目标

补齐 43 张 dk 卡缺失的标准 section，使 `kdo lint` 不再报 `Dark knowledge card missing section` 类 ERROR。

## 范围

需补齐以下 6 个 section（文件清单见 `90_control/.tmp/lint_batch2_dk_section.json`）：

- `## 原始表述`（Truman/来源人物的原话）
- `## 使用场景`（什么情况下用这个暗知识）
- `## 操作方法`（具体怎么操作）
- `## 适用边界`（什么时候不适用）
- `## 为什么值钱`（公开语料中为什么找不到）
- `## 与其他知识的关联`（链接到其他卡片（至少1张概念卡+1张暗知识卡））

预计影响文件：**约 43 张 dk 卡**，其中 40 张六 section 全缺。

> **含 Batch1 复查追加文件**：这 43 张 dk 卡中，有若干来自 `hermes_lint_safe_batch_remaining.json`（原标记为 `colon_in_scalar_other` 的 125 个文件）。这些文件 frontmatter 已修复，当前暴露 `Dark knowledge card missing section` 错误，一并纳入本任务。

## 规则

1. **优先从正文中萃取内容填入对应 section**，不要凭空编造。
2. 正文已有信息但无 section 的，把信息归类后移入 section，保留原文要点。
3. 缺失原话的，用 `src_unknown` 占位并标注 `待补充来源原话`。
4. `与其他知识的关联` 至少放 1 个 concept wikilink + 1 个 dk wikilink；没有的用 `src_unknown` 占位。
5. 每张卡改完后跑 `kdo pre-submit -f <路径>`。

## 验证

- 全部 43 张 dk 卡 `kdo lint` 不再报 `Dark knowledge card missing section`。
- 每张卡 `kdo pre-submit` 通过。

## 输出

完成后在本任务单末尾写执行报告。
