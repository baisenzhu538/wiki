---
id: 471
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T11:26:56.734450+00:00'
version: v1.0
doc_id: D-20260823-019
instance: huangyaoshi
---
# #471 L1 全量采集投入运行最小闭环（常驻调度+体积红线）

- **任务号**：#471
- **状态**：queued（老朱已拍板常驻注册 2026-08-23——可开工）
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（风清扬审计实锤：建成✅投入运行⚠️半闭环——l1_capture.py 只在 #463 狗粮跑过一次，之后需手动）
- **立项**：2026-08-23 王语嫣（风清扬建议书 `diag_20260823_fengqingyang-l1-capture-scheduling.md` 采纳）

## 范围（风清扬建议 1+2）

1. **l1_capture.py 常驻调度**：计划任务 `kdo-l1-capture` 每 30 分钟（增量采集+trace+镜像+verify）；与 `kdo-conveyor-probe`（10min）错峰；失败可见（stderr+待收口记录，复用 #434 口径，禁静默吞）
2. **体积红线监控**：每次采集后记录 `D:\KDO-memory\L1-full\` 体积；超限告警并降频；告警走既有通道（conveyor_probe/飞书，禁新造扫描器）
3. **L3 活体验证**（建议 3，一次性可延后）：次日复盘抽查一个角色的 L1 全量原文回放「昨天做了什么」

## 验证（验证分层声明）

- L1 单测；L2 狗粮=手动触发一轮采集+体积记录；L3 待活体=次日回放抽查+调度自动跑 24h 零静默失败

## 边界

- 注册常驻计划任务以老朱拍板为前提（不拍板=本单挂起）；一次注册一次验收，不留「待确认漂移」

## 执行报告（2026-08-23 黄药师）

**完成内容**：L1 全量采集投入运行最小闭环——①`kdo-l1-capture` 计划任务注册（每 30 分钟 19:37 起，与 conveyor-probe 错峰）；②`kdo-l1-capture.cmd` 包装（增量采集+trace+镜像+verify 一条链，失败可见 #434 口径）；③体积红线监控（l1_capture.py 采集后注体积至 `90_control/l1-size.log`，超 5000MB 红线 → gate-blocked.log 机器自报，conveyor_probe 第五探针扫到即飞书通知王语嫣——复用既有通道，禁新造扫描器）。

**交付物**（改动文件清单）：
1. `kdo-tools/kdo-l1-capture.cmd`（新建）：常驻调度包装——capture + verify 一条链 + 失败写 pending-git-commits.log（纯 ASCII）
2. `kdo-tools/l1_capture.py`：`_log_size_and_alert()`（体积注 `90_control/l1-size.log` 追加 + 超限写 `90_control/gate-blocked.log` 机器自报）+ capture() 尾部挂钩
3. `kdo-tools/tests/test_l1_capture.py`（新建）：5 用例（体积计算/未超限仅注日志/超限 gate-blocked 自报/追加历史）
4. 计划任务：`kdo-l1-capture`（/SC MINUTE /MO 30 /ST 19:37，下次运行 2026-08-23 19:37 已验证）

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_l1_capture.py` → **5 passed**；kdo-tools 全量 → **52 passed**
- L2 狗粮：①手动触发 `kdo-l1-capture.cmd`——增量 41 新文件/跳过 7272/镜像同步 42/**verify PASS**（7315 文件一致 + 抽样 hash 全同）exit=0；②体积日志落盘（762.6 MB < 红线 5000，无告警=正常路径）；③计划任务 `schtasks /Query /TN kdo-l1-capture` 注册确认（19:37:00 下次运行）
- L3 待活体：①计划任务自动跑 24h 零静默失败（次日验）；②次日复盘抽查一角色 L1 全量原文回放「昨天做了什么」（建议 3，一次性可延后）；③体积超限告警真实触发（当前 762MB 距红线 6.5 倍，短期内不会触发——机制由单测覆盖）

**未做项**：
- 降频自动化未做——超限告警提示人工降频（任务书口径"超限告警并降频"，最小闭环=告警先行，降频由人裁定频率）
- 建议 3 L3 活体验证（次日回放抽查）——本单声明为待活体，次日执行

**需要谁动作**：
- 欧阳锋：终审本单（抽「计划任务注册/capture+verify 链路/体积红线正反用例」）
- 老朱：L3 次日回放抽查时配合（可选）
