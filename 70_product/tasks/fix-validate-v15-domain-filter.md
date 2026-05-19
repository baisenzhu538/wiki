---
id: fix-validate-v15-domain-filter
title: "修复 kdo validate --v15 的 --domain 过滤失效"
status: pending
priority: P1
assigned_to: 黄药师
reviewer: 欧阳锋
created: 2026-05-19
depends_on: quality-gate-automation-v15
---

## 问题

`_read_frontmatter()` 用单行正则 `^(\w[\w_-]*):\s*(.*)` 提取 frontmatter，无法处理多行 YAML 列表格式。

当前 vault 中 domain 字段三种格式分布：

| 格式 | 示例 | 数量 |
|------|------|------|
| 多行 YAML 列表 | `domain:\n  - yitang` | 168 张 |
| 单行 Python 列表 | `domain: ['yitang']` | ~15 张 |
| 单行简单值 | `domain: yitang` | ~12 张 |

`--domain yitang` 预期命中 ~140 张，实际只命中 7 张。

## 修复位置

`kdo/commands/quality.py` → `_read_frontmatter()` 函数（第 301-318 行）

## 修复要求

`_read_frontmatter` 返回值改为 `dict[str, list[str]]`，`domain` 字段统一解析为字符串列表：

- `domain: yitang` → `["yitang"]`
- `domain: ['yitang']` → `["yitang"]`
- `domain:\n  - yitang` → `["yitang"]`
- `domain:\n  - yitang\n  - master` → `["yitang", "master"]`

修改 `cmd_validate_v15` 中 domain 过滤逻辑：
```python
# 改前
if args.domain and fm.get("domain", "") != args.domain:

# 改后
if args.domain and args.domain not in fm.get("domain", []):
```

`type` 字段也存在同样问题（`type: tool` vs `type:\n  - tool`），一并修。

## 验证

```bash
# 修复前：7 张
kdo validate --v15 --domain yitang | head -3

# 修复后：应返回 ~140 张
kdo validate --v15 --domain yitang | head -3

# type 过滤不变（102 张 tool）
kdo validate --v15 --type tool | head -3

# pytest 无回归
pytest tests/ -q
```

## 不做

- 不引入 PyYAML 依赖（保持零外部依赖）
- 不改动 `_read_frontmatter` 的返回值给其他调用方（检查是否有，如有则适配）
