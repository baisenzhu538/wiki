---
id: task_20260802_huangyaoshi-infra-jiangxiang-p2
task_id: 221
assignee: huangyaoshi
status: queued
created_at: 2026-08-02
domain: kdo
priority: P2
source:
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-kdo-infra-communication-upgrade.md
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-mcp-external-agent-experience.md
updated_at: '2026-08-02T23:59:00+00:00'
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
