---
id: task_20260726_wangyuyan-kdo-query-alias-fix
task_id: 208
assignee: huangyaoshi
status: queued
created_at: 2026-07-26
domain: system
priority: P0
implementation: 见 60_feedback/diagnosis/diag_20260726_huangyaoshi-index-pipeline-upgrade.md (黄药师建议书·三层改动：aliases 3x + tags 2x + discoverable_by 2x)
---

# kdo query 索引管道全面修复

## 问题

`kdo query` 当前只索引 title + content。最近三周铺开的三个关键元数据字段全部不被索引：

| 字段 | 何时加入 | 索引？ | 后果 |
|:--|:--|:--|:--|
| aliases | 早期 | ❌ | 坏世界研究搜不到（alias已写） |
| discoverable_by | #201 | ❌ | Agent触发词不命中 |
| tags | #206 Phase1 | ❌ | 多维分类搜不到 |

不是个别卡片的问题——所有元数据优化都在卡片层，查询管道没跟上。

## 修复

索引管道升级为：**title + content + aliases + discoverable_by + tags + domain**

权重：title = aliases > discoverable_by > tags > content

## 验收

1. `kdo query "坏世界"` → 命中三张卡
2. `kdo query "如何系统创新"` → 命中闪电模型（discoverable_by已有此触发词）
3. `kdo query "method:thinking-tool"` → 命中对应标签卡
