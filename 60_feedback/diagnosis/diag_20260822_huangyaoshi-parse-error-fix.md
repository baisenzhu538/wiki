---
title: "#409 库级 YAML 修复执行报告——parse-error 58 张归零"
author: 黄药师
date: 2026-08-22
task: "task_20260822_huangyaoshi-parse-error-yaml-fix"
type: diagnosis
---

# #409 执行报告：库级 YAML 修复（parse-error 58 → 0）

## 一、修复前清单（58 张，full-library-rescan 实测基线）

- **A 类 parse-error（47 张）**：frontmatter 列表块结构损坏——顶格列表项混入缩进式列表（`expected <block end>, but found '-'`）+ 粘连行（`- src_unknown - src_unknown`）。全库分布：cases×6 / concepts×27 / dark-knowledges×3 / entities×3 / frameworks×4 / systems×3 / tools×4。根因与 #373 同族（历史批量脚本 P-29 正则破坏）
- **B 类 BOM+CRLF（7 张）**：文件头 UTF-8 BOM + CRLF 换行（yt-panproduct×6 + skill-yitang-project-spiral-thinking）——扫描器 `startswith("---")` 与 `find("\n---\n")` 均失败
- **C 类无 frontmatter（4 张）**：系统索引文件（30_wiki/index.md / links/index.md / personal-os/README.md / concept-card-index-latest.md）——无 frontmatter，扫描器判 no frontmatter

## 二、修复方法（样本校准先行 + 状态机规则）

1. **A 类**：yaml 级逐行状态机——跟踪每个 key 的列表风格（indented/top），顶格列表项在"列表已为缩进式"时补缩进 2 空格；粘连行 `- src_unknown - src_unknown` 保持缩进拆两行；**key 后顶格块序列（如 `domain:\n- strategy`）是合法 YAML，保留不动**（样本验证后才定规则，避免过度修复）
2. **B 类**：去 BOM + CRLF→LF（扫描器闭合判定依赖 `\n---\n`）
3. **C 类**：补最小 frontmatter（id/title/type: index/status: stable），正文零改动

每张修复后 `yaml.safe_load` 验证通过才进入下一步（dry-run 全程 0 失败才 apply）。

## 三、归零验收（#399 纪律：附工具输出）

```
[full-library-rescan] 全库复扫（2839 文件）
  parse-error           : 剩余 0
Status: PASS
```

**58 → 0 路径**：A 类 47 张（结构修复）+ B 类 7 张（编码规范化）+ C 类 4 张（补 frontmatter）。无退回清单（全部机械修复成功，无内容歧义卡）。

## 四、内容语义零变化验证

- **58 张 body 对比**（git HEAD vs 修复后，归一化换行）：54 张 body 逐字节一致
- **C 类 4 张**：body 差异全部归因 kdo index 自动化产物（index.md 时间戳更新/新卡登记/死链清理），非本任务引入；frontmatter 补充本身零正文改动
- 抽查 git diff（case-strategy-cool-boiled-water）：17 行变化全部在 source_refs 列表区（粘连拆分+补缩进），`reviewed_by` 及之后零变化

## 五、回归确认

- `kdo index` 重建（4066 文档）已完成/进行中——58 张修复卡重新入索引
- git commit：`cced88551`（58 files +765/-468，path-scoped 不裹挟）

## 六、遗留观察

- B 类 7 张的 CRLF→LF 是**结构性必要**（扫描器不认 CRLF frontmatter），但 git diff 显示整文件变化——已确认内容不变，属换行符规范化
- 扫描器对 CRLF 的容错可作为后续改进项（当前 0 遗漏）

*黄药师 · 2026-08-22*
