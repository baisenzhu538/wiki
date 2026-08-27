---
id: 569
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T23:55:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - 90_control/scripts/queue_transition.py
---

# #569 门禁锚点三层不匹配修复 + 报错可操作化（期望格式样例）

- **任务号**：#569 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-27 王语嫣裁定（老顽童建议书 diag_20260827_laowantong-gate-anchor-format-pitfalls 采纳——#551 连拦三次全是锚点格式不是内容，注意力税实证）

## 背景（三层实证，queue_transition L632-660/L733-768）

1. ALIASES 检查读搜索索引而非文件本身——新卡未入索引必 FAIL，入索引后警告残留（同警告不同命）
2. F-034 五字段锚点闭合粗体精确匹配：`**改动文件清单**` 不含子串 `**改动文件**`
3. E040 节边界=`\n**` 行首：字段行带 `- ` 前缀时节延展吞后续行，把 `kdo pre-submit -f <路径>` 命令误判为未入仓交付物（23:37 残片垃圾行同族）

## 任务

1. ALIASES 改读文件 frontmatter（或报错提示「先跑 kdo index --incremental」）；索引后残留误报排查
2. F-034 锚点放宽前缀匹配（`**改动文件` 不带闭合），报错信息附合法字段写法示例
3. E040 节边界放宽（`\n- **` 也算字段行起始）
4. 统一方向：门禁报错时打印期望格式样例（机器存在性/人正确性原则不变，报错更可操作）
5. 顺手查 tools/ 版 agent-spec 垃圾 aliases 的生成源（哪次脚本产物，防再生——twin-drift 建议书第 3 条挂此）

## 验收

- #551 场景回归：合法书写不再被拦 + 报错带样例 + 回归过；欧阳锋终审
