---
id: task_20260902_huangyaoshi-instance-naming-role-only
title: 实例命名铁律落地：拉起器/状态机实例名去工具后缀（{role}-kimi → {role}），兼容在途旧名
seq: 620
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 直令铁律：实例命名只有角色名没有工具名（工具可换，工具名进实例名=制造混乱）
reviewer: 欧阳锋
instance: huangyaoshi
matrix_exempt: true
# §3.19 矩阵豁免理由：#620 纯重构——实例锁匹配裸名口径/claim 门禁，无新信号、无通道、无门禁语义变更（#537 口径）
code_files:
  - 90_control/scripts/queue_transition.py
  - 90_control/scripts/kimi-headless-launch.py
  - 90_control/scripts/tests/test_queue_transition.py
  - 90_control/scripts/tests/test_reviewer_flip_616.py
updated_at: '2026-09-02T16:46:43.994130+00:00'
---

# #620 实例命名去工具后缀（黄药师）

## 背景

老朱 09-02 直令：双实例/拉起实例命名**只有角色名**，禁带工具后缀（laowantong-kimi → laowantong）。理由：工具可换（kimi 没额度会换其他 agent 干活），工具名进实例名制造不必要混乱。

实证现状：`kimi-headless-launch.py` L45 prompt 模板写死 `--instance {role}-kimi`；队列里已有 claimed-huangyaoshi-kimi（#619 在途）等旧名。

## 任务

1. `90_control/scripts/kimi-headless-launch.py`：实例名改 `{role}`（工具仍走 TOOLS 路由表，工具是变量不进名字）
2. `queue_transition.py` 实例锁匹配兼容：过渡期接受 `{role}` 精确匹配 + `{role}-<tool>` 旧名尾缀（在途单如 #619 claimed-huangyaoshi-kimi 须能 complete）；新 claim 一律裸角色名
3. `#616` 翻转通道里「查 wangyuyan 登记实例」的逻辑同步裸名口径
4. active-instances.json / liveness 登记面如有工具后缀写入，一并改

## 红线

- 过渡期兼容不清历史数据（队列里旧名行不改写）
- 回归：旧名 complete 能过 + 新名 claim/complete 全流程走通

## 交付

- diff + 回归实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 620）

## 执行报告（2026-09-03 黄药师）

**交付物**：4 文件改动（见 frontmatter code_files）+ 任务单本报告；diff 见下节。
**完成内容**：
1. `kimi-headless-launch.py` PROMPT 纪律行：`--instance {role}-kimi` → `--instance {role}`（工具仍走 TOOLS 路由表，工具=变量不进实例名；日志名 headless-{role}-{ts} 原即裸角色名）
2. `queue_transition.py` 新增 `_claimed_by_role()`：实例锁匹配=裸角色名精确 + 同角色在途旧名 `{role}-<tool>` 尾缀（含 `-0902` 日期变体）；complete（预检+锁内重检两处）与 release 三处统一接入
3. `queue_transition.py` action_claim 顶部新增裸名门禁 `_legacy_dash_ok()`：带 `-` 的新名拒止（提示 register 或 --force 留痕）；在册存量旧名（在途身份自然消亡）+ INSTANCE_ROLE_MAP 历史键（hermes）放行——含 `-` 的正式角色 skills-assistant 在册不受影响
4. `_check_review_authority()`（#616 翻转通道）角色比对同步裸名口径：在册旧身份 `wangyuyan-kimi-0902` 按同角色登记计，防王语嫣翻转通道被旧名登记卡死
5. 登记面核查：claim/register 是唯一写入 .kdo/active-instances.json 的路径，claim 裸名门禁即写面封口；conveyor_probe 只读消费无写后缀；role_clock 不写队列实例名
**验证**：90_control/scripts/tests 全量 **238 passed**（含新增 7 用例：匹配矩阵/裸名门禁拒止/在册旧名放行/force 留痕/裸名收口旧名 complete/异角色拒绝/裸名释放旧名）；kdo-tools/tests 237 passed + 2 失败——**2 失败经 git stash 隔离实证为本单无关的存量债务**（infra_status 覆盖门禁 6 资产未登记 + queue_archive 月界漂移），红线内嵌于 7 用例（旧名 complete 能过+新名 claim/complete 全流程）
**边界**：①存量队列行/登记表历史旧名不回改（红线，在途自然消亡）②in-flight 旧名实例（如 #625 huangyaoshi-kimi）claim 新单仍允许（在册身份）——其 claim 写出的仍是旧名，待全部消亡后新名唯一 ③真实队列仅验证裸名 claim 路径（本次双单 huangyaoshi 领取实证）；旧名收口走单测覆盖
**需要谁动作**：欧阳锋终审 #620；王语嫣——另发现 6 资产（transcribe_win/vault_git_backup/clock_watchdog/kimi-headless-launch/vault-integrity-check/wiki-vault-restore）未登记 infrastructure-inventory.md 致 infra_status 覆盖测试持续红（#488 存量债务，friction-log 09-03 已记），待裁定登记归属或立项

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
