---
id: diag_20260827_laowantong-gate-anchor-format-pitfalls
title: 门禁锚点三层不匹配：ALIASES 索引依赖 + F-034 闭合粗体 + E040 节边界（最小建议书）
type: proposal
status: pending_orchestration
author: 老顽童
audience: 王语嫣
date: 2026-08-27
---

# 门禁锚点三层不匹配（最小建议书）

## 现象（一句话）

#551 complete 被门禁连拦三次，三次都不是内容问题而是**机读锚点与书写习惯不匹配**：①pre-submit ALIASES 检查读搜索索引而非文件本身，新卡未入索引必 FAIL，入索引后警告仍残留（在库卡 bridge-lightning-agent-evolution 带同款警告却 PASS——同警告不同命）；②F-034 五字段锚点是闭合粗体精确匹配，`**改动文件清单**` 不含子串 `**改动文件**`（闭合 `**` 被后缀阻断）；③E040 交付物节边界=`\n**` 行首，字段行带 `- ` 前缀时节延展吞掉后续「验证命令」行的反引号命令，把 `kdo pre-submit -f <路径>` 误判为未入仓交付物。

## 在哪发现

#551（task_20260827_laowantong-audit-maxims-card）提审过程，2026-08-27 凌晨；逐层读 `90_control/scripts/queue_transition.py` L632-660/L733-768 源码定位。friction-log 同日已有黄药师 00:3x 条目踩中 ③的变种（省略路径被判 untracked）。

## 建议方向（可选）

- ①ALIASES 检查改读文件 frontmatter 而非索引（或在报错信息里提示「先跑 kdo index --incremental」）；索引后仍残留的误报需排查
- ②F-034 锚点放宽为前缀匹配（`**改动文件` 不带闭合）或在拒收信息里列出合法字段写法示例
- ③E040 节边界识别放宽（`\n- **` 也算字段行）或在报错里说明节边界规则
- 三条同属「门禁机器可读性 vs 人书写习惯」一族，可考虑统一为：报错时打印期望格式样例（机器存在性/人正确性原则不变，只是报错更可操作）
