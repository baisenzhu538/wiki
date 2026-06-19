---
id: dk-p18-yaml-parser
title: P-18：手写YAML解析器导致嵌套数据丢失 — 97行bug → 15行修复
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-18
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-18
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
created_at: 2026-06-03
updated_at: '2026-06-18'
related:
- '[[dk-c2-dual-status-machine]]'
- '[[kdo-yaml-frontmatter-safety]]'
- '[[master-first-principles]]'
- '[[dk-f13-handwritten-yaml-parser]]'
- '[[dk-p11-regex-cutoff]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-enriched
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 批量处理 YAML/JSON 文件后发现嵌套结构被拍扁或字段丢失
  framework_lens: 手写解析器陷阱
  follow_up_question: 这个脚本使用的是标准库（yaml.safe_load / json.load）还是手写正则/字符串替换？
- signal: 一个看似简单的解析器只能处理“最常见”的格式，遇到列表内 dict 或多行字符串就出错
  framework_lens: 格式复杂度低估
  follow_up_question: 这个格式是否有官方/成熟库？为什么没用？
---
# P-18：手写YAML解析器导致嵌套数据丢失 — 97行bug → 15行修复

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

- 你需要写一个处理 YAML/JSON 的工具
- 你考虑手写解析器而非使用标准库
- 你发现数据在批量处理后损失或变形
- 你需要建立批量文件修改的安全流程

## 操作方法

1. **不要手写解析器**：
   - YAML 用 `yaml.safe_load()` / `yaml.dump()`
   - JSON 用 `json.load()` / `json.dump()`
   - 标准库已经处理了所有边界情况，不需要重造轮子

2. **round-trip 校验**：
   - 修改前：读取原文件 → 解析 → 重新序列化 → 与原文件对比
   - 如果有差异，解析器有 bug，停止操作
   - 不要在没有 round-trip 验证的情况下运行批量修改

3. **全量扫描验证**：
   - 修改完成后，对所有文件重新解析
   - 确保没有 YAML parse error
   - 确保数据结构与修改前一致

4. **修复流程**：
   - 发现 bug 后立即停止使用有缺陷的代码
   - 修复代码（用标准库替代手写）
   - git restore 受损文件
   - 用修复后的代码重新运行

5. **不要做的事**：
   - 不要手写 YAML/JSON/XML 解析器
   - 不要在没有 round-trip 校验的情况下运行批量修改
   - 不要用 regex 处理嵌套数据结构

## 适用边界

- 适用于所有涉及解析标准格式的场景
- 不适用于非标准格式的自定义文本解析
- **与 P-11 的区别**：P-11 是"手写 regex 解析 Markdown"，P-18 是"手写 YAML 解析器"——同一类问题的不同表现
- **与 F-KDO-013 的关系**：F-KDO-013 是同一问题的早期版本，P-18 是更严重的复发

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:---|:---|:---|:---|
| **手写 YAML 解析器拍扁嵌套结构** | `visual_analysis` 列表内 dict 变成扁平字符串；`related` 链接丢失 | 只处理平面键值对和一层嵌套，忽略 YAML 规范复杂性 | 用 `yaml.safe_load()` / `yaml.dump()` 替代手写解析器 |
| **批量修改不做 round-trip 校验** | 写入后才发觉数据损坏，已无法低成本回滚 | 缺少写前验证机制 | 修改前先解析并重新序列化，与原文件对比 |
| **用字符串替换处理 YAML frontmatter** | 文件看起来还是 YAML，实际结构已损毁 | 把结构化格式当作文本处理 | 始终使用 YAML 库，避免正则/字符串替换 |
| **损坏后没有立即停用问题代码** | 继续运行导致更多文件受损 | 应急响应流程缺失 | 立即停用 → 修复代码 → git restore 受损文件 → 重跑 |
| **只验证“能解析”不验证“结构一致”** | 批量修改后 YAML 能 load，但字段类型或层级已变 | 验证只覆盖语法，不覆盖语义 | 对关键字段做结构快照对比，确认类型/层级/数量一致 |

## 为什么值钱

- 这是"不要重造轮子"的经典案例：97 行自制代码 vs 1 行标准库
- 极具破坏力：数据损坏是静默的，不会报错，只会在使用时发现
- 揭示了"复杂度僧恨"——手写解析器的复杂度越高，bug 越难发现
- **AI 训练语料中不会有这条**：没有任何文档会写"手写 YAML 解析器可能拍扁嵌套结构"

## 与其他知识的关联

- [[dk-c2-dual-status-machine]] — 同一领域：frontmatter 中 `status` 字段被两个状态机共用，说明对 frontmatter 的轻率语义设计同样会级联放大
- [[dk-f13-handwritten-yaml-parser]] — F-KDO-013 是同一问题的早期版本
- [[dk-p11-regex-cutoff]] — P-11 是同一类问题在 Markdown 解析上的表现
- `30_wiki/decisions/fix-data-curator-parse-bug.md` — 修复决策记录
- `.agent/pitfalls.md` → P-18（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
