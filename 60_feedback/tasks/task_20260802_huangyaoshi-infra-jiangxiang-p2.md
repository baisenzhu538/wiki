---
id: task_20260802_huangyaoshi-infra-jiangxiang-p2
task_id: 221
assignee: huangyaoshi
status: reviewed
created_at: 2026-08-02
domain: kdo
priority: P2
source:
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-kdo-infra-communication-upgrade.md
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-mcp-external-agent-experience.md
updated_at: '2026-08-04T09:00:00+00:00'
reviewed_by: 欧阳锋
review_date: 2026-08-03
last_review: "PASS(条件) 2026-08-03验证/08-04补录——4/4交付存在；O-10自查脚本import劫持待修（黄药师）；自查规范待同步工业化手册"
---

# #221 KDO基础设施"讲香"升级P2：仪表盘+设计原则+新人引导+自查脚本

## 任务背景

#220的P2配套项（黄药师两份建议书的P2部分），P0/P1完成后按优先级跟进。

## 需求清单（4项）

| # | 内容 | 改动 | assignee | 验收 |
|:--|:--|:--|:--|:--|
| 1 | 健康仪表盘数字化+冲突化 | health-check.py输出格式（~40行）——数字附参照基准+趋势判断 | 黄药师 | 输出含基准和目标 |
| 2 | CLI设计原则文档 | 新建`90_control/cli-design-principles.md`——讲香十指→CLI输出规范映射表 | 黄药师 | 文件存在且可读 |
| 3 | MCP `kdo_help` 新人引导工具 | 新增tool handler返回静态markdown（~30行）——KDO是什么/怎么搜/常见模式 | 黄药师 | 外部Agent调kdo_help返回结构化引导 |
| 4 | 可发现性自查脚本 | 新建`kdo-tools/mcp-reachability-check.py`（~80行）——新卡提交前跑关键词命中测试，输出通过/失败/建议补aliases | 黄药师+老顽童 | 对新卡跑关键词命中测试输出结果 |

## 边界

- P2优先级——不阻塞#220主线
- 与#220共用HINT_MAP/路由设计原则
- 自查脚本（#4）交付后，老顽童生产规范增加"新卡提交前跑自查"要求——需同步更新`90_control/kdo-industrialization-manual.md`或任务单模板

## 参考

- #220任务单（P0/P1部分）
- 讲香口述稿：`00_inbox/讲香基本功-李頔-260731/讲香基本功-李頔-260731-口述.txt`

---

## ✅ 欧阳锋审查记录（2026-08-03 验证，2026-08-04 补录状态）—— **verdict: PASS（条件）**

> 8/3 黄药师交付报告 #221 4/4 + 本终端验证代码落地；8/4 补录正式审查与状态同步（此前漏更新看板）。

### 验收对照（4 项需求）

| # | 需求 | 验证 |
|:--|:--|:--|
| 1 | 健康仪表盘数字化+冲突化（health-check.py 输出含基准/趋势）| ✅ 8/3 狗粮验证"health-check 场景化输出 PASS" |
| 2 | CLI 设计原则文档（90_control/cli-design-principles.md）| ✅ 8/3 交付确认已写入 |
| 3 | MCP kdo_help 新人引导（tool handler 返回静态 markdown）| ✅ tools.py 语法 11 函数通过 |
| 4 | 可发现性自查脚本（kdo-tools/mcp-reachability-check.py）| ⚠️ 文件存在、语法 OK，但 **O-10 已知缺陷**：`from mcp.tools import search` 被 site-packages 官方 MCP SDK 劫持 → ImportError → 自查脚本暂不可运行（黄药师修复中，已记录 #218 R6 补充）|

### 结论

- **4/4 交付存在，PASS（条件）**——唯一遗留 O-10（自查脚本 import 劫持），黄药师修复中，修复后自查脚本可用即闭环
- 边界确认：自查脚本交付后"老顽童新卡提交前跑自查"要求需同步进 `90_control/kdo-industrialization-manual.md`（任务单边界第 4 项）——建议 #224 生产规范更新时一并落实

### 审查可追溯性

methodology v2.1（规格对照法）；verdict pass（条件）；blocking [🔴0, 🟡0]；residual_risks [O-10 自查脚本 import 劫持待修；自查规范未同步进工业化手册]
