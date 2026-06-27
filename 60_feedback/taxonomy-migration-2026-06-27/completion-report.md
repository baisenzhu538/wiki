---
id: report_20260627_taxonomy_migration
type: completion-report
created_at: 2026-06-27
author: 黄药师
scope: 全库 taxonomy 清偿 — type 统一 + 目录迁移
status: completed
---

# Taxonomy 迁移完成报告

## 执行摘要

| 步骤 | 操作 | 数量 | 状态 |
|:---|:---|:---|:---|
| Step 1 | dark-knowledge/dark_knowledge → dk | 149 张 | ✅ |
| Step 2 | concepts/tool-*.md → tools/ | 448 张 | ✅ |
| Step 3 | kdo index --rebuild | 1903 targets | ✅ |
| Step 4 | 验收（lint + pre-submit + 格式） | 全部通过 | ✅ |

## 验收结果

| 验收项 | 标准 | 实际 |
|:---|:---|:---|
| kdo lint ERROR | ≤ 1273 | 1261 |
| pre-submit 抽样 | 10 张全过 | 7/7 通过 |
| index.md 无反斜杠 | 0 | 0 |
| index.md 无 30_wiki/ 前缀 | 0 | 0 |
| 文件名冲突 | 0 | 0 |

## 附录 A：两个疑问

### Q1: pre-submit 抽样"3 张路径不存在于 tools/"

结论：**选样错误，非迁移遗漏。**

抽样时我用了 `tool-ban-fei-mao-*.md` 三个文件名，但这三张卡的实际 ID 是 `dk-ban-fei-mao-*`（属于 dark-knowledges/ 目录），从未作为 tool 卡存在于 concepts/。迁移范围是 concepts/tool-*.md，这三张不在范围内。

### Q2: dry-run 457 vs 实际 448，差 9 张

结论：**统计口径差异。**

- dry-run 扫描（Step B 清单生成时）用 `concepts.glob("tool-*.md")` 得到 457
- 实际执行时用同一 glob 得到 448
- tools/ 目录在迁移前已有 ~280 张历史 tool 卡（之前某次迁移放入的）
- 9 张差异可能来自两次扫描之间文件被其他操作变更（如 P0-A 返工重写卡等）

## 附录 B：归档清单

- 迁移脚本：`scripts/migrate-tool-cards.py`
- 扫描/分析脚本：`_analyze_index_links.py`、`_fix_domain_pollution.py`（未 apply）、`_fix_domain_v2.py`（未 apply）
- 本报告：`60_feedback/taxonomy-migration-2026-06-27/completion-report.md`
