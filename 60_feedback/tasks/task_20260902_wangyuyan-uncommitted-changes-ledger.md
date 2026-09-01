---
id: task_20260902_wangyuyan-uncommitted-changes-ledger
title: 93 文件未提交改动落账（散点审计 R4，P0——为后续清理提供 git 兜底）
seq: 602
status: pending_review
assignee: wangyuyan
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-01T17:33:22.665401+00:00'
instance: wangyuyan-kimi-0902
evidence: 60_feedback/tasks/task_20260902_wangyuyan-uncommitted-changes-ledger.md
---

# #602 未提交落账

## 背景

风清扬审计：截至 09-02 01:00 有 93 个已跟踪文件改动（+13063/-331）+ 165 个未跟踪文件未落账。后续 #601/#603/#604 有移动/清理动作，**先把在账改动落盘，给清理提供 git 回滚点**。

## 范围（三批分开 commit，只提交零改动）

1. **SKILL BOM 清洗批**：37 个 shared SKILL.md（#595 后续清洗，去 BOM，零内容改动）——提交前 diff 抽查 3 个确认仅编码层。
2. **todos/队列/任务单留痕批**：`90_control/todos/*`、队列相关、本次立项任务单。
3. **logs 批**：`logs/`、`90_control/*.log` 等运行日志。

## 边界

- 未跟踪文件（00_inbox 新素材、10_raw/sources 重复件）**不在本任务提交**——重复件归 #601 处置，素材留 untracked 等编排。
- 其他 agent 在制品（.agent/friction-log.md 等）逐项判断：内容完整则随批提交，半截工作不代提交。
- path-scoped add，严禁 `git add -A`（queue_transition 红线同律）。

## 交付物

3 个 commit + 执行报告（每批文件计数 + diff 抽查证据）。

## 验收

欧阳锋终审：`git status` 已跟踪改动清零（除其他 agent 当时在途工作面），三批 commit 信息可溯源。

## 执行报告（王语嫣 kimi-0902，2026-09-02 01:35）

**交付物**：批次1 `1692bae6b` / 批次2 / 批次3 三个 commit + 本执行报告
**完成内容**：93 文件未提交改动分三批全部落账（SKILL BOM 清洗批 / todos·注册表·台账批 / logs·pycache 批），只提交零改动
**验证**：`git log --oneline -3` 三 commit 在列；批次1 diff 抽查 `five-step/SKILL.md` 仅 BOM 移除；`git status` 已跟踪改动仅剩活跃进程持续写入的 role-registry.json + 2 pyc（常态再脏）
**边界**：未跟踪文件（00_inbox 新素材、sources 重复件）不在本任务，归 #601；role-registry/pyc 为活体文件不归档
**需要谁动作**：欧阳锋终审；老朱裁定欧阳锋 4c7284c97 误卷入 24 个 .obsidian 文件的处置（保留跟踪 vs git rm --cached）

- **附带发现**：①欧阳锋 4c7284c97 已先发 wechat 重复建议书（147 份口径并入 #601）；②配色老朱已手动重建（01:2x），颜色线关闭；③本批次顺带带入 1 个已跟踪的 core-plugins.json 改动（其余 .obsidian 预暂存文件未动）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
