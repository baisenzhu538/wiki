---
id: report_20260627_wikilink_gate_verification
type: verification-report
created_at: 2026-06-27
author: 黄药师
---

# Pre-Submit Wikilink Gate 验证报告

## 验证方法

创建包含 broken wikilink 的测试卡片，运行 `kdo pre-submit -f`。

## 结果

```
[WIKILINK]: 2 errors, 0 warnings
  Broken wikilink: [[nonexistent-file-xyz-123]] — no matching file found in vault
  Broken wikilink: [[also-missing]] — no matching file found in vault
Result: FAIL
```

## 结论

**Gate 已启用且正常工作。** 任何新增 broken wikilink 会让 pre-submit FAIL。无需修复。

Gate 包含两道 wikilink 检查：
1. 反斜杠检测（`\` in target → ERROR）
2. 存在性检测（target 不在 vault 中 → ERROR）
