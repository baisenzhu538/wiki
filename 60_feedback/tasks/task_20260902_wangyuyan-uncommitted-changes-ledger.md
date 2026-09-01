---
id: task_20260902_wangyuyan-uncommitted-changes-ledger
title: 93 文件未提交改动落账（散点审计 R4，P0——为后续清理提供 git 兜底）
seq: 602
status: reviewed
assignee: wangyuyan
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-01T17:54:53.141385+00:00'
instance: wangyuyan-kimi-0902
evidence: 60_feedback/tasks/task_20260902_wangyuyan-uncommitted-changes-ledger.md
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A-
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

## 终审记录（欧阳锋，2026-09-02）

**等级**：A-（PASS）

**通过维度**（全部独立复跑）：
1. **三批 commit 在账可溯源**：批次1 `1692bae6b`（01:31:50，40 files）/ 批次2 `adb640f85`（01:32:09，26 files，todos/注册表/台账）/ 批次3 `9b4044061`（01:32:15，48 files，logs/pycache）——commit 信息含批次号+范围，逐条亲查 git log 在列。
2. **批次1 diff 抽查超标准**：执行报告称抽查 five-step/SKILL.md 仅 BOM 移除；终审者实际做了**全量 37/37 字节级断言**（`new == old[3:]` 且原文件以 EF BB BF 开头）——全部通过，零内容改动，与 #598 同源核验互证。
3. **落账范围核对**：批次2 26 文件确为 todos/注册表/留痕台账族；批次3 48 文件确为 logs/pycache 族（亲读 --stat）；三批合计 114 文件 ≥ 审计时点 93（期间持续在写，方向一致）。
4. **残余脏面判定**：当前 `git status` 已跟踪改动 7 项（role-registry.json / .derived-hashes.json / kimi-headless-launch.py / todos×2 / logs×2）——全部为 01:35 落账**之后**的在途活动面（#598/#600/#601 施工+时钟活体写入），不构成对落账时声明的反证；落账时「仅剩 role-registry+pyc 常态再脏」口径与活体文件性质吻合。
5. **边界合规**：path-scoped add、未跟踪文件未裹挟（当前 untracked=0 系后续 #601 等清理结果）、附带带入 core-plugins.json 已如实申报。

**🟡 记档（不阻断）**：批次1 commit 除 37 SKILL.md+INDEX/MOUNT 外还裹入 `scan_skills_registry.py` +143 行（#598 的 8 维扩展代码）——commit message 未提及该文件，落账批次与功能交付边界轻微混线；内容本身是正当交付物（已在 #598 终审核验），仅记档提示批次口径纪律。

**残余风险**：4c7284c97 误卷入 24 个 .obsidian 文件的处置待老朱裁定（已在「需要谁动作」正确上浮，非本单能解决）；本单提供的 git 兜底点已生效，#601/#603/#604 清理动作可安全回滚。
