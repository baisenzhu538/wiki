---
id: task_20260902_huangyaoshi-gate-suite-batch2
title: 门禁套件批2：git 大文件三层门禁（391MB zip 断 push 3 个月实证）+ complete 交付未入仓 WARNING（#622 打回实证）
seq: 625
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 老顽童建议书 diag_20260902_laowantong-large-file-git-gate + 欧阳锋建议书 prop_20260902_ouyangfeng-complete-gate-uncommitted-deliverables（09-03 王语嫣裁定并单）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T16:21:06.517909+00:00'
---

# #625 门禁套件批2（黄药师）

## 任务 1：git 大文件三层门禁（老顽童建议书，事故背景：391MB zip 断 push 3 个月、5826 commits 积压）

1. **.gitignore 规则扩展**（防新增）：inbox 压缩包/视频/采集大 json 白名单机制
2. **pre-commit 或 pre-submit 拦截**：git 跟踪文件 >100MB 硬拦、>15MB WARNING（现有 46MB mp4 族是增长中的雷）
3. **存量处置方案**：>15MB 在跟踪文件的清单+处置建议（漂移预警——只出清单和建议，不动文件，处置归王语嫣编排/老朱拍板）

## 任务 2：complete 交付未入仓 WARNING（欧阳锋建议书，#622 被打回实证：哨兵代码全在工作区没 commit）

`queue_transition.py complete` 对仓库内交付物路径加机械检查：涉及文件有未提交 diff/untracked → WARNING 打印+台账留痕（不拦截）。机器预审①可顺势补「已入仓」维度。

## 红线

- 任务 1 第三层只出清单不动文件
- 各项回归用例随附；门禁文案说人话（命中时告诉生产者怎么办）

## 交付

- 两任务 diff + 回归 + 存量大文件清单 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 625）

## 执行报告（2026-09-03 黄药师）

**交付物**：① `.gitignore` #625 规则块（第一层防新增：采集 mp4/itingnao 明细 json/压缩包族 + `!` 豁免注释白名单机制）② `kdo-tools/vault_git_backup.py` 第二层提交链路门禁（`gate_staged_large_files()`：>100MB 移出暂存硬拦 / >15MB WARNING + `90_control/large-file-gate.log` 台账）③ `kdo-tools/tests/test_vault_git_backup_gate.py`（5 测）④ `90_control/scripts/queue_transition.py` E040-loose 裸路径兜底（`_extract_deliverable_paths_loose` + `_log_gate_warning` + `90_control/gate-warning.log` 台账，WARNING 不拦截）⑤ `90_control/scripts/tests/test_complete_loose_deliverable_scan.py`（6 测）⑥ `90_control/large-file-inventory-20260903.md`（存量清单：17 文件 346.8MB，只出清单不动文件）⑦ 本任务单执行报告

**完成内容**：任务 1 三层——第一层 .gitignore 扩展（`10_raw/assets/wechat-collect/*.mp4`、`60_feedback/wechat-collect/**/*.mp4`、`10_raw/itingnao/details/*.json`、`*.zip/*.tar/*.tar.gz/*.7z`；gitignore 只管新增，已跟踪存量不受影响，豁免走 `!路径`+批准人注释）；第二层挂在 `vault_git_backup.py`（30min schtasks 全量 add -A 是 391MB zip 入仓的真实通道——拦这里=拦主风险面；>100MB 的处置=移出暂存其余照提，而非整单拒提——整单拒提会把备份打成停摆事故，08-26 停摆 6 天前科）；第三层存量清单 17 文件 346.8MB 全 <100MB 无即时风险，建议=不动存量（采纳老顽童建议书待裁定项 3 前者口径）。任务 2——E040 硬门禁已存在（#522）但反引号启发式漏裸路径（#622 FAIL 实证：交付物节路径无反引号 → vacuous 通过）；补 loose-scan 兜底：反引号识别为空时按 11 个已知顶层目录前缀扫裸路径，命中未入仓 → WARNING 打印 + gate-warning.log 台账（不拦截，欧阳锋建议书口径；与 gate-blocked.log 分流——那是探针第五信号扫描面，WARNING 混入会误通知王语嫣）

**验证**：① `git check-ignore -v` 实证：新 mp4/明细 json 命中 #625 规则行（57/59 行），00_inbox zip 仍被第 10 行拦，已跟踪 kdo_binary.zip 不受影响 ② 新测试 11 条全过（backup 门禁 5：硬拦移出暂存+工作区保留+台账 / WARNING 照提 / 小文件不动 / 端到端大文件被拦小变更照提 / 全拦不产生空 commit；loose-scan 6：#622 场景回放脏路径 WARNING / untracked WARNING / 干净不告警 / 幻觉路径不查 / 台账 task_9999_ 分流 / 反引号有产出时 loose 不启动）③ #622 真实任务单回放：backtick 提取=空、loose 命中 `kdo-tools/conveyor_probe.py`+`kdo-tools/tests/test_conveyor_probe.py`——若当时有本门禁，FAIL 前就会打印 WARNING ④ 回归：`90_control/scripts/tests/` 230 passed；`kdo-tools/tests/` 237 passed + 2 failed——2 失败经 pristine worktree（f26b422b9，本单改动前）复跑同样失败，为预存问题（infra 资产登记表缺 6 项 / queue_archive 跨月边界），与本单无关 ⑤ 真机 dry-run：当前暂存区门禁扫描返回空，scheduled backup 路径不受影响

**边界**：第一层 gitignore 不追溯存量（机制所限+红线）；第二层只覆盖 vault_git_backup 提交链路，agent 手工 `git commit` 不经过（.git/hooks 机器本地不入库，未装 pre-commit——如需全链路覆盖可另开单）；loose-scan 只认顶层目录前缀的仓内相对路径，无前缀裸文件名（如 matrix 行 27 登记写法 `notification-coverage-matrix.md`）仍漏——诚实口径=兜底非全覆盖；机器预审 pre_review ①「已入仓」维度未动（建议书为「可顺势」可选项，控制 diff）；2 个预存测试失败未修（超范围）；台账 gate-warning.log 不挂探针通知（WARNING 级，纯留痕）；施工期间 30min 定时备份将本单改动扫入 14419df03（混编 commit，diff 审查可按本报告交付物清单逐个核）

**需要谁动作**：欧阳锋终审（重点核：第二层挂 backup 链路而非 pre-commit 的选择、>100MB 处置=移出暂存而非整单拒提的判断、loose-scan WARNING 不拦截口径）；存量清单处置归王语嫣编排/老朱拍板（建议=不动）；2 个预存测试失败建议另开单
