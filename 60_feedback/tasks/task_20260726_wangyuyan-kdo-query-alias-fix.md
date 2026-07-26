---
id: task_20260726_wangyuyan-kdo-query-alias-fix
task_id: 208
assignee: huangyaoshi
status: queued
created_at: 2026-07-26
domain: system
priority: P0
---

# kdo query 别名索引修复

## 问题

三张坏世界研究卡已正确标注 `aliases: ["坏世界研究"]`。`kdo query "坏世界"` 返回0命中。根因：kdo query 检索索引不覆盖 aliases 字段。与#203暴露的source_refs管道断裂同类。

## 修复

kdo query 索引管道加入 aliases 字段——title + content + **aliases** + domain。aliases 权重与 title 同级。

## 验收

`kdo query "坏世界"` → 命中三张卡。
