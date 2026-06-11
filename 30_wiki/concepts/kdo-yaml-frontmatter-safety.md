---
id: "kdo-yaml-frontmatter-safety"
title: "KDO YAML Frontmatter 安全操作指南"
type: "concept"
status: "draft"
domain:
  - "master"
created_at: 2026-05-31
updated_at: 2026-05-31
target_roles:
  - "黄药师（Builder）"
  - "欧阳锋（Architect）"
related:
  - "fix-data-curator-parse-bug"
  - "gold-standard-manual-labels"
tags:
  - #scene/agent-infrastructure/skill-registry
  - #scene/knowledge-management/tagging
pipeline:
  - confidence-draft
---

# KDO YAML Frontmatter 安全操作指南

> **背景**：2026-05-31 Data Curator Phase 2 Clean 因手写 YAML 解析器导致 `visual_analysis` 4 图→5 字符串、`related` 4 链接→`level: intermediate` 的数据丢失。教训：**不要手写 YAML 解析器，用标准库**。

---

## 核心原则

1. **永远用 `yaml.safe_load()` 读，不要手写逐行解析**
2. **永远用 `yaml.dump()` 写嵌套结构，不要用 `json.dumps(str(value))`**
3. **写文件前做 round-trip 校验：读回来确认嵌套结构无损**
4. **`#` 在 YAML 中是注释标记，标签值必须加引号**（如 `- "#master"` 而非 `- #master`）

---

## 读 frontmatter

### ✅ 正确做法

```python
import yaml

def read_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter safely."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    raw = text[4:end]
    try:
        meta = yaml.safe_load(raw)
        if not isinstance(meta, dict):
            return {}
        # Replace None values with empty string
        for k, v in list(meta.items()):
            if v is None:
                meta[k] = ""
        return meta
    except yaml.YAMLError:
        return {}
```

### ❌ 错误做法（逐行解析，已踩坑）

```python
# ❌ 以下代码无法解析 YAML 列表、嵌套 dict、深层结构
for line in raw.splitlines():
    if ":" not in line:
        continue
    key, val = line.split(":", 1)
    metadata[key.strip()] = val.strip()
# visual_analysis 会被拍平，related 列表会丢失
```

---

## 写 frontmatter

### ✅ 正确做法：标量用内联，嵌套用 yaml.dump

```python
import yaml

def render_frontmatter(metadata: dict) -> str:
    """Render metadata dict to YAML frontmatter string."""
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, (list, dict)):
            # 嵌套结构用 yaml.dump
            yaml_str = yaml.dump(
                {key: value},
                default_flow_style=None,
                allow_unicode=True,
                sort_keys=False,
            ).strip()
            lines.append(yaml_str)
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif value is None:
            lines.append(f"{key}: null")
        elif isinstance(value, str) and (":" in value or value.startswith("#")):
            lines.append(f"{key}: \"{value}\"")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"
```

### ❌ 错误做法（Python repr 输出）

```python
# ❌ 以下代码会把 dict 渲染成 Python repr: {'map': 'personal'}
# 而不是合法的 YAML: map: personal
lines.append(f"{key}: {value}")  # 当 value 是 dict 时，输出 "{'map': 'personal'}"
```

---

## Round-trip 校验

**每次写文件前，必须确认 frontmatter 能无损读回来：**

```python
def check_roundtrip(metadata: dict) -> list[str]:
    """Check if metadata survives render→parse round-trip without data loss."""
    rendered = render_frontmatter(metadata)
    reparsed, _ = parse_frontmatter(rendered)
    issues = []
    for key in metadata:
        if key not in reparsed:
            issues.append(f"Key '{key}' lost in round-trip")
        elif type(metadata[key]) != type(reparsed[key]):
            issues.append(
                f"Key '{key}' type changed: {type(metadata[key]).__name__} "
                f"→ {type(reparsed[key]).__name__}"
            )
    return issues
```

---

## 常见陷阱

| 陷阱 | 表现 | 修复 |
|:-----|:-----|:-----|
| `- #master` 作 list item | YAML 把 `#master` 当成注释，值为 null | 加引号：`- "#master"` |
| dict 值用 Python repr | 输出 `{'key': 'val'}` 而非 `key: val` | 用 `yaml.dump()` |
| 多行字符串不缩进 | YAML 解析截断 | 用 `|-` 或 `>` 块标量 |
| 手写推断类型 | `"true"` 被识别为 bool | 用 YAML 原生的类型推断 |
| `:` 在字符串值中 | 被解析为新的 key:value | 加引号包裹 |
| `visual_analysis` 类嵌套结构 | 解析为扁平 dict 或列表 | 必须用 `yaml.safe_load()` |

---

## KDO 各文件的 frontmatter 处理现状

| 文件 | 使用的解析器 | 状态 |
|:-----|:------------|:----:|
| `kdo/workspace.py` | `yaml.safe_load()` + `yaml.dump()` | ✅ 已修复 2026-05-31 |
| `clean_cards.py`（独立脚本） | `yaml.safe_load()` | ✅ 已修复 2026-05-31 |
| `kdo/commands/curation.py` | 调 `workspace.parse_frontmatter` | ✅ 间接修复 |
| `kdo/commands/label.py` | 只读 tag-registry（`yaml.safe_load`）+ 不重写卡片 | ✅ 无风险 |

---

## 参考

- `[[30_wiki/decisions/fix-data-curator-parse-bug]]` — 原始 bug 报告与修复方案
- `[[30_wiki/decisions/gold-standard-manual-labels]]` — 受影响的案例

---

*欧阳锋 · 2026-05-31*
