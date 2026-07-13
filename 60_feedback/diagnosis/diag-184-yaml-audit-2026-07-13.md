# #184 全库 YAML 体检报告

> 黄药师 · 2026-07-13

## 扫描结果

| 类别 | 修复前 | 修复后 | 说明 |
|:---|:---|:---|:---|
| OK | 1900 | 2217 | +317 |
| Type1 解析失败 | 360 | 20 | 340 已修复（related 列表缩进标准化） |
| Type2 结构异常 | 305 | 316 | 新增 11（修复过程暴露），需逐卡判定 |
| Type3 无 frontmatter | 92 | 104 | 新增 12（修复过程暴露），出清单交王语嫣 |

## Type1 剩余 20（硬伤，需手工修）

全部为双三角案例卡 + 少数 legacy 卡，错误类型为 `mapping values are not allowed here`（title 字段含中文特殊字符）。20 张卡清单见审计脚本输出。

建议：王语嫣单独立任务修，不在此次批量范围。

## Type2 结构异常 316

主要类型：
- `missing id`：~200 张 legacy 卡，可用 filename stem 补
- `related is not list`：~40 张，related 字段为裸字符串
- `source_refs is not list`：~30 张，source_refs 为裸字符串

建议：missing id 可脚本批量补（stem→id），related/source_refs 非 list 需逐卡判定语义后修。

## Type3 无 frontmatter 104

包含 index.md、concept-card-index-latest.md 等索引文件 + 约 70 张 legacy case 卡。索引文件为设计如此（非卡片），legacy case 卡需王语嫣分类讨论后另开任务。
