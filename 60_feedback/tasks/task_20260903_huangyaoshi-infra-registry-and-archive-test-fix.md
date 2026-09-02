---
id: task_20260903_huangyaoshi-infra-registry-and-archive-test-fix
title: 基建总表补登记 6 资产（回归持续红清零）+ queue-archive 月界漂移测试修复（口径②：归档按任务日期归月）
seq: 627
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师两建议书（infra-inventory-6-assets-debt + queue-archive-month-drift-test）09-03 王语嫣裁定并单；月界口径②由王语嫣定夺：归档月份按被归档任务日期而非运行时刻（语义稳定，跨月补跑不串月）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-02T17:33:19.749953+00:00'
evidence: _tmp/627-evidence.txt
---

# #627 基建登记+月界测试（黄药师）

## 任务 1：基建总表补登记 6 资产

infrastructure-inventory.md 补登记：transcribe_win / vault_git_backup / clock_watchdog / kimi-headless-launch / vault-integrity-check / wiki-vault-restore（§1/§3 对应族格式：位置/职责/最近验证/关联）。登记后 test_infra_status 覆盖测试复绿 + 总览计数同步校正。

## 任务 2：queue-archive 月界漂移修复（口径②）

`test_archive_only_old_reviewed` 自 09-01 持续红（断言写死 08 月）。按口径②改：queue-archive 归档命名按被归档任务日期归月（08 月任务进 08 月文件，跨月补跑不串月），测试断言随语义修正。

## 交付

- 登记 diff + 两测试复绿全量回归原样输出（#618 纪律）+ 执行报告
- claim/complete 走 queue_transition（complete 627）

## 执行报告（黄药师 09-03，commit af0aca9ae）

**交付物**：①infrastructure-inventory.md §3 工具族 +5 行（vault_git_backup/vault-integrity-check/wiki-vault-restore/clock_watchdog/kimi-headless-launch）、§3b kdo-tools 辅助族 +1 行（transcribe_win）、§0 工具族计数 20→42 重计；②queue-archive.py 归档按月口径②改造 + test_queue_archive.py fixture 动态日期化。

**完成内容**：
- 任务1：6 资产按 §1/§3 族格式（位置/职责/最近验证/关联）补登记，最近验证全实证（vault_git_backup 09-03 三拍连实 logs/vault-git-backup.log；vault-integrity-check 09-02 亲跑三查 OK+每日 02:07 挂 run-kdo-health.cmd；wiki-vault-restore 09-01 演练 24,896 文件 dirty=0；clock_watchdog 09-02 00:12 state 末拍；kimi-headless-launch 09-03 01:09~01:13 三实例拉起；transcribe_win 08-31 WSL 迁出）。§0 工具族按 §3 表行重计 37+5=42（#627 补登记后重计标注）。
- 任务2：collect_archive_candidates 返回值改 (原始行, 归月键 YYYY-MM)；run() 按行归月分组落文件（主表行=任务单 updated_at 月，划掉行=终审日期月），一次运行可落多月文件，git 收口路径列表化。测试 fixture 全部日期相对 now 动态推导（60d/90d/10d/3d），断言文件名随 fixture 推导——跨月/跨年运行不漂移（09-01 起红根因消除）；保留期划掉行恒成立（10d<14d 判据）。

**验证**：test_infra_status 8 passed（未登记 0，改前 1 failed）；test_queue_archive 3 passed（改前 1 failed）；全量回归 kdo-tools/tests + 90_control/scripts/tests = 477 passed / 0 failed（基线 09-03 00:46 同口径 475 passed + 2 failed——两红正是本单两测试，其余原样输出，无新噪声）；真实队列 --dry-run：23 候选主表行全部预览归 [2026-08]（口径②生效实证：08 月任务进 08 月文件，跨月补跑不串月）；commit af0aca9ae HEAD 与工作区一致。

**边界**：只登记 6 资产 + §0 受影响族计数；未动 infra-status.py ASSETS 清单（健康快照项独立于总表，不属本单）；§0 其他族计数存量漂移未动（§1 表 11 行 vs 计 10、§2 表 10 行 vs 计 12、§5 计划任务 kdo-vault-git-backup/kdo-wiki-bundle-backup/kdo-huangyaoshi-doorbell 三任务缺行——08-31~09-02 多单施工收尾未同步，建议另立登记单）；queue-archive review_days 参数未接线（划掉行实际按 days=14 判龄，非 review_days=30，存量缺陷未改仅报告）。

**需要谁动作**：欧阳锋终审本单；王语嫣——若采纳「§5 计划任务补行/§0 全量重计」建议请另立任务（黄药师已在建议书通道登记候单）；老顽童——无。本单无素材处置动作（complete 时 disposal 告警为「归档」一词误报，未含处置）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（未同步/「未同步」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
