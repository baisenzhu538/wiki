---
id: dk-f13-handwritten-yaml-parser
title: F-KDO-013：手写 YAML 解析器导致嵌套数据丢失
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-013
source_refs:
- 90_control/failure-modes.md#F-KDO-013
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[kdo-yaml-frontmatter-safety]]'
- '[[master-first-principles]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# F-KDO-013：手写 YAML 解析器导致嵌套数据丢失

## 原始表述

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

## 使用场景

- 你需要批量修改大量卡片的 frontmatter（如统一添加某个字段、批量更新 source_refs）
- 你在写脚本处理 Markdown 文件的 frontmatter 时，想用字符串替换而非 YAML 库
- 你发现某些卡片的 frontmatter 结构被破坏了，需要排查是哪个操作导致的
- 你在审查他人提交的批量修改脚本时，需要检查是否正确处理了 YAML

## 操作方法

1. **不手写**：任何涉及 YAML 的操作，始终使用 `PyYAML` 或类似的库，不要用正则表达式或字符串替换
2. **做 round-trip 校验**：批量修改前，写一个小脚本：读取 YAML → 解析为 Python dict → 不做任何修改 → 写回 YAML → 与原文件比较
3. **先 dry-run**：批量修改时，先输出到临时目录，人工抽检几个文件确认嵌套结构完好
4. **验证嵌套结构**：特别检查列表项（`- item`）、多级嵌套、多行字符串这些容易出问题的地方
5. **使用 git diff**：批量修改后用 `git diff` 检查变更，如果某个文件的变更量过大或看起来"不对"，立即回滚

## 适用边界

- 适用于所有涉及 YAML frontmatter 批量修改的场景
- 不适用于单个简单字段的手动编辑（如只改一个 `title` 字段）——这种情况手动修改安全
- 如果你使用的是 JSON frontmatter（`---json` 格式），同样道理适用——用 `json.load()` 而非字符串替换
- 对于非标准的 YAML 扩展（如 YAML 1.2 特有特性），即使 `yaml.safe_load()` 也可能有差异，需要注意
- **根治方案是使用库而非手写**，但即使用库也建议做 round-trip 校验

## 为什么值钱

- 这是 KDO 特有的数据损坏模式：**每张卡片都有 YAML frontmatter，批量修改 frontmatter 是常见操作**
- 手写 YAML 解析器的危险极高：YAML 看起来简单，实际规范复杂——一个小小的缩进或引号错误就能导致整个 frontmatter 结构崩溃
- 揭示了一个普遍的工程误区：**看起来简单的格式（如 YAML、JSON、Markdown）往往比想象复杂，不要手写解析器**
- 任何 AI 训练语料中都不会有"KDO 的卡片批量修改时手写 YAML 解析器会导致嵌套数据丢失"这条知识

## 与其他知识的关联

- dk-c1-regex-on-cjk — 同一模式："手写解析器忽视了格式的复杂性"。C-1 是"regex `\b` 不识别 CJK"，F-13 是"手写 YAML 解析器不处理嵌套结构"——两者都是"轻视已有库函数的复杂性，试图用简单方法替代"
- master-systems-thinking — 系统思维中的"抽象漏洞"：YAML 解析是一个已经被高度抽象化的问题，手写解析器就是重新发明轮子
- `90_control/failure-modes.md` → F-KDO-013（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
