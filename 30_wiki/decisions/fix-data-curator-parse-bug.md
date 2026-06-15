---
id: fix-data-curator-parse-bug
title: Data Curator Phase 2 Clean — parse_frontmatter 修复方案
type: improvement-plan
status: pending
domain:
- master
created_at: 2026-05-31
updated_at: '2026-06-16'
target_roles:
- 黄药师（Builder）
reviewer: 欧阳锋（Architect）
related:
- '[[plan_20260531_data-curator-v1]]'
- '[[gold-standard-manual-labels]]'
- '[[kdo-15-dimension-label-spec]]'
author: legacy
source_context: KDO internal record （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
source_refs:
- source_unknown
reviewed_by: pending
confidence: 0.75
trust_level: medium
---
# Data Curator Phase 2 Clean — parse_frontmatter 修复方案

> **报告人**：欧阳锋  
> **执行人**：黄药师  
> **优先级**：P0（阻塞 Pilot 启动）  
> **修复预期**：30-60 分钟（代码修改 10 分钟 + 重新跑 20 分钟 + 验证 10 分钟）

---

## 一、问题摘要

`clean_cards.py` 的 `parse_frontmatter()` 是一个**手写的逐行 YAML 解析器**（193 行），只能处理平面键值对和一层嵌套，遇到 `visual_analysis` 这种"列表内嵌 dict"结构时，把 4 张图 20+ 条结构化描述拍成了 5 条扁平字符串。**3 张图 15 条分析丢失**。

另：`yt-model-aesthetic-progression.md` 的 `related` 字段被从 4 个链接覆盖为 `level: intermediate`。

**根因**：重复造轮子。Python 标准库就有 `yaml.safe_load()`，不需要手写 YAML 解析器。

---

## 二、修复步骤

### Step 0：备份

```powershell
# 备份受损文件（两步保险）
Set-Location "C:\Users\Administrator\Desktop\wiki"
$backupDir = "60_feedback/data-quality/backups/parse-bug-20260531"
mkdir $backupDir -Force

# 备份已知受损的两张卡
Copy-Item "30_wiki/concepts/yt-decision-y-model.md" "$backupDir/yt-decision-y-model.md.bak"
Copy-Item "30_wiki/concepts/yt-model-aesthetic-progression.md" "$backupDir/yt-model-aesthetic-progression.md.bak"
```

---

### Step 1：替换 `parse_frontmatter` — 用 `yaml.safe_load()` 替代手写解析

**文件**：`40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py`

**删除**：整个 `parse_frontmatter()` 函数（行 69-165）  
**替换为**：

```python
import yaml

def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter using proper YAML parser. Returns (metadata, body, raw_frontmatter)."""
    text = text.replace("\r\n", "\n")
    if text.startswith("﻿"):
        text = text[1:]
    if not text.startswith("---\n"):
        return {}, text, ""

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, ""

    raw_fm = text[4:end]
    body = text[end + 5:]

    try:
        metadata = yaml.safe_load(raw_fm)
    except yaml.YAMLError as e:
        print(f"  [WARN] YAML parse error in frontmatter: {e}", file=sys.stderr)
        return {}, text, ""

    if not isinstance(metadata, dict):
        return {}, text, raw_fm

    # Normalize None values to empty string
    for k, v in list(metadata.items()):
        if v is None:
            metadata[k] = ""

    return metadata, body, raw_fm
```

**关键改动**：
- 用 `yaml.safe_load()` 替代 97 行手写逻辑
- `yaml.safe_load()` 原生支持：YAML 列表、嵌套 dict、多级嵌套、JSON 兼容标量
- 不再需要 `current_key` / `current_list` 状态机

---

### Step 2：修复 `render_frontmatter` — dict 值渲染支持嵌套结构

**文件**：同上，`render_frontmatter()` 函数（行 353-390）

当前 `render_frontmatter` 的 dict 分支（行 372-378）：

```python
elif isinstance(value, dict):
    lines.append(f"{key}:")
    for k, v in value.items():
        if isinstance(v, str):
            lines.append(f"  {k}: {v}")
        else:
            lines.append(f"  {k}: {v}")
```

**问题**：只处理一层嵌套。如果 dict 的值是另一个 dict 或 list，会输出非法的 YAML。

**替换为**：

```python
elif isinstance(value, dict):
    # Use yaml.dump for nested dicts to handle arbitrary depth
    dict_yaml = yaml.dump(value, default_flow_style=False, allow_unicode=True).strip()
    lines.append(f"{key}:")
    for sub_line in dict_yaml.split("\n"):
        lines.append(f"  {sub_line}")
```

这样 `visual_analysis` 这类复杂嵌套结构会被 `yaml.dump` 正确地序列化为多级 YAML。

---

### Step 3：回滚受损文件

```powershell
Set-Location "C:\Users\Administrator\Desktop\wiki"

# 回滚已知受损的两张卡
git restore --source=HEAD~2 "30_wiki/concepts/yt-decision-y-model.md"
git restore --source=HEAD~2 "30_wiki/concepts/yt-model-aesthetic-progression.md"
```

`HEAD~2` 是 Data Curator Clean 前的版本（已用 `git show` 验证，那时这两张卡的 frontmatter 完好）。

> **为什么不用 `git checkout`**：当前工作目录的 git 是 auto-backup 模式，不能用 `git checkout` 切分支。用 `git restore --source=<commit>` 可以从特定 commit 恢复单个文件。

---

### Step 4：全量扫描受损清单

修复 `parse_frontmatter` 后，找出其他可能受损的文件：

```python
# scan_corrupted.py — 在修复后的 clean_cards.py 基础上
# 遍历 353 个修改文件，用 yaml.safe_load() 重新解析 frontmatter
# 对比 round-trip 前后的一致性

import sys
import yaml
from pathlib import Path

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"

def check_frontmatter_integrity(filepath: Path) -> list[str]:
    """Check if frontmatter survives round-trip without data loss."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return []
    
    end = text.find("\n---\n", 4)
    if end == -1:
        return []
    
    raw_fm = text[4:end]
    issues = []
    
    try:
        metadata = yaml.safe_load(raw_fm)
    except yaml.YAMLError as e:
        issues.append(f"YAML parse error: {e}")
        return issues
    
    if not isinstance(metadata, dict):
        issues.append("Frontmatter is not a dict after parse")
        return issues
    
    # Check for known-bug patterns
    for key, value in metadata.items():
        if isinstance(value, dict):
            # Check if dict has keys starting with "- " (pregenerated list-as-dict)
            for k in value:
                if k.startswith("-") and len(value) > 1:
                    issues.append(f"Field '{key}' appears to be flattened list-as-dict ({len(value)} items)")
                    break
        elif isinstance(value, list):
            # Check if list items are strings that look like dimension descriptions
            str_items = [i for i in value if isinstance(i, str) and ":" in i]
            if len(str_items) >= 3 and len(str_items) == len(value):
                issues.append(f"Field '{key}' has {len(str_items)} string items with ':' — may be flattened structured data")
    
    return issues

# Check all files modified by Data Curator
affected = []
for f in sorted(CONCEPTS_DIR.glob("*.md")):
    issues = check_frontmatter_integrity(f)
    if issues:
        affected.append((f, issues))
        print(f"\n⚠ {f.stem}")
        for issue in issues:
            print(f"  {issue}")

print(f"\n\nTotal: {len(affected)} file(s) with potential issues")
```

运行方式：
```powershell
python scan_corrupted.py
```

---

### Step 5：重新跑 Clean（修复后）

```powershell
# 在修复 parse_frontmatter 和 render_frontmatter 后
Set-Location "C:\Users\Administrator\Desktop\wiki"
python "40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py" --batch 353 --dry-run
# 确认 dry-run 无异常
python "40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py" --batch 353 --write --no-backup
```

---

### Step 6：验证修复

```powershell
# 1. 检查已知受损文件已恢复
Set-Location "C:\Users\Administrator\Desktop\wiki"
python -c "
import yaml
text = open('30_wiki/concepts/yt-decision-y-model.md', encoding='utf-8').read()
fm = yaml.safe_load(text.split('---')[1])
va = fm.get('visual_analysis', [])
print(f'visual_analysis items: {len(va)}')
for item in va:
    if isinstance(item, dict):
        print(f'  - image: {item.get(\"image\", \"?\"[:40])}')
        dims = item.get('dimensions', [])
        print(f'    dimensions: {len(dims)}')
"

# 预期输出：
# visual_analysis items: 4
#   - image: 一堂-科学决策-决策三角形.png
#     dimensions: 5
#   - image: 一堂-科学决策-一堂双三角磨合追求.png
#     dimensions: 5
#   - image: 一堂-科学决策-关键假设ABCD模型.png
#     dimensions: 0
#   - image: 一堂-科学决策-项目方案评估三角形.png
#     dimensions: 10
```

```powershell
# 2. 全量 round-trip 完整性校验
python -c "
import yaml
from pathlib import Path
ok = fail = 0
for f in Path('30_wiki/concepts').glob('*.md'):
    text = f.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---\n'):
        continue
    end = text.find('\n---\n', 4)
    if end == -1:
        continue
    raw = text[4:end]
    try:
        d = yaml.safe_load(raw)
        if isinstance(d, dict):
            ok += 1
        else:
            fail += 1
            print(f'FAIL: {f.stem}')
    except:
        fail += 1
        print(f'PARSE ERROR: {f.stem}')
print(f'OK={ok} FAIL={fail}')
"
# 预期输出：OK=380+ FAIL=0
```

---

### Step 7：全量测试确认无回归

```powershell
Set-Location "C:\Users\Administrator\Knowledge Delivery OS 0.0.1"
python -m pytest tests/ -v --tb=short
# 预期：413+ passed, 0 failed
```

---

## 三、文件修改汇总

| 文件 | 改动 | 行数预估 |
|------|------|:-------:|
| `clean_cards.py` `parse_frontmatter()` | 97 行手写解析 → 调用 `yaml.safe_load()`（~20行） | **-80 行** 🎉 |
| `clean_cards.py` `render_frontmatter()` dict 分支 | 6 行 → 用 `yaml.dump()` 处理嵌套（~5行） | **不变** |
| `scan_corrupted.py`（新增） | 全量扫描验证脚本 | +60 行 |
| 回滚 `yt-decision-y-model.md` | git restore | 无损 |
| 回滚 `yt-model-aesthetic-progression.md` | git restore | 无损 |

净减少 80 行手写代码 + 正确性大幅提升。**手写 YAML 解析器是一个已经踩过的坑——不要再造。**

---

## 四、为什么不用 `yaml.safe_load()`？

| 对比 | 手写 parser | `yaml.safe_load()` |
|------|------------|-------------------|
| 行数 | 97 行 | 1 行 |
| 支持列表 | ⚠️ 一层 | ✅ 任意嵌套 |
| 支持嵌套 dict | ⚠️ 一层 | ✅ 任意深度 |
| 支持列表内 dict | ❌ | ✅ |
| 支持多行字符串 | ❌ | ✅ |
| 处理日期格式 | 手写 regex | ✅ 原生支持 |
| 安全性 | 安全（纯文本） | `safe_load()` 安全 |
| Python 依赖 | 无（self-contained） | `PyYAML`（已在 requirements 中） |

`clean_cards.py` 顶部已有 `import json` 但没引入 yaml。Python 标准库没有 `yaml`，但 KDO 的 `pyproject.toml` 依赖中已有 `PyYAML`（`tag_cards.py` 和 `label.py` 都在用 `import yaml`）。所以没有新增依赖。

---

## 五、时间线

| 步骤 | 预估 | 谁做 |
|:----:|:----:|------|
| Step 1-2：改代码 | 10 min | 黄药师 |
| Step 3：回滚 | 2 min | 黄药师 |
| Step 4：全量扫描 | 5 min | 黄药师 |
| Step 5：重新跑 Clean | 20 min | 黄药师 |
| Step 6：验证 | 5 min | 黄药师 |
| Step 7：全量测试 | 30 min | 黄药师 |
| **复审** | 10 min | **欧阳锋** |
| **总计** | **~80 min** | |

修复通过复审后，Pilot 启动。

---

## 六、防呆：提交前校验

在 `clean_cards.py` 的 `clean_card()` 函数中，write 前加一道 round-trip 校验：

```python
# After rendering, before writing
try:
    test_metadata, _, _ = parse_frontmatter(new_fm + "\n" + body)
    # Check that nested structures survived round-trip
    for key in normalized:
        if isinstance(normalized[key], (dict, list)):
            if key not in test_metadata:
                raise ValueError(f"Key '{key}' lost during YAML round-trip")
            if type(normalized[key]) != type(test_metadata[key]):
                raise ValueError(
                    f"Key '{key}' type changed from {type(normalized[key]).__name__} "
                    f"to {type(test_metadata[key]).__name__} during round-trip"
                )
except Exception as e:
    print(f"ROUND-TRIP CHECK FAILED: {e}")
    print("Writing ABORTED. Fix the renderer before retrying.")
    return {"file": str(filepath), "status": "aborted", "reason": str(e)}
```

这样可以防止任何未来对 `render_frontmatter` 的修改引入新的数据丢失。

---

*欧阳锋 · 2026-05-31*
