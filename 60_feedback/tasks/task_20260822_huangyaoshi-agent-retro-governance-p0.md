---
id: 418
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-22T12:20:09.127200+00:00'
---
# #418 agent复盘 治理 P0（T1-T3：归并+双轨合并+格式收口）

- **任务号**：#418
- **状态**：queued
- **assignee**：huangyaoshi（执行；王语嫣复核）
- **优先级**：P0（先治理再迁移——W4 迁移专案前置）
- **立项**：2026-08-22 王语嫣（风清扬审计 diag_20260822_fengqingyang-agent-retro-audit T1-T3，复核采纳）

## 内容价值判断（#375 处置门禁补充节，2026-08-22 黄药师领取时补）

- **处置对象已核实**：均为 agent复盘 历史产出（观察者 codex 12 文件/5 复盘、双轨助理目录、wangyuyan 旧格式复盘）——治理动作=**归并/归档/收口，不删除内容**（T1 内容不动只移文件、T2 留中文套五件套齐的、T3 归档不删除）
- **删除仅限空目录**（双轨合并后空目录）与明确废弃占位（codex 清零后 DEPRECATED 占位）——空目录无内容价值
- **处置依据**：王语嫣立项（风清扬审计 diag T1-T3 复核采纳，老朱会诊拍板 W4 迁移专案前置）
- **逐件老朱亲批**：本任务单即授权（会诊 P0 拍板）；执行报告附 before/after 目录对比供复核

## 范围（桌面 `agent复盘/`，治理对象）

- **T1 codex→fengqingyang 归并**：观察者历史产出（顶层 12 文件+daily-context 5 篇）移入 fengqingyang 目录（内容不动只移文件）；migration-staging 整体归档（迁移中台已完成，移出复盘区）
- **T2 中英功能助理双轨合并**：meeting-assistant→科学开会助理、sales-dialogue-assistant→销售对话参谋（留中文套，五件套齐的那套）；空目录删除
- **T3 复盘三轨收口**：wangyuyan 顶层散落 8 复盘文件+daily_cognitive_review（旧七节式）归档；只留 daily-context；huangyaoshi/daily-context 的 tmp-review.txt 移出；AI基本功教练 -v2 后缀文件改名合并

## 硬前置（E014）

**先出引用清单再动手**：grep 各角色 context 文件/启动恢复清单/脚本中对 `Desktop\agent复盘\` 及 `codex` 等旧路径的引用——改路径前全部登记，改后同步更新。

## 验收

- fengqingyang 目录含全部历史产出；codex 目录清零或 DEPRECATED 占位
- 每助理/每角色只剩一套目录、daily-context 单一格式
- 引用清单+更新记录附执行报告；commit 入档（agent复盘 非 git 仓——本单完成=文件系统事实+清单入 git 会诊目录）
- 欧阳锋终审抽"归并完整性"（无文件丢失，逐目录 before/after 对比）
