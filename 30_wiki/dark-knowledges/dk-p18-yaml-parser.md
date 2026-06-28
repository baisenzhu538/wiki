---

id: dk-p18-yaml-parser
title: P-18：手写YAML解析器导致嵌套数据丢失 — 97行bug → 15行修复
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-18
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-18'
related:
- [[kdo-yaml-frontmatter-safety]]
- [[fix-data-curator-parse-bug]]
- [[tool-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]
- [[dk-p19-quote-yaml]]
- [[dk-f13-handwritten-yaml-parser]]
- [[dk-c2-dual-status-machine]]
- [[kdo-yaml-frontmatter-safety]]
- [[master-first-principles]]
- [[dk-f13-handwritten-yaml-parser]]
- [[dk-p11-regex-cutoff]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 手写解析器陷阱
  follow_up_question: 这个脚本使用的是标准库（yaml.safe_load / json.load）还是手写正则/字符串替换？
- signal: src_unknown
  framework_lens: 格式复杂度低估
  follow_up_question: 这个格式是否有官方/成熟库？为什么没用？# P-18：手写YAML解析器导致嵌套数据丢失 — 97行bug → 15行修复
---
## 原始表述 / 核心洞察

> **症状**：Data Curator Clean 跗完后，`yt-decision-y-model.md` 的 `visual_analysis` 字段从 4 张图的完整结构化描述变成 5 条扁平字符串，3 张图 15 条分析丢失。`yt-model-aesthetic-progression.md` 的 `related` 字段从 4 个链接变成 `level: intermediate`。
>
> **根因**：`clean_cards.py` 使用 97 行手写 YAML 解析器，只能处理平面键值对和一层嵌套。遇到 `visual_analysis` 这种"列表内嵌 dict"结构时直接拍扁成字符串。
>
> **对策**：
> - **绝对不要手写 YAML/JSON 解析器**。Python 标准库 `yaml.safe_load()` 1行替代97行
> - 任何批量文件修改工具必须在 write 前做 round-trip 校验
> - 修改后全量扫描 `yaml.safe_load()` 确认 0 损坏
> - 修复流程：代码修复→回滚受损文件(git restore)→重跗
>
> **定位**：`30_wiki/decisions/fix-data-curator-parse-bug.md`

**核心洞察**：标准格式（YAML/JSON/Markdown）看起来简单，但规范细节（缩进、引号、嵌套列表、多行字符串）远超直觉。手写解析器时，开发者往往只覆盖自己当下看到的“常见情况”，却在边界结构上静默破坏数据。最危险的 bug 不是崩溃，而是文件看起来仍然可读、流程仍然跑通，但关键信息已经被拍扁或替换。防御关键只有两条：永远用成熟库，写前做 round-trip 校验。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **不要手写解析器**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **round-trip 校验**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **全量扫描验证**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **修复流程**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:
|:---|:---|:---|
| **手写 YAML 解析器拍扁嵌套结构** | `visual_analysis` 列表内 dict 变成扁平字符串；`related` 链接丢失 | 只处理平面键值对和一层嵌套，忽略 YAML 规范复杂性 | 用 `yaml.safe_load()` / `yaml.dump()` 替代手写解析器 |
| **批量修改不做 round-trip 校验** | 写入后才发觉数据损坏，已无法低成本回滚 | 缺少写前验证机制 | 修改前先解析并重新序列化，与原文件对比 |
| **用字符串替换处理 YAML frontmatter** | 文件看起来还是 YAML，实际结构已损毁 | 把结构化格式当作文本处理 | 始终使用 YAML 库，避免正则/字符串替换 |
| **损坏后没有立即停用问题代码** | 继续运行导致更多文件受损 | 应急响应流程缺失 | 立即停用 → 修复代码 → git restore 受损文件 → 重跑 |
| **只验证“能解析”不验证“结构一致”** | 批量修改后 YAML 能 load，但字段类型或层级已变 | 验证只覆盖语法，不覆盖语义 | 对关键字段做结构快照对比，确认类型/层级/数量一致 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
