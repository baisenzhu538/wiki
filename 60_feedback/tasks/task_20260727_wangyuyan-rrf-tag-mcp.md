---
id: task_20260727_wangyuyan-rrf-tag-mcp
task_id: 212
assignee: huangyaoshi
status: in_progress
created_at: 2026-07-27
domain: system
priority: P0
source: 60_feedback/diagnosis/diag_20260726_huangyaoshi-index-pipeline-upgrade.md
  (黄药师建议书·第二+三层)
updated_at: '2026-07-26T16:58:12.725578+00:00'
---

# RRF tag维度匹配 + MCP标签暴露

## 背景

#208完成了第一层（索引感知元数据）。但tag打了只是"能被搜到"——还不能"按维度智能排序"。小昭搜"CEO怎么设计分钱规则"需要RRF根据tags维度决定排序，而非只靠BM25关键词匹配。

## 第二层：RRF融合增加tag维度匹配

改动 `KDO/commands/delivery.py` → `_rrf_fuse()`：

```
if card.tags 包含 "audience:ceo" and query 含 "CEO/战略/决策":
  score += 额外 boost
if card.tags 包含 "scene:diagnosis" and query 含 "怎么做/步骤/操作":
  score += 额外 boost
```

效果：小昭搜"CEO该怎么设计分钱规则"→ tags `audience:ceo` + `scene:diagnosis` 双命中 → 地位互换测试卡排第一。

## 第三层：MCP Tool返回tags字段

改动 `kdo-tools/mcp/tools.py` → `search()` + `onboard()`：

返回结果加 `tags` 和 `aliases` 字段。小昭不需要 `kdo_read` 全文就能判断卡片适用性。

## 验收

1. `kdo query "CEO怎么设计分钱规则"` → 坏世界研究卡（tags: audience:ceo, scene:diagnosis, method:collaboration）排序在前
2. MCP `kdo_search` 返回含tags字段
