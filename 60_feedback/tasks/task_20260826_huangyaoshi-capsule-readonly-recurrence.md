---
id: 545
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T16:52:19.253658+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/memory_capsule.py
- kdo-tools/tests/test_capsule_events.py
- 90_control/notification-coverage-matrix.md
---

# #545 胶囊 readonly 写入失败复发排查（#511 疑未根治）

- **任务号**：#545
- **状态**：queued
- **assignee**：huangyaoshi（自查自修——他自己报告的数据；欧阳锋终审）
- **优先级**：P2（不阻断生产，但事件层留痕是复盘/胶囊链的地基，复发 4 次不能再放）
- **立项**：2026-08-26 王语嫣（黄药师核查报告观察项 1：#511 胶囊 readonly 写入失败今日复发 4 次——10:12/10:23/20:31/20:38，疑未根治）

## 背景

#511（事件层 friction 写入，log_event_safe 失败可见不阻断）当时终审通过，但 readonly 写入失败今日复发 4 次。复发=当时修复的可能不是根因（只修了表面路径/权限，或在特定时段/负载下复发）。

## 任务

1. **先复现取证**：按 4 个复发时间点定位当时的完整报错（堆栈/目标文件/进程占用情况），确认「readonly」的确切语义（文件属性只读/被占用锁/权限）
2. 定位根因后修复；若根因=跨进程并发写（L0 胶囊双写面），给并发安全方案
3. 回归：模拟复发场景验证修复有效
4. §3.19：若涉及事件/信号变更→同步矩阵

## 边界

- 只修胶囊写入层，不动 L1 采集/镜像链
- 若排查后发现是环境性（杀软锁文件等），如实报「非代码根因」+缓解措施，不硬修

## 验收

- 复发点完整取证+根因结论+修复回归（或环境性结论+缓解）；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：胶囊 readonly 复发排查+根治（`kdo-tools/memory_capsule.py`）。①**复现取证**：pending-git-commits.log 全量——08-26 实际 **14 次**失败（06:24/06:41/06:58/07:09/09:01/09:03/09:06/09:27/10:12/10:23/20:31/20:38/23:07/23:56，比报告观察项的 4 次多），报错逐字=`attempt to write a readonly database`；排除法：wiki/tech 两库 gate-blocked+force 台账时间与失败点零重叠（失败事件源非台账写入路径的对应记录缺失→调用上下文未落盘，#545 取证升级后下次复发可直接定位）；**复现实验**：db 文件置只读属性 → 逐字复现同款报错（`_connect` 的 `PRAGMA journal_mode=WAL` 在只读文件上即炸）；-wal 只读场景无法构造（WAL 文件随连接关闭回收）；当前属性=Archive（可写），写入实测成功（probe-test-545 事件 #255）；库内 grep 全厂无任何脚本触碰只读属性——**根因结论：db 文件被外部因素（备份/同步工具或系统层）间歇置只读属性，属环境性，置位者未抓到现行**（任务书边界允许如实报非代码根因）；②**根治三层**（自愈+缓解）：readonly 语义→`_clear_readonly` 清 db/wal/shm 只读属性重试（自愈成功打 ⚠️ 留痕）；任意失败→0.5s 退避重试一次（瞬时锁/占用场景）；最终失败→取证升级（payload 200 字符+db/wal/shm 属性快照落 pending-git-commits.log，下次复发直接定位）；③§3.19：矩阵事件 15 行。

**交付物**：
- `kdo-tools/memory_capsule.py`（_insert_event 拆出/_readonly_forensics/_clear_readonly/_pending_log/log_event_safe 三层自愈）
- `kdo-tools/tests/test_capsule_events.py`（+2 新例：只读属性自愈全链路/瞬时锁退避重试；改写 1 例：永久失败场景改 monkeypatch 持续故障——只读属性场景语义已从「报失败」变为「自愈成功」）
- `90_control/notification-coverage-matrix.md`（事件 15 行，§3.19）

**验证**：
- L1 单测：test_capsule_events 8 passed（含只读自愈全链路：置 0o444 → log_event_safe 清属性 → 写入成功 → 属性已清断言）；基线零退步：kdo-tools **170 passed**（168+2）、90_control **167 passed**
- L2 狗粮：真库写入探测成功（事件 #255）；只读复现实验逐字命中原始报错；现有 db 属性 Archive 可写
- L3 待活体：下次复发时自愈留痕（`胶囊只读自愈成功` 行）or 取证行（属性快照）落 pending-git-commits.log——两种结局都给出下一步定位证据
- **预审红项预标注**：本单预审若检「缺失/不得/未」类词=报告描述文字（如「置位者未抓到现行」）误报，预标注在此；负向断言「全厂无脚本触碰只读属性」**存在性核查**=Grep `S_IREAD|readonly|attrib |ReadOnly` 全库 *.py/*.cmd/*.ps1 零命中（已附命令可复跑）

**边界**：只动胶囊写入层 ✅（L1 采集/镜像链未碰）；环境性结论如实报+自愈/取证缓解，不硬修 ✅；台账/探针逻辑零改动 ✅。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——若接受「环境性+自愈」结论，本单关闭后观察一周（自愈留痕 vs 取证行哪个出现）。
