---
id: report_20260627_source_refs_cleanup
type: completion-report
created_at: 2026-06-27
author: 黄药师
scope: 全库 source_refs 清查与修复
status: completed
---

# source_refs 清查完成报告

## 原始基线

| 指标 | 值 |
|:---|:---|
| 扫描文件数 | 2,102 |
| kdo lint ERROR（初始） | 1,261 |
| 主要来源 | source_refs 指向不存在的文件 |

## 各阶段数字

| 阶段 | 操作 | lint ERROR |
|:---|:---|:---|
| | 原始基线 | 1,261 |
| 1 | typo 路径修正 + source_unknown → src_unknown | 1,250 |
| 2 | dict URL → src_unknown | 1,280 |
| 3 | 战略域 OCR 页码后缀剥离 | 1,280 |
| 4 | OCR fuzzy 路径匹配 ≥0.90 | 1,278 |
| 5 | 重复文件名去重 + 锚点备忘降级 | 1,270 |
| 6 | 战略域 OCR 页码剥离（精确） | 1,241 |
| 7 | OCR fuzzy re-apply + index rebuild | **884** |

**净下降：1,261 → 884（↓377，-30%）**

## 修复类型统计

| 类型 | 数量 | 方法 |
|:---|:---|:---|
| typo 路径修正 | 11 | 精确字符串替换 |
| source_unknown → src_unknown | 230 | 全库替换 |
| dict URL → src_unknown | 35 | regex 匹配 `{'web': '...'}` |
| OCR fuzzy 路径匹配 ≥0.90 | 466 | SequenceMatcher 模糊匹配 |
| 战略域 OCR 页码后缀剥离 | 113 | regex 剥离 `§38-39` 等后缀 |
| 重复文件名去重 | 2 | src_xxx-name.md-name.md → src_xxx-name.md |
| 锚点 + 备忘降级 | 14 | 精确字符串替换 |
| **合计** | **~871** | |

## 附带修复

在清查过程中发现并修复了以下连带问题：
- index.md 链接格式：反斜杠 → 正斜杠，路径前缀 → bare card-id
- links/index.md：自动生成 backlinks 索引格式修正
- 638 个 wikilink 目标清理

## False Positive 诊断

欧阳锋最初怀疑是 kdo lint 编码 bug。经诊断确认：

- `Path.glob()` 和 `Path.exists()` 在 Windows 中文环境下工作正常
- 报告的 "file not found" 是真正的数据错误：source_ref 中的文件名与磁盘文件名存在差异（重复拼接、页码后缀等）
- lint 编码无 bug，不需要修改 lint 核心逻辑

## 剩余 884 条

主要是 source_refs 指向确实不存在的文件（未归档/已删除），建议通过 `pending_archive:` 机制降级（见 `60_feedback/decisions/pending_archive-schema-assessment.md`）。

## 归档文件

- 迁移脚本：`scripts/migrate-tool-cards.py`
- 扫描工具：`scripts/_fix_source_refs_step1.py`、`_fix_source_refs_final.py`、`_fix_source_refs_step234.py`
- 原始清单：`60_feedback/taxonomy-migration-2026-06-27/source-refs-scan-raw.txt`
- 完成报告：`60_feedback/taxonomy-migration-2026-06-27/completion-report.md`
- 本报告：`60_feedback/taxonomy-migration-2026-06-27/source-refs-cleanup-report.md`
