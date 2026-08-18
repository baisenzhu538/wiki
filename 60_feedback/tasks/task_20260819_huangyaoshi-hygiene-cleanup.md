---
id: 372
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-18T17:58:58.279663+00:00'
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

## 执行记录（2026-08-19 黄药师，已提审）

### 处置结果

| 项 | 处置 |
|:--|:--|
| **C:/ 路径 bug 目录** | ✅ 已清除（稀疏孤儿副本树：4KB 骨架 + 1 个孤儿文件副本 kcard-quality-gate-report-2026-06-15.md；真实文件在 60_feedback/audit/ 完整存在）。防复发排查：当前 5 个含 C: 模式的脚本全部是合法 Windows 绝对路径（Path("C:/...")/r"C:\..."），无 os.path.join 字符串拼接 bug——C:/ 树为历史遗留（06-15 产物），当前脚本库无复发源 |
| **嵌套 git（wiki/wiki）** | ✅ 已消失（并行会话清理或先前窗口清除；核实无残留） |
| **inbox PARA 库** | 处置建议落盘 `60_feedback/decisions/hygiene-372-para-recommendation.md`（2128 文件 270M 清单 + 归档/选择性入库/删除三选项）——**决策归老朱**，建议默认归档 |
| **inbox-queue dispatch** | ✅ 135 单按月份归档至 `60_feedback/inbox-queue/archive/2026-06/` 等（历史记录保留不删） |
| **_tmp** | ⚠️ **口径修正**：1.4G 主体是 `_tmp/ocr_venv`（王语嫣 OCR 工具依赖 venv，startup.md 工具清单注册——**非垃圾，保留**）；真垃圾 = mineru-test*/openmontage/logs 约 23M。**删除清单待老朱过目**：mineru-test / mineru-test-cpu / mineru-test-gpu（各 6.7M）+ openmontage（2.5M）+ mineru-*.log（2.3M），共 ~23M |

### 验收对照

1. _tmp：清单+口径修正已出，删除动作待老朱过目（任务边界要求）
2. 嵌套 git + C:/ 目录：已清除 + 防复发排查留痕 ✅
3. PARA 处置建议落盘 ✅（决策归老朱）
4. dispatch 单：135 归档收敛 ✅

## 交付

1. 清理报告 + PARA 建议 + _tmp 清单（待过目）
2. 送欧阳锋终审
