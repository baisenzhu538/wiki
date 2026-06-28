---

id: dk-f13-handwritten-yaml-parser
title: F-KDO-013：手写 YAML 解析器导致嵌套数据丢失
type: dk
dark_knowledge_type: failure
status: enriched
domain:
  - master
source_person: system
source_context: failure-modes.md F-KDO-013
source_refs:
  - 10_raw/sources/src_20260619_d967c8f5_90_control_failure_modes.md#F-KDO-013
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
  - [[kdo-yaml-frontmatter-safety]]
  - [[tool-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]
  - [[dk-p18-yaml-parser]]
  - [[dk-p19-quote-yaml]]
  - [[proposal-yaml-frontmatter-standardization]]
  - [[kdo-yaml-frontmatter-safety]]
  - [[master-first-principles]]
  - [[dk-c1-cjk-regex-silent-fail]]
pipeline:
  - confidence-draft
  - confidence-source-cited
  - confidence-reviewed
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
  - signal: "批量修改 frontmatter 的脚本使用字符串替换、正则或 `.split(\\"---
\\\")` 拆分，而非 `yaml.safe_load()`"
  framework_lens: '手写解析器只能处理平铺 `key: value`，遇到嵌套列表、字典、多行字符串会静默损毁结构'
  follow_up_question: '检查脚本是否使用 PyYAML 等标准库解析并回写；若不是，立即停止并改用 `yaml.safe_load()` + `yaml.dump()`'
- signal: '批量修改后某些卡片的 `related:` 列表项合并/丢失，或 `domain:` 层级被抹平'
  framework_lens: 'YAML 的缩进、引号、列表标记 `-`、多行字符串规则被忽略，结构已损坏但文件看起来仍像合法 YAML'
  follow_up_question: '立即用 `git diff` 检查变更，对异常文件做 round-trip 校验（读取→dump→比对）确认结构是否一致'
- signal: 'dry-run 输出目录中抽检发现嵌套结构异常'
  framework_lens: '手写解析器的错误在批量场景下被放大，dry-run 与人工抽检是拦截结构损坏的最后一道防线'
  follow_up_question: '批量修改前是否输出到临时目录并抽检 3-5 个文件的列表、字典、多行字符串是否完好？'
---

# F-KDO-013：手写 YAML 解析器导致嵌套数据丢失

## 原始表述/核心洞察

> **触发条件**：批量修改 KDO 卡片 frontmatter 时，为了"简单快捷"而手写字符串替换逻辑来解析 YAML。
>
> **表现**：frontmatter 中的嵌套结构（如列表 `related:`、字典 `domain:`、多行字符串）被破坏或丢失。文件看起来"还是 YAML"，但实际结构已经损毁。
>
> **根因**：YAML 规范比想象复杂得多：缩进敏感、引号规则、换行符处理、嵌套列表的 `-` 标记等。手写解析器忽略了这些细节，只处理了最简单的 `key: value` 平铺结构。
>
> **防御措施**：
> - **永久修复**：始终使用 `yaml.safe_load()` + `yaml.dump()` 处理 frontmatter，不要手写字符串替换
> - **事前检查**：批量修改 frontmatter 前，先做 round-trip 校验：读入 YAML → 写回 YAML → 比较是否一致
> - **dry-run 策略**：任何批量修改先输出到临时目录，人工抽检 3-5 个文件的嵌套结构是否完好
>
> **状态**：代码已修复（改用 `yaml.safe_load()`），但模式未归档入库。

核心洞察：**YAML（以及 JSON、Markdown 等"看起来简单"的格式）的规范复杂度远超直觉，任何手写解析或字符串替换都是数据损毁的高危行为**。KDO 每张卡片都依赖 YAML frontmatter 维护元数据与概念关系，批量修改 frontmatter 是高频操作；一旦用手写解析器替代标准库，嵌套结构会在"无报错"的情况下被静默破坏，且损毁结果往往看起来仍是合法的 YAML，极难事后排查。这不是"代码写错了"，而是**对"已有库函数复杂度"的系统性低估**。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **不手写**：任何涉及 YAML 的操作，始终使用 `PyYAML` 或类似的库，不要用正则表达式或字符串替换
2. **做 round-trip 校验**：批量修改前，写一个小脚本：读取 YAML → 解析为 Python dict → 不做任何修改 → 写回 YAML → 与原文件比较
3. **先 dry-run**：批量修改时，先输出到临时目录，人工抽检几个文件确认嵌套结构完好
4. **验证嵌套结构**：特别检查列表项（`- item`）、多级嵌套、多行字符串这些容易出问题的地方
5. **使用 git diff**：批量修改后用 `git diff` 检查变更，如果某个文件的变更量过大或看起来"不对"，立即回滚

## 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 适合 | 所有涉及 YAML frontmatter 批量修改的场景，尤其是 KDO 卡片批量更新 |
| ✅ 适合 | 审查任何自称"简单处理一下 frontmatter"的脚本或 Prompt |
| ❌ 不适合 | 单个简单字段的手动编辑（如只改一个 `title` 字段）——这种情况手动修改安全 |
| ⚠️ 注意 | JSON frontmatter（`---json` 格式）同样道理适用：用 `json.load()` 而非字符串替换 |
| ⚠️ 注意 | 非标准的 YAML 1.2 特有特性即使 `yaml.safe_load()` 也可能有差异，需谨慎 |
| ⚠️ 注意 | 即使用库也建议做 round-trip 校验，库也可能改变格式或丢失注释 |

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|:-----|:------|:-----|:-----|
| 手写字符串替换解析 YAML | 脚本用 `.replace()`、regex 或 `.split("---")` 处理 frontmatter | 低估 YAML 规范复杂度，误以为"就是 key:value" | 改用 `yaml.safe_load()` + `yaml.dump()` |
| 嵌套列表被扁平化/丢失 | `related:` 的 `-` 项合并成一行或整段消失 | 只识别平铺结构，未处理列表标记与缩进 | 用 YAML 库解析后回写，并做 round-trip 比对 |
| 字典层级被抹平 | `domain:` 从多级结构变成字符串或字段错乱 | 未处理嵌套缩进与键值边界 | 解析为 dict 后再修改，禁止字符串拼接 |
| 多行字符串/引号断裂 | `summary:` 长文本被截断、引号不配对、换行异常 | 未处理 YAML 引号规则与 `|`/`>` 多行语法 | 用库重新 dump，并抽检多行字段 |
| 批量修改后 git diff 异常 | 某文件变更量过大或"看起来不对" | 手写解析器造成结构性损毁 | 立即回滚，改用库函数重写脚本 |
| dry-run 未抽检嵌套结构 | 正式运行后才发现大量卡片 frontmatter 损坏 | 只检查了字段存在性，没验证结构完整性 | dry-run 输出到临时目录，人工抽检 3-5 个嵌套字段 |

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

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
