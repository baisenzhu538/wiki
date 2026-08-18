---
id: 372
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T02:30:00+00:00'
title: 卫生债大扫除（P2，小昭体检采纳）——_tmp 29286 文件 + 嵌套 git 仓库 + C:/ 路径 bug 目录 + inbox PARA 库决策
priority: P2
dependency: []
reviewed_by: 欧阳锋
---

# #372 卫生债大扫除（P2）

## 任务目标

清理纯垃圾债与路径事故残留（小昭体检 §六，王语嫣抽核实锤）。

## 素材/证据

- `_tmp/` 29286 个文件（最大单体垃圾）
- `wiki/wiki/.git` 嵌套 git 仓库（31 文件）——王语嫣实证存在
- `wiki/C:/` 路径 bug 目录（脚本盘符处理错误产物）——王语嫣实证存在
- inbox 950+ 篇 PARA 风格英文导入库（Handle the business 609 / Advanced modeling 116 / Manage projects 150…）从未消化
- 60_feedback/inbox-queue/ 135 份 dispatch 单只增不删

## 修改范围

1. **_tmp 处置**：统计后归档/删除（先 dry-run 列清单，老朱过目后执行）
2. **嵌套 git + C:/ 目录**：确认无价值内容后移除，并排查产生它们的脚本路径 bug（防复发）
3. **inbox PARA 库**：出处置建议（入库消化 / 归档 / 删除）——**内容处置决策归老朱**，本任务只出清单+建议
4. **inbox-queue/ dispatch 单**：加处理状态标记或归档已完成的

## 边界

- 删除类动作必须先清单后执行，老朱过目
- inbox PARA 库的内容价值判断不在本任务（如涉及入库另立生产任务）

## 验收标准

1. _tmp 清零或归档，磁盘占用对比留痕
2. 嵌套 git/C:/ 目录移除 + 路径 bug 脚本修复
3. PARA 库处置清单+建议落盘（决策另行）
4. dispatch 单状态收敛

## 交付

1. 清理报告 + 防复发修复
2. 送欧阳锋终审
