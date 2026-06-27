---
id: kdo-yaml-frontmatter-safety
title: "KDO YAML Frontmatter 安全操作指南"
type: concept
status: enriched
domain:
  - src_unknown
created_at: "2026-05-31"
updated_at: "2026-06-17"
target_roles:
  - src_unknown
  - src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
pipeline:
  - src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75
trust_level: medium
source_refs:
- src_unknown
source_context: 原始source无法追溯，已标记为src_unknown，待后续补充
diagnostic_signals:
  - src_unknown
    lens: "解析器错误"
    follow_up: "检查是否用yaml.safe_load()而非逐行解析，做round-trip校验"
  - src_unknown
    lens: "嵌套结构损坏"
    follow_up: "检查是否用yaml.dump()写嵌套结构，不要用json.dumps(str(value))"
  - src_unknown
    lens: "注释误解析"
    follow_up: "检查#开头的标签是否加引号：- \"#master\"而非- #master"
  - src_unknown
    lens: "round-trip失败"
    follow_up: "写文件前做round-trip校验：读回来确认嵌套结构无损"
---# KDO YAML Frontmatter 安全操作指南

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

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 开发/修改KDO流水线中的YAML frontmatter处理代码 |
| ✅ 适合 | 新建卡片或批量修改卡片元数据 |
| ✅ 适合 | 排查数据丢失或字段被拍平的bug |
| ❌ 不适合 | 纯内容编辑（不涉及frontmatter） → 无需关注YAML安全 |
| ❌ 不适合 | 使用KDO CLI正常读写（已内置安全处理） → 无需手动干预 |
| ❌ 不适合 | 非YAML格式文件（如纯txt/json） → 用对应格式解析器 |
| ❌ 不适合 | 紧急修复时跳过round-trip校验 → 宁可慢，不可错 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **手写解析器** | 逐行split(':')，嵌套结构丢失 | 统一用yaml.safe_load()，删除所有手写解析代码 |
| **Python repr输出** | dict渲染成{'key': 'val'}而非YAML | 嵌套结构用yaml.dump()，不用str(value) |
| **注释误解析** | #master标签变成null | 所有#开头值加引号："#master" |
| **跳过round-trip** | 写文件后直接上线，未验证读回 | 写文件前强制做round-trip校验，issues为空才通过 |
| **多行字符串截断** | 长文本未缩进，YAML解析失败 | 用\|-或>块标量处理多行字符串 |
| **类型推断错误** | "true"被识别为bool，"123"被识别为int | 需要字符串时显式加引号 |
| **冒号分隔误解析** | 字符串值中含:被当成新key:value | 含:的字符串值加引号包裹 |

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

- src_unknown
- src_unknown
- src_unknown

---

*欧阳锋 · 2026-05-31*
