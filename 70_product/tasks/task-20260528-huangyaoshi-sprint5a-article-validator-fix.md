---
title: "黄药师：Sprint 5a — Article Validator source_refs 识别修复"
assigned_to: "黄药师 (Builder)"
priority: "P1"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 黄药师：Sprint 5a — Article Validator source_refs 识别修复

## 背景

Sprint 5 ✅ 已通过。老顽童 Phase C 文章 3 篇的内容质量审查通过，但 `kdo validate --v15 --article` 报错导致质量门未通过：

```
FAIL target_audience: Missing target audience
FAIL core_thesis: Missing core thesis
WARN traceable_sources: No source_refs or footnotes found
```

前两项为文章结构问题（老顽童修），第三项是 **validator 本身的 bug**——文章 frontmatter 中已有 `source_refs`，但 article validator 未识别。

当前行为：

```yaml
# 文章 frontmatter （已有 source_refs）
source_refs:
  - 30_wiki/tools/yt-pitch-storytelling
  - 30_wiki/tools/yt-pitch-quantification
```

但 `kdo validate --v15 --article` 仍报 "No source_refs or footnotes found"。

---

## 修复目标

让 article v15 validator 正确识别文章 frontmatter 中的 `source_refs` 字段，将 WARN 改为 PASS。

---

## 代码位置

**主逻辑**：`kdo/commands/quality.py` — `cmd_validate_article` 或 v15 article gate 检查函数

**相关函数**（需 grep 确认）：
- `cmd_validate_article`（quality.py L1489+）
- 或 v15 gate 内部的 article 检查路径

---

## 做法

### Step 1：定位（~5min）

查找 article v15 gate 中检查 source_refs/footnotes 的逻辑。可能在：
1. `commands/quality.py` 中 `cmd_validate_article` 调用的某个 gate check 函数
2. 或 `gate.py` 中 article 相关的检查

```bash
# 定位 grep
grep -n "source_refs\|footnote\|traceable" kdo/commands/quality.py
grep -n "source_refs\|footnote\|traceable" kdo/gate.py
```

### Step 2：修复（~15min）

**问题原因**：article validator 只检查了文章 body 中的 `[^1]` inline footnotes，未读取 frontmatter `source_refs` 字段。

**修复方案**：在 article 的 source_refs/footnotes 检查中，增加对 frontmatter `source_refs` 的识别：

```python
# 伪代码示意——在现有 footnote 检查逻辑中追加
frontmatter_source_refs = metadata.get("source_refs", []) or []
if frontmatter_source_refs:
    # source_refs found in frontmatter → PASS
    pass
elif re.search(pattern, body_text):
    # inline footnotes found → PASS
    pass
else:
    # WARN: no traceable sources
```

**约束**：
- 不改动 card 和 skill 的 validator（只动 article 检查）
- frontmatter `source_refs` 为列表类型（`list[str]`），空列表视为无
- 如果文章既有 frontmatter source_refs 又有 inline footnotes，仍然 PASS（不冲突）

### Step 3：测试（~10min）

```bash
kdo validate --v15 --article 40_outputs/content/articles/art_20260528_storytelling_vs_truth.md
kdo validate --v15 --article 40_outputs/content/articles/art_20260528_quantification_traps.md
kdo validate --v15 --article 40_outputs/content/articles/art_20260528_metaphor_cognitive_implant.md
```

**预期**：WARN `traceable_sources` 消失，三篇均不再报此问题。

### Step 4：全量 pytest 确认不降级（~5min）

```bash
pytest
```

**预期**：当前 388 passed, 1 skipped 不降级。

---

## 验收

| # | 验收项 | 判定 |
|:-:|:------|:----:|
| 1 | 三篇文章的 `kdo validate --v15 --article` 不再报 traceable_sources WARN | 终端 |
| 2 | 仅改 article validator，不影响 card/skill 的 source_refs 检查 | pytest |
| 3 | pytest 全量不降级 | 388 passed, 1 skipped |

## 不做

- **不做** 修改文章内容或结构（那是老顽童的活——缺 Audience/Core Thesis 节）
- **不做** 重写 article validator 架构
- **不做** 为 card/skill 增加类似 frontmatter source_refs 回退逻辑
- **不做** 修改 CLI 或新增 flag

---

## 欧阳锋审查报告（2026-05-29）

### 验收结果

| # | 验收项 | 目标 | 实测 | 判定 |
|:-:|:------|:---:|:----:|:----:|
| 1 | 三篇文章的 `kdo validate --v15 --article` 不再报 traceable_sources WARN | WARN → PASS | ✅ 三篇均 PASS | ✅ **PASS** |
| 2 | 仅改 article validator，不影响 card/skill 的 source_refs 检查 | 不改无关代码 | ✅ 仅动 quality.py article 路径 | ✅ **PASS** |
| 3 | pytest 全量不降级 | 388 passed, 1 skipped | ✅ 388 passed, 1 skipped | ✅ **PASS** |

### 代码审查

**quality.py** L1357-1363 —— 正则回退检测 `source_refs`：

```python
if not source_refs:
    if re.search(r'^source_refs:\s*\n(?:\s+-.+\n?)+', raw, re.MULTILINE):
        source_refs = ["detected"]
```

**问题原因诊断**：`parse_frontmatter` 是逐行解析器，遇到 YAML 多行列表（`source_refs:\n  - xxx\n  - yyy`）时丢弃了列表项，导致 `fm.get("source_refs", [])` 返回空列表。正则回退方案正确——在正常解析返回空时，回头在原始文本中搜 `source_refs:` + 列表模式。

**边界安全性**：
- 正则命中后设 `["detected"]` 哨兵值而非真实列表。当前代码路径只有 `if source_refs or has_footnotes:` 这一个判断点，哨兵值足够。如果后续代码遍历 `source_refs` 拿具体路径，会拿不到真值——目前无此路径，安全。
- 正则 `(?:\s+-.+\n?)+` 要求缩进 `-` 开头，对 YAML 有效缩进（`  - xxx`）可匹配。tab 缩进或 inline 格式 `source_refs: [a, b]` 不会命中——但此时 `parse_frontmatter` 也不会丢，不需回退。覆盖合理。

### 附带发现

黄药师 working tree 中还有 Sprint 5 的改动（delivery.py/+42、feedback.py/+125、cli.py/+1、test_ship_gate.py、test_feedback_loop.py）尚未 commit。Sprint 5 审查时已通过但未入库。建议一并提交。

### 签发

> **黄药师：Sprint 5a — Article Validator source_refs 识别修复 ✅ PASS**
>
> 修复正确，目标行为验证通过（3/3 文章 traceable_sources 从 WARN 变为 PASS）。pytest 388/1 无降级。改动量 8 行，精准解决了 `parse_frontmatter` 丢弃 YAML 多行列表的问题。
>
> *欧阳锋 · 2026-05-29*

---

*欧阳锋 · 2026-05-28*
