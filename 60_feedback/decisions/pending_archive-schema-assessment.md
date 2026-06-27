---
id: dec_20260627_pending_archive_schema
type: decision_memo
created_at: 2026-06-27
author: 黄药师
scope: 评估 kdo 是否支持 pending_archive 机制保留缺失来源信息
confidence: 0.95
---

# pending_archive Schema 评估

## 问题

source_refs 中有 ~884 条指向磁盘上不存在的文件。直接降级为 `src_unknown` 会丢失原始路径信息。王语嫣建议引入 `pending_archive:<原始路径>` 格式保留来源线索。

## 当前 Schema

source_refs 是 `list[str]`，YAML frontmatter 示例：

```yaml
source_refs:
  - src_20260606_640c2818
  - 10_raw/sources/xxx.md
```

无类型约束，任意字符串合法。

## Lint 检查点

`_lint_source_refs_exist`（workspace.py:867）有三种解析路径：

| 路径 | 条件 | 失败行为 |
|:---|:---|:---|
| state.json 查找 | ref 在 source_locations | ERROR: file not found |
| 直接文件路径 | ref 含 `/` 或以 `.md` 结尾 | ERROR: file not found |
| source ID glob | ref 不匹配上述 | WARNING: not found |

## 结论：**需要改代码，但改动量极小。**

只需在 `_lint_source_refs_exist` 的三个检查路径前各加一行 skip：

```python
ref = ref.strip()
# NEW: skip pending_archive entries — they're intentionally unresolved
if ref.startswith("pending_archive:"):
    continue
```

改动量：**1 行代码**，零 schema 变更。

## 建议格式

```
source_refs:
  - pending_archive:00_inbox/战略专题/冉鹏战略课录屏_ocr.md
  - src_20260606_640c2818
```

lint 看到 `pending_archive:` 前缀 → 跳过存在性检查。人类/Agent 看到前缀 → 知道这曾经指向某个文件，可以事后补归档。

## 是否支持

| 维度 | 结论 |
|:---|:---|
| Schema 兼容 | ✅ 不需要改，source_refs 已是 list[str] |
| Lint 兼容 | ⚠️ 需加 1 行 skip 逻辑 |
| 向后兼容 | ✅ 不影响现有功能 |
| 人类可读 | ✅ 保留原始路径线索 |

**总评：可以支持。** 批准后 5 分钟改完。

## 实施记录

- 2026-06-27：已实现。`_lint_source_refs_exist`（workspace.py:897）加 `pending_archive:` 前缀跳过逻辑。
- lint ERROR: 884 → 862（pending_archive 条目不触发错误）
- 状态：**implemented**

